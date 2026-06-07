---
name: Terra-Registry
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#43474c'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#74777d'
  outline-variant: '#c4c6cd'
  surface-tint: '#4e6073'
  primary: '#162839'
  on-primary: '#ffffff'
  primary-container: '#2c3e50'
  on-primary-container: '#96a9be'
  inverse-primary: '#b5c8df'
  secondary: '#7c5730'
  on-secondary: '#ffffff'
  secondary-container: '#fdcb9b'
  on-secondary-container: '#79542d'
  tertiary: '#252728'
  on-tertiary: '#ffffff'
  tertiary-container: '#3b3d3d'
  on-tertiary-container: '#a7a7a8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e4fb'
  primary-fixed-dim: '#b5c8df'
  on-primary-fixed: '#091d2e'
  on-primary-fixed-variant: '#36485b'
  secondary-fixed: '#ffdcbd'
  secondary-fixed-dim: '#eebd8e'
  on-secondary-fixed: '#2c1600'
  on-secondary-fixed-variant: '#61401b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style

This design system is built upon the principles of architectural permanence and legal authority. It targets high-net-worth investors and institutional entities seeking the security of physical assets with the efficiency of digital tokenization. The aesthetic is "Structural Minimalism"—a style that prioritizes the engineering-grade precision of a blueprint with the refined materiality of a luxury estate office.

The UI must evoke a sense of "digital limestone": heavy, stable, and immutable. We avoid ephemeral trends in favor of a legacy-driven visual language that balances dense financial data with expansive, airy layouts. The emotional response should be one of absolute trust, quiet confidence, and institutional rigor.

## Colors

The palette is derived from raw architectural materials: slate, clay, and stone. 

- **Deep Slate (#2C3E50):** Used for primary typography and structural headers to convey authority and the weight of legal titles.
- **Earthy Clay Brown (#A67C52):** Reserved for primary actions, success states related to land acquisition, and subtle accents that bridge the digital/physical gap.
- **Architectural White (#F9F9F9):** The primary canvas color, providing a crisp, clean background that allows data to breathe.
- **Support Tones:** We utilize a muted neutral slate for secondary data and a refined gold-tinted clay for "verified" or "premium" statuses.

## Typography

This design system employs a sophisticated typographic hierarchy that mirrors a legal deed or a high-end architectural portfolio.

- **Headings:** We use **Libre Caslon Text**. Its historical roots and refined serifs provide the necessary gravitas for luxury property titles. 
- **UI & Data:** We use **Metropolis**. Its geometric, balanced construction ensures maximum legibility in data-dense tables and technical specifications.
- **Data Treatment:** All numerical values, token IDs, and technical specifications should use the `data-mono` or `label-caps` styles to emphasize precision and engineering-grade accuracy.

## Layout & Spacing

The layout is governed by a strict 12-column grid with a fixed maximum width to maintain a "monumental" feel on wide displays. 

- **Grid:** A 12-column system for desktop, collapsing to 4 columns for mobile.
- **Rhythm:** We use an 8px base unit. Component padding should be generous (24px+) to prevent the high data density from feeling cluttered.
- **Organization:** Content is grouped into logical "blocks" that align strictly to the vertical grid lines. Use whitespace as a separator rather than heavy horizontal rules whenever possible to maintain a clean, architectural floor-plan aesthetic.

## Elevation & Depth

To maintain a sophisticated and grounded aesthetic, depth is created through **tonal layering** and **fine lines** rather than aggressive shadows.

- **Tiers:** The background is `tertiary_color_hex`. Content containers (cards) use the absolute white `background_paper`.
- **Shadows:** Use only one shadow style: an "Ambient Foundation" shadow (0px 4px 20px rgba(44, 62, 80, 0.04)). It should be barely perceptible, suggesting the component is sitting directly on the surface.
- **Structural Lines:** Use 1px borders in a very faint slate (rgba(44, 62, 80, 0.1)) for table headers and section dividers to reinforce the engineering-grade grid.

## Shapes

The shape language is **sharp and rectangular**. In alignment with architectural motifs, we avoid rounded corners which can appear too "consumer-tech." 

- **Primary Elements:** Buttons, input fields, and cards must have 0px border-radius. 
- **Exceptions:** For interactive status chips or very small UI labels, a minimal 2px radius (Soft) may be used to differentiate them from structural layout elements, but the preference is always for sharp, 90-degree angles.

## Components

- **Buttons:** Solid Deep Slate for primary actions; Earthy Clay for secondary/call-to-property actions. Text must be `label-caps`. No gradients.
- **Cards:** White background, sharp corners, 1px faint border. No heavy shadows.
- **Input Fields:** Bottom-border only (blueprint style) or a full 1px border. Focus state uses a 2px Earthy Clay bottom border.
- **Data Tables:** High-density, using `Metropolis` for all entries. Rows should have a subtle hover state (#F4F4F4) but no visible alternating row colors.
- **Property Badges:** Small, sharp-edged rectangles using the Earthy Clay palette to denote "Luxury," "Commercial," or "Residential" status.
- **Token Progress Bars:** Thin, 4px height bars using Clay Brown on a Slate track to show funding or ownership percentages.