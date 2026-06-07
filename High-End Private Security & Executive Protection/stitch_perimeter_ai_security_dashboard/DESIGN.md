---
name: Perimeter-AI
colors:
  surface: '#121416'
  surface-dim: '#121416'
  surface-bright: '#37393c'
  surface-container-lowest: '#0c0e11'
  surface-container-low: '#1a1c1e'
  surface-container: '#1e2022'
  surface-container-high: '#282a2c'
  surface-container-highest: '#333537'
  on-surface: '#e2e2e5'
  on-surface-variant: '#c6c6cb'
  inverse-surface: '#e2e2e5'
  inverse-on-surface: '#2f3033'
  outline: '#8f9095'
  outline-variant: '#45474b'
  surface-tint: '#c3c6cf'
  primary: '#c3c6cf'
  on-primary: '#2d3137'
  primary-container: '#0a0e14'
  on-primary-container: '#787b83'
  inverse-primary: '#5b5e66'
  secondary: '#ffb59a'
  on-secondary: '#5a1b00'
  secondary-container: '#ff5e07'
  on-secondary-container: '#531900'
  tertiary: '#c4c6cf'
  on-tertiary: '#2d3037'
  tertiary-container: '#0b0e14'
  on-tertiary-container: '#787b83'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2eb'
  primary-fixed-dim: '#c3c6cf'
  on-primary-fixed: '#181c22'
  on-primary-fixed-variant: '#43474e'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#802a00'
  tertiary-fixed: '#e0e2eb'
  tertiary-fixed-dim: '#c4c6cf'
  on-tertiary-fixed: '#191c22'
  on-tertiary-fixed-variant: '#44474e'
  background: '#121416'
  on-background: '#e2e2e5'
  surface-variant: '#333537'
typography:
  display:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style

The design system is engineered to project absolute authority, technical precision, and unwavering vigilance. It is tailored for high-stakes environments where clarity and rapid response are paramount. The aesthetic draws heavily from Heads-Up Displays (HUDs) and tactical interfaces, prioritizing functional density over decorative white space.

The style is **Technical-Brutalist**, characterized by sharp edges, rigid structural grids, and a high-contrast utilitarian feel. It aims to evoke a sense of "Mission Control"—sophisticated yet purely functional. Every element exists to provide situational awareness, utilizing visual cues that mimic high-end hardware interfaces to foster trust in the system's defensive capabilities.

## Colors

This design system utilizes a "Deep-Night" palette optimized for 24/7 monitoring and low-light environments. 

- **Midnight Blue (#0A0E14):** The foundational void. Used for the primary background to minimize eye strain and maximize the pop of data overlays.
- **Safety Orange (#FF5C00):** The primary kinetic color. Reserved strictly for active detection, critical alerts, and primary calls to action. It must be used sparingly to maintain its psychological urgency.
- **Graphite (#2C2F36):** The structural anchor. Used for secondary surfaces, component borders, and dividing lines to create mechanical separation without breaking the dark aesthetic.
- **Accents:** Active states leverage subtle orange glows (`rgba(255, 92, 0, 0.3)`) to simulate illuminated hardware buttons.

## Typography

Typography in this design system is split between two functional roles: **Communication** and **Telemetry**.

**Geist** is the primary typeface for all UI controls, navigation, and messaging. Its geometric clarity ensures legibility at a glance, maintaining a clean, modern technical feel.

**JetBrains Mono** is utilized for all "Telemetry Data"—coordinates, timestamps, sensor readings, and system logs. The monospaced nature allows for character alignment in scanning lists and emphasizes the "technical readout" aesthetic. Headers should prioritize high-contrast weights, while labels should frequently utilize uppercase styling to mimic military and security documentation protocols.

## Layout & Spacing

This design system employs a **Fixed-Modular Grid** system. Layouts should feel constructed rather than flowing. 

- **The Grid:** A strict 12-column system with 16px gutters.
- **Rhythm:** All spacing must be multiples of 4px. Use tight internal padding (8px, 12px) for components to reinforce the high-density HUD feel.
- **Containment:** Use "Paneling" to group related data. Panels should be separated by 1px Graphite borders. 
- **Information Density:** Prioritize "At-a-Glance" visibility. Video feeds should occupy primary real estate, with telemetry data docked in sidebar "blades" or bottom "trays."

## Elevation & Depth

Elevation is conveyed through **Tonal Layering** and **Luminescence** rather than shadows. 

1. **Base Level:** Midnight Blue background (Deepest).
2. **Surface Level:** Graphite containers with 1px solid borders (#3F434C) to define edges.
3. **Active Level:** Elements in an active or hovered state gain a subtle interior glow or a 1px Safety Orange border.
4. **Overlays:** Modals or urgent alerts use a backdrop blur (12px) with a semi-transparent Graphite fill to maintain context of the surveillance feed behind them. 

Avoid ambient shadows entirely; use crisp, high-contrast borders to indicate the stacking order of panels.

## Shapes

The design system strictly adheres to **Sharp (0px)** roundedness. Every corner must be a perfect 90-degree angle to reinforce the mechanical, high-security nature of the brand. 

In rare instances where a visual "cut-off" is needed for buttons or status tags, use a 45-degree chamfered corner (dog-ear) to mimic military hardware design, but avoid standard border-radius settings entirely. This ensures the interface feels like it was precision-milled rather than rendered.

## Components

- **Buttons:** Rectangular with 1px borders. Primary buttons use Safety Orange backgrounds with black text. Secondary buttons use Graphite backgrounds with Orange borders.
- **Inputs:** Solid Midnight Blue fills with 1px Graphite borders. On focus, the border shifts to Orange with a faint outer glow. Use JetBrains Mono for input text.
- **Status Indicators:** Small square pips. Constant "Pulse" animations are used for active recording or live sensor states.
- **Cards/Panels:** Header areas of panels should have a distinct Graphite background tint and include a "Corner Accent"—a small L-shaped bracket in the top-left to frame the content.
- **Data Tables:** High-density, no vertical lines, only horizontal Graphite separators. Row hovers should trigger a dim Orange highlight.
- **Crosshairs/Reticles:** Use thin 1px lines for camera viewfinders and target tracking, rendered in Safety Orange for detected threats and White for neutral tracking.
- **Telemetry Chips:** Small, monospaced labels used to tag objects in a video feed (e.g., "ID: VEHICLE_084").