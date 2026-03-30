import os
from PIL import Image, ImageChops

output_dir = "assets/clients/optimized_logos"
os.makedirs(output_dir, exist_ok=True)

groups = [
    ("assets/clients/group1.png", 5, 4),
    ("assets/clients/group2.png", 5, 4),
    ("assets/clients/group3.png", 5, 4),
]

def autocrop_image(image):
    bg = Image.new(image.mode, image.size, (255, 255, 255))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)
    return image

count = 1
valid = 0
for file, cols, rows in groups:
    if not os.path.exists(file):
        continue
    img = Image.open(file).convert('RGB')
    w, h = img.size
    
    cell_w = w / cols
    cell_h = h / rows
    
    for row in range(rows):
        for col in range(cols):
            x1 = int(col * cell_w)
            y1 = int(row * cell_h)
            x2 = int(x1 + cell_w)
            y2 = int(y1 + cell_h)
            
            cell = img.crop((x1, y1, x2, y2))
            cw, ch = cell.size
            
            pad_x = int(cw * 0.1)
            pad_y = int(ch * 0.1)
            bottom_crop = int(ch * 0.25)
            
            inner_box = (pad_x, pad_y, cw - pad_x, ch - bottom_crop)
            try:
                logo_region = cell.crop(inner_box)
                cropped_logo = autocrop_image(logo_region)
                
                if cropped_logo.width < 10 or cropped_logo.height < 10:
                    continue
                    
                extrema = cropped_logo.convert("L").getextrema()
                if extrema[0] >= 245 and extrema[1] >= 245:
                    continue
                    
                final_w = cropped_logo.width + 20
                final_h = cropped_logo.height + 20
                final_img = Image.new("RGBA", (final_w, final_h), (255, 255, 255, 0))
                
                logo_rgba = cropped_logo.convert("RGBA")
                final_img.paste(logo_rgba, (10, 10))
                
                out_path = f"{output_dir}/logo_{count}.png"
                final_img.save(out_path)
                valid += 1
                count += 1
            except Exception as e:
                pass

print(f"Optimized {valid} logos.")
