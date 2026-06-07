---
name: Aeronautical Precision
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#c1c6d7'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#303031'
  outline: '#8b91a0'
  outline-variant: '#414754'
  surface-tint: '#abc7ff'
  primary: '#abc7ff'
  on-primary: '#002f66'
  primary-container: '#448fff'
  on-primary-container: '#002859'
  inverse-primary: '#005cbc'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#4ae183'
  on-tertiary: '#003919'
  tertiary-container: '#00a657'
  on-tertiary-container: '#003115'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#004590'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#6bfe9c'
  tertiary-fixed-dim: '#4ae183'
  on-tertiary-fixed: '#00210c'
  on-tertiary-fixed-variant: '#005228'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
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
    letterSpacing: 0.02em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
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
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style
The design system is engineered for the high-stakes environment of global air freight and airport logistics. It targets logistics coordinators, pilots, and fleet managers who require instantaneous data comprehension and absolute reliability. The brand personality is professional and technologically advanced, prioritizing efficiency through visual clarity.

The aesthetic utilizes a **Glass-Cockpit** style—a hybrid of **Minimalism** and **Glassmorphism**. It evokes the flight deck of a modern freighter, using semi-transparent layers and high-contrast instrumentation to organize dense information without visual clutter. The "aerodynamic" feel is achieved through horizontal momentum, thin linear accents, and a sense of weightlessness in the UI layers.

## Colors
The color strategy for this design system is rooted in a "Night Flight" dark mode, which reduces eye strain during long-shift logistics monitoring.

- **Primary (Sky Blue):** Used for critical action states, active flight paths, and primary branding elements. It provides high visibility against the dark base.
- **Secondary (Silver):** Used for structural lines, borders, and secondary text. It mimics the metallic surfaces of aircraft fuselage.
- **Tertiary (Signal Green):** Reserved for "Clear for Takeoff" statuses, successful delivery confirmations, and positive system health.
- **Neutral (Matte Black):** The foundation of the UI, providing a deep, non-reflective surface that allows high-contrast data to pop.

## Typography
This design system employs a dual-font strategy to balance technical character with utilitarian readability. 

**Space Grotesk** is used for headlines and telemetry readouts. Its geometric, slightly futuristic construction echoes aeronautical engineering and digital flight displays. 

**Inter** is the workhorse for body copy, data tables, and labels. It ensures maximum legibility for complex cargo manifests and logistical coordinates. For data-heavy environments, use the `data-mono` variant to ensure numerical alignment in tracking tables.

## Layout & Spacing
The layout follows a **Fixed Grid** model within a maximum container width of 1440px to simulate a centralized control console. The system uses a 12-column grid with tight 16px gutters to maximize screen real estate for data visualizations.

The spacing rhythm is based on a 4px base unit, emphasizing density and precision. Components should use horizontal padding that is 1.5x their vertical padding to reinforce the aerodynamic, "wide-screen" feel of the cockpit aesthetic.

## Elevation & Depth
In this design system, depth is conveyed through **Glassmorphism and Tonal Layering** rather than traditional shadows.

1.  **Base Layer:** The Matte Black (#1A1A1B) surface acts as the "outside world" or background.
2.  **Instrumentation Layer:** Semi-transparent "Glass" panels (Background blur: 12px, Opacity: 40%) house the primary content.
3.  **Active Layer:** Elements that are being interacted with or require immediate attention use a subtle Sky Blue inner glow or a thin 1px Silver border.

Use "Aerodynamic Lines"—ultra-thin (0.5pt to 1pt) silver strokes—to separate sections within glass panels, creating the look of high-tech instrumentation.

## Shapes
The shape language is "Soft-Tech." While the industry is precise, absolute sharp corners feel dated and aggressive. A **Soft (4px)** radius is applied to standard UI components like buttons and input fields to maintain a modern, sleek feel.

For structural "Glass" containers, use a **Rounded-LG (8px)** radius to create a distinct separation from the content within. Interactive elements like toggle switches or status pills may use a fully "Pill-shaped" radius to indicate their tactile nature.

## Components
### Buttons
- **Primary:** Solid Sky Blue with white text. Apply a subtle top-to-bottom gradient (lighter blue to #007FFF) to give a slight 3D "backlit" effect.
- **Secondary:** Ghost style with a Silver 1px border and frosted glass background.

### Input Fields
Inputs are dark-themed with a 1px Silver border that illuminates in Sky Blue on focus. Labels should use the `label-caps` typography style, positioned above the field for clear vertical scanning.

### Cards & Panels
All cards must utilize the backdrop-filter (blur) effect. Borders are 1px Silver at 20% opacity. For "High-Priority" cards, add a 2px Sky Blue accent on the left vertical edge.

### Data Visualizations
Charts should use thin lines and high-contrast colors (Sky Blue for the primary metric, Silver for the baseline). Avoid solid fills; use gradients that fade into the Matte Black background to maintain the "Glass-Cockpit" transparency.

### Specialized Logistics Components
- **Telemetry Readouts:** Small, high-density blocks showing coordinates, weights, or timestamps using `data-mono` typography.
- **Status Indicators:** Small glowing "LED" dots next to text (Signal Green for active, Amber for delay, Red for grounded).