import os

# Read template from services.html
with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract header and footer
main_start = html.find('<main>')
main_end = html.find('</main>') + len('</main>')

header = html[:main_start]
footer = html[main_end:]

services = [
    {
        "id": "lip-flip",
        "title": "Lip Flip",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuCd9mQNT129pizCnrMcJos55LHQ1HJdChAoLImDNDxyf9EcgZjCDzg3hNUBpuDclC1TIvojjozNNZYFBBJYapjA-6QHWFWZe3v-K35CtZRmay9yTkxE4QyeZME0UczFchxkv2yJZ4XjCa8RtyGkJXnD50PSgzNUJHRxI_gIYQ8Mm2T5PnAQ2gynnanTMVHofEWJ1B_rqNgnM1Zr0A61uik5IoMJ70FJKG2Iryf7MRCZylgBFiw85GeScoenldPJ3Rk7jgf7YVYeqD0",
        "content": """
            <h2 class="font-display-lg text-primary mb-4">Effortless Enhancement. Beautifully Natural Results.</h2>
            <p class="font-body-lg text-on-surface-variant mb-8">A <strong>Lip Flip</strong> is a refined, non-surgical treatment designed to enhance your natural smile with subtle elegance. Using Botox® or another FDA-approved neuromodulator, strategically placed injections relax the muscles surrounding the upper lip, allowing it to gently roll outward. The result is the appearance of a fuller, more defined upper lip—without adding volume or dermal filler.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">This treatment is perfect for those who desire a soft, natural enhancement, want to reveal more of their upper lip when smiling, or wish to minimize the appearance of a gummy smile.</p>
            
            <h3 class="font-headline-lg text-deep-plum mb-6">Treatment at a Glance</h3>
            <ul class="list-disc pl-6 space-y-3 font-body-lg text-on-surface-variant mb-12">
                <li><strong>Treatment Time:</strong> Approximately 15 minutes</li>
                <li><strong>Comfort Level:</strong> Quick, minimally invasive, and well tolerated</li>
                <li><strong>Downtime:</strong> Little to none—you can return to most daily activities immediately</li>
                <li><strong>Results:</strong> Begin to appear within 3–7 days, with optimal results in approximately 2 weeks</li>
                <li><strong>Longevity:</strong> Typically last 12 weeks</li>
                <li><strong>Investment:</strong> $150</li>
            </ul>

            <h3 class="font-headline-lg text-deep-plum mb-6">Lip Flip vs. Lip Filler</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Although both treatments enhance the lips, they achieve beautifully different results.</p>
            
            <h4 class="font-headline-md text-primary mt-6 mb-2">Lip Flip</h4>
            <p class="font-body-md text-on-surface-variant mb-2">A Lip Flip enhances the <em>appearance</em> of fullness by relaxing the muscles around the upper lip. Ideal for patients who:</p>
            <ul class="list-disc pl-6 space-y-1 font-body-md text-on-surface-variant mb-6">
                <li>Prefer a subtle, naturally enhanced look</li>
                <li>Feel their upper lip disappears when they smile</li>
                <li>Want to soften the appearance of a gummy smile</li>
                <li>Are curious about lip enhancement without adding volume</li>
            </ul>

            <h4 class="font-headline-md text-primary mt-6 mb-2">Lip Filler</h4>
            <p class="font-body-md text-on-surface-variant mb-2">Lip filler uses hyaluronic acid to create <em>true volume, shape, and definition</em> within the lips. Ideal for patients who:</p>
            <ul class="list-disc pl-6 space-y-1 font-body-md text-on-surface-variant mb-12">
                <li>Desire fuller, more sculpted lips</li>
                <li>Want enhanced symmetry and definition</li>
                <li>Are looking for longer-lasting volume and contour</li>
                <li>Prefer a more noticeable transformation</li>
            </ul>

            <h3 class="font-headline-lg text-deep-plum mb-6">Your Personalized Lip Enhancement</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Every smile is unique, and your treatment should be too. During your consultation, our experienced aesthetic provider will evaluate your facial anatomy, discuss your aesthetic goals, and recommend the treatment—or combination of treatments—that will deliver the most beautiful, balanced, and natural-looking results.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Whether you're seeking a delicate enhancement or a more defined pout, we're here to help you achieve lips that complement your natural beauty with confidence and sophistication.</p>
        """
    },
    {
        "id": "migraine",
        "title": "Chronic Migraine Prevention with Botox®",
        "image": "images/botox.png",
        "content": """
            <p class="font-body-lg text-on-surface-variant mb-8">Chronic migraines can be debilitating, impacting your work, relationships, and quality of life. Botox® (onabotulinumtoxinA) is an FDA-approved preventive treatment for adults living with chronic migraine, offering a clinically proven approach to reducing both the frequency and severity of migraine attacks before they begin.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Unlike treatments that address symptoms after a migraine starts, Botox® works proactively by interrupting the pain pathways involved in chronic migraine, helping patients experience fewer migraine days and improved daily function.</p>
            
            <h3 class="font-headline-lg text-deep-plum mb-6">Who Is a Candidate?</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Botox® for chronic migraine is intended for adults diagnosed with chronic migraine, rather than occasional headaches or episodic migraines. You may be a candidate if you:</p>
            <ul class="list-disc pl-6 space-y-3 font-body-lg text-on-surface-variant mb-6">
                <li>Experience 15 or more headache days each month</li>
                <li>Have at least 8 days per month that meet the criteria for migraine</li>
                <li>Have headaches lasting 4 hours or longer</li>
                <li>Have not achieved adequate relief with, or have been unable to tolerate, at least two preventive migraine medications</li>
            </ul>
            <p class="font-body-lg text-on-surface-variant mb-12">During your consultation, our board-certified Physician Assistant will perform a comprehensive evaluation of your migraine history, symptoms, and previous treatments to determine whether Botox® is the right option for you.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">How Botox® Works</h3>
            <p class="font-body-lg text-on-surface-variant mb-12">Botox® does far more than relax muscles. It works by targeting the sensory nerve endings involved in chronic migraine, helping prevent the release of key pain-signaling neurotransmitters, including calcitonin gene-related peptide (CGRP) and Substance P. By interrupting these pain pathways before they activate, Botox® helps reduce the cascade of inflammation and nerve signaling that contributes to chronic migraine.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">Personalized, Expert Care</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Every treatment is performed by a board-certified Physician Assistant with more than 20 years of medical and surgical experience, including extensive expertise in orthopedics, musculoskeletal anatomy, and advanced neuromuscular treatments. This advanced understanding of anatomy allows for precise injection placement, ensuring treatment is both safe and tailored to your individual needs.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Our philosophy combines medical excellence with a luxury patient experience, providing compassionate, individualized care in an elegant, welcoming environment. Whether your goal is fewer migraine days, greater productivity, or simply reclaiming the moments that matter most, we are committed to helping you find lasting relief with confidence and exceptional care.</p>
        """
    },
    {
        "id": "nefertiti",
        "title": "Nefertiti Lift™ & Platysmal Band Treatment",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuAJCV6xecRE5wt4XOBO-ttFvKBZgDafzOUXb6ZhZJ4_WXugkJ5__3aR2OM9DVIy8CXISsTqROXpx0VN5HmUVBp3WrRtjYXHcua6-IvnFYgv33bax8bPkL7SsqMSzgUj-r29qACeJtjGbfWaCE05NI27MyGeqC5zvBfGq6PD-bUvGIi1WGUNIQESqB82YGKFwu9YPIVHHsXoV6QG0E3OLH1J5CNuij82WHC7sJHKlmY0knnHsfeA_MfNaSpoH3aWrJoYaGXYzujdeQI",
        "content": """
            <p class="font-body-lg text-on-surface-variant mb-8">Graceful definition along the jawline and neck is one of the hallmarks of a youthful appearance. Over time, the platysma muscle can become more prominent, creating visible vertical neck bands, softening the jawline, and contributing to the appearance of jowls.</p>
            <p class="font-body-lg text-on-surface-variant mb-4">The <strong>Nefertiti Lift™</strong> is an advanced, non-surgical Botox® treatment designed to relax the platysma muscle, creating a smoother neck, a more defined jawline, and a naturally refreshed profile—without surgery or downtime.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Every treatment is performed by a <strong>board-certified Physician Assistant with more than 20 years of medical and surgical experience</strong>, including extensive expertise in <strong>orthopedics, musculoskeletal anatomy, and advanced muscle treatments</strong>. With an in-depth understanding of facial anatomy and muscle dynamics, each treatment is carefully customized to enhance your natural features while preserving balanced, effortless facial expression.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">How the Nefertiti Lift™ Works</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">The platysma is a broad muscle that extends from the collarbone to the lower face. As it becomes more active with age, it can pull downward on the jawline and create prominent vertical neck bands. Strategically placed Botox® injections relax this downward pull, allowing the muscles that elevate the face to work more effectively.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">The result is a subtle yet noticeable improvement in jawline definition, neck smoothness, and lower facial contour—all while maintaining natural movement.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">Benefits of Treatment</h3>
            <ul class="list-disc pl-6 space-y-3 font-body-lg text-on-surface-variant mb-12">
                <li>Softens visible platysmal (neck) bands</li>
                <li>Enhances jawline definition</li>
                <li>Creates a smoother, more youthful neck contour</li>
                <li>Reduces the appearance of early jowling</li>
                <li>Provides a refreshed, naturally lifted appearance</li>
                <li>Non-surgical treatment with little to no downtime</li>
            </ul>

            <h3 class="font-headline-lg text-deep-plum mb-6">What to Expect</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Treatment is performed in a comfortable, luxury setting and typically takes less than 30 minutes. Most patients begin noticing improvement within <strong>7–14 days</strong>, with full results developing over the following weeks. Results generally last <strong>3–4 months</strong>, depending on muscle activity and individual metabolism.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Your provider will perform a comprehensive facial assessment to determine whether a Nefertiti Lift™ alone or in combination with other aesthetic treatments will best achieve your desired outcome.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">Precision Meets Artistry</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Exceptional results require more than technical skill—they require a sophisticated understanding of anatomy, muscle balance, and facial aesthetics. With two decades of medical and surgical experience treating complex musculoskeletal conditions, our provider combines clinical precision with an artistic eye to deliver elegant, natural-looking rejuvenation.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Whether you're looking to soften prominent neck bands, restore a more sculpted jawline, or maintain a youthful profile without surgery, your treatment plan is designed around your unique anatomy and aesthetic goals, delivering refined, timeless results that never look overdone.</p>
        """
    },
    {
        "id": "tmj",
        "title": "TMJ Relief with Botox®",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBm-V8k6N-34ED3yWrQ8QLyEbadliHn1vbRJEeBK0A2136z8nOit10rWMJZ1EO2NHvCbcGY1x3BCd6M6a-sGRn0gVLrVfaJl0Yc_Ao7-sktthFD8TEjXlvXNZmEkAwaJhA4034W3UJOsXYuboZ6P91aozHQl87nq2hlAAZBiWMjTM4Ec4EnbUfJ7MMgoIpRN3ShGu99oOaJDsYWT55IDy59IPdO5CGseVhCg_Swh4TH7GSAx_B5Jflup-dDTOrsB19FIdkXUOpI1XE",
        "content": """
            <p class="font-body-lg text-on-surface-variant mb-8">Chronic jaw tension, teeth grinding, and TMJ discomfort can impact your comfort, sleep, and overall quality of life. At our practice, TMJ treatment with Botox® is more than a cosmetic procedure—it's a precision-based medical treatment designed to relieve pain, restore function, and help you feel your best.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Every treatment is performed by a board-certified Physician Assistant with more than 20 years of medical and surgical experience, including extensive expertise in orthopedics, musculoskeletal anatomy, and advanced muscle treatments. With a deep understanding of facial anatomy and muscle function, each treatment is thoughtfully customized to address the root cause of your symptoms while maintaining natural movement and facial harmony.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">A Targeted Approach to Lasting Relief</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Botox® works by temporarily relaxing the overactive muscles responsible for jaw clenching and teeth grinding. By reducing excessive muscle activity in the masseter and surrounding muscles, tension on the temporomandibular joint (TMJ) is relieved, allowing the muscles to rest and function more comfortably.</p>
            <p class="font-body-lg text-on-surface-variant mb-4">Many patients experience:</p>
            <ul class="list-disc pl-6 space-y-3 font-body-lg text-on-surface-variant mb-12">
                <li>Relief from chronic jaw pain and facial tension</li>
                <li>Reduced teeth grinding and clenching (bruxism)</li>
                <li>Fewer tension headaches related to TMJ dysfunction</li>
                <li>Improved comfort while chewing and speaking</li>
                <li>A softer, more balanced jawline in patients with enlarged masseter muscles</li>
            </ul>

            <h3 class="font-headline-lg text-deep-plum mb-6">What to Expect</h3>
            <p class="font-body-lg text-on-surface-variant mb-12">Treatment is performed in a comfortable, luxurious setting and typically takes less than 30 minutes with little to no downtime. Most patients begin noticing improvement within <strong>7–14 days</strong>, with results lasting approximately <strong>3–6 months</strong>. Because every patient is unique, your treatment plan is tailored to your anatomy, muscle strength, and individual goals.</p>

            <h3 class="font-headline-lg text-deep-plum mb-6">Expertise You Can Trust</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">Your care deserves more than technical skill—it deserves experience. With two decades of hands-on medical and surgical practice treating complex musculoskeletal conditions, our provider brings a level of clinical expertise that extends far beyond aesthetics. This advanced understanding of muscle function allows for precise dosing and injection placement, maximizing therapeutic benefit while preserving natural expression and movement.</p>
            <p class="font-body-lg text-on-surface-variant mb-12">Whether you're seeking relief from chronic TMJ symptoms, persistent jaw clenching, or nighttime grinding, you'll receive personalized care focused on restoring comfort, improving function, and enhancing your overall well-being.</p>
        """
    },
    {
        "id": "b12",
        "title": "Vitamin B12 Wellness Injections",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBy2fw-voRZz5Y8tBaMgfhGCXPK39CsN63WCVbydkQ4Wbems6axRj2PH5vDT8wb0Ks3-U0Yyvvwu4SiFR2EpRVf5zbM6I2OKcQwkm_t8ejv9SsrDODIwt6J5LZpyItVrZgFB8kRxwrknVq_y-_Q-46RJApy4cjzkDUF5wXEfE0EXffRMLlnEF2IOxUn3icM92Adg-nmzfrxePpnh25mrhUiqr-Y3dRSfZ6gKIPQVNjrusZbMBUTlnjBnf7JkHLU5Q3If3jDZtnQAjg",
        "content": """
            <p class="font-body-lg text-on-surface-variant mb-8">Boost your energy, improve metabolism, and support your nervous system with a quick and effective Vitamin B12 wellness injection. Whether you're feeling sluggish, struggling with focus, or simply looking to support your overall wellness, B12 injections provide an immediate, bioavailable boost of this essential nutrient directly into your system.</p>
            
            <h3 class="font-headline-lg text-deep-plum mb-6">The Benefits of B12</h3>
            <ul class="list-disc pl-6 space-y-3 font-body-lg text-on-surface-variant mb-12">
                <li><strong>Increased Energy:</strong> Say goodbye to afternoon fatigue and sluggishness.</li>
                <li><strong>Improved Metabolism:</strong> Supports the conversion of food into usable energy.</li>
                <li><strong>Mental Clarity:</strong> Enhances focus, memory, and cognitive function.</li>
                <li><strong>Better Sleep:</strong> Helps regulate circadian rhythms and promote restful sleep.</li>
                <li><strong>Immune Support:</strong> Strengthens the immune system and aids in cellular repair.</li>
            </ul>

            <h3 class="font-headline-lg text-deep-plum mb-6">Why Choose Injections?</h3>
            <p class="font-body-lg text-on-surface-variant mb-12">While B12 is available in oral supplements, it is often poorly absorbed through the digestive tract. By delivering B12 intramuscularly, the nutrient bypasses the digestive system and enters the bloodstream directly, resulting in 100% absorption and much faster, more noticeable results. The treatment is virtually painless and takes just a few minutes, making it a perfect quick pick-me-up for your busy lifestyle.</p>
        """
    },
    {
        "id": "nad",
        "title": "NAD+ Injections for Cellular Repair",
        "image": "https://lh3.googleusercontent.com/aida-public/AB6AXuBy2fw-voRZz5Y8tBaMgfhGCXPK39CsN63WCVbydkQ4Wbems6axRj2PH5vDT8wb0Ks3-U0Yyvvwu4SiFR2EpRVf5zbM6I2OKcQwkm_t8ejv9SsrDODIwt6J5LZpyItVrZgFB8kRxwrknVq_y-_Q-46RJApy4cjzkDUF5wXEfE0EXffRMLlnEF2IOxUn3icM92Adg-nmzfrxePpnh25mrhUiqr-Y3dRSfZ6gKIPQVNjrusZbMBUTlnjBnf7JkHLU5Q3If3jDZtnQAjg",
        "content": """
            <p class="font-body-lg text-on-surface-variant mb-8">Enhance cellular repair, mental clarity, and anti-aging with NAD+ therapy, designed to revitalize your body at the molecular level. Nicotinamide Adenine Dinucleotide (NAD+) is a crucial coenzyme found in every cell in your body, responsible for producing energy, maintaining DNA health, and regulating cellular aging. Unfortunately, our natural NAD+ levels decline significantly as we age.</p>
            
            <h3 class="font-headline-lg text-deep-plum mb-6">Why Replenish NAD+?</h3>
            <p class="font-body-lg text-on-surface-variant mb-4">By restoring your NAD+ levels through targeted injections, you can support a wide range of biological functions that promote vitality and longevity:</p>
            <ul class="list-disc pl-6 space-y-3 font-body-lg text-on-surface-variant mb-12">
                <li><strong>Cellular Energy:</strong> Restores ATP production, naturally boosting physical and mental stamina.</li>
                <li><strong>Anti-Aging:</strong> Activates sirtuins, the "longevity genes" that protect cells from age-related decline.</li>
                <li><strong>Cognitive Enhancement:</strong> Improves brain health, mental clarity, focus, and memory.</li>
                <li><strong>Metabolic Support:</strong> Aids in weight management and metabolic efficiency.</li>
                <li><strong>Inflammation Reduction:</strong> Helps reduce chronic inflammation and promotes faster recovery from physical exertion.</li>
            </ul>

            <h3 class="font-headline-lg text-deep-plum mb-6">What to Expect</h3>
            <p class="font-body-lg text-on-surface-variant mb-12">NAD+ injections are a quick and effective way to elevate your NAD+ levels compared to oral supplements. The treatment is administered quickly in our office and many patients report feeling a noticeable difference in their energy and clarity within 24-48 hours. Depending on your wellness goals, we can customize a treatment schedule that keeps you feeling revitalized, focused, and resilient against the effects of aging.</p>
        """
    }
]

for s in services:
    page_html = header + f'''
    <main class="pt-32 pb-section-gap">
        <div class="max-w-container mx-auto px-margin-mobile md:px-margin-desktop">
            <a href="services.html" class="inline-flex items-center gap-2 text-deep-plum hover:text-soft-blush transition-colors font-label-lg mb-8 uppercase tracking-widest"><span class="material-symbols-outlined">arrow_back</span> Go Back to Services</a>
            
            <div class="bg-paper-white rounded-2xl overflow-hidden shadow-sm mb-12">
                <div class="w-full h-[400px] overflow-hidden relative">
                    <img src="{s["image"]}" class="w-full h-full object-cover" alt="{s["title"]}">
                </div>
                <div class="p-8 md:p-16">
                    <h1 class="font-display-lg text-display-lg-mobile md:text-display-lg text-deep-plum mb-12">{s["title"]}</h1>
                    
                    {s["content"]}
                    
                    <div class="mt-16 pt-12 border-t border-medical-gray/20 text-center">
                        <h2 class="font-headline-lg text-primary mb-6">Ready to get started?</h2>
                        <button onclick="window.location.href='https://squareup.com/appointments/book/L5CWQHE9Q1V00'" class="bg-deep-plum text-paper-white px-10 py-4 font-label-lg uppercase tracking-widest hover:bg-deep-plum/90 transition-all text-lg shadow-sm hover:shadow-md cursor-pointer">Book Now</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
    ''' + footer
    
    with open(f'service-{s["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(page_html)

print("Generated 6 service pages.")
