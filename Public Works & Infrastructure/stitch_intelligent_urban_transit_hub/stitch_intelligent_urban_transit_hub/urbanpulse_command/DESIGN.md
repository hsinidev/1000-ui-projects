---
name: UrbanPulse Command
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#111518'
  on-tertiary: '#ffffff'
  tertiary-container: '#26292c'
  on-tertiary-container: '#8d9094'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e0e2e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1f'
  on-tertiary-fixed-variant: '#44474a'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
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
  xl: 32px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is engineered for the high-stakes environment of municipal logistics and transit oversight. The brand personality is authoritative, vigilant, and hyper-efficient, designed to evoke a sense of absolute control and real-time responsiveness. The target audience—transit controllers and urban planners—requires a UI that prioritizes cognitive clarity over decorative flair.

The design style is **Corporate / Modern** with a technical edge. It borrows the density of industrial dashboards while maintaining the accessibility of a modern SaaS product. The interface utilizes a rigorous "Command Center" aesthetic, characterized by high-density information clusters, structured data grids, and a systematic approach to visual hierarchy that ensures the most critical alerts are surfaced instantly without overwhelming the operator.

## Colors

The palette is anchored by **Royal Blue (#002366)**, used strategically to denote primary actions and brand presence. **Graphite (#333333)** serves as the foundation for typography and structural borders, providing high contrast against the **White (#FFFFFF)** workspace.

The color system utilizes a functional logic:
- **Primary:** Navigation, primary buttons, and active state indicators.
- **Secondary (Graphite):** Text, iconography, and high-emphasis borders.
- **Neutral (Light Gray/White):** Surface backgrounds and container fills to reduce visual noise.
- **Status Tints:** High-saturation Red, Amber, and Green are reserved strictly for traffic status and transit alerts to maintain the "Precision" aesthetic.

## Typography

This design system utilizes **Inter** for all functional and reading text due to its exceptional legibility in data-dense environments. For technical readouts, timestamps, and "command center" labels, **Space Grotesk** is used to provide a subtle geometric, futuristic feel that distinguishes raw data from UI instructions.

- **Headlines:** Use tight letter spacing and bold weights to project authority.
- **Body:** Standardized at 14px for optimal density; line height is kept tight but breathable.
- **Labels:** Small caps with increased tracking are used for non-interactive metadata to save vertical space while remaining legible.

## Layout & Spacing

The design system employs a **Fluid Grid** model with a 4px baseline shift. This allows the UI to scale across massive operations-center displays and mobile tablets alike. 

- **Grid:** A 12-column system is used for dashboard layouts.
- **Density:** High. Padding within components is minimized (8px–12px) to maximize the "at-a-glance" data surface area.
- **Rhythm:** Vertical spacing between data widgets follows a 16px (md) scale to create clear separation between distinct transit streams.

## Elevation & Depth

To maintain a "Fast & Precise" feel, the system avoids heavy shadows. Depth is communicated primarily through **Tonal Layers** and **Crisp Borders**.

- **Surfaces:** The main canvas is White (#FFFFFF). Secondary panels or sidebars use a very light gray (#F9FAFB) to recede.
- **Borders:** All interactive containers and data widgets use a 1px solid border (#E5E7EB). Active or focused states upgrade this to the Primary Royal Blue or Graphite.
- **Shadows:** Use only one level of elevation—a "precision shadow." This is a tight, 2px blur with 5% opacity, used only to lift active modals or floating map controls off the base layer.

## Shapes

The shape language is **Soft (1)**, using a 0.25rem (4px) corner radius as the standard. This maintains a technical, "engineered" look that is more approachable than sharp 90-degree angles but more serious than highly rounded UI.

- **Small elements:** Buttons and input fields use the 4px radius.
- **Large elements:** Dashboard cards and map containers use an 8px radius (`rounded-lg`) to provide a subtle structural frame.
- **Indicators:** Circular pips are used exclusively for status lights (Live/Active/Offline).

## Components

- **Buttons:** Primary buttons are solid Royal Blue with white text. Secondary buttons use a Graphite ghost style (border only). Transitions must be instant (150ms) to feel "fast."
- **Data Chips:** Small, rectangular labels with light background tints. Used for vehicle IDs, route numbers, and delay times.
- **Inputs:** Clean, white boxes with 1px Graphite borders. Labels sit above the input in the `label-caps` typography style.
- **Cards:** The primary container for data. Cards have no shadow; they rely on 1px borders and a consistent 16px internal padding.
- **Status Indicators:** Small, glowing pips (using a 4px outer glow) to represent real-time connectivity or transit health.
- **Map Controls:** Floating, white, bordered icon buttons placed in the corners of the viewport to maximize the map's visible area.
- **Data Tables:** Zebra-striped with very faint grays, using `mono-data` font for numerical values to ensure decimal alignment.