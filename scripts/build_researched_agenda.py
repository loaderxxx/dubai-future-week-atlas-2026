"""Build a sourced agenda index for reviewed people from the saved event snapshot."""
from pathlib import Path
import csv,json
p=Path(__file__).resolve().parents[1]
people={r['name']:r['profile'] for r in csv.DictReader((p/'research/queue.csv').open()) if r['entity_type']=='person' and r['profile']}
a=json.loads((p/'data/sessions.json').read_text())
lines=['# Сессии исследованных спикеров','', 'Источник: сохранённый официальный API-срез 18 ноября 2026; не live-расписание. Dubai UTC+4. Public не гарантирует места или отсутствие отдельной регистрации. Invite-only не открывается общим пропуском. Для Government Foresight Peers: In Practice есть противоречие access_level и описания: требуется уточнение у организатора.','']
for day in sorted({x['event_day'] for x in a}):
 lines+=['## '+day,'','| Время | Сессия | Изученные спикеры | Доступ | Место |','|---|---|---|---|---|']
 for x in a:
  ns=[n for n in x['speakers'].split('; ') if n in people]
  if x['event_day']!=day or not ns:continue
  who=', '.join('['+n+']('+people[n].removeprefix('research/')+')' for n in ns)
  lines.append('| '+x['starts_at'][11:16]+'–'+x['ends_at'][11:16]+' | ['+x['title'].replace('|','/')+']('+x['source']+') | '+who+' | '+x['access_level']+' | '+str(x['venue'])+' |')
 lines+=['']
(p/'research/agenda-reviewed.md').write_text('\n'.join(lines))
