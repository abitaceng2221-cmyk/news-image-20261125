# World News — 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/abitaceng2221-cmyk/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/abitaceng2221-cmyk/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

Entry for the make.fun bounty [Sum up 25 November's world news in one image](https://make.fun/bounty/news-image-20261125).

The program copies one infographic, `entry.png` (1024×1024), to `/output/entry.png`.
The image sums up Wednesday, 25 November 2026 in six stories: tankers hit by mines
in the Strait of Hormuz, US tariffs proposed on 14 trading partners, the leaked
Russian war death toll near 500,000, the first Pakistani astronaut in orbit aboard
Shenzhou-24, 20 hostages freed in Cartagena, and the Solomon Islands–Australia treaty.

## How the image was made

`gen_image.py` draws the infographic with code (PIL + DejaVu Sans, both already
on the machine). No fonts or images were downloaded. Run it to regenerate the
image deterministically:

```sh
python3 gen_image.py
```

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This copies `entry.png` to the output directory, byte for byte, deterministically.
