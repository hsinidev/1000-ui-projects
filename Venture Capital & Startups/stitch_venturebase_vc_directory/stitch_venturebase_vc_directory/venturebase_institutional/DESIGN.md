---
name: VentureBase Institutional
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#444657'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#747689'
  outline-variant: '#c4c5da'
  surface-tint: '#1941ff'
  primary: '#0028c2'
  on-primary: '#ffffff'
  primary-container: '#0038ff'
  on-primary-container: '#c8ceff'
  inverse-primary: '#bbc3ff'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#3f4345'
  on-tertiary: '#ffffff'
  tertiary-container: '#575a5c'
  on-tertiary-container: '#cfd1d3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dee0ff'
  primary-fixed-dim: '#bbc3ff'
  on-primary-fixed: '#000e5e'
  on-primary-fixed-variant: '#002cce'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display-xl:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 16px
  margin: 32px
  density-compact: 8px
  density-comfortable: 16px
---

## Brand & Style

The design system is engineered for the high-stakes world of venture capital, where clarity and precision are paramount. The brand personality is institutional, authoritative, and clinical, designed to facilitate rapid data synthesis and comparison. It adopts a **Corporate / Modern** style that leans heavily into **Minimalism** to ensure that complex financial datasets remain the focal point.

The aesthetic avoids unnecessary ornamentation, focusing instead on structural integrity and a systematic approach to information hierarchy. The emotional response is one of reliability and "quiet power"—positioning the platform as an indispensable tool for professional investors who value efficiency over flair.

## Colors

This design system utilizes a high-contrast palette anchored in Royal Blue to signify trust and technological sophistication. 

- **Primary (Royal Blue):** Reserved for primary actions, active states, and critical data highlights.
- **Secondary (Slate):** Used for supporting UI elements, iconography, and secondary text to provide a sophisticated, neutral backdrop.
- **Neutral (Deep Slate/Black):** Applied to primary headings and body text to ensure maximum readability against the white workspace.
- **Tertiary (Cloud):** A very light slate used for subtle backgrounds, row striping, and divider lines to organize high-density information without adding visual noise.

The "White" workspace provides the necessary "air" to prevent high-density data from feeling cluttered, maintaining a clean, professional canvas.

## Typography

The typographic strategy prioritizes "scannability." **Public Sans** is used for headlines to provide a sturdy, institutional feel. **Inter** is the workhorse for all UI and data displays; its tall x-height and tabular numeral properties make it the ideal choice for comparing financial figures and dense cap tables.

- **Data Density:** Use `body-sm` for secondary metadata and `data-tabular` for all numerical values in tables to ensure perfect vertical alignment.
- **Case Usage:** Utilize `label-md` in all-caps with increased letter spacing for table headers and section overviews to create a clear visual distinction from the data itself.

## Layout & Spacing

This design system employs a **Fixed Grid** model (12-columns) centered on a 1440px canvas. This ensures that data visualization remains consistent and predictable across professional-grade monitors.

The spacing rhythm is built on a 4px base unit to allow for tight, "compact" layouts necessary for data-heavy dashboards.
- **Information Density:** Vertical padding in data tables should be kept to `density-compact` to maximize the number of rows visible above the fold. 
- **Logical Grouping:** Use larger `margin` values (32px+) only between major functional modules to maintain a clear separation of concerns.

## Elevation & Depth

To maintain a "clean" and "professional" look, this design system rejects heavy shadows in favor of **Low-contrast outlines** and **Tonal layers**. 

- **Level 0 (Background):** White (#FFFFFF) or Ghost Gray (#F8FAFC) for the main canvas.
- **Level 1 (Cards/Modules):** White background with a 1px border in Slate-200 (#E2E8F0).
- **Level 2 (Interactive/Popovers):** A very subtle, "clinical" shadow (0px 4px 12px rgba(15, 23, 42, 0.08)) is used only for elements that temporarily float above the UI, such as dropdown menus or filter panels.

Depth is primarily communicated through color-blocking and borders rather than physical metaphors.

## Shapes

The shape language is "Soft" (0.25rem / 4px). This slight rounding of corners takes the edge off a purely "Brutalist" grid without sacrificing the serious, corporate tone. 

- **Primary Elements:** Buttons and Input fields use a 4px radius.
- **Structural Elements:** Data containers and cards use an 8px (rounded-lg) radius to provide a subtle containerization of information.
- **Visual Indicators:** Status badges (e.g., "Seed", "Series A") may use a fully rounded (pill) shape to distinguish them from interactive buttons.

## Components

- **Buttons:** Solid Royal Blue for primary actions with high-contrast white text. Secondary buttons use a Slate-200 border with Royal Blue text. No gradients.
- **Data Tables:** The core of the system. Use "Zebra striping" with Tertiary color for rows. Header rows are sticky, using `label-md` typography.
- **Input Fields:** 1px Slate borders that transition to Royal Blue on focus. Labels are always persistent (not floating) to ensure user orientation during complex data entry.
- **Comparison Chips:** Used for filtering VCs. These should be compact, using `body-sm` with a "dismiss" icon.
- **KPI Cards:** Large-format numerical displays for "Total Funding" or "Dry Powder," utilizing `headline-lg` for the value and `label-md` for the metric name.
- **VC Profile Cards:** High-density summaries featuring a small firm logo, primary sector tags (chips), and a 3-column mini-table of recent investments.