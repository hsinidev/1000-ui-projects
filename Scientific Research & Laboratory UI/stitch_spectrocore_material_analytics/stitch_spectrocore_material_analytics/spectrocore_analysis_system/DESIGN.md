---
name: SpectroCore Analysis System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
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
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#faf8f7'
  on-tertiary: '#303030'
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
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-mono:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-tabular:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.08em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  grid-overlay: 32px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style

The design system is engineered for high-stakes chemical and material analysis. It evokes the atmosphere of a darkened laboratory where precision is paramount. The personality is clinical, authoritative, and hyper-focused, catering to research scientists and lab technicians who require maximum data density without visual fatigue.

The visual style is a fusion of **Minimalism** and **Technical Brutalism**. It prioritizes structural integrity through rigid grid systems and high-contrast logic. Every element serves a functional purpose, utilizing "Dark Lab" aesthetics—matte surfaces, glowing data indicators, and metallic accents—to create a tool-like interface that feels like a piece of high-end hardware.

## Colors

This design system utilizes a restricted, high-contrast palette optimized for dark environments.

*   **Matte Black (#121212):** The singular base for all primary surfaces to minimize light bleed and maximize focus on data.
*   **Neon Cyan (#00F3FF):** Reserved for critical data points, active laser states, primary action buttons, and successful analysis peaks. It should appear to "glow" against the dark background.
*   **Silver (#C0C0C0):** Used for structural elements, secondary labels, and inactive states. It provides a metallic, tactile quality to the UI.
*   **Deep Charcoal (#1A1A1A):** Used for subtle layering and card backgrounds to provide separation from the pure matte base.
*   **Alert Red (#FF3B3B):** Used exclusively for spectral anomalies or system errors.

## Typography

The typography strategy balances rapid legibility with a technical aesthetic. **Space Grotesk** is used for headlines to provide a futuristic, geometric edge. **Inter** handles the bulk of the interface's functional text for maximum clarity at small sizes. **JetBrains Mono** is utilized for all coordinate data, spectral values, and chemical formulas to ensure character distinction and tabular alignment. 

Vertical rhythm is tight to accommodate data density, and all labels should use uppercase styling with increased tracking to emphasize the "instrumentation" feel.

## Layout & Spacing

This design system employs a **Fixed Technical Grid**. The layout is divided into a 12-column system, but incorporates a persistent 32px background grid overlay in a low-opacity Silver (#C0C0C0 at 5% opacity). 

Components must snap to the 4px base unit. Spacing is intentionally compact to allow for multiple simultaneous spectral views and real-time telemetry panels. Information is grouped into modules with 1px Silver borders, creating a "schematic" look rather than using whitespace for separation.

## Elevation & Depth

Depth is conveyed through **Bold Borders** and tonal layering rather than shadows. Because the UI represents a high-precision instrument, surfaces do not "float."

1.  **Level 0 (Base):** Matte Black (#121212) for the global background.
2.  **Level 1 (Panels):** Deep Charcoal (#1A1A1A) with a 1px Silver (#C0C0C0) border at 20% opacity.
3.  **Level 2 (Active Elements):** Elements requiring focus use a 1px Neon Cyan (#00F3FF) border.
4.  **Data Overlays:** Tooltips and floating menus use a slight backdrop blur (4px) with a semi-opaque Matte Black fill to maintain legibility over complex line graphs.

## Shapes

The shape language is strictly **Sharp (0px)**. To maintain the professional, scientific aesthetic, all containers, buttons, and input fields must have square corners. This reinforces the precision-machined hardware metaphor and ensures perfect alignment with the technical grid. 

Exceptions are made only for status indicators (LED style), which remain perfect circles.

## Components

*   **Buttons:** Primary buttons are Solid Neon Cyan with Black text. Secondary buttons are Ghost-style with a 1px Silver border and Silver text. Hover states should trigger a subtle outer glow (0 0 8px) in Cyan.
*   **Data Graphs:** Line graphs must use 1.5px stroke width. The primary data line is Neon Cyan. Comparison lines use Silver or dashed patterns. Grid lines within the graph use 10% opacity Silver.
*   **Input Fields:** Minimalist design with only a bottom 1px Silver border. On focus, the border turns Neon Cyan and the label shifts to the `label-caps` style above the field.
*   **Chips/Badges:** Small, rectangular tags with 1px borders. Used for chemical element symbols (e.g., [Fe], [Cu]).
*   **Telemetry Lists:** Dense rows of data using JetBrains Mono. Alternate rows may have a 5% Silver fill for scanability.
*   **Status Indicators:** Small circular "LED" icons. Neon Cyan for "Active/Scanning," Dim Silver for "Standby," and Red for "Error."
*   **Crosshairs:** Use thin, 0.5px Cyan lines for graph cursors and data point selection to emphasize surgical precision.