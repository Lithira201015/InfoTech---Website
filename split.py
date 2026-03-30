import sys, re

def modify_file(filepath, sections_to_keep):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = {
        'hero': (r'<!-- Hero Section -->\n', r'    <!-- Why InfoTech Section \(About\) -->'),
        'about': (r'<!-- Why InfoTech Section \(About\) -->\n', r'    <!-- Services Section -->'),
        'services': (r'<!-- Services Section -->\n', r'    <!-- Why Choose Us / Stats -->'),
        'stats': (r'<!-- Why Choose Us / Stats -->\n', r'    <!-- Dedicated Clients Showcase -->'),
        'clients': (r'<!-- Dedicated Clients Showcase -->\n', r'    <!-- Support CTA -->'),
        'cta': (r'<!-- Support CTA -->\n', r'    <!-- Contact & Footer Area -->'),
    }

    for name, (start_tag, end_tag) in sections.items():
        if name not in sections_to_keep:
            pattern = start_tag + r'.*?(?=' + end_tag + r')'
            print(f'Removing {name} from {filepath}')
            content = re.sub(pattern, '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

modify_file('about.html', ['about', 'stats', 'cta'])
modify_file('services.html', ['services', 'cta'])
modify_file('clients.html', ['clients', 'stats', 'cta'])
modify_file('contact.html', ['cta'])
