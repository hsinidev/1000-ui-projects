---
name: Crisis-Connect
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#363a3d'
  surface-container-lowest: '#0b0f12'
  surface-container-low: '#181c1f'
  surface-container: '#1c2023'
  surface-container-high: '#272a2e'
  surface-container-highest: '#323539'
  on-surface: '#e0e2e7'
  on-surface-variant: '#e7bcba'
  inverse-surface: '#e0e2e7'
  inverse-on-surface: '#2d3134'
  outline: '#ae8885'
  outline-variant: '#5d3f3d'
  surface-tint: '#ffb3af'
  primary: '#ffb3af'
  on-primary: '#68000e'
  primary-container: '#d90429'
  on-primary-container: '#ffeae8'
  inverse-primary: '#bf0022'
  secondary: '#b5cad3'
  on-secondary: '#20333b'
  secondary-container: '#364a52'
  on-secondary-container: '#a4b8c2'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#6b6c6c'
  on-tertiary-container: '#eeeeee'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410005'
  on-primary-fixed-variant: '#930018'
  secondary-fixed: '#d1e6f0'
  secondary-fixed-dim: '#b5cad3'
  on-secondary-fixed: '#0a1e25'
  on-secondary-fixed-variant: '#364a52'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#101417'
  on-background: '#e0e2e7'
  surface-variant: '#323539'
typography:
  display-xl:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '800'
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
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 16px
  margin: 24px
---

## Brand & Style
This design system is engineered for high-stakes environments where every millisecond counts. The brand personality is authoritative, vigilant, and unshakeable. It targets emergency responders, dispatchers, and crisis managers who require a UI that eliminates cognitive load during high-stress scenarios.

The visual style is a fusion of **Modern Brutalism** and **Tactical Command-Center** aesthetics. It prioritizes raw functionality and data density over decorative flourishes. The interface relies on heavy borders, high-contrast states, and a rigid structural hierarchy to convey ultra-reliability. The emotional response is one of absolute clarity and immediate situational awareness.

## Colors
The palette is optimized for low-light command centers to reduce eye strain while maximizing the "pop" of critical alerts. 

- **Deep Navy (#001219):** Used as the primary canvas. It provides deep professional depth and ensures that luminous text remains legible.
- **Signal Red (#D90429):** Reserved exclusively for high-priority alerts, primary destructive actions, and active crisis indicators.
- **Pure White (#FFFFFF):** Used for primary data points and high-readability body text.
- **Neutral Accents:** Mid-tone greys are used for structural borders and inactive states to keep the focus on active data.

## Typography
This design system utilizes a dual-font strategy to balance rapid readability with technical precision. 

**JetBrains Mono** is the industrial engine, used for all headlines, tactical labels, and dynamic data strings. Its monospaced nature ensures that fluctuating numbers (like coordinates or timers) do not cause layout shifts.

**Inter** handles complex instructional text and long-form reports. It provides a clean, humanist counterpoint to the rigid mono font, ensuring that descriptive content remains legible under duress. All labels should use uppercase styling to evoke a sense of military-grade urgency.

## Layout & Spacing
The design system employs a **12-column fixed grid** with a strict 4px baseline rhythm. Layouts should feel "locked-in" and architectural.

- **Data Density:** Use tight spacing (sm/md) for data tables and status monitors to maximize information per screen.
- **Action Zones:** Use generous spacing (lg/xl) around primary touch targets to prevent accidental triggers in high-stress physical environments.
- **Sectioning:** Use 2px solid borders instead of whitespace to define clear boundaries between functional modules.

## Elevation & Depth
Depth is signaled through **Tonal Layering** and **Bold Outlines** rather than soft shadows. In a command-center environment, shadows can muddy the interface; therefore, this system uses a "flat-stack" approach.

- **Level 0 (Base):** Deep Navy (#001219).
- **Level 1 (Modules):** A slightly lighter navy hex to define container backgrounds.
- **Level 2 (Active Elements):** High-contrast borders (1px or 2px) in Signal Red or Pure White.
- **Interaction:** When an element is focused or active, it should utilize an inner glow or a solid 3px border to simulate a "lit" hardware button.

## Shapes
This design system uses a **Sharp (0px)** radius for all primary structural elements. Rectangular geometry reinforces the industrial, "no-nonsense" reliability of the system. 

The only exception to the 0px rule is for specific status icons (circular "online" pips) to differentiate them from interactive buttons. All containers, input fields, and action triggers must maintain hard 90-degree corners.

## Components
- **High-Visibility Headers:** Every module must have a header bar with a background of Neutral-800 and white mono-type labels. Headers should include a "Tactical Status Indicator" (e.g., a pulsing red dot for live feeds).
- **Tactical Buttons:** Large, blocky triggers. Primary actions use Signal Red backgrounds with White bold text. Secondary actions use transparent backgrounds with 2px White borders.
- **Input Fields:** Heavy 2px borders. On focus, the border turns Signal Red. Labels are always persistent (never hidden as placeholders) and positioned above the field in uppercase mono.
- **Status Indicators:** Small rectangular "pills" with high-saturation fills (Success Green, Alert Red, Warning Yellow). These should never rely on color alone; include a short text code (e.g., "ACTV", "PEND", "CRIT").
- **Alert Banners:** Full-width strips that use Signal Red backgrounds. Text should blink or cycle intensity slightly if the urgency level is "Critical."
- **Data Cards:** Modules that contain telemetry or personnel info. They use a "Header-Body-Footer" structure with visible dividers between each segment.