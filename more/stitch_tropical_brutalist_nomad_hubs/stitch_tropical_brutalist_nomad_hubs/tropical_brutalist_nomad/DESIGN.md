---
name: Tropical Brutalist Nomad
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bbcbbb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#869486'
  outline-variant: '#3d4a3e'
  surface-tint: '#4ae183'
  primary: '#54e98a'
  on-primary: '#003919'
  primary-container: '#2ecc71'
  on-primary-container: '#005027'
  inverse-primary: '#006d37'
  secondary: '#ffb4a4'
  on-secondary: '#630e00'
  secondary-container: '#b72301'
  on-secondary-container: '#ffcdc2'
  tertiary: '#3de4e7'
  on-tertiary: '#003738'
  tertiary-container: '#00c7ca'
  on-tertiary-container: '#004e4f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6bfe9c'
  primary-fixed-dim: '#4ae183'
  on-primary-fixed: '#00210c'
  on-primary-fixed-variant: '#005228'
  secondary-fixed: '#ffdad3'
  secondary-fixed-dim: '#ffb4a4'
  on-secondary-fixed: '#3d0600'
  on-secondary-fixed-variant: '#8c1800'
  tertiary-fixed: '#5af8fb'
  tertiary-fixed-dim: '#2ddbde'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#004f51'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.03em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  grid-margin: 32px
  grid-gutter: 24px
---

## Brand & Style
This design system establishes a visual language for a nomadic lifestyle that balances urban grit with natural tranquility. The brand personality is grounded, adventurous, and uncompromisingly modern. It targets sophisticated digital professionals who value architectural integrity and high-performance infrastructure as much as lush, tropical environments.

The UI employs a **Brutalist-Minimalist** hybrid style. It uses raw, "honest" materials like concrete textures and heavy borders to convey structural stability, contrasted against vibrant botanical photography that breathes life into the rigid layouts. The emotional response is one of "calculated escape"—a feeling of being in a high-tech hub nestled within a wild jungle.

## Colors
The palette is rooted in the "Urban Jungle" concept. The foundation is built on deep charcoals and slate greys that mimic raw concrete and asphalt. 

- **Primary (Monstera Green):** A lush, vibrant green used for success states and key brand indicators.
- **Secondary (Sunset Orange):** A high-energy accent reserved for primary Call-to-Actions and urgent notifications.
- **Tertiary (Electric Teal):** Used for data visualization and interactive elements like links or active toggles.
- **Backgrounds:** Use a layered approach of nearly-black neutrals with subtle grain overlays to simulate depth and texture.

## Typography
The typography strategy creates a tension between technical precision and bold expression. 

**Space Grotesk** is used for all headings and UI labels to provide a futuristic, architectural feel. Its geometric nature complements the Brutalist grid. Large headings should be tightly tracked to emphasize their weight.

**Work Sans** serves as the workhorse for body copy and descriptions. Its neutral, highly legible characteristics ensure that long-form content remains readable against textured backgrounds. Data points (like WiFi speeds or pricing) should use the "data-mono" style to emphasize technical reliability.

## Layout & Spacing
The layout follows a **12-column fixed grid** that feels structural and intentional. Negative space is not "empty" but "air," used to separate heavy content blocks.

- **Structural Grid:** Use 2px solid borders (Slate Grey or Primary Green) to define sections instead of shadows.
- **Asymmetry:** Allow high-quality photography of tropical foliage to break the grid, overlapping text containers or borders to create a sense of organic growth over a man-made structure.
- **Rhythm:** Use an 8px baseline grid to ensure all elements align to the architectural "bones" of the design system.

## Elevation & Depth
In this design system, elevation is achieved through **structural layering and borders** rather than soft shadows.

- **Borders:** Every container uses a minimum 2px solid border. This replaces the need for elevation levels.
- **Surface Layering:** Use a "Concrete-on-Coal" approach. The base background is the darkest neutral; secondary surfaces (cards, inputs) are slightly lighter slate with a 3% grain overlay.
- **Overlays:** Images of tropical plants should use "Cut-out" masking, placed on a Z-index above the rigid grid lines to create physical depth without using blur or transparency.

## Shapes
The shape language is strictly **Sharp (0px)**. All buttons, cards, and input fields must have square corners to maintain the Brutalist architectural aesthetic. 

- **Structural Elements:** Use thick, 2px to 4px strokes for borders.
- **Iconography:** Icons should be thin-stroke, geometric, and avoid rounded terminals.
- **Emphasis:** Use "Block-shadows"—a solid offset fill behind a container (usually in Primary Green) to indicate focus or activity.

## Components

- **Buttons:** Rectangular with no border-radius. Primary buttons use a solid Secondary Orange fill with black text. Secondary buttons use a transparent background with a 2px Primary Green border.
- **Data Cards:** Designed for high-density information. They must include clear labels for technical stats (e.g., "900 Mbps Down") using the "data-mono" typography. Borders are mandatory.
- **Inputs:** Underlined or fully boxed with 2px borders. Use Primary Green for the focus state.
- **Chips/Badges:** Small, rectangular tags with "label-sm" typography. Use tertiary teal for "Available" states and deep grey for "Booked."
- **Image Containers:** Large-format photography of tropical locations. Where possible, apply a "concrete" texture multiply-blend over the top of the image to unify the organic and the industrial.
- **Navigation:** Vertical or horizontal, strictly aligned to the grid with visible "separators" between items to mimic architectural blueprints.