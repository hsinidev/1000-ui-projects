---
name: Legacy-Loupe
colors:
  surface: '#fcf9f4'
  surface-dim: '#dcdad5'
  surface-bright: '#fcf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ee'
  surface-container: '#f0ede8'
  surface-container-high: '#ebe8e3'
  surface-container-highest: '#e5e2dd'
  on-surface: '#1c1c19'
  on-surface-variant: '#51443a'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f3f0eb'
  outline: '#847469'
  outline-variant: '#d6c3b6'
  surface-tint: '#855324'
  primary: '#552c00'
  on-primary: '#ffffff'
  primary-container: '#704214'
  on-primary-container: '#f1b179'
  inverse-primary: '#fbb980'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#493205'
  on-tertiary: '#ffffff'
  tertiary-container: '#63481b'
  on-tertiary-container: '#ddb880'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdcc1'
  primary-fixed-dim: '#fbb980'
  on-primary-fixed: '#2e1500'
  on-primary-fixed-variant: '#693c0e'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#ffdeae'
  tertiary-fixed-dim: '#e7c188'
  on-tertiary-fixed: '#281800'
  on-tertiary-fixed-variant: '#5c4215'
  background: '#fcf9f4'
  on-background: '#1c1c19'
  surface-variant: '#e5e2dd'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Courier Prime
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  caption:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-edge: 48px
  section-gap: 120px
---

## Brand & Style

The design system is rooted in the "Nostalgic-Editorial" aesthetic, designed to evoke the quiet confidence of a heritage auction house or a luxury horology journal. It targets sophisticated collectors who value provenance, craftsmanship, and the passage of time.

The style is defined by **Minimalism** blended with **Tactile Print Media** influences. It prioritizes the "archival" feel—using the digital screen as a canvas for high-fidelity photography and structured information. The emotional response is one of absolute trust, historical depth, and curated exclusivity. Every layout should feel like a deliberate composition from a high-end physical monograph, utilizing generous whitespace to allow the product—the timepieces—to breathe as artifacts rather than mere inventory.

## Colors

This design system utilizes a restricted, high-contrast palette to maintain an editorial tone.
- **Background (#F5F2ED):** A warm, parchment-inspired Off-White that reduces eye strain and provides a vintage "paper" base.
- **Primary (Sepia - #704214):** Used for key accents, meaningful highlights, and specific call-to-actions, mimicking aged ink or fine leather.
- **Secondary (Obsidian Black - #1A1A1A):** Used for primary text and structural lines to ensure maximum legibility and authority.
- **Tertiary (Brass - #8E6F3E):** A muted metallic used for subtle decorative elements, metadata, and dividers.

Avoid gradients or vibrant digital colors. Color application should remain flat and purposeful, echoing traditional lithographic printing.

## Typography

The typographic scale reinforces the editorial narrative. 
- **Headlines:** `ebGaramond` provides a literary, historical authority. Large-scale displays should use tight letter-spacing to mimic traditional book titling.
- **Body:** `hankenGrotesk` ensures high legibility for long-form horological descriptions, providing a clean, modern counterpoint to the classic serif.
- **Data & Labels:** `courierPrime` is used for serial numbers, technical specifications, and "archival" metadata, evoking the feel of a typewriter-stamped logbook or a watchmaker's tag.

## Layout & Spacing

This design system employs a **Fixed Grid** model reminiscent of a broadsheet magazine. The layout is structured on a 12-column grid with generous gutters to maintain visual breathing room.

Key layout principles:
- **Asymmetry:** Use intentional offset columns for imagery and text to create a dynamic, editorial flow.
- **Vertical Rhythm:** Large section gaps (120px+) differentiate "chapters" of the user journey (e.g., from the Hero to the Collection).
- **The "Frame" approach:** Content should feel framed by wide outer margins, never touching the screen edges, reinforcing the "object-in-a-gallery" presentation.

## Elevation & Depth

To maintain the print-media aesthetic, this design system avoids drop shadows and modern blurs. Depth is achieved through:
- **Hairline Outlines:** 1px borders in `Sepia` or `Black` (at 20% opacity) define containers.
- **Tonal Layering:** Using subtle shifts between Off-White and a slightly darker Sepia-tinted cream to separate the background from foreground modules.
- **Overlapping Elements:** High-fidelity imagery may slightly overlap text or borders to create a physical, "scrapbook" sense of depth without using artificial shadows.

## Shapes

The shape language is strictly **Sharp (0px)** for all primary containers, buttons, and image frames, echoing the precise edges of a cut page or a technical watch blueprint.

To contrast the rigid grid, **Retro-inspired Geometric Shapes** are used as decorative accents:
- **Perfect Circles:** For image masks or "magnification" details.
- **Octagons/Hexagons:** Used as subtle icon backgrounds or ornamental bullet points, referencing watch bezels and movement components.
- **Horizontal Rules:** Thin, 1px lines serve as the primary organizational tool, separating editorial sections.

## Components

### Buttons
Buttons are rectangular with sharp corners. The "Primary" state is a solid Black fill with Off-White text. The "Secondary" state is a 1px Black or Sepia border with no fill. Hovers should trigger a full color inversion (e.g., Black fill becomes Off-White with a border).

### Input Fields
Fields consist of a single 1px bottom border (ledger style) rather than a box. Labels use the `label-caps` (Courier Prime) style, positioned strictly above the line.

### Cards & Collection Items
Watch cards should feature "Archival Photography"—clean, high-contrast shots on neutral backgrounds. Captions are placed below the image using `headline-sm` for the model name and `label-caps` for the price/reference number.

### The "Loupe" Interaction
A custom cursor or hover state that acts as a magnification circle (the 'Loupe'), allowing users to see the intricate details of watch dials and movements in high-fidelity, reinforcing the brand's focus on horological scrutiny.

### Navigation
The header should be minimalist, utilizing `label-caps` for navigation links, separated by small geometric dots or vertical pipes.