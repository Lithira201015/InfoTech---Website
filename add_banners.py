import sys, re

banners = {
    'about.html': 'About Us',
    'services.html': 'Products & Services',
    'clients.html': 'Our Clientele',
    'contact.html': 'Contact Us'
}

for file, title in banners.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    banner_html = f'''
    <!-- Subpage Banner -->
    <section class="pt-32 pb-16 bg-brand-900 text-center relative overflow-hidden">
        <div class="absolute inset-0 bg-[url(\'https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80\')] bg-cover bg-center opacity-10"></div>
        <div class="max-w-7xl mx-auto px-4 relative z-10">
            <h1 class="text-4xl md:text-5xl font-bold text-white tracking-tight">{title}</h1>
            <p class="mt-4 text-brand-100 text-lg">InfoTech Computers (Private) Limited</p>
        </div>
    </section>'''
    content = re.sub(r'(</nav>)', r'\1\n' + banner_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Banners added")
