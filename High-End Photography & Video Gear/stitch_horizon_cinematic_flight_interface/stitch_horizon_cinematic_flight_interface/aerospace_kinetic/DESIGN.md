---
name: Aerospace Kinetic
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
  on-surface-variant: '#bbc9cf'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#859398'
  outline-variant: '#3c494e'
  surface-tint: '#3cd7ff'
  primary: '#a8e8ff'
  on-primary: '#003642'
  primary-container: '#00d4ff'
  on-primary-container: '#00586b'
  inverse-primary: '#00677e'
  secondary: '#b9c7e4'
  on-secondary: '#233148'
  secondary-container: '#3c4962'
  on-secondary-container: '#abb9d6'
  tertiary: '#e1dedf'
  on-tertiary: '#303031'
  tertiary-container: '#c4c2c3'
  on-tertiary-container: '#505051'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b4ebff'
  primary-fixed-dim: '#3cd7ff'
  on-primary-fixed: '#001f27'
  on-primary-fixed-variant: '#004e5f'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#e5e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474647'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
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
  margin: 40px
  container-max: 1440px
---

## Brand & Style

This design system embodies the precision and velocity of high-end aerial imaging. The brand personality is authoritative, technical, and forward-looking, targeting professional cinematographers and aerospace engineers who require instantaneous data clarity and high-performance reliability. 

The visual style is a fusion of **Glassmorphism** and **Minimalism**, filtered through a cockpit-instrumentation lens. It utilizes deep layering to simulate the depth of the horizon, while maintaining a rigorous, grid-based structural integrity. Design elements should evoke the feeling of a Head-Up Display (HUD), using vector-line graphics and technical schemas to imply motion and altitude. The emotional response is one of total control and premium craftsmanship.

## Colors

The palette is optimized for low-light environments and high-contrast legibility. 

- **Primary (Cyan):** Used exclusively for interactive states, data visualization, and critical telemetry indicators. It represents active energy.
- **Secondary (Deep Navy):** The foundational canvas color, providing a professional depth that reduces eye strain during long-duration flight monitoring.
- **Tertiary (Carbon Gray):** Used for structural backgrounds and "solid" hardware-mimicking components.
- **Neutral (Crisp White):** Reserved for high-priority typography and essential iconography to ensure maximum readability against dark backgrounds.
- **Surface Accents:** Subtle gradients of Navy to Carbon Gray are used to define component boundaries without heavy borders.

## Typography

This design system utilizes a dual-font strategy to balance character and utility. **Space Grotesk** provides a technical, futuristic edge for headlines and labels, echoing the aesthetics of aerospace instrumentation. **Inter** is employed for body copy and telemetry readouts due to its exceptional legibility and neutral tone.

All labels should be set in uppercase with increased letter spacing to mimic cockpit dial markings. Data readouts should prioritize the tabular-nums feature of Inter to ensure vertical alignment in fluctuating numerical displays.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model within a maximum container width, transitioning to a fluid behavior for internal data modules. A 12-column grid is standard, with generous 24px gutters to allow technical line art and 3D configurators room to breathe. 

Spacing is governed by a 4px base unit. Component internal padding should be generous (16px or 24px) to emphasize the "clean" aerospace aesthetic. Vertical rhythm is strictly maintained to ensure that multi-column telemetry dashboards remain scannable during high-velocity interaction.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and **Tonal Layering** rather than traditional drop shadows.

1.  **Base Layer:** Solid Deep Navy Blue (#0A192F).
2.  **Surface Layer:** Carbon Fiber Gray (#1A1A1B) with a subtle diagonal 2px pattern overlay at 5% opacity.
3.  **Overlay Layer:** Frosted Cyan or Navy glass. Use `backdrop-filter: blur(12px)` and a 1px inner border (stroke) of #FFFFFF at 10% opacity to define the edges.
4.  **Interactive Layer:** High-luminance Cyan glow. When an element is active, use a soft outer glow (`box-shadow: 0 0 15px rgba(0, 212, 255, 0.3)`) instead of a traditional shadow to imply light emission from a screen.

## Shapes

The shape language is "Soft-Industrial." Corners are predominantly set to a 4px (0.25rem) radius to maintain a precise, engineered feel without being unnecessarily sharp. 

- **Standard Elements:** 4px radius.
- **Large Containers/Cards:** 8px radius.
- **Data Tags:** 2px radius or sharp edges to emphasize a "cut-metal" aesthetic.
- **Vector Accents:** Use 45-degree clipped corners (chamfers) on decorative line art to reinforce the aerospace theme.

## Components

- **Buttons:** Primary buttons feature a solid Cyan fill with black text for maximum contrast. Secondary buttons use a "ghost" style with a 1px Cyan border and glass background.
- **High-Contrast Data Readouts:** Numerical displays should be housed in dark, recessed containers with "glow" text effects for critical alerts.
- **3D-Perspective Configurators:** Interactive drone models should be framed by technical crosshairs and coordinate axes in 0.5px line weight.
- **Input Fields:** Use an "underlined" style or a very subtle glass inset. The focus state must trigger a full-border Cyan illumination.
- **Chips/Status Indicators:** Small, rectangular tags with monochromatic fills. Use the "Data-Mono" typography style.
- **Technical Line Art:** All icons and decorative elements must use a consistent 1.5px stroke width with open paths to imply blueprints.
- **Telemetry Cards:** Utilize a 10% transparent white border and a subtle carbon fiber background texture to separate high-level stats from the main viewport.