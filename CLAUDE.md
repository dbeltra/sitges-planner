# Sitges 2026 Planner

Static PWA: a day-by-venue grid of the Sitges Film Festival programme. No build step, no dependencies.
Hosted on GitHub Pages from `main`: https://dbeltra.github.io/sitges-planner/

## Layout

- `index.html` — the whole app (CSS, markup and JS in one file).
- `sw.js` — offline service worker (cache first, refreshes in the background).
- `data/schedule.js` — generated programme (`SCHEDULE`), loaded by `index.html`. Do not edit by hand.
- `data/*.py` — scripts that download and build the programme (see README). The raw downloads
  (`data/*.json`, `data/pages/`, `data/films/`, `data/film-pages/`) are gitignored and never published.
- `CHANGELOG.md` — Keep a Changelog format, semver.

## Publishing a new build

Every change that ships:

1. Bump `BUILD` in `index.html` (semver, shown at the bottom of Settings).
2. Bump `VERSION` in `sw.js` (`sitges26-vN` → `vN+1`) so installed apps drop the old cache.
3. Add a `## [x.y.z] - YYYY-MM-DD` entry to `CHANGELOG.md`, written in plain words for the app's users.
4. Commit and push to `main`. GitHub Pages serves it; installed apps update the next time they open.

Commits use this repo's local git identity (`dbeltra@gmail.com`), not the global work one.

## Texts

All UI strings are in the `STR` object in `index.html`, with `ca` (default) and `en`. Change both languages
together, and keep a label and the title of the window it opens the same (e.g. Catalan "Ajustos").
Plural entries use `Intl.PluralRules`; some Catalan entries are functions for grammar (`caDe`, `caAt`).

## Conventions

- Persistent state goes through `store` (localStorage, keys prefixed `sitges26:`).
- A session starting before 06:00 belongs to the previous festival day (`DAY_START_HOUR`).
- `?now=2026-10-10T18:00` fakes the current time, for testing the "now" line and the day tabs.
- Keep it simple: no frameworks, no dependencies. Deliberate shortcuts are marked with `ponytail:` comments.

## Run locally

`python3 -m http.server 8000` from the repo root (the service worker needs http, not `file://`).
