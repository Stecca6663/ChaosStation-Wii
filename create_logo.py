"""
Create a 'New Super Mario Bros. Wii : Chaos Station' title logo.
Designed to be 630x260 pixels (same as original) with RGBA transparency.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math
import random


def create_chaos_station_logo(output_path='title_logo.png'):
    W, H = 630, 260
    
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Find bold system fonts
    font_paths = [
        "C:/Windows/Fonts/impact.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/trebucbd.ttf",
    ]
    
    font_title = None
    font_main = None
    
    for fp in font_paths:
        if os.path.exists(fp):
            font_title = ImageFont.truetype(fp, 36)  # "NEW SUPER MARIO BROS. WII"
            font_main = ImageFont.truetype(fp, 80)   # "CHAOS STATION"
            break
    
    if font_title is None:
        font_title = font_main = ImageFont.load_default()
    
    # Colors
    RED = (220, 30, 30)
    RED_DARK = (140, 10, 10)
    ORANGE = (255, 140, 0)
    YELLOW = (255, 220, 40)
    GOLD = (255, 200, 0)
    WHITE = (255, 255, 255)
    SHADOW = (80, 20, 20)
    
    center_x = W // 2
    
    def draw_text_with_outline(draw, pos, text, fill, outline, font, outline_width=2):
        x, y = pos
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if abs(dx) + abs(dy) <= outline_width:
                    draw.text((x + dx, y + dy), text, fill=outline, font=font)
        draw.text((x, y), text, fill=fill, font=font)
    
    def draw_star(draw, cx, cy, r_outer, r_inner, fill, n=5):
        points = []
        for i in range(n * 2):
            angle = math.pi / 2 + i * math.pi / n
            r = r_outer if i % 2 == 0 else r_inner
            px = cx + int(r * math.cos(angle))
            py = cy - int(r * math.sin(angle))
            points.append((px, py))
        draw.polygon(points, fill=fill)
    
    # === LINE 1: "NEW SUPER MARIO BROS. WII" ===
    title_text = "NEW SUPER MARIO BROS. WII"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_w = bbox[2] - bbox[0]
    title_h = bbox[3] - bbox[1]
    title_x = center_x - title_w // 2
    title_y = 10
    
    draw_text_with_outline(draw, (title_x, title_y), title_text, WHITE, RED_DARK, font_title, 2)
    
    # === LINE 2: "CHAOS STATION" ===
    main_text = "CHAOS STATION"
    bbox2 = draw.textbbox((0, 0), main_text, font=font_main)
    main_w = bbox2[2] - bbox2[0]
    main_h = bbox2[3] - bbox2[1]
    main_x = center_x - main_w // 2
    main_y = title_y + title_h + 20
    
    # Shadow
    draw.text((main_x + 3, main_y + 3), main_text, fill=SHADOW, font=font_main)
    
    # Outline
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx) + abs(dy) > 0 and abs(dx) + abs(dy) <= 2:
                draw.text((main_x + dx, main_y + dy), main_text, fill=RED_DARK, font=font_main)
    
    # Base fill: "CHAOS" in red, "STATION" in gold
    draw.text((main_x, main_y), "CHAOS", fill=RED, font=font_main)
    
    chaos_bbox = draw.textbbox((0, 0), "CHAOS", font=font_main)
    chaos_w = chaos_bbox[2] - chaos_bbox[0]
    station_x = main_x + chaos_w + 5
    draw.text((station_x, main_y), "STATION", fill=GOLD, font=font_main)
    
    # Gradient overlay on CHAOS (red -> orange, top -> bottom)
    for y in range(main_y, main_y + main_h):
        ratio = (y - main_y) / main_h
        for x in range(main_x, main_x + chaos_w):
            if 0 <= x < W and 0 <= y < H:
                r, g, b, a = img.getpixel((x, y))
                if a > 100 and r > 150:
                    nr = min(255, int(r + 40 * ratio))
                    ng = min(255, int(g + 70 * ratio))
                    img.putpixel((x, y), (nr, ng, b, a))
    
    # Highlight on top of CHAOS
    for y in range(main_y, main_y + main_h // 3):
        fade = max(0, 1 - (y - main_y) / (main_h * 0.35))
        for x in range(main_x, main_x + chaos_w):
            if 0 <= x < W and 0 <= y < H:
                r, g, b, a = img.getpixel((x, y))
                if a > 100:
                    nr = min(255, int(r + 80 * fade))
                    ng = min(255, int(g + 60 * fade))
                    nb = min(255, int(b + 50 * fade))
                    img.putpixel((x, y), (nr, ng, nb, a))
    
    # Highlight on top of STATION
    for y in range(main_y, main_y + main_h // 3):
        fade = max(0, 1 - (y - main_y) / (main_h * 0.35))
        for x in range(station_x, station_x + main_w):
            if 0 <= x < W and 0 <= y < H:
                r, g, b, a = img.getpixel((x, y))
                if a > 100:
                    nr = min(255, int(r + 60 * fade))
                    ng = min(255, int(g + 60 * fade))
                    img.putpixel((x, y), (nr, ng, b, a))
    
    draw = ImageDraw.Draw(img)
    
    # === DECORATIONS ===
    
    # Stars
    draw_star(draw, main_x - 20, main_y + 40, 14, 6, GOLD)
    draw_star(draw, main_x + main_w + 25, main_y + 50, 12, 5, GOLD)
    draw_star(draw, title_x - 15, title_y + 18, 10, 4, YELLOW)
    draw_star(draw, title_x + title_w + 15, title_y + 18, 10, 4, YELLOW)
    
    # Underline swoosh
    swoosh_y = main_y + main_h + 15
    for i in range(400):
        t = i / 400.0
        x = int(115 + t * 400)
        y = int(swoosh_y + 8 * (1 - (2*t - 1)**2))
        color_t = t
        r = int(255 * (1 - color_t) + 200 * color_t)
        g = int(150 * (1 - color_t) + 30 * color_t)
        b = int(0 + 20 * color_t)
        for w in range(3):
            if 0 <= x < W and 0 <= y + w < H:
                img.putpixel((x, y + w), (r, g, b, 255))
    
    # Sparkle particles
    random.seed(42)
    for _ in range(40):
        px = random.randint(main_x - 20, main_x + main_w + 20)
        py = random.randint(main_y - 15, main_y + main_h + 10)
        pr = random.randint(1, 3)
        color = random.choice([GOLD, YELLOW, ORANGE, WHITE])
        alpha = random.randint(100, 220)
        spark = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(spark).ellipse([px-pr, py-pr, px+pr, py+pr], fill=(*color, alpha))
        img = Image.alpha_composite(img, spark)
    
    img.save(output_path)
    print(f"Logo saved: {output_path} ({W}x{H})")
    return img


if __name__ == '__main__':
    create_chaos_station_logo()
