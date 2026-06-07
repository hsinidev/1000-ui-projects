---
name: Atmospheric Luxe
colors:
  surface: '#0e1320'
  surface-dim: '#0e1320'
  surface-bright: '#343947'
  surface-container-lowest: '#090e1a'
  surface-container-low: '#161b28'
  surface-container: '#1a1f2c'
  surface-container-high: '#252a37'
  surface-container-highest: '#303542'
  on-surface: '#dee2f4'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#dee2f4'
  inverse-on-surface: '#2b303e'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#0d0f0f'
  on-tertiary-container: '#7a7c7c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0e1320'
  on-background: '#dee2f4'
  surface-variant: '#303542'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  technical-sm:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max: 1440px
---

## Brand & Style

This design system is engineered to evoke a sense of quiet power, artistic precision, and exclusivity. It caters to a discerning audience of architects, interior designers, and luxury homeowners who view lighting as both a technical requirement and a sculptural statement. 

The aesthetic is rooted in **Modern Minimalism** infused with **Glassmorphism**. By leaning into high-contrast visuals and dark-mode defaults, the system allows the product—light itself—to become the hero. The interface should feel like a high-end gallery at night: hushed, focused, and expensive. Visual interest is generated through light falloff effects and the interplay between deep shadow and warm luminescence, rather than heavy decorative elements.

## Colors

The palette is strictly curated to reflect the "Golden Hour" in a midnight setting. 

- **Primary (Midnight Blue):** Used for the core canvas. It provides a deep, receding background that allows light effects to pop.
- **Secondary (Warm Gold):** Reserved for highlights, accents, and high-value actions. This color represents the warmth of a filament or a luxury finish.
- **Tertiary (Pure White):** Used exclusively for high-readability text and crisp iconography.
- **Neutral (Surface):** A slightly elevated blue-grey used for container backgrounds to create subtle separation from the primary canvas.

Gradients should rarely be linear; instead, use soft radial glows of Gold (#D4AF37) at 5–10% opacity against the Midnight Blue to simulate the natural dispersion of light.

## Typography

The typographic hierarchy relies on the tension between the classic, authoritative **notoSerif** and the technical, utilitarian **inter**.

- **Headlines:** Use serif fonts to convey heritage and artistry. Large display type should use tighter letter-spacing to feel like a fashion editorial.
- **UI & Technical Specs:** Use the sans-serif font for all interactive elements, data tables, and technical specifications. This ensures maximum legibility and a high-performance, modern feel.
- **Labels:** Small labels and captions should be uppercase with generous tracking (letter-spacing) to maintain a premium, architectural look.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for desktop to ensure the compositions remain balanced and gallery-like, centered within the viewport. 

- **Grid:** A 12-column grid with generous 24px gutters. 
- **Margins:** External margins are wide (64px+) to provide "breathing room," reinforcing the luxury positioning. 
- **Rhythm:** Spacing should follow an 8px base unit. Vertical rhythm is intentionally loose; use white space (or "dark space") as a functional tool to separate different product categories or technical sections. 
- **Alignment:** Lean heavily into asymmetrical layouts for editorial sections to keep the visual interest high, while maintaining strict grid alignment for technical product specifications.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and **Light Falloff** rather than traditional drop shadows.

- **Tonal Layers:** Surfaces are differentiated by slight shifts in color (from Midnight Blue to a slightly lighter Surface Neutral).
- **Glassmorphism:** Overlays, navigation bars, and modal windows use a backdrop-filter (blur: 20px) with a 10% opaque white or gold border. This mimics the appearance of frosted glass or high-end acrylic.
- **Glows:** Instead of black shadows, use "ambient glows." For example, an active card might have a very faint, diffused gold outer glow (#D4AF37 at 15% opacity) to suggest it is illuminated from within.

## Shapes

The shape language is **Soft (Level 1)**, leaning toward architectural rigidity.

- **Standard Corners:** 4px (0.25rem) for buttons and input fields to maintain a crisp, professional edge.
- **Large Containers:** 8px (0.5rem) for cards and modals.
- **Media:** Photography of lighting fixtures should use sharp corners (0px) to feel like framed art pieces, or very large radii (12px+) if used as a floating element.
- **Interactive Elements:** Avoid full-pill shapes; stick to subtle rounding to ensure the UI feels structural rather than "bubbly."

## Components

### Buttons
- **Primary:** Solid Warm Gold (#D4AF37) with Midnight Blue text. No shadow; use a subtle inner glow on hover.
- **Secondary:** Ghost style. Transparent background with a 1px Gold border and Gold text.
- **Tertiary:** Pure White text with a simple underlined transition.

### Cards
- Cards feature a 1px border using a gradient from Gold to Transparent. 
- Backgrounds use a subtle glass blur to separate the card content from the primary background.

### Input Fields
- Dark backgrounds (#1C212E) with 1px border in a muted neutral. 
- On focus, the border transitions to Warm Gold with a soft 4px gold outer "bloom."

### Chips & Tags
- Used for technical attributes (e.g., "LED", "2700K"). 
- Small, uppercase text with a subtle background tint and high letter spacing.

### Additional Elements
- **Light Sliders:** Custom ranges for brightness/temperature should use a gold track with a white "light-source" handle that glows as it is adjusted.
- **Iconography:** Thin-stroke (1px to 1.5px) vector icons in Pure White or Gold.