---
name: Clinical Vitality
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#3f484c'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#6f787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0c6780'
  primary: '#0c6780'
  on-primary: '#ffffff'
  primary-container: '#87ceeb'
  on-primary-container: '#005870'
  inverse-primary: '#89d0ed'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#865219'
  on-tertiary: '#ffffff'
  tertiary-container: '#fbb674'
  on-tertiary-container: '#76450c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#baeaff'
  primary-fixed-dim: '#89d0ed'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d62'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ffdcbf'
  tertiary-fixed-dim: '#feb876'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6a3b01'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  section-padding: 80px
---

## Brand & Style

The design system is anchored in the intersection of rigorous scientific integrity and the warmth of biological renewal. It targets an audience of medical professionals, researchers, and patients seeking high-efficacy regenerative treatments. The emotional response is one of calm confidence, precision, and hope.

The visual style is **Clinical Minimalism** with high-end editorial flourishes. It prioritizes clarity and functionality through generous whitespace, ensuring that complex medical data feels accessible rather than overwhelming. The use of thin-line geometry and a restricted palette reflects the precision of stem cell isolation, while subtle micro-animations of fluid, organic shapes evoke the process of cellular regeneration.

## Colors

The palette is engineered to balance sterile professionalism with the warmth of high-end care. 

- **Primary (Sky Blue):** Utilized for primary actions and trust-building elements. It represents the "Vitality" aspect of the brand.
- **Secondary (Gold):** Used sparingly as an accent for prestige markers, high-level certifications, and subtle borders to signify premium quality and "Scientific Excellence."
- **Neutrals:** A range of cool-toned greys facilitate the hierarchy. Pure white is the dominant background color to maintain a "Clinical" environment.
- **Status Colors:** Success, Warning, and Error states should use desaturated versions of green and red to remain consistent with the sophisticated tone.

## Typography

This design system utilizes a dual-font strategy to establish authority and legibility. 

**Headings** employ a traditional serif to reference the heritage of medical journals and academic research. These should be set with tighter tracking and generous leading to maintain an editorial feel.

**Body Text** uses a modern sans-serif designed for clarity. Its geometric yet warm character ensures that long-form clinical case studies remain highly readable. 

**Labels and Metadata** should be set in the sans-serif with increased letter spacing and uppercase styling to differentiate technical data from narrative content.

## Layout & Spacing

The layout philosophy follows a **Fixed-Width Grid** within a centered container to ensure focus and readability. A 12-column system is used for desktop layouts, with an emphasis on "Negative Space" as a functional element rather than a void.

- **Vertical Rhythm:** Sections are separated by significant padding (80px+) to allow the content to "breathe," mirroring the clean environment of a modern laboratory.
- **Grids:** Use 4-column spans for informational cards and 8-column spans for primary body text to optimize the line length for scientific reading.

## Elevation & Depth

To maintain a "Clinical" feel, this design system avoids heavy shadows. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**.

- **Surfaces:** Use subtle light-grey fills (#F1F5F9) to distinguish secondary content areas from the primary white background.
- **Outlines:** Elements like cards and input fields should use 1px solid borders in a very light neutral tone. 
- **Glassmorphism:** For overlays, navigation bars, or modals, use a high-density backdrop blur (20px+) with 80% white opacity to maintain a sense of sterile transparency and innovation.

## Shapes

The shape language is precise and disciplined. **Soft corners (4px)** are applied to most UI components to prevent the interface from feeling "sharp" or "aggressive," while maintaining the professional structure required for a medical institution.

Large imagery, particularly clinical case studies and laboratory photography, should maintain sharp edges or very subtle rounding to emphasize the "Scientific Integrity" of the data presented.

## Components

- **Buttons:** Primary buttons feature a Sky Blue fill with white text. Secondary buttons use a transparent background with a Gold 1px border. All buttons should have a subtle 200ms transition on hover.
- **Input Fields:** Minimalist design with a bottom-border only or a very light 4-sided stroke. Focus states use a thin Sky Blue glow.
- **Cards:** White background with a 1px "Gold" or "Light Grey" border. No heavy drop shadows. Use internal padding of 32px to ensure content clarity.
- **Thin-Line Icons:** Use 1.5pt stroke weight icons. Icons should be monochrome (Grey or Sky Blue) and never filled, preserving the "Lightness" of the UI.
- **Data Visualization:** Charts and graphs should utilize the Sky Blue for primary data and Gold for highlighted insights, set against a clean grid background.
- **Micro-animations:** Implement subtle, non-looping CSS animations for "regeneration" effects when elements enter the viewport—gentle fades and slight scale-ups (1.0 to 1.02).