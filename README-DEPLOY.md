# sanfranciscofloodrepair.com — North Bay Buildout (Marin · Sonoma · Napa)
Build: 2026-10-14 · Scripts: `_build/engine.py`, `_build/pages.py`, `_build/links.py` (re-runnable; `_build/` is git-ignored)

## Deploy
1. GitHub Desktop → review changes → **Commit to main** → **Push origin**. No force push.
2. After the deploy goes green, resubmit `https://www.sanfranciscofloodrepair.com/sitemap.xml` in Search Console.
3. Request indexing in Search Console for `/water-damage-repair-petaluma/`, `/mold-inspection-san-rafael/`, `/north-bay-restoration/`.
4. Point the Petaluma Google Business Profile website link at `/sonoma-county-restoration/` or `/restoration-services-petaluma/`.

## What changed
**Petaluma water page rebuilt** (`/water-damage-repair-petaluma/`, same URL): "water damage restoration petaluma" = 200/mo at ~$55 CPC.
It was old-template, said "Petaluma, San Francisco", and had **1** internal link; now **59**. Google was ranking `/water-damage-napa/` for Petaluma.

**11 new service pages** (Ahrefs US volume):
| Page | Target | Vol |
|---|---|---|
| /mold-inspection-san-rafael/ | mold inspection san rafael | 200 |
| /mold-removal-sausalito/ | mold removal sausalito | 90 |
| /water-damage-restoration-sausalito/ | water damage (restoration) sausalito | 70 |
| /mold-remediation-sonoma-county/ | mold remediation sonoma county | 60 |
| /mold-remediation-san-anselmo/ | mold remediation san anselmo | 50 |
| /mold-inspection-santa-rosa/ | mold inspection santa rosa | 50 |
| /fire-damage-restoration-sonoma/ | fire damage restoration sonoma | 50 |
| /fire-damage-restoration-healdsburg/ | fire damage restoration healdsburg | 40 |
| /fire-damage-restoration-rohnert-park/ | fire damage restoration rohnert park | 40 |
| /water-damage-restoration-larkspur/ | water damage larkspur | 30 |
| /fire-damage-restoration-sonoma-county/ | fire damage restoration sonoma county | 10+ |

**4 hubs:** /north-bay-restoration/, /marin-county-restoration/, /sonoma-county-restoration/, /napa-county-restoration/ — linked from /cities-we-serve/ and /restoration-services-petaluma/.

**7 duplicate pages consolidated** (meta-refresh + canonical + noindex, same pattern as before) — none ranked in Ahrefs:
santa-rosa-fire-damage-repair → fire-damage-restoration-santa-rosa · napa-fire-damage-clean-up-for-homes-and-businesses → fire-damage-restoration-napa ·
napa-mold-cleanup-from-arc → mold-remediation-napa · water-damage-san-rafael → water-mitigation-san-rafael · arc-flood-damage-repair-marin → water-damage-restoration-marin-county ·
marin-smoke-damage-repair-services → fire-restoration-marin-county · call-arc-for-water-damage-repair-american-canyon → water-damage-american-canyon.
Plus 5 nested duplicates under /property-repair-services/ (Corte Madera, Larkspur, Belvedere mold; Santa Rosa fire; San Rafael sewage) now point to their root pages.

**Retargets:** water-mitigation-san-rafael (title/H1 → "Water Damage Restoration San Rafael"), Mill Valley smoke page → fire damage, Mill Valley flood page → water damage.

**45 existing North Bay pages** got a "More [County] Restoration Services" link block (county hub, North Bay hub, Petaluma water, new pages).
**24 pages fixed** whose bottom banner said "Serving Santa Rosa 24/7" (Petaluma, Napa, San Rafael, Novato, Oakland, San Jose, etc.).
**Sitemap rebuilt:** 600 canonical URLs — also picked up ~25 August city pages that were never added to sitemap.xml.

Checks: 0 broken internal links, all JSON-LD valid, new-page similarity median 33% / max 60%.

---

# sanfranciscofloodrepair.com — Geo SEO Expansion + Cannibalization Repair
Build: 2026-08-25 · Script: `fix_geo_20260825.py` (re-runnable)

## Deploy (same process as alliedrentalco)

1. Unzip this download.
2. Copy **all** contents into your local `Documents\GitHub\sffloodrepair\` folder, overwriting.
3. Confirm **`CNAME`** landed in the root (contains `www.sanfranciscofloodrepair.com`).
   Also new: **`.nojekyll`** — leave it there.
4. GitHub Desktop → review changes → **Commit to main** → **Push origin**. No force push.
5. After the deploy goes green, submit `https://www.sanfranciscofloodrepair.com/sitemap.xml`
   in Search Console. 26 URLs are new.

Images were untouched — your `images/` folder is unchanged.

## What changed

**25 new city × service pages** filling verified demand gaps with no existing page:

| City | Pages added |
|---|---|
| San Jose | water, mold, fire |
| Oakland | water, mold, fire |
| Berkeley | water, mold, fire |
| Walnut Creek | mold, fire |
| Richmond, Vallejo, San Leandro | water + mold |
| Santa Rosa, Napa | fire |
| Petaluma | mold, fire |
| San Rafael, Hayward, Novato, Alameda | mold |

Each page carries curated local content — real neighborhoods, the actual local
failure modes (San Jose slab leaks, Oakland crawlspaces, Berkeley landmarked
Brown Shingles, Santa Rosa post-2017 rebuild defects), the dispatching office
and its address, Service + FAQPage schema, and breadcrumbs.
Cross-page similarity: 31% median, 55% max — under the 60% risk threshold.

**7 pages retargeted** (title / meta / H1 / OG / Twitter):
- `/mold-remediation-clean-up-san-francisco/` → "mold remediation san francisco" (200 vol, KD 3)
- `/fire-smoke-clean-up-san-francisco/` → "fire damage restoration san francisco" (150 vol)
- `/water-mitigation-san-rafael/` → "water damage restoration san rafael"
- `/how-do-soot-and-ash-do-damage/` → "soot damage" (500 vol, KD 0, currently #19)
- `/water-damage-restoration-sonoma-county/` → Santa Rosa + Petaluma emphasis
- `/water-damage-restoration-marin-county/` → Marin city coverage
- `/mold-remediation-cupertino/` → correct primary term

**6 pages de-optimized** so they stop competing with the homepage for
"water damage restoration san francisco (ca)": `/property-repair-services/`,
`/biohazard-cleanup-services/`, `/team/`, `/damage-repair-tips/`,
`/water-damage-clean-up-san-francisco/`, `/water-damage-cleaning-service-san-francisco/`.
They stay indexed and useful — they just no longer target the head term.

**115 city pages** got a "Nearby Service Areas" block, ring-linked so every page
in each service family receives inbound links (new pages: 7–8 inbound each).

**5 hub pages** (`/cities-we-serve/` + the four office pages) now link the new cities.

**12 blog pagination pages fixed.** `/damage-repair-tips/page-2/` through `page-12/`
were emitting `../../../` from a depth-2 directory. Every one of those pages has
been loading **no CSS** and every nav link on them 404s. This was pre-existing and
is the reason site-wide broken links dropped from 622 to 0.

**sitemap.xml regenerated** — 651 URLs (was 578; 48 live pages were missing entirely).

## Validation

| Check | Before | After |
|---|---|---|
| Pages | 626 | 651 |
| Broken internal links | 622 | 0 |
| Broken image refs | 0 | 0 |
| Invalid JSON-LD blocks | — | 0 of 1,496 |
| URLs in sitemap | 578 | 651 |

## After deploy

1. Search Console → submit sitemap, then request indexing on the 6 highest-value
   new URLs: San Jose water/mold/fire, Oakland water/mold, Walnut Creek mold.
2. Add the new cities to the service areas of the matching Google Business Profile
   (San Jose office → San Jose; Walnut Creek → Oakland, Berkeley, Richmond, Hayward,
   Alameda, San Leandro; Petaluma → Santa Rosa, Napa, Petaluma, Novato, San Rafael, Vallejo).
3. Recrawl in Ahrefs in 3–4 weeks and compare against the 29-keyword baseline.
