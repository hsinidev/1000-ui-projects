---
name: Stable-Vision
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#363a3d'
  surface-container-lowest: '#0b0f12'
  surface-container-low: '#181c1f'
  surface-container: '#1c2023'
  surface-container-high: '#262a2e'
  surface-container-highest: '#313538'
  on-surface: '#e0e3e7'
  on-surface-variant: '#c6c6cc'
  inverse-surface: '#e0e3e7'
  inverse-on-surface: '#2d3134'
  outline: '#909096'
  outline-variant: '#45474c'
  surface-tint: '#c1c6d7'
  primary: '#c1c6d7'
  on-primary: '#2a303e'
  primary-container: '#080e1a'
  on-primary-container: '#757b8b'
  inverse-primary: '#585e6d'
  secondary: '#ffb59a'
  on-secondary: '#5a1b00'
  secondary-container: '#ff5e07'
  on-secondary-container: '#531900'
  tertiary: '#c1c8ca'
  on-tertiary: '#2b3234'
  tertiary-container: '#080f11'
  on-tertiary-container: '#757c7f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde2f4'
  primary-fixed-dim: '#c1c6d7'
  on-primary-fixed: '#161c28'
  on-primary-fixed-variant: '#414755'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#802a00'
  tertiary-fixed: '#dde4e6'
  tertiary-fixed-dim: '#c1c8ca'
  on-tertiary-fixed: '#161d1f'
  on-tertiary-fixed-variant: '#41484a'
  background: '#101417'
  on-background: '#e0e3e7'
  surface-variant: '#313538'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-padding: 1.5rem
---

## Brand & Style

This design system is engineered for high-stakes environmental monitoring where precision and split-second reaction times are paramount. The brand personality is authoritative, vigilant, and uncompromisingly professional. It draws from **Tactical Minimalism**, utilizing a "dark-mode-first" philosophy to reduce eye strain during 24/7 surveillance and ensure that critical alerts pierce through the visual field with maximum impact.

The aesthetic avoids decorative elements in favor of functional density. Every border, margin, and color shift serves a specific informational purpose. The goal is to evoke a sense of military-grade reliability and industrial durability, positioning the interface as a mission-critical tool rather than a standard consumer application.

## Colors

The palette of this design system is optimized for low-light environments and emergency visibility. 

- **Midnight Blue (Background/Depth):** Used as the foundational canvas to maintain high contrast with text while minimizing blue-light fatigue for users monitoring foaling stalls overnight.
- **Safety Orange (Critical/Action):** Reserved exclusively for active alerts, hazardous status changes, and primary calls to action. It is the "breaking" color that disrupts the deep background.
- **Graphite (Structure):** Used for component surfaces, panel dividers, and secondary navigation elements to provide architectural structure without competing with data.
- **Signal Greens/Reds:** Standardized status indicators for "System OK" and "Active Recording," used sparingly to maintain the hierarchy of the Safety Orange alerts.

## Typography

Typography in this design system prioritizes rapid data scanning. **Space Grotesk** is used for headlines and technical data labels; its geometric construction gives the UI a "technical readout" feel and ensures that numbers and characters remain distinct even at a distance. 

**Inter** is utilized for body text and descriptive logs, providing a neutral, highly legible counterpoint to the technical styling of the headings. All labels for sensor data (temperature, motion frequency, heart rate) must use the `label-caps` or `data-mono` styles to ensure they are perceived as telemetry rather than standard prose.

## Layout & Spacing

This design system employs a **strict 12-column fluid grid** designed for multi-monitor setups and ruggedized tablets. The layout philosophy is "Information Density over White Space." 

A modular pane system allows for flexible dashboard configurations. Key telemetry is grouped into high-density widgets with consistent 16px gutters. Precision is maintained through a 4px baseline rhythm, ensuring that all structural elements align to a technical grid, reinforcing the authoritative and professional nature of the software. Margins are kept tight to maximize the real estate for live video feeds and real-time data visualization.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **High-Contrast Outlines** rather than traditional shadows. Shadows are avoided to prevent the UI from feeling "soft" or "consumer-grade."

- **Base Layer:** Midnight Blue (Darkest).
- **Surface Layer:** Graphite panels with a subtle 1px inner stroke to define boundaries.
- **Active Layer:** Elements currently being interacted with or highlighting a specific stall are given a subtle outer glow in Safety Orange or a higher-luminosity Graphite.
- **Alert Layer:** Overlays use full-opacity backgrounds and sharp, high-contrast borders to sit "on top" of the telemetry data, physically separating emergency information from routine monitoring.

## Shapes

The shape language of this design system is **Industrial and Rugged**. A "Soft" roundedness (4px radius) is applied to most UI components to suggest precision engineering, similar to the chamfered edges of high-end hardware. 

Buttons, input fields, and panel corners follow this consistent radius. Alerts and critical notifications may occasionally utilize sharp (0px) corners to create a jarring visual distinction from the rest of the interface, signaling that the current state is an exception to the normal operational flow.

## Components

### Alert Cards
High-contrast cards featuring a 4px solid Safety Orange left border. Critical alerts utilize a solid Safety Orange header with black text to ensure maximum legibility during emergency foaling events.

### Data Monitoring Widgets
Compact, data-heavy containers. They feature a Graphite background, `label-caps` headers, and large-format `data-mono` telemetry values. Sparklines within these widgets should be thin (1.5px) and use high-contrast colors against the Midnight Blue background.

### Precision Controls
Buttons and toggles are large enough for gloved interaction or rapid touch input. Primary buttons are solid Safety Orange. Secondary controls are outlined in Graphite.

### System Status Chips
Small, utilitarian indicators. Use "Status: Active" or "Mode: Vigilance" with a small circular icon. These are monochromatic unless a status change occurs, at which point the chip adopts the color of the new state (e.g., Orange for "Alert").

### Input Fields
Dark-themed inputs with Graphite borders. The "Focus" state is indicated by a 2px Safety Orange border, never a glow, to maintain the clean, technical aesthetic of this design system.