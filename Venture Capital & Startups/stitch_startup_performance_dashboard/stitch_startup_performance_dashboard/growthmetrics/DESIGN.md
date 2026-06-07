---
name: GrowthMetrics
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c4df'
  on-secondary: '#2f2e43'
  secondary-container: '#47475d'
  on-secondary-container: '#b8b6d0'
  tertiary: '#faf6f6'
  on-tertiary: '#313030'
  tertiary-container: '#dddad9'
  on-tertiary-container: '#605f5f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e0fc'
  secondary-fixed-dim: '#c6c4df'
  on-secondary-fixed: '#1a1a2e'
  on-secondary-fixed-variant: '#45455b'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  metric-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
  label-xs:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
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
  container-margin: 32px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
This design system is engineered for high-stakes financial environments where technical precision and rapid data processing are paramount. The brand personality is clinical, futuristic, and authoritative, designed to evoke a sense of absolute control over complex startup metrics. 

The aesthetic leverages **Glassmorphism** and **High-Contrast** modernism. By layering semi-transparent surfaces over a deep, matte foundation, the system creates a sense of depth that mimics a high-performance heads-up display (HUD). Visual priority is strictly managed through luminous accents, ensuring that critical "burn-rate" and "runway" data points command immediate attention against the dark, immersive backdrop.

## Colors
The palette is rooted in a "void" aesthetic to minimize eye strain during deep work.
- **Base Layer:** The absolute background uses Matte Black (#0D0D0D), providing a canvas for high-contrast light effects.
- **Surface Layer:** Deep Indigo (#1A1A2E) is utilized for interactive containers and cards, providing a subtle distinction from the base.
- **Action & Glow:** Neon Cyan (#00F2FF) is the primary interactive color. It is used sparingly for buttons, active states, and "glowing" data trends to simulate a digital light source.
- **Semantic Accents:** High-vibrancy reds and ambers are reserved for runway alerts and negative growth trends, utilizing outer glows to signal urgency.

## Typography
The typographic strategy balances technical character with utilitarian readability. **Space Grotesk** is used for headlines to provide a modern, geometric edge that aligns with the startup tech aesthetic. **Inter** is the workhorse for all data-heavy contexts. 

For all numerical displays (KPIs, Burn Rates, Dollar amounts), the system enforces `tabular-nums` (tnum) to ensure columns of figures align perfectly in tables. Labels utilize a bold, uppercase style with increased letter spacing to serve as clear anchors for dense information layouts.

## Layout & Spacing
This design system utilizes a **12-column fluid grid** designed for 1440px+ dashboards, scaling down to a compact single column for mobile. The spacing rhythm is based on a tight 4px baseline grid to support high-density information architecture.

- **Data Density:** Gutters are kept at a lean 16px to maximize horizontal space for complex tables.
- **Grouping:** Related metrics are grouped into clusters with 8px internal padding, while major sections are separated by 32px of vertical space to prevent cognitive overload.

## Elevation & Depth
Depth is conveyed through **Glassmorphism** and light-based layering rather than traditional drop shadows.
- **The Glass Effect:** Cards use a 60% opaque Deep Indigo fill with a `backdrop-filter: blur(12px)`. 
- **Border Illumination:** Surfaces are defined by 1px solid borders. On the top and left edges, the border uses a higher opacity to simulate a light source coming from the top-left.
- **Glow states:** Elevated or urgent components (like Runway Alerts) utilize a `box-shadow` that mimics a neon glow using the Primary or Critical color, with a blur radius of 15-20px at low opacity (20-30%).

## Shapes
The shape language is "Soft" yet disciplined. A baseline radius of 4px (`rounded-sm`) is applied to inputs and small buttons to maintain a technical feel. Larger containers and metric cards use an 8px (`rounded-lg`) radius. This subtle rounding prevents the UI from feeling aggressive while maintaining the precision required for a financial tool. Interactive elements do not use pill shapes; they remain rectangular to maximize click-area efficiency in dense layouts.

## Components
- **Metric Cards:** Feature a large-format KPI, a percentage change indicator, and an integrated sparkline. The sparkline uses a gradient stroke that glows in the color of the trend (Cyan for positive, Red for negative).
- **Runway Alert Widget:** A high-priority card with a pulsed "Critical Red" border-glow effect and a high-contrast countdown timer.
- **Data Tables:** High-density rows with `1px` Indigo dividers. Hover states trigger a subtle Cyan left-border highlight (2px width).
- **Buttons:** Primary buttons are solid Cyan with black text. Secondary buttons are "Ghost" style with Cyan borders and glowing text on hover.
- **Inputs:** Darker than the surface layer with a fixed-width monospaced font for numerical entry. Focus states trigger a 1px Cyan glow.
- **Status Indicators:** Small, circular "LED" style icons that use inner shadows to appear as if they are physical lights embedded in the interface.