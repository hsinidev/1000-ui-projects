---
name: Aero-Technical Hub
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c1c7ce'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8b9198'
  outline-variant: '#41484d'
  surface-tint: '#9accf3'
  primary: '#e1f0ff'
  on-primary: '#00344d'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#2e6385'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#eeeeee'
  on-tertiary: '#2f3131'
  tertiary-container: '#d1d2d2'
  on-tertiary-container: '#585a5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-desktop: 48px
  margin-mobile: 16px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for the precision-obsessed world of high-performance EV aerodynamics. It projects a "Scientific-Sleek" personality: authoritative, cold, and hyper-efficient. The target audience—aerodynamicists, automotive engineers, and performance data analysts—requires an interface that feels less like a website and more like a high-precision digital instrument.

The visual narrative is driven by **Glassmorphism** and **Technical Minimalism**. It evokes the sensation of looking through a clean laboratory viewport into a wind tunnel. Surfaces are semi-translucent to maintain a sense of depth and layered data, while thin, high-contrast technical borders define the structure. Glowing accents and "wind-tunnel" gradients (linear streaks representing airflow) provide a sense of motion and kinetic energy without compromising the rigorous, data-first utility.

## Colors

The palette is anchored in **Deep Slate (#1A1A1A)** to provide a void-like technical contrast, essential for high-fidelity data visualization. **Ice Blue (#A5D8FF)** serves as the primary functional color, used for active states, data highlights, and simulated "airflow" accents. 

**Silver (#C0C0C0)** and **Clean White (#FFFFFF)** are reserved for technical nomenclature and high-priority readouts, ensuring maximum legibility against dark backgrounds. This design system utilizes "wind-tunnel" gradients—subtle, horizontal linear transitions from Ice Blue to transparent—to indicate directionality and fluid dynamics within the UI.

## Typography

This design system employs a dual-font strategy to distinguish between UI navigation and technical data. **Inter** provides a neutral, high-end sans-serif foundation for layout labels, headers, and descriptive text, ensuring the interface remains sophisticated and readable.

**JetBrains Mono** is the "instrument font." It is used exclusively for numerical readouts, sensor data, telemetry, and any technical labels. The monospaced nature ensures that fluctuating data values do not cause visual "jitter," maintaining the stability required for high-precision monitoring. All data labels should use the `label-caps` style to mimic engraved markings on laboratory equipment.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to simulate the locked-in feel of a dashboard. A 12-column grid is used for desktop, with a tight 16px gutter to maximize data density. Components are aligned to a strict 4px baseline grid, ensuring that every instrument and readout feels mathematically aligned.

On mobile, the grid collapses to 4 columns with reduced margins. Padding within components is intentionally sparse to maintain a "technical" feel, prioritizing information density over "breathability." High-priority telemetry should occupy the top-level "Viewport" area, while secondary controls are docked in collapsible side-panels to mimic professional CAD software.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional shadows. Surfaces are treated as physical layers of glass:
- **Level 1 (Base):** Deep Slate (#1A1A1A).
- **Level 2 (Panels):** Semi-transparent Deep Slate with a 12px Backdrop Blur and a 0.5px solid Silver border at 20% opacity.
- **Level 3 (Pop-overs/Modals):** Lighter transparency with a 20px blur and a subtle 1px Ice Blue outer glow to indicate focus.

Instead of shadows, use "inner-glow" strokes on active elements to simulate backlighting. This creates a self-illuminated look consistent with modern high-end vehicle cockpits.

## Shapes

The design system utilizes **Sharp (0)** corners for all primary containers, panels, and data modules to reinforce the feeling of precision engineering. Soft or rounded corners are avoided as they imply "consumer-friendly" softness, whereas sharp 90-degree angles communicate rigor and technical accuracy.

Subtle exceptions are made for "status pills" or "active flow indicators," which may use a 1px radius to prevent visual aliasing on low-resolution displays, but the overarching aesthetic remains strictly rectilinear.

## Components

### Buttons & Controls
Buttons are designed as "switches." They feature a transparent background with a 1px Silver border. On hover, the border glows Ice Blue and a faint "wind-tunnel" gradient fills the background from left to right. Text is always uppercase JetBrains Mono.

### Technical Inputs
Input fields are simple underlines rather than boxes, with the current value displayed in JetBrains Mono. When focused, the underline expands into a thin Ice Blue rectangle with a 10% opacity fill.

### Data Cards
Cards are the primary container for telemetry. They must include a "technical header" — a thin Silver line at the top with the sensor ID in the top-left corner and the timestamp in the top-right in `label-caps`.

### Wind-Tunnel Visualizers
A unique component for this system, these use Ice Blue vector lines to show airflow density. They should be overlaid on semi-transparent glass panels to maintain the multi-layered viewport effect.

### Checkboxes & Radios
These are rendered as "bits." A checkbox is a small empty square that fills with a solid Ice Blue square when active. No checkmarks are used—only geometric state changes.