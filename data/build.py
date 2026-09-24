# Joins the raw downloads into schedule.json. Offline: reads local files only.
import json, glob, os, re, html

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load(pattern, key):
    return [x for p in sorted(glob.glob(pattern)) for x in json.load(open(p))[key]]

films = {f['id']: f for f in load('films/*.json', 'films')}
sessions = load('pages/*.json', 'sessions')
directors = json.load(open('directors.json'))
trailers = json.load(open('trailers.json'))
cats = json.load(open('categories.json'))
sections = {s['id']: s['name']['ca'] for s in cats['sections']}
locations = {l['id']: l['name']['ca'] for l in json.load(open('locations.json'))['locations']}
RENAME = {'Sala Llevant': 'Brigadoon'}
locations = {k: RENAME.get(v, v) for k, v in locations.items()}

def text(h):
    # Synopses are small HTML fragments; the app shows plain text, one paragraph per <p>/<br>.
    h = re.sub(r'(?i)<br\s*/?>|</p>', '\n', h or '')
    h = html.unescape(re.sub(r'<[^>]+>', '', h)).replace('\xa0', ' ')
    return '\n'.join(l.strip() for l in h.split('\n') if l.strip())

def query(f):  # search text for YouTube and IMDb: original title and year
    return (f['original_title'] or f['title']['en']).strip(' "') + (f' {f["year"]}' if f['year'] else '')

out = []
for s in sessions:
    fs = [films[i] for i in s['films'] if i in films]
    out.append({
        'id': s['internal_id'],
        'title': s['name']['ca'],
        'films': [{'title': f['title']['ca'], 'directors': directors.get(f['id'], []), 'url': f['url']['ca'], 'image': f['image'], 'synopsis': text(f['synopsis']['ca']), 'sections': sorted({sections.get(x, x) for x in f['sections']}), 'trailer': trailers.get(f['id']), 'query': query(f)} for f in fs],
        'sections': sorted({sections.get(x, x) for f in fs for x in f['sections']}),
        'location': ', '.join(locations.get(x, x) for x in s['locations']),
        'start': s['start_date'],
        'end': s['end_date'],
        'duration': s['duration'],
    })
out.sort(key=lambda x: (x['start'], x['location']))
json.dump(out, open('schedule.json', 'w'), ensure_ascii=False, indent=1)

missing = [s['films'] for s in sessions if any(i not in films for i in s['films'])]
assert not missing, missing
print(len(out), 'sessions,', len({s['location'] for s in out}), 'locations')
# ponytail: JS wrapper so index.html works from file:// without a server
open('schedule.js', 'w').write('window.SCHEDULE = ' + json.dumps(out, ensure_ascii=False) + ';\n')
