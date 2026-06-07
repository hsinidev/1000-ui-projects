---
name: Fluid & Technical
colors:
  surface: '#f7fafc'
  surface-dim: '#d7dadc'
  surface-bright: '#f7fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f6'
  surface-container: '#ebeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#e0e3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#43474e'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f3'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#455f88'
  primary: '#002045'
  on-primary: '#ffffff'
  primary-container: '#1a365d'
  on-primary-container: '#86a0cd'
  inverse-primary: '#adc7f7'
  secondary: '#545f72'
  on-secondary: '#ffffff'
  secondary-container: '#d5e0f7'
  on-secondary-container: '#586377'
  tertiary: '#00213e'
  on-tertiary: '#ffffff'
  tertiary-container: '#003762'
  on-tertiary-container: '#58a2f0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f7'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#d8e3fa'
  secondary-fixed-dim: '#bcc7dd'
  on-secondary-fixed: '#111c2c'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#d2e4ff'
  tertiary-fixed-dim: '#9fcaff'
  on-tertiary-fixed: '#001d37'
  on-tertiary-fixed-variant: '#00497e'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is engineered for the high-stakes environment of municipal infrastructure management. The brand personality is authoritative, precise, and hyper-aware, blending industrial reliability with the dynamic nature of fluid dynamics. The UI evokes a sense of "controlled flow"—translating complex sewage and water data into a high-precision, actionable interface.

The design style utilizes a **Modern-Technical** approach with **Glassmorphism** accents. It prioritizes clarity through high-contrast data visualization while softening the industrial edge with translucent layers that suggest the transparency of water. The emotional response is one of calm confidence, ensuring operators feel in control of critical city systems.

## Colors

The palette is anchored by **Deep Cobalt**, representing the depth and reliability of municipal water systems. **Slate Grey** provides the industrial scaffolding, used for structural elements and secondary metadata. **Crisp White** serves as the sterile, high-contrast canvas for data.

To support the "Fluid" aesthetic, a secondary **Data Cyan** and **Electric Blue** are introduced for active flow states and "Liquid" progress indicators. High-contrast status colors are reserved for critical alerts, ensuring they pierce through the technical interface during emergencies.

## Typography

This design system employs a dual-typeface strategy. **Inter** handles all functional UI and long-form reading, providing a neutral, systematic foundation. **Space Grotesk** is used for all data points, telemetry, and labels to inject a "Technical/Futuristic" geometric quality that aligns with infrastructure sensors.

All numerical data should be set in Space Grotesk to ensure maximum readability in high-density dashboards. Use uppercase labels for hardware IDs and sensor locations to maintain an industrial, schematic feel.

## Layout & Spacing

The layout follows a **Rigid Fluid Grid**. While the overall container stretches to fill industrial monitors (fluid), the internal components are locked to a strict 4px baseline grid (rigid). 

Dashboards utilize a 12-column system where cards and data modules snap to specific column spans (3, 4, 6, or 12). Gutters are generous at 24px to prevent visual "clogging" of information, reflecting the need for clear pathways and flow.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Glassmorphism** rather than traditional drop shadows. 

1.  **Base Surface:** Crisp White (#FFFFFF) for the main work area.
2.  **Translucent Overlays:** Used for sidebars and floating inspector panels. These feature a `backdrop-filter: blur(12px)` and a highly subtle 1px border in Deep Cobalt at 10% opacity.
3.  **Inset Depth:** Progress bars and data wells use an inner-shadow effect to appear "recessed" into the hardware, simulating pipes or channels.
4.  **Active Elevation:** Only the most critical active alerts use a soft, Deep Cobalt ambient shadow to lift them above the technical noise.

## Shapes

The shape language is **Technical-Precision**. A "Soft" (0.25rem) radius is applied to primary UI containers to prevent the interface from feeling sharp or hostile, yet it remains sufficiently rectangular to feel like a professional instrument.

Interactive elements like buttons use the same 0.25rem radius, while "Liquid" progress bars utilize a fully rounded (Pill) shape to mimic the internal profile of a pipe.

## Components

### Buttons & Inputs
Buttons are high-contrast: Deep Cobalt background with White text for primary actions. They feature a subtle "sheen" gradient (top-to-bottom) to suggest a physical, wipe-clean surface. Inputs are "Slate Grey" outlines that fill with a 5% Deep Cobalt tint when focused.

### Liquid Progress Bars
Instead of flat color fills, progress bars utilize a "Wave" animation. The fill color is a gradient of Data Cyan, and the leading edge of the bar has a slight oscillation effect to simulate fluid movement within the track.

### Data Visualization
Charts must use thick stroke weights (3px minimum) for line graphs to represent "pipes." Intersections of data points should be marked with "Node" icons—hollow circles that suggest connectivity points in a network.

### Cards & Modules
Cards serve as "Sensor Blocks." They feature a header area with a Space Grotesk label and a 1px bottom divider. Backgrounds are solid white, but "Secondary Modules" can use a glassmorphic background when placed over map layers.

### Infrastructure Chips
Small, high-contrast tags used to identify "Sewage," "Potable," or "Stormwater." These use the Label-Caps typography and are color-coded based on the specific utility type.