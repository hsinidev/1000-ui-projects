---
name: Fortress Protocol
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#444653'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#757684'
  outline-variant: '#c5c5d5'
  surface-tint: '#3e54c1'
  primary: '#001360'
  on-primary: '#ffffff'
  primary-container: '#002395'
  on-primary-container: '#8094ff'
  inverse-primary: '#bac3ff'
  secondary: '#5e5e5d'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdd'
  on-secondary-container: '#626361'
  tertiary: '#161948'
  on-tertiary: '#ffffff'
  tertiary-container: '#2c2f5e'
  on-tertiary-container: '#9598ce'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dee1ff'
  primary-fixed-dim: '#bac3ff'
  on-primary-fixed: '#001159'
  on-primary-fixed-variant: '#223aa8'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e0e0ff'
  tertiary-fixed-dim: '#bfc2fb'
  on-tertiary-fixed: '#131645'
  on-tertiary-fixed-variant: '#3f4273'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.25'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.55'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.45'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  mono-data:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
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
  gutter: 24px
  margin: 32px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to evoke an atmosphere of absolute technical authority and unwavering security. Targeted at enterprise legal teams, AI researchers, and compliance officers, the visual language balances high-stakes safety with corporate reliability.

The chosen style is **Hardened Corporate Minimalism**. It leverages the structural integrity of a grid-heavy layout combined with a "hardened" aesthetic—utilizing precise borders, layered surfaces, and high-density information displays. The UI should feel like a high-performance instrument: objective, meticulous, and resilient. Every element is designed to feel anchored and intentional, minimizing fluff to prioritize rapid risk assessment and data clarity.

## Colors

The palette is anchored by **Royal Blue**, serving as the primary signal of institutional trust and authority. This is supported by **Platinum Silver**, which provides a high-tech, metallic structural feel to the interface.

- **Primary (Royal Blue):** Used for primary actions, active states, and brand-critical identifiers.
- **Secondary (Platinum Silver):** Used for structural borders, background layering, and inactive states to create a "brushed steel" professionalism.
- **Deep Navy:** Used for text headers and high-contrast navigational elements.
- **Backgrounds:** A tiered system of Clean White (#FFFFFF) for content surfaces and Light Silver Grays (#F8F9FA) for layout scaffolding.
- **Risk Indicators:** Subtle but high-saturation Ambers and Reds are reserved exclusively for safety violations and compliance warnings.

## Typography

This design system utilizes **Inter** exclusively for its systematic, utilitarian clarity and exceptional legibility at small sizes. 

The typographic scale is highly structured. Headlines use bold weights and tighter letter-spacing to appear "dense" and authoritative. Body copy is optimized for readability with generous line heights. A specific **Label-Caps** style is used for metadata and technical categories to differentiate descriptive content from data. For raw AI logs or compliance code snippets, a fallback monospace font is used to maintain technical context.

## Layout & Spacing

The system follows a **Fixed-Fluid Hybrid Grid**. The main content area is capped at 1440px to ensure line lengths remain readable for dense reports, while the margins expand to fill ultra-wide monitors.

A strict **4px baseline grid** governs all spatial relationships. 
- **Density:** The layout favors a high-density information model. Padding is intentionally compact (16px–24px) to allow for the simultaneous display of multiple data streams and risk charts.
- **Rhythm:** Elements are grouped using a "Box-in-Box" philosophy, where nested components use progressively smaller spacing units to indicate relationship hierarchies.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and **Low-Contrast Outlines** rather than dramatic shadows. This reinforces the "hardened" aesthetic.

- **Surfaces:** Level 0 is the Light Silver background. Level 1 is the White content card. 
- **Borders:** Every card and container uses a 1px solid border (#E5E4E2). This creates a sense of structural integrity.
- **Shadows:** When necessary to indicate modals or popovers, shadows are extremely subtle: 0px 4px 12px with a 5% opacity Deep Navy tint.
- **Active States:** Elevation is conveyed by shifting the border color from Platinum Silver to Royal Blue, rather than increasing shadow depth.

## Shapes

The design system uses a **Soft (0.25rem)** roundedness level. This small radius softens the edges enough to feel modern and accessible, yet remains sharp enough to convey precision and institutional rigor.

- **Primary Components:** Buttons, inputs, and cards use a 4px corner radius.
- **Large Containers:** Modals or large dashboard panels may use a 8px radius (`rounded-lg`) to differentiate them from the primary grid.
- **Risk Indicators:** Status dots and certain "Pill" chips for safety categories use a fully rounded radius to differentiate them from interactive UI elements.

## Components

- **Buttons:** Primary buttons are solid Royal Blue with white text. Secondary buttons use a Platinum Silver border with Deep Navy text. All buttons feature a "hard" hover state (slight darken) without translation or bounce animations.
- **Input Fields:** Use a white background with a 1px Platinum Silver border. On focus, the border thickens to 2px Royal Blue. Labels are always positioned above the field in `Label-Caps`.
- **Status Chips:** Small, rectangular indicators with a light tint of the semantic color (e.g., Light Red background) and dark text (e.g., Deep Red). These must be used for risk levels (Critical, High, Moderate, Low).
- **Data Cards:** Containers for AI metrics. They must feature a 1px header separator and a 4px left-accent border colored by the risk status of the data within.
- **Compliance Lists:** High-density rows with alternating subtle gray backgrounds. Each row includes a "Hardened Border" to clearly delineate data points.
- **Risk Gauges:** Custom data visualization components using thin, circular strokes to show AI safety scores, utilizing the semantic color palette for immediate visual feedback.