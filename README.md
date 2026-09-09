# Mensa Peeker

Shows today's lunch plan for a University of Freiburg mensa in the terminal.

## Install

```
uv tool install .
```

Installs a `mensapeeker` command onto your PATH (via `~/.local/bin`), so it's independent of this checkout's `.venv` afterwards. Re-run the same command to pick up code changes, or use `--editable .` instead to have it track the source in place.

## Usage

```
mensapeeker
mensapeeker --location institutsviertel
```

Without installing, `uv run mensapeeker` works the same from inside this checkout.

## Development

```
uv sync
uv run pytest
```

See `plan.md` for scope notes.
