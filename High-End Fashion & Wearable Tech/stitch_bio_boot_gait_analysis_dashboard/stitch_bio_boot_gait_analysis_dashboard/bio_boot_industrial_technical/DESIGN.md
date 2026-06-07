---
name: Bio-Boot Industrial Technical
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0c0f0f'
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
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
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
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  body-fixed:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-margin: 24px
  gutter: 16px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for high-performance athletic environments where data precision and rugged durability are paramount. The brand personality is unapologetically technical, evoking the aesthetics of heavy machinery, aerospace telemetry, and tactical gear. It targets professional athletes and industrial workers who require real-time biometric feedback in demanding conditions.

The visual style is a hybrid of **Industrial Brutalism** and **High-Contrast Data Visualization**. It prioritizes function over form, utilizing a rigid structural grid, monospaced typography, and a "HUD" (Heads-Up Display) aesthetic. The interface should feel like a piece of precision equipment—reliable, cold, and hyper-accurate. Emotional responses should range from a sense of empowerment to intense focus, facilitated by a dark, low-distraction environment punctuated by high-visibility safety signals.

## Colors

The palette is strictly functional, derived from industrial safety standards. 

- **Primary Backgrounds:** Charcoal (#333333) serves as the foundation for all UI surfaces to reduce eye strain in high-glare environments.
- **Deep Surfaces:** Matte Black (#1A1A1A) is used for "wells," inset containers, and background depth to establish hierarchy without shadows.
- **Action & Alert:** Safety Orange (#FF6600) is the exclusive color for interactive triggers, critical alerts, and "Pressure-Point" highlights.
- **Data Readouts:** Crisp White and Light Gray (#F2F2F2) are reserved for telemetry, labels, and primary body text to ensure maximum legibility against dark backgrounds.
- **Glow Effects:** Use 15-25% opacity Safety Orange outer glows for active biometric zones to simulate hardware illumination.

## Typography

This design system utilizes a tiered typographic approach to separate brand expression from raw data.

- **Headlines:** Space Grotesk provides a technical yet modern geometric feel for high-level category headers.
- **Body & UI:** Inter is used for general descriptive text and interface controls due to its exceptional legibility at small sizes.
- **Data & Telemetry:** JetBrains Mono is mandatory for all numerical readouts, timestamps, and technical specs. Its fixed-width nature ensures that shifting data values do not cause layout "jitter."
- **Styling:** Use uppercase exclusively for labels and technical metadata. Headings should be tight and impactful.

## Layout & Spacing

The layout is built on a rigid 4px baseline grid, reflecting the precision of engineering schematics. 

- **Grid System:** A 12-column fluid grid is used for desktop views, transitioning to a 4-column grid for mobile/wearable interfaces.
- **Gutters & Margins:** Heavy 16px gutters reinforce the "blocky" industrial feel. 
- **Rhythm:** Spacing is strictly mathematical. Use 8px (2 units) for related elements and 24px-32px (6-8 units) to separate distinct functional modules.
- **Alignment:** All content must be hard-aligned to the grid. Avoid centering elements; favor left-aligned data blocks to mimic technical documentation.

## Elevation & Depth

This design system rejects ambient shadows and soft blurs in favor of **Structural Layering** and **Bold Outlines**.

- **Tiers:** Elevation is expressed through color stepping. The base is Matte Black (#1A1A1A). Secondary containers are Charcoal (#333333). 
- **Borders:** Surfaces are defined by 1px solid borders in Light Gray at 20% opacity. 
- **Pressure Points:** Interactive or high-interest zones use a 1px Safety Orange border.
- **Depth:** Use "inner-stroke" effects for input fields and data wells to make them appear recessed into the hardware frame. No drop shadows are permitted; if separation is needed, use a 1px offset line to simulate a physical seam.

## Shapes

The shape language is strictly **Sharp (0px)**. 

Every UI element—from buttons and cards to checkboxes and input fields—must feature 90-degree corners. This communicates a sense of structural integrity and industrial precision. Angled "clipped corners" (45-degree chamfers) are permitted for decorative frame elements or specialized data tags to reinforce the military/industrial aesthetic, but standard rounded corners are strictly prohibited.

## Components

- **Buttons:** Solid Safety Orange with Matte Black JetBrains Mono text for primary actions. Secondary actions use a 1px Orange ghost border with no fill.
- **Data Chips:** Small, rectangular modules with a Matte Black background and a 1px Charcoal border. Use JetBrains Mono for the content.
- **Lists:** Separated by 1px horizontal lines (Charcoal). Each list item should have a "status bar" indicator on the far left (2px wide).
- **Inputs:** Recessed (Matte Black) fields with a "scanning" line animation when focused. Labels must sit above the field in uppercase JetBrains Mono.
- **Pressure-Point Visualizations:** Used for heatmaps or stress zones. These feature a Safety Orange outer glow (`box-shadow: 0 0 8px #FF6600`) to indicate active data flow.
- **Icons:** 2px stroke-weight, non-rounded icons. Icons should look like technical symbols or schematics.
- **Cards:** No padding at the top/bottom if a "header" bar is used. Header bars should be a contrasting color (Charcoal) with the title inset.