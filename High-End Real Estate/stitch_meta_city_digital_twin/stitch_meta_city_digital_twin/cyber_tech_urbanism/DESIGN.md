---
name: Cyber-Tech Urbanism
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#fbf8f7'
  on-tertiary: '#313030'
  tertiary-container: '#dedbdb'
  on-tertiary-container: '#616060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
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
    fontWeight: '500'
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
    lineHeight: '1.6'
  technical-data:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

The design system targets urban planners and data architects who require high-density information environments. The brand personality is clinical, futuristic, and authoritative, evoking the sensation of a high-stakes command center. 

The visual style is a fusion of **Glassmorphism** and **High-Contrast Precision**. It utilizes a "HUD" (Heads-Up Display) philosophy where the interface feels like a digital overlay atop a physical city. Key characteristics include semi-transparent surfaces, ultra-thin glowing strokes, and animated "scanning" background patterns that suggest real-time data processing. The emotional response is one of total control and technical sophistication.

## Colors

The palette is anchored in deep blacks to maximize the "void" effect of a dark-mode interface. 

- **Matte Black (#0A0A0A):** Used for the primary canvas and deep background layers.
- **Neon Cyan (#00F3FF):** The primary action and signal color. It is used for interactive elements, data highlights, and glowing accents.
- **Graphite (#2D2D2D):** Used for component surfaces and secondary containers.
- **Slate Grey (#1A1A1A):** Used for subtle sectioning and background elevations.

Apply a 1px Cyan glow (`box-shadow: 0 0 8px rgba(0, 243, 255, 0.4)`) only to active or critical technical states.

## Typography

This design system uses a dual-font strategy to balance editorial clarity with technical rigor. 

- **Headings & UI Labels:** Use **Space Grotesk**. Its geometric construction complements the cyber-tech aesthetic. Headlines should be tight and impactful.
- **Body Text:** Use **Inter** for maximum readability in documentation and descriptions.
- **Data & Metrics:** Use the system monospaced font for all numerical data, coordinates, and code snippets to imply mathematical precision. All labels for data visualizations should be in `label-caps`.

## Layout & Spacing

The layout follows a **Fixed Grid** model within a 1440px container, utilizing a 12-column structure. Spacing is strictly mathematical, built on a 4px base unit to reinforce the sense of engineering.

Margins are generous (32px) to allow the "glowing" UI elements room to breathe against the dark background. A subtle 20px "scanning line" grid pattern should be overlaid on the background at 5% opacity to provide a visual anchor for the technical data.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Tonal Layering** rather than traditional shadows.

1.  **Level 0 (Background):** Matte Black (#0A0A0A) with a faint CSS linear-gradient grid.
2.  **Level 1 (Sub-panels):** Slate Grey (#1A1A1A) with 0% blur.
3.  **Level 2 (Active Cards/Modals):** Graphite (#2D2D2D) with a `backdrop-filter: blur(12px)` and a semi-transparent opacity (85%).
4.  **Level 3 (Interactive/Floating):** Use a 1px solid border of Neon Cyan (#00F3FF) at 30% opacity. 

Shadows are replaced by "outer glows" using the Cyan primary color for high-priority elements.

## Shapes

The design system utilizes **Sharp (0px)** corners for all primary containers, buttons, and input fields. This choice emphasizes the "hard-tech" nature of urban planning and data analysis. 

Small circular indicators may be used exclusively for status pips or data points on maps, but all structural UI elements must remain strictly rectangular. Use 45-degree chamfered corners for "Special" action buttons to evoke a military-grade hardware feel.

## Components

- **Buttons:** Primary buttons are Matte Black with a 1px Neon Cyan border and Cyan text. On hover, the button fills with Cyan and text flips to Black.
- **Input Fields:** Background is Slate Grey (#1A1A1A) with a bottom-only border of Graphite. On focus, the bottom border turns Neon Cyan with a faint vertical glow.
- **Cards:** No background fill; use a 1px Graphite border and a translucent Graphite header bar.
- **Data Visualizations:** Use Neon Cyan for primary trends. Use pure White for secondary lines. Background grid lines in visualizations must match the Slate Grey accent color.
- **Chips/Status:** Use monospaced font, all caps, enclosed in a thin Slate Grey box.
- **Scanning Bar:** A horizontal Neon Cyan line (1px) that slowly translates vertically across the viewport or specific data cards at low opacity.