---
name: Sentinel-SOC
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#46352e'
  surface-container-lowest: '#170b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362620'
  surface-container-highest: '#42312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#969797'
  on-tertiary-container: '#2e3030'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#42312a'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.3'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.5'
  mono-label:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-point:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.02em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 12px
  container-padding: 24px
---

## Brand & Style
This design system is engineered for high-stakes environments where rapid information processing and decisive action are paramount. The aesthetic follows a **Command Center** philosophy: dark, high-contrast, and technically precise. It balances **Minimalism** with **Glassmorphism** to create a layered, multi-dimensional interface that feels like a futuristic tactical HUD.

The personality is authoritative, vigilant, and ultra-functional. It avoids all decorative fluff, favoring a "data-first" approach that minimizes cognitive load while highlighting anomalies through aggressive color accents. The emotional response is one of controlled urgency and absolute clarity.

## Colors
The palette is dominated by **Deep Charcoal (#1A1A1A)** to reduce eye strain during extended monitoring sessions. **Safety Orange (#FF6700)** serves as the primary tactical color, used exclusively for interactive elements and primary call-to-actions.

Criticality is color-coded using a strict hierarchy:
- **Critical (Red):** Immediate threat, requires instant intervention.
- **High (Orange):** Priority alert, primary accent color.
- **Medium (Yellow):** Warning state, investigate soon.
- **Low (Blue):** Informational/Routine, stable state.

All text is rendered in **White (#FFFFFF)** or high-opacity grays to ensure maximum legibility against the dark void of the background.

## Typography
The typography system uses **Space Grotesk** for headlines to inject a technical, futuristic edge, while **Inter** is used for all body text and data points to ensure peak readability. 

A heavy emphasis is placed on "mono-label" styles for metadata and system tags, often using uppercase transformation and slight letter spacing to mimic military-grade hardware labeling. Data density is prioritized; therefore, line heights are tighter than standard web applications to allow more information to be visible above the fold.

## Layout & Spacing
The layout utilizes a **12-column fluid grid** with narrow gutters (12px) to maximize the "Command Center" high-density feel. Information is organized into modular "Dashboard Tiles" that snap to the grid. 

Spacing follows a strict 4px base unit. Margins are kept tight to the edges of the screen to utilize every available pixel for monitoring data. Horizontal rows in data tables and lists are compressed to increase the volume of visible logs without requiring excessive scrolling.

## Elevation & Depth
Depth is achieved through **Tonal Layering** and **Glassmorphism**, rather than traditional soft shadows. 
- **Base Level:** Deep Charcoal (#1A1A1A).
- **Surface Level:** Slightly lighter charcoal (#242424) with a 1px solid border (#333333).
- **Overlay/Glass Level:** Semi-transparent panels (20-40% opacity) with a `backdrop-filter: blur(12px)`. These panels represent active monitors or floating modals.

Edges are kept sharp and aggressive. No soft ambient shadows are permitted; if a shadow is used for separation, it must be a high-contrast, tight glow using the primary accent color or a 100% black hard shadow to simulate depth.

## Shapes
This design system utilizes **Sharp Edges (0px)** for all primary UI components, including buttons, cards, and input fields. This reinforces the technical, brutalist nature of a SOC environment. The only exception is for circular status indicators (pings) or specific data visualization nodes where a circle conveys "status" more effectively than a square.

## Components

### Buttons & Critical Actions
- **Primary:** Solid Safety Orange (#FF6700) with Black text. 0px border radius.
- **Secondary:** Ghost style with a 1px Safety Orange border and White text.
- **Critical:** Pulse animation effect on solid Red backgrounds for high-priority alerts.

### High-Density Data Cards
Cards are the backbone of the system. Each card features a 2px vertical "Criticality Strip" on the left edge, color-coded based on the severity level (Red, Orange, Yellow, Blue). Card headers use the `mono-label` typography style.

### Inputs & Terminal Fields
Input fields are dark (#111111) with 1px borders (#333333). On focus, the border shifts to Safety Orange. The caret is a solid orange block, mimicking a terminal cursor.

### Status Chips
Small, rectangular tags with a background color reflecting the criticality level. Text inside chips is always high-contrast (Black on bright colors, White on dark colors).

### System Health Visualizers
Include sparklines (miniature charts) within cards to show 24-hour trends. These should use thin, 1px lines without fills to maintain the high-density technical aesthetic.