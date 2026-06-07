---
name: High-Luxury Dental Editorial
colors:
  surface: '#faf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#faf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e8'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3031'
  inverse-on-surface: '#f2f0f0'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#5e5f5d'
  on-secondary: '#ffffff'
  secondary-container: '#e0e0dd'
  on-secondary-container: '#626361'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#241a00'
  on-tertiary-container: '#a08000'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1a1c1a'
  on-secondary-fixed-variant: '#464745'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#faf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.2em
spacing:
  margin-page: 2rem
  gutter-grid: 1rem
  section-gap: 4rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
---

## Brand & Style

This design system establishes an atmosphere of "Elite Aesthetic Artistry," moving away from clinical coldness toward the warmth of a high-fashion lifestyle magazine. The target audience is the ultra-high-net-worth individual who views cosmetic dentistry as a luxury investment in their personal brand.

The aesthetic follows a **Minimalist-Luxury** approach. It utilizes expansive whitespace (or "ivory space"), razor-thin geometric accents, and high-fashion photography to evoke a sense of exclusivity and calm. The interface should feel like a physical, heavy-stock paper magazine—tactile yet digital—prioritizing visual storytelling over dense information architecture.

## Colors

The palette is strictly curated to maintain a boutique feel. 

- **Warm Ivory (#FAF9F6):** Used as the primary canvas color. It is softer and more premium than pure white, suggesting a natural, healthy tooth enamel and high-end stationery.
- **Deep Black (#000000):** Used for primary typography and structural elements to provide high-contrast "editorial" impact.
- **Metallic Gold (#D4AF37):** Used sparingly as an accent for hairline borders, active states, and call-to-action iconography.
- **Secondary Neutral:** Soft greys are used only for secondary metadata to ensure the black-and-ivory contrast remains dominant.

## Typography

The typography pairing is the cornerstone of this design system's editorial feel. 

**Noto Serif** acts as the "Editorial Voice." It should be used for all major headlines and impactful quotes. Its high-contrast strokes mimic the look of *Vogue* or *Harper's Bazaar*. 

**Manrope** provides a "Modern Concierge" feel for body copy. To maintain the luxury aesthetic, body copy must use generous line heights and increased letter spacing (tracking). Section labels and small buttons should always be in uppercase Manrope with high letter spacing (0.2em) to emulate luxury brand tagging.

## Layout & Spacing

This design system uses a **No Grid / Fluid Layout** philosophy optimized for mobile. Instead of a rigid column structure, it relies on "Safe Margins" and "Visual Anchors."

- **Margins:** A generous 32px (2rem) side margin ensures content feels framed, like a magazine page.
- **Verticality:** Use extreme vertical padding (64px+) between sections to force a slow, deliberate scroll speed, encouraging the user to appreciate the photography.
- **Asymmetry:** Occasionally offset images or text blocks from the center to create a dynamic, editorial rhythm.

## Elevation & Depth

This design system rejects traditional shadows and depth. It uses **Flat Tonal Layering** and **Hairline Accents** to define hierarchy.

- **Layering:** Hierarchy is achieved by stacking elements directly. A gold-bordered card sits flat on the Ivory background.
- **Borders:** Use 0.5pt or 1pt Gold (#D4AF37) lines to separate high-level sections or frame "Featured" content.
- **Glassmorphism:** Reserved exclusively for the "Minimalist Navigation Bar" (a bottom-fixed or top-fixed blur) to ensure the full-screen photography remains the focus while providing legibility for nav items.

## Shapes

The shape language is **Architectural and Sharp**. 

All buttons, image containers, and input fields must have a 0px border radius. Sharp corners convey a sense of precision, clinical excellence, and high-end modernism. Any deviation into rounded corners will dilute the "Boutique" feel and move the brand toward "Friendly/Casual," which should be avoided.

## Components

- **Primary Buttons:** Solid Deep Black background with Warm Ivory text. Sharp corners. No shadows. On tap, the background transitions to Metallic Gold.
- **Editorial Cards:** Full-bleed imagery with a thin Gold border (#D4AF37) on the bottom or as a frame. Text is overlaid using a subtle dark gradient at the base for legibility.
- **Navigation:** A minimalist "Menu" label in all-caps Sans-Serif. Use a full-screen overlay for the menu itself, featuring large-scale Noto Serif links.
- **Inputs:** A single Deep Black bottom border (hairline). No box. Labels appear in all-caps Sans-Serif above the line.
- **Lifestyle Chips:** Used for selecting treatments. Transparent background with a 1px Deep Black border. When selected, the border turns Gold.
- **Signature Component (The Reveal):** A "Before/After" slider using a vertical Gold hairline handle to showcase dental transformations.