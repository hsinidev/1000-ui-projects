---
name: Midnight & Gold Vault
colors:
  surface: '#0d141e'
  surface-dim: '#0d141e'
  surface-bright: '#333945'
  surface-container-lowest: '#080e19'
  surface-container-low: '#161c27'
  surface-container: '#1a202b'
  surface-container-high: '#242a35'
  surface-container-highest: '#2f3541'
  on-surface: '#dde2f2'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#dde2f2'
  inverse-on-surface: '#2a313c'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#bfc5e4'
  on-secondary: '#292f48'
  secondary-container: '#424862'
  on-secondary-container: '#b1b7d6'
  tertiary: '#c3ccf8'
  on-tertiary: '#252f51'
  tertiary-container: '#a8b1db'
  on-tertiary-container: '#3a4367'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#dce1ff'
  secondary-fixed-dim: '#bfc5e4'
  on-secondary-fixed: '#141a32'
  on-secondary-fixed-variant: '#3f465f'
  tertiary-fixed: '#dce1ff'
  tertiary-fixed-dim: '#bbc5f0'
  on-tertiary-fixed: '#0f193b'
  on-tertiary-fixed-variant: '#3c4569'
  background: '#0d141e'
  on-background: '#dde2f2'
  surface-variant: '#2f3541'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-edge: 40px
  section-gap: 80px
---

## Brand & Style

This design system is engineered to evoke the atmosphere of an ultra-exclusive private bank's viewing room. The brand personality is prestigious, impenetrable, and quiet—luxury that doesn't need to shout. It targets high-net-worth horology collectors who value security as much as aesthetic excellence.

The design style is **Minimalist-Tactile**. It leverages the clean lines and generous whitespace of modern minimalism but introduces high-fidelity textures and "physical" metaphors common in skeuomorphism. The interface should feel like a physical vault: heavy, deliberate, and engineered with precision. Subtle micro-interactions—such as the soft glint of light across a gold border or a slow, damped expansion of a card—reinforce the sensation of high-end mechanical security.

## Colors

The palette is anchored by "Midnight Navy," a deep, near-black blue that provides more depth and sophistication than pure black. This serves as the canvas for "Brushed Gold" accents, which are used sparingly to denote value, action, and premium status.

- **Backgrounds:** Use the primary navy (#0A1128) for the base layer and the tertiary navy (#121C3E) for elevated surfaces like cards or modals.
- **Accents:** Gold (#D4AF37) is reserved for interactive elements, borders of distinction, and critical brand moments. 
- **Typography:** Use pure white (#FFFFFF) for maximum legibility against dark backgrounds, and the neutral grey (#8E94A2) for secondary metadata and de-emphasized labels.
- **Success/Security:** Subtle greens should be desaturated to maintain the high-end editorial feel, never clashing with the gold.

## Typography

This design system employs a high-contrast typographic pairing to balance heritage with modern security. 

**Noto Serif** is the voice of the vault. It is used for headlines and numerical values (like watch reference numbers or valuations) to provide a traditional, editorial feel reminiscent of high-end horology magazines. 

**Manrope** provides the functional layer. Its clean, geometric proportions ensure that technical data—such as movement specifications or security logs—remains legible and feels modern. All small labels should be set in uppercase Manrope with increased letter spacing to evoke the engraved serial numbers found on luxury timepieces.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy within a centered container to create an intimate, focused experience. Wide margins and generous vertical breathing room (section gaps) are essential to maintain the "exclusive" feel; density is the enemy of luxury.

- **Grid:** Use a 12-column grid for desktop with 24px gutters.
- **Rhythm:** All spacing must be multiples of 8px. Use larger padding (40px+) for card internals to emphasize the "precious" nature of the content within.
- **Alignment:** Center-aligned layouts are preferred for landing and authentication screens, while a structured left-aligned grid is used for the "Collection" view.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and **Subtle Metallic Sheens** rather than heavy drop shadows.

- **Surface Tiers:** The base level is the darkest navy. Components like cards sit one tonal step higher.
- **Inner Glows:** Instead of outer shadows, use 1px inner borders or subtle inner glows in gold (at 10-20% opacity) to make elements feel inset or "carved" into the interface.
- **The "Glass Vault":** Use high-clarity background blurs (30px+) on modals to simulate thick, protective glass.
- **Light Source:** Assume a consistent top-down light source. Gold borders should have a linear gradient (top-left to bottom-right) to simulate a brushed metal texture.

## Shapes

The shape language is **Sharp and Architectural**. To reflect the precision engineering of a luxury watch and the solidity of a vault, rounded corners are strictly avoided.

- **Corners:** Use 0px (sharp) corners for all primary containers, buttons, and input fields.
- **Borders:** Use ultra-fine 1px lines. For secondary elements, use the tertiary navy color for borders. For primary elements, use the gold gradient.
- **Icons:** Use thin-stroke (1px) linear icons. Avoid filled or "bubbly" icon styles.

## Components

### Buttons
- **Primary:** Gold-rimmed (1px border) with no background fill. Text in Gold. On hover, a subtle gold "shimmer" gradient sweeps across the background.
- **Secondary:** Ghost style with white text and a 1px border in the tertiary navy.

### Elegant Cards
- Cards feature no shadow but are distinguished by a slightly lighter navy background (#121C3E) and a 1px border. 
- For "Featured" watches, the card should have a gold top-border (2px) and a subtle grain texture overlay.

### Input Fields
- Underline-only inputs are preferred for a minimalist look. When focused, the 1px white underline transitions into a 1px gold underline with a slow fade.

### The "Vault Lock" Loader
- A custom animation involving interlocking gold concentric circles that rotate into alignment, simulating a safe's combination dial.

### Watch Display
- Use large, high-resolution imagery with "Shadow-masking"—where the edges of the watch photo fade into the midnight navy background, making the timepiece appear to emerge from the darkness.