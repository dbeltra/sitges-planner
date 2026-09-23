# Sitges 2026 Planner

A day-by-venue grid of the Sitges Film Festival 2026 programme. Mark the sessions you want to see and get warnings for overlaps, tight venue changes and films marked twice. Installable on Android as a PWA.

Live: https://dbeltra.github.io/sitges-planner/

## Update the programme

The festival data is downloaded once and stored locally; the raw files are not committed. From the repo root:

```sh
python3 data/fetch.py      # download the programme (only pages whose version changed)
python3 data/directors.py  # director names; fetches only film pages not cached yet
python3 data/build.py      # write data/schedule.js for the app
```

Then commit `data/schedule.js` and push. The installed app picks up the new data the next time it is opened.

## Run locally

Open `index.html` directly, or serve the folder (needed for the offline service worker):

```sh
python3 -m http.server 8000
```
