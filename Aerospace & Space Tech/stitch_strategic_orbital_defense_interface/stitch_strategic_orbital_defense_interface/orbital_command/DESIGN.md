---
name: Orbital Command
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#36393e'
  surface-container-lowest: '#0b0f12'
  surface-container-low: '#181c20'
  surface-container: '#1c2024'
  surface-container-high: '#272a2e'
  surface-container-highest: '#323539'
  on-surface: '#e0e2e8'
  on-surface-variant: '#c5c6ca'
  inverse-surface: '#e0e2e8'
  inverse-on-surface: '#2d3135'
  outline: '#8f9194'
  outline-variant: '#45474a'
  surface-tint: '#c4c6cb'
  primary: '#c4c6cb'
  on-primary: '#2e3135'
  primary-container: '#2c2f33'
  on-primary-container: '#94969b'
  inverse-primary: '#5c5e63'
  secondary: '#c2c6d8'
  on-secondary: '#2b303e'
  secondary-container: '#424655'
  on-secondary-container: '#b0b5c6'
  tertiary: '#e9c400'
  on-tertiary: '#3a3000'
  tertiary-container: '#c9a900'
  on-tertiary-container: '#4c3f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e2e7'
  primary-fixed-dim: '#c4c6cb'
  on-primary-fixed: '#191c20'
  on-primary-fixed-variant: '#44474b'
  secondary-fixed: '#dee2f4'
  secondary-fixed-dim: '#c2c6d8'
  on-secondary-fixed: '#161b28'
  on-secondary-fixed-variant: '#424655'
  tertiary-fixed: '#ffe16d'
  tertiary-fixed-dim: '#e9c400'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#544600'
  background: '#101417'
  on-background: '#e0e2e8'
  surface-variant: '#323539'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  h3:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.04em
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
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  grid_columns: '12'
  panel_padding: 12px
---

## Brand & Style

This design system establishes a "hardened" aesthetic tailored for high-stakes aerospace defense and space situational awareness. The brand personality is authoritative, precise, and utilitarian, evoking the atmosphere of a strategic command center. It targets defense contractors, orbital mechanics, and security analysts who require immediate clarity under pressure.

The visual style blends **Modern Brutalism** with **Glassmorphism**. It utilizes rigid grid structures and high-contrast "tactical" borders to create a sense of structural integrity. Overlays and telemetry data are presented on semi-transparent frosted surfaces to maintain situational awareness of the underlying orbital maps. The emotional response is one of absolute control, reliability, and technical sophistication.

## Colors

The palette is anchored in high-density metallics and deep space tones. **Gunmetal Grey** serves as the primary structural color for surfaces, providing an industrial foundation. **Deep Navy** is used for the base environment and command backgrounds, creating depth. 

**Alert Yellow** is the primary accent, reserved for critical data paths and warnings. UI Accents utilize **Tactical Blue** for active states and **Slate Grey** for secondary telemetry. Status indicators follow a strict protocol: Green for secure systems, Yellow for cautionary anomalies, and Red for immediate orbital threats or hardware failure.

## Typography

The typographic system prioritizes legibility in low-light environments. Headlines use **Space Grotesk**, a geometric face that reflects aerospace engineering; these are always set in all-caps to reinforce a military/strategic tone. 

**Inter** is the workhorse for body text and telemetry, chosen for its exceptional clarity in data-dense layouts. A "Data-Mono" variant of Inter (utilizing tabular numbers) is applied to coordinates, timestamps, and encryption keys to ensure alignment and rapid scanning. Tracking is slightly increased on all-caps labels to prevent letter-clogging on backlit displays.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy based on a 4px base unit. The primary interface is divided into a 12-column structure with 16px gutters. 

Layouts are intentionally dense, maximizing information display without sacrificing organization. Strategic "Safe Zones" are maintained at 24px margins. Elements are aligned to a rigid internal grid, creating "Tactical Containers" that group related telemetry (e.g., fuel, trajectory, and comms). Consistency in spacing reinforces the feeling of a calibrated, high-precision instrument.

## Elevation & Depth

Depth is conveyed through a combination of **Glassmorphism** and **Tonal Layering**. Unlike consumer apps, this system avoids soft ambient shadows. Instead, it uses:

1.  **Backdrop Blurs:** High-strength (20px-30px) blurs on semi-transparent gunmetal surfaces allow orbital maps to remain visible behind active menus.
2.  **Inner Bevels:** Subtle, 1px light-source highlights on the top edges of buttons and containers to simulate physical, milled hardware.
3.  **High-Contrast Outlines:** 1px borders in Slate Grey (#4A4E54) or Tactical Blue define container boundaries, ensuring clear separation of data streams.
4.  **Z-Axis Priority:** Modal windows and critical alerts use higher opacity and brighter border-weights to "pierce" through the background telemetry.

## Shapes

The shape language is strictly **Sharp (0px)**. All containers, buttons, and status indicators use right angles to communicate a "hardened" and industrial aesthetic. 

The only exception to this rule is the "Telemetry Node" or "Satellite Icon," which uses geometric circles for mathematical accuracy. By avoiding rounded corners, the interface feels more like a piece of military hardware than a consumer software product. Use 45-degree chamfered corners on high-level navigation tabs to reinforce the aerospace theme.

## Components

### Buttons
Primary buttons are solid Alert Yellow with black text. Secondary buttons are ghost-style with Gunmetal Grey borders and Tactical Blue text. All buttons feature a 1px inner bevel for a tactile feel and use all-caps typography.

### Tactical Containers (Cards)
Containers use a semi-transparent Deep Navy background with a 1px Slate Grey border. For critical alerts, the border pulses in Alert Yellow. Header bars within containers are Gunmetal Grey with a distinct separation line.

### Data Inputs
Input fields are "inset" with a darker Navy background and a high-contrast bottom border. Focused states change the border color to Tactical Blue and trigger a subtle outer glow.

### Status Indicators
Small, square blocks that use high-saturation status colors. "Secure" states use a steady Green, while "Warning" or "Critical" states may include a slow-pulsing animation to draw immediate attention.

### Telemetry HUD
Specialized components for displaying real-time coordinates. These use the Data-Mono font weight and are often housed in a "Glass" overlay with a heavy backdrop blur to ensure they remain legible over complex 3D orbital renders.

### Coordinate Grids
Background elements featuring faint 1px grid lines and axis labels at the periphery, providing a constant sense of spatial orientation.