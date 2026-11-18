"""Read publicly served event agenda; retain only public business metadata."""
import json,csv,urllib.request,pathlib,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
url='https://prd-api.dubaifutureweek.com/api/public/agenda/sessions/?page=1&page_size=100'
rows=[]; expected=None
while url:
 with urllib.request.urlopen(url,timeout=40) as r: j=json.load(r)
 expected=j['count']; rows+=j['results'];url=j['next']
clean=[]
for r in rows:
 if 'web_programme' in r.get('hidden_placements',[]): continue
 v=r.get('venue') or {};t=r.get('track') or {}
 clean.append(dict(code=r['code'],title=r['title'],starts_at=r['starts_at'],ends_at=r['ends_at'],event_day=r['event_day'],venue=v.get('title'),location=v.get('location'),access_level=r.get('access_level'),session_type=r.get('session_type'),concept=r.get('agenda_type'),track=t.get('name'),speakers='; '.join(x['name'] for x in r.get('speakers',[])),organizations='; '.join(dict.fromkeys(x.get('organization','') for x in r.get('speakers',[]) if x.get('organization'))),partners='; '.join(x['name'] for x in r.get('sponsors',[])),source='https://www.dubaifutureweek.com/en/programme?session='+r['code'],verified_date='2026-11-18'))
(ROOT/'data/sessions.json').write_text(json.dumps(clean,ensure_ascii=False,indent=2))
with (ROOT/'data/sessions.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(clean[0]));w.writeheader();w.writerows(clean)
print('API count',expected,'retrieved',len(rows),'unique',len({r['code'] for r in rows}));print('Hidden placement values',set(str(r.get('hidden_placements')) for r in rows))
for r in clean:
 if r['event_day']=='2026-11-18' and any(x in r['title'].lower() for x in [' ai ','intelligence','agent','pitch','grandmaster']):print(r)
