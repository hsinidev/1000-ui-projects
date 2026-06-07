---
name: Heritage Loft
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#55423e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#89726d'
  outline-variant: '#dcc1ba'
  surface-tint: '#9c432e'
  primary: '#873420'
  on-primary: '#ffffff'
  primary-container: '#a64b35'
  on-primary-container: '#ffded7'
  inverse-primary: '#ffb4a3'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#504e48'
  on-tertiary: '#ffffff'
  tertiary-container: '#69665f'
  on-tertiary-container: '#e9e5dc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad2'
  primary-fixed-dim: '#ffb4a3'
  on-primary-fixed: '#3d0700'
  on-primary-fixed-variant: '#7d2c19'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e7e2d9'
  tertiary-fixed-dim: '#cac6be'
  on-tertiary-fixed: '#1d1c16'
  on-tertiary-fixed-variant: '#494740'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 32px
  margin-edge: 64px
  section-padding: 120px
---

## Brand & Style

The design system is rooted in the intersection of architectural history and contemporary luxury. It targets discerning investors and urban residents who value craftsmanship, preservation, and the soulful character of revitalized spaces. The emotional response is one of "stately nostalgia"—a feeling of stability, warmth, and enduring quality.

The visual style blends **Minimalism** with **Tactile** elements. By prioritizing generous whitespace and a limited, high-contrast palette, the system allows high-resolution architectural photography to serve as the primary visual driver. Subtle textures suggestive of aged paper or masonry are applied to backgrounds to provide a sense of physical history without cluttering the interface.

## Colors

The palette is derived from the structural materials of industrial-era architecture. **Aged Parchment** serves as the primary canvas, providing a warmer, more sophisticated alternative to pure white. **Exposed Brick Red** is used sparingly for primary actions and highlights, evoking the raw material of revitalization. **Deep Charcoal** provides the necessary weight for typography and structural borders, ensuring the interface feels grounded and authoritative.

Use the Parchment background for all primary surfaces to maintain the "archival" feel. Reserve the Brick Red for high-intent interactions and the Charcoal for architectural lines and headers.

## Typography

This design system utilizes a high-contrast typographic pairing to signal both heritage and professionalism. **Noto Serif** is the voice of the brand, used for large display text and headlines to convey timeless elegance. It should be typeset with slightly tighter letter-spacing in larger sizes to mimic editorial layouts.

**Work Sans** provides a functional counterpoint. Its neutral, architectural proportions ensure maximum legibility for property specifications, body copy, and legal disclosures. Small labels and metadata should always be set in uppercase Work Sans with increased tracking to evoke the aesthetic of vintage architectural blueprints.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to mirror the structured precision of a floor plan. The central content container is capped to maintain optimal line lengths for reading, surrounded by expansive margins that suggest exclusivity and breathing room.

A strict 8px rhythm governs all vertical spacing. Generous section padding (120px+) is encouraged between distinct content blocks to prevent the UI from feeling "crowded," maintaining the airy, expansive atmosphere of a high-ceilinged loft. Use 32px gutters for grid-based listings to allow each property card sufficient visual autonomy.

## Elevation & Depth

Depth is communicated through **Tonal Layers** and **Low-Contrast Outlines** rather than heavy shadows. The interface should feel flat and physical, like documents laid out on a drafting table.

- **Surface Tiers:** Use subtle variations of the neutral parchment (slightly darker or lighter) to define nested areas.
- **Borders:** Instead of shadows, use 1px solid borders in Charcoal (at 15-20% opacity) to define cards and input fields.
- **Micro-Textures:** A faint, monochromatic noise overlay (3% opacity) should be applied to the primary Parchment background to simulate the grain of high-quality paper.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. This choice reflects the hard edges of industrial materials—steel beams, bricks, and window frames. Every UI element, from buttons to image containers, must maintain 90-degree corners to reinforce the architectural and "blueprint" aesthetic.

Geometric accents, such as thin vertical lines or square bullets, may be used as decorative flourishes to guide the eye or break up long passages of text.

## Components

### Sophisticated Buttons
Buttons are rectangular with no corner radius. Primary buttons use a solid Deep Charcoal background with Aged Parchment text. On hover, the background shifts to Exposed Brick Red. Secondary buttons use a 1px Charcoal border with a transparent center.

### Elegant Listing Cards
Cards feature a large, full-width image at the top, followed by a content area with generous internal padding. Use the "Label-Caps" typography style for property status (e.g., "AVAILABLE" or "UNDER RESTORATION") in the top corner. Borders should be minimal—only a 1px bottom stroke to separate the card from the background.

### Before & After Slider
The custom slider component is the centerpiece of the portfolio. It features a thin 1px Charcoal vertical divider with a circular handle in Brick Red. Labels for "Original State" and "Restored" should appear in the "Label-Caps" style at the bottom corners of the component, fading in only when the user interacts with the slider.

### Inputs & Forms
Form fields are underlined only (not boxed) using a 1px Charcoal stroke. The label sits above the line in Work Sans. When focused, the stroke weight increases to 2px and changes to Brick Red.

### Accents
Use thin, decorative horizontal rules to separate major sections, mimicking the lines of a ledger or architectural drawing.