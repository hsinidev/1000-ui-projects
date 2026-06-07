---
name: Celestial Technical
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#36393e'
  surface-container-lowest: '#0b0f12'
  surface-container-low: '#181c20'
  surface-container: '#1c2024'
  surface-container-high: '#272a2e'
  surface-container-highest: '#323539'
  on-surface: '#e0e2e8'
  on-surface-variant: '#d6c4ac'
  inverse-surface: '#e0e2e8'
  inverse-on-surface: '#2d3135'
  outline: '#9e8e78'
  outline-variant: '#514532'
  surface-tint: '#ffba38'
  primary: '#ffd79b'
  on-primary: '#432c00'
  primary-container: '#ffb300'
  on-primary-container: '#6b4900'
  inverse-primary: '#7e5700'
  secondary: '#c6c6c9'
  on-secondary: '#2f3133'
  secondary-container: '#454749'
  on-secondary-container: '#b4b5b7'
  tertiary: '#dcdde2'
  on-tertiary: '#2e3134'
  tertiary-container: '#c0c1c6'
  on-tertiary-container: '#4d4f53'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdeac'
  primary-fixed-dim: '#ffba38'
  on-primary-fixed: '#281900'
  on-primary-fixed-variant: '#604100'
  secondary-fixed: '#e2e2e5'
  secondary-fixed-dim: '#c6c6c9'
  on-secondary-fixed: '#1a1c1e'
  on-secondary-fixed-variant: '#454749'
  tertiary-fixed: '#e1e2e7'
  tertiary-fixed-dim: '#c5c6cb'
  on-tertiary-fixed: '#191c1f'
  on-tertiary-fixed-variant: '#44474b'
  background: '#101417'
  on-background: '#e0e2e8'
  surface-variant: '#323539'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the precision of radio-telescopy and deep-space data processing. The brand personality is cold, vast, and intellectually rigorous, mirroring the silent vacuum of space. It evokes a sense of "scientific discovery in progress," positioning the user as the pilot of a high-tech observatory.

The aesthetic follows a **Technical Minimalism** approach blended with **High-Contrast Data Visualization**. It utilizes mathematical patterns—such as Voronoi tessellations or radial coordinate systems—as subtle vector backgrounds to reinforce the theme of structured entropy. Every element is designed to feel like part of a sophisticated instrument, favoring clarity and information density over decorative flair.

## Colors

The palette is anchored in the depths of the cosmos. The primary background is a deep **Midnight Blue** (#05070A), providing a "true dark" canvas that allows data points to pop. UI surfaces and structural elements use **Charcoal** (#1A1C1E) to create subtle separation without breaking the dark-mode immersion.

The primary accent is **Amber Glow** (#FFB300), reserved for critical data points, active states, and frequency peaks. This color simulates the aesthetic of vintage monochromatic monitors while providing high legibility against the dark background. Success and error states should utilize muted spectral tones (e.g., deep nebula violets or frozen cyans) to maintain the celestial theme without relying on standard "stoplight" colors.

## Typography

This design system employs a dual-font strategy to balance legibility with a technical atmosphere. **Inter** is the primary sans-serif for interface navigation, headers, and long-form descriptions, chosen for its neutral and utilitarian character.

For technical readouts, coordinate systems, and numeric data, **JetBrains Mono** (or a similar high-quality monospace font) is used. All labels for telemetry and instrumentation are set in **Space Grotesk** with high letter spacing and uppercase styling to evoke the feel of mission control panels. Typography should be treated as a data element itself; keep line heights tight in charts and generous in documentation.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to simulate the rigid, reliable interface of a laboratory workstation. A 12-column grid is used for the main dashboard, with fixed 16px gutters to ensure that complex charts do not bleed into one another.

Spacing is based on a 4px incremental scale. However, density is prioritized; "whitespace" should be viewed as "dead space" that could otherwise hold telemetry. Use 32px margins for the primary viewport containers to give the content a framed, "screen-within-a-screen" appearance. Navigation should be pinned to the peripheries (sidebar or top bar) to maximize the central area for data visualization.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Low-contrast Outlines** rather than traditional drop shadows. Surfaces are stacked by increasing lightness: the further "forward" an element is, the lighter its Charcoal shade becomes. 

To emphasize the "Celestial Technical" look, use 1px solid borders in a slightly lighter charcoal (#2A2D31) for containers. For active or "pulsing" elements, a very subtle **Amber Glow**—implemented as a 0% to 15% opacity outer glow—is used to simulate light emitting from a sensor or star. Backgrounds may feature a "coordinate grid" pattern at 5% opacity to provide a fixed spatial reference for the eye.

## Shapes

The shape language is strictly **Sharp (0)**. There are no rounded corners in this design system. Every card, button, and input field uses 90-degree angles to reinforce the feeling of precision engineering and mathematical certainty.

Structural elements like frequency bars or coordinate markers should utilize thin 1px or 2px lines. Occasional 45-degree "clipped corners" can be used for primary action buttons to give them a distinctive, aerospace-grade appearance, but the overarching theme is a rigid, rectangular grid.

## Components

- **Technical Cards:** Non-rounded containers with a 1px border. They feature a "Header Bar" using the `label-caps` typography style and a background color slightly lighter than the main canvas.
- **Frequency Charts:** High-contrast line graphs using the Amber Glow accent. The area under the curve should have a subtle vertical scan-line pattern.
- **Coordinate Grids:** Interactive zones with X/Y axes labeled in monospace. Crosshair cursors should follow the mouse to provide exact telemetry readouts.
- **Glowing Status Indicators:** Small square pips that use the Amber Glow (for Active), a muted Slate (for Standby), or a vivid Crimson (for Error). These indicators should have a soft CSS "pulse" animation.
- **Buttons:** Sharp-edged boxes with no fill and an Amber border for secondary actions; solid Amber fill with black text for primary actions. 
- **Input Fields:** Monospace text only, with a blinking underscore cursor to mimic terminal-style entry.
- **Telemetry Strips:** Horizontal or vertical bars displaying real-time scrolling data strings in monospace, used at the top or bottom of the interface as a status "ticker."