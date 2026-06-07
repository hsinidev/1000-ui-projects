---
name: Aerospace-Industrial Training Interface
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#00e639'
  on-tertiary: '#003907'
  tertiary-container: '#00af29'
  on-tertiary-container: '#003807'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#72ff70'
  tertiary-fixed-dim: '#00e639'
  on-tertiary-fixed: '#002203'
  on-tertiary-fixed-variant: '#00530e'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  heading-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: -0.02em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  grid_columns: '12'
  border_width: 1px
---

## Brand & Style
The brand personality is clinical, rigorous, and mission-critical. This design system serves elite athletes and aerospace professionals where performance data is a matter of safety and precision. 

The aesthetic is **Aerospace-Industrial**, a fusion of **Brutalism** and **Tactile** design. It prioritizes "engineering-grade" utility over decoration. Visuals should evoke the cockpit of a high-altitude aircraft or the control panel of a hyperbaric chamber. The UI is characterized by high-contrast information density, rigid structural grids, and functional "glow" states that signify active hardware processes. Every pixel must feel intentional, durable, and synchronized with physical instrumentation.

## Colors
This design system utilizes a high-visibility dark mode palette to minimize eye strain in low-light training environments and maximize the "glow" effect of critical indicators.

- **Matte Black (#121212)** serves as the primary void, providing a non-reflective base for all data.
- **Safety Orange (#FF6700)** is the primary action and warning color, used exclusively for interactive elements and critical alerts.
- **Silver (#C0C0C0)** provides structural definition, used for borders, labels, and secondary metadata.
- **Matrix Green (#00FF41)** is introduced as a functional tertiary color to indicate "Safe" or "Nominal" status in contrast to the orange alerts.

Use subtle radial gradients of #1A1A1A on larger surfaces to simulate brushed metal or composite carbon fiber textures.

## Typography
The typography strategy bifurcates information into **Contextual (Sans-Serif)** and **Technical (Monospaced)**.

- **Inter** is used for headings and descriptive text to ensure rapid readability and a modern, professional feel.
- **JetBrains Mono** is used for all "Live Data" outputs, telemetry, and instructional labels. The fixed-width nature of the font prevents UI jitter during rapid value changes (e.g., pressure readings or heart rate monitoring).

All labels must be in uppercase with increased letter spacing to mimic engraved industrial plate markings. Critical numbers should be oversized to ensure legibility from a distance of 3-5 meters.

## Layout & Spacing
The layout is based on an **Engineering-Grade Fixed Grid**. All components must align to a 4px baseline shift. 

The layout should feel like a technical schematic. Use "Outer Margins" of 32px to create a safety buffer from the edge of the display hardware. Gutters are strictly 16px. Every content block must be enclosed within a defined border—nothing should float "freely" in the vacuum of the Matte Black background. Use 1px Silver borders to delineate modules, creating a clear modular hierarchy.

## Elevation & Depth
This design system rejects traditional shadows. Depth is achieved through **Tonal Layering** and **Luminescent Effects**.

- **Level 0 (Floor):** Matte Black (#0A0A0A) - The deep background.
- **Level 1 (Panels):** Raised surfaces (#1A1A1A) with 1px Silver (#C0C0C0) borders at 20% opacity.
- **Level 2 (Active Elements):** Elements "glow" rather than "rise." Active states use a `box-shadow` of Safety Orange with a 10px-20px blur at low opacity (0.3) to simulate an illuminated hardware button or LED.

Texture is applied to Level 1 surfaces using a subtle noise filter (1-2% opacity) to mimic the grainy finish of industrial-grade plastics or metals.

## Shapes
The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to maintain an aggressive, high-precision industrial aesthetic. 

Chamfered corners (clipped 45-degree angles) may be used on primary containers or buttons to emphasize the aerospace/stealth influence. Use 1px stroke lines for all UI borders to maintain a "wireframe" technical feel.

## Components
- **Buttons:** Rectangular with no border-radius. Primary buttons are solid Safety Orange with Matte Black text. Secondary buttons are transparent with a 1px Silver border.
- **Status Indicators:** Small square pips. A "Glowing" state is achieved with a 4px blur of the indicator's color (Orange for warning, Green for nominal).
- **Inputs:** Underlined or fully boxed in Silver. Labels sit on the top-left border, interrupting the line (industrial stencil style).
- **Cards/Modules:** Must feature a "Header Bar" (24px height) in Silver with Matte Black monospaced text identifying the module (e.g., [O2_SATURATION_01]).
- **Progress Bars:** Segmented blocks rather than smooth fills, mimicking legacy vacuum-fluorescent displays (VFD).
- **Crosshairs/Grids:** Use subtle 0.5px hairlines to mark the center of data visualizations or to connect related data points, reinforcing the engineering schematic look.