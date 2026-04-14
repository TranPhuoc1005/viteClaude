import os
from PIL import Image, ImageOps

target_size = (1920, 960)

images_to_resize = [
    "hero_about_highres_1776149500939.png",
    "software_featured_display_1776013473061.png",
    "trading_course_banner_1776013581136.png",
    "bg_chart_blurred_1776134354009.png",
    "bg_crypto_blurred_1776134339166.png"
]

img_dir = "images"

for img_name in images_to_resize:
    path = os.path.join(img_dir, img_name)
    if os.path.exists(path):
        with Image.open(path) as img:
            print(f"Processing {img_name}: current size {img.size}")
            if img.size != target_size:
                # Resize and crop to exactly 1920x960 with Lanczos high quality resampling
                img_resized = ImageOps.fit(img, target_size, method=Image.Resampling.LANCZOS)
                img_resized.save(path, quality=100)
                print(f"-> Resized output saved to {img_name} as {target_size}")
            else:
                print(f"-> Already {target_size}")
    else:
        print(f"Error: {path} not found")
