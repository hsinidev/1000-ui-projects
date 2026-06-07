---
name: Hydro-Twin
colors:
  surface: '#101414'
  surface-dim: '#101414'
  surface-bright: '#353a3a'
  surface-container-lowest: '#0a0f0f'
  surface-container-low: '#181c1c'
  surface-container: '#1c2020'
  surface-container-high: '#262b2b'
  surface-container-highest: '#313635'
  on-surface: '#dfe3e2'
  on-surface-variant: '#bdc9c8'
  inverse-surface: '#dfe3e2'
  inverse-on-surface: '#2c3131'
  outline: '#879392'
  outline-variant: '#3e4949'
  surface-tint: '#76d6d5'
  primary: '#76d6d5'
  on-primary: '#003737'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#006a6a'
  secondary: '#bec8cd'
  on-secondary: '#293236'
  secondary-container: '#414a4f'
  on-secondary-container: '#b0babf'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#717373'
  on-tertiary-container: '#f9f9f9'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#dbe4e9'
  secondary-fixed-dim: '#bec8cd'
  on-secondary-fixed: '#141d21'
  on-secondary-fixed-variant: '#3f484c'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#101414'
  on-background: '#dfe3e2'
  surface-variant: '#313635'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: 0px
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  panel-gap: 2px
---

## Brand & Style

This design system embodies a **Nautical-Industrial** aesthetic, blending the precision of naval engineering with the high-stakes clarity of a bridge command center. The personality is authoritative, resilient, and technical. It is designed for engineers and captains who require immediate situational awareness in high-glare, high-contrast maritime environments.

The visual style leans into **Tactile Industrialism**. It utilizes robust borders, monospaced data readouts, and subtle metallic textures to mimic physical yacht instrumentation. Every pixel serves a functional purpose, eschewing decorative fluff for high-density information architecture that feels "bolted down" and permanent.

## Colors

The palette is optimized for visibility under direct sunlight and the dark of the bridge. 
- **Gunmetal (#2C3539):** Acts as the structural foundation, used for panels and deep UI surfaces.
- **Teal (#008080):** The primary brand color, representing fluid systems and mechanical status.
- **Crisp White (#FFFFFF):** Used exclusively for high-priority data and primary labels to ensure maximum legibility.
- **Accent Glow (#00FFFF):** A more vibrant cyan used for active states and "on" indicators, mimicking LED backlit physical toggles.

Surface colors should use a dark-mode base to reduce eye strain, with high-contrast borders separating functional zones.

## Typography

Typography focuses on "read-at-a-glance" performance. **Space Grotesk** provides a technical, geometric feel for headings and large status readouts. **JetBrains Mono** is utilized for all data points, coordinates, and body text to maintain the "monitored system" aesthetic and ensure numerical alignment in data tables.

All labels should lean toward uppercase with increased letter spacing to emulate etched industrial plates. Weight should be bold for primary data and medium/regular for secondary units.

## Layout & Spacing

This design system uses a **Fixed Grid** approach within modular panels. The layout resembles a physical bulkhead or console where every instrument has a dedicated slot. 

- **Grid:** A 12-column grid with narrow 16px gutters to maximize data density.
- **Micro-spacing:** Built on a 4px base unit.
- **Modular Panels:** Layouts are divided into "Instrument Clusters." Use a tight 2px gap between adjacent panels with heavy borders to create a "fitted" appearance.
- **Reflow:** On mobile, clusters stack vertically, prioritizing "Critical System Alerts" at the top of the viewport.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering and Insets** rather than ambient shadows. 
- **The "Case" Layer:** The darkest gunmetal base represents the physical hull.
- **The "Panel" Layer:** Slightly lighter gunmetal surfaces, outlined with a 1px solid Teal or Gunmetal border.
- **The "Recessed" Layer:** Data input fields and secondary monitors use an inset inner shadow to appear carved into the panel.
- **Active Glow:** Active buttons or critical alerts use an outer neon glow (`#00FFFF`) with 0 blur and 2px spread to simulate a lit lamp.

## Shapes

The shape language is strictly **Sharp (0px)**. All containers, buttons, and status indicators use 90-degree corners to reflect the rigid, no-nonsense nature of maritime hardware. 

Angled corners (45-degree chamfers) are permitted for decorative "plate" corners or high-level navigation tabs to provide a subtle "stealth-ship" geometric flair, but standard UI components must remain perfectly rectangular.

## Components

- **Buttons:** Solid Gunmetal background with a 2px Teal border. On hover/active, the border and text transition to the Glow color (#00FFFF).
- **Status Indicators:** "Physical" circular LEDs. Green (#00FFC2) for nominal, Red (#FF3B30) for alarm, and Teal for standby. Pulsing animations are used for active critical errors.
- **Cards/Panels:** Heavy 2px Teal borders on the top and left, with 1px Gunmetal borders on the bottom and right to create a "beveled" mechanical look.
- **Input Fields:** Recessed styling with a monospaced cursor. Labels sit in a "tab" cutout at the top-left of the border.
- **Gauges & Dials:** High-contrast linear or radial bars. Avoid skeuomorphic glass reflections; use flat, high-contrast segmented bars to show percentage levels.
- **Data Tables:** Zebra-striping is replaced by 1px horizontal dividers. Columns are strictly aligned using the monospaced grid.
- **Additional Components:** "Bulkhead Dividers" (heavy horizontal lines with technical serial numbers) and "Safety Toggles" (switches that require a "long-press" or "slide-to-confirm" to simulate physical safety covers).