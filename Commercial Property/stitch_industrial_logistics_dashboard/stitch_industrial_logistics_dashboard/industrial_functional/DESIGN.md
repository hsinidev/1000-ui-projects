---
name: Industrial Functional
colors:
  surface: '#071617'
  surface-dim: '#071617'
  surface-bright: '#2d3c3d'
  surface-container-lowest: '#031011'
  surface-container-low: '#0f1e1f'
  surface-container: '#132223'
  surface-container-high: '#1e2c2e'
  surface-container-highest: '#293738'
  on-surface: '#d5e6e7'
  on-surface-variant: '#cfc6ae'
  inverse-surface: '#d5e6e7'
  inverse-on-surface: '#243334'
  outline: '#98907a'
  outline-variant: '#4c4634'
  surface-tint: '#e7c433'
  primary: '#ffeebb'
  on-primary: '#3b2f00'
  primary-container: '#f4d03f'
  on-primary-container: '#6c5900'
  inverse-primary: '#705d00'
  secondary: '#b5c8df'
  on-secondary: '#203243'
  secondary-container: '#36485b'
  on-secondary-container: '#a4b7cd'
  tertiary: '#ebeff0'
  on-tertiary: '#2c3132'
  tertiary-container: '#cfd3d4'
  on-tertiary-container: '#565b5c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe174'
  primary-fixed-dim: '#e7c433'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#554500'
  secondary-fixed: '#d1e4fb'
  secondary-fixed-dim: '#b5c8df'
  on-secondary-fixed: '#091d2e'
  on-secondary-fixed-variant: '#36485b'
  tertiary-fixed: '#dfe3e4'
  tertiary-fixed-dim: '#c3c7c8'
  on-tertiary-fixed: '#181c1d'
  on-tertiary-fixed-variant: '#434849'
  background: '#071617'
  on-background: '#d5e6e7'
  surface-variant: '#293738'
typography:
  display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
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
    fontFamily: Inter
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
  unit: 8px
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for the high-stakes environment of industrial logistics and warehouse management. It prioritizes **durability, precision, and high utility** above all else. The brand personality is authoritative and no-nonsense, evoking the reliability of heavy machinery and the clarity of architectural blueprints. 

The visual style is a fusion of **Industrial Minimalism** and **Neo-Brutalism**. It utilizes raw, unrefined structural elements, heavy strokes, and a strict adherence to a utilitarian grid. This design system avoids decorative flourishes, ensuring that every UI element serves a specific operational purpose, facilitating rapid decision-making in high-pressure environments.

## Colors

The palette for this design system is rooted in industrial safety standards. 

- **Safety Yellow (#F4D03F):** Reserved exclusively for primary actions, critical alerts, and focal data points. It is the "high-vis" layer of the interface.
- **Charcoal (#2C3E50):** The primary structural background. It provides a deep, stable foundation that reduces eye strain in warehouse environments and maximizes the vibrance of the yellow highlights.
- **Light Grey (#ECF0F1):** Used for borders, secondary backgrounds (containers), and metadata to create legible separation without breaking the high-contrast aesthetic.
- **Status Colors:** Use standard hazard Red for errors and Emerald for "Clear/Safe" status, ensuring they maintain the same high-saturation "signal" quality as the primary yellow.

## Typography

This design system utilizes **Inter** for its neutral, systematic, and highly legible qualities. Typography is treated as a functional labeling system rather than an editorial choice.

- **Headlines:** Use heavy weights (800-900) to create clear information hierarchy.
- **Data Display:** Numerical values should use the `data-mono` style to ensure tabular alignment and clarity in rapidly changing metrics.
- **Labels:** All-caps labeling is used for UI markers, categories, and "tag-style" information to mimic industrial signage and shipping crate markings.

## Layout & Spacing

This design system employs a **12-column fluid grid** that prioritizes density and data-rich environments. The rhythm is based on an **8px linear scale**, ensuring consistent alignment across complex dashboards.

- **Density:** Elements are tightly packed to allow for maximum information visibility without scrolling, reflecting the "at-a-glance" requirements of logistics controllers.
- **Gaps:** Use rigid 16px gutters for horizontal separation. 
- **Alignment:** Every element must align to the grid; "optical" centering is discouraged in favor of mathematical precision.

## Elevation & Depth

To maintain the rugged, high-utility aesthetic, this design system rejects soft shadows and ambient blurs. Instead, depth is communicated through **Bold Borders** and **Tonal Layering**.

- **Surface Tiers:** Backgrounds use Charcoal (#2C3E50). Elevated containers (Cards, Modals) use a slightly lighter shade of Charcoal or a 1px solid Light Grey border to define their boundaries.
- **Interactions:** "Pressed" states are indicated by color inversion (Yellow background with Charcoal text) rather than physical lifts.
- **Hazard Patterns:** Use 45-degree diagonal striped patterns (Safety Yellow and Charcoal) for "Caution" areas or active loading states to add a tactile, industrial depth.

## Shapes

The shape language of this design system is strictly **Sharp (0px)**. 

Hard 90-degree angles are used for all buttons, inputs, cards, and containers. This reinforces the feeling of structural integrity, precision-cut steel, and industrial reliability. Circular elements are reserved strictly for status pips or specific iconography to ensure they stand out as signals against the rectangular grid.

## Components

Components in this design system are built to feel like physical controls on an industrial console.

- **Buttons:** Primary buttons use a solid Safety Yellow fill with bold Charcoal text. Secondary buttons use a Light Grey 2px border with no fill.
- **Input Fields:** Styled as recessed "wells" with Charcoal backgrounds and 1px Light Grey borders. Focus states use a 2px Safety Yellow border.
- **Data Visualizations:** Use high-contrast bar charts and step-line graphs. Avoid smooth curves; use jagged, precise lines to indicate real-time data.
- **Chips & Tags:** Small, rectangular blocks with `label-caps` typography. Use status colors (Red/Yellow/Green) as thin 4px vertical "hazard stripes" on the left edge of the chip.
- **Cards:** No shadows. Define card edges with 1px Light Grey strokes. Use a "Header Bar" in Charcoal (slightly lighter than background) to separate titles from content.
- **Status Indicators:** Use "Hazard" styling for alerts—bold yellow/black diagonal patterns for headers of critical system notifications.