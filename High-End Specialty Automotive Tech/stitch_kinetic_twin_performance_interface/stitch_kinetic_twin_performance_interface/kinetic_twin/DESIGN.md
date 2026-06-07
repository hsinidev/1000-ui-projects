---
name: Kinetic-Twin
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#c6c6ce'
  on-secondary: '#2f3036'
  secondary-container: '#45464d'
  on-secondary-container: '#b4b4bc'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e2e2ea'
  secondary-fixed-dim: '#c6c6ce'
  on-secondary-fixed: '#1a1b21'
  on-secondary-fixed-variant: '#45464d'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-display:
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
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  data-numeral:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1'
spacing:
  unit: 4px
  gutter: 16px
  margin-desktop: 32px
  margin-mobile: 16px
  container-max: 1440px
---

## Brand & Style
The design system is engineered to evoke the high-stakes environment of a professional racing cockpit. It prioritizes technical authority, precision, and immediate data legibility. The brand personality is aggressive yet controlled, utilizing a "Tactile-Technical" style that blends hyper-realistic textures (carbon fiber) with futuristic digital overlays. 

The UI should feel like a mission-critical instrument cluster. Every element must appear purpose-built, avoiding decorative fluff in favor of functional density. It targets automotive engineers and performance drivers who require a high-contrast, low-latency visual experience that remains authoritative under high-pressure scenarios.

## Colors
This design system utilizes a restricted, high-impact palette to maintain focus and urgency. 

*   **Carbon Fiber Black (#0A0A0A):** The foundation. Used for deep backgrounds. Apply a subtle 45-degree micro-weave texture overlay at 5% opacity to provide tactile depth.
*   **Neon Red (#FF0000):** The primary kinetic color. Used for critical data, active states, and warnings. It should utilize a CSS `drop-shadow` or `box-shadow` glow effect (0 0 8px) to simulate illuminated hardware.
*   **Engineered Silver (#C0C0C8):** The primary typographic and structural color. It provides a cold, metallic contrast against the dark base.
*   **Onyx Surface (#1A1A1A):** Used for secondary containers and recessed areas to create a tiered hardware appearance.

## Typography
Typography is treated as a precision instrument. 
*   **Space Grotesk** is used for headers and primary telemetry readouts, providing a sharp, geometric edge that feels futuristic.
*   **Inter** serves as the workhorse for technical descriptions and system settings, ensuring legibility at smaller sizes.
*   **JetBrains Mono** is reserved for technical labels, timestamps, and sensor metadata, reinforcing the "digital twin" engineering aesthetic.
*   **Tabular Numerals:** All data-heavy displays must use tabular lining to prevent layout shift during high-speed data refreshes.

## Layout & Spacing
The layout follows a **Rigid Grid** philosophy. Elements are locked into a 12-column system on desktop to mimic the compartmentalized nature of a dashboard.

*   **Density:** High density is preferred. Use a 4px base unit to allow for tight packing of telemetry widgets.
*   **Gutters:** Fixed 16px gutters create clear "channels" between data modules, preventing visual bleeding.
*   **Breakpoints:** 
    *   **Desktop (1200px+):** Full multi-pane cockpit view.
    *   **Tablet (768px - 1199px):** Condensed 8-column view; secondary telemetry moves to overflow drawers.
    *   **Mobile (<767px):** Single column focus on critical vitals (Speed, Battery/Fuel, Alerts).

## Elevation & Depth
Depth is created through **Structural Machining** rather than traditional shadows.
*   **Recessed Containers:** Use inner shadows and darker backgrounds (#050505) to make data wells look "carved" into the carbon fiber dashboard.
*   **Beveled Borders:** Apply 1px solid borders using the Engineered Silver at 20% opacity. Use a "top-light" effect with a slightly brighter 1px line on the top edge of cards to simulate overhead cockpit lighting.
*   **Glow Layers:** Active alerts or critical thresholds use a Neon Red outer glow. This is the only form of "shadow" permitted, used strictly as a functional status indicator rather than an aesthetic depth tool.

## Shapes
This design system utilizes a **Zero-Radius** approach. All corners are 90-degree sharp angles to reflect precision engineering and military-grade hardware. 

To add visual interest without compromising the sharp aesthetic, use **chamfered corners** (angled cuts) at 45 degrees for primary action buttons or decorative frame elements. This reinforces the "machined" look of the interface.

## Components
*   **Buttons:** High-contrast blocks. Primary buttons use a solid Neon Red background with black text. Secondary buttons use a silver 1px border with no fill. State changes should be instantaneous (no slow transitions).
*   **Telemetry Cards:** These are the primary containers. They feature a 1px Silver border (20% opacity) and a Label-Caps header. Data within should be oversized and high-contrast.
*   **Gauges & Sliders:** Linear scales are preferred over circular ones to maximize horizontal space. Use segmented bars to show progress/levels, mimicking LED light strips.
*   **Status Indicators:** Small square pips. Neon Red (Alert), Dim Silver (Inactive), or Pure White (Active).
*   **Input Fields:** Ghost-style inputs with a bottom-only border. When focused, the bottom border glows Neon Red.
*   **Special Component (The Kill-Switch):** A specific modal or button for emergency overrides, featuring a diagonal "hazard" stripe pattern in Red and Black.