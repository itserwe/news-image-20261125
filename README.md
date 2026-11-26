# The World Today — 25 November 2026 (REVISED)

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/itserwe/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/itserwe/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A single-page newspaper front page for Wednesday 25 November 2026, revised
from the first entry (which ranked 11,843rd of 18,764 at 96.27%): two oil
tankers hit by mines in the Strait of Hormuz, a Houthi strike on Saudi
Arabia's Ras Tanura refinery, and a wild Wall Street swing before
Thanksgiving — now with 38 stories instead of 34, re-curated across all five
world regions with the day's full news, including the judges urging
Netanyahu's bribery case dropped, Russia's biggest military budget since
Soviet times, 31 killed in a Cairo fuel-tanker fire, 29 miners trapped in
Indonesia, a "terrorist attack" blackout in Colombia, North Korea expelling
Swiss diplomats, and a US-led deal for Lukoil's foreign assets. A UTC
timeline of the day, a numbers strip with per-region counts, a map of where
it all happened, and a date-check box that leaves out events from other days
— including the Hong Kong Tai Po fire, which happened on 26 November, not
the 25th. Every item carries its source.

## How the page is made

`entry.png` (1024 × 1024) was drawn with Pillow in the build session —
masthead, headlines, lead stories, secondaries, map, briefs, everything.
No image generator is involved. `main.py` (standard library only) copies
the pre-drawn `entry.png` to the output directory, so the page comes out
byte-identical on every run, including on a machine without Pillow.

## Regenerate

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.png`.
