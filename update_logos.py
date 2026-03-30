import sys, re

files = ['index.html', 'clients.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    imgs1 = [f'<div class="px-8 py-6 bg-white border border-gray-100 rounded-xl shadow-md flex items-center justify-center min-w-[250px] h-36 hover:shadow-2xl hover:border-brand-300 group transition-all duration-500 overflow-hidden"><img src="assets/clients/client{i}.png" alt="Valued Client" class="max-h-24 max-w-[200px] object-contain filter grayscale opacity-60 group-hover:grayscale-0 group-hover:opacity-100 group-hover:scale-110 transition-all duration-500"></div>' for i in range(1, 6)]
    
    row1_html = '\n                '.join(imgs1 * 3)
    row2_html = '\n                '.join(imgs1[::-1] * 3)
    
    # Replace [&>span] with [&>div] for cleanliness
    content = content.replace('[&>span]:w-max', '[&>div]:w-max')

    pattern1 = r'(<!-- First Row \(moving left\) -->\s*<div class="flex items-center justify-center gap-6 \[\&>div\]:w-max animate-marquee">).*?(</div>\s*<!-- Second Row)'
    content = re.sub(pattern1, r'\1\n                ' + row1_html + r'\n            \2', content, flags=re.DOTALL)
    
    pattern2 = r'(<!-- Second Row -->\s*<div class="flex items-center justify-center gap-6 \[\&>div\]:w-max animate-marquee ml-32">).*?(</div>\s*</div>)'
    content = re.sub(pattern2, r'\1\n                ' + row2_html + r'\n            \2', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Client logos successfully injected!")
