from dataclasses import dataclass, field

DINNER_PREFIX = "Abendessen"


@dataclass
class MenuItem:
    category: str
    dish_lines: list[str]
    price_student: str | None = None
    dietary_tags: list[str] = field(default_factory=list)

    @property
    def is_lunch(self) -> bool:
        return not self.category.startswith(DINNER_PREFIX)


@dataclass
class DayPlan:
    tab_id: str
    label: str
    items: list[MenuItem]

    @property
    def lunch_items(self) -> list[MenuItem]:
        return [item for item in self.items if item.is_lunch]
