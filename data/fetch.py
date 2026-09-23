# Downloads the festival programme into data/. Re-run to update: pages whose version hash is unchanged are skipped.
import json, os, time, urllib.request

os.chdir(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://sitgesfilmfestival.com'
YEAR = 2026
FILES = {
    'edition.json': f'/public/api/films/{YEAR}/edition.json',
    'categories.json': '/public/api/films/categories.json',
    'locations.json': '/public/api/films/locations.json',
}
MANIFESTS = {  # local manifest file, folder for its pages, page file prefix, URL
    'sessions': ('sessions-manifest.json', 'pages', 'sessions', f'/api/v1/se/films/{YEAR}/sessions/manifest?format=full'),
    'films': ('films-manifest.json', 'films', 'films', f'/api/v1/se/films/{YEAR}/films/manifest?format=full'),
}
requests = 0


def get(path):
    global requests
    if requests:
        time.sleep(1)  # public site: stay polite
    requests += 1
    req = urllib.request.Request(SITE + path, headers={'User-Agent': 'Mozilla/5.0 (sitges-planner)'})
    with urllib.request.urlopen(req, timeout=30) as res:
        return res.read()


def save(path, data):
    json.loads(data)  # refuse to overwrite good data with an error page
    tmp = path + '.tmp'
    open(tmp, 'wb').write(data)
    os.replace(tmp, path)


for name, url in FILES.items():
    save(name, get(url))

for key, (manifest_file, folder, prefix, url) in MANIFESTS.items():
    old = {}
    if os.path.exists(manifest_file):
        old = {p['start']: p['v'] for p in json.load(open(manifest_file))['pages']}
    data = get(url)
    pages = json.loads(data)['pages']
    os.makedirs(folder, exist_ok=True)
    wanted, fetched = set(), 0
    for p in pages:
        out = f"{folder}/{prefix}-{p['start']}.json"
        wanted.add(os.path.basename(out))
        if old.get(p['start']) == p['v'] and os.path.exists(out):
            continue
        save(out, get(p['url']))
        fetched += 1
    removed = [f for f in os.listdir(folder) if f.endswith('.json') and f not in wanted]
    for f in removed:
        os.remove(f'{folder}/{f}')
    save(manifest_file, data)  # last, so an interrupted run re-fetches what it missed
    print(f'{key}: {len(pages)} pages, {fetched} downloaded, {len(pages) - fetched} unchanged, {len(removed)} removed')

print(f'{requests} requests')
