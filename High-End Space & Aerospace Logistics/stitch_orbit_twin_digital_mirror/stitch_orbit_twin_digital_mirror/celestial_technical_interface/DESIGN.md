---
name: Celestial-Technical Interface
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#333b3b'
  surface-container-lowest: '#081010'
  surface-container-low: '#151d1e'
  surface-container: '#192122'
  surface-container-high: '#232b2c'
  surface-container-highest: '#2e3637'
  on-surface: '#dce4e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dce4e4'
  inverse-on-surface: '#2a3232'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#fff7e9'
  on-tertiary: '#3b2f00'
  tertiary-container: '#ffd93d'
  on-tertiary-container: '#725e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffe173'
  tertiary-fixed-dim: '#e8c426'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#0d1515'
  on-background: '#dce4e4'
  surface-variant: '#2e3637'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
  margin: 32px
---

## Brand & Style
This design system is engineered for high-stakes LEO satellite fleet management, where precision is paramount and data density is a requirement, not a choice. The aesthetic is rooted in a **Technical-Glassmorphic** style, blending the stark, authoritative clarity of a command center with the fluid, ethereal depth of orbital space.

The brand personality is **unflinching, precise, and futuristic**. It evokes the feeling of a sophisticated instrument panel rather than a standard SaaS application. Users should feel like they are operating at the edge of the atmosphere, supported by a system that prioritizes situational awareness and rapid data synthesis. Visual cues are drawn from head-up displays (HUDs) and telemetry consoles, utilizing thin lines, luminous accents, and layered transparency to create a sense of three-dimensional depth within a professional, dark-mode environment.

## Colors
The palette is hyper-focused to minimize cognitive load while maximizing the visibility of critical telemetry data.

- **Deep Space Black (#0B0E14):** The foundational void. It provides the infinite canvas required for high-contrast data visualization.
- **Neon Cyan (#00F3FF):** The primary signal. Used exclusively for interactive elements, active satellite trajectories, and critical status updates. It should be treated as a light source.
- **Silver (#C0C0C0):** The structural backbone. Used for borders, inactive iconography, and secondary metadata to provide a metallic, industrial feel.
- **Semantic Accents:** While Cyan is the hero, use desaturated reds for orbital decay/warnings and amber for signal interference, always maintaining the thin-stroke aesthetic.

## Typography
The typographic strategy balances human-readable sans-serifs for interface navigation with technical monospaced fonts for telemetry.

- **Inter** is utilized for primary UI labels and headers, ensuring high legibility even when rendered behind glassmorphic blurs.
- **JetBrains Mono** is the workhorse for all technical data, coordinates, timestamps, and orbital parameters. It reinforces the "command center" feel and ensures that columns of changing numbers remain stable and easy to scan.
- **Hierarchy:** Use all-caps labels for metadata headers to evoke an architectural or engineering blueprint aesthetic.

## Layout & Spacing
The design system employs a **Modular Technical Grid**. This is a 12-column fixed-grid system designed for high-resolution desktop monitors (1920px+), typical of operations centers.

A subtle background grid overlay, set at 32px increments with #C0C0C0 at 5% opacity, should be visible at all times to provide a sense of mathematical alignment. Components should snap to this grid. 

- **Density:** High density is preferred. Information should be grouped into logical "Modules" (cards) with 16px gutters.
- **Margins:** Generous 32px outer margins ensure the UI feels like a floating HUD within the monitor's frame.
- **Mobile:** On smaller viewports, the grid collapses to a single column, but technical data (monospaced) should scale down in size rather than wrapping, to maintain tabular integrity.

## Elevation & Depth
Depth is not communicated through shadows, but through **translucency and luminosity**.

1.  **The Void (Level 0):** The solid #0B0E14 background.
2.  **The Grid (Level 1):** The subtle silver grid overlay.
3.  **Surfaces (Level 2):** Glassmorphic panels using a 12px to 20px background blur and a 1px Silver (#C0C0C0) border at 20% opacity. 
4.  **Active Elements (Level 3):** Elements with a "Neon Glow." Use a 0 0 10px Cyan drop shadow (outer glow) to indicate selected satellites or active alerts.

This "stacking" creates a high-tech layering effect where data feels like it is projected onto glass panes between the operator and the vacuum of space.

## Shapes
This design system utilizes **Sharp** geometry. 0px border radii are used for almost all containers and buttons to maintain an aggressive, industrial, and military-grade precision. 

The only exception is for circular status indicators (pills) used to represent satellite health or orbital icons. All structural components—cards, inputs, and button frames—must remain strictly rectangular to reinforce the feeling of a rigid, technical instrument.

## Components

- **Buttons:** Primary buttons are Neon Cyan with black text. Secondary buttons are transparent with a 1px Silver border and Silver text. On hover, buttons should emit a subtle Cyan outer glow.
- **Glass Cards:** The primary container. These use `backdrop-filter: blur(12px)` and a thin `1px` border of Silver at low opacity. They should have no background color other than the subtle tint of the glass variable.
- **Data Readouts:** Large numerical displays (e.g., Altitude, Velocity) must use JetBrains Mono. Use small all-caps labels above the data for context.
- **Inputs:** Text fields are simple underlines in Silver. When focused, the underline transitions to Cyan with a small glowing "caret" at the end of the line.
- **Telemetry Charts:** Use thin line weights (1px). Grid lines within charts should match the background grid aesthetic. No fills under line charts; use only strokes to maintain transparency.
- **Status Indicators:** Use a "Pulse" animation for critical alerts. A Cyan dot that expands and fades out conveys "Active Signal" or "Contact Established."