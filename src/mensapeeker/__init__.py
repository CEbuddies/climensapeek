import argparse
import sys
from datetime import date

import requests
from rich.console import Console

from .fetch import fetch_week_html
from .locations import DEFAULT_LOCATION, LOCATIONS
from .parse import parse_week, tab_id_for_weekday
from .render import render_day


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="mensapeeker", description="Show today's Uni Freiburg mensa lunch plan."
    )
    parser.add_argument(
        "--location", choices=sorted(LOCATIONS), default=DEFAULT_LOCATION
    )
    args = parser.parse_args()

    console = Console()
    url = LOCATIONS[args.location]

    try:
        html = fetch_week_html(url)
    except requests.RequestException as exc:
        console.print(f"[red]Could not reach the mensa website: {exc}[/red]")
        sys.exit(1)

    week = parse_week(html)
    tab_id = tab_id_for_weekday(date.today().weekday())
    day_plan = week.get(tab_id) if tab_id else None

    render_day(day_plan, console)
