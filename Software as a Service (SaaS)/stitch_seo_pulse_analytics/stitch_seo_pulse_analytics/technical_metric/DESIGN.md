---
name: Technical Metric
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353536'
  on-surface: '#e4e2e3'
  on-surface-variant: '#baccb0'
  inverse-surface: '#e4e2e3'
  inverse-on-surface: '#303031'
  outline: '#85967c'
  outline-variant: '#3c4b35'
  surface-tint: '#2ae500'
  primary: '#efffe3'
  on-primary: '#053900'
  primary-container: '#39ff14'
  on-primary-container: '#107100'
  inverse-primary: '#106e00'
  secondary: '#c8c6c7'
  on-secondary: '#303031'
  secondary-container: '#49494a'
  on-secondary-container: '#bab8b9'
  tertiary: '#f9fafa'
  on-tertiary: '#2f3131'
  tertiary-container: '#dddddd'
  on-tertiary-container: '#606162'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#79ff5b'
  primary-fixed-dim: '#2ae500'
  on-primary-fixed: '#022100'
  on-primary-fixed-variant: '#095300'
  secondary-fixed: '#e5e2e3'
  secondary-fixed-dim: '#c8c6c7'
  on-secondary-fixed: '#1b1b1c'
  on-secondary-fixed-variant: '#474647'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131314'
  on-background: '#e4e2e3'
  surface-variant: '#353536'
typography:
  display-metrics:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  table-data:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max: 1440px
---

## Brand & Style
This design system is engineered for the high-intensity SEO professional, prioritizing data density and immediate legibility over decorative flourishes. The brand personality is clinical, precise, and authoritative, evoking the feeling of a high-performance terminal or an industrial monitoring station. 

The aesthetic blends **Modern Minimalism** with **Technical Brutalism**. It utilizes a strict dark-mode environment to reduce eye strain during prolonged data analysis. Visual interest is derived from functional elements—charts, gauges, and status indicators—rather than imagery. The UI should feel like a precision tool, where every pixel serves a diagnostic purpose, providing users with a sense of total control over complex search engine datasets.

## Colors
The palette is rooted in a "Terminal Dark" philosophy. The primary background uses Deep Graphite (#1A1A1B) to provide a low-glare canvas. Neon Green (#39FF14) is reserved exclusively for primary actions, positive growth metrics, and "healthy" status indicators, creating a high-contrast focal point against the dark base.

Crisp White (#FFFFFF) is used for primary data points and headers to ensure maximum readability. Secondary UI elements, such as component backgrounds and borders, utilize a tiered series of dark grays to create subtle depth without breaking the technical aesthetic. Functional accent colors (Yellow and Red) are used sparingly for warnings and critical rank drops.

## Typography
The typographic system utilizes a dual-font approach to distinguish between operational UI and raw data. **Inter** handles all interface labels, instructions, and navigational elements, providing a neutral and highly legible sans-serif foundation.

**Space Grotesk** is used for all metrics, data tables, and headers. Its semi-monospaced appearance reinforces the technical nature of the platform and ensures that numerical values align vertically in tables, aiding in quick scanning. Headlines should be tight and punchy, while labels use all-caps with increased letter spacing to differentiate them from interactive data points.

## Layout & Spacing
This design system employs a **Fluid Grid** model with a high-density 4px baseline shift. The layout is designed to maximize information "above the fold." Desktop views utilize a 12-column grid with narrow 16px gutters to pack widgets and tables efficiently.

On mobile devices, the layout transitions to a single-column flow with horizontal-scroll containers for data tables, ensuring that columns do not become unreadably narrow. Charts and health gauges are prioritized at the top of the mobile view to provide an immediate "Daily Rank" snapshot. Content containers should use "tight" padding (12px to 16px) to maintain the technical, data-rich feel.

## Elevation & Depth
Depth is communicated through **Tonal Layering** and **Low-Contrast Outlines** rather than traditional shadows. This maintains a flat, digital-first aesthetic. 

The base layer is the deepest graphite (#1A1A1B). Surface containers (cards, table headers, sidebars) use a slightly lighter neutral (#2D2D2E). Active states or "hover" effects are indicated by a 1px solid border in Neon Green or a subtle increase in surface brightness. For complex overlays or modals, a 20% opacity Neon Green outer glow may be used to indicate focus, but ambient shadows should be avoided to keep the UI feeling "sharp" and "engineered."

## Shapes
The shape language is strictly **Sharp (0px)**. This design system eschews rounded corners to emphasize a professional, industrial, and "un-softened" tool aesthetic. Right angles are used for all buttons, input fields, cards, and chart containers. This rigidity reinforces the grid-based structure and allows for seamless tiling of data widgets in complex dashboard views.

## Components
- **Buttons:** Primary buttons are solid Neon Green with black text, strictly rectangular. Secondary buttons use a 1px White border with transparent backgrounds.
- **Data Tables:** High-density rows (32px height) with 1px border-bottom separators. Headers are sticky and use the `label-caps` typography style.
- **Sparklines:** Compact, monochromatic line charts without axes, integrated directly into table rows to show 7-day trends.
- **Health Score Gauges:** Semi-circular or circular strokes. The stroke color is dynamic (Green/Yellow/Red) based on the value, with the metric displayed in the center using `display-metrics` font.
- **Input Fields:** Bottom-border only or full-outline with no radius. Focus state is a 2px Neon Green border.
- **Chips/Badges:** Small, rectangular tags used for keyword categories or "Change" percentages (e.g., +2.4%). 
- **Interactive Rank Visuals:** Large-scale line charts with a crosshair cursor that displays vertical "hover-lines" to highlight specific data points across multiple metrics simultaneously.