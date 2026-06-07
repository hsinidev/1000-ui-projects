---
name: Financial-Sleek System
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
  on-surface-variant: '#44474d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#75777e'
  outline-variant: '#c5c6cd'
  surface-tint: '#515f78'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#0d1c32'
  on-primary-container: '#76849f'
  inverse-primary: '#b9c7e4'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#191c1d'
  on-tertiary-container: '#828485'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
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
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is engineered to evoke institutional stability and modern agility, catering to founders and investors who require absolute clarity in equity management. The aesthetic balances the weight of a traditional financial firm with the frictionless experience of a seed-stage startup.

The style is **Corporate / Modern** with a lean towards **Minimalism**. It prioritizes legibility and information density without inducing cognitive overload. This is achieved through generous whitespace, a restricted color palette, and high-precision typography. The emotional response is one of "calculated trust"—where every pixel feels intentional and every data point is secure.

## Colors

The palette is anchored by **Deep Navy (#0A192F)**, used to represent authority and depth in headers, primary actions, and key navigation elements. **Silk White (#F8F9FA)** serves as the primary canvas, providing a crisp, non-glare background that enhances focus on data. 

**Silver (#C0C0C0)** is utilized for structural elements, refined borders, and secondary iconography, creating a metallic, high-end feel. Subtle gradients should transition from Silk White to a very light Silver to denote depth in interactive components. Functional colors (Success/Error) are desaturated to maintain the professional, understated atmosphere of the design system.

## Typography

This design system utilizes a dual-sans-serif approach to maximize clarity. **Public Sans** is used for headlines to provide a sturdy, institutional feel. **Inter** is the workhorse for all data-heavy environments and body copy, chosen for its exceptional legibility at small sizes and its "tabular lining" features, which ensure that columns of numbers align perfectly in financial tables.

High contrast is maintained by using Deep Navy for all primary text and a mid-tone slate for secondary labels. Paragraph widths are strictly controlled to ensure comfortable reading of legal and financial disclosures.

## Layout & Spacing

The design system employs a **Fixed Grid** model for dashboard views to ensure consistency across complex data visualizations. A 12-column grid is used for the primary layout, with a 24px gutter to provide breathing room between dense data sets.

The spacing rhythm is based on an 8px scale. Generous vertical padding (lg and xl units) is used between sections to prevent the UI from feeling "cramped," a common pitfall in financial software. Alignment is strictly left-heavy for text and right-heavy for numerical financial data to follow standard accounting patterns.

## Elevation & Depth

Visual hierarchy is established primarily through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. 

1.  **Level 0 (Surface):** Silk White background.
2.  **Level 1 (Cards/Sections):** 1px Silver (#C0C0C0) border with no shadow.
3.  **Level 2 (Modals/Popovers):** A subtle, diffused ambient shadow (Deep Navy at 5% opacity, 20px blur) to lift the element off the page without breaking the flat aesthetic.

Subtle linear gradients (Silk White to #F1F3F5) are used on primary buttons and header bars to provide a "tactile-lite" feel that suggests interactability while remaining professional.

## Shapes

The design system uses a **Soft (Level 1)** shape language. A standard radius of 4px (0.25rem) is applied to all buttons, input fields, and small UI components. Larger containers and cards use a 8px (0.5rem) radius.

This subtle rounding softens the "coldness" of the financial data while maintaining a precise, engineering-led appearance. Sharp 0px corners are reserved exclusively for internal table dividers and decorative hairline separators to emphasize a "grid-like" precision.

## Components

### Data Tables
Tables are the core of this design system. They must feature:
*   **Sticky headers** with a 1px Silver bottom border.
*   **Row highlighting** using a subtle Silk White to Silver hover state.
*   **Tabular numbers** for alignment of currency and equity percentages.

### Financial Charts
*   **Pie/Donut Charts:** Use a monochromatic Navy-to-Silver gradient scale to represent different stakeholders.
*   **Bar Charts:** Clean, vertical bars with 2px rounded top corners and no outlines.

### Interactive Sliders
Used for "what-if" equity scenarios. The track is Silver, and the active fill is Deep Navy. The handle is a Silk White circle with a 1px Silver border, providing a high-contrast, tactile point of interaction.

### Secure Document Components
Representing SAFEs, Note agreements, or Term Sheets. These components use a "vault" style: a Silver background, a padlock icon in Deep Navy, and a clear "Verified" badge using the status success color.

### Buttons & Inputs
*   **Primary Button:** Deep Navy background, Silk White text, 4px border-radius.
*   **Input Fields:** 1px Silver border that transitions to a 2px Deep Navy border on focus, ensuring clear user feedback during data entry.