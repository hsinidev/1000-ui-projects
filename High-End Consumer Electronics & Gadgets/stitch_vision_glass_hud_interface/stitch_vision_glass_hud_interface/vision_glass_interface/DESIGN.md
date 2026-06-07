---
name: Vision-Glass Interface
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1c1b1d'
  surface-container: '#201f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e5e1e4'
  on-surface-variant: '#c7c5ce'
  inverse-surface: '#e5e1e4'
  inverse-on-surface: '#313032'
  outline: '#919098'
  outline-variant: '#46464d'
  surface-tint: '#c1c4e6'
  primary: '#c1c4e6'
  on-primary: '#2b2f49'
  primary-container: '#0a0e27'
  on-primary-container: '#777a99'
  inverse-primary: '#595c79'
  secondary: '#ddfcff'
  on-secondary: '#00363a'
  secondary-container: '#00f1fe'
  on-secondary-container: '#006a70'
  tertiary: '#bfc4ef'
  on-tertiary: '#292e51'
  tertiary-container: '#070c2e'
  on-tertiary-container: '#757aa1'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dee0ff'
  primary-fixed-dim: '#c1c4e6'
  on-primary-fixed: '#161a33'
  on-primary-fixed-variant: '#414561'
  secondary-fixed: '#74f5ff'
  secondary-fixed-dim: '#00dbe7'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#dfe0ff'
  tertiary-fixed-dim: '#bfc4ef'
  on-tertiary-fixed: '#13183a'
  on-tertiary-fixed-variant: '#3f4468'
  background: '#131315'
  on-background: '#e5e1e4'
  surface-variant: '#353437'
typography:
  display-data:
    fontFamily: spaceGrotesk
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-h1:
    fontFamily: spaceGrotesk
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-h2:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '300'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  body-sm:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '300'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-mono:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  fov-safe-margin: 48px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 40px
---

## Brand & Style

This design system is engineered for an immersive, high-performance Augmented Reality environment. It evokes a sense of hyper-precision, technical sophistication, and immediate data accessibility. The brand personality is clinical yet visionary, prioritizing information density without sacrificing clarity.

The visual style is a hybrid of **HUD-Minimalism** and **Glassmorphism**. It utilizes ultra-thin lines and semi-transparent surfaces to ensure that the interface feels integrated into the user's physical environment rather than a layer on top of it. The aesthetic mimics high-end aerospace instrumentation—functional, lightweight, and cutting-edge.

## Colors

The palette is optimized for AR transparency and OLED efficiency. 

- **Primary (Deep Indigo):** Used for depth layers and background "shielding" where high legibility is required against bright real-world environments.
- **Secondary (Neon Cyan):** The primary interactive color. Used for active states, borders, and data visualizations. It should be applied with a subtle outer glow (0-2px) to simulate light emission.
- **Accent (Pure White):** Reserved for primary text and critical thin-line accents to provide maximum contrast.
- **Tertiary:** A mid-tone indigo for subtle container grouping.

All overlays must utilize variable opacity (typically 40% to 80%) to maintain the "Glass" effect, allowing the real world to remain visible behind the interface.

## Typography

Typography in this design system functions as a data readout. **Space Grotesk** is used for headlines and labels to provide a technical, geometric edge. **Inter** is used for body copy to ensure maximum legibility at thin weights during movement.

To maintain the HUD aesthetic, utilize "Light" (300) and "Regular" (400) weights almost exclusively. Avoid bold weights, as they can cause visual "blooming" in AR lenses; instead, use Neon Cyan color or capitalization to denote emphasis.

## Layout & Spacing

The layout philosophy is based on **Field of View (FoV) Clarity**. Information is organized on a 4px modular grid. 

A "Safe Zone" margin of 48px is enforced on all sides of the display to prevent UI clipping at the edge of the glasses' lenses. Content is arranged in "Modules" that can be anchored to real-world objects or fixed to the user's viewport. The system uses a **No-Grid Fluid model**, where elements float with precise coordinate-based positioning, ensuring that the center of the user's vision remains unobstructed unless an alert is active.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and Z-axis layering rather than traditional shadows. 

1.  **Backdrop Blur:** Surfaces use a high-density Gaussian blur (10px - 20px) to separate the UI from the visual noise of the real world.
2.  **Luminescent Borders:** Layers are distinguished by 1px solid borders in Neon Cyan or 20% White.
3.  **Z-Tracking:** Interactive elements exist on a closer Z-plane than background data, appearing slightly larger and more vibrant.
4.  **Subtle Glows:** Instead of drop shadows, active elements emit a Cyan outer glow (4-8px blur, low opacity) to indicate "power-on" states.

## Shapes

The design system utilizes **Sharp (0px)** corners to maintain a technical, high-precision instrument aesthetic. 

Structural elements should feel like they were machined or digitally rendered with absolute accuracy. Octagonal "clipped" corners (45-degree cuts) may be used for decorative elements or specific data tags to further the HUD readout visual language. All stroke widths are strictly 1px.

## Components

- **Buttons:** Ghost-style buttons with 1px Neon Cyan borders. Upon hover or focus, the button fills with a 10% Cyan tint and the border glow intensifies. Text is always centered and uppercase.
- **Glass Cards:** Semi-transparent Deep Indigo (#0A0E27 at 60% opacity) with a 1px White (20% opacity) top-border to simulate a light catch on glass edges.
- **Data Readouts:** Small-caps labels paired with thin-weight numbers. Often accompanied by a 1px "scanning" line animation.
- **Icons:** Custom 24px grid icons using 1px stroke weight. No fills; icons must be "hollow" to preserve background visibility.
- **Status Indicators:** Small geometric shapes (triangles or squares) that blink or pulse in Neon Cyan to indicate active processes.
- **Input Fields:** A simple 1px bottom-line with bracketed corners. The cursor is a blinking Cyan block.