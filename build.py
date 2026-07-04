import os

src_dir = "stitch_modern_medspa_website"
out_dir = "."

files_to_process = {
    "index.html": os.path.join(src_dir, "smm_med_spa_home", "code.html"),
    "about.html": os.path.join(src_dir, "about_smm_med_spa_expertise_compassion", "code.html"),
    "services.html": os.path.join(src_dir, "our_services_precision_aesthetics", "code.html"),
    "consultation.html": os.path.join(src_dir, "request_a_consultation_smm_med_spa", "code.html")
}

# The hero section CSS to inject
hero_css = """
    <style>
    #scroll-container { height: 8000px; width: 100%; position: relative; }
    #sticky-viewport { position: sticky; top: 0; width: 100%; height: 100vh; overflow: hidden; }
    #loading-screen { position: absolute; inset: 0; z-index: 50; display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: #000; transition: opacity 0.5s; }
    #hero-image { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; object-position: center; }
    .hero-overlay { position: absolute; inset: 0; z-index: 1; background: linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0) 35%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.55) 100%); pointer-events: none; }
    .hero-section { position: absolute; inset: 0; z-index: 10; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0 24px; opacity: 0; pointer-events: none; transform: translateY(40px); transition: opacity 0.1s, transform 0.1s; }
    .hero-section h1 { font-size: clamp(40px, 8vw, 100px); font-weight: 200; line-height: 1.1; margin: 0; text-shadow: 0 2px 20px rgba(0,0,0,0.5); color: #fff; font-family: 'Libre Caslon Text', serif; }
    .hero-section p { color: rgba(255,255,255,0.7); font-size: 14px; letter-spacing: 0.4em; text-transform: uppercase; margin-bottom: 12px; }
    .hero-section .subtitle { color: rgba(255,255,255,0.6); font-size: clamp(14px, 1.5vw, 18px); font-weight: 300; max-width: 480px; letter-spacing: normal; text-transform: none; margin-top: 28px; }
    .hero-divider { width: 60px; height: 1px; background-color: rgba(255,255,255,0.4); margin: 28px 0; }
    .hero-btn { padding: 14px 40px; border: 1px solid rgba(255,255,255,0.6); background-color: rgba(255,255,255,0.05); color: #fff; font-size: 13px; letter-spacing: 0.25em; text-transform: uppercase; cursor: pointer; backdrop-filter: blur(8px); transition: all 0.4s ease; margin-top: 36px; }
    .hero-btn:hover { background-color: #fff; color: #000; }
    #scroll-indicator { position: absolute; bottom: 32px; left: 50%; transform: translateX(-50%); z-index: 10; display: flex; flex-direction: column; align-items: center; pointer-events: none; }
    @keyframes scrollPulse { 0%, 100% { transform: translateY(0); opacity: 0.3; } 50% { transform: translateY(14px); opacity: 1; } }
    .scroll-track { width: 1px; height: 28px; background-color: rgba(255,255,255,0.3); margin-top: 10px; }
    .scroll-thumb { width: 100%; height: 50%; background-color: rgba(255,255,255,0.7); animation: scrollPulse 1.5s ease-in-out infinite; }
    </style>
"""

hero_html = """
<!-- Hero Section (Scroll Animation) -->
<div id="scroll-container">
  <div id="sticky-viewport">
    
    <div id="loading-screen">
      <div style="color: rgba(255,255,255,0.5); font-size: 12px; letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 24px; font-family: sans-serif;">
        Loading Experience
      </div>
      <div style="width: 200px; height: 2px; background-color: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden;">
        <div id="loading-bar" style="height: 100%; width: 0%; background-color: rgba(255,255,255,0.7); transition: width 0.3s ease-out;"></div>
      </div>
      <div id="loading-text" style="color: rgba(255,255,255,0.35); font-size: 11px; margin-top: 12px; letter-spacing: 0.2em; font-family: sans-serif;">
        0%
      </div>
    </div>

    <img id="hero-image" src="" alt="">
    <div class="hero-overlay"></div>

    <!-- Section 1 -->
    <div class="hero-section" id="sec-1">
      <p>Welcome to</p>
      <h1>SSM Health</h1>
      <h2 style="color: rgba(255,255,255,0.8); font-size: clamp(20px, 3.5vw, 42px); font-weight: 300; margin: 4px 0 0; text-shadow: 0 2px 10px rgba(0,0,0,0.4); font-family: 'Libre Caslon Text', serif;">Medical Spa</h2>
      <div class="hero-divider"></div>
      <div class="subtitle">Where modern science meets timeless beauty</div>
    </div>

    <!-- Section 2 -->
    <div class="hero-section" id="sec-2">
      <p>Our Expertise</p>
      <h1>Advanced Aesthetics</h1>
      <div class="hero-divider"></div>
      <div class="subtitle">Precision treatments tailored to your unique natural beauty</div>
    </div>

    <!-- Section 3 -->
    <div class="hero-section" id="sec-3">
      <p>Begin Your Journey</p>
      <h1>Step Inside</h1>
      <div class="hero-divider"></div>
      <div class="subtitle">Experience world-class care in an environment of absolute tranquility</div>
      <button class="hero-btn" onclick="window.location.href='consultation.html'">Book a Consultation</button>
    </div>

    <!-- Scroll Indicator -->
    <div id="scroll-indicator">
      <div style="color: rgba(255,255,255,0.45); font-size: 11px; letter-spacing: 0.3em; text-transform: uppercase;">Scroll to explore</div>
      <div class="scroll-track">
        <div class="scroll-thumb"></div>
      </div>
    </div>

  </div>
</div>

<script>
  const FRAME_COUNT = 240;
  const framePaths = [];
  for (let i = 1; i <= FRAME_COUNT; i++) {
    framePaths.push(`frames/ezgif-170fe61aa28c72d3-jpg/ezgif-frame-${i.toString().padStart(3, "0")}.jpg`);
  }

  const imgRef = document.getElementById('hero-image');
  const loadingScreen = document.getElementById('loading-screen');
  const loadingBar = document.getElementById('loading-bar');
  const loadingText = document.getElementById('loading-text');
  const container = document.getElementById('scroll-container');
  const scrollIndicator = document.getElementById('scroll-indicator');

  const sections = [
    { el: document.getElementById('sec-1'), startFade: 0.0, startFull: 0.06, endFull: 0.2, endFade: 0.3 },
    { el: document.getElementById('sec-2'), startFade: 0.34, startFull: 0.4, endFull: 0.55, endFade: 0.65 },
    { el: document.getElementById('sec-3'), startFade: 0.68, startFull: 0.75, endFull: 0.92, endFade: 1.0 }
  ];

  let images = new Array(FRAME_COUNT);
  let loadedCount = 0;
  let isLoaded = false;
  let currentFrame = 0;
  let rafId = 0;

  for (let i = 0; i < FRAME_COUNT; i++) {
    const img = new Image();
    img.src = framePaths[i];
    img.onload = () => { loadedCount++; updateLoading(); };
    img.onerror = () => { loadedCount++; updateLoading(); };
    images[i] = img;
  }

  function updateLoading() {
    const progress = Math.round((loadedCount / FRAME_COUNT) * 100);
    if(loadingBar) loadingBar.style.width = `${progress}%`;
    if(loadingText) loadingText.innerText = `${progress}%`;
    if (loadedCount === FRAME_COUNT) {
      isLoaded = true;
      setTimeout(() => {
        if(loadingScreen) loadingScreen.style.opacity = '0';
        setTimeout(() => { if(loadingScreen) loadingScreen.style.display = 'none'; }, 500);
      }, 200);
      if(images[0]) imgRef.src = images[0].src;
      onScroll();
    }
  }

  function updateSections(p) {
    sections.forEach(sec => {
      if(!sec.el) return;
      let opacity = 0;
      let ty = 40;
      if (p >= sec.startFade && p < sec.startFull) {
        const t = (p - sec.startFade) / (sec.startFull - sec.startFade);
        opacity = t; ty = 40 * (1 - t);
      } else if (p >= sec.startFull && p <= sec.endFull) {
        opacity = 1; ty = 0;
      } else if (p > sec.endFull && p <= sec.endFade) {
        const t = (p - sec.endFull) / (sec.endFade - sec.endFull);
        opacity = 1 - t; ty = -20 * t;
      }
      sec.el.style.opacity = opacity;
      sec.el.style.transform = `translateY(${ty}px)`;
      sec.el.style.pointerEvents = opacity > 0.1 ? 'auto' : 'none';
    });
    if(scrollIndicator) scrollIndicator.style.opacity = Math.max(0, 1 - p * 10);
  }

  function onScroll() {
    if(!container) return;
    if (rafId) cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(() => {
      const rect = container.getBoundingClientRect();
      const scrollable = rect.height - window.innerHeight;
      const scrolled = -rect.top;
      let progress = Math.max(0, Math.min(1, scrolled / scrollable));
      
      if (isLoaded) {
        const frameIndex = Math.round(progress * (FRAME_COUNT - 1));
        if (frameIndex !== currentFrame) {
          currentFrame = frameIndex;
          if (images[currentFrame] && images[currentFrame].complete) {
            imgRef.src = images[currentFrame].src;
          }
        }
      }
      updateSections(progress);
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
</script>
"""

import re

for output_name, input_path in files_to_process.items():
    if not os.path.exists(input_path):
        print(f"Skipping {output_name}, source not found at {input_path}")
        continue
    
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update navigation links
    content = re.sub(r'<a[^>]*href="#"[^>]*>Face</a>\s*', '', content)
    content = re.sub(r'<a[^>]*href="#"[^>]*>Body</a>\s*', '', content)
    content = re.sub(r'<a[^>]*href="#"[^>]*>Injectables', '<a href="services.html">Injectables', content)
    content = re.sub(r'href="#"[^>]*>About Us', 'href="about.html">About Us', content)
    content = re.sub(r'href="#"[^>]*>Consultation', 'href="consultation.html">Consultation', content)
    
    # Update Request Consultation buttons
    content = content.replace('href="#consultation-form"', 'href="consultation.html"')
    content = content.replace('<button class="bg-deep-plum', '<button onclick="window.location.href=\\\'consultation.html\\\'" class="bg-deep-plum')
    
    # Also update 'SMM Med Spa' nav logo link if it has a #
    content = content.replace('href="#">\n                SMM Med Spa', 'href="index.html">\n                SMM Med Spa')
    content = content.replace('href="/">\n                SMM Med Spa', 'href="index.html">\n                SMM Med Spa')

    # Remove mobile numbers
    content = re.sub(r'<a[^>]*href="tel:[^>]*>[^<]*</a>\s*', '', content)
    content = re.sub(r'Phone: \(210\) 942-6672(?:<br/>)?', '', content)
    content = re.sub(r'<p[^>]*>\(210\) 942-6672</p>\s*', '', content)

    # Remove phone number inputs from forms
    phone_input_regex_1 = r'<div class="space-y-2">\s*<label[^>]*>Phone Number\*</label>\s*<input[^>]*type="tel"/>\s*</div>'
    content = re.sub(phone_input_regex_1, '', content)
    
    phone_input_regex_2 = r'<div class="group">\s*<label[^>]*>Phone Number\*</label>\s*<input[^>]*type="tel"/>\s*</div>'
    content = re.sub(phone_input_regex_2, '', content)

    # Keep all procedure cards in index.html and services.html
    # (Removed previous regex substitutions that stripped Face and Body)
    
    if output_name == "index.html":
        # Inject CSS
        content = content.replace('</head>', hero_css + '\n</head>')
        
        # Replace hero section
        # The hero section in smm_med_spa_home starts with <header class="relative min-h-screen flex items-center pt-20 overflow-hidden">
        # and ends with </header>
        
        start_idx = content.find('<!-- Hero Section -->')
        end_idx = content.find('<!-- Procedure Grid Section -->')
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + hero_html + '\n' + content[end_idx:]
    
    with open(os.path.join(out_dir, output_name), 'w', encoding='utf-8') as f:
        f.write(content)

print("Build complete.")
