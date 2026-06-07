---
name: Apex-Track
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#acd600'
  primary: '#ffffff'
  on-primary: '#293500'
  primary-container: '#c5f400'
  on-primary-container: '#566c00'
  inverse-primary: '#516600'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#ffffff'
  on-tertiary: '#2f3131'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#636565'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c5f400'
  primary-fixed-dim: '#acd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-metrics:
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
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
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
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The brand personality is aggressive, precise, and uncompromising. It is engineered for elite athletes and coaches who demand immediate, actionable insights from dense biometric data. The visual language avoids decorative softness, instead favoring a technical aesthetic that mirrors high-end performance hardware and automotive telemetry.

This design system utilizes a **Technical Glassmorphism** style. It leverages deep "Carbon Black" layers, semi-transparent frosted surfaces, and ultra-sharp accents. The emotional response is one of intensity and focus, creating a "cockpit" experience where the interface recedes to let high-contrast data visualizations dominate.

## Colors

The palette is rooted in a high-contrast, dark-mode-first architecture. 

- **Primary (Neon Volt):** Reserved strictly for primary call-to-actions, active state indicators, and critical performance peaks.
- **Secondary (Carbon Black):** The foundation of the UI. Used for deep background layers to minimize eye strain during low-light training sessions.
- **Tertiary (Crisp White):** Used for primary headings and critical data points to ensure maximum legibility against dark backgrounds.
- **Neutral (Slate/Obsidian):** Various shades of dark grey are used for borders, secondary text, and inactive states to maintain hierarchy without clutter.
- **Accents:** "Optimal" blue and "Critical" red are used sparingly for biometric threshold alerts.

## Typography

This design system uses a dual-font strategy to balance technical aggression with data clarity. 

**Space Grotesk** is used for headlines, large metric displays, and labels. Its geometric, slightly futuristic construction reinforces the "High Performance" narrative. **Inter** is utilized for body copy and dense data tables due to its exceptional legibility and neutral, utilitarian tone. 

Key data points should utilize the "Data-Mono" style to ensure numerical alignment in rapidly updating streams. All labels should be set in uppercase with increased letter spacing to mimic technical schematics.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid Grid**. Content is housed within a 12-column grid system with a maximum width of 1440px for dashboard views. 

The spacing rhythm is strictly based on a 4px baseline unit. 
- **Tight (8px):** For grouping related data points or icons with text.
- **Standard (24px):** For spacing between elements within a glass card.
- **Structural (48px):** For major section breaks and vertical rhythm.

Layouts should prioritize high-density information. Sidebars and utility panels use fixed widths (280px), while the main performance stage fluidly adapts to the viewport.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional shadows. 

1.  **Base Layer:** Solid Carbon Black (#121212).
2.  **Surface Layer (Cards):** Background blur (20px) with a 10% opacity white fill. 
3.  **Borders:** Each card must have a 1px solid border. The top and left borders use a higher opacity (20%) while the bottom and right use lower (5%) to simulate a subtle top-down technical light source.
4.  **Active Elevation:** When a component is focused or active, it gains a subtle outer glow using the Neon Volt color (0px blur, 2px spread, low opacity) instead of a shadow.

## Shapes

To maintain the "aggressive" and "technical" aesthetic, this design system utilizes a **Sharp (0px)** roundedness philosophy. 

All buttons, cards, input fields, and containers feature hard 90-degree angles. This conveys precision and structural integrity. The only exceptions are circular elements used for specific status pips or athlete avatars to provide a clear visual distinction between "human" elements and "system" elements.

## Components

- **Buttons:** Primary buttons use a solid Neon Volt background with black text. Secondary buttons are transparent with a 1px white border. All buttons use the `label-caps` type style.
- **Cards:** Utilize the glassmorphism treatment. Headers within cards should be separated by a 1px horizontal line (10% white opacity).
- **Inputs:** Dark backgrounds (#181818) with 1px borders that turn Neon Volt on focus. Labels sit strictly above the input in uppercase.
- **Chips/Status Tags:** Small, rectangular blocks. High-performance states use the Neon Volt color; warning states use high-contrast red.
- **Data Visualizations:** Line charts should use 2px stroke widths with no smoothing (stepped or straight lines only) to emphasize raw data over "beautified" trends. 
- **Biometric Ticker:** A specialized component for real-time data that uses the `data-mono` font style and a vertical scrolling animation for updates.