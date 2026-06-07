---
name: Nautical Industrial Interface
colors:
  surface: '#111414'
  surface-dim: '#111414'
  surface-bright: '#373a3a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#191c1c'
  surface-container: '#1d2020'
  surface-container-high: '#272a2a'
  surface-container-highest: '#323535'
  on-surface: '#e1e3e2'
  on-surface-variant: '#bfc8c8'
  inverse-surface: '#e1e3e2'
  inverse-on-surface: '#2e3131'
  outline: '#899292'
  outline-variant: '#3f4849'
  surface-tint: '#96d1d3'
  primary: '#96d1d3'
  on-primary: '#003738'
  primary-container: '#004b4d'
  on-primary-container: '#7fbabc'
  inverse-primary: '#2a6769'
  secondary: '#c5c7c6'
  on-secondary: '#2e3131'
  secondary-container: '#444747'
  on-secondary-container: '#b3b5b5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#414343'
  on-tertiary-container: '#afafb0'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b1edef'
  primary-fixed-dim: '#96d1d3'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#084f51'
  secondary-fixed: '#e1e3e2'
  secondary-fixed-dim: '#c5c7c6'
  on-secondary-fixed: '#191c1c'
  on-secondary-fixed-variant: '#444747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#111414'
  on-background: '#e1e3e2'
  surface-variant: '#323535'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  title-sm:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 15px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.02em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
  panel-padding: 20px
---

## Brand & Style

This design system embodies the precision and durability of high-end maritime engineering. It is a synthesis of **Industrial Technical** and **Modern Luxury**, designed for high-stakes environments where clarity and reliability are paramount. The aesthetic is inspired by naval bridge consoles and precision chronometers.

The style leverages a **Dark Mode primary** foundation to reduce eye strain in low-light operational environments. It utilizes a **Glassmorphic-Industrial** hybrid approach: structural elements are grounded by solid, rugged surfaces, while interactive overlays and telemetry data float on semi-transparent glass layers. Crisp, hairline borders and a strict grid provide the "rugged" discipline required for complex vehicle telemetry.

## Colors

The palette is anchored by **Gunmetal (#111414)**, providing a deep, non-reflective base that mimics treated hull steel. **Deep Teal (#004b4d)** serves as the primary functional color, used for interactive elements, primary actions, and navigational cues, evoking a nautical technical feel.

**Crisp White** is reserved for high-priority data readouts and essential typography to ensure maximum legibility against the dark background. A secondary "Oxy-Teal" (#007a7d) is used for hover states and active telemetry paths. Borders should remain low-contrast except when highlighting active status, where the Deep Teal is applied with high saturation.

## Typography

The design system uses **Hanken Grotesk** exclusively to maintain a sharp, contemporary, and engineered appearance. The typeface’s geometry excels in technical readouts where numeral clarity is essential.

- **Headlines:** Use Bold weights with tight tracking for a powerful, commanding presence.
- **Data Labels:** Always use `label-caps` for administrative metadata to evoke industrial labeling plates.
- **Numeric Data:** Ensure high contrast for telemetry values, utilizing Medium weights to stand out from descriptive text.
- **Body:** Kept at a comfortable 15px to allow for high information density without sacrificing professional polish.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid Grid**. Administrative controls are housed in fixed-width sidebars (280px), while telemetry and mapping data occupy a fluid central 12-column grid.

A strict **4px baseline grid** governs all internal spacing. Gutters are kept narrow (16px) to emphasize the "tight-tolerance" feel of industrial machinery. Panels are grouped into logical clusters with 24px margins between major functional blocks. On ultra-wide displays, telemetry widgets expand to fill the width, maintaining a modular, "dashboard-bridge" configuration.

## Elevation & Depth

Depth is communicated through **Material Layering** and **Backdrop Filtering** rather than traditional shadows.

1.  **Floor (Level 0):** The Gunmetal base (#111414).
2.  **Panels (Level 1):** Solid Surface (#161b1b) with a 1px `border-subtle`. No shadow.
3.  **Overlays (Level 2):** `surface-glass` with a 12px backdrop-blur and a 1px `border-strong` top-and-left highlight to simulate a beveled glass edge.
4.  **Active Modals (Level 3):** Increased backdrop-blur (20px) with a subtle outer glow using the Primary Teal at 10% opacity to indicate focus.

Depth is "mechanical"—think of glass plates stacked over a metal dashboard.

## Shapes

The design system utilizes **Sharp (0px)** corners for all structural components, including panels, buttons, and input fields. This reinforces the rugged, industrial nature of the interface and maximizes screen real estate for complex data. 

Small exceptions are made for circular status indicators or toggle switches to differentiate "analogue" mechanical states from "digital" structural containers.

## Components

### Buttons & Controls
- **Primary Action:** Solid Deep Teal fill, white uppercase text, sharp corners. On hover, the fill brightens to Teal-Light.
- **Secondary Action:** Transparent fill with a 1px Deep Teal border.
- **Ghost Action:** No border, text-only with `label-caps` styling.

### Input Fields & Telemetry
- **Inputs:** Darker than the surface (#0d0f0f) with a bottom-only 1px border. The border glows Teal when focused.
- **Telemetry Readouts:** Housed in glassmorphic "pods." Numerical data is 20% larger than descriptive labels.

### Cards & Panels
- **Administrative Cards:** No rounded corners. 1px `border-subtle` on all sides. Header areas should have a subtle diagonal-stripe texture (CSS pattern) to signify an "industrial zone."

### Navigation
- **Sidebar:** Vertical orientation, using high-contrast icons. Active states use a vertical Teal "light bar" on the left edge of the menu item.

### Specialized Components
- **Status Indicators:** Small, square "LED" pips. Solid Green (Active), Pulsing Amber (Warning), Flashing Red (Critical).
- **Grid Dividers:** Hairline 1px strokes in `border-subtle`, used to separate dense data columns.