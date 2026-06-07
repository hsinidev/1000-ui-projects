---
name: Industrial Maritime
colors:
  surface: '#111412'
  surface-dim: '#111412'
  surface-bright: '#373a37'
  surface-container-lowest: '#0c0f0d'
  surface-container-low: '#1a1c1a'
  surface-container: '#1e201e'
  surface-container-high: '#282b28'
  surface-container-highest: '#333533'
  on-surface: '#e2e3df'
  on-surface-variant: '#c4c6cc'
  inverse-surface: '#e2e3df'
  inverse-on-surface: '#2f312e'
  outline: '#8e9196'
  outline-variant: '#44474c'
  surface-tint: '#bac8dc'
  primary: '#bac8dc'
  on-primary: '#243141'
  primary-container: '#0d1b2a'
  on-primary-container: '#768497'
  inverse-primary: '#525f71'
  secondary: '#91d3c1'
  on-secondary: '#00382e'
  secondary-container: '#005143'
  on-secondary-container: '#80c2b0'
  tertiary: '#afc9ea'
  on-tertiary: '#17324d'
  tertiary-container: '#001b33'
  on-tertiary-container: '#6b85a4'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e4f9'
  primary-fixed-dim: '#bac8dc'
  on-primary-fixed: '#0f1c2c'
  on-primary-fixed-variant: '#3a4859'
  secondary-fixed: '#adf0dd'
  secondary-fixed-dim: '#91d3c1'
  on-secondary-fixed: '#00201a'
  on-secondary-fixed-variant: '#005143'
  tertiary-fixed: '#d1e4ff'
  tertiary-fixed-dim: '#afc9ea'
  on-tertiary-fixed: '#001d36'
  on-tertiary-fixed-variant: '#2f4865'
  background: '#111412'
  on-background: '#e2e3df'
  surface-variant: '#333533'
typography:
  display-xl:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
  data-mono:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is engineered for the high-stakes, high-density environment of maritime logistics. The brand personality is **unyielding, authoritative, and precise**. It evokes the physical presence of massive shipping containers, steel cranes, and deep-water hulls. 

The aesthetic leverages **Industrial Brutalism** refined by **Corporate Modernism**. It prioritizes structural integrity over decorative flair, using heavy stroke weights and rigid alignments to communicate stability. The goal is to provide operators with a "cockpit" experience that feels as grounded and reliable as the heavy machinery they manage. Every element is designed to feel "bolted down," minimizing cognitive load through extreme visual clarity and a strictly enforced hierarchy.

## Colors

The color palette is anchored in **Deep Navy (#0D1B2A)**, serving as the "ballast" of the UI. This dark mode default reduces eye strain during long shifts and provides a high-contrast foundation for data visualization. 

**Seafoam Green (#71B2A1)** is utilized as the primary action and "active state" color, providing a professional and legible contrast against the navy depths. **Graphite (#415A77)** acts as the structural color, used for borders, dividers, and secondary interface elements to define the "massive" architecture of the application. Neutral tones are kept crisp to ensure that high-density text remains legible across various hardware qualities found in port environments.

## Typography

This design system utilizes **Public Sans** for its institutional clarity and exceptional legibility in high-density layouts. As a typeface designed for government and public interfaces, it offers the neutral, "official" tone necessary for maritime operations.

- **Headlines:** Use heavy weights (700-800) to create a sense of massive scale and importance.
- **Data Display:** Manifest numbers, container IDs, and timestamps utilize a slightly tracked-out medium weight to ensure every character is distinct.
- **Labels:** Small-scale labels are set in Bold Uppercase to cut through complex data sets and act as structural signposts.
- **Scale:** Typographic contrast is intentionally high to ensure that critical alerts are immediately distinguishable from standard operational data.

## Layout & Spacing

The layout follows a **Rigid Fluid Grid** philosophy. While the containers stretch to accommodate the vast amount of data inherent in port logistics, the internal spacing is governed by a strict 4px/8px baseline rhythm to maintain an organized, industrial feel.

The 12-column grid uses substantial 16px gutters to prevent information bleed in high-density tables. Margins are kept wide (24px+) to frame the UI, providing a "contained" feel that mirrors the structured environment of a shipping terminal. Layouts should prioritize vertical stacking and clear horizontal divisions, avoiding overlapping elements to maintain the "grounded" aesthetic.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Stacking and Bold Borders** rather than shadows. This reinforces the "Massive & Grounded" feel, as shadows often imply lightness or "floating" elements—the opposite of the intended port aesthetic.

- **Base Layer:** Deep Navy (#0D1B2A).
- **Component Layer:** Graphite (#415A77) with a 2px solid border.
- **Active Layer:** Seafoam Green (#71B2A1) borders or fills for high-priority focus.
- **Borders:** All primary containers must feature a 2px or 3px solid border. This "heavy-duty" framing creates a sense of physical weight and separates complex data modules without the need for blurs or gradients.

## Shapes

The shape language is strictly **Sharp (0)**. Every UI element—from buttons to cards to dropdowns—features 90-degree corners. 

This rejection of roundedness emphasizes the industrial nature of the product, mimicking the sharp angles of containers, gantries, and dockyards. Sharp corners allow for more efficient use of screen real estate in high-density data views and contribute to the "unrefined but professional" industrial style requested.

## Components

### Buttons
Buttons are massive and rectangular. Primary buttons use a Seafoam Green fill with Deep Navy text (Bold). Secondary buttons are hollow with a 2px Graphite border. Hover states should not use "glows," but rather a solid color inversion to signal mechanical feedback.

### Cards & Modules
All modules are encased in 2px Graphite borders. Headers are separated from content by a solid 2px horizontal rule. This creates a "blueprinted" look that manages high-density data effectively.

### Data Tables
Tables are the core of this design system. They feature alternating row highlights (using a slightly lighter navy) and prominent 1px vertical dividers. Headers are Bold Uppercase with a distinct background color to act as an anchor for the eye.

### Input Fields
Inputs use a 2px Graphite border that thickens to 3px Seafoam Green on focus. Labels are always "bolted" to the top-left of the input field, never floating, to ensure the structure remains rigid.

### Status Chips
Status indicators (In-Transit, Docked, Delayed) are rectangular blocks. They do not use soft tints; they use high-saturation solid borders and bold text to ensure safety-critical information is never missed.

### Additional Components
- **Gantt Charts:** For vessel scheduling, using rigid blocks of color.
- **Telemetry Readouts:** High-visibility "odometer-style" displays for crane or gate throughput.
- **Map Overlays:** Simplified vector maps with high-contrast vessel markers.