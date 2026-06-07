---
name: LunarBase Monitoring
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e4e2e4'
  on-surface-variant: '#e7bdb7'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#ad8883'
  outline-variant: '#5d3f3b'
  surface-tint: '#ffb4aa'
  primary: '#ffb4aa'
  on-primary: '#690003'
  primary-container: '#ff5545'
  on-primary-container: '#5c0002'
  inverse-primary: '#c0000a'
  secondary: '#c6c6cb'
  on-secondary: '#2f3034'
  secondary-container: '#46464b'
  on-secondary-container: '#b5b4ba'
  tertiary: '#c8c6c8'
  on-tertiary: '#303032'
  tertiary-container: '#919092'
  on-tertiary-container: '#29292b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#930005'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e4e2e4'
  tertiary-fixed-dim: '#c8c6c8'
  on-tertiary-fixed: '#1b1b1d'
  on-tertiary-fixed-variant: '#474649'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353437'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  data-readout:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for mission-critical reliability and technical precision. It prioritizes the cognitive load of astronauts operating in high-stress, low-light extraterrestrial environments. The brand personality is sterile, authoritative, and unapologetically functional. It eschews decorative flourishes in favor of raw utility and data density.

Drawing from **Minimalism** and **Brutalism**, the visual language utilizes a rigid structural grid and high-contrast signaling. The emotional response is one of absolute stability and clarity—there is no ambiguity in the interface. Every pixel serves a purpose in the monitoring of life-support systems and habitat integrity.

## Colors

The palette is optimized for dark-room environments to preserve the user's night vision and minimize screen glare. 

- **Lunar Grey Palette:** The foundation of the UI. Deep charcoals (#0A0A0A to #1C1C1E) form the background layers, while mid-tones provide structural definition.
- **Signal Red:** Reserved exclusively for critical alerts, hardware failures, and high-priority warnings. It is never used for decorative purposes.
- **White & High-Contrast Data:** Pure white (#FFFFFF) or high-density grey (#E5E5E7) is used for telemetry and readouts to ensure legibility against the dark void of the background.
- **Status Amber (Supporting):** Used sparingly for "Caution" or "Impending Maintenance" states.

## Typography

Typography in this design system is treated as a specialized instrument. 

**Space Grotesk** is used for all technical readouts, headlines, and status labels. Its geometric nature provides a "tech-heavy" aesthetic while maintaining excellent legibility at various scales. Tabular figures must be enabled to ensure that numerical data in monitoring lists remains aligned during real-time updates.

**Inter** is utilized for long-form instructional text or system logs, providing a neutral, highly readable sans-serif counterpoint to the more aggressive display font. All labels should lean toward uppercase for a formalized, military-spec appearance.

## Layout & Spacing

This design system employs a **Fixed Grid** model to ensure that critical monitoring panels remain in predictable locations. A 12-column grid is used for desktop-class habitat monitors, while a 4-column grid is used for handheld or forearm-mounted displays.

Spacing follows a strict 4px base unit. Density is high; information is packed tightly to allow for a comprehensive "at-a-glance" overview of the habitat. Elements are separated by 1px borders rather than wide margins to maximize the use of screen real estate.

## Elevation & Depth

Elevation is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than shadows. In a zero-glare environment, shadows are visually noisy and physically inconsistent.

1.  **Level 0 (Base):** Deepest charcoal (#0A0A0A), used for the viewport background.
2.  **Level 1 (Panels):** Mid-charcoal (#1C1C1E), used for primary data containers.
3.  **Level 2 (Active Elements):** Lighter grey (#2C2C2E), used for active input fields or hovered states.

Separation is achieved through 1px solid borders in a slightly lighter grey (#3A3A3C). For critical alerts, the elevation is "broken" by a solid Signal Red stroke that draws immediate optical attention.

## Shapes

The shape language is strictly **Sharp (0px)**. All containers, buttons, and input fields utilize hard 90-degree angles. This reinforces the sterile, industrial aesthetic of habitat hardware and suggests a modular, interconnected system. Circular elements are reserved exclusively for radial gauges or specific hardware-mapped icons (e.g., airlock controls).

## Components

- **Buttons:** Rectangular with 1px borders. Primary actions use solid white backgrounds with black text for maximum contrast. Danger actions use Signal Red.
- **Status Indicators:** Small square pips. A "Pulse" animation is used only for "Critical" states to provide a temporal cue for the eye.
- **Telemetry Cards:** Bordered containers with a "label-caps" header. Data points within cards should be aligned to a sub-grid for vertical scanning.
- **Inputs:** Simple boxed fields with no background fill. Focus is indicated by a weight increase in the border from 1px to 2px.
- **Progress Bars:** Segmented blocks rather than smooth gradients. This provides a clearer sense of discrete measurement units (e.g., O2 levels).
- **Gauges:** Minimalist radial or linear scales with needle indicators. Digital readouts must always accompany visual gauges.