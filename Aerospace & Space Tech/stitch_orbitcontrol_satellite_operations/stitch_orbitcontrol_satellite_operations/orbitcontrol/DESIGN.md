---
name: OrbitControl
colors:
  surface: '#0c160a'
  surface-dim: '#0c160a'
  surface-bright: '#313c2e'
  surface-container-lowest: '#071106'
  surface-container-low: '#141e12'
  surface-container: '#182216'
  surface-container-high: '#222d20'
  surface-container-highest: '#2d382a'
  on-surface: '#dae6d2'
  on-surface-variant: '#b9ccb2'
  inverse-surface: '#dae6d2'
  inverse-on-surface: '#283326'
  outline: '#84967e'
  outline-variant: '#3b4b37'
  surface-tint: '#00e639'
  primary: '#ebffe2'
  on-primary: '#003907'
  primary-container: '#00ff41'
  on-primary-container: '#007117'
  inverse-primary: '#006e16'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#f8f8ff'
  on-tertiary: '#2d3137'
  tertiary-container: '#d9dce5'
  on-tertiary-container: '#5d6168'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#72ff70'
  primary-fixed-dim: '#00e639'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#00530e'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#dfe2eb'
  tertiary-fixed-dim: '#c3c6cf'
  on-tertiary-fixed: '#181c22'
  on-tertiary-fixed-variant: '#43474e'
  background: '#0c160a'
  on-background: '#dae6d2'
  surface-variant: '#2d382a'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.05em
  data-mono:
    fontFamily: monospace
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  body-standard:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 100%
  density-high: 8px
  density-medium: 16px
---

## Brand & Style

This design system is engineered for high-stakes environments where split-second decision-making is paramount. It adopts a **Glass-Cockpit** aesthetic, blending the precision of aerospace instrumentation with the clarity of modern data architecture. The brand personality is clinical, authoritative, and vigilant.

The visual style leverages **High-Contrast Brutalism** mixed with **Glassmorphism**. It utilizes a strict grid-based layout to organize high-density information without visual clutter. Design elements are treated as tactical instruments—functional, high-fidelity, and stripped of unnecessary ornamentation. Vector-line graphics and subtle "active" glows communicate live data streams and system vitality, ensuring that users feel they are at the helm of a sophisticated mission control center.

## Colors

The palette is rooted in the "Deep Midnight" of outer space, providing a low-light environment that reduces eye strain during extended monitoring sessions. 

- **Laser Green (#00FF41):** Used exclusively for primary actions, active states, and successful data telemetry. It provides a sharp, phosphor-like glow against the dark background.
- **Silver (#C0C0C0):** The primary color for typography and secondary UI elements, offering high legibility without the harshness of pure white.
- **Deep Midnight (#0A0E14):** The foundation of the UI, creating depth and a "black-hole" effect for content containers.
- **Critical Alerts:** A searing red is reserved for life-critical failures, ensuring immediate visual dominance over the green-dominant interface.

## Typography

This design system employs a dual-typeface strategy to distinguish between UI navigation and technical telemetry.

- **UI Elements:** Use **Inter** for body text and descriptive content. Its neutral, systematic nature ensures clarity in high-density layouts.
- **Technical/Headlines:** Use **Space Grotesk** for headings and labels. Its geometric, futuristic skeleton reinforces the mission-control aesthetic.
- **Data Display:** All dynamic data values and coordinates must be rendered in a **Monospace** font (falling back to Space Grotesk if unavailable) to ensure character alignment in tables and live-updating counters. All labels should be uppercase to mimic military and aerospace nomenclature.

## Layout & Spacing

The layout is built on a **Fluid Grid** system that maximizes screen real estate. Given the mission-critical nature of the system, "whitespace" is treated as a luxury; information density is prioritized.

The system uses a strict **4px baseline grid**. Components are packed tightly, using 8px (density-high) gaps for related data points and 16px (gutter) for distinct module separation. A 12-column grid is standard for wide-screen monitoring stations, with data cards spanning 3, 4, or 6 columns. Content should be edge-to-edge with 24px outer margins to maintain a "command center" dashboard feel.

## Elevation & Depth

Depth is communicated through **Tonal Layers** and **Glassmorphism** rather than traditional shadows. This design system avoids soft ambient shadows, which can appear "muddy" on high-density dark screens.

1.  **Base Layer:** The Deep Midnight background (#0A0E14).
2.  **Instrument Layer:** Semi-transparent containers with a subtle 1px "Silver" border at 10-20% opacity. A "Backdrop Blur" (8px to 12px) is applied to these containers to create a frosted-glass effect over the background.
3.  **Active Layer:** Elements currently being interacted with receive a "Laser Green" outer glow (2px to 4px spread, 0.4 opacity) to simulate an illuminated hardware button.
4.  **Vector Overlay:** Grid lines and axis markers are rendered in 1px strokes with 10% opacity, providing a structural map for the UI.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. 

Rounded corners are avoided to maximize information density and maintain a rigid, technical appearance. This "sharp-edge" philosophy applies to buttons, cards, input fields, and data-viz bars. The only exception is for circular status indicators (LED style) or radar-graph elements. Containers should use 1px borders to define their boundaries, creating a "wireframe" feel that suggests the UI is rendered in real-time by a high-performance computer.

## Components

- **Buttons:** Rectangular with 1px borders. Primary buttons use a solid Laser Green background with black text. Secondary buttons are transparent with a Silver border and Silver text. On hover, buttons should emit a subtle green glow.
- **Data Cards:** High-contrast containers with a 1px Silver top-border. Headlines are always uppercase and positioned in the top-left, with a "System Status" indicator in the top-right.
- **Inputs:** Simple underline or full-box 1px border. The cursor and active text must be Laser Green to simulate a terminal prompt.
- **Chips/Status Badges:** Compact, rectangular blocks. Active states are solid Laser Green; warning states are Amber; critical states are Red.
- **Vector Graphics:** Use thin 1px lines for charts and graphs. Data points should be small squares or crosses (not circles) to maintain the technical, plotter-style aesthetic.
- **Critical Alerts:** Modal overlays that use a "Warning Stripe" pattern (diagonal Red/Black) on the top and bottom edges to command immediate attention.