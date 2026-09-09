from rich.console import Console
from rich.table import Table

from .models import DayPlan


def render_day(day_plan: DayPlan | None, console: Console) -> None:
    if day_plan is None:
        console.print("[yellow]No lunch today — the mensa is closed on Sundays.[/yellow]")
        return

    lunch_items = day_plan.lunch_items
    if not lunch_items:
        console.print(f"[yellow]No lunch items found for {day_plan.label}.[/yellow]")
        return

    table = Table(title=day_plan.label, show_lines=True)
    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Dish")
    table.add_column("Price (students)", justify="right")
    table.add_column("Rating", justify="right")
    table.add_column("Tags", style="green")

    for item in lunch_items:
        table.add_row(
            item.category,
            "\n".join(item.dish_lines),
            item.price_student or "-",
            item.rating or "-",
            ", ".join(item.dietary_tags),
        )

    console.print(table)
