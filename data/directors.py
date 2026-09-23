# Builds directors.json: names from film credits, else from the film page JSON-LD (cached in film-pages/).
import json, glob, re, html, time, urllib.request, os

films = [f for p in glob.glob('films/*.json') for f in json.load(open(p))['films']]

def from_credits(f):
    m = re.search(r'Direcci[^<]*</strong>(.*?)(<strong>|$)', html.unescape(f['credits']['ca']), re.S)
    return [n.strip() for n in re.sub(r'<[^>]+>', ' ', m.group(1)).replace('\xa0', ' ').split(',') if n.strip()] if m else []

def from_page(s):
    names = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        for node in json.loads(block).get('@graph', []):
            if node.get('@type') == 'Movie':
                d = node.get('director') or []
                names += [x['name'] for x in (d if isinstance(d, list) else [d])]
    return names

out = {}
for f in films:
    n = from_credits(f)
    if n:
        out[f['id']] = n
        continue
    if not f['directors']:
        continue
    path = f"film-pages/{f['internal_id']}.html"
    if not os.path.exists(path):
        req = urllib.request.Request('https://sitgesfilmfestival.com' + f['url']['ca'], headers={'User-Agent': 'Mozilla/5.0'})
        open(path, 'wb').write(urllib.request.urlopen(req).read())
        time.sleep(1)
    out[f['id']] = from_page(open(path).read())

json.dump(out, open('directors.json', 'w'), ensure_ascii=False, indent=1)
