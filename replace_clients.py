import sys, re

files = ['index.html', 'clients.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_html = r'''<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 pb-16">
            <div class="flex flex-col gap-12 sm:gap-16 items-center">
                <div class="w-full bg-white rounded-2xl md:rounded-[2rem] p-6 shadow-xl shadow-brand-900/5 border border-brand-100/50 hover:shadow-2xl transition-all duration-300">
                    <img src="assets/clients/group1.png" alt="Corporate Clients Group 1" class="w-full h-auto object-contain mix-blend-multiply">
                </div>
                <div class="w-full bg-white rounded-2xl md:rounded-[2rem] p-6 shadow-xl shadow-brand-900/5 border border-brand-100/50 hover:shadow-2xl transition-all duration-300">
                    <img src="assets/clients/group2.png" alt="Corporate Clients Group 2" class="w-full h-auto object-contain mix-blend-multiply">
                </div>
                <div class="w-full bg-white rounded-2xl md:rounded-[2rem] p-6 shadow-xl shadow-brand-900/5 border border-brand-100/50 hover:shadow-2xl transition-all duration-300">
                    <img src="assets/clients/group3.png" alt="Corporate Clients Group 3" class="w-full h-auto object-contain mix-blend-multiply">
                </div>
            </div>
        </div>'''
        
    pattern = r'<div class="w-full inline-flex flex-col gap-6 overflow-hidden \[mask-image:_linear-gradient.*?</div>\s*</div>\s*</div>'
    content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("done")
