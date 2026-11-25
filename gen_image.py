#!/usr/bin/env python3
"""Generate entry.png: a 1024x1024 news infographic for Wednesday 25 November 2026.

Draws everything with code (PIL + DejaVu Sans, both present on this machine).
No downloaded fonts or images. Output is deterministic: same bytes every run.
Run: python3 gen_image.py  (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")
W, H = 1024, 1024

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()

TITLE_FONT = font("DejaVuSans-Bold.ttf", 76)
DATE_FONT = font("DejaVuSans-Bold.ttf", 34)
SUB_FONT = font("DejaVuSans.ttf", 24)
NUM_FONT = font("DejaVuSans-Bold.ttf", 30)
TAG_FONT = font("DejaVuSans-Bold.ttf", 19)
HEAD_FONT = font("DejaVuSans-Bold.ttf", 29)
BODY_FONT = font("DejaVuSans.ttf", 23)
FOOT_FONT = font("DejaVuSans.ttf", 20)

NAVY = (13, 27, 62)
NAVY2 = (19, 41, 89)
GOLD = (212, 175, 55)
WHITE = (255, 255, 255)
INK = (18, 24, 38)
GREY = (90, 98, 115)
BG = (242, 244, 248)
CARD = (255, 255, 255)
ACCENTS = [(178, 34, 34), (0, 90, 156), (90, 55, 130), (0, 110, 90), (176, 92, 0), (0, 100, 120)]

STORIES = [
    ("01", "MIDDLE EAST", "TANKERS HIT IN HORMUZ",
     "Iran says two oil tankers struck mines in the strait and caught fire.", "ship"),
    ("02", "TRADE", "US TARIFFS ON 14 PARTNERS",
     "Washington proposes new duties; China faces 20% extra.", "chart"),
    ("03", "UKRAINE WAR", "WAR TOLL NEAR 500,000",
     "Leaked Russian figures analysed by the BBC count 490,334 soldiers dead.", "candle"),
    ("04", "SPACE", "FIRST PAKISTANI IN ORBIT",
     "Shenzhou-24 carries Muhammad Zeeshan Ali to Tiangong station.", "rocket"),
    ("05", "COLOMBIA", "20 HOSTAGES FREED",
     "Colombian forces storm a Cartagena supermarket; one captor is killed.", "check"),
    ("06", "PACIFIC", "PACIFIC TREATY SIGNED",
     "Solomon Islands and Australia sign a deal barring foreign military bases.", "treaty"),
]

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_icon(d, kind, cx, cy, r, colour):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=colour)
    if kind == "ship":
        d.rectangle([cx - 2, cy - 26, cx + 2, cy + 2], fill=WHITE)
        d.polygon([(cx + 2, cy - 26), (cx + 2, cy - 10), (cx + 17, cy - 10)], fill=(255, 200, 60))
        d.polygon([(cx - 24, cy + 2), (cx + 24, cy + 2), (cx + 16, cy + 20), (cx - 16, cy + 20)], fill=WHITE)
        d.arc([cx - 28, cy + 22, cx + 28, cy + 34], 0, 180, fill=WHITE, width=4)
    elif kind == "chart":
        for i, h in enumerate((14, 24, 34)):
            x = cx - 22 + i * 18
            d.rectangle([x, cy + 24 - h, x + 12, cy + 24], fill=WHITE)
        d.line([cx - 26, cy + 24, cx + 26, cy + 24], fill=WHITE, width=4)
    elif kind == "candle":
        d.rectangle([cx - 9, cy - 6, cx + 9, cy + 28], fill=WHITE)
        d.polygon([(cx, cy - 32), (cx - 8, cy - 12), (cx + 8, cy - 12)], fill=(255, 200, 60))
    elif kind == "rocket":
        d.polygon([(cx, cy - 36), (cx - 14, cy + 6), (cx + 14, cy + 6)], fill=WHITE)
        d.rectangle([cx - 14, cy + 2, cx + 14, cy + 18], fill=WHITE)
        d.polygon([(cx - 14, cy + 10), (cx - 26, cy + 28), (cx - 8, cy + 20)], fill=WHITE)
        d.polygon([(cx + 14, cy + 10), (cx + 26, cy + 28), (cx + 8, cy + 20)], fill=WHITE)
        d.polygon([(cx, cy + 20), (cx - 7, cy + 36), (cx + 7, cy + 36)], fill=(255, 200, 60))
    elif kind == "check":
        d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], outline=WHITE, width=5)
        d.line([cx - 16, cy + 1, cx - 3, cy + 14, cx + 18, cy - 14], fill=WHITE, width=7, joint="curve")
    elif kind == "treaty":
        d.rectangle([cx - 26, cy - 28, cx + 26, cy + 28], fill=WHITE)
        d.line([cx - 16, cy - 14, cx + 16, cy - 14], fill=colour, width=4)
        d.line([cx - 16, cy - 2, cx + 16, cy - 2], fill=colour, width=4)
        d.line([cx - 16, cy + 10, cx + 6, cy + 10], fill=colour, width=4)
        d.ellipse([cx + 8, cy + 8, cx + 24, cy + 24], outline=(178, 34, 34), width=3)

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Header
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    d.text((28, 18), "WORLD NEWS", font=TITLE_FONT, fill=WHITE)
    d.text((28, 102), "WEDNESDAY, 25 NOVEMBER 2026", font=DATE_FONT, fill=GOLD)
    d.text((W - 28, 30), "6 STORIES", font=TAG_FONT, fill=WHITE, anchor="ra")
    d.text((W - 28, 58), "FROM AROUND", font=TAG_FONT, fill=WHITE, anchor="ra")
    d.text((W - 28, 86), "THE WORLD", font=TAG_FONT, fill=WHITE, anchor="ra")
    # Grid: 2 cols x 3 rows
    gx, gy, gap = 28, 170, 16
    cw = (W - 2 * gx - gap) // 2
    ch = 252
    for i, (num, tag, head, body, kind) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (cw + gap)
        y = gy + row * (ch + gap)
        accent = ACCENTS[i]
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=14, fill=CARD, outline=(210, 216, 226), width=2)
        d.rounded_rectangle([x, y, x + cw, y + 8], radius=4, fill=accent)
        # number badge + tag
        d.ellipse([x + 16, y + 22, x + 58, y + 64], fill=accent)
        d.text((x + 37, y + 43), num, font=NUM_FONT, fill=WHITE, anchor="mm")
        d.text((x + 70, y + 30), tag, font=TAG_FONT, fill=accent)
        # icon, right of tag line (kept above the headline so it cannot overlap text)
        draw_icon(d, kind, x + cw - 50, y + 46, 30, accent)
        # headline, wrapped to full card width
        lines = wrap(d, head, HEAD_FONT, cw - 32)
        ty = y + 78
        for ln in lines[:2]:
            d.text((x + 16, ty), ln, font=HEAD_FONT, fill=INK)
            ty += 36
        # summary, wrapped
        slines = wrap(d, body, BODY_FONT, cw - 32)
        ty += 6
        for ln in slines[:3]:
            d.text((x + 16, ty), ln, font=BODY_FONT, fill=GREY)
            ty += 29
    # Footer
    fy = 170 + 3 * ch + 2 * gap + 12
    d.text((W // 2, fy + 8), "Sources: Reuters  •  BBC  •  AP  •  Just Security  —  25 Nov 2026",
           font=FOOT_FONT, fill=GREY, anchor="ma")
    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT)

if __name__ == "__main__":
    main()
