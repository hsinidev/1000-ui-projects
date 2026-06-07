---
name: Hardcourt Analytics
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#46362e'
  surface-container-lowest: '#170b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362720'
  surface-container-highest: '#41312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#9ccaff'
  on-tertiary: '#003257'
  tertiary-container: '#059eff'
  on-tertiary-container: '#003357'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#d0e4ff'
  tertiary-fixed-dim: '#9ccaff'
  on-tertiary-fixed: '#001d35'
  on-tertiary-fixed-variant: '#00497b'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#41312a'
typography:
  h1-bold:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  h2-bold:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  stats-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  body-reg:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
  density-compact: 8px
  density-comfortable: 16px
---

## Brand & Style

The design system is engineered for professional basketball scouts, analysts, and high-stakes fans who demand immediate clarity from complex data. The brand personality is **aggressive, precise, and authoritative**, mirroring the high-intensity atmosphere of a professional basketball arena.

The visual style is a hybrid of **High-Contrast Bold** and **Modern Brutalism**. It prioritizes function and data density over decorative whitespace. The aesthetic uses sharp edges and a dark canvas to simulate a premium "war room" dashboard, where critical insights are highlighted by vibrant, glowing accents that draw the eye to statistical anomalies and key performance indicators.

## Colors

The palette is anchored in a high-contrast dark mode. The **Vibrant Orange (#FF6B00)** serves as the primary action color and brand identifier, used sparingly for critical CTAs and active states to maintain its impact. 

- **Backgrounds:** The primary interface uses Matte Black (#1A1A1A) for the base layer, with Deep Grey (#2D2D2D) used for elevated containers and card backgrounds to create subtle structural depth.
- **Accents:** A signature "Orange Glow" is used for data visualization highlights, providing a sense of illumination against the dark backgrounds.
- **Data Status:** High-saturation Teal and Red are used exclusively for performance indicators (e.g., shooting percentage vs. league average) to ensure instant legibility.

## Typography

This design system utilizes a three-font strategy to balance impact with data legibility. 

1.  **Headlines (Inter):** Leveraged in its boldest weights and condensed tracking for an "editorial" feel that commands attention. All major headings are set in uppercase.
2.  **Data Points (Space Grotesk):** Chosen for its geometric precision and technical feel. It is used for numerical values, player stats, and labels where clarity in small sizes is paramount.
3.  **Body Text (Lexend):** Used for analytical descriptions and notes. Its specific design for readability ensures that long-form scouting reports are easy to digest against the dark background.

## Layout & Spacing

The layout utilizes a **12-column fluid grid** with a 4px base unit. To maximize data density, the system favors compact margins and narrow gutters (16px). 

Rhythm is maintained through a "Modular Block" approach. Content is grouped into logical modules that snap to the grid. Information hierarchy is controlled through vertical stacking rather than generous whitespace; we use color-blocking and borders to separate data sets rather than padding.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layering and Bold Borders** rather than traditional soft shadows. 

- **Level 0 (Base):** #1A1A1A (The court floor).
- **Level 1 (Cards/Modules):** #2D2D2D with a 1px solid border of #3D3D3D.
- **Level 2 (Popovers/Modals):** #2D2D2D with a high-contrast 2px border of the Primary Orange.
- **Interactive Depth:** When an element is focused or hovered, it emits a subtle outer glow (0px 0px 12px) using the Primary Orange at 30% opacity, creating a "neon" effect that signifies activity.

## Shapes

The shape language is strictly **Sharp (0px radius)**. This reinforces the "hardcourt" aesthetic and professional technical nature of the tool. 

Every UI element—from buttons and input fields to card containers and progress bars—must have 90-degree corners. This creates a rigid, structural look that aligns with the grid-heavy layout and ensures no space is wasted in high-density data tables.

## Components

- **Buttons:** Primary buttons are solid #FF6B00 with black uppercase text. Secondary buttons use a 2px orange outline with no fill. Interaction states involve a white 1px inner border on click.
- **Data Grids:** Tables should use alternating row colors (Matte Black and Deep Grey) for horizontal scanning. Headers are uppercase `label-caps` typography with a bottom border of #FF6B00.
- **Stat Chips:** Used for player positions or status. Rectangular, dark grey background, with a small 4px vertical accent bar on the left side in the primary or status color.
- **Input Fields:** Bottom-border only or fully enclosed in 1px grey borders. Text is always indented by 12px for clarity.
- **Shot Charts & Visuals:** Data points in visualizations should use the primary orange with a 4px outer blur to create a "glowing" heatmap effect against the dark background. 
- **Progress Bars:** Flat, rectangular bars with no rounding. The background is a dark grey, and the fill is a solid orange or status-driven gradient.