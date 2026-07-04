---
name: Serene Medical Aesthetic
colors:
  surface: '#fbf9f7'
  surface-dim: '#dbdad8'
  surface-bright: '#fbf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efedec'
  surface-container-high: '#eae8e6'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1b'
  on-surface-variant: '#4e4448'
  inverse-surface: '#30302f'
  inverse-on-surface: '#f2f0ee'
  outline: '#807478'
  outline-variant: '#d2c3c7'
  surface-tint: '#775464'
  primary: '#452836'
  on-primary: '#ffffff'
  primary-container: '#5e3e4d'
  on-primary-container: '#d5abbc'
  inverse-primary: '#e6bbcd'
  secondary: '#75584b'
  on-secondary: '#ffffff'
  secondary-container: '#ffd7c7'
  on-secondary-container: '#7a5c4f'
  tertiary: '#392f29'
  on-tertiary: '#ffffff'
  tertiary-container: '#51453e'
  on-tertiary-container: '#c3b3aa'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd8e8'
  primary-fixed-dim: '#e6bbcd'
  on-primary-fixed: '#2d1320'
  on-primary-fixed-variant: '#5d3d4c'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#e5beaf'
  on-secondary-fixed: '#2b160d'
  on-secondary-fixed-variant: '#5b4135'
  tertiary-fixed: '#f1dfd6'
  tertiary-fixed-dim: '#d4c3ba'
  on-tertiary-fixed: '#231a14'
  on-tertiary-fixed-variant: '#50443e'
  background: '#fbf9f7'
  on-background: '#1b1c1b'
  surface-variant: '#e4e2e0'
  deep-plum: '#5E3E4D'
  muted-taupe: '#8B7D75'
  soft-blush: '#C5A192'
  paper-white: '#FDFDFD'
  medical-gray: '#EDEDED'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 64px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '400'
    lineHeight: 32px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  display-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
  headline-xl-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
spacing:
  base: 8px
  section-desktop: 120px
  section-mobile: 64px
  gutter: 24px
  margin-edge: 40px
  stack-sm: 16px
  stack-md: 32px
---

## Brand & Style

This design system embodies the "Beauty Refined" philosophy, creating a digital environment that feels like a sanctuary of professional excellence and quiet luxury. The brand personality is clinical yet compassionate, balancing medical rigor with a high-end spa experience. 

The aesthetic direction is **Minimalism** infused with **Tonal Layering**. It prioritizes vast white space to symbolize cleanliness and clarity, using high-quality photography as a primary design element. The emotional response should be one of immediate calm, safety, and the assurance of expert-level results. Every interaction is intentional, avoiding loud transitions in favor of a smooth, understated flow that respects the user's focus.

## Colors

The palette is anchored in warm, organic tones that reflect skin health and sophisticated medical care. 

- **Primary (Deep Plum):** Used for critical conversion points and high-level branding. It provides enough contrast for clinical authority without the harshness of pure black.
- **Secondary (Soft Blush):** A refined accent color used for subtle highlights, hover states, and callouts. It evokes a healthy glow and natural beauty.
- **Tertiary (Muted Taupe):** Used for sub-headings and secondary UI elements like labels and iconography.
- **Neutral (Paper White & Medical Gray):** The foundation of the system, providing a clean, "scrubbed" feel that ensures content remains the hero.

**Color Usage Rules:**
- Avoid using pure black (`#000000`). Use **Deep Plum** for text to maintain a softer, more editorial feel.
- Use **Medical Gray** for borders and dividers to keep the UI light and airy.

## Typography

This system utilizes a "High-End Medical" pairing of a classic, authoritative serif and a modern, technical sans-serif.

- **Libre Caslon Text (Headlines):** Provides an editorial, prestigious feel. It should be used for all major headers and brand statements. Use large font sizes with generous line height to maintain a "breathable" luxury feel.
- **Manrope (Body & Labels):** Chosen for its clean, professional, and balanced proportions. It ensures maximum readability for complex medical information and clinical descriptions.

**Stylistic Note:** Headings should never be bolded. The weight of the Serif provides enough visual hierarchy naturally. Labels for form fields and buttons should use increased letter-spacing in uppercase for a more structured, premium look.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** with generous, intentional whitespace to avoid any sense of "clutter" or "medical anxiety."

- **Desktop:** A 12-column centered grid with a maximum width of 1280px. Gutters are 24px.
- **Mobile:** A 4-column fluid grid with 20px margins.
- **Rhythm:** We use a strict 8px baseline. Section spacing is intentionally oversized (120px) to clearly demarcate procedure categories and bio sections.

**Reflow Rules:** 
- In the "Procedure Grid," cards should stack vertically on mobile while retaining a "shifted" or staggered appearance to maintain visual interest.
- Form fields transition from a two-column layout on desktop to a single column on mobile to ensure ease of entry for patients.

## Elevation & Depth

To maintain a clean and sterile aesthetic, this design system avoids heavy shadows. Hierarchy is instead established through **Tonal Layers** and **Soft Accents**.

- **Surface Levels:** The primary background is `paper-white`. Secondary content blocks use a very soft tint of `neutral-color` to define depth without creating a "floating" effect.
- **Depth Markers:** Where shadows are necessary (e.g., a high-priority "Request Consultation" modal), use an ultra-diffused, 10% opacity shadow with a `muted-taupe` tint. 
- **Borders:** Use thin, 1px lines in `medical-gray` for input fields and section dividers. This maintains a "plotted" and precise medical feel.

## Shapes

The design system uses a **Sharp (0)** roundedness strategy. All buttons, input fields, and image containers utilize 90-degree corners. 

This decision reinforces a sense of precision, professional discipline, and clinical excellence. Soft, rounded corners can feel overly "friendly" or "consumer-grade," whereas sharp lines align with the meticulous nature of surgical and medical aesthetic procedures.

**Exceptions:** Circular elements may be used for social media profile icons or specific "Service Spotlight" badges, but structural UI must remain sharp.

## Components

### Buttons
- **Primary:** Solid `deep-plum` background with `paper-white` text. No rounded corners. 1px inset border on hover.
- **Secondary:** Transparent background with `deep-plum` 1px border. 
- **Hover States:** Subtle background color shifts (e.g., `deep-plum` to a 90% opacity). Avoid aggressive animations.

### Input Fields
- **Styling:** 1px border in `medical-gray` with a sharp corner. Label placed above in `label-md`. 
- **Focus:** Border transitions to `muted-taupe`.

### Cards (Procedures)
- **Visuals:** Full-bleed imagery with text overlays in a structured grid.
- **Content:** The headline of the procedure should be in `headline-md` (Libre Caslon Text) to give each service a premium title feel.

### Selection & Form Controls
- **Checkboxes:** Square, custom-styled to match the `deep-plum` primary color.
- **Dropdowns:** Simple, chevron-indicated menus using the same sharp border style as input fields.

### Lists
- Use a `soft-blush` chevron or simple line-break to separate procedure sub-types (e.g., Rhinoplasty > Facelift).