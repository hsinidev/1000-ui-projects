---
name: Performance Industrial UI
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e7bcb9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#ae8885'
  outline-variant: '#5d3f3d'
  surface-tint: '#ffb3ae'
  primary: '#ffb3ae'
  on-primary: '#68000c'
  primary-container: '#e6192e'
  on-primary-container: '#fffcff'
  inverse-primary: '#c00020'
  secondary: '#a3c9ff'
  on-secondary: '#00315d'
  secondary-container: '#1493ff'
  on-secondary-container: '#002a51'
  tertiary: '#ffba20'
  on-tertiary: '#412d00'
  tertiary-container: '#996d00'
  on-tertiary-container: '#fffcff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ae'
  on-primary-fixed: '#410005'
  on-primary-fixed-variant: '#930016'
  secondary-fixed: '#d3e3ff'
  secondary-fixed-dim: '#a3c9ff'
  on-secondary-fixed: '#001c39'
  on-secondary-fixed-variant: '#004883'
  tertiary-fixed: '#ffdea8'
  tertiary-fixed-dim: '#ffba20'
  on-tertiary-fixed: '#271900'
  on-tertiary-fixed-variant: '#5e4200'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: spaceGrotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-base:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: spaceGrotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
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
  gutter: 16px
  margin: 24px
  container-max: 1280px
---

## Brand & Style
This design system is engineered for the high-performance automotive enthusiast. It evokes the atmosphere of a professional tuning garage: precise, rugged, and unapologetically technical. The visual narrative centers on "Mechanical Fidelity"—where every interface element feels like a machined component rather than a digital abstraction.

The style is a hybrid of **Tactile Skeuomorphism** and **High-Contrast Industrialism**. It utilizes depth, texture, and light to simulate physical materials like carbon fiber, brushed aluminum, and powder-coated steel. The emotional goal is to instill confidence through a "tool-grade" aesthetic, prioritizing durability and performance over softness or playfulness.

## Colors
The palette is dominated by "Oil and Steel"—a range of ultra-dark neutrals that provide a high-contrast foundation for critical data visualization.

*   **Primary (Racing Red):** Reserved for high-priority actions, critical warnings, and performance indicators.
*   **Secondary (Electric Blue):** Used for technical data, tuning parameters, and interactive states.
*   **Tertiary (Nitrous Yellow):** Used for cautionary states and secondary data highlights.
*   **Neutrals:** A spectrum of grays from `Onyx (#0A0A0A)` to `Titanium (#A1A1A1)`. 

Apply a 10% opacity noise texture or carbon-fiber pattern overlay on the primary background layers to eliminate flat surfaces and reinforce the industrial theme.

## Typography
Typography follows the logic of automotive instrumentation: clarity under pressure. 

**Space Grotesk** serves as the primary technical typeface for headlines, labels, and data readouts. Its geometric construction mimics the legibility of modern digital dashboards. **Inter** is used for body copy to ensure long-form readability in manuals and forum threads.

All labels should be rendered in uppercase with wide tracking to emulate stamped metal plates. Numerical data should always use tabular figures to ensure alignment in high-frequency data streams.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model based on a 4px "Machined" rhythm. Components are tightly packed to maximize information density, reflecting the complex layouts of professional diagnostic tools.

*   **Grid:** 12-column system with 16px gutters.
*   **Density:** High. Padding within components should be minimal but consistent to maintain a "precise" feel.
*   **Alignment:** Hard edges and strict vertical alignment are mandatory. Avoid loose, floating elements; every component should feel "bolted" to the grid.

## Elevation & Depth
Depth is achieved through **Tonal Layering** and **Internal Beveling** rather than traditional drop shadows. 

1.  **Sunken Layers (Inputs/Wells):** Use inner shadows and darker backgrounds to make elements look recessed into the dashboard.
2.  **Raised Layers (Buttons/Cards):** Use subtle linear gradients (top-to-bottom, light-to-dark) to simulate a physical, convex surface.
3.  **Metallic Accents:** Apply 1px "specular highlights" to the top edge of components to simulate light catching on a beveled metal edge.
4.  **Carbon Surfaces:** Use texture overlays for the lowest z-index surfaces to provide visual weight.

## Shapes
The shape language is "Soft-Industrial." While sharp 90-degree angles are the baseline, a subtle 0.25rem (4px) radius is applied to external corners to simulate "milled" edges that have been deburred for handling.

Avoid large, organic curves or pill shapes. Circles are permitted only for gauges and dials that mimic analog instrumentation. Container borders should be prominent, using a 1px or 2px stroke in a "Gunmetal" or "Steel" shade to define boundaries clearly.

## Components
### Buttons
Buttons are treated as "Actuators." The default state features a subtle metallic gradient and a 1px border. The `Active` state should look "pressed" via an inner shadow, while the `Hover` state increases the brightness of the primary accent color (Racing Red or Electric Blue) as if the component is being backlit.

### Inputs
Inputs are "recessed wells." They should feature a darker background than the surface they sit on, with a sharp internal shadow. Focus states are indicated by a high-intensity outer glow in the secondary accent color.

### Cards & Containers
Containers should use "Carbon Fiber" or "Brushed Metal" background textures. Headers within cards should be separated by a "v-groove" (a 2px divider consisting of a 1px dark line and a 1px light highlight line).

### Status Chips
Chips are designed to look like integrated LED indicators. Use a small circular icon with a "glow" effect (radial gradient) to indicate system status (e.g., Engine: OK, Diagnostics: Active).

### Specialized Components
*   **Gauges:** Circular or semi-circular progress bars with segmented increments to show torque, RPM, or pressure.
*   **Data Strips:** Dense, monospaced rows of data with alternating background shades for high-speed scanning of repair logs.