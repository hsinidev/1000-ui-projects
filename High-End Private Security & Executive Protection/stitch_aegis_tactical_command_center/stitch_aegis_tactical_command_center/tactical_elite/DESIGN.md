---
name: Tactical-Elite
colors:
  surface: '#0d141b'
  surface-dim: '#0d141b'
  surface-bright: '#333a42'
  surface-container-lowest: '#080f16'
  surface-container-low: '#161c24'
  surface-container: '#1a2028'
  surface-container-high: '#242a33'
  surface-container-highest: '#2f353e'
  on-surface: '#dde3ee'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#dde3ee'
  inverse-on-surface: '#2b3139'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#c1c6d6'
  on-secondary: '#2b313c'
  secondary-container: '#434956'
  on-secondary-container: '#b3b8c7'
  tertiary: '#cac6c3'
  on-tertiary: '#32302f'
  tertiary-container: '#0b0a09'
  on-tertiary-container: '#7c7977'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#dde2f2'
  secondary-fixed-dim: '#c1c6d6'
  on-secondary-fixed: '#161c27'
  on-secondary-fixed-variant: '#414753'
  tertiary-fixed: '#e6e1df'
  tertiary-fixed-dim: '#cac6c3'
  on-tertiary-fixed: '#1d1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#0d141b'
  on-background: '#dde3ee'
  surface-variant: '#2f353e'
typography:
  headline-xl:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the high-stakes environment of global executive protection. The brand personality is uncompromising, clinical, and vigilant. It prioritizes rapid information ingestion and authoritative presence.

The visual style is a fusion of **High-Contrast Minimalism** and **Technical Brutalism**. By stripping away decorative elements and focusing on sharp geometric precision, the UI reflects the reliability of a high-end security detail. The emotional response is one of absolute security, situational awareness, and technical superiority. 

Key stylistic pillars:
- **Zero-Tolerance Geometry:** No rounded corners; every element is cut with 90-degree precision.
- **Vigilant Contrast:** Deep blacks paired with surgical reds to immediately signal hierarchy.
- **Technical Atmosphere:** Subtle glows and monospaced accents mimic heads-up displays (HUDs) used in elite tactical gear.

## Colors

The palette is restricted to a "Stealth-Ops" spectrum, ensuring that when color is used, it carries maximum weight.

- **Matte Black (#0A0A0A):** The foundation. Used for primary backgrounds to minimize eye strain in low-light tactical environments.
- **Slate Grey (#2E3440):** The surface layer. Used for cards, sidebars, and elevated containers to provide subtle separation without breaking the dark-mode immersion.
- **Signal Red (#CC0000):** The action layer. Reserved exclusively for critical alerts, emergency triggers, and active "threat" states.
- **Functional Neutrals:** A range of cool grays (from the Nord-inspired palette) used for secondary text and non-critical UI borders.

Active elements should utilize a subtle `0 0 8px #CC00004D` outer glow to indicate focus without softening the sharp edges of the design.

## Typography

Typography is treated as a data-delivery mechanism. The system utilizes a dual-font approach:

1. **JetBrains Mono:** Used for headlines, labels, and data readouts. Its fixed-width nature conveys mathematical precision and technical reliability. All labels must be uppercase to evoke a military-briefing aesthetic.
2. **Inter:** Used for body copy and long-form intelligence reports. It provides the necessary legibility to balance the starkness of the monospaced headlines.

Avoid italics. Use weight and tracking (letter-spacing) to create hierarchy.

## Layout & Spacing

This design system employs a **Fixed Grid** on a 4px baseline. All layouts should be built on a 12-column grid to maintain structural integrity.

- **Gutters:** Standardized at 16px to maintain a dense, high-information layout.
- **Margins:** 32px external margins provide a "safe zone" for the UI content.
- **Rhythm:** Vertical spacing must strictly follow multiples of 4px. Use larger gaps (48px+) only to separate primary mission modules.

Layouts should prioritize "Dashboard" views where all critical telemetry is visible within a single frame, minimizing the need for scrolling.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layering** and **Line Work**, rather than shadows. 

- **Level 0 (Base):** #0A0A0A. Background.
- **Level 1 (Surfaces):** #2E3440. Cards, navigation bars, and modals.
- **Borders:** All surfaces must have a 1px solid border (#4C566A).
- **Active State:** Elements in focus or active states gain a 1px Signal Red (#CC0000) border and a faint, sharp outer glow.

Shadows are strictly prohibited. Depth is perceived through the contrast between the matte black background and the grey surfaces.

## Shapes

The shape language is strictly **Sharp**. 

- **Radius:** 0px for all buttons, inputs, cards, and modals.
- **Iconography:** Use 2px stroke-weight icons with sharp corners. Avoid any rounded terminators or circular enclosures.
- **Dividers:** Use thin 1px lines. For "Alert" states, dividers may increase to 4px in thickness to create a physical sense of a barrier or warning.

## Components

### Buttons
- **Primary:** Background #CC0000, Text #FFFFFF, sharp corners, uppercase JetBrains Mono.
- **Secondary:** Transparent background, 1px #4C566A border, white text.
- **Ghost:** No background or border, Signal Red text, used for low-priority actions.

### Alert Cards
- **Emergency State:** Cards must feature a 4px solid #CC0000 border on all sides. 
- **Header:** Accompanied by a flashing "STATUS: CRITICAL" label in the top right.

### Input Fields
- **Default:** Slate Grey (#2E3440) background, 1px border. 
- **Focus:** 1px Signal Red border with 0 0 4px #CC0000 glow. Text enters as mono-data font.

### Progress Bars
- Flat, rectangular bars. "Active" progress should be Signal Red. "Background" track should be #0A0A0A with a 1px border.

### Status Indicators
- Small square pips (not circles) used to indicate "Online," "Scanning," or "Threat Detected."