---
name: NeoDistrict Brutalist-Tech
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c7c6c6'
  on-secondary: '#2f3031'
  secondary-container: '#464747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#fbf7f7'
  on-tertiary: '#313030'
  tertiary-container: '#dedbda'
  on-tertiary-container: '#616060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  mono-label:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-point:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
  margin: 40px
---

## Brand & Style

The design system is engineered to evoke a "Neo-Industrial" atmosphere, targeting urban dwellers who value architectural integrity and technological edge. The aesthetic is defined by **Hard-Tech Brutalism**: a synthesis of raw construction materials and high-fidelity digital accents. 

The emotional response should be one of "Uncompromising Modernity." The UI does not apologize for its sharp edges or industrial origins; instead, it frames luxury through the lens of structural honesty and "glitch-perfect" execution. Visual interest is driven by the tension between the cold, matte surfaces of concrete and the high-energy vibration of neon light.

## Colors

This design system utilizes a high-contrast tri-color palette optimized for a dark-mode default experience. 

*   **Matte Black (#121212):** The structural foundation. Used for deep backgrounds and solid heavy-duty containers.
*   **Neon Blue (#00F3FF):** The "Pulse." Used exclusively for interactive states, data highlights, and glowing accents to simulate light emitting from hardware.
*   **Concrete Grey (#8E8E8E):** The "Texture." Used for borders, secondary text, and architectural dividers.
*   **Pure White (#FFFFFF):** Reserved for high-priority legibility and critical data points against the dark substrate.

Apply a 5% noise texture overlay across the Matte Black surfaces to simulate the grit of cast concrete.

## Typography

The typographic system relies on **Space Grotesk** to bridge the gap between architectural geometry and technical precision. 

Headlines must be aggressive, tight, and massive. Use "mono-label" for all metadata, system status, and technical descriptions to lean into the industrial-spec feel. All labels should be uppercase with increased letter spacing to mimic stamped metal or blueprints. For data visualization or loft numbers, use the boldest weights available to emphasize the structural weight of the brand.

## Layout & Spacing

The layout follows a **Rigid Grid** philosophy. Elements must feel "bolted" to a 12-column grid. 

*   **Gutters:** Fixed at 24px, treated as structural gaps.
*   **Margins:** Generous 40px outer margins to frame the content like a blueprint.
*   **Alignment:** Use hard vertical lines (1px Concrete Grey) to separate columns visually in complex dashboards. 
*   **Rhythm:** Spacing is strictly mathematical, moving in multiples of 4px. Avoid soft, organic whitespace; favor dense information blocks separated by heavy structural dividers.

## Elevation & Depth

In this design system, depth is achieved through **Luminance and Structural Borders** rather than soft shadows. 

1.  **Level 0 (Base):** Matte Black (#121212) with a grit/noise texture.
2.  **Level 1 (Panels):** Defined by 2px solid Concrete Grey (#8E8E8E) borders. No background color change.
3.  **Level 2 (Active/Hover):** Inner glows using Neon Blue (#00F3FF) with a 10px-20px blur radius to simulate light spill from behind a panel.
4.  **Structural Insets:** Use 1px highlights on the top and left edges to create a "machined" look, suggesting the UI is etched into a surface.

## Shapes

The shape language is strictly **Rectilinear**. 

There are zero rounded corners in the design system. Every button, input field, card, and image container must have a 0px border radius. This reinforces the "Brutalist" architectural theme. To add technical detail, use "clipped corners" (45-degree chamfers) on primary buttons or active tab indicators to evoke military-grade hardware or industrial stencils.

## Components

*   **Buttons:** Rectangular with a 2px Concrete Grey border. On hover, the border and text switch to Neon Blue with a matching outer "neon glow" drop shadow (0 0 15px #00F3FF).
*   **Input Fields:** Bottom-border only (2px Concrete Grey). Focus state triggers a full Neon Blue box-shadow and a monospaced "INPUT_ACTIVE" label in the top right.
*   **Cards:** Transparent backgrounds with 2px Concrete Grey borders. Headlines within cards should be followed by a horizontal "structural beam" (divider line).
*   **Chips/Tags:** Monospaced text inside a solid Concrete Grey box with black text. No padding on the top/bottom to keep them compact and technical.
*   **Status Indicators:** Use a "flicker" animation for active Neon Blue elements to simulate a high-voltage connection.
*   **Progress Bars:** Segmented blocks rather than a continuous line, resembling a digital readout on a piece of machinery.