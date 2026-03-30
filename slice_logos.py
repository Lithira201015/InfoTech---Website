import os
from PIL import Image

output_dir = "assets/clients/logos"
os.makedirs(output_dir, exist_ok=True)

groups = [
    ("assets/clients/group1.png", 5, 4),
    ("assets/clients/group2.png", 5, 4),
    ("assets/clients/group3.png", 5, 4),
]

count = 1
valid_logos = []

for file, cols, rows in groups:
    img = Image.open(file)
    w, h = img.size
    
    cell_w = w / cols
    cell_h = h / rows
    
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_w
            y1 = row * cell_h
            x2 = x1 + cell_w
            y2 = y1 + cell_h
            
            box = (int(x1), int(y1), int(x2), int(y2))
            cropped = img.crop(box)
            
            # check if it's practically blank (white)
            grayscale = cropped.convert("L")
            extrema = grayscale.getextrema()
            # If the min pixel and max pixel are very close to 255, it's blank white
            if extrema[0] >= 250 and extrema[1] >= 250:
                continue
                
            out_file = f"{output_dir}/logo_{count}.png"
            if cropped.mode != 'RGBA':
                cropped = cropped.convert('RGBA')
            cropped.save(out_file)
            valid_logos.append(f"logo_{count}.png")
            count += 1

print(f"Generated {len(valid_logos)} logos.")
