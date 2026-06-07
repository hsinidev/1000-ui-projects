---
name: Scientific-Zen Methodology
colors:
  surface: '#fbf9f7'
  surface-dim: '#dbdad8'
  surface-bright: '#fbf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1b'
  on-surface-variant: '#424845'
  inverse-surface: '#303130'
  inverse-on-surface: '#f2f0ef'
  outline: '#727875'
  outline-variant: '#c2c8c4'
  surface-tint: '#4e635a'
  primary: '#4e635a'
  on-primary: '#ffffff'
  primary-container: '#8da399'
  on-primary-container: '#263932'
  inverse-primary: '#b5ccc1'
  secondary: '#5e604d'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1c9'
  on-secondary-container: '#636451'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#9d9e9e'
  on-tertiary-container: '#343536'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#e4e4cc'
  secondary-fixed-dim: '#c8c8b0'
  on-secondary-fixed: '#1b1d0e'
  on-secondary-fixed-variant: '#474836'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f7'
  on-background: '#1b1c1b'
  surface-variant: '#e4e2e0'
typography:
  h1:
    fontFamily: Literata
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Literata
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Literata
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max-width: 1280px
  gutter: 24px
  margin: 40px
  section-gap: 80px
---

## Brand & Style

This design system establishes a visual language centered on the intersection of biological precision and holistic tranquility. The target audience includes health-conscious individuals and medical professionals who require dense epigenetic data presented with clarity and calm. 

The style is a fusion of **Organic Minimalism** and **Modern Corporate**. It prioritizes high-contrast readability to ensure scientific data is accessible, while utilizing fluid, organic containers to echo the natural complexity of DNA. The emotional response is one of "Informed Peace"—users should feel that the information is technically rigorous yet personally nurturing. Visual clutter is eliminated in favor of intentional whitespace, reinforcing a laboratory-clean environment softened by botanical tones.

## Colors

The palette is derived from natural elements to ground the scientific nature of the product. 
- **Sage Green (#8DA399)**: The primary brand color, representing growth, vitality, and clinical calm. It is used for primary actions and key data highlights.
- **Pale Wood (#F5F5DC)**: Serving as the secondary surface color, it provides a warm, tactile contrast to the clinical white, used for grouping content and subtle section differentiation.
- **Clean White (#FFFFFF)**: The base for all workspaces to ensure maximum contrast and a "Scientific-Zen" aesthetic.
- **Neutral Dark (#2D3431)**: A deep, desaturated green-charcoal used for high-readability typography, replacing pure black to maintain the organic feel.

## Typography

This design system utilizes a dual-font strategy to balance editorial elegance with functional data density.

**Headings (Literata):** A scholarly serif that conveys authority and biological heritage. Large headlines should use tighter letter spacing to maintain a premium feel. It is reserved for titles, narrative summaries, and section headers.

**Body & Data (Inter):** A neutral, systematic sans-serif chosen for its exceptional legibility in data-heavy contexts. All DNA sequences, nutritional values, and technical instructions are rendered in Inter to ensure zero ambiguity. Small labels should utilize increased letter spacing and bold weights for rapid scanning.

## Layout & Spacing

The layout follows a **Fixed Grid** model with a 12-column structure, providing a rigid foundation for complex data visualization. However, individual containers within the grid utilize fluid internal padding to maintain the "Zen" aesthetic.

- **Whitespace:** Generous section gaps (80px+) are mandatory to prevent cognitive overload.
- **Rhythm:** An 8px linear scale governs all padding and margins, ensuring a disciplined alignment that mirrors the precision of genetic sequencing.
- **Data Densities:** Use the 12-column grid to create asymmetric layouts—for example, a 4-column summary side-by-side with an 8-column data visualization.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Soft Ambient Shadows** rather than aggressive highlights.

1.  **Base Layer:** Clean White (#FFFFFF).
2.  **Surface Layer:** Pale Wood (#F5F5DC) for cards or secondary navigation bars, creating a soft, tactile lift.
3.  **Shadows:** Use extremely diffused, low-opacity shadows (Opacity: 4-6%) with a subtle Sage Green tint (#8DA399). This mimics natural light passing through a leaf, avoiding the "plastic" feel of standard grey shadows.
4.  **Borders:** Fine, 1px strokes in a darkened version of Sage Green are used for input fields and data cells to maintain scientific sharpness without breaking the zen flow.

## Shapes

The shape language is **Organic and Soft**. While the grid is structured, the elements themselves avoid harsh 90-degree angles.

- **Primary Containers:** Use the `rounded-lg` (1rem) setting to mimic cellular structures.
- **Secondary Elements:** Buttons and tags use `rounded-xl` (1.5rem) or full pill shapes to feel approachable and "hand-carved."
- **Fluidity:** Incorporate non-symmetrical "blob" shapes occasionally in the background (using Pale Wood) to break the rigidity of data tables and evoke biological fluidity.

## Components

### Buttons & Controls
- **Primary Button:** Solid Sage Green with White typography. High roundedness (Pill).
- **Secondary Button:** Outlined Sage Green with a subtle Pale Wood hover state.
- **Selection Controls:** Radio buttons and checkboxes should feature a custom "double-helix" checkmark icon to reinforce the brand's DNA focus.

### Cards & Summaries
Cards are the primary vehicle for genetic insights. They utilize a Pale Wood background with a 1px Sage stroke. The header of the card always uses the Serif typeface for the insight title, followed by Sans-serif for the supporting data points.

### Data Visualization
Charts should prioritize clarity. Use Sage Green for the primary data line and Pale Wood for background chart areas. Avoid multi-colored "rainbow" charts; instead, use varying shades and opacities of Sage Green to maintain a monochromatic, focused aesthetic.

### Iconography
Icons must follow a "Double-Helix" style—thin, continuous lines with soft curves. Avoid sharp edges or filled-in "heavy" icons. Every icon should feel like it was drawn with a single stroke of a technical pen.

### Information Callouts
"Epigenetic Tips" are housed in fluid, organic-shaped containers with a Sage Green tint, set apart from the standard grid to draw the eye to actionable advice.