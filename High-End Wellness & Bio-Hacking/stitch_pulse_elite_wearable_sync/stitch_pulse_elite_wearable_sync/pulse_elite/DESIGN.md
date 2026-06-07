---
name: Pulse-Elite
colors:
  surface: '#15121b'
  surface-dim: '#15121b'
  surface-bright: '#3b3742'
  surface-container-lowest: '#0f0d15'
  surface-container-low: '#1d1a23'
  surface-container: '#211e27'
  surface-container-high: '#2c2832'
  surface-container-highest: '#37333d'
  on-surface: '#e7e0ed'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#e7e0ed'
  inverse-on-surface: '#322f39'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#c8c5ca'
  on-secondary: '#303033'
  secondary-container: '#47464a'
  on-secondary-container: '#b6b4b8'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#909191'
  on-tertiary-container: '#282a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#e4e1e6'
  secondary-fixed-dim: '#c8c5ca'
  on-secondary-fixed: '#1b1b1e'
  on-secondary-fixed-variant: '#47464a'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#15121b'
  on-background: '#e7e0ed'
  surface-variant: '#37333d'
typography:
  display-xl:
    fontFamily: Geist
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  data-point:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.02em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
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
  container-padding: 16px
  gutter: 12px
  bento-gap: 8px
---

## Brand & Style

The brand persona is authoritative, precise, and high-performance. This design system is engineered for elite users who require immediate, actionable insights from complex wearable data. It balances the urgency of a "command center" with the elegance of a luxury product.

The aesthetic blends **Modern Corporate** structure with **High-Tech Minimalism**. It utilizes a dark-mode-first approach to reduce eye strain during frequent checks and to make data visualizations pop. The visual language is defined by dense information density, organized through modular layouts that suggest a sophisticated digital cockpit.

## Colors

The palette is anchored in **Graphite** to provide a deep, non-distracting canvas. **Royal Purple** serves as the primary tactical color, used sparingly for active states, critical data points, and interactive accents. **Crisp White** is reserved for high-contrast typography and primary surfaces to ensure maximum legibility against the dark background.

Functional color application:
- **Primary (Royal Purple):** Used for "Live" status, progress indicators, and interactive highlights.
- **Surface (Graphite):** Applied to Bento-box containers to separate data clusters.
- **Contrast (White):** Used for primary headings and essential data metrics.
- **Glow:** A soft purple luminescence is applied to active containers to signify real-time data streaming.

## Typography

The typography strategy prioritizes "Data Readability" above all else. **Geist** is used for its geometric precision and technical feel, providing the high-contrast clarity needed for mobile-first data consumption. For supplemental metadata and secondary technical readouts, a monospaced font is introduced to reinforce the command-center aesthetic.

Hierarchy is established through extreme weight contrast. Large, bold data points are paired with tiny, uppercase monospaced labels to create a professional, "instrument-panel" look.

## Layout & Spacing

The design system utilizes a **Fluid Bento-Box** layout model. On mobile, this manifests as a 4-column grid where modules can span 2x2, 4x2, or 4x4 configurations. The layout is intentionally dense, minimizing scrolling by grouping related metrics into tight, modular clusters.

A 4px base unit drives all spacing. The "Bento-gap" of 8px creates a distinct, tight separation between data cards, maximizing the available screen real estate without feeling cluttered.

## Elevation & Depth

Depth is conveyed through **Low-Contrast Outlines** and **Tonal Layering** rather than traditional shadows. 

1.  **Base Layer:** The deepest Graphite (#09090B) for the app canvas.
2.  **Surface Layer:** Slightly lighter Graphite (#18181B) for bento cards, defined by a 1px thin border (#27272A).
3.  **Active State:** Elements in a "Live" or "Selected" state receive a subtle 4px blur glow in Royal Purple.
4.  **Glassmorphism:** Overlays (modals/drawers) use a high-blur backdrop (20px) with 80% opacity to maintain context of the data dashboard beneath.

## Shapes

The shape language is "Soft-Technical." The 0.25rem (4px) base radius ensures that components feel modern and premium while maintaining the sharp, industrial precision of a data-heavy interface. Large containers (Bento cards) use the `rounded-lg` (8px) token to provide a subtle structural container feel that doesn't feel overly "bubbly" or consumer-grade.

## Components

-   **Bento Cards:** The core structural unit. Each card must have a 1px border and a monospaced label in the top-left corner.
-   **Data Badges:** Small, pill-shaped indicators for "Live," "Peak," or "Syncing" states, using the Royal Purple background with white text.
-   **Sparklines:** Simplified, stroke-only charts embedded within bento cards. Strokes should be 1.5px thick in Royal Purple or White.
-   **Primary Buttons:** Full-width or high-contrast White buttons with black text for immediate action. No gradients; use flat color for a high-end feel.
-   **Input Fields:** Minimalist under-line inputs or subtle dark-grey wells with no fill, focusing on the 1px border.
-   **Status Indicators:** Small circular pips that utilize the "glow" effect when active to draw the user's eye to changing data.