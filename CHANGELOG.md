# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.4.0] - 2026-09-23

### Added
- Session details panel: tap ⓘ on a session to see posters, times, venue, sections, every film with its directors and a link to its film page, the session's warnings, and a Mark / Unmark button. It opens as a bottom sheet on phones.
- Sync: share your plan (marked sessions, hidden venues and edited walk times) as a link or a code, and import it on another device. The import shows what it will replace before it applies.
- Now line: a red line marks the current time on today's grid, and the app opens on today, scrolled to it.
- Next bar: shows the session you are in and your next marked session, when it starts and when to leave to walk there. Tap it to jump to that session.
- `?now=YYYY-MM-DDTHH:MM` in the URL simulates a time, to try the festival-day features early.

### Changed
- The ⓘ details button replaces the ↗ film-page link on each session; the film pages are linked from the details panel.
- The offline service worker only runs over HTTPS, so local testing always shows the latest files.

### Fixed
- An empty white bar no longer appears under the summary line.
- A hovered session no longer covers the venue headers or the time axis.

## [1.3.0] - 2026-09-23

### Added
- `data/fetch.py` downloads the programme, skipping pages whose version is unchanged, so the repo can be rebuilt and the programme updated.
- README with the update steps.

### Changed
- Updated posters for Hungry and Split Rock from the latest programme data.

## [1.2.0] - 2026-09-23

### Added
- Warning when the same film is marked in more than one session, including films inside multi-film sessions such as marathons and galas.

## [1.1.0] - 2026-09-23

### Changed
- Compact phone layout: day tabs on top, one line of controls and one line of summary, short venue names in the column headers.

## [1.0.0] - 2026-09-23

### Added
- Day-by-day grid with one column per venue, with session blocks sized by duration, including sessions that run past midnight.
- Mark sessions, and show only marked sessions.
- Warnings for overlapping sessions and for venue changes shorter than the walk time.
- Walk times between each pair of venues, with editable defaults.
- Hide venues you will not go to; hidden venues are remembered.
- Multi-film sessions list each film and its directors.
- Sitges Film Festival colours and fonts.
- Installable on Android as an app (PWA), with offline support.

[Unreleased]: https://github.com/dbeltra/sitges-planner/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/dbeltra/sitges-planner/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/dbeltra/sitges-planner/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/dbeltra/sitges-planner/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/dbeltra/sitges-planner/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/dbeltra/sitges-planner/releases/tag/v1.0.0
