---
name: Synthetic Intelligence
colors:
  surface: '#111318'
  surface-dim: '#111318'
  surface-bright: '#37393e'
  surface-container-lowest: '#0c0e13'
  surface-container-low: '#191c20'
  surface-container: '#1e2025'
  surface-container-high: '#282a2f'
  surface-container-highest: '#33353a'
  on-surface: '#e2e2e9'
  on-surface-variant: '#c8c5ce'
  inverse-surface: '#e2e2e9'
  inverse-on-surface: '#2e3036'
  outline: '#928f98'
  outline-variant: '#47464d'
  surface-tint: '#c7c3e7'
  primary: '#c7c3e7'
  on-primary: '#2f2d4a'
  primary-container: '#0d0b26'
  on-primary-container: '#7b7899'
  inverse-primary: '#5d5b7a'
  secondary: '#c6c6cb'
  on-secondary: '#2e3034'
  secondary-container: '#47494d'
  on-secondary-container: '#b7b8bd'
  tertiary: '#e5bfa3'
  on-tertiary: '#422b17'
  tertiary-container: '#1b0a00'
  on-tertiary-container: '#94755c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c7c3e7'
  on-primary-fixed: '#1a1833'
  on-primary-fixed-variant: '#464461'
  secondary-fixed: '#e2e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1c1f'
  on-secondary-fixed-variant: '#45474b'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#e5bfa3'
  on-tertiary-fixed: '#2b1705'
  on-tertiary-fixed-variant: '#5b412c'
  background: '#111318'
  on-background: '#e2e2e9'
  surface-variant: '#33353a'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-metric:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Inter
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
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 32px
---

## Brand & Style
The brand personality is authoritative, precise, and high-performance. It is designed for technical power users who require rapid data synthesis without visual fatigue. The aesthetic sits at the intersection of **Corporate Modern** and **Glassmorphism**, leveraging a dark-mode-first approach to reduce eye strain in data-heavy environments. 

The visual style utilizes translucent layers to create a sense of depth, ensuring that despite the high information density, the interface remains breathable. Subtle neon accents provide clear "heat" and action cues, while the foundational indigo tones ground the experience in professional stability.

## Colors
The palette is dominated by **Deep Indigo** (#0D0B26) as the primary canvas, creating a sophisticated backdrop that allows metrics to pop. **Graphite** (#2B2D31) and **Neutral** (#1C1E23) are used for container backgrounds and secondary surface areas to establish a clear hierarchy.

**Neon Mint** (#3FFFB2) serves as the primary action color, reserved for buttons, active states, and critical path highlights. Growth indicators utilize a slightly more saturated version of the mint, while declines are signaled with a high-contrast red. All background surfaces should maintain a slight blue bias to remain cohesive with the indigo theme.

## Typography
This design system employs a dual-font strategy. **Space Grotesk** is used for headlines and large display metrics, providing a technical, geometric edge that reinforces the "analytical" nature of the tool. **Inter** is the workhorse font for all body text, UI labels, and dense data tables.

Crucially, all numerical data—especially within tables and dashboards—must utilize `tabular-nums` (monospaced figures). This ensures that columns of numbers align perfectly, allowing users to scan and compare values vertically with precision.

## Layout & Spacing
The layout follows a **Fluid Grid** model with a 12-column architecture. To accommodate high-density data, the base unit is a tight 4px grid. Standard margins are set to 32px to provide a professional frame, while internal gutters are kept at 16px to maximize information real estate.

Containers should utilize a consistent padding of 16px or 20px depending on complexity. In data-rich views, vertical spacing between rows should be minimized to 8px to reduce the need for excessive scrolling, while maintaining legibility through clear horizontal borders.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and tonal layering rather than traditional drop shadows. Cards and panels use a semi-transparent background (`rgba(28, 30, 35, 0.6)`) with a `backdrop-filter: blur(12px)`.

Hierarchy is reinforced by a 1px solid border in a low-opacity white (`rgba(255, 255, 255, 0.08)`), which gives the elements a "etched" look. Higher-level surfaces (like modals) should have a slightly lighter background and a subtle outer glow using a desaturated version of the primary indigo to simulate light emission rather than a dark shadow.

## Shapes
The shape language is disciplined and "Soft" (0.25rem). This small radius maintains a professional, engineering-focused look while avoiding the harshness of perfectly sharp corners. Buttons and data chips follow this 4px standard, while larger dashboard cards may scale up to a "rounded-lg" (0.5rem) to better define the primary layout containers.

## Components
- **Buttons:** Primary buttons use a solid Neon Mint background with dark indigo text. Secondary buttons are "Ghost" style with a 1px border and no fill, emphasizing the background blur.
- **Cards (Glass):** Standard containers for charts and tables. Must feature a top-aligned "header" section with 1px bottom border.
- **Data Chips:** Small, pill-shaped indicators for tags or status. Success states use Neon Mint text with a 10% opacity Mint background.
- **Input Fields:** Darkened Graphite backgrounds with a 1px border that glows Neon Mint on focus. Use Inter-Medium for placeholder text.
- **Growth Indicators:** Small upward/downward arrows adjacent to metrics. Use #00F59B for positive and #FF4D4D for negative.
- **Data Tables:** Zebra striping is avoided in favor of 1px horizontal dividers. Header rows use `label-sm` typography with a subtle background tint to differentiate from data rows.
- **Sparklines:** Compact, high-density line charts embedded within table rows or cards to show trend-lines without axes, using the Neon Mint accent.