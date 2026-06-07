---
name: SteelFrame Industrial
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb596'
  primary: '#ffb596'
  on-primary: '#581e00'
  primary-container: '#ff6600'
  on-primary-container: '#561d00'
  inverse-primary: '#a33e00'
  secondary: '#96ccff'
  on-secondary: '#003353'
  secondary-container: '#025483'
  on-secondary-container: '#8ec8fe'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#989696'
  on-tertiary-container: '#2f2f2f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb596'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#cee5ff'
  secondary-fixed-dim: '#96ccff'
  on-secondary-fixed: '#001d32'
  on-secondary-fixed-variant: '#004a75'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin: 48px
  max_width: 1440px
---

## Brand & Style
The design system is engineered to project structural integrity, technical precision, and high-visibility reliability. It is designed for a target audience of architects, general contractors, and civil engineers who value durability and professional-grade performance over aesthetic softness. 

The visual style is a hybrid of **Industrial Brutalism** and **High-Contrast Modernism**. It utilizes raw, unrefined structural elements—such as visible grid lines and heavy borders—to mimic the skeletal frames of skyscrapers. The interface should feel as solid as the steel it represents: grounded, immutable, and strictly functional.

## Colors
This design system utilizes a high-visibility palette rooted in industrial safety and raw materials.

*   **Safety Orange (#FF6600):** Used exclusively for primary actions, critical alerts, and focal points that require immediate attention.
*   **Steel Blue (#4682B4):** Applied to secondary structural elements, data visualizations, and links to provide a cooler, professional contrast to the heat of the orange.
*   **Charcoal (#333333):** The foundational surface color, providing a deep, non-reflective background that mimics oxidized steel and construction sites.
*   **Neutral Off-White (#E0E0E0):** Used for primary body text and high-contrast labels to ensure legibility against dark surfaces.

The default mode is **Dark**, simulating the high-end workstation environments used by draftsmen and engineers.

## Typography
The typographic hierarchy in this design system is built for maximum impact and technical clarity. 

**Space Grotesk** is used for all headlines and labels. Its geometric, slightly technical character evokes the precision of CAD software. All headers must be rendered in uppercase with heavy weights to simulate industrial stamping.

**Work Sans** is used for body copy and technical specifications. It is chosen for its exceptional legibility and neutral, reliable personality, ensuring that complex project data remains easy to parse.

## Layout & Spacing
The layout is governed by a **heavy fixed grid** model. This design system utilizes a strict 12-column grid with visible 1px borders between sections to emphasize the "frame" metaphor. 

Rhythm is maintained through an 8px base unit. Wide margins and generous gutters provide the necessary breathing room to prevent the heavy typography from feeling cluttered. Alignment should always be hard-edged; avoid centered layouts in favor of strong left-aligned columns that feel like architectural columns.

## Elevation & Depth
In alignment with the structural theme, this design system rejects soft shadows and ambient blurs. Depth is conveyed through **Bold Borders** and **Tonal Layers**.

*   **Structural Lines:** Use 2px solid borders in Charcoal (on light backgrounds) or Neutral (on dark backgrounds) to define containers.
*   **Inset Depth:** Form fields and interactive areas should use subtle "pressed" effects through darker background shades, rather than shadows.
*   **Layering:** Elements are stacked like steel plates. A higher-priority element does not cast a shadow but instead utilizes a high-contrast border or a bright fill color (Safety Orange) to "pop" forward in the visual hierarchy.

## Shapes
The shape language is strictly **Sharp (0px radius)**. Every element—from buttons to cards to input fields—must feature 90-degree angles. This reinforces the "Steel" aesthetic, echoing the hard cuts of I-beams and structural plates. There are no rounded corners in this design system, as softness contradicts the brand's industrial strength.

## Components
Components in this design system are built to feel substantial and tactile.

*   **Buttons:** Rectangular, heavy 2px borders, uppercase text. The primary button uses a solid Safety Orange fill with Charcoal text. On hover, the button should invert colors or shift to a slightly lighter orange.
*   **Cards:** Defined by a 1px Charcoal border. Headers within cards should have a distinct background tint to separate them from the card body, resembling a header plate on a shipping container.
*   **Input Fields:** High-contrast boxes with a 1px Steel Blue border that thickens to 3px on focus. Labels sit directly above the field in "label-caps" style.
*   **Chips/Tags:** Used for status (e.g., "In Progress," "Shipped"). These are solid blocks of color with zero transparency, using high-contrast text.
*   **Structural Dividers:** 2px solid lines. Occasionally, use a "diagonal stripe" pattern (Safety Orange/Black) for warning zones or critical section breaks to mimic hazard tape.
*   **Data Tables:** Strict, heavy borders between all cells. Header rows should be Steel Blue with white uppercase text.