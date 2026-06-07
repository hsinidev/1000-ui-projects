---
name: Industrial Intelligence
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
  on-surface-variant: '#5a4136'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#8e7164'
  outline-variant: '#e3bfb1'
  surface-tint: '#a23f00'
  primary: '#a23f00'
  on-primary: '#ffffff'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#ffb595'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#969797'
  on-tertiary-container: '#2e3030'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
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
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-mono:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-padding: 1.5rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

The design system is engineered for the high-stakes environment of global logistics and supply chain management. It prioritizes mechanical reliability and structural integrity over decorative flair. The aesthetic is **Industrial-Technical**, a hybrid of Corporate Modern efficiency and a refined Architectural Brutalism.

The target audience consists of logistics coordinators and data analysts who require immediate clarity in complex environments. The UI evokes a "mission control" atmosphere—utilitarian, rugged, and precise. Visual weight is used to communicate stability, while high-contrast accents ensure critical alerts are impossible to miss amidst dense data sets.

## Colors

The palette is derived from industrial safety standards and heavy machinery. 

- **Safety Orange (#FF6700):** Reserved exclusively for primary actions, critical alerts, and active state indicators. It functions as the "hazard" light of the interface, drawing immediate eye movement.
- **Charcoal (#333333):** Used for primary typography, heavy borders, and structural headers to provide a grounded, high-contrast foundation.
- **Light Grey (#F4F4F4):** The primary surface color for secondary containers and layout partitioning, reducing eye strain during long monitoring sessions while maintaining a clean, technical backdrop.

Color application must follow a strict functional hierarchy: if a component is not interactive or alarming, it should remain within the monochromatic Charcoal and Grey spectrum.

## Typography

Typography in this design system is optimized for rapid scanning and data density. 

**Inter** is utilized for all body copy and tabular data. Its neutral, systematic geometry ensures legibility at small scales in complex tables. **Space Grotesk** is used for headlines, labels, and technical readouts to inject a "cutting-edge" engineering feel. 

Technical labels should often use uppercase styling with increased letter spacing to mimic industrial equipment tagging. Numeric data should prioritize clarity; where possible, use tabular figures to ensure columns of numbers align perfectly for easier comparison.

## Layout & Spacing

This design system employs a **12-column fluid grid** with a tight 16px gutter to maximize the "data-per-square-inch" ratio. The layout model is built on a 4px baseline grid, ensuring all components align to a rigorous vertical rhythm.

Information density is categorized into two modes:
1.  **Monitoring Mode:** Compact spacing with minimal padding for large-scale data tables and fleet overviews.
2.  **Management Mode:** Increased breathing room (using `stack-lg`) for configuration screens and detailed report generation.

Layouts should favor structural grouping using 1px Charcoal borders rather than excessive whitespace to maintain the rugged, blueprint-inspired aesthetic.

## Elevation & Depth

To maintain the professional, rugged feel, this design system avoids soft ambient shadows. Depth is communicated through **Bold Borders** and **Tonal Layers**.

- **Z-0 (Base):** Light Grey (#F4F4F4) for the global background.
- **Z-1 (Surface):** White (#FFFFFF) for primary cards and content areas, defined by a 1px solid Charcoal (#333333) or Mid-Grey border.
- **Z-2 (Active):** Safety Orange (#FF6700) borders or subtle Charcoal "hard shadows" (2px offset, 0 blur, 100% opacity) for interactive elements like hovered buttons or selected cards.

This approach creates a tactile, "stamped" appearance that feels structural rather than ethereal.

## Shapes

The shape language is strictly **Soft (0.25rem)**. While a completely sharp (0px) edge can feel too aggressive, a small radius provides enough modernization without losing the industrial "machined" look.

Interactive elements like buttons and input fields use the base 4px radius. Status badges and indicators use the same radius to maintain consistency across the UI. Circular shapes are reserved exclusively for status "pips" or user avatars to create a clear visual distinction between data categories and people.

## Components

### Technical Data Tables
Tables are the core of the design system. They must feature Charcoal headers with white text for maximum contrast. Rows should use alternating zebra striping in Light Grey. Cell padding should be tight to support high data density.

### High-Contrast Data Cards
Cards are used for summarizing KPIs. They feature a 1px Charcoal top-border or left-accent. Important metrics should be displayed in Space Grotesk Bold. If a metric exceeds a threshold, the card's accent border changes to Safety Orange.

### Buttons
- **Primary:** Solid Safety Orange with White or Charcoal text. Sharp, high-visibility.
- **Secondary:** Transparent background with a 2px Charcoal border. 
- **Tertiary:** Charcoal text with an underline on hover, used for low-priority actions within data rows.

### Status Indicators
Status is communicated through a "Signal Lamp" pattern: a small colored circle (Safety Orange for Warning/Critical, Charcoal for Neutral/Idle, Green for Success) paired with an all-caps label in Space Grotesk.

### Input Fields
Inputs must feel like form fields on a technical spec sheet: White background, 1px Charcoal border, and sharp corners. The focus state replaces the Charcoal border with a 2px Safety Orange border.