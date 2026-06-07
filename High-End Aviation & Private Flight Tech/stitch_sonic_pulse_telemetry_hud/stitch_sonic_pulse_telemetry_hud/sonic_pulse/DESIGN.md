---
name: Sonic-Pulse
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
  surface-tint: '#ffb596'
  primary: '#ffb596'
  on-primary: '#581e00'
  primary-container: '#ff6600'
  on-primary-container: '#561d00'
  inverse-primary: '#a33e00'
  secondary: '#c7c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#969797'
  on-tertiary-container: '#2e3030'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb596'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '300'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.2'
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for high-stakes aerospace environments, prioritizing cognitive efficiency, rapid data processing, and technical precision. The brand personality is clinical and high-performance, evoking the atmosphere of a next-generation flight deck. 

The aesthetic is a fusion of **Minimalism** and **High-Contrast Boldness**. It rejects decorative fluff in favor of raw, functional utility. The UI is designed to feel "kinetic"—as if it is moving at Mach speeds—using thin, sharp lines and glowing indicators that cut through the darkness of the Charcoal base. The user experience should feel like operating a sophisticated instrument rather than browsing a website; every pixel serves a tactical purpose.

## Colors

The color palette is restricted to a high-contrast, mission-critical scheme. 

- **Charcoal (#121212):** The foundation. A deep, non-reflective black used to minimize glare and provide a void-like backdrop for data.
- **Safety Orange (#FF6600):** The primary signal color. Used exclusively for active states, critical alerts, and interactive "hot" zones. It must be used sparingly to maintain its urgency.
- **Brushed Steel (#A0A0A0):** The structural skeleton. Used for borders, dividers, and inactive icons, mimicking the metallic surfaces of an airframe.
- **Pure White (#FFFFFF):** Used for primary data readouts and text to ensure maximum legibility against the dark background.

Glowing accents should utilize the primary orange with a soft 4-8px outer blur to simulate illuminated hardware displays.

## Typography

The typography system mimics a Heads-Up Display (HUD). It utilizes **Space Grotesk** for structural headings to provide a futuristic, geometric feel, and **JetBrains Mono** for all telemetry, labels, and body text to ensure technical clarity and fixed-width alignment.

Text should be kept "thin-line" to maintain the minimalist aesthetic. Large data readouts (Data-Display) are the hero of the interface, ensuring pilots can read Mach speeds or altitude at a glance. All labels should be uppercase to reinforce the authoritative, military-spec nature of the system.

## Layout & Spacing

The layout is modeled after a **cockpit instrument cluster**. It uses a strict 12-column grid but allows for modular "pods" or "widgets" that function as independent instruments.

- **Modular Grid:** Elements are grouped into rectangular sectors defined by thin 1px Brushed Steel borders.
- **Density:** The layout is data-heavy. White space is utilized not for "breathability" but for "segmentation." Spacing follows a 4px base unit to allow for precise alignment of technical readouts.
- **Adaptation:** On mobile/tablet devices, the "pods" stack vertically, but the header—containing critical flight status—remains persistent. On desktop, the layout expands to fill the horizontal field of view, simulating a panoramic flight deck.

## Elevation & Depth

This design system avoids traditional shadows to prevent visual "mud." Depth is achieved through **Tonal Layers** and **Structural Outlines**:

- **Level 0 (Background):** Solid Charcoal (#121212).
- **Level 1 (Panels):** Defined by 1px Brushed Steel borders. No fill change; the border alone defines the containment.
- **Level 2 (Active/Modal):** Panels may have a very subtle inner glow or a secondary border in Safety Orange to indicate focus.
- **Glow Effects:** Critical alerts use a "Light-as-Depth" approach, where an orange glow effect creates the illusion of an illuminated physical bulb or LED behind the glass.

## Shapes

The shape language is **Sharp (0px)**. Aerospace engineering is about structural integrity and aerodynamics; in this UI, that translates to hard 90-degree angles and precise 45-degree chamfers on corners for specific "action" buttons.

There are no circles or soft curves in the structural elements. Circular elements are reserved exclusively for gauges and compasses (radial data) to ensure they are visually distinct from the navigational framework.

## Components

- **Buttons:** Rectangular with 0px radius. Default state is a 1px Brushed Steel border. Active/Hover state fills with Safety Orange and black text.
- **Telemetry Cards:** Deep Charcoal background with a 1px border. The top-left corner features a "Label-Caps" title. The center features a "Data-Display" value.
- **Checkboxes/Radios:** Square-only. When selected, they fill with a high-intensity orange glow.
- **Inputs:** Underlined with a 1px Brushed Steel stroke. Upon focus, the stroke turns Safety Orange and a subtle "scanning" animation (a thin vertical line moving left-to-right) may appear.
- **Status HUD:** A persistent top-bar displaying system health. Uses monospaced text and miniature sparklines for real-time engine/speed data.
- **Alerts:** Full-border Safety Orange boxes with blinking "Label-Caps" text for extreme conditions.