---
name: High-Energy Tech Analytics
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c1c6d7'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#8b90a0'
  outline-variant: '#414754'
  surface-tint: '#adc7ff'
  primary: '#adc7ff'
  on-primary: '#002e68'
  primary-container: '#4a8eff'
  on-primary-container: '#00285b'
  inverse-primary: '#005bc0'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display:
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
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
spacing:
  base: 4px
  unit-1: 4px
  unit-2: 8px
  unit-4: 16px
  unit-6: 24px
  unit-8: 32px
  unit-12: 48px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for high-performance data environments, evoking a sense of technical dominance and real-time urgency. The brand personality is aggressive, precise, and authoritative, targeting data scientists and growth engineers who require clarity amidst complexity. 

The visual style is a fusion of **High-Contrast Bold** and **Modern Technical** aesthetics. It rejects soft, organic forms in favor of architectural rigidity and digital-first vibrance. The atmosphere is that of a "Command Center"—where high-density information is organized through strict hierarchies and punctuated by the "Electric Blue" of active signals. A subtle use of luminous glow effects provides a "live" feel to static screens, suggesting a continuous stream of incoming data.

## Colors

The color strategy utilizes a "Void" approach—using a deep black base to allow the Electric Blue primary color to vibrate with maximum luminosity. White is reserved for high-priority data and primary actions, ensuring a stark contrast ratio that minimizes eye strain during deep analysis.

Grays are meticulously stepped to create a sense of physical depth without using shadows. Each gray represents a different functional tier: darker grays for background containers and lighter grays for interactive or hovering elements. Functional colors (Success, Warning, Error) should maintain the same saturation levels as the Electric Blue to ensure a cohesive high-energy feel across the entire dashboard.

## Typography

The typography system balances technical character with utilitarian performance. **Space Grotesk** is used for headlines and primary metrics to provide a futuristic, geometric edge that aligns with the "high-energy" brand narrative. 

For dense data tables, Sankey diagram labels, and body text, **Inter** is utilized for its exceptional legibility and neutral tone. To emphasize the analytical nature of the platform, labels and secondary metrics utilize a high-weight, uppercase styling with increased letter spacing. This creates a "tabular" feel even when using a sans-serif font, ensuring that numbers and technical terms are easily scannable in high-density metric comparison cards.

## Layout & Spacing

This design system employs a 12-column fluid grid designed for maximum screen utilization. In a data-heavy environment, whitespace is used strategically as a separator rather than just "breathing room." A strict 4px base unit ensures mathematical alignment across all complex visualization containers.

Layouts should prioritize "dashboard density," allowing multiple metric cards and heatmaps to coexist without clutter. Gutters are fixed at 24px to provide clear visual lanes, while internal card padding follows a tighter 16px rhythm to keep related data points grouped tightly. Complex visualizations like Sankey diagrams should span at least 8 columns to maintain legible node paths.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Luminous Accents** rather than traditional shadows. This creates a flat, "HUD" (Heads-Up Display) effect that feels integrated into the screen.

- **Level 0 (Background):** Solid Black (#000000).
- **Level 1 (Containers):** Surface-Low (#121212) with a 1px solid border (#333333).
- **Level 2 (Interaction/Active):** Surface-Mid (#1E1E1E) with an Electric Blue glow.

Glow effects are used sparingly to denote "active" or "critical" states. A glow consists of a primary color border paired with a drop-shadow with 0px offset and a 10px-15px spread at 40% opacity. This makes key metrics appear as if they are emitting light from the screen.

## Shapes

The shape language of this design system is strictly **Sharp**. 0px border radii are applied to all buttons, input fields, cards, and data containers. This choice reinforces the precision, technical accuracy, and "high-energy" tech aesthetic. 

The absence of curves ensures that every pixel is utilized for data display and creates a rigid, grid-locked appearance that mirrors the structured nature of the analytics provided. Diagonal lines may be used in specific data viz icons to suggest movement and speed, but all structural UI elements must remain rectangular.

## Components

- **Metric Comparison Cards:** These are the core components. They feature a Sharp #121212 background, a 1px border, and a "glow" state when a metric deviates by >10%.
- **Buttons:** High-contrast White (#FFFFFF) with Black text for primary actions. Secondary actions use a ghost style with an Electric Blue border and 0px radius.
- **Data Visualization Containers:** Clean, border-only containers. Sankey diagrams and Heatmaps should use a standardized palette of Electric Blue gradients to show intensity, avoiding the typical "rainbow" heatmap in favor of monochromatic blue-scale.
- **Chips & Tags:** Small, rectangular blocks with uppercase Inter Bold labels. Status indicators (e.g., "Live", "Syncing") should feature a pulsing 4px square "signal" icon.
- **Input Fields:** Bottom-border only or full-border sharp rectangles. Focus state is indicated by a change from Gray to Electric Blue with no glow, maintaining text clarity.
- **List Items:** Separated by 1px solid lines (#333333), with a high-contrast hover state that shifts the background to #1E1E1E.