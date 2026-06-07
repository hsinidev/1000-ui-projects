---
name: SkyCen
colors:
  surface: '#121416'
  surface-dim: '#121416'
  surface-bright: '#38393c'
  surface-container-lowest: '#0c0e10'
  surface-container-low: '#1a1c1e'
  surface-container: '#1e2022'
  surface-container-high: '#282a2c'
  surface-container-highest: '#333537'
  on-surface: '#e2e2e5'
  on-surface-variant: '#bec7d4'
  inverse-surface: '#e2e2e5'
  inverse-on-surface: '#2f3033'
  outline: '#88919d'
  outline-variant: '#3f4852'
  surface-tint: '#98cbff'
  primary: '#98cbff'
  on-primary: '#003354'
  primary-container: '#00a3ff'
  on-primary-container: '#00375a'
  inverse-primary: '#00629d'
  secondary: '#c5c7ca'
  on-secondary: '#2e3133'
  secondary-container: '#44474a'
  on-secondary-container: '#b3b5b8'
  tertiary: '#ffb4aa'
  on-tertiary: '#690003'
  tertiary-container: '#ff6f5f'
  on-tertiary-container: '#700003'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#cfe5ff'
  primary-fixed-dim: '#98cbff'
  on-primary-fixed: '#001d33'
  on-primary-fixed-variant: '#004a77'
  secondary-fixed: '#e1e2e6'
  secondary-fixed-dim: '#c5c7ca'
  on-secondary-fixed: '#191c1e'
  on-secondary-fixed-variant: '#44474a'
  tertiary-fixed: '#ffdad5'
  tertiary-fixed-dim: '#ffb4aa'
  on-tertiary-fixed: '#410001'
  on-tertiary-fixed-variant: '#930005'
  background: '#121416'
  on-background: '#e2e2e5'
  surface-variant: '#333537'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  telemetry-data:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  body-sm:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
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
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 12px
  margin: 16px
---

## Brand & Style
This design system is engineered for the high-stakes environment of municipal aviation and airspace management. It adopts a **High-Tech Glassmorphism** aesthetic, drawing direct inspiration from modern avionics and integrated flight decks. The brand personality is clinical, precise, and authoritative, ensuring that operators can manage complex telemetry without cognitive overload.

The visual language balances the ethereal nature of flight with the rigid hardware of a cockpit. Every element is designed to feel like a calibrated instrument, utilizing semi-transparent surfaces to maintain spatial awareness across multiple data layers. The result is a professional, aerodynamic interface that evokes trust and technical mastery.

## Colors
The palette is centered on a deep **Matte Black** base to minimize glare in low-light operations centers and cockpits. **Sky Blue** serves as the primary action and "active state" color, providing high-contrast visibility against the dark background. 

**Silver** is utilized for secondary information, borders, and inactive states, mimicking the brushed-metal housing of flight instruments. An auxiliary **Alert Red** (Tertiary) is reserved strictly for critical telemetry warnings and airspace incursions. The use of color is disciplined, ensuring that every hue on the screen conveys specific operational meaning.

## Typography
**Space Grotesk** is the sole typeface for this design system, chosen for its geometric precision and technical "cutting-edge" feel. Its open apertures ensure legibility at small sizes, which is critical for dense data displays.

The typographic hierarchy prioritizes alphanumeric clarity. Telemetry readouts utilize a specific weight and tracking to mimic digital altimeters. Labels are frequently set in uppercase with increased letter-spacing to distinguish them from dynamic data points. All type must be rendered with high-contrast anti-aliasing to maintain sharpness against glass-morphic backgrounds.

## Layout & Spacing
The layout follows a **Fluid Grid** model optimized for ultra-wide monitoring stations. A strict 4px baseline rhythm is used to maintain a "tight but functional" density, allowing for a high volume of telemetry on a single screen without sacrificing scanability.

Containers and panels use narrow gutters (12px) to maximize the use of screen real estate. Information is clustered into logical modules—reminiscent of Multi-Function Displays (MFDs)—with consistent internal padding (16px) to ensure touch and click targets are distinct in high-stress situations.

## Elevation & Depth
Elevation in this design system is achieved through **Backdrop Blurs and Tonal Layering** rather than traditional drop shadows. Shadows are avoided to prevent the UI from feeling "heavy" or "muddy."

1.  **Base Layer:** Solid Matte Black (#0A0C0E).
2.  **Surface Layer:** Semi-transparent Sky Blue or Silver (5-10% opacity) with a 20px backdrop blur.
3.  **Border Layer:** 1px solid Silver or Sky Blue at 20% opacity. This creates the "crisp border" effect that defines the glass cockpit aesthetic.
4.  **Active Focus:** Elements in focus increase their border opacity to 80% and may utilize a subtle inner glow to simulate backlighting.

## Shapes
This design system utilizes a **Soft (Level 1)** roundedness approach. A 4px (0.25rem) corner radius is applied to all primary panels, buttons, and input fields. This slight rounding suggests aerodynamic efficiency while maintaining the rigid, professional structure required for an industrial aviation tool. 

Radar sweeps and circular status indicators are the only exceptions, utilizing full pill or circular shapes to represent radial data accurately.

## Components
### Buttons & Inputs
Buttons are rendered as "bezel-less" glass tiles with 1px crisp borders. The primary action button uses a Sky Blue border and text, filling with a 15% Sky Blue tint on hover. Input fields are dark, recessed wells with technical labels positioned inside the top border.

### Telemetry Cards
The core of the interface; these cards house real-time data like wind speed, altitude, and aircraft ID. They feature a header area with `label-caps` typography and a main area for `telemetry-data`.

### Status Chips
Small, high-contrast indicators that flash or pulse when data exceeds safety parameters. These use the Tertiary (Alert Red) or Primary (Sky Blue) colors to indicate "Danger" or "Active Tracking."

### Glass Panels
All main layout sections are contained within glass panels. These panels must have a `backdrop-filter: blur(20px)` and a thin, high-contrast silver border to separate them from the tactical map or radar background.

### Tactical Radar Overlay
A custom component featuring concentric rings and vector lines, using the Primary Sky Blue for all markings. All UI elements placed over the radar must use the glass-morphic style to ensure the underlying map data remains partially visible.