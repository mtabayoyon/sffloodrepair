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
