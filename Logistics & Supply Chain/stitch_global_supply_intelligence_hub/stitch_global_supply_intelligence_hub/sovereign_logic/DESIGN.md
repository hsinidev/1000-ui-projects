---
name: Sovereign Logic
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#4c4451'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#7d7483'
  outline-variant: '#cec3d3'
  surface-tint: '#7b41b3'
  primary: '#2e0052'
  on-primary: '#ffffff'
  primary-container: '#4b0082'
  on-primary-container: '#ba7ef4'
  inverse-primary: '#ddb7ff'
  secondary: '#8333c6'
  on-secondary: '#ffffff'
  secondary-container: '#b96cfd'
  on-secondary-container: '#41006f'
  tertiary: '#301600'
  on-tertiary: '#ffffff'
  tertiary-container: '#4f2700'
  on-tertiary-container: '#c98c5c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0dbff'
  primary-fixed-dim: '#ddb7ff'
  on-primary-fixed: '#2c0050'
  on-primary-fixed-variant: '#622599'
  secondary-fixed: '#f1daff'
  secondary-fixed-dim: '#dfb7ff'
  on-secondary-fixed: '#2d004f'
  on-secondary-fixed-variant: '#690bac'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#fbb884'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#693c12'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  data-tabular:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.06em
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 32px
---

## Brand & Style

The design system is engineered for high-stakes global logistics, emphasizing precision, authority, and real-time intelligence. The personality is "Commanding Professionalism"—it provides a high-density environment where complex data is distilled into actionable insights without sacrificing detail.

The visual style is a hybrid of **Modern Corporate** and **Technical Minimalism**. It prioritizes information density through a rigid structural grid, sharp geometric edges, and a sophisticated monochromatic neutral base punctuated by Royal Purple. The aesthetic avoids decorative elements, opting instead for functional clarity and a sense of institutional stability.

## Colors

This design system utilizes a "Power Neutral" palette. **Royal Purple** serves as the primary anchor, used for high-level branding, active states, and primary calls to action. It conveys a sense of premium service and decisiveness.

The neutral scale is expansive, ranging from a crisp white background to a deep charcoal for text. Intermediate greys are used strictly for structural borders and secondary metadata. Semantic colors (Success, Warning, Critical) are desaturated to ensure they do not compete with the primary purple but remain distinct for immediate recognition in data-rich environments.

## Typography

The typography strategy employs **Manrope** for headlines to provide a modern, slightly geometric character that feels premium. For the core data and interface elements, **Inter** is used for its exceptional legibility at small sizes and its neutral, utilitarian tone.

High-density views should utilize the `data-tabular` and `label-caps` styles to maximize vertical space. All numerical data should be set with tabular lining figures to ensure vertical alignment in tables and dashboards.

## Layout & Spacing

The design system follows a **Fixed-Fluid Hybrid Grid**. Global navigation and sidebars are fixed, while the central data workspace spans a 12-column fluid grid. A strict 4px baseline rhythm is enforced to maintain alignment across dense components.

Margins and gutters are kept tight (16px) to maximize the "data-per-pixel" ratio. Large white space is reserved only for high-level dashboard overviews; operational views should prioritize compact information density.

## Elevation & Depth

To maintain a "sharp" and professional aesthetic, the design system avoids heavy drop shadows. Depth is primarily achieved through **Tonal Layering** and **Low-Contrast Outlines**.

- **Level 0 (Floor):** Background color (#F8F9FA).
- **Level 1 (Cards/Panels):** Pure white surface with a 1px solid border (#D1D5DB).
- **Level 2 (Hover/Active):** A subtle, highly diffused "Ambient Shadow" (0px 4px 12px rgba(0, 0, 0, 0.05)) to indicate interactivity without softening the edges.
- **Level 3 (Modals/Overlays):** A more defined 1px border with a slightly darker neutral tint.

Interactions should feel mechanical and immediate; transitions are short (150ms) and linear.

## Shapes

The design system utilizes **Sharp Edges (0px radius)** for all primary containers, data cards, and input fields. This reinforces the technical, precise nature of supply chain logistics. 

Subtle rounding (2px) is permitted only for internal micro-components like checkboxes or progress bar fills to prevent visual "vibration" in dense layouts, but the overarching container philosophy remains strictly orthogonal.

## Components

### Data Cards
Cards are the primary vessel for shipment details. They feature a 1px border, no corner radius, and a top-aligned "Status Accent" bar using Royal Purple or semantic colors. Content within cards is divided by hair-line separators (0.5px).

### Progress Bars
Progress bars are sleek and 4px in height. The track is a light grey (#E5E7EB), and the fill is Royal Purple. For multi-stage logistics, segmented progress bars with sharp vertical dividers are used to show distinct transit phases.

### Alert Badges
Badges are rectangular with 0px rounding. They use high-contrast text against desaturated background tints (e.g., light purple background with deep purple text). In high-density views, badges may be reduced to simple colored square icons.

### Interactive Inputs
Input fields use a 1px neutral border that shifts to a 2px Royal Purple border on focus. Labels are positioned above the field using the `label-caps` typography style to ensure the UI remains readable when multiple fields are stacked.

### Tactical Components
- **Data Grids:** High-density tables with zebra-striping and "sticky" header/column capabilities.
- **Status Monoliths:** Large-scale counters for global KPIs (e.g., "Active Shipments", "Port Delays") using the `display-lg` type style.