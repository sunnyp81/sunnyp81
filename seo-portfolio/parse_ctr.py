import csv, io, json

raw = open('/home/user/sunnyp81/seo-portfolio/_raw.txt').read()
# unescape markdown
raw = raw.replace('\\_','_').replace('\\#','#')
lines = [l.strip() for l in raw.splitlines() if l.strip()]
header = lines[0]
rows = []
for line in lines[1:]:
    parts = line.split(',')
    # columns: site,page,clicks,impressions,ctr,position,expected_ctr,potential_clicks,prev_clicks,prev_impressions,prev_position
    if len(parts) < 8:
        continue
    site = parts[0]
    page = parts[1]
    clicks = float(parts[2])
    impressions = float(parts[3])
    ctr = float(parts[4])
    position = float(parts[5])
    expected_ctr = float(parts[6])
    potential_clicks = float(parts[7])
    rows.append({
        'site': site, 'page': page, 'clicks': clicks, 'impressions': impressions,
        'ctr': ctr, 'position': position, 'expected_ctr': expected_ctr,
        'potential_clicks': potential_clicks,
        'click_gap': round(potential_clicks - clicks, 2)
    })

# sort by potential_clicks desc
rows.sort(key=lambda r: r['potential_clicks'], reverse=True)

# priority
def priority(r):
    if r['position'] < 10:
        return 'P1'
    elif r['position'] <= 20:
        return 'P2'
    return 'P3'

# write action list csv
with open('/home/user/sunnyp81/seo-portfolio/02-ctr-action-list.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['rank','site','page','position','impressions','clicks','expected_ctr','potential_clicks','click_gap','priority','notes'])
    for i,r in enumerate(rows,1):
        pri = priority(r)
        notes = []
        # SERP feature suspicion: page1, decent position, near-zero ctr, big impressions
        if r['position'] < 10 and r['clicks']==0 and r['impressions']>=300:
            notes.append('SERP-feature suspect (0 clicks, pos<10, high impr) - possible AI overview/snippet eating clicks')
        elif r['position'] < 8 and r['ctr'] < (r['expected_ctr']*0.4) and r['impressions']>=500:
            notes.append('Far below expected CTR at strong position - title/snippet fix')
        if '#' in r['page']:
            notes.append('Anchor/fragment URL - dedupe in GSC, fix parent page')
        if pri=='P1':
            notes.append('Page 1 - fastest win')
        elif pri=='P2':
            notes.append('Page 2 - secondary tier')
        w.writerow([i, r['site'], r['page'], round(r['position'],2), int(r['impressions']),
                    int(r['clicks']), r['expected_ctr'], r['potential_clicks'], r['click_gap'],
                    pri, '; '.join(notes)])

# totals
p1_gap = sum(r['click_gap'] for r in rows if priority(r)=='P1')
p2_gap = sum(r['click_gap'] for r in rows if priority(r)=='P2')
total_gap = sum(r['click_gap'] for r in rows)
print('rows', len(rows))
print('P1 total click_gap', round(p1_gap,1))
print('P2 total click_gap', round(p2_gap,1))
print('total click_gap', round(total_gap,1))
print('biggest:', rows[0]['page'], rows[0]['potential_clicks'], 'gap', rows[0]['click_gap'])

# dump top 30 (non-fragment preferred for rewrites) as json
top = [r for r in rows][:35]
json.dump(top, open('/home/user/sunnyp81/seo-portfolio/_top.json','w'), indent=1)
for r in rows[:30]:
    print(round(r['potential_clicks'],1), '| pos', round(r['position'],1), '| impr', int(r['impressions']), '| clk', int(r['clicks']), '|', priority(r),'|', r['page'])
