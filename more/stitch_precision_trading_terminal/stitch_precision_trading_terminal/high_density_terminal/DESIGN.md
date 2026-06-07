---
name: High-Density Terminal
colors:
  surface: '#101418'
  surface-dim: '#101418'
  surface-bright: '#363a3e'
  surface-container-lowest: '#0b0f13'
  surface-container-low: '#181c20'
  surface-container: '#1c2024'
  surface-container-high: '#262a2f'
  surface-container-highest: '#31353a'
  on-surface: '#e0e2e8'
  on-surface-variant: '#bbcac0'
  inverse-surface: '#e0e2e8'
  inverse-on-surface: '#2d3135'
  outline: '#85948b'
  outline-variant: '#3c4a42'
  surface-tint: '#44dfa3'
  primary: '#44dfa3'
  on-primary: '#003825'
  primary-container: '#00c087'
  on-primary-container: '#004730'
  inverse-primary: '#006c4a'
  secondary: '#ffb4aa'
  on-secondary: '#690003'
  secondary-container: '#c5020b'
  on-secondary-container: '#ffd2cc'
  tertiary: '#b6c4ff'
  on-tertiary: '#002780'
  tertiary-container: '#8ca4ff'
  on-tertiary-container: '#00329d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#67fcbe'
  primary-fixed-dim: '#44dfa3'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#005237'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4aa'
  on-secondary-fixed: '#410001'
  on-secondary-fixed-variant: '#930005'
  tertiary-fixed: '#dce1ff'
  tertiary-fixed-dim: '#b6c4ff'
  on-tertiary-fixed: '#001550'
  on-tertiary-fixed-variant: '#003ab3'
  background: '#101418'
  on-background: '#e0e2e8'
  surface-variant: '#31353a'
typography:
  ticker-lg:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  price-md:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 20px
  data-table:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 16px
  ui-label:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
  ui-body:
    fontFamily: Work Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  caption:
    fontFamily: Work Sans
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 14px
spacing:
  unit: 4px
  gutter: 1px
  margin-sm: 8px
  margin-md: 16px
  panel-padding: 12px
---

## Brand & Style
This design system is engineered for professional traders who require maximum information density and zero latency in visual processing. The personality is hyper-utilitarian, cold, and precise, evoking the feeling of a sophisticated mission-control center. 

The aesthetic blends **Minimalism** with **Modern Corporate** efficiency. Every pixel must serve a functional purpose; decorative elements are stripped away in favor of structural clarity. The UI prioritizes "at-a-glance" readability of volatile data, using a high-contrast dark environment to reduce eye strain during extended sessions.

## Colors
The palette is dominated by a deep charcoal base to provide a void-like canvas where data can pop. 

- **Primary (Bullish):** #00C087 is used exclusively for positive price action, buy signals, and growth metrics.
- **Secondary (Bearish):** #FF3B30 is reserved for negative price action, sell signals, and alerts.
- **Surface Colors:** Variations of charcoal are used to create structural containment without breaking the dark-mode immersion.
- **Borders:** Extremely subtle separators (#1E2329) define the grid without creating visual noise.

## Typography
The system employs a dual-font strategy to balance UI navigation with data integrity. 

**Work Sans** is used for all interface labels, buttons, and instructional text to provide a modern, approachable frame. 

**JetBrains Mono** (or a similar monospace font) is mandatory for all numerical values, price tickers, and timestamps. This ensures that as numbers fluctuate, characters remain vertically aligned, preventing "jitter" and allowing for instant column-based scanning of order books and trade histories.

## Layout & Spacing
The system utilizes a **Fluid Grid** model designed for multi-monitor setups. The layout is composed of "Panels" separated by 1px borders rather than wide gutters to maximize screen real estate.

- **Grid:** A 12-column logic is applied within individual panels, but the overall dashboard uses a tiling window manager approach.
- **Rhythm:** A tight 4px baseline grid ensures high density. 
- **Density:** Padding is kept to a minimum (8px to 12px) to allow as many data rows as possible to be visible above the fold.

## Elevation & Depth
In this design system, depth is communicated through **Tonal Layering** and **Glassmorphism** rather than traditional shadows.

1.  **Level 0 (Base):** #0A0E12 - Main dashboard background.
2.  **Level 1 (Panels):** #14191F - Standard trading widgets (Charts, Order Book).
3.  **Level 2 (Translucent Overlays):** Uses a backdrop-blur (12px to 20px) with a semi-transparent surface (rgba(20, 25, 31, 0.8)). This is reserved for floating docks, command palettes, and right-click context menus.
4.  **Level 3 (Modals):** Solid #1E2329 with a 1px border of #363C4E.

Shadows are avoided to maintain the "flat" professional terminal look, using 1px contrast borders to define edge priority.

## Shapes
The shape language is strictly geometric and sharp. 

- **Standard Elements:** Buttons, input fields, and panels use a 0px (Sharp) radius by default to reinforce the utilitarian feel.
- **Micro-Elements:** Small indicators or tags may use up to a 4px radius, but never beyond that. 
- **Active Indicators:** Selected states in the navigation or tabs are indicated by 2px thick lines (Primary color) rather than rounded pills.

## Components
- **Buttons:** Primary buttons are solid color blocks with sharp corners. Secondary buttons use a "ghost" style with a 1px border. Use monospace for button labels only if they contain data (e.g., "Buy at 24,000.00").
- **Order Book:** High-density rows with background "depth bars" (low opacity green/red) representing volume at specific price levels.
- **Data Inputs:** Darker than the surface (#0A0E12), using 1px borders that highlight in the Primary color on focus.
- **Translucent Docks:** Global navigation or utility bars that float over the workspace, utilizing `backdrop-filter: blur()` to maintain context of the charts underneath.
- **Status Chips:** Small, rectangular badges for "Open," "Filled," or "Cancelled" orders, using minimal padding and bold weight monospace text.
- **Sparklines:** Compact, monochromatic line charts for watchlists to show 24h trends without axis labels.