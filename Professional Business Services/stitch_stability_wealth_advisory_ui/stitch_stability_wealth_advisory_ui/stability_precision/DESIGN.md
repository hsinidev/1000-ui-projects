---
name: Stability & Precision
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#434843'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#151817'
  on-tertiary: '#ffffff'
  tertiary-container: '#292c2c'
  on-tertiary-container: '#919392'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e1e3e2'
  tertiary-fixed-dim: '#c5c7c6'
  on-tertiary-fixed: '#191c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
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
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
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
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  section-padding: 80px
---

## Brand & Style

The visual identity of the design system is anchored in the concepts of institutional permanence and fiduciary responsibility. It is designed to evoke a sense of calm, calculated authority, specifically catering to high-net-worth individuals and corporate entities who prioritize security over trends.

The design style follows a **Corporate Modern** philosophy, leaning heavily into **Minimalism**. Every interface element is justified by function; there are no decorative flourishes. The aesthetic relies on the rigorous application of a grid, generous whitespace to reduce cognitive load, and a color palette that signals growth and groundedness. The goal is to create an environment where complex financial information feels structured, accessible, and immutable.

## Colors

The "Stability" palette is designed to be conservative yet distinct. 

- **Primary (Dark Forest Green):** Used for key brand touchpoints, primary call-to-actions, and structural navigation. It represents wealth, growth, and traditional banking heritage.
- **Secondary (Charcoal):** Reserved for high-level headings and primary text to ensure maximum contrast and readability.
- **Tertiary (Soft Slate):** A neutral background color used to differentiate sections without the starkness of pure white, providing a "paper-like" quality to reports.
- **Neutral (Mid-Grey):** Used for secondary text, metadata, and borders.

The system operates primarily in **Light Mode** to maintain a "white-paper" professional feel, which is essential for reading long-form financial disclosures and complex data tables.

## Typography

The design system utilizes **Inter** exclusively due to its exceptional legibility and sophisticated "tabular lining" features, which are critical for financial data.

- **Numerical Clarity:** For all financial figures and balances, use the `data-tabular` style. This ensures that columns of numbers align perfectly, facilitating easy comparison.
- **Hierarchy:** Headlines use a tighter letter-spacing and heavier weights to command attention, while body text uses a generous 1.5–1.6x line height to ensure readability in long-form advisory reports.
- **Labels:** Small, uppercase labels are used for metadata and table headers to provide clear categorization without competing with primary content.

## Layout & Spacing

This design system employs a **Fixed-Fluid Grid** hybrid. Content is housed within a maximum-width container of 1280px to prevent line lengths from becoming unreadable on ultra-wide monitors.

The internal rhythm is built on an **8px base unit**. 
- **Grids:** A 12-column system is used for desktop layouts, providing the flexibility needed for complex dashboards and multi-column financial statements.
- **Whitespace:** Use "generous" vertical spacing between sections (80px+) to signal premium positioning. 
- **Precision:** Elements must align strictly to the grid; avoiding "organic" or offset placements that could suggest a lack of rigor.

## Elevation & Depth

To maintain an authoritative and secure tone, the design system avoids aggressive shadows or floating elements. Instead, it uses **Low-Contrast Outlines** and **Tonal Layers**.

- **Borders:** Define containers using 1px solid borders in a lightened version of the Secondary color (#E0E0E0).
- **Z-Axis:** Instead of shadows, use subtle background shifts. For example, a card might sit on a `#F4F5F4` background with a white fill to indicate elevation.
- **Focus:** Shadows are only permitted on active states (e.g., a dropdown menu) and must be extremely diffused (30px+ blur) with very low opacity (5-8%) to mimic natural ambient light rather than digital glow.

## Shapes

The shape language is disciplined and geometric. 

The system uses a **Soft** (4px) corner radius. This choice provides a subtle modern touch that softens the "coldness" of a financial interface without appearing playful or consumer-grade. Large containers, such as cards or data tables, follow this 4px rule, while primary buttons may utilize the same radius to maintain a cohesive, "stamped" appearance. Sharp 90-degree angles are reserved for structural dividers and grid lines.

## Components

### Buttons
Primary buttons use the Dark Forest Green background with white text. They should be rectangular with a subtle 4px radius. Secondary buttons use a ghost style (Charcoal border and text) to indicate secondary actions. Avoid hover effects that include "bouncing" or scaling; use simple opacity or color shifts.

### Data Tables
Tables are the core of this design system. Use "zebra-striping" with the Tertiary color for readability. Table headers must be in `label-caps`. Cell padding should be generous (16px vertical) to ensure data doesn't feel cramped.

### Input Fields
Fields should have a 1px Charcoal border. When focused, the border weight remains 1px but transitions to Dark Forest Green. Labels should always be visible (never use placeholder-only labels) to ensure a sense of security and clarity during data entry.

### Cards & Containers
Used for grouping related financial metrics. Cards should have no shadow; they are defined by a 1px border. Use a white background to contrast against the soft grey page background.

### Progress & Status Indicators
Status indicators (e.g., "Verified," "Pending") must use desaturated versions of green and amber. High-saturation "traffic light" colors are too loud for this system; use subtle, sophisticated tones that prioritize the data over the alert.