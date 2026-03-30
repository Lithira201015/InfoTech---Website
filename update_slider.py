import os, re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

logos_row1 = ""
logos_row2 = ""

count = 1
for i in range(1, 61):  # Just scanning up to 60 because some might be skipped
    path = f"assets/clients/optimized_logos/logo_{i}.png"
    if os.path.exists(path):
        img_str = f'<div class="flex-shrink-0 mx-6 md:mx-10 flex items-center justify-center cursor-pointer group h-24 transition-transform duration-300 hover:scale-110"><img src="{path}" alt="Trusted Client" class="h-12 md:h-16 lg:h-[70px] w-auto object-contain filter grayscale group-hover:grayscale-0 transition-all duration-300 drop-shadow-sm"></div>\n'
        if count % 2 == 1:
            logos_row1 += img_str
        else:
            logos_row2 += img_str
        count += 1

logos_row1 = logos_row1 * 6
logos_row2 = logos_row2 * 6

marquee_html = f'''    <!-- Clients Section -->
    <section id="clients" class="py-20 bg-white border-y border-gray-100 overflow-hidden text-center relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
            <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-2">Our Clients</h2>
            <h3 class="text-3xl font-bold text-gray-900">Trusted by leading organizations</h3>
        </div>
        
        <div class="w-full relative [mask-image:_linear-gradient(to_right,transparent_0,_black_128px,_black_calc(100%-128px),transparent_100%)]">
            <div class="flex items-center animate-carousel hover:[animation-play-state:paused] w-max">
                {logos_row1}
            </div>
            
            <div class="flex items-center animate-carousel pt-8 hover:[animation-play-state:paused] w-max ml-20" style="animation-direction: reverse;">
                {logos_row2}
            </div>
        </div>
    </section>'''

# Replace clients section
content = re.sub(r'<!-- Clients Marquee.*?<section id="clients".*?(?=<!-- CTA -->)', marquee_html + '\n\n', content, flags=re.DOTALL)

# Add keyframes for carousel if not present
if '@keyframes carousel' not in content:
    css = '''        .animate-carousel { animation: carousel 60s linear infinite; }
        @keyframes carousel { 0% { transform: translateX(0%); } 100% { transform: translateX(-50%); } }'''
    content = content.replace('</style>', css + '\n    </style>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Slider injected successfully with {count-1} logos")
