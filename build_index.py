import os

logos_row1 = ""
logos_row2 = ""

count = 1
for i in range(1, 58):
    if os.path.exists(f"assets/clients/logos/logo_{i}.png"):
        img_str = f'<img src="assets/clients/logos/logo_{i}.png" alt="Client {i}" class="h-20 w-auto min-w-[150px] object-contain filter grayscale hover:grayscale-0 transition-all duration-300 bg-white p-4 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-1">'
        if count % 2 == 1:
            logos_row1 += img_str
        else:
            logos_row2 += img_str
        count += 1

logos_row1 = logos_row1 * 4
logos_row2 = logos_row2 * 4

html_content = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InfoTech | Business & IT Support Services Provider</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{ 50: '#f0f9ff', 100: '#e0f2fe', 500: '#0ea5e9', 600: '#0284c7', 800: '#075985', 900: '#0f172a' }}
                    }},
                    fontFamily: {{ sans: ['Inter', 'sans-serif'] }}
                }}
            }}
        }}
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .animate-marquee {{ animation: marquee 35s linear infinite; }}
        .animate-marquee-slow {{ animation: marquee 45s linear infinite reverse; }}
        @keyframes marquee {{ 0% {{ transform: translateX(0%); }} 100% {{ transform: translateX(-50%); }} }}
    </style>
</head>
<body class="font-sans antialiased text-gray-800 bg-gray-50 flex flex-col min-h-screen">

    <!-- Header -->
    <nav class="fixed w-full top-0 z-50 bg-white/90 backdrop-blur-md shadow-sm border-b border-gray-100 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-20">
            <a href="index.html" class="flex items-center gap-3">
                <img src="assets/logo.png" alt="InfoTech Logo" class="h-14 w-auto object-contain">
            </a>
            <div class="hidden md:flex items-center space-x-8 font-medium">
                <a href="#home" class="text-gray-900 hover:text-brand-600 transition-colors">Home</a>
                <a href="#about" class="text-gray-600 hover:text-brand-600 transition-colors">About</a>
                <a href="#services" class="text-gray-600 hover:text-brand-600 transition-colors">Services</a>
                <a href="#projects" class="text-gray-600 hover:text-brand-600 transition-colors">Projects</a>
                <a href="#clients" class="text-gray-600 hover:text-brand-600 transition-colors">Clients</a>
                <a href="#contact" class="px-6 py-2.5 bg-brand-600 hover:bg-brand-900 text-white rounded-full transition-all shadow-md hover:shadow-lg">Contact Us</a>
            </div>
        </div>
    </nav>

    <!-- Hero -->
    <section id="home" class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 bg-brand-900 flex items-center min-h-[90vh]">
        <div class="absolute inset-0">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=1920&q=80" alt="Tech Background" class="w-full h-full object-cover opacity-20">
            <div class="absolute inset-0 bg-gradient-to-r from-brand-900 via-brand-900/95 to-transparent"></div>
        </div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
            <div class="max-w-3xl">
                <span class="inline-block px-4 py-1.5 rounded-full bg-brand-500/20 text-brand-100 font-semibold mb-6 border border-brand-500/30">#1 Enterprise IT Solutions</span>
                <h1 class="text-5xl lg:text-7xl font-extrabold text-white leading-tight mb-8 tracking-tight">
                    Business & IT Support <span class="text-brand-500">Services Provider</span>
                </h1>
                <p class="text-xl text-gray-300 mb-10 leading-relaxed max-w-2xl">
                    We help businesses grow with digital solutions, custom software, and highly reliable IT infrastructure tailored for modern enterprises.
                </p>
                <div class="flex flex-wrap gap-4">
                    <a href="#services" class="px-8 py-4 bg-brand-500 hover:bg-brand-600 text-white rounded-full font-bold transition-all shadow-lg flex items-center gap-2 group">
                        Get Started <i class="fas fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
                    </a>
                    <a href="#contact" class="px-8 py-4 border-2 border-white hover:bg-white hover:text-brand-900 text-white rounded-full font-bold transition-all">
                        Contact Us
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- About -->
    <section id="about" class="py-24 bg-white relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col lg:flex-row gap-16 items-center">
                <div class="lg:w-1/2">
                    <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">About InfoTech</h2>
                    <h3 class="text-4xl font-bold text-gray-900 mb-6 leading-tight">Driving Innovation & Quality in Enterprise IT</h3>
                    <p class="text-lg text-gray-600 mb-8 leading-relaxed">
                        InfoTech Computers (Pvt) Ltd is a leading technology partner dedicated to empowering modern businesses. We combine industry-leading expertise with a commitment to quality, innovation, and unwavering reliability to secure and optimize your IT operations.
                    </p>
                    <div class="grid grid-cols-2 gap-6">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center text-xl shrink-0"><i class="fas fa-lightbulb"></i></div>
                            <div>
                                <h4 class="font-bold text-gray-900 mb-1">Creative Ideas</h4>
                                <p class="text-sm text-gray-500">Innovative approaches to technical challenges.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center text-xl shrink-0"><i class="fas fa-gem"></i></div>
                            <div>
                                <h4 class="font-bold text-gray-900 mb-1">High Quality</h4>
                                <p class="text-sm text-gray-500">Premium hardware and software solutions.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center text-xl shrink-0"><i class="fas fa-rocket"></i></div>
                            <div>
                                <h4 class="font-bold text-gray-900 mb-1">Fast Delivery</h4>
                                <p class="text-sm text-gray-500">Rapid deployment and support response.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 rounded-lg bg-brand-50 text-brand-600 flex items-center justify-center text-xl shrink-0"><i class="fas fa-hand-holding-dollar"></i></div>
                            <div>
                                <h4 class="font-bold text-gray-900 mb-1">Value for Money</h4>
                                <p class="text-sm text-gray-500">Cost-effective strategies that scale.</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="lg:w-1/2 relative">
                    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80" alt="About InfoTech" class="rounded-2xl shadow-2xl relative z-10 hover:-translate-y-2 transition-transform duration-500">
                    <div class="absolute -bottom-8 -left-8 w-64 h-64 bg-brand-100 rounded-full mix-blend-multiply filter blur-3xl opacity-70"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services -->
    <section id="services" class="py-24 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">What We Do</h2>
                <h3 class="text-4xl font-bold text-gray-900 mb-6">Comprehensive IT Services</h3>
                <p class="text-gray-600 text-lg">From foundational IT support to full-scale enterprise software and media offerings, we deliver end-to-end digital solutions.</p>
            </div>
            
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- S1 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-code"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Web Development</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">Modern, responsive websites and enterprise portals tailored to your corporate identity.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S2 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-laptop-code"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Software Development</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">Custom POS, ERP, and localized software solutions to automate your business.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S3 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-mobile-alt"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">App Development</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">High-performance iOS and Android applications for your customer base.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S4 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-palette"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Graphic Design</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">Premium branding, corporate identity materials, and digital advertising graphics.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S5 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-share-nodes"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Social Media Management</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">Strategic scheduling, analytics, and targeted campaigns to expand your reach.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S6 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-camera"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Product Photography</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">High-resolution, studio-grade commercial photography showcasing your products.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S7 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-server"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Hardware & Networking</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">Infrastructure design, CCTV, servers, and ongoing corporate IT maintenance.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
                <!-- S8 -->
                <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:-translate-y-2 transition-all group">
                    <div class="w-14 h-14 bg-brand-50 text-brand-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:bg-brand-600 group-hover:text-white transition-colors"><i class="fas fa-file-invoice"></i></div>
                    <h4 class="text-xl font-bold text-gray-900 mb-3">Accounting & Legal</h4>
                    <p class="text-gray-600 text-sm mb-6 leading-relaxed">Consultation and integration for corporate legal filings and accounting systems.</p>
                    <a href="#" class="text-brand-600 font-semibold group-hover:text-brand-800">Learn More &rarr;</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="py-24 bg-brand-900 text-white relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h3 class="text-4xl font-bold mb-6">Why InfoTech is the Right Choice</h3>
                <p class="text-brand-100 text-lg max-w-2xl mx-auto">We back every project with industry expertise and our absolute commitment to client success.</p>
            </div>
            
            <div class="grid md:grid-cols-4 gap-8 text-center">
                <div>
                    <i class="fas fa-users text-5xl text-brand-500 mb-4"></i>
                    <h4 class="text-xl font-bold mb-2">Experienced Team</h4>
                    <p class="text-sm text-gray-400">Certified engineers and specialized developers at your service.</p>
                </div>
                <div>
                    <i class="fas fa-bolt text-5xl text-brand-500 mb-4"></i>
                    <h4 class="text-xl font-bold mb-2">Fast Delivery</h4>
                    <p class="text-sm text-gray-400">Strict adherence to project timelines and milestones.</p>
                </div>
                <div>
                    <i class="fas fa-tags text-5xl text-brand-500 mb-4"></i>
                    <h4 class="text-xl font-bold mb-2">Affordable Pricing</h4>
                    <p class="text-sm text-gray-400">Premium corporate solutions structured for your budget.</p>
                </div>
                <div>
                    <i class="fas fa-heart text-5xl text-brand-500 mb-4"></i>
                    <h4 class="text-xl font-bold mb-2">Customer Satisfaction</h4>
                    <p class="text-sm text-gray-400">Dedicated helpdesk and lasting after-sales support.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects / Portfolio -->
    <section id="projects" class="py-24 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12">
                <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">Portfolio</h2>
                <h3 class="text-4xl font-bold text-gray-900 mb-6">Our Recent Projects</h3>
            </div>
            
            <!-- Filter Tabs -->
            <div class="flex justify-center gap-4 mb-12 overflow-x-auto no-scrollbar py-2">
                <button class="px-6 py-2 rounded-full bg-brand-600 text-white font-medium shadow-md">All</button>
                <button class="px-6 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 font-medium transition-colors">Web</button>
                <button class="px-6 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 font-medium transition-colors">Software</button>
                <button class="px-6 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 font-medium transition-colors">Apps</button>
                <button class="px-6 py-2 rounded-full bg-gray-100 text-gray-600 hover:bg-gray-200 font-medium transition-colors">Design</button>
            </div>
            
            <!-- Gallery Grid -->
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="group relative rounded-2xl overflow-hidden shadow-lg aspect-[4/3] cursor-pointer">
                    <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80" alt="Web Project" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-8">
                        <span class="text-brand-400 text-sm font-bold tracking-wider mb-2">WEB DEVELOPMENT</span>
                        <h4 class="text-white text-2xl font-bold">Corporate Banking Portal</h4>
                    </div>
                </div>
                <div class="group relative rounded-2xl overflow-hidden shadow-lg aspect-[4/3] cursor-pointer">
                    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80" alt="Software Project" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-8">
                        <span class="text-brand-400 text-sm font-bold tracking-wider mb-2">SOFTWARE</span>
                        <h4 class="text-white text-2xl font-bold">Enterprise Analytics Dashboard</h4>
                    </div>
                </div>
                <div class="group relative rounded-2xl overflow-hidden shadow-lg aspect-[4/3] cursor-pointer">
                    <img src="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=800&q=80" alt="App Project" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-brand-900/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end p-8">
                        <span class="text-brand-400 text-sm font-bold tracking-wider mb-2">APP DEVELOPMENT</span>
                        <h4 class="text-white text-2xl font-bold">Retail Ordering Mobile App</h4>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="py-24 bg-gray-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h3 class="text-4xl font-bold text-gray-900 mb-6">What Our Clients Say</h3>
                <p class="text-gray-600 text-lg">Trusted by Sri Lanka's leading enterprises for technical excellence.</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <div class="bg-white p-8 rounded-2xl shadow-md border border-gray-100 relative">
                    <div class="text-brand-500 mb-4 flex gap-1">
                        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                    </div>
                    <p class="text-gray-600 italic mb-6">"InfoTech has completely transformed our corporate IT infrastructure. Their rapid response and software quality are unmatched."</p>
                    <div class="flex flex-col">
                        <span class="font-bold text-gray-900">Saman Kumara</span>
                        <span class="text-sm text-brand-600">Operations Director, MAS</span>
                    </div>
                    <i class="fas fa-quote-right absolute top-8 right-8 text-6xl text-gray-50 opacity-50 -z-0"></i>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-md border border-gray-100 relative">
                    <div class="text-brand-500 mb-4 flex gap-1">
                        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                    </div>
                    <p class="text-gray-600 italic mb-6">"The web development team delivered a perfect corporate portal well ahead of schedule. Highly recommended."</p>
                    <div class="flex flex-col">
                        <span class="font-bold text-gray-900">Nipuni Perera</span>
                        <span class="text-sm text-brand-600">Marketing Head, People's Bank</span>
                    </div>
                    <i class="fas fa-quote-right absolute top-8 right-8 text-6xl text-gray-50 opacity-50 -z-0"></i>
                </div>
                <div class="bg-white p-8 rounded-2xl shadow-md border border-gray-100 relative">
                    <div class="text-brand-500 mb-4 flex gap-1">
                        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                    </div>
                    <p class="text-gray-600 italic mb-6">"Excellent continuous support. Their hardware and network team provides 24/7 reliability for our distribution centers."</p>
                    <div class="flex flex-col">
                        <span class="font-bold text-gray-900">Dinesh Roshan</span>
                        <span class="text-sm text-brand-600">IT Manager, CBL Group</span>
                    </div>
                    <i class="fas fa-quote-right absolute top-8 right-8 text-6xl text-gray-50 opacity-50 -z-0"></i>
                </div>
            </div>
        </div>
    </section>

    <!-- Clients Marquee using Extracted Logos! -->
    <section id="clients" class="py-24 bg-white border-y border-gray-100 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 text-center">
            <h2 class="text-brand-600 font-bold tracking-wider uppercase text-sm mb-3">Who Trusts Us</h2>
            <h3 class="text-3xl md:text-5xl font-bold text-gray-900">Our Prestigious Clientele</h3>
        </div>
        
        <!-- Marquee Rows -->
        <div class="w-full flex flex-col gap-6 [mask-image:_linear-gradient(to_right,transparent_0,_black_128px,_black_calc(100%-128px),transparent_100%)]">
            <div class="flex flex-nowrap items-center gap-6 animate-marquee w-max">
                {logos_row1}
            </div>
            <div class="flex flex-nowrap items-center gap-6 animate-marquee-slow w-max ml-12">
                {logos_row2}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-brand-600 relative overflow-hidden text-center">
        <div class="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMiIgY3k9IjIiIHI9IjEiIGZpbGw9IiNmZmYiIGZpbGwtb3BhY2l0eT0iMC4xIi8+PC9zdmc+')]"></div>
        <div class="max-w-3xl mx-auto px-4 relative z-10">
            <h3 class="text-4xl md:text-5xl font-bold text-white mb-8">Ready to grow your business?</h3>
            <a href="#contact" class="inline-flex px-10 py-5 bg-white text-brand-900 rounded-full font-bold text-lg hover:bg-gray-100 transition-colors shadow-2xl hover:-translate-y-1">
                Contact Us Today
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer id="contact" class="bg-gray-900 text-white pt-20 pb-10 border-t-4 border-brand-500 uppercase tracking-wide">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12 normal-case tracking-normal">
                <div>
                    <img src="assets/logo.png" alt="InfoTech Logo" class="h-14 bg-white p-2 rounded-lg mb-6 w-auto">
                    <p class="text-gray-400 mb-6">The trusted technology partner for modern corporations. Securing and optimizing your IT infrastructure with comprehensive digital solutions.</p>
                    <div class="flex gap-4">
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center text-gray-400 hover:bg-brand-500 hover:text-white transition-colors"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center text-gray-400 hover:bg-brand-500 hover:text-white transition-colors"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center text-gray-400 hover:bg-brand-500 hover:text-white transition-colors"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
                
                <div>
                    <h4 class="font-bold text-lg mb-6 uppercase tracking-wider">Quick Links</h4>
                    <ul class="space-y-3 text-gray-400">
                        <li><a href="#home" class="hover:text-brand-400 transition-colors">Home</a></li>
                        <li><a href="#about" class="hover:text-brand-400 transition-colors">About Us</a></li>
                        <li><a href="#services" class="hover:text-brand-400 transition-colors">Our Services</a></li>
                        <li><a href="#projects" class="hover:text-brand-400 transition-colors">Portfolio</a></li>
                        <li><a href="#clients" class="hover:text-brand-400 transition-colors">Clients</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-bold text-lg mb-6 uppercase tracking-wider">Services</h4>
                    <ul class="space-y-3 text-gray-400">
                        <li><a href="#" class="hover:text-brand-400 transition-colors">Software Development</a></li>
                        <li><a href="#" class="hover:text-brand-400 transition-colors">Web & App Design</a></li>
                        <li><a href="#" class="hover:text-brand-400 transition-colors">Hardware & Networking</a></li>
                        <li><a href="#" class="hover:text-brand-400 transition-colors">Social Media Management</a></li>
                        <li><a href="#" class="hover:text-brand-400 transition-colors">Accounting & Legal IT</a></li>
                    </ul>
                </div>
                
                <div>
                    <h4 class="font-bold text-lg mb-6 uppercase tracking-wider">Contact Info</h4>
                    <ul class="space-y-4 text-gray-400">
                        <li class="flex items-start gap-3">
                            <i class="fas fa-map-marker-alt text-brand-500 mt-1"></i> 
                            <span>No. 801, 4th Floor, Sausiri Shopping Complex, High Level Road, Nugegoda</span>
                        </li>
                        <li class="flex items-center gap-3">
                            <i class="fas fa-phone text-brand-500"></i> +94 11 219 9446
                        </li>
                        <li class="flex items-center gap-3">
                            <i class="fas fa-envelope text-brand-500"></i> info@infotechcomputers.lk
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-gray-500 text-sm normal-case tracking-normal">
                <p>&copy; 2026 InfoTech Computers (Pvt) Ltd. All rights reserved.</p>
                <div class="flex gap-4 mt-4 md:mt-0">
                    <a href="#" class="hover:text-white transition-colors">Privacy Policy</a>
                    <a href="#" class="hover:text-white transition-colors">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html fully rebuilt!")
