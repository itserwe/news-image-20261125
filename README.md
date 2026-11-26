# The World Today — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/itserwe/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/itserwe/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A single-page newspaper front page for Wednesday 25 November 2026: two
oil tankers hit by mines in the Strait of Hormuz, a Houthi strike on Saudi
Arabia's Ras Tanura refinery, and a wild Wall Street swing before
Thanksgiving — with 31 more stories, a UTC timeline of the day, a numbers
strip, and a map of where it all happened. Every item carries a CONFIRMED
or REPORTED mark plus its source, and a date-check box leaves out events
that happened on other days.

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
