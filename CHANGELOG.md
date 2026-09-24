# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.1] - 2026-09-24

### Changed
- A session's details now show each film the same way as in Pel·lícules, with its other screenings, so when two sessions clash you can see right away when else a film plays.
- On phones, a faded edge shows when there are more days or venues to scroll to, and the selected day always scrolls into view.
- Ajustos is tidier: the language is at the bottom, "Restableix" sits next to the walk times it resets, and the tip is no longer repeated there.

### Fixed
- Turning on "Només les meves sessions" no longer shifts the schedule and misaligns the sessions.
- On narrow phones, each walk time in Ajustos is on one line again: the two venues on the left, the minutes on the right.

## [2.0.0] - 2026-09-24

### Added
- The app now has three sections: Programa (the schedule), Pel·lícules and El meu pla. On phones they sit in a bar at the bottom of the screen, with an icon for each, and each section slides in when you switch.
- El meu pla lists all your marked sessions day by day, with their warnings. Tap one to see its details, or jump to that day in the schedule.
- The phone's Back button now closes the open panel or goes back to the schedule, instead of leaving the app.
- Tap a film in Pel·lícules to see its details: poster, director, sections, synopsis and all its screenings.
- In Pel·lícules you can pick several sections at once.
- Film details show the trailer when the festival has one (it plays right there), or a link to search for it on YouTube, plus a link to search the film on IMDb.

### Changed
- Tapping a session now opens its details. To mark it, tap the ☆ on the session, or Marca in its details.
- Ajustos is now a page of its own, and Sync is inside it.
- In sessions with several films, each film now has a plain dot instead of a red star, so it no longer looks like the watchlist mark.
- The red watchlist diamond on sessions is bigger and easier to spot.

### Removed
- The Imprescindible (!) mark on watchlist films. It only changed the order of the list.

## [1.8.2] - 2026-09-23

### Fixed
- In Catalan, the Settings window title now says "Ajustos", the same as its button.

## [1.8.1] - 2026-09-23

### Fixed
- On phones, the count badges on the day tabs are no longer cut off at the top, and the tabs have some space above them.

## [1.8.0] - 2026-09-23

### Added
- Build number at the bottom of Settings, to see which version a device runs.

### Fixed
- On phones, the circle that marks a session always started from the same corner. Chrome on Android drew the clip-path animation with a wrong origin inside the scrolling grid; the app now draws each frame itself. A tap also no longer gives the block the keyboard focus.

## [1.7.0] - 2026-09-23

### Changed
- Marked sessions are plain black blocks, without the yellow border and star; only warnings add a coloured frame.
- All panels work the same: a ✕ at the top right, a tap outside closes them, and the bottom only keeps real actions. On phones, Settings and Sync open full screen like Films. Settings and Sync keep their title in a fixed header while the content scrolls.
- The summary line shows only the warnings that exist, or "No conflicts", so it fits on one line.
- Hidden venues are in one "+N" button in the corner of the venue headers, which opens a list to show them again.
- The help hint shows once as a tip you can dismiss, and stays in Settings.
- Short transitions: panels fade and rise in when they open (the details panel slides up on phones), marking or unmarking a session spreads the new colour as a circle from where you tapped, and a new day fades in. They are off when the device asks for reduced motion.
- Sessions with more text than fits show a fade and "⋯" at the bottom, so the cut text does not look like an error.

### Fixed
- The help text in Settings now uses the full width of the panel.

## [1.6.0] - 2026-09-23

### Added
- Short-night warning: when the time from your last session of a night to your first session the next day is below your minimum rest (8 hours by default), both sessions show a warning, the day tab turns red and the summary counts short nights.
- The last session of each night shows the time until your first session the next day.
- Minimum rest setting. Sync also moves it.
- Replan: buttons in Settings clear all marked sessions or the whole watchlist, with a second tap to confirm and Undo for 10 seconds.
- Catalan and English for all app texts, including dates. Choose the language in Settings; the first time, the app uses Catalan on Catalan or Spanish phones and English on other phones.

### Changed
- The "Walk times" button is now "Settings", with the minimum rest and the walk times.
- The midnight line is now a dark dashed line, so red on the grid only marks the current time.
- On phones, the Settings, Films and Sync buttons sit together at the right of the bar.

## [1.5.0] - 2026-09-23

### Added
- Films view: search all films by title or director, filter by section, and see every screening.
- Watchlist: add films from the Films view or the details panel, and flag must-see films. Each film shows if a marked session covers it, how many screenings are still free, or why it cannot fit.
- Sessions that show a watchlist film have a ◆ marker on the grid.
- Sync also moves the watchlist.
- Film synopsis in Catalan in the session details panel, for every film that has one (297 of the 421 films in the programme).

### Changed
- Sessions whose name is not the film's title (for example "Sessió Especial", "Estrena Llargmetratge" or a retrospective cycle) now list the film they show, like multi-film sessions.

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

[Unreleased]: https://github.com/dbeltra/sitges-planner/compare/v1.8.1...HEAD
[1.8.1]: https://github.com/dbeltra/sitges-planner/compare/v1.8.0...v1.8.1
[1.8.0]: https://github.com/dbeltra/sitges-planner/compare/v1.7.0...v1.8.0
[1.7.0]: https://github.com/dbeltra/sitges-planner/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.com/dbeltra/sitges-planner/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/dbeltra/sitges-planner/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/dbeltra/sitges-planner/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/dbeltra/sitges-planner/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/dbeltra/sitges-planner/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/dbeltra/sitges-planner/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/dbeltra/sitges-planner/releases/tag/v1.0.0
