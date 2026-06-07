---
name: Apex Engineering
colors:
  surface: '#210e0b'
  surface-dim: '#210e0b'
  surface-bright: '#4b332f'
  surface-container-lowest: '#1b0907'
  surface-container-low: '#2a1613'
  surface-container: '#2f1a16'
  surface-container-high: '#3b2420'
  surface-container-highest: '#472f2b'
  on-surface: '#ffdad4'
  on-surface-variant: '#eabcb4'
  inverse-surface: '#ffdad4'
  inverse-on-surface: '#422b26'
  outline: '#b08780'
  outline-variant: '#5f3e39'
  surface-tint: '#ffb4a7'
  primary: '#ffb4a7'
  on-primary: '#670400'
  primary-container: '#ff553d'
  on-primary-container: '#5b0300'
  inverse-primary: '#be0e00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#abc7ff'
  on-tertiary: '#002f66'
  tertiary-container: '#438fff'
  on-tertiary-container: '#002959'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a7'
  on-primary-fixed: '#400200'
  on-primary-fixed-variant: '#910900'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#d7e2ff'
  tertiary-fixed-dim: '#abc7ff'
  on-tertiary-fixed: '#001b3f'
  on-tertiary-fixed-variant: '#00458f'
  background: '#210e0b'
  on-background: '#ffdad4'
  surface-variant: '#472f2b'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
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
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  panel-padding: 20px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system is engineered to evoke the high-stakes, precision-driven atmosphere of a Formula 1 paddock. It targets engineers, strategists, and high-performance fans who demand instantaneous data clarity and technical depth. The brand personality is aggressive, hyper-functional, and unapologetically industrial.

The visual style combines **Glassmorphism** with **Industrial Minimalism**. Surfaces use semi-transparent dark layers to allow underlying carbon-fiber textures and data visualizations to remain visible, creating a sense of depth and complexity. Interactive elements feature glowing, high-energy borders that simulate live telemetry and active power states.

## Colors
The palette is rooted in a "Blacked Out" aesthetic to maximize contrast for critical telemetry.

- **Primary (Racing Red):** Used exclusively for high-priority actions, critical alerts, and active state highlights.
- **Secondary (Metallic Silver):** Reserved for technical labels, secondary UI borders, and iconography to provide a cold, machined feel.
- **Backgrounds:** A tiered system of Deep Charcoal and Pure Black. Use the `background_base` for the main canvas and `background_surface` for panels.
- **Functional States:** Success is represented by a high-vis Cyan, Warning by Amber, and Danger by the Primary Racing Red.

## Typography
Typography in this design system is built for speed and legibility under pressure. 

**Space Grotesk** is utilized for all headings and technical labels, always set in italics to suggest forward momentum. High-contrast headers should be used to anchor data-heavy layouts. **Lexend** is used for body copy to provide a grounding, athletic readability. All numerical data should use the "data-mono" style to ensure columns of figures align perfectly for rapid scanning.

## Layout & Spacing
The design system utilizes a **Fixed 12-Column Grid** for dashboard views and a **Fluid Flexbox Model** for component internals. 

A 4px baseline grid ensures mathematical precision in element alignment. Margins and gutters are kept tight (16-24px) to increase information density, reflecting the cramped, efficient cockpit of an F1 car. Use "Stack" variables to maintain consistent vertical rhythm between data visualizations and their associated controls.

## Elevation & Depth
Depth is created through transparency and light rather than shadows.

- **Tier 1 (Base):** Solid `#0A0A0A` with a subtle carbon-fiber texture overlay (low opacity).
- **Tier 2 (Panels):** Semi-transparent `#141414` (80% opacity) with a 1px `Metallic Silver` border (15% opacity).
- **Tier 3 (Overlays/Modals):** Glassmorphism effect with a 20px backdrop blur and a 1px `Racing Red` border for active alerts.
- **Interactive Depth:** When an element is focused or active, it should emit an outer "inner glow" using the `accent_glow` token, simulating illuminated cockpit buttons.

## Shapes
The design system employs a **Sharp (0px)** corner radius across all primary components to reinforce a technical, machined aesthetic. 

- **Angled Cuts:** Use 45-degree chamfered corners for buttons and status badges to evoke aerodynamic components.
- **Dividers:** Use ultra-thin 1px lines in Metallic Silver to separate data sets.
- **Active Indicators:** Use small, vertical rectangular "pips" next to menu items or tabs to indicate selection.

## Components
Consistent implementation of these components ensures the interface feels like an integrated piece of racing hardware.

- **Primary Buttons:** Sharp edges, solid `Racing Red` background, white uppercase text. On hover, apply a 2px outer glow of the same color.
- **Gauges & Charts:** Radial gauges should use segmented arcs. Line charts should be rendered with 1px width and no smoothing (sharp vertices) to emphasize raw data.
- **Status Badges:** Use "Angled Cut" containers. Backgrounds should be low-opacity versions of the status color (e.g., 10% Red) with a high-saturation 1px border.
- **Segmented Controls:** Designed to look like physical toggle switches. The active segment should be Metallic Silver with black italicized text.
- **Technical Inputs:** Dark backgrounds with a subtle bottom-only border. Upon focus, the border animates to a full box in Racing Red with a "Data Scanning" pulse effect.
- **Data Cards:** Utilize the glassmorphism style defined in Elevation. Include a small "Sensor ID" label in the top-right corner in the `label-caps` typography style.