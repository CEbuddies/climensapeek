from pathlib import Path

from mensapeeker.parse import parse_week, tab_id_for_weekday

FIXTURES = Path(__file__).parent / "fixtures"
FIXTURE = FIXTURES / "institutsviertel_week.html"


def load_week(fixture: Path = FIXTURE):
    return parse_week(fixture.read_text(encoding="utf-8"))


def test_parses_all_six_days():
    week = load_week()
    assert set(week) == {
        "tab-mon", "tab-tue", "tab-wed", "tab-thu", "tab-fri", "tab-sat",
    }


def test_monday_lunch_excludes_dinner():
    week = load_week()
    monday = week["tab-mon"]

    categories = [item.category for item in monday.items]
    assert "Abendessen 1" in categories  # fixture does contain dinner entries

    lunch_categories = [item.category for item in monday.lunch_items]
    assert all(not c.startswith("Abendessen") for c in lunch_categories)
    assert "Schneller Teller" in lunch_categories


def test_item_fields_parsed():
    week = load_week()
    schneller_teller = next(
        item for item in week["tab-mon"].items if item.category == "Schneller Teller"
    )
    assert schneller_teller.dish_lines == ["Aglio Spaghetti with Sun-dried Tomatoes"]
    assert schneller_teller.price_student == "2,50 €"
    assert "pflanzlich" in schneller_teller.dietary_tags
    assert schneller_teller.rating == "4,0"


def test_item_without_rating_is_none():
    week = load_week()
    schneller_teller_wed = next(
        item for item in week["tab-wed"].items if item.category == "Schneller Teller"
    )
    assert schneller_teller_wed.rating is None


def test_tab_id_for_weekday_monday_to_saturday():
    assert tab_id_for_weekday(0) == "tab-mon"
    assert tab_id_for_weekday(5) == "tab-sat"


def test_tab_id_for_weekday_sunday_is_none():
    assert tab_id_for_weekday(6) is None


def test_rempartstrasse_fixture_has_lunch_only_categories():
    week = load_week(FIXTURES / "rempartstrasse_week.html")
    monday = week["tab-mon"]

    assert monday.items, "expected at least one dish for Monday"
    assert monday.lunch_items == monday.items
    assert {item.category for item in monday.items} == {
        "Schneller Teller", "Essen 1", "Essen 2", "Essen 3", "Wochenangebot",
    }
