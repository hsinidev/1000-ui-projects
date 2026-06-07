---
name: Spatial-Lab
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#333b3b'
  surface-container-lowest: '#081010'
  surface-container-low: '#151d1e'
  surface-container: '#192122'
  surface-container-high: '#232b2c'
  surface-container-highest: '#2e3637'
  on-surface: '#dce4e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dce4e4'
  inverse-on-surface: '#2a3232'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c3c6d7'
  on-secondary: '#2c303d'
  secondary-container: '#454957'
  on-secondary-container: '#b5b8c9'
  tertiary: '#f9f9f9'
  on-tertiary: '#303030'
  tertiary-container: '#dcdcdc'
  on-tertiary-container: '#606060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#dfe2f3'
  secondary-fixed-dim: '#c3c6d7'
  on-secondary-fixed: '#171b28'
  on-secondary-fixed-variant: '#434654'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#0d1515'
  on-background: '#dce4e4'
  surface-variant: '#2e3637'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.2em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  panel-padding: 24px
  safe-area: 64px
---

## Brand & Style
The design system is engineered for a high-performance AR educational environment where clarity and immersion are paramount. The brand personality is clinical, precise, and authoritative, mirroring the aesthetic of advanced aerospace or medical diagnostic interfaces. 

The style utilizes a **HUD-based Glassmorphism** approach. It avoids heavy, solid containers in favor of light-emitting surfaces and semi-transparent planes that allow the real-world environment to remain visible behind the interface. Every element is designed to feel like a projected holographic layer, utilizing high-contrast outlines and "active" light states to indicate interactivity. The emotional response is one of heightened focus and technological empowerment.

## Colors
The palette is rooted in a "Void and Neon" philosophy. 
- **Deep Indigo (#0A0E1A)** serves as the primary substrate for semi-transparent surfaces, providing enough contrast for legibility against varied physical backgrounds.
- **Neon Cyan (#00F3FF)** is the "Active Light" color, used for all interactive borders, text readouts, and data points. It represents energy and connectivity.
- **Black (#000000)** is reserved for absolute occlusions or deep shadows within the HUD to simulate depth.

Transparency is a functional requirement: background surfaces should never be 100% opaque. Use the `background_overlay` for glass panels to maintain the clinical, lightweight feel of an AR projection.

## Typography
This design system utilizes a dual-font strategy to balance futuristic geometry with technical readability. 
- **Space Grotesk** is used for primary headers and large display numbers. Its aggressive, wide proportions reinforce the cutting-edge narrative.
- **JetBrains Mono** is the workhorse for all body text, technical readouts, and UI labels. The monospaced nature ensures that fluctuating data values do not cause layout shifts and maintains the "terminal" aesthetic.

All labels should be rendered in uppercase with increased letter-spacing to mimic instrument panel markings.

## Layout & Spacing
The layout philosophy follows a **Fixed HUD Grid** model. Since the platform is AR-integrated, the UI is anchored to a "safe zone" within the user's field of vision, avoiding the extreme edges where lens distortion occurs.

A strict 4px grid system ensures alignment of geometric lines and borders. Panels should feel modular and detachable, using consistent 16px gutters. Important technical data should be pinned to the corners of the viewport, while the central area remains clear for holographic educational content.

## Elevation & Depth
Depth is communicated through **Optical Luminance and Backdrop Blurs** rather than traditional shadows.
- **Level 1 (Base):** Subtle, 70% opacity Deep Indigo planes with a 20px backdrop blur.
- **Level 2 (Active):** Panels with a 1px Neon Cyan stroke and a faint inner glow.
- **Level 3 (Alert/Focus):** Increased stroke weight (2px) and a pulsed "breathing" animation on the border to draw immediate ocular attention.

To simulate holographic projection, higher-elevation elements should have a slightly higher Cyan saturation and a faint "scanline" texture overlay.

## Shapes
The shape language is strictly **Sharp and Geometric**. All containers, buttons, and input fields must use 0px border-radius. To add visual interest, use "clipped corners" (45-degree chamfers) on larger panels to reinforce the military-grade hardware aesthetic. Circular elements are reserved exclusively for gesture indicators and radial data visualizations to distinguish them from structural UI.

## Components
- **Buttons:** Rectangular with 1px Cyan borders. Hover/Active states trigger a full Cyan fill with Black text. Include small "corner marks" (L-shaped brackets) to define the hit area.
- **Circular Gesture Indicators:** Peripheral rings that pulse when a hand gesture is detected. Use concentric dashed lines to show progress or "lock-on" status.
- **Input Fields:** Bottom-aligned Cyan borders only. Placeholder text should look like a command-line prompt (`> _`).
- **Cards/Holographic Overlays:** Semi-transparent Indigo backgrounds. Header sections should be separated by a thin, glowing horizontal rule. Include "X-Y" coordinates in the corners for a technical readout effect.
- **Data Visualizations:** High-contrast line graphs and radar charts. Use no fills, only glowing Cyan strokes and dots.
- **Navigation:** A minimal vertical "Rail" on the left side of the FOV, using geometric icons without labels unless hovered.