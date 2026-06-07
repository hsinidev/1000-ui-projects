---
name: Curate-Sync
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#16191a'
  on-tertiary-container: '#808283'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 60px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
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
  xl: 48px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system centers on a "Curated Vault" philosophy, merging the analytical rigor of high-end fintech with the spatial elegance of a modern art gallery. The brand personality is institutional yet accessible, projecting an aura of exclusivity and high-trust stability. 

The visual style utilizes a high-contrast **Minimalism** framework layered with **Glassmorphism** to signify depth and transparency. Surfaces should feel like polished obsidian or frosted glass, allowing data to sit "on top" of the canvas. Every element is designed to hero the artwork while providing the investor with dense, legible market analytics. The emotional response is one of calm confidence—where wealth management meets cultural appreciation.

## Colors

The palette is anchored by **Deep Navy (#0A192F)**, which serves as the primary canvas color. This depth provides a receding background that makes art assets and data visualizations pop. **Silver (#C0C0C0)** is used as a structural accent for borders, dividers, and secondary actions, mimicking the architectural metalwork found in galleries.

**Silk White (#F8F9FA)** is reserved for primary typography and "Key Cards" where maximum focus is required. For data visualizations, high-chroma greens and reds are used sparingly to indicate market performance, ensuring they stand out against the muted navy and silver environment. Gradient applications should be subtle, using a "Linear Top-Down" approach to simulate gentle gallery lighting.

## Typography

The typographic scale creates a tension between editorial luxury and technical precision. **Playfair Display** is used for high-level headings and asset titles, evoking the feel of a printed exhibition catalog. It should always be set with tighter letter-spacing in larger sizes to maintain a premium look.

**Inter** handles all functional UI and data-heavy components. For financial figures and percentage changes, use the "data-mono" style to ensure tabular alignment and clarity. Maintain a strict hierarchy where Serif is for "The Art" and Sans-Serif is for "The Investment."

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop experiences to mirror the structured layout of an art installation. A 12-column grid is standard, with generous 24px gutters to provide "breathing room" between dense data modules. 

Spacing follows a base-4 scale. Large vertical margins (XL) should be used between major sections to emphasize exclusivity and prevent the interface from feeling cluttered. Alignment should be mathematically precise, with text elements often left-aligned to a strong vertical axis to reinforce the "technical" nature of the platform.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Tonal Layers** rather than heavy shadows. 

1.  **Base Layer:** The Deep Navy background.
2.  **Mid Layer:** Semi-transparent Silver glass (Backdrop-filter: blur(12px), opacity 10%) for secondary containers and navigation bars.
3.  **Top Layer:** Silk White cards for primary calls-to-action or featured assets, creating a dramatic focal point.

Instead of traditional drop shadows, use **inner glows** or **1px silver strokes** to define the edges of surfaces. This gives the UI a "lit from within" quality, similar to illuminated display cases.

## Shapes

The shape language is disciplined and architectural. **Soft (0.25rem)** roundedness is used for buttons and standard input fields to provide a touch of modern approachability without losing professional edge. 

Large asset cards may use **Rounded-LG (0.5rem)** to subtly frame the artwork. Interactive elements should never be pill-shaped or fully round, as sharp/soft corners better communicate the "precision" of investment data.

## Components

**Buttons:**
Primary buttons are solid Silk White with Deep Navy text. Secondary buttons are "Ghost" style, featuring a 1px Silver border and Silver text. Hover states should involve a subtle glow effect rather than a color shift.

**Cards:**
Art asset cards use a glassmorphic footer for the title and price, overlaid on the bottom 20% of the image. The glass effect must have a high blur radius to ensure text legibility over diverse art styles.

**Data Visualizations:**
Charts should be high-contrast. Line charts use a 2px Silver stroke with a subtle Navy-to-Transparent gradient fill beneath the line. Points of interest on graphs should use the Silk White to pop against the dark background.

**Inputs:**
Fields are defined by a bottom-border only (1px Silver) to maintain a minimalist look. When focused, the border transitions to Silk White with a subtle 2px vertical "caret" marker on the left.

**Additional Components:**
- **The "Vault" Indicator:** A specialized badge for verified assets, using a metallic silver gradient.
- **Price Ticker:** A refined, monospaced scrolling bar for real-time art market indices.