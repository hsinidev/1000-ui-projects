---
name: Kinetic-Mirror Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#e9bcb9'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#b08784'
  outline-variant: '#5f3e3d'
  surface-tint: '#ffb3af'
  primary: '#ffb3af'
  on-primary: '#68000e'
  primary-container: '#ff5357'
  on-primary-container: '#5c000b'
  inverse-primary: '#bf0024'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a29'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410006'
  on-primary-fixed-variant: '#930019'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Sora
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Sora
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0.05em
  data-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.1em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '400'
    lineHeight: 12px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

The design system is engineered for high-stakes, real-time automotive telemetry and digital twin management. The brand personality is aggressive, precise, and uncompromising, evoking the sensation of a high-tech cockpit. It targets performance engineers and professional drivers who require immediate data synthesis in high-stress environments.

The visual style is a hybrid of **Glassmorphism** and **Tactile Technical** aesthetics. It utilizes deep layering to simulate depth within a digital "mirror" of a physical vehicle. Key characteristics include:
- **Technical Precision:** Every line and border serves a structural purpose, mimicking HUD (Heads-Up Display) instrumentation.
- **High-Performance Darkness:** A foundation of carbon fiber textures and deep blacks to minimize glare and maximize the "pop" of critical alerts.
- **Kinetic Energy:** The use of neon red glows to signify active states, high-RPM thresholds, or critical system warnings.

## Colors

This design system operates exclusively in **dark mode** to maintain focus and reduce eye strain in cockpit environments. 

- **Deep Carbon (#121212):** The structural base. Use this for the primary background and foundational containers. 
- **Neon Red (#FF0033):** The "Pulse." This high-chroma accent is reserved for interactive states, critical data points, and emergency alerts. It should appear as if it is emitting light.
- **Metallic Silver (#C0C0C0):** The "Frame." Used for secondary UI elements, borders, and icons to provide a cold, industrial feel that contrasts against the dark base.
- **Surface Overlays:** Use semi-transparent variants of the neutral gray (#2A2A2A) with 40-60% opacity to create the glassmorphic layering effect.

## Typography

The typography strategy prioritizes rapid legibility and a "mechanical" feel. 

- **Headlines:** Use **Space Grotesk** for a modern, geometric tech look. Headlines should be tight and impactful.
- **UI & Interaction:** Use **Sora** for its wide stance and excellent readability at various weights, ensuring touch targets and descriptions are clear.
- **Data & Telemetry:** Use **JetBrains Mono** for all numerical readouts, timestamps, and technical logs. The monospaced nature ensures that fluctuating numbers do not cause layout shifts, maintaining a steady "instrument cluster" feel.
- **Hierarchy:** Data labels should always be in uppercase JetBrains Mono to distinguish metadata from the values they describe.

## Layout & Spacing

This design system uses a **4px baseline grid** to ensure mathematical precision in element alignment. 

- **Layout Model:** A fluid grid system optimized for high data density. On mobile, components stack vertically or use horizontal "stripes" for telemetry. On larger displays, a 12-column grid allows for complex dashboards with side-pinned navigation.
- **Data Density:** Use tight spacing (`stack-sm`) between related data points to maximize the information visible on a single screen.
- **Safe Zones:** High-stress environments require larger tap targets. While data is dense, interactive elements (buttons, toggles) must maintain at least a 44px hit area regardless of visual size.

## Elevation & Depth

Depth in this design system is achieved through **translucency and inner glows** rather than traditional drop shadows.

- **Background Layer:** A subtle carbon fiber texture overlay on #121212.
- **Middle Layer (Glass):** Semi-transparent panels with a `backdrop-filter: blur(20px)`. These panels feature a 1px inner border in Metallic Silver (#C0C0C0) at 20% opacity to define the edge.
- **Top Layer (Active):** Interactive or "warning" states utilize a `box-shadow` that mimics a neon glow using Neon Red (#FF0033) with a high spread and low opacity.
- **Z-Axis Hierarchy:** Higher elevation layers are slightly lighter in color and have increased blur intensity to simulate being "closer" to the user.

## Shapes

The shape language is **Soft (0.25rem)**, bordering on sharp. This maintains the aggressive, technical feel of automotive machinery while ensuring the UI doesn't feel "primitive" or "brutalist."

- **Standard Elements:** Use 4px corner radius for buttons and input fields.
- **Dashboard Widgets:** Large containers use 8px (`rounded-lg`) to soften the overall layout and provide a clear frame for the internal data.
- **Status Indicators:** Small pips or status dots remain perfectly square or circular to contrast with the rectangular grid of the interface.

## Components

- **Buttons:** Primary buttons feature a solid Neon Red background with white or black text. Secondary buttons use a transparent background with a 1px Metallic Silver border. All buttons should have a "glossy" top-down gradient to simulate a physical toggle.
- **Data Chips:** Small, monospaced labels used for status (e.g., "ENGINE: OK"). These use the Metallic Silver border and a dim glow if the status is active.
- **Telemetry Cards:** Utilize the glassmorphism effect with a subtle carbon fiber texture visible through the background blur. Headers within cards use the **Data Label** typography style.
- **Input Fields:** Darker than the background layer (#0A0A0A) with a bottom-only Neon Red border that illuminates when the field is focused.
- **Progress Bars / Gauges:** Custom-designed "segmented" bars that fill with Neon Red. Each segment represents a data increment, reinforcing the digital/quantized nature of the software-defined vehicle.
- **Digital Twin Viewport:** A dedicated 3D space with a wireframe or high-gloss metallic shader for the vehicle model, utilizing the Metallic Silver for edges.