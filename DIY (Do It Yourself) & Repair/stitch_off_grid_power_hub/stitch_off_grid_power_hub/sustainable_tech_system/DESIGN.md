---
name: Sustainable Tech System
colors:
  surface: '#fff9ef'
  surface-dim: '#e1d9c7'
  surface-bright: '#fff9ef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf3e0'
  surface-container: '#f6edda'
  surface-container-high: '#f0e7d5'
  surface-container-highest: '#eae2cf'
  on-surface: '#1f1b10'
  on-surface-variant: '#4d4732'
  inverse-surface: '#343024'
  inverse-on-surface: '#f9f0dd'
  outline: '#7e775f'
  outline-variant: '#d0c6ab'
  surface-tint: '#705d00'
  primary: '#705d00'
  on-primary: '#ffffff'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#e9c400'
  secondary: '#0c6780'
  on-secondary: '#ffffff'
  secondary-container: '#9ae1ff'
  on-secondary-container: '#09657f'
  tertiary: '#00696f'
  on-tertiary: '#ffffff'
  tertiary-container: '#00f1ff'
  on-tertiary-container: '#006a70'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#baeaff'
  secondary-fixed-dim: '#89d0ed'
  on-secondary-fixed: '#001f29'
  on-secondary-fixed-variant: '#004d62'
  tertiary-fixed: '#79f5ff'
  tertiary-fixed-dim: '#00dbe8'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#fff9ef'
  on-background: '#1f1b10'
  surface-variant: '#eae2cf'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for the intersection of ecological responsibility and high-performance technology. The brand personality is **Technical Optimism**: it balances the cold precision of data-heavy engineering with the warmth of renewable energy sources. 

The aesthetic draws from **Technical Minimalism**, prioritizing clarity, structured information density, and a high-contrast environment. It avoids decorative clutter in favor of functional aesthetics, using color only to denote importance or specific data categories. The target audience—ranging from energy analysts to sustainable-asset investors—requires a UI that feels reliable, institutional, and forward-thinking.

## Colors

The palette is anchored by a high-contrast foundation of pure whites and architectural light greys. 

- **Sun-Yellow (#FFD700)**: Reserved strictly for primary actions, success states related to solar yields, and high-priority alerts. It serves as a beacon of energy within the interface.
- **Sky-Blue (#87CEEB)**: Utilized for technical accents, secondary buttons, and as the primary hue for data visualization (wind energy, water metrics, or neutral data points).
- **Greyscale**: A range of cool-toned greys provides the structural "container" for the data, ensuring that the primary and secondary colors remain impactful and functional.

## Typography

The typography system relies on a pairing of geometric innovation and utilitarian clarity. 

**Space Grotesk** is used for headlines and data callouts. Its technical, slightly futuristic letterforms reinforce the "tech" aspect of the brand. **Inter** is used for all body copy and interface labels to ensure maximum legibility at small sizes within complex dashboards. 

For data-heavy interfaces, use the `data-mono` style for numerical values to ensure they remain aligned and readable in tables or real-time monitoring feeds.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model on desktop (12 columns, 1280px max-container) and a fluid 4-column model on mobile. The spacing rhythm is strictly based on an 8px base unit.

Layouts should favor vertical stacks with generous whitespace between logical sections to prevent "data fatigue." In data-heavy views, use the `sm` (12px) spacing for internal card padding to maintain density, while using `lg` (48px) for section margins to create visual breathing room.

## Elevation & Depth

To maintain the "clean" and "organized" feel, the system avoids heavy, blurred shadows. Instead, it uses **Low-contrast Outlines** and **Tonal Layers**.

- **Level 0 (Floor):** Background Alt (#F4F7F6).
- **Level 1 (Cards/Surface):** Pure White (#FFFFFF) with a 1px solid border (#E2E8F0).
- **Level 2 (Hover/Active):** Pure White with a subtle, tight shadow (0px 2px 4px rgba(0,0,0,0.05)) and a Sky-Blue accent border.

Depth is communicated through the stacking of surfaces rather than light sources. Semi-transparent overlays (Sky-Blue at 5% opacity) can be used to highlight active states in lists or navigation.

## Shapes

The shape language is **Soft** (Level 1). Elements use a 0.25rem (4px) corner radius to retain a sense of precision and engineered structure. 

Large containers and cards should never exceed 0.5rem (8px) roundedness. This "tight" cornering suggests a professional, industrial-grade software environment while remaining modern and accessible. Buttons follow the same logic; do not use pill-shaped buttons as they conflict with the technical nature of the platform.

## Components

- **Buttons:** Primary buttons use Sun-Yellow with black text (#1A1C1E) for maximum contrast. Secondary buttons use a Sky-Blue outline with Sky-Blue text. Tertiary buttons are text-only with Sky-Blue labels.
- **Data Cards:** Must feature a 2px top-border in Sky-Blue to denote "technical info" or Sun-Yellow for "active generation/yield."
- **Input Fields:** Use a white background with a 1px Grey border. On focus, the border shifts to Sky-Blue with a 2px inner glow.
- **Chips/Status:** Status chips use Sky-Blue for "Stable" or "Processing" and Sun-Yellow for "Active" or "Peak."
- **Data Visualizations:** Use Sky-Blue as the primary stroke/fill color. For comparative data, use varying shades of Sky-Blue (tints) and Grey. Sun-Yellow should be used only for the most important data point on a graph (e.g., current day vs. historical).
- **Progress Bars:** Thin 4px tracks in light grey with Sky-Blue progress fills.