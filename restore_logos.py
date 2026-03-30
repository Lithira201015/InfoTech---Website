import os, re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

logos_row1 = ""
logos_row2 = ""

count = 1
for i in range(1, 58):
    if os.path.exists(f"assets/clients/logos/logo_{i}.png"):
        img_str = f'<div class="bg-white rounded-xl shadow-md border border-gray-100 p-4 w-48 h-24 flex items-center justify-center shrink-0 hover:-translate-y-1 hover:shadow-lg transition-all"><img src="assets/clients/logos/logo_{i}.png" alt="Client Logo" class="max-w-full max-h-full object-contain mix-blend-multiply"></div>\n'
        if count % 2 == 1:
            logos_row1 += img_str
        else:
            logos_row2 += img_str
        count += 1

logos_row1 = logos_row1 * 6
logos_row2 = logos_row2 * 6

marquee_html = f'''    <!-- Clients Marquee using Local High-Res Color Logos -->
    <section id="clients" class="py-24 bg-white border-y border-gray-100 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 text-center">
            <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">Who Trusts Us</h2>
            <h3 class="text-3xl md:text-5xl font-bold text-gray-900">Our Prestigious Clientele</h3>
        </div>
        
        <!-- Slow Marquee Rows -->
        <div class="w-full flex flex-col gap-6 [mask-image:_linear-gradient(to_right,transparent_0,_black_128px,_black_calc(100%-128px),transparent_100%)] relative z-10 py-6">
            <div class="flex items-center gap-8 animate-marquee-slower w-max">
                {logos_row1}
            </div>
            <div class="flex items-center gap-8 pt-4 animate-marquee-slower w-max ml-12" style="animation-direction: reverse;">
                {logos_row2}
            </div>
        </div>
    </section>'''

# Use regex correctly to match the clients section
# From line 323 <!-- Clients Marquee using High-Res Web Logos --> to <!-- CTA -->
content = re.sub(r'<!-- Clients Marquee.*?(?=<!-- CTA -->)', marquee_html + '\n\n', content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"done, processed {count-1} logos")
