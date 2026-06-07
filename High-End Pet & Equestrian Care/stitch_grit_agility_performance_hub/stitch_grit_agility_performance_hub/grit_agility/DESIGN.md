---
name: Grit-Agility
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
  on-surface-variant: '#e9bcb5'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#b08781'
  outline-variant: '#5f3f3a'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690000'
  primary-container: '#e60000'
  on-primary-container: '#fff7f5'
  inverse-primary: '#c00000'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#737272'
  on-tertiary-container: '#fbf8f7'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-lg:
    fontFamily: Lexend
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Lexend
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Lexend
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 20px
---

## Brand & Style

This design system is engineered for the high-intensity world of professional canine athletics. The brand personality is aggressive, precise, and uncompromising, mirroring the split-second decision-making required in agility trials. It targets elite trainers and competitive handlers who demand performance-grade tools.

The visual style is **High-Contrast / Bold** with a heavy influence from automotive racing and technical sportswear. It utilizes raw, dark surfaces contrasted against vibrant "Racing Red" to create a sense of urgency and forward momentum. Every interface element is designed to feel "fast," utilizing sharp angles and mechanical textures to evoke the grit of the training field and the precision of the podium.

## Colors

The palette is strictly limited to maximize visual impact and maintain a "motorsports" aesthetic. 

- **Racing Red (#E60000):** Used exclusively for primary actions, critical alerts, and kinetic accents. It represents the energy and "grit" of the canine athlete.
- **Carbon Black (#1A1A1A):** The foundation of the dark mode interface. It provides a deep, non-distracting backdrop that makes white text and red accents pop.
- **Pure White (#FFFFFF):** Reserved for high-priority typography and essential iconography to ensure maximum readability during high-motion activities.
- **Neutral Charcoal (#2D2D2D):** Used for secondary containers, input fields, and UI borders to create subtle depth without breaking the high-contrast theme.

## Typography

This design system utilizes **Lexend** for its athletic readability and geometric precision. To convey speed and kinetic energy, all headlines and functional labels are set in **Bold Italic**. This creates a consistent "forward-leaning" visual rhythm throughout the application. 

Body text remains upright for sustained legibility, while labels and callouts utilize uppercase styling to mimic technical equipment markings. Tight line heights on headlines emphasize the compact, muscular nature of the brand.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for mobile-first professional use. A strict 4px baseline grid ensures mathematical precision in element alignment. 

Margins and gutters are kept tight (16px–20px) to maximize screen real estate for performance data and video analysis. Content containers should utilize dynamic padding that scales, ensuring the UI feels "packed" and energetic rather than sparse. Use horizontal scrolling "strips" for quick access to dog profiles or heat maps, maintaining a focused vertical flow for primary training metrics.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and texture rather than traditional shadows. This design system avoids soft ambient shadows to maintain its sharp, technical edge.

- **Base Layer:** Solid Carbon Black (#1A1A1A).
- **Surface Layer:** Neutral Charcoal (#2D2D2D) with a subtle 5% opacity "carbon fiber" diagonal pattern overlay.
- **Accents:** Racing Red surfaces should appear "lit" from within using a subtle inner glow rather than a drop shadow.
- **Interactive Elements:** Use thin, 1px borders in high-contrast white or red to define boundaries, creating a "schematic" or "blueprinted" look.

## Shapes

The shape language is strictly **Sharp (0px)**. There are no rounded corners in this design system. Every button, card, and input field features 90-degree angles to evoke a sense of structural integrity, precision, and industrial strength. To add visual interest, use "clipped" corners (45-degree chamfers) on primary action buttons and headers to reinforce the aggressive, aerodynamic aesthetic.

## Components

- **Buttons:** Primary buttons are solid Racing Red with white, bold-italic uppercase text. They feature a 45-degree chamfer on the top-right and bottom-left corners.
- **Chips/Badges:** Small, rectangular blocks with a Carbon Black background and a 1px Racing Red border. Text is set in `label-bold`.
- **Input Fields:** Dark Charcoal backgrounds with a bottom-only 2px border that turns Racing Red when focused. No rounded corners.
- **Cards:** Use a Neutral Charcoal background with a subtle carbon fiber texture. No border, but a 4px Racing Red vertical "stripe" on the left edge to indicate active or high-priority status.
- **Progress Bars:** High-contrast White "track" with a Racing Red "fill." Fill should feature diagonal "hazard" stripes to imply movement.
- **Toggle/Switch:** Rectangular and mechanical. The "on" state is Racing Red; the "off" state is a dark grey. No soft sliding animations; use immediate, "snappy" transitions.
- **Data Visualization:** Line charts should use "neon" red paths with sharp nodes, avoiding any smoothing or curves.