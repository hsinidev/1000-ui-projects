---
name: Modern-Heritage Luxury
colors:
  surface: '#faf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#584141'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#8c7071'
  outline-variant: '#e0bfbf'
  surface-tint: '#af2b3e'
  primary: '#570013'
  on-primary: '#ffffff'
  primary-container: '#800020'
  on-primary-container: '#ff828a'
  inverse-primary: '#ffb3b5'
  secondary: '#5e604d'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1c9'
  on-secondary-container: '#636451'
  tertiary: '#272726'
  on-tertiary: '#ffffff'
  tertiary-container: '#3d3d3c'
  on-tertiary-container: '#a9a7a6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdada'
  primary-fixed-dim: '#ffb3b5'
  on-primary-fixed: '#40000b'
  on-primary-fixed-variant: '#8e0f28'
  secondary-fixed: '#e4e4cc'
  secondary-fixed-dim: '#c8c8b0'
  on-secondary-fixed: '#1b1d0e'
  on-secondary-fixed-variant: '#474836'
  tertiary-fixed: '#e4e2e0'
  tertiary-fixed-dim: '#c8c6c4'
  on-tertiary-fixed: '#1b1c1b'
  on-tertiary-fixed-variant: '#474745'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 4.5rem
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 2.5rem
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 1.75rem
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

This design system is anchored in a **Modern-Heritage** aesthetic, blending the gravitas of traditional high-end auction houses with the streamlined precision of modern digital commerce. It is designed for a discerning audience that values provenance, craftsmanship, and exclusivity. 

The visual style is **Tactile Minimalism**. It avoids the sterility of pure modernism by incorporating subtle physical cues—specifically paper and leather textures—that suggest a world of tangible assets. The emotional response is one of prestige and "quiet luxury," where every pixel feels intentional and every interaction feels like a private concierge service. The system prioritizes breathing room (whitespace), allowing high-resolution product photography to serve as the primary visual anchor.

## Colors

The palette is rooted in classical luxury. 
- **Primary (Deep Burgundy):** Used exclusively for primary actions, critical alerts, and brand signifiers. It represents authority and passion.
- **Secondary (Cream):** The foundational surface color. It is warmer and softer than pure white, reducing eye strain and evoking aged parchment.
- **Tertiary (Charcoal/Ink):** Used for primary text and borders to maintain high legibility without the harshness of true black.
- **Neutrals:** A range of "Stone" and "Parchment" tones used for secondary surfaces, subtle dividers, and background layering.

Apply a subtle noise overlay (2-3% opacity) on Cream backgrounds to simulate the grain of high-quality heavy-stock paper.

## Typography

The typographic strategy relies on a high-contrast pairing:
- **Noto Serif** provides the "Heritage." It is used for all editorial headings, product titles, and storytelling elements. It should be set with generous leading to maintain an airy, sophisticated feel.
- **Work Sans** provides the "Modern." It is used for functional UI, navigation, price points, and metadata. Its utilitarian nature ensures that the interface remains efficient and readable even at small scales.

Use **Label Caps** for categories and overlines to evoke the look of a curated gallery label.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model for desktop, centered on a 12-column layout with wide 32px gutters. The layout is intentionally "spacious," using significantly larger margins (64px+) than standard e-commerce to create an editorial, high-end feel. 

Vertical rhythm is governed by a 4px baseline, but large-scale components should utilize "Section Gaps" (128px+) to separate different narratives or product categories, preventing the UI from feeling cluttered. Alignment should be asymmetrical in editorial sections to mimic high-end print magazines, while remaining strictly aligned for functional search and filter results.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Low-Contrast Outlines** rather than heavy shadows. 
- **Surfaces:** Use a slight color shift (e.g., Cream to a slightly darker Parchment) to indicate depth.
- **Borders:** Use thin (1px), charcoal-tinted borders at 10-15% opacity to define areas without creating visual noise.
- **Shadows:** When necessary for floating elements (like dropdowns), use "Ambient Shadows"—extremely diffused, long-range shadows with a hint of Burgundy in the tint (#800020 at 5% opacity) to maintain warmth.
- **Tactile Depth:** Incorporate a subtle "inner-pressed" shadow on input fields to simulate leather embossing or stamped paper.

## Shapes

The shape language is **Sharp (0)**. To maintain the prestige and architectural rigor of the design system, elements use 0px border-radii. Sharp corners evoke precision, luxury watchmaking, and formal stationary. 

In rare instances where a softer touch is required for user comfort (such as mobile avatars), a maximum of 2px radius may be used, but all primary buttons, cards, and image containers must remain perfectly rectangular.

## Components

- **Buttons:** Primary buttons are solid Deep Burgundy with white Work Sans text (All Caps). Secondary buttons use a Charcoal outline with no fill.
- **Cards:** Product cards have no outer border or shadow. They rely on the image and centered typography. A "Quick View" overlay appears on hover with a semi-transparent cream wash.
- **Inputs:** Simple bottom-border only (the "underline" style) for a minimalist, bespoke feel. Labels should always be visible in the Label-Caps style.
- **Chips:** Rectangular with a 1px border. Used for filters like "Provenance," "Era," and "Material."
- **Lists:** Separated by thin, full-width horizontal rules that stop short of the screen edges, mimicking the layout of a ledger.
- **Specialty Component - The 'Provenance Seal':** A decorative element using a circular border-radius (the only exception to the sharp rule) containing a small brand mark or "Certified" text, used to denote authenticity on item pages.