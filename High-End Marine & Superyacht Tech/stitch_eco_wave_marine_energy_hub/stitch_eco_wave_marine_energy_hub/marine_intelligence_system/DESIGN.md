---
name: Marine Intelligence System
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c1c7ce'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8b9198'
  outline-variant: '#41484d'
  surface-tint: '#9accf3'
  primary: '#e1f0ff'
  on-primary: '#00344d'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#2e6385'
  secondary: '#afc8f0'
  on-secondary: '#163152'
  secondary-container: '#2f486a'
  on-secondary-container: '#9eb7de'
  tertiary: '#efeeee'
  on-tertiary: '#2f3131'
  tertiary-container: '#d2d2d2'
  on-tertiary-container: '#595a5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#d4e3ff'
  secondary-fixed-dim: '#afc8f0'
  on-secondary-fixed: '#001c3a'
  on-secondary-fixed-variant: '#2f486a'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Montserrat
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-display:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 34px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  margin-edge: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for the high-stakes environment of marine energy management. It projects a personality that is authoritative yet visionary, combining the precision of aerospace instrumentation with the fluid aesthetics of the ocean. The target audience—energy analysts, marine engineers, and sustainability officers—requires a UI that facilitates deep focus and rapid data interpretation.

The visual style is a refined **Glassmorphic-Modern** hybrid. It utilizes translucent layers to simulate the depth of water, anchored by high-contrast structural elements to ensure professional reliability. Subtle kinetic energy is conveyed through "liquid" transitions and soft pulses, mirroring the rhythmic nature of tidal and wave energy. The emotional response is one of calm control and technological sophistication.

## Colors

The palette is centered on a deep maritime contrast. **Deep Navy** (#001F3F) serves as the primary structural color and canvas, providing the necessary depth for light-emitting data visualizations. **Ice Blue** (#A5D8FF) is used for primary actions, active states, and energized data points, acting as the "source of light" within the interface.

**Clean White** (#FFFFFF) is reserved for high-priority typography and iconography to ensure maximum legibility against dark backgrounds. **Silver** (#C0C0C0) is utilized for secondary metadata, borders, and inactive states. For heat-maps and thermal overlays, a complementary spectrum of teals and deep purples is permitted to maintain the "cool" marine aesthetic without relying on traditional red/yellow warm scales.

## Typography

The typography in this design system prioritizes rapid scanning of technical metrics. **Montserrat** is used for headlines to provide a geometric, high-tech architectural feel. **Inter** is the workhorse for all body copy and tabular data, chosen for its exceptional legibility and neutral character.

Numerical data should always utilize Inter with tabular-lining features enabled to ensure vertical alignment in dashboards. High-level metrics use the `data-display` style to stand out. All labels should be rendered in uppercase with slight letter spacing to differentiate them from interactive content.

## Layout & Spacing

This design system employs a **12-column fluid grid** for desktop environments, transitioning to a **4-column grid** for mobile. The layout philosophy is "Information Density with Breathing Room," using generous outer margins (32px) to frame complex data visualizations.

Spacing follows an 8px base grid. Components are grouped into "Data Pods"—logical clusters of information separated by 24px gutters. On mobile devices, the grid collapses into a single-column stack, and internal component padding is reduced from 24px to 16px to maximize screen real estate for graphs.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and tonal layering rather than traditional drop shadows. Surfaces are defined by:
1. **Base Layer:** The Deep Navy background.
2. **Container Layer:** Semi-transparent white (5-10% opacity) with a 20px backdrop blur and a subtle 1px border in Silver (#C0C0C0) at 20% opacity.
3. **Active/Elevated Layer:** Higher transparency (15%) with a soft outer glow in Ice Blue (#A5D8FF) to signify focus or critical alerts.

This "submerged" layering effect creates a sense of spatial depth that allows the user to differentiate between global navigation, primary dashboards, and modal overlays without breaking the marine aesthetic.

## Shapes

The shape language is fluid and organic yet controlled. Standard UI containers use a 16px (1rem) corner radius. Small interactive elements like chips and input fields use a 8px (0.5rem) radius. 

The design system incorporates **circular geometry** for specialized monitoring tools. Circular gauges must maintain a consistent stroke weight that matches the iconography, ensuring a cohesive "instrument panel" feel. All "liquid-style" progress bars should feature fully rounded ends to mimic fluid tension.

## Components

### Buttons & Interaction
Primary buttons use a solid Ice Blue (#A5D8FF) fill with Deep Navy text. Secondary buttons are "ghost" style with an Ice Blue border and semi-transparent fill. Hover states should trigger a subtle "ripple" gradient animation.

### Data Visualizations
- **Circular Gauges:** Use a dual-track system; a Silver background track and an Ice Blue active track for pressure and turbine speed.
- **Liquid Progress Bars:** Used for energy storage levels. The "fill" should have a slight wave-motion animation and a gradient from Deep Navy to Ice Blue.
- **Line Graphs:** Minimalist, high-contrast lines on a grid-less background. Use a subtle gradient fill below the line to show "volume."

### Input Fields & Cards
Input fields are dark-filled with a 1px Silver border that illuminates in Ice Blue upon focus. Cards (Data Pods) use the glassmorphic style with internal padding of 24px, ensuring that complex technical data never feels cramped.

### Specialized Indicators
Heat-map overlays for thermal data should use a "Cool-to-Colder" color ramp, utilizing Deep Navy for stable temps and bright Ice Blue for high-energy thermal output.