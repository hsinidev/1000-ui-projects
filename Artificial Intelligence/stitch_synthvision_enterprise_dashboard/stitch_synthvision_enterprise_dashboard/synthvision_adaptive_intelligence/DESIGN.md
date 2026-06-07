---
name: SynthVision Adaptive Intelligence
colors:
  surface: '#101418'
  surface-dim: '#101418'
  surface-bright: '#36393f'
  surface-container-lowest: '#0a0f13'
  surface-container-low: '#181c21'
  surface-container: '#1c2025'
  surface-container-high: '#262a2f'
  surface-container-highest: '#31353a'
  on-surface: '#e0e2e9'
  on-surface-variant: '#c5c6ca'
  inverse-surface: '#e0e2e9'
  inverse-on-surface: '#2d3136'
  outline: '#8f9194'
  outline-variant: '#44474a'
  surface-tint: '#c6c6c9'
  primary: '#c6c6c9'
  on-primary: '#2f3133'
  primary-container: '#1a1c1e'
  on-primary-container: '#838486'
  inverse-primary: '#5d5e61'
  secondary: '#ffb3b2'
  on-secondary: '#680012'
  secondary-container: '#ff525c'
  on-secondary-container: '#5b000f'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e5'
  primary-fixed-dim: '#c6c6c9'
  on-primary-fixed: '#1a1c1e'
  on-primary-fixed-variant: '#454749'
  secondary-fixed: '#ffdad8'
  secondary-fixed-dim: '#ffb3b2'
  on-secondary-fixed: '#410008'
  on-secondary-fixed-variant: '#92001e'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#101418'
  on-background: '#e0e2e9'
  surface-variant: '#31353a'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-reg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 1px
  margin-sm: 16px
  margin-md: 32px
  grid-size: 64px
---

## Brand & Style

The brand identity is rooted in the concept of "The Digital Eye"—a synthesis of industrial robustness and surgical precision. This design system communicates high-performance reliability for enterprise computer vision, evoking a sense of absolute control and impenetrable security. 

The visual language draws heavily from **Brutalism** and **Technical HUDs (Heads-Up Displays)**. It rejects soft aesthetics in favor of sharp lines, data density, and structural integrity. Every pixel serves a function, mirroring the logic of the machine learning models it represents. The emotional response is one of authority and clinical accuracy; it is a tool for operators who require split-second insights within high-stakes industrial environments.

## Colors

The palette is engineered for high-contrast visibility in dark-room monitoring environments. 

- **Gunmetal Grey (Primary/Background):** Used in varying shades to create structural hierarchy without breaking the immersion of the dark interface.
- **Laser Red (Accent/Alert):** Reserved for critical data points, active scanning states, and "Target Acquired" indicators. It provides a sharp, aggressive contrast against the desaturated base.
- **Pure White (Typography/Borders):** Used for technical readouts and razor-thin container borders to ensure maximum legibility and a clinical feel.
- **Grid Lines:** Rendered in a low-opacity Gunmetal (#2D3136) to provide a constant spatial reference without overwhelming the content.

## Typography

This design system utilizes a dual-font strategy to balance modern elegance with technical utility. 

**Space Grotesk** is the primary driver for headlines and all technical/data labels. Its geometric, futuristic construction reinforces the "High-Tech" aesthetic. It should be used in uppercase for labels to mimic industrial machinery plates.

**Inter** provides the functional backbone for body copy and dense documentation, ensuring that complex technical descriptions remain readable during extended monitoring sessions.

Monospaced styling is simulated via Space Grotesk with increased letter spacing for all numerical readouts, timestamps, and coordinate data.

## Layout & Spacing

The layout is governed by a **Strict Precision Grid**. A background mesh of 64px cells defines the primary structural blocks. 

- **Grid Lines:** A 1px Gunmetal border should visible globally behind the UI, creating a blueprint effect.
- **Fixed-Width Sidebars:** Navigation and telemetry panels occupy fixed 256px or 320px columns to maintain layout stability during data refreshes.
- **Data Density:** Spacing is compact. Internal padding within cards is kept to a minimum (16px) to maximize the "at-a-glance" information density required for computer vision monitoring.
- **Gutters:** Use 1px borders as gutters rather than whitespace to emphasize the "Industrial" interconnectedness of the modules.

## Elevation & Depth

This system eschews traditional shadows in favor of **Tonal Layering and Bold Borders**. Depth is communicated through architectural stacking rather than light sources.

- **Stacking:** The background is the darkest (#0F1113). Containers sit one level above (#1A1C1E). Active overlays or modals use a slightly lighter grey or a subtle Laser Red outer glow to signify "active" status.
- **HUD Overlays:** Use semi-transparent layers (80% opacity) for floating panels over video feeds, combined with a 1px solid white or red border.
- **Scanning Lines:** A horizontal, high-contrast red line with a soft trailing gradient should move vertically across active video containers to simulate real-time processing.

## Shapes

The shape language is **Strictly Linear**. To maintain the industrial and high-performance vibe, all corners are set to 0px (Sharp). 

- **Corner Details:** For primary containers, use "clipped corners" (45-degree chamfers) on the top-right and bottom-left to evoke military-spec hardware.
- **Framing:** Elements are defined by their stroke rather than their fill. Use thin, 1px lines to frame content, often leaving corners "open" or adding small crosshair "L" brackets at the four corners of an image or video feed.

## Components

- **Buttons:** Rectangular, sharp-edged. Primary buttons use a solid Laser Red fill with White uppercase text. Secondary buttons are ghost-style with a White 1px border. On hover, buttons should trigger a subtle "glitch" shift or a rapid color inversion.
- **Data Cards:** High-density containers with a 1px border. Each card must feature a "Label Header" in the top left, often accompanied by a small flickering "Live" indicator.
- **Status Chips:** Small, rectangular tags. "Optimal" is White/Grey; "Alert" is solid Laser Red. No rounded corners.
- **Input Fields:** Bottom-border only or full 1px box. Focus state changes the border to Laser Red and triggers a scanning animation across the input box.
- **HUD Crosshairs:** Tracking components that follow "detected objects" in video feeds. These consist of four "L" brackets and a small floating text label displaying the confidence score (e.g., "MATCH: 98.4%").
- **Telemetry Lists:** Compact, monospaced lists of coordinates or logs, using zebra-striping with a 2% difference in grey tones for legibility.