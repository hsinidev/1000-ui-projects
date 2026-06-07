---
name: High-Performance Athleticism
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c7c9ab'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#303031'
  outline: '#919378'
  outline-variant: '#464932'
  surface-tint: '#bdd200'
  primary: '#ffffff'
  on-primary: '#2e3400'
  primary-container: '#d8ef00'
  on-primary-container: '#5f6a00'
  inverse-primary: '#596400'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8ef00'
  primary-fixed-dim: '#bdd200'
  on-primary-fixed: '#1a1e00'
  on-primary-fixed-variant: '#434b00'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for elite performance, speed, and raw energy. The brand personality is aggressive and motivating, targeting athletes and high-achievers who demand excellence. The visual language is inspired by track-and-field aesthetics and high-end automotive design, favoring movement and high-contrast tension over softness.

The design style is **High-Contrast / Bold**. It utilizes a dark, immersive environment where the neon primary color acts as a high-visibility signal for action. Layouts prioritize large-scale, impactful imagery of human movement, often using extreme crops and dynamic angles to evoke a sense of forward momentum.

## Colors

The palette is anchored by a lethal combination of **Deep Black (#000000)** and **Neon Yellow (#E6FF00)**. This pairing ensures maximum legibility and visual punch, mimicking safety gear and high-intensity sporting apparel.

- **Primary:** Neon Yellow is reserved for calls-to-action, progress indicators, and critical data points. It should be used sparingly but boldly to guide the eye.
- **Surface Tiers:** Depth is achieved through a hierarchy of dark grays:
    - **Surface 0:** #000000 (Pure Black for backgrounds)
    - **Surface 1:** #121212 (Primary containers)
    - **Surface 2:** #1A1A1A (Secondary cards and hover states)
    - **Surface 3:** #2E2E2E (Input fields and borders)
- **Accents:** Subtle glows using the primary color are permitted to simulate light-emitting hardware displays.

## Typography

Typography in this design system is built for speed and impact. **Space Grotesk** is used for headlines to provide a technical, geometric edge. Headlines should frequently utilize uppercase transformations and tight tracking to emphasize the "condensed" and "strong" aesthetic.

**Lexend** is the primary body face, chosen for its exceptional readability and athletic character. It provides a human, accessible counterpoint to the technical rigidity of the display type. 

Vertical rhythm is strict; use the `label-caps` style for all navigational elements and data headers to maintain a disciplined, military-grade information hierarchy.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on desktop (12 columns) and a fluid model on mobile. A strict 8px spacing rhythm ensures consistency across the interface. 

Whitespace is used strategically—not for "airy" minimalism, but to create "lanes" of focus. Margins are generous at the edges of the screen to keep content centered and intense. Use `lg` and `xl` spacing to separate major content blocks, creating a rhythmic "pulse" as the user scrolls through the platform.

## Elevation & Depth

This design system eschews soft, naturalistic shadows in favor of **Tonal Layers** and **Neon Emittance**. 

1.  **Depth via Value:** Elements closer to the user are lighter in value (using Surface 1 or Surface 2 grays) against the Pure Black background.
2.  **Hard Outlines:** Use 1px or 2px solid borders in Neon Yellow or Surface 3 to define boundaries. 
3.  **The Glow:** Active states and high-priority metrics utilize a "Neon Glow"—a drop shadow with 0 spread, a subtle blur (8px-16px), and #E6FF00 at 30-50% opacity. This creates a high-performance "head-up display" (HUD) effect.

## Shapes

The shape language is defined by **Sharp Edges (0px)**. There are no rounded corners in this design system. Every button, card, and input field must have 90-degree angles to convey precision, discipline, and uncompromising performance.

Diagonal clipping (angled corners) at 45 degrees may be used for decorative elements or specific "Hero" buttons to further emphasize the athletic, aerodynamic aesthetic.

## Components

### Buttons
- **Primary:** Solid #E6FF00 background with #000000 text. Sharp corners. No border. On hover, apply a subtle neon outer glow.
- **Ghost:** Transparent background with a 2px #E6FF00 border. Text in #E6FF00.

### Cards
- Backgrounds use Surface 1 (#121212). Borders are 1px Surface 3 (#2E2E2E).
- Content should be pinned to a strict internal padding of 24px (md).

### Input Fields
- Underline style or fully enclosed sharp boxes.
- Focus state: Border transitions from Surface 3 to Primary Neon Yellow with a 1px solid weight.

### Chips & Tags
- Rectangular with all-caps label text. Backgrounds use high-contrast dark grays to separate from the main surface.

### Additional Components
- **Performance Gauges:** Use thick, non-rounded stroke weights for circular or linear progress bars to track workout completion.
- **Metric Tiles:** Large-scale display typography paired with the `label-caps` description for instant data recognition.