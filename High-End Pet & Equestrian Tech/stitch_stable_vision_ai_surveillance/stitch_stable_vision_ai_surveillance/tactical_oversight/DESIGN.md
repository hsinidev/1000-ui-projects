---
name: Tactical Oversight
colors:
  surface: '#0d1320'
  surface-dim: '#0d1320'
  surface-bright: '#333947'
  surface-container-lowest: '#080e1b'
  surface-container-low: '#151c29'
  surface-container: '#19202d'
  surface-container-high: '#242a38'
  surface-container-highest: '#2f3543'
  on-surface: '#dce2f5'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#dce2f5'
  inverse-on-surface: '#2a303e'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c2c6db'
  on-secondary: '#2b3040'
  secondary-container: '#414658'
  on-secondary-container: '#b0b4c9'
  tertiary: '#c3c6d6'
  on-tertiary: '#2c303d'
  tertiary-container: '#9598a7'
  on-tertiary-container: '#2d313d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#dee1f7'
  secondary-fixed-dim: '#c2c6db'
  on-secondary-fixed: '#161b2b'
  on-secondary-fixed-variant: '#414658'
  tertiary-fixed: '#dfe2f2'
  tertiary-fixed-dim: '#c3c6d6'
  on-tertiary-fixed: '#171b27'
  on-tertiary-fixed-variant: '#434654'
  background: '#0d1320'
  on-background: '#dce2f5'
  surface-variant: '#2f3543'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1-technical:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-standard:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  timestamp-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.2'
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style
This design system is engineered for mission-critical reliability and high-stakes surveillance. It adopts an **Industrial Mission-Control** aesthetic, emphasizing precision, technical authority, and zero-latency response. The brand personality is vigilant and uncompromising, designed for users who require absolute clarity during 24/7 monitoring cycles.

The visual language draws from aeronautic and security interfaces: high-contrast elements, rigid structural grids, and a focus on "status-at-a-glance" ergonomics. Every pixel serves a functional purpose, eliminating decorative bloat to ensure that critical foaling events or security breaches are identified instantly. The emotional response is one of controlled calm—providing the operator with the tools to manage life-critical data through a professional, high-security lens.

## Colors
The palette is optimized for low-light environments and long-duration monitoring to reduce ocular strain while highlighting critical data.

- **Midnight Blue (#0A0F1E):** The primary depth color, used for the base application canvas to provide a stable, recessed foundation.
- **Graphite (#1E222E):** The surface color for all interactive containers, tiles, and sidebars, creating a clear distinction between the background and active work areas.
- **Safety Orange (#FF6B00):** The high-visibility accent used exclusively for primary actions, critical alerts, and active monitoring states.
- **Status Colors:** Use "Matrix Green" (#00FF41) for healthy AI heartbeat signals and "Warning Gold" (#FFD600) for non-critical telemetry anomalies.

## Typography
The typographic strategy balances rapid readability with technical density. 

**Hanken Grotesk** is used for all primary UI labels and headings to provide a clean, modern, and highly legible sans-serif foundation. **JetBrains Mono** is reserved for all variable data, including timestamps, AI confidence scores, and sensor telemetry. This distinction allows the user’s eye to immediately separate "Interface Controls" from "Live Data." Headlines should utilize uppercase styling to reinforce the industrial, authoritative tone of the system.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model optimized for dashboard density. A 12-column grid structure is the standard for desktop monitoring views, allowing for modular "tiles" that can span 3, 4, or 6 columns.

The spacing rhythm is based on a strict 4px baseline. Compactness is prioritized over whitespace to ensure that video feeds and data charts remain the primary focus. Gutters are kept tight (16px) to maximize the "Command Center" feel, creating a sense of a highly integrated, singular tool rather than a collection of disparate parts.

## Elevation & Depth
In this system, depth is communicated through **Tonal Layering** and **High-Contrast Outlines** rather than traditional shadows. This ensures visibility is maintained on low-quality or high-brightness industrial monitors.

- **Level 0 (Base):** Deepest background (#05070A).
- **Level 1 (Canvas):** Midnight Blue (#0A0F1E).
- **Level 2 (Containers):** Graphite (#1E222E) with a 1px solid border (#32394D).
- **Active State:** Elements in an active or hovered state should feature a subtle inner glow in Safety Orange and an increased border contrast. 

Avoid drop shadows; use "Outer Glows" (bloom) only for critical alert indicators to simulate the appearance of a physical warning light on a console.

## Shapes
The shape language is strictly **Sharp (0px roundedness)**. This reinforces the technical, industrial nature of the system and ensures that layout containers fit together with surgical precision. 

The use of 90-degree angles across all buttons, input fields, and cards communicates a "no-nonsense" security posture. The only exception to this rule is the use of circular status pips to represent "Live" or "Online" connectivity states, providing a singular organic shape to draw the eye to active status indicators.

## Components
- **Alert Cards:** These must feature a thick (2px - 4px) left-hand border in Safety Orange. On critical triggers, the entire card background should pulse between Graphite and a dark variant of Safety Orange.
- **Monitoring Tiles:** Data-rich containers featuring a header bar with a Monospaced timestamp and a "Confidence Score" indicator. Tiles should be collapsible to allow for custom cockpit configurations.
- **Buttons:** Primary buttons are solid Safety Orange with black text. Secondary buttons are ghost-style with Graphite borders and Hanken Grotesk bold labels.
- **Input Fields:** Dark-filled Graphite fields with 1px borders. The focus state must use a "Safety Orange" glow effect on the border.
- **Status Chips:** Small, rectangular labels using Monospaced type. Use high-contrast background fills (e.g., Matrix Green background with Black text) for immediate state recognition.
- **Data Scrubber:** A custom timeline component for video playback using a monospaced ruler and a Safety Orange playhead for precise event locating.