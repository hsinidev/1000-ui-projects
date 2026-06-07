---
name: CyberMetric Design System
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
  secondary: '#c6c6cb'
  on-secondary: '#2f3034'
  secondary-container: '#46464b'
  on-secondary-container: '#b5b4ba'
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
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: spaceGrotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-md:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0px
  data-mono:
    fontFamily: spaceGrotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-padding: 12px
---

## Brand & Style

This design system is engineered for the high-stakes environment of cybersecurity operations. The aesthetic, **Defensive-Tech**, prioritizes immediate scanability and cognitive clarity under pressure. It draws from **Minimalism** and **Brutalism**, utilizing a rigid structural grid and a "no-fluff" approach to interface elements. 

The atmosphere is one of a darkened command center: silent, authoritative, and precise. The UI remains invisible until a threat is detected, at which point the system transitions into a high-alert state using targeted visual "stressors." The user should feel in total control of a complex machine, with an emotional response rooted in vigilance and technical mastery.

## Colors

The palette is anchored by **Matte Black (#0D0D0D)** to minimize eye strain during long shifts and maximize contrast for critical data. **Laser Red (#FF0000)** is used with extreme discipline; it is reserved exclusively for high-severity alerts and destructive actions. 

**Neutral Grey (#8E8E93)** serves as the primary color for non-critical UI scaffolding, ensuring that the interface recedes into the background. A secondary "Matrix Green" (#00FF41) is utilized for "System Healthy" states to provide a clear binary opposite to the red alert signals. Surfaces are layered using subtle shifts in dark values rather than shadows, maintaining a flat, matte appearance.

## Typography

This design system employs a dual-font strategy to separate UI narrative from raw data. **Space Grotesk** is used for headlines, labels, and technical readouts; its geometric construction evokes a futuristic, scientific tone. **Inter** is used for all standard body text and interface controls to ensure maximum readability in dense documentation or log entries.

All data readouts (IP addresses, timestamps, hashes) should utilize the **data-mono** style to ensure character alignment and rapid pattern recognition. Text hierarchy is strictly enforced through scale and uppercase labeling for section headers.

## Layout & Spacing

The layout utilizes a **12-column fluid grid** designed for 24-inch and 32-inch monitor standards common in Security Operations Centers (SOC). To maximize data density, gutters are kept at a lean 16px. 

A 4px base unit drives the spacing rhythm. Components should be packed tightly to allow for the simultaneous viewing of multiple data streams (e.g., world map, live log feed, and incident queue). Use "Zone-based" layouts where critical telemetry is locked to the center, while navigation and secondary filters are docked to the periphery.

## Elevation & Depth

In keeping with the "Matte Black" aesthetic, traditional drop shadows are prohibited. Depth is communicated through **Tonal Layering** and **Low-Contrast Outlines**. 

- **Level 0 (Base):** Matte Black (#0D0D0D).
- **Level 1 (Cards/Widgets):** Surface #141414 with a 1px border of #2C2C2C.
- **Level 2 (Popovers/Tooltips):** Surface #1C1C1C with a 1px border of #8E8E93.

**Glow Effects:** Critical status indicators and trend lines may use a "bloom" effect (a 4px to 12px blur of the stroke color) to simulate a physical LED or phosphor display. This is used strictly for emphasis, not for layering.

## Shapes

The shape language is strictly **Sharp (0px)**. All containers, buttons, and input fields must have 90-degree corners. This reinforces the technical, aggressive, and "unfiltered" nature of the data. 

The only exceptions are status pips or map markers which may be circular to distinguish them from structural UI elements. Lines and borders should be 1px wide to maintain a "blueprint" or "schematic" feel.

## Components

**Buttons:**
Primary buttons are solid Neutral Grey (#8E8E93) with Black text. Critical action buttons are Laser Red (#FF0000) with a subtle outer glow when hovered. Use ghost buttons (border only) for secondary actions to reduce visual noise.

**Data Grids:**
The core of the system. Grids must support ultra-high density. Zebra-striping is replaced by 1px horizontal dividers. Columns should be sortable with monospaced data values.

**Status Chips:**
Small rectangular badges. When a status is "Critical," the chip should have a Laser Red background and a pulse animation to draw immediate attention.

**Input Fields:**
Underlined or fully boxed with a 1px border. The focus state should change the border color to Neutral Grey or Laser Red depending on the context of the form.

**Sparklines:**
Simplified, monochromatic trend lines embedded in widgets. Use the "bloom" glow effect for the line itself to make it appear as if it is an oscilloscope trace.

**Navigation:**
A vertical sidebar with collapsed icons. Icons should be thin-stroke (1px) to match the technical aesthetic.