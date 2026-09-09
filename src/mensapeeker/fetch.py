"""Fetching raw mensa plan HTML from swfr.de.

The site renders the whole current week (Mon-Sat) server-side into one page;
client-side JS only toggles which day tab is visible. So a plain GET of the
location page already contains every day's plan and no query parameters are
needed to reach "today".
"""

import requests

USER_AGENT = "mensapeeker/0.1 (personal terminal mensa viewer)"
TIMEOUT_SECONDS = 10.0


def fetch_week_html(url: str) -> str:
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.text
