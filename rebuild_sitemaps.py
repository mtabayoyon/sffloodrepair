#!/usr/bin/env python3
"""
Allied Restoration — Sitemap Rebuilder
Run this script ANY TIME pages are added/removed to regenerate both sitemaps.
Usage: python3 rebuild_sitemaps.py
It scans every index.html on disk (recursively), excludes non-canonical alias
pages automatically, and rewrites both sitemap.xml and sitemap.html in sync.
"""
import re, glob, os
from collections import defaultdict
from datetime import date

root = '/home/claude/sffloodrepair'
SITE = 'https://www.sanfranciscofloodrepair.com'
GH = 'https://mtabayoyon.github.io/sffloodrepair'
today = date.today().isoformat()

EXCLUDE = {'2643-2','privacy-policy-2','projects-in-action-video','subscribe-to-get-updates',
           'thank-you','thanks-contacting-us','zoho-contact-form','sitemap','404',
           'www.sanfranciscofloodrepair.com'}

def get_title(fp):
    try:
        with open(fp) as f: c = f.read(3000)
        m = re.search(r'<title>([^<]+)</title>', c)
        if m: return re.sub(r'\s*\|.*$','', m.group(1)).strip()
    except: pass
    return os.path.basename(os.path.dirname(fp)).replace('-',' ').title()

def get_canonical(fp):
    try:
        with open(fp) as f: c = f.read(4000)
        m = re.search(r'<link rel="canonical" href="https://www\.sanfranciscofloodrepair\.com/([^"]*)"', c)
        if m: return m.group(1).rstrip('/')
    except: pass
    return None

# ── Scan ALL pages recursively ────────────────────────────────────────────────
all_pages = []  # (slug, title, is_canonical)
for fp in glob.glob(f'{root}/**/index.html', recursive=True):
    slug = fp.replace(root+'/','').replace('/index.html','')
    if slug in EXCLUDE: continue
    if 'damage-repair-tips/page-' in slug: continue
    canon = get_canonical(fp)
    is_canonical = (canon is None or canon == slug)
    all_pages.append((slug, get_title(fp), is_canonical))
# root index
all_pages.append(('', 'Allied Restoration — San Francisco Flood Repair', True))

# ── sitemap.xml: canonical pages only ─────────────────────────────────────────
def priority(slug):
    if slug == '': return '1.0'
    if any(x in slug for x in ['water-damage-repair-in-san-francisco','mold-remediation-clean-up','fire-smoke-clean-up','raw-sewage-clean-up','emergency-water-damage','commercial-restoration-services','commercial-water-damage','commercial-fire-damage','large-loss-restoration','restoration-services-','water-damage-restoration-near-me']): return '0.9'
    if any(x in slug for x in ['water-damage-','mold-remediation-','commercial-','fire-damage-','how-to-','cost']): return '0.8'
    return '0.6'

xml = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
xml_count = 0
for slug, title, is_canon in sorted(all_pages):
    if not is_canon: continue
    url = f'{SITE}/' if slug=='' else f'{SITE}/{slug}/'
    xml.append(f'  <url><loc>{url}</loc><lastmod>{today}</lastmod><priority>{priority(slug)}</priority></url>')
    xml_count += 1
xml.append('</urlset>')
with open(f'{root}/sitemap.xml','w') as f:
    f.write('\n'.join(xml))

# ── sitemap.html: all pages, categorized ──────────────────────────────────────
def categorize(slug):
    if slug=='': return ('Core Pages',1)
    if slug=='damage-repair-tips': return ('Articles & Resources',7)
    if slug.startswith('commercial-') or slug=='large-loss-restoration': return ('Commercial & Industrial',2)
    if slug in ('upstairs-neighbor-flooded-my-apartment','what-to-do-when-your-apartment-floods','water-leaking-through-ceiling','does-water-damage-decrease-home-value'): return ('Renter & Homeowner Guides',8)
    if slug in ('fire-damage-inspection','water-mitigation-vs-restoration','what-to-throw-away-after-smoke-damage','what-is-a-restoration-technician'): return ('Expert Guides',8)
    if slug.startswith('restoration-services-'): return ('Services Near Me',2)
    if slug.startswith('hrf_faq/'): return ('FAQ Pages',16)
    if slug.startswith('property-repair-services/'): return ('Property Repair Services',13)
    if re.match(r'^water-damage-[a-z]', slug) and slug not in ('water-damage-repair-in-san-francisco','water-damage-restoration-near-me','water-damage-restoration-cost-san-francisco'): return ('City Water Damage Pages',14)
    if re.match(r'^mold-remediation-[a-z]', slug) and slug not in ('mold-remediation-clean-up-san-francisco','mold-remediation-cost-san-francisco','mold-remediation-technician'): return ('City Mold Pages',15)
    if any(x in slug for x in ['water-damage-in-','water-damage-repair-in-','flood-clean-up-pacific','water-damage-repair-petaluma']): return ('SF Neighborhoods — Water',3)
    if slug.startswith('fire-and-smoke-damage'): return ('SF Neighborhoods — Fire',4)
    if 'mold-damage-and-restoration-in-' in slug: return ('SF Neighborhoods — Mold',5)
    if any(x in slug for x in ['biohazard','decontam','environmental','infectious']): return ('Biohazard & Environmental',13)
    if any(x in slug for x in ['hardwood','floor','carpet','laminate','birch','oak-hardwood','walnut-hardwood','maple-hardwood']): return ('Flooring Services',9)
    if any(x in slug for x in ['employment','manager','accounts','restoration-tech','mitig','office-admin','seeking','pdmm','technician']): return ('Careers',11)
    if any(x in slug for x in ['arc-','marin','corte-madera','mill-valley','san-anselmo','san-rafael','novato','fairfax','belvedere','larkspur','napa','american-canyon','sebastopol','santa-rosa','rohnert','cotati']): return ('Bay Area Regional',10)
    if any(x in slug for x in ['black-mold','water-mitigation','storm-damage','smoke-remediation','sewage-damage','basement-flooding','crawl-space','emergency-water','how-to-','board-up','structural-drying']): return ('Service & Resource Pages',2)
    return ('Service & Informational Pages',12)

groups = defaultdict(list)
for slug, title, _ in all_pages:
    cat, order = categorize(slug)
    groups[(order,cat)].append((slug,title))

sections = ''
html_count = 0
for (order,cat) in sorted(groups.keys()):
    items = sorted(groups[(order,cat)], key=lambda x:x[1].lower())
    li = ''.join(f'<li><a href="{GH}/{(s+"/") if s else ""}">{t}</a></li>' for s,t in items)
    sections += f'<div class="sm-section"><h3>{cat} <span class="sm-count">({len(items)})</span></h3><ul>{li}</ul></div>\n'
    html_count += len(items)

page = f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Sitemap | Allied Restoration Company</title><meta name="robots" content="index,follow">
<link rel="stylesheet" href="css/style.css">
<style>.sm-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px;margin-top:24px}}.sm-section h3{{font-family:var(--fh);font-size:16px;color:#003262;border-bottom:2px solid #eef0f3;padding-bottom:8px;margin-bottom:10px}}.sm-count{{color:#9aa0a6;font-weight:400;font-size:13px}}.sm-section ul{{list-style:none;padding:0;margin:0}}.sm-section li{{padding:3px 0;font-size:13px}}.sm-section a{{color:#5a6270;text-decoration:none}}.sm-section a:hover{{color:#003262}}</style>
</head><body>
<div class="eb">🚨 Water Damage Emergency? Call Now: <a href="tel:+14155295637">(415) 529-5637</a> — Available 24/7</div>
<header class="sh"><div class="hi"><a href="index.html" class="logo"><img src="images/allied-logo.svg" alt="Allied Restoration Company" style="height:44px;width:auto"></a><nav class="mn" id="mn"><a href="/">Home</a><a href="water-damage-repair-in-san-francisco/">Water Damage</a><a href="commercial-restoration-services/">Commercial</a><a href="cities-we-serve/">Locations</a><a href="contact/" class="nc">📞 Emergency Call</a></nav><button class="nt" id="nt"><span></span><span></span><span></span></button></div></header>
<main><section style="background:#003262;padding:40px 24px"><div style="max-width:1100px;margin:0 auto"><h1 style="font-family:var(--fh);font-size:36px;font-weight:800;color:#fff;margin:0">Sitemap</h1><p style="color:rgba(255,255,255,.8);margin:8px 0 0"><strong>{html_count} total pages</strong> organized by category</p></div></section>
<section class="sec"><div class="con" style="max-width:1100px;margin:0 auto"><div class="sm-grid">{sections}</div></div></section></main>
<footer class="ft"><div class="fi2"><div class="fb"><div style="font-family:var(--fh);font-size:18px;font-weight:700;color:#fff">Allied Restoration Company</div><a href="tel:+14155295637" style="font-size:20px;font-weight:700;color:#fff;display:block;margin-top:8px">(415) 529-5637</a></div></div><div class="fb2"><p>© 2026 Allied Restoration Company.</p></div></footer>
<script src="js/main.js"></script></body></html>'''
with open(f'{root}/sitemap.html','w') as f:
    f.write(page)

print(f"✓ sitemap.xml  — {xml_count} canonical URLs")
print(f"✓ sitemap.html — {html_count} pages in {len(groups)} categories")
