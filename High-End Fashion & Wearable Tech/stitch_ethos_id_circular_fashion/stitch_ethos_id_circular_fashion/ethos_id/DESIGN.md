---
name: Ethos-ID
colors:
  surface: '#fbf9f7'
  surface-dim: '#dbdad8'
  surface-bright: '#fbf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1b'
  on-surface-variant: '#424844'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ee'
  outline: '#737874'
  outline-variant: '#c2c8c3'
  surface-tint: '#4f6358'
  primary: '#4c6056'
  on-primary: '#ffffff'
  primary-container: '#65796e'
  on-primary-container: '#f5fff7'
  inverse-primary: '#b6ccbe'
  secondary: '#5f5e5b'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfda'
  on-secondary-container: '#63635f'
  tertiary: '#725455'
  on-tertiary: '#ffffff'
  tertiary-container: '#8d6d6d'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8da'
  primary-fixed-dim: '#b6ccbe'
  on-primary-fixed: '#0c1f17'
  on-primary-fixed-variant: '#374b41'
  secondary-fixed: '#e4e2dd'
  secondary-fixed-dim: '#c8c6c2'
  on-secondary-fixed: '#1b1c19'
  on-secondary-fixed-variant: '#474743'
  tertiary-fixed: '#ffdad9'
  tertiary-fixed-dim: '#e4bdbd'
  on-tertiary-fixed: '#2b1516'
  on-tertiary-fixed-variant: '#5b4040'
  background: '#fbf9f7'
  on-background: '#1b1c1b'
  surface-variant: '#e4e2e0'
typography:
  display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-margin: 32px
  gutter: 24px
---

## Brand & Style

The design system embodies a "Sustainable-Modern" aesthetic, bridging the gap between high-end luxury and technical transparency. It centers on the concept of a product’s "digital soul"—using blockchain data to tell a story of longevity and ethical circularity.

The visual style is a blend of **Minimalism** and **Tactile** design. It prioritizes clarity and whitespace to evoke a sense of premium calm, while utilizing "Paper" textures to ground the digital experience in the physical world of textiles and natural materials. The emotional response should be one of quiet confidence, radical honesty, and artisanal quality.

## Colors

The palette is rooted in organic, muted tones that signal sustainability without sacrificing sophistication.

- **Sage Green (Primary):** A desaturated, earthy green used for primary actions and brand signifiers. It represents growth and environmental stewardship.
- **Off-White (Background/Surface):** A warm, parchment-like neutral that avoids the sterility of pure white. It serves as the primary canvas, providing a soft, high-end feel.
- **Black (Text/Accents):** A deep, near-black used for high-contrast typography and structural borders.
- **Surface Tints:** Subtle variations of the off-white are used to differentiate "Paper" layers and card surfaces.

## Typography

This design system utilizes **Inter** for its systematic, utilitarian precision, which mirrors the accuracy of blockchain verification. 

To maintain a luxury editorial feel, typography should rely on generous line heights and intentional tracking. Headlines use a lighter weight with tighter tracking for a modern look, while labels utilize uppercase styling and increased letter spacing to denote technical data or secondary metadata.

## Layout & Spacing

The layout follows a **fixed grid** philosophy for desktop environments to maintain a controlled, gallery-like experience. For mobile, a fluid grid with substantial side margins (32px) ensures content feels uncrowded.

Spacing is used aggressively to create a "spacious" layout. Vertical rhythms should favor large gaps (LG and XL units) between sections to allow the imagery and "Paper" textures to breathe. Elements are grouped using a tight 8px base, but sections are separated by significant whitespace to emphasize the premium nature of the brand.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layers** and **Paper Textures** rather than traditional heavy shadows.

- **Texture:** All primary surfaces should feature a subtle grain or paper-fiber overlay (at ~3-5% opacity) to create a tactile, physical quality.
- **Shadows:** Use extremely diffused, low-opacity ambient shadows (e.g., Blur 30px, Y 10px, 4% Opacity Black). Shadows should feel like a natural light source hitting a thick sheet of paper.
- **Layers:** Use "Off-White" for the background and a slightly brighter white for cards to create a subtle lift. Interactive elements may use a soft inner-shadow on press to simulate a tactile "squish."

## Shapes

The shape language is defined by "Rounded" (Level 2) geometry. This softens the technical aspect of blockchain data and aligns with the organic nature of sustainable fashion.

- **Standard Elements:** 0.5rem (8px) radius for buttons and input fields.
- **Cards/Containers:** 1.5rem (24px) radius to create a distinct, high-end silhouette that stands out against the grid.
- **Pills:** Used exclusively for "Status" or "Blockchain Verified" tags to differentiate them from functional buttons.

## Components

### Cards
High-end cards are the cornerstone of the UI. They feature a 24px corner radius, a subtle paper texture, and a 1px border in a slightly darker neutral tone. Content within cards should have at least 32px of internal padding.

### Buttons
Primary buttons use the Sage Green background with white or black text. They should feel tactile—consider a very subtle gradient or a soft 1px "rim light" highlight at the top edge. 

### Icons
Use elegant, thin-stroke (1px to 1.5px) icons. Icons should be functional but minimalist, avoiding complex fills.

### Blockchain Transparency Tags
These are unique components that display "Verified" status. They should use the "label-caps" typography and a small, pulsing green dot to indicate live data or authenticity.

### Input Fields
Fields are minimalist, featuring only a bottom border or a very light-filled background with no side borders. Labels should be small and float above the field.

### Tactile Elements
Include large, touch-friendly toggles and sliders that mimic physical switches found on luxury appliances or high-end apparel hardware.