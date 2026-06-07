---
name: Clean-Utility Infrastructure System
colors:
  surface: '#f8f9fb'
  surface-dim: '#d9dadc'
  surface-bright: '#f8f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f6'
  surface-container: '#edeef0'
  surface-container-high: '#e7e8ea'
  surface-container-highest: '#e1e2e4'
  on-surface: '#191c1e'
  on-surface-variant: '#45464c'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#575e70'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#141b2b'
  on-primary-container: '#7d8497'
  inverse-primary: '#c0c6db'
  secondary: '#0058be'
  on-secondary: '#ffffff'
  secondary-container: '#2170e4'
  on-secondary-container: '#fefcff'
  tertiary: '#735c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cea700'
  on-tertiary-container: '#4e3e00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce2f7'
  primary-fixed-dim: '#c0c6db'
  on-primary-fixed: '#141b2b'
  on-primary-fixed-variant: '#404758'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#ffe083'
  tertiary-fixed-dim: '#eec200'
  on-tertiary-fixed: '#231b00'
  on-tertiary-fixed-variant: '#574500'
  background: '#f8f9fb'
  on-background: '#191c1e'
  surface-variant: '#e1e2e4'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 30px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.08em
  helper-text:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
  panel-padding: 20px
---

## Brand & Style

The brand personality is authoritative, systematic, and resilient. Designed for high-stakes municipal management, this design system evokes the "Industrial-Grade" reliability of physical infrastructure translated into a digital interface. It targets city engineers, utility operators, and data analysts who require high situational awareness without visual fatigue.

The design style is a hybrid of **Minimalism** and **Modern Corporate**, with a focus on "Utility-First" aesthetics. It prioritizes information density and operational clarity over decorative elements. Surfaces are treated as functional panels, and motion is reserved for critical status changes and real-time data streaming. The emotional response is one of calm control and unwavering precision.

## Colors

This design system utilizes a "Foundation + Signal" color strategy. The base is built on a neutral, low-chroma palette of light greys (#F3F4F6) to minimize eye strain during long shifts. 

The color hierarchy is strictly functional:
- **Vibrant Blue (#2563EB):** Dedicated exclusively to Water infrastructure and hydraulic data.
- **Vibrant Yellow (#EAB308):** Dedicated exclusively to Power grids and electrical monitoring.
- **Deep Slate (#111827):** Used for typography and structural framing to provide high-contrast grounding.
- **Utility Grey (#D1D5DB):** Used for borders and grid lines to define the modular architecture.
- **Alert Red (#DC2626):** Reserved for system failures and safety-critical notifications.

## Typography

The typography pairing combines the technical, geometric precision of **Space Grotesk** for headlines and large metrics with the neutral, systematic clarity of **Inter** for all functional data and body text. 

For real-time data readouts, Inter should be used with tabular numbering (tnum) to ensure numerical columns align perfectly. Headlines are kept tight and impactful, while labels use increased letter-spacing and uppercase styling to denote categorical information. High-contrast black (#111827) text on grey/white backgrounds ensures maximum legibility in all lighting conditions.

## Layout & Spacing

The layout utilizes a **12-column fluid grid** designed for 24/7 monitoring workstations. It follows an 8px rhythmic scale, with 4px sub-units for tight component internal spacing. 

The philosophy is "Panel-Based Modularity." Content is organized into discrete, draggable containers that snap to the grid. This allows operators to customize their dashboard views based on their current focus (e.g., prioritizing Water pressure sensors during a storm). Gutters are strictly maintained at 16px to ensure visual separation of disparate data streams, while a 24px outer margin provides a professional "frame" for the entire application.

## Elevation & Depth

This design system avoids traditional shadows in favor of **Tonal Layering and Crisp Borders**. This minimizes visual "fuzziness" and reinforces the industrial aesthetic.

1.  **Level 0 (Background):** The canvas (#F3F4F6) acts as the floor of the system.
2.  **Level 1 (Panels):** Pure white (#FFFFFF) surfaces with a 1px solid border (#D1D5DB). These are the primary data containers.
3.  **Level 2 (Active/Dragging):** When a panel is moved or active, it gains a subtle, high-performance "utility shadow" (4px offset, 0px blur, black at 10% opacity) to simulate physical stacking.
4.  **Level 3 (Alerts):** High-visibility banners sit atop all other layers, using saturated background colors (Blue, Yellow, or Red) without transparency to ensure total readability.

## Shapes

The shape language is "Soft-Industrial." Elements use a consistent **0.25rem (4px) corner radius** (Soft). This provides enough modern refinement to feel "high-end" while maintaining the rigid, structured feel required for professional tools. Buttons, input fields, and panel containers all share this radius. Large structural elements, such as the main dashboard sidebar or header, utilize 0px (Sharp) corners to ground the interface against the browser edges.

## Components

### Buttons & Inputs
- **Primary Utility Button:** Solid Slate (#111827) with white Inter Bold text. 4px radius. 
- **Ghost Action:** Transparent background with 1px Slate border. Used for secondary dashboard controls.
- **Data Inputs:** White background with a persistent 1px border (#D1D5DB). On focus, the border thickens and changes to Blue (#2563EB).

### Draggable Containers (Panels)
- Each panel features a "Grab Header": a 32px top section with a light grey background (#E5E7EB) and a knurled texture icon (6 dots) to signify draggability.
- Panel titles use `headline-md` (Space Grotesk).

### High-Visibility Alert Banners
- **Water Alert:** Solid Blue (#2563EB) background, white text, 100% width.
- **Power Alert:** Solid Yellow (#FACC15) background, black text, 100% width.
- Alerts must include a "Timestamp" in `label-caps` for forensic tracking.

### Real-time Data Visualizations
- Line charts must use a 2px stroke width. 
- Areas below lines should use a 5% opacity fill of the stroke color.
- Use the **Power Yellow** or **Water Blue** for the primary data series to maintain semantic consistency.

### Status Chips
- Small, rectangular indicators with a background tint (10% opacity) and a high-contrast dot of the core color to indicate "Online," "Offline," or "Maintenance."