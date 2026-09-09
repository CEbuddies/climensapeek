from bs4 import BeautifulSoup

from .models import DayPlan, MenuItem

# date.weekday(): Monday=0 ... Saturday=5, Sunday=6 (mensa is closed, no tab).
WEEKDAY_TAB_IDS = ["tab-mon", "tab-tue", "tab-wed", "tab-thu", "tab-fri", "tab-sat"]


def tab_id_for_weekday(weekday: int) -> str | None:
    if weekday >= len(WEEKDAY_TAB_IDS):
        return None
    return WEEKDAY_TAB_IDS[weekday]


def parse_week(html: str) -> dict[str, DayPlan]:
    soup = BeautifulSoup(html, "lxml")
    return {
        str(tab["id"]): _parse_day(tab)
        for tab in soup.find_all("div", class_="menu-tagesplan")
        if tab.get("id")
    }


def _parse_day(tab) -> DayPlan:
    tab_id = str(tab["id"])
    heading = tab.find("h3")
    label = heading.get_text(strip=True) if heading else tab_id
    items = [_parse_item(h5) for h5 in tab.find_all("h5")]
    return DayPlan(tab_id=tab_id, label=label, items=[item for item in items if item])


def _parse_item(h5) -> MenuItem | None:
    card = h5.find_parent("div", class_="bg-lighter-cyan")
    if card is None:
        return None

    category = "".join(h5.find_all(string=True, recursive=False)).strip()

    dish_el = card.find("small", class_="extra-text")
    dish_lines = (
        [line.strip() for line in dish_el.get_text(separator="\n").split("\n") if line.strip()]
        if dish_el
        else []
    )

    price_label = card.find("dt", class_="price-studierende")
    price_value = price_label.find_next_sibling("dd") if price_label else None
    price_student = price_value.get_text(strip=True) if price_value else None

    dietary_tags = [
        img["data-x-tooltip"]
        for img in card.find_all("img", attrs={"data-x-tooltip": True})
        if img["data-x-tooltip"] != "Bewertung"
    ]

    rating_el = card.find("a", class_="rating")
    rating = rating_el.get_text(strip=True) if rating_el else None

    return MenuItem(
        category=category,
        dish_lines=dish_lines,
        price_student=price_student,
        dietary_tags=dietary_tags,
        rating=rating,
    )
