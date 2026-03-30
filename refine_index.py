import os, re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove Projects links
content = re.sub(r'<a href="#projects" class="[^"]+">Projects</a>\s*', '', content)
content = re.sub(r'<li><a href="#projects" class="[^"]+">Portfolio</a></li>\s*', '', content)

# Remove Projects Section
content = re.sub(r'<!-- Projects / Portfolio -->\s*<section id="projects".*?(?=<!-- Testimonials -->)', '', content, flags=re.DOTALL)

# Rebuild Services
services_html = '''    <!-- Services Section -->
    <section id="services" class="py-24 bg-gray-50 relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">Our Expertise</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-gray-900 mb-6 tracking-tight">Products & Services</h3>
                <p class="text-lg text-gray-600 leading-relaxed">We provide end-to-end technology solutions designed to boost productivity, enhance security, and scale with your business.</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Service 1 -->
                <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 border border-gray-100 flex flex-col">
                    <div class="relative h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="IT Infrastructure Design" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 text-white text-3xl">
                            <i class="fas fa-server drop-shadow-lg"></i>
                        </div>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <h4 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-600 transition-colors">IT Infrastructure Design & Management</h4>
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">Design, implementation, and ongoing management of reliable IT infrastructure environments tailored to business needs.</p>
                        <a href="#contact" class="mt-auto inline-flex items-center text-brand-600 font-medium hover:text-brand-800 transition-colors">
                            Explore Service <i class="fas fa-arrow-right ml-2 text-xs transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Service 2 -->
                <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 border border-gray-100 flex flex-col">
                    <div class="relative h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Helpdesk Services" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 text-white text-3xl">
                            <i class="fas fa-headset drop-shadow-lg"></i>
                        </div>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <h4 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-600 transition-colors">IT Outsourcing & Helpdesk Services</h4>
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">End-to-end IT outsourcing, including helpdesk operations, system monitoring, and continuous technical support.</p>
                        <a href="#contact" class="mt-auto inline-flex items-center text-brand-600 font-medium hover:text-brand-800 transition-colors">
                            Explore Service <i class="fas fa-arrow-right ml-2 text-xs transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 border border-gray-100 flex flex-col">
                    <div class="relative h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1531297172867-4f4013628f18?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Equipment Sales" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 text-white text-3xl">
                            <i class="fas fa-desktop drop-shadow-lg"></i>
                        </div>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <h4 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-600 transition-colors">IT Equipment Sales</h4>
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">Supply of branded desktops, laptops, printers, copiers, UPS systems, and enterprise-grade IT accessories.</p>
                        <a href="#contact" class="mt-auto inline-flex items-center text-brand-600 font-medium hover:text-brand-800 transition-colors">
                            Explore Service <i class="fas fa-arrow-right ml-2 text-xs transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Service 4 -->
                <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 border border-gray-100 flex flex-col">
                    <div class="relative h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Equipment Rental" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 text-white text-3xl">
                            <i class="fas fa-laptop-house drop-shadow-lg"></i>
                        </div>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <h4 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-600 transition-colors">IT Equipment Rental Services</h4>
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">Flexible short-term and long-term rental solutions for PCs, laptops, printers, copiers, UPS systems, and event-based requirements.</p>
                        <a href="#contact" class="mt-auto inline-flex items-center text-brand-600 font-medium hover:text-brand-800 transition-colors">
                            Explore Service <i class="fas fa-arrow-right ml-2 text-xs transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Service 5 -->
                <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 border border-gray-100 flex flex-col">
                    <div class="relative h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1581092160562-40aa08e78837?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Repairs & AMC" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 text-white text-3xl">
                            <i class="fas fa-screwdriver-wrench drop-shadow-lg"></i>
                        </div>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <h4 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-600 transition-colors">Repairs, Maintenance & AMC Services</h4>
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">Preventive and corrective maintenance through Annual Maintenance Contracts to ensure system reliability and minimal downtime.</p>
                        <a href="#contact" class="mt-auto inline-flex items-center text-brand-600 font-medium hover:text-brand-800 transition-colors">
                            Explore Service <i class="fas fa-arrow-right ml-2 text-xs transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- Service 6 -->
                <div class="group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all duration-300 border border-gray-100 flex flex-col">
                    <div class="relative h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1557597774-9d273605dfa9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Security Solutions" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-brand-900/40 to-transparent"></div>
                        <div class="absolute bottom-4 left-6 text-white text-3xl">
                            <i class="fas fa-shield-halved drop-shadow-lg"></i>
                        </div>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <h4 class="text-xl font-bold text-gray-900 mb-3 group-hover:text-brand-600 transition-colors">Network, CCTV & Security Solutions</h4>
                        <p class="text-gray-600 text-sm leading-relaxed mb-6">Design and implementation of secure networking, structured cabling, CCTV surveillance, and access control systems.</p>
                        <a href="#contact" class="mt-auto inline-flex items-center text-brand-600 font-medium hover:text-brand-800 transition-colors">
                            Explore Service <i class="fas fa-arrow-right ml-2 text-xs transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>'''
content = re.sub(r'<!-- Services -->.*?(?=<!-- Why Choose Us -->)', services_html + '\n\n', content, flags=re.DOTALL)

# Rebuild clients
client_domains = [
    "peoplesbank.lk", "masholdings.com", "muncheelk.com", "jatholdings.com", 
    "accessengsl.com", "gallefacehotel.com", "godrej.com", "softlogic.lk", 
    "lionbeer.com", "pizzahut.lk", "tacobell.lk", "aia.com", "malibanbiscuit.com",
    "bureauveritas.com", "cic.lk", "brandix.com", "hemas.com", "keells.com", "dialog.lk", "mobitel.lk"
]

marquee_images = ""
for d in client_domains:
    # Adding a white container for the colored logo, adjusting size.
    marquee_images += f'<div class="bg-white rounded-xl shadow-md border border-gray-100 p-6 w-56 h-32 flex items-center justify-center shrink-0 hover:-translate-y-1 hover:shadow-lg transition-all"><img src="https://logo.clearbit.com/{d}?size=150" alt="Client Logo" class="max-w-full max-h-full object-contain" onerror="this.parentElement.style.display=\'none\'"></div>\n'

# Make it extremely long so it animates reliably.
repeated_images = marquee_images * 8

marquee_html = f'''    <!-- Clients Marquee using High-Res Web Logos -->
    <section id="clients" class="py-24 bg-white border-y border-gray-100 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 text-center">
            <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">Who Trusts Us</h2>
            <h3 class="text-3xl md:text-5xl font-bold text-gray-900">Our Prestigious Clientele</h3>
        </div>
        
        <!-- Slow Marquee Row -->
        <div class="w-full flex-nowrap overflow-hidden [mask-image:_linear-gradient(to_right,transparent_0,_black_128px,_black_calc(100%-128px),transparent_100%)] relative z-10 py-6">
            <div class="flex items-center gap-8 animate-marquee-slower w-max">
{repeated_images}
            </div>
        </div>
    </section>'''

content = re.sub(r'<!-- Clients Marquee.*?(?=<!-- CTA -->)', marquee_html + '\n\n', content, flags=re.DOTALL)

# Inject the slow marquee CSS class
if '.animate-marquee-slower' not in content:
    content = re.sub(r'(</style>)', r'        .animate-marquee-slower { animation: marquee 120s linear infinite; }\n    \1', content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("done")
