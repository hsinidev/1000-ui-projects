---
name: Ethos-ID Design System
colors:
  surface: '#faf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#faf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f0'
  surface-container: '#efeeea'
  surface-container-high: '#e9e8e4'
  surface-container-highest: '#e3e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#424845'
  inverse-surface: '#2f312e'
  inverse-on-surface: '#f2f1ed'
  outline: '#727875'
  outline-variant: '#c2c8c4'
  surface-tint: '#4e635a'
  primary: '#4e635a'
  on-primary: '#ffffff'
  primary-container: '#8da399'
  on-primary-container: '#263932'
  inverse-primary: '#b5ccc1'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#5a605b'
  on-tertiary: '#ffffff'
  tertiary-container: '#9aa09a'
  on-tertiary-container: '#313732'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#dee4dd'
  tertiary-fixed-dim: '#c2c8c1'
  on-tertiary-fixed: '#171d19'
  on-tertiary-fixed-variant: '#424843'
  background: '#faf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e3e2df'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
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
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

This design system is built upon the pillars of **Conscious Luxury** and **Radical Transparency**. It serves a sophisticated audience that values both high-end craftsmanship and the ethical footprint of their acquisitions. The aesthetic is "Sustainable-Modern"—a fusion of organic, tactile elements with the precision of blockchain technology.

The visual direction utilizes a **Minimalist-Tactile** style. We prioritize generous whitespace to evoke a sense of calm and exclusivity. To differentiate from "cold" tech platforms, this system incorporates a subtle paper texture across background surfaces, grounding the digital experience in the physical world of luxury textiles and archival records. The emotional response should be one of quiet confidence, institutional trust, and environmental stewardship.

## Colors

The palette is intentionally restrained to emphasize the products and their provenance.

- **Primary (Sage Green):** A desaturated, earthy green used for meaningful actions, success states, and the 'Lifecycle-Chain' motifs. It represents growth and sustainability.
- **Secondary (Obsidian Black):** Used for typography and high-contrast accents. It provides the "anchor" for luxury branding.
- **Background (Off-White):** A warm, parchment-leaning neutral that serves as the base layer. It avoids the clinical feel of pure white.
- **Surface (Pale Sage):** A tertiary tint used for subtle grouping, hover states, and card backgrounds to maintain a monochromatic, harmonious flow.

## Typography

The typography strategy balances modern technicality with editorial elegance.

- **Headlines:** Use **Manrope**. Its refined, geometric proportions feel contemporary yet premium. We utilize lighter weights (300/400) for larger displays to emphasize a high-fashion, airy feel.
- **Body & UI:** Use **Inter**. Chosen for its exceptional legibility and systematic "tech" feel, it reinforces the blockchain-backed reliability of the platform.
- **Labels:** Small caps with increased letter spacing are used for metadata, product IDs, and blockchain hash references to create a "spec-sheet" aesthetic that feels both archival and futuristic.

## Layout & Spacing

The design system employs a **Fixed Grid** philosophy to maintain a structured, gallery-like presentation.

- **Grid:** A 12-column grid with generous 64px outer margins on desktop. This "frame" effect makes the content feel like a curated exhibit.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Whitespace:** Emphasize "Vertical Breathing." Sections should be separated by large padding blocks (80px–120px) to prevent the UI from feeling cluttered, ensuring the user focuses on one transparency data point at a time.

## Elevation & Depth

Depth is achieved through **Tonal Layering** rather than traditional shadows. 

- **The Base:** The primary background features a high-resolution, low-opacity "Paper Texture" overlay (multiply blend mode at 3-5% opacity).
- **Surface Levels:** Elements like cards or modals use a slightly lighter or darker tint of Off-White or Pale Sage to distinguish themselves from the base.
- **Borders:** Instead of shadows, use "Ghost Borders"—1px strokes in a slightly darker neutral or primary tint (#D1D5D1). This keeps the UI flat and architectural.
- **Active States:** Subtle, diffused ambient shadows (0px 4px 20px, 4% opacity Black) are reserved only for floating elements like dropdowns or high-priority modals.

## Shapes

The shape language is **Soft-Architectural**. 

While luxury often utilizes sharp 90-degree angles, this design system uses a "Soft" (4px) corner radius to bridge the gap between human/organic sustainability and the precision of digital blockchain interfaces. 

- **Primary Elements:** Buttons and Input fields use the standard 4px radius.
- **Data Viz:** Points on the provenance timeline should be perfectly circular to represent "Nodes" in the circular fashion economy.
- **Interactive Containers:** Cards utilize a slightly larger `rounded-lg` (8px) to feel approachable.

## Components

- **Minimalist Buttons:** Text-only or ghost-style buttons with 1px Obsidian Black borders. No heavy fills unless it is the Primary CTA, which uses a solid Sage Green fill with White text.
- **Lifecycle-Chain Timeline:** A vertical or horizontal thin 1px line connecting circular nodes. Each node represents a "Life Event" (e.g., Harvest, Craft, Sale, Resale). Completed events are filled with Sage Green; upcoming events are outlined.
- **Provenance Data Viz:** Use clean, monochromatic bar charts or "DNA-style" line graphs to display material composition or CO2 impact. Avoid multi-color charts; use shades of Sage and Black only.
- **Input Fields:** Bottom-border only (border-b-1px) with labels in the `label-sm` style. This mimics the look of a high-end physical ledger.
- **Sustainability Chips:** Small, pill-shaped tags used to denote certifications (e.g., GOTS, FSC). These should be `tertiary_color` with `secondary_color` text.