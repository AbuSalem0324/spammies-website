"""Generate public/og.jpg from hero sandwich + sign assets."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
bg_path = root / "public/images/hero/hero-sandwich.jpg"
sign_path = root / "public/images/brand/sign-hero.jpg"
out_path = root / "public/og.jpg"

W, H = 1200, 630

bg = Image.open(bg_path).convert("RGB")
bw, bh = bg.size
scale = max(W / bw, H / bh)
nw, nh = int(bw * scale), int(bh * scale)
bg = bg.resize((nw, nh), Image.Resampling.LANCZOS)
left = (nw - W) // 2
top = (nh - H) // 2
bg = bg.crop((left, top, left + W, top + H))

navy = Image.new("RGB", (W, H), (27, 58, 75))
deep = Image.new("RGB", (W, H), (19, 42, 54))
canvas = Image.blend(bg, navy, 0.55)
canvas = Image.blend(canvas, deep, 0.35)

overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
for x in range(0, 720):
    a = int(200 * (1 - x / 720) ** 0.7)
    od.line([(x, 0), (x, H)], fill=(19, 42, 54, a))
canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay)

sign = Image.open(sign_path).convert("RGB")
sw_max, sh_max = 460, 300
s_scale = min(sw_max / sign.width, sh_max / sign.height)
sw, sh = int(sign.width * s_scale), int(sign.height * s_scale)
sign = sign.resize((sw, sh), Image.Resampling.LANCZOS)

pad = 12
frame_w, frame_h = sw + pad * 2, sh + pad * 2
frame = Image.new("RGBA", (frame_w, frame_h), (27, 58, 75, 255))
fd = ImageDraw.Draw(frame)
fd.rectangle([0, 0, frame_w - 1, frame_h - 1], outline=(243, 235, 212, 255), width=3)
frame.paste(sign, (pad, pad))
sx = W - frame_w - 56
sy = (H - frame_h) // 2
canvas.paste(frame, (sx, sy), frame)

draw = ImageDraw.Draw(canvas)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if bold:
        candidates = [
            r"C:\Windows\Fonts\georgiab.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\segoeuib.ttf",
            r"C:\Windows\Fonts\georgia.ttf",
        ]
    else:
        candidates = [
            r"C:\Windows\Fonts\georgia.ttf",
            r"C:\Windows\Fonts\segoeui.ttf",
            r"C:\Windows\Fonts\arial.ttf",
        ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


gold = (232, 200, 74)
cream = (243, 235, 212)
muted = (220, 210, 190)

draw.text((64, 120), "MORLEY  ·  LEEDS  ·  FAMILY-OWNED", font=font(22, bold=True), fill=gold)
draw.text((64, 168), "Spammies", font=font(78, bold=True), fill=gold)
draw.rectangle([64, 256, 280, 260], fill=gold)
draw.text((64, 270), "Proper sandwiches.", font=font(36, bold=True), fill=cream)
draw.text((64, 318), "Proper breakfasts.", font=font(36, bold=True), fill=cream)
draw.text((64, 390), "135 Wide Lane, Morley, Leeds", font=font(24), fill=muted)
draw.text((64, 426), "LS27 8DF", font=font(24), fill=muted)
draw.text((64, 500), "Tel. 07902 771 542", font=font(26, bold=True), fill=gold)

out_rgb = canvas.convert("RGB")
out_rgb.save(out_path, "JPEG", quality=90, optimize=True)
print(f"Wrote {out_path} ({out_path.stat().st_size} bytes) {out_rgb.size}")
