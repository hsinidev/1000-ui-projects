---
name: Institutional Real Estate
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e0'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f9'
  surface-container: '#efedf3'
  surface-container-high: '#e9e7ee'
  surface-container-highest: '#e3e2e8'
  on-surface: '#1a1b20'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3035'
  inverse-on-surface: '#f1f0f6'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#2d0700'
  on-tertiary: '#ffffff'
  tertiary-container: '#501300'
  on-tertiary-container: '#d37758'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#ffb59e'
  on-tertiary-fixed: '#390b00'
  on-tertiary-fixed-variant: '#783018'
  background: '#faf8ff'
  on-background: '#1a1b20'
  surface-variant: '#e3e2e8'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  h1-investment:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h2-sidebar:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-metric:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
  body-standard:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  table-data:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin: 32px
  card-padding: 24px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style

The design system is engineered for an institutional real estate investment audience, where trust, precision, and clarity are paramount. The aesthetic is rooted in **Corporate Modernism**, prioritizing functional density without sacrificing breathing room. It aims to evoke a sense of "Blue Chip" stability, positioning the platform as a reliable authority in high-stakes financial data. 

The style is minimalist and high-contrast, stripping away decorative flourishes to highlight key investment metrics. It utilizes a restrained palette and structural grid to ensure that complex multi-family asset data remains legible and actionable for institutional investors and fund managers.

## Colors

The color strategy centers on **Royal Blue (#002366)** to establish institutional credibility and legacy. **Slate Grey (#708090)** serves as the functional secondary, used for utility icons, secondary labels, and UI borders to provide a sophisticated, muted contrast against the primary brand color. 

The background is strictly **White (#FFFFFF)** to maintain a "Paper-white" financial report feel. A specialized semantic palette is included for financial indicators: a deep forest green for positive yield/growth and a sharp crimson for risk/deficit. Neutral greys are used exclusively for structural grouping and disabled states, ensuring the primary blue remains the dominant focal point for primary actions.

## Typography

The design system utilizes **Inter** for its exceptional legibility in data-heavy environments. The hierarchy is optimized for financial scanning:
- **Numerical Data:** Uses medium weights (500-600) to ensure that cap rates and valuations are immediately visible.
- **Headers:** Reserved for asset names and section titles, utilizing a tighter letter spacing for a modern, authoritative look.
- **Labels:** Small-scale uppercase labels provide a clear taxonomy for data categories without competing with the values themselves.
- **Tables:** A specific 13px size is used for tabular data to maximize information density while maintaining vertical alignment.

## Layout & Spacing

The layout follows a **12-column fixed grid** with a maximum container width of 1440px to ensure a consistent viewing experience on professional workstations. An 8px base unit dictates all spatial relationships.

- **Dashboards:** Utilize a modular grid where components span 3, 4, 6, or 12 columns.
- **Information Density:** Spacing between data points is compact (stack-sm) while the space between distinct functional blocks is generous (stack-md) to prevent visual fatigue.
- **Margins:** Large 32px outer margins ensure the content feels framed and prestigious.

## Elevation & Depth

This design system employs a **Layered Tonal** approach rather than heavy skeuomorphism. 
- **Levels:** Level 0 is the white background. Level 1 consists of white cards with a subtle 1px border (#E5E7EB).
- **Shadows:** A single, soft "Institutional Shadow" is used for hover states and active cards (0px 4px 12px rgba(0, 0, 0, 0.05)).
- **Depth:** Interactive map elements and modals use a slightly more pronounced shadow to indicate temporary placement over the base data layer.
- **High-Contrast Outlines:** Tables do not use shadows; they use 1px horizontal dividers in Slate Grey at low opacity to maintain a crisp, structured appearance.

## Shapes

The design system utilizes a **Soft (4-8px)** rounding logic. 
- **Standard Components:** Buttons, input fields, and small cards use a 4px (0.25rem) radius to feel modern yet professional.
- **Large Containers:** Dashboard cards and map containers use an 8px (0.5rem) radius to soften the institutional edge.
- **Interactive Elements:** Checkboxes and status pills maintain the 4px radius, avoiding fully rounded pill shapes to keep the interface feeling "square" and serious.

## Components

### Data Visualization Cards
Investment cards feature a Royal Blue header accent. Primary metrics (e.g., IRR, Equity Multiple) are placed in the top right with high-contrast semi-bold weights. The body of the card uses Slate Grey for secondary descriptors.

### High-Contrast Tables
Tables are the core of the platform. They feature:
- Sticky headers with a subtle Slate Grey bottom border.
- Alternating row highlights (zebra striping) using a 2% opacity Slate Grey.
- Column-specific alignment: text to the left, financial figures to the right.

### Map Interface
The interactive map uses a "Silver" or "Light" base map style. Custom markers are Royal Blue with white icons. On-hover tooltips use the standard Level 1 elevation with an 8px radius.

### Buttons & Inputs
- **Primary Button:** Solid Royal Blue with White text.
- **Secondary Button:** White background with a 1px Slate Grey border and Royal Blue text.
- **Input Fields:** 1px Slate Grey border that thickens to 2px Royal Blue on focus. Labels are always persistent and positioned above the field.

### Status Indicators
Small, rectangular chips with 4px corners. They use low-saturation background tints of the semantic colors (Success/Error) with high-saturation text to ensure accessibility and professional restraint.