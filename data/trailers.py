# YouTube trailer id per film, from the video the festival embeds on the film page. Fetches only film pages not cached yet.
import json, glob, re, time, urllib.request, urllib.parse, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

films = [f for p in glob.glob('films/*.json') for f in json.load(open(p))['films']]
os.makedirs('film-pages', exist_ok=True)
out = {}
for f in films:
    path = f"film-pages/{f['internal_id']}.html"
    if not os.path.exists(path):
        req = urllib.request.Request('https://sitgesfilmfestival.com' + f['url']['ca'], headers={'User-Agent': 'Mozilla/5.0 (sitges-planner)'})
        open(path, 'wb').write(urllib.request.urlopen(req, timeout=30).read())
        time.sleep(1)  # public site: stay polite
    m = re.search(r'oembed\?url=([^&"]+)', open(path).read())
    v = m and re.search(r'(?:v=|youtu\.be/)([\w-]{11})', urllib.parse.unquote(m.group(1)))
    if v:
        out[f['id']] = v.group(1)

json.dump(out, open('trailers.json', 'w'), indent=1)
print(len(out), 'trailers for', len(films), 'films')
