---
name: Aero-Pilot Design System
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c4c7c9'
  on-secondary: '#2d3133'
  secondary-container: '#464a4b'
  on-secondary-container: '#b6b9bb'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#171919'
  on-tertiary-container: '#808282'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e0e3e5'
  secondary-fixed-dim: '#c4c7c9'
  on-secondary-fixed: '#181c1e'
  on-secondary-fixed-variant: '#444749'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-hud:
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
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
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
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 4px
  unit-xs: 0.25rem
  unit-sm: 0.5rem
  unit-md: 1rem
  unit-lg: 1.5rem
  unit-xl: 2.5rem
  grid_columns: '12'
  mobile_margin: 1rem
  desktop_margin: 2rem
---

## Brand & Style

This design system is engineered for professionals who demand technical precision and split-second legibility. The brand personality is rooted in aviation heritage but executed through a contemporary digital lens. It evokes the feeling of a high-end flight deck—utilitarian, reliable, and sophisticated.

The aesthetic follows an **Instrumental-Modern** approach, blending the tactile feel of brushed metal with the digital clarity of a Heads-Up Display (HUD). We utilize **Glassmorphism** to create depth without losing the "cockpit" feel, overlaying transparent data layers onto structural steel backgrounds. Visual elements are prioritized by mission criticality, ensuring the user remains focused on essential flight and timekeeping data.

## Colors

The palette is strictly functional. The foundation is **Deep Navy Blue**, providing a high-contrast environment that minimizes eye fatigue during night operations. **Brushed Steel Silver** is used for structural framing and surface containers, lending a physical, machined quality to the UI.

**Stark White** is reserved for high-priority data and primary labels to ensure maximum legibility. **Aviation Orange** is our singular "Critical Alert" color, used sparingly for HUD warnings, active toggles, and time-sensitive notifications. An auxiliary **Lume Glow** (cyan-green) is introduced specifically for "Lume-Mode" states, mimicking the phosphorescent glow of high-end mechanical pilot watches.

## Typography

The typography strategy prioritizes rapid data ingestion. **Space Grotesk** is used for large displays and headlines, providing a technical yet modern geometric feel. **Inter** serves as the primary body face for its exceptional legibility on mobile screens and neutral profile.

For technical readouts, coordinates, and serial numbers, **JetBrains Mono** is utilized. Its fixed-width nature ensures that shifting data (like altimeters or timers) does not cause layout jitter. All labels should use uppercase with slight tracking to mimic industrial plate engraving.

## Layout & Spacing

This design system employs a **mobile-first fluid grid** based on a 4px baseline rhythm. On mobile devices, use a 4-column layout with 16px margins. On larger displays, expand to a 12-column system. 

Padding should be generous within interactive components to accommodate "gloves-on" touch precision, while data density remains high in informational readouts. Use horizontal "rules" (1px lines) to separate instrument clusters, maintaining a structured, panel-based layout similar to an aircraft's overhead console.

## Elevation & Depth

Depth is conveyed through **material hierarchy** rather than traditional drop shadows.
1.  **Base Layer:** Deep Navy Blue (#0A192F).
2.  **Structural Layer:** Brushed Steel Silver (#B0B3B5) with a subtle vertical grain texture.
3.  **Interactive Layer:** Glassmorphic panels with `backdrop-filter: blur(12px)` and a 1px Stark White border at 10% opacity.
4.  **HUD Overlay:** Floating elements that utilize a subtle outer glow (`box-shadow: 0 0 15px rgba(255,149,0,0.3)`) when in an active or critical state.

In "Lume-Mode," all primary white text and iconography switch to the Lume Glow color with a soft CSS glow filter to simulate phosphorescence.

## Shapes

To maintain a "Professional Tool" aesthetic, we utilize **Sharp (0px)** corners for all structural containers, frames, and buttons. This reinforces the machined, industrial nature of aviation instruments. 

Only specific circular gauges (altimeters, chronographs) and status indicators should deviate from the rectangular grid. Any "pill" or "rounded" elements are prohibited to avoid a "consumer-tech" or "soft" appearance.

## Components

### Buttons
Primary buttons use the Aviation Orange background with Black text for maximum visibility. Secondary buttons are "Ghost" style: 1px Silver borders with transparent backgrounds. All buttons use uppercase Mono type and have a "haptic" press state where the border color brightens.

### HUD Data Chips
Used for displaying live metrics (e.g., knots, altitude). These are glassmorphic rectangles with a 1px left-side accent bar in Orange or Silver depending on status.

### Lists & Tables
Data-heavy lists should use alternating row opacities (zebras) using the Deep Navy and a slightly lighter Navy shade. High-contrast white text for data, Silver for labels.

### Input Fields
Inputs are bottom-border only, mimicking technical fill-in-the-blank logs. Active states are highlighted with an Aviation Orange underline and a very subtle inner glow.

### Lume-Mode Toggle
A specialized switch that, when active, applies a global `drop-shadow` to all typography and iconography, simulating the light bleed of a watch dial in total darkness.

### Gauges & Chronos
Custom SVG components that use thin 1px strokes to represent analog needles over digital data, bridging the gap between mechanical watches and modern flight displays.