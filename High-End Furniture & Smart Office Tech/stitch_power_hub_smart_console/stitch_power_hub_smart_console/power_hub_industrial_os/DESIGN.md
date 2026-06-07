---
name: Power-Hub Industrial OS
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#9a9999'
  on-tertiary-container: '#313131'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-metrics:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-technical:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-readout:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  card-padding: 20px
  stack-gap: 8px
  flow-line-thickness: 2px
---

## Brand & Style

This design system establishes a high-performance, industrial-technical aesthetic tailored for luxury hardware management. The visual language balances the raw utility of professional power equipment with the refined precision of modern GaN (Gallium Nitride) technology. The primary goal is to evoke a sense of absolute reliability, safety, and real-time responsiveness.

The style is a hybrid of **High-Contrast Minimalism** and **Technical Glassmorphism**. It utilizes a "utility-first" architecture where information density is prioritized without sacrificing legibility. Flow lines—thin, animated strokes—provide a kinetic representation of energy distribution, while subtle translucent layers suggest the advanced internal cooling and layered circuitry of the device. The emotional response is one of command and control: the user should feel like they are operating a sophisticated mission-control interface for their desktop ecosystem.

## Colors

The palette is strictly functional, utilizing extreme contrast to define hierarchy. 

*   **Charcoal (#1A1A1A):** The foundation. Used for deep backgrounds to minimize eye strain and allow hardware metrics to pop.
*   **Safety Orange (#FF6B00):** The primary kinetic color. Reserved for interactive triggers, active power states, and critical warnings. It signals high-energy zones.
*   **Clean White (#FFFFFF):** Used for primary data readouts and high-readability labels. It provides a surgical contrast against the dark base.
*   **Accent Neutrals:** Mid-tone charcoals are used for card borders and "Flow" path backgrounds to create a sense of mechanical depth.

## Typography

Typography in this design system is treated as a calibrated instrument. 

**JetBrains Mono** is the workhorse for all quantitative data, ensuring that numerical values (wattage, voltage, temperature) align perfectly in tabular layouts and real-time streams. 

**Space Grotesk** provides a technical yet geometric flair for headlines, reinforcing the cutting-edge hardware theme. 

**Inter** handles standard UI labels and descriptive text, offering high legibility and a neutral professional tone. All technical labels should utilize uppercase styling with increased letter-spacing to mimic industrial stencil markings.

## Layout & Spacing

The layout follows a **Modular Grid System** designed for "Utility-First" cards. This allows the interface to scale based on the number of connected peripherals or active power ports.

*   **Modular Cards:** Components are housed in fixed-aspect ratio containers that snap to a 12-column grid.
*   **Flow Lines:** Dynamic energy paths (2px thickness) connect "Source" modules to "Output" modules, visually representing real-time electricity distribution.
*   **Spacing Rhythm:** A 4px baseline grid ensures tight, mechanical alignment. Gutters are kept narrow (16px) to maintain a sense of high-density data visualization.

## Elevation & Depth

Elevation is achieved through material density rather than traditional soft shadows.

*   **Tonal Layering:** The primary background is the deepest Charcoal. Secondary containers use a slightly lighter grey (#222222) with a 1px solid border (#333333).
*   **Subtle Glassmorphism:** For premium GaN-tech cards, use a backdrop-blur (12px) with a 10% opacity white fill. This creates a "frosted tech" feel that suggests internal complexity.
*   **Inner Glow:** Critical active states (like an active AC port) utilize a subtle inner glow in Safety Orange to simulate the light bleed of a physical LED indicator.
*   **No Soft Shadows:** Avoid ambient shadows. Depth should feel physical and structured, like panels on a rack-mounted server.

## Shapes

The shape language is **Precision-Industrial**. Sharp corners are the default to maintain a serious, professional tool aesthetic.

*   **Sharp Edges:** Outer containers and large modular blocks use 0px radius (Sharp).
*   **Micro-Radii:** Smaller interactive elements like buttons and input fields use a 2px "Softened Sharp" radius to prevent the UI from feeling overly aggressive while maintaining the technical look.
*   **Diagonal Chamfers:** Optional 45-degree chamfered corners may be used on primary action buttons or high-level status badges to evoke aerospace or heavy-machinery design.

## Components

*   **Utility Cards:** These are the primary containers. They feature a top-aligned `label-technical` header, a 1px divider, and a central `display-metrics` area.
*   **Power-Toggle Buttons:** Large, high-contrast switches. In the 'OFF' state, they feature a Charcoal background with White text. In the 'ON' state, they flood with Safety Orange.
*   **Flow Indicators:** Animated SVG lines with a "dash-array" offset that speeds up or slows down based on the actual wattage being drawn through the hub.
*   **Real-Time Charts:** Sparklines using Safety Orange for current and a subtle Clean White for historical averages. No fill under the line; keep it wireframe.
*   **Safety Alerts:** High-visibility banners using Safety Orange backgrounds with black text for immediate attention. For critical failure, use #FF0000 with a pulsing animation.
*   **Port Chips:** Small modular badges identifying USB-C, USB-A, or AC ports, using `jetbrainsMono` for technical specifications (e.g., "PD 3.1 - 140W").