"""Known mensa locations and their full plan URLs on swfr.de.

Full URLs (not a shared base + slug) because the widget doesn't always live
at the same path for every location: most locations embed it on the English
page (/en/food/mensa-cafeterias-menus/freiburg/{slug}), but Rempartstraße's
English page is missing it — only the German page
(/essen/mensen-cafes-speiseplaene/freiburg/{slug}) has it, as of 2026-09.

Verify a new/changed location by fetching its URL and checking for a
`menu-tagesplan` element before adding or trusting it here.
"""

_EN = "https://www.swfr.de/en/food/mensa-cafeterias-menus/freiburg/{slug}"
_DE = "https://www.swfr.de/essen/mensen-cafes-speiseplaene/freiburg/{slug}"

LOCATIONS: dict[str, str] = {
    "rempartstrasse": _DE.format(slug="mensa-rempartstrasse"),
    "institutsviertel": _EN.format(slug="mensa-institutsviertel"),
    "littenweiler": _EN.format(slug="mensa-littenweiler"),
    "flugplatz": _EN.format(slug="mensa-flugplatz-und-cafe-flugplatz"),
    "musikantine": _EN.format(slug="musikantine"),
    "haus-zur-lieben-hand": _EN.format(slug="haus-zur-lieben-hand"),
    "ausgabestelle-eh-freiburg": _EN.format(slug="ausgabestelle-eh-freiburg"),
}

DEFAULT_LOCATION = "rempartstrasse"
