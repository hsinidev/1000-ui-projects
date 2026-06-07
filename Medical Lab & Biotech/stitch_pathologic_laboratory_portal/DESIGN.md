---
name: Clinical Precision
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#424752'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#727784'
  outline-variant: '#c2c6d4'
  surface-tint: '#115cb9'
  primary: '#003f87'
  on-primary: '#ffffff'
  primary-container: '#0056b3'
  on-primary-container: '#bbd0ff'
  inverse-primary: '#acc7ff'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#3b4249'
  on-tertiary: '#ffffff'
  tertiary-container: '#535a60'
  on-tertiary-container: '#cad1d9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#acc7ff'
  on-primary-fixed: '#001a40'
  on-primary-fixed-variant: '#004491'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#dce3eb'
  tertiary-fixed-dim: '#c0c7cf'
  on-tertiary-fixed: '#151c22'
  on-tertiary-fixed-variant: '#40484e'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  tabular-nums:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is anchored in the concept of "Clinical Minimalism." It evokes the atmosphere of a high-end medical facility: sterile, efficient, and uncompromisingly accurate. The target audience—physicians, lab technicians, and hospital administrators—requires a UI that prioritizes information density without sacrificing clarity. 

The aesthetic is authoritative and functional. By utilizing a heavy emphasis on whitespace and a restrained color palette, this design system builds institutional trust. Every element serves a purpose; there is no decorative flourish that does not contribute to the speed of data interpretation or the execution of critical diagnostic workflows.

## Colors

The color strategy for this design system is strictly functional. **Laboratory Blue (#0056B3)** is used exclusively for primary actions and brand presence, signifying intelligence and reliability. **Slate (#708090)** provides the necessary contrast for secondary information and structural borders, offering a sophisticated alternative to pure black.

**Sterile White (#FFFFFF)** dominates the background to reinforce the laboratory aesthetic. To ensure accessibility and readability in high-glare environments, the system utilizes high-contrast ratios. Subtle shifts into **Tertiary Blue-Grey (#EBF2FA)** are used to demarcate different data regions or specimen processing states without breaking the "clean-room" feel.

## Typography

This design system utilizes **Inter** for its exceptional legibility and systematic structure. The typography scales are designed to handle complex medical terminology and numerical data with ease. 

A critical feature of this design system is the use of **Tabular Figures** for all lab results and turnaround times, ensuring that columns of numbers align perfectly for rapid scanning. Headlines are bold and compact to establish a clear hierarchy, while labels utilize an uppercase style with increased letter-spacing to act as "tags" for specimen metadata.

## Layout & Spacing

The layout is built on a rigorous **8px grid system**, mirroring the precision of histology slides. This design system employs a **Fixed Grid** for internal dashboard views to ensure that data visualizations and specimen tables remain in consistent, predictable locations. 

Spacing is generous to prevent "visual contamination" and to help the user focus on one data point at a time. Gutters are kept wide to clearly separate distinct analytical modules, while margins ensure that content never feels cramped against the viewport edges.

## Elevation & Depth

To maintain the sterile aesthetic, this design system avoids heavy shadows. Instead, it utilizes **Low-Contrast Outlines** and **Tonal Layering**. 

Depth is communicated through 1px borders in Slate at low opacities (10-20%) and the use of slightly off-white backgrounds for container surfaces. This "flat-plus" approach ensures that the UI feels integrated and high-precision rather than floating or amorphous. Only critical modals or "floating action" elements may use a subtle, highly-diffused 10% opacity shadow to indicate their temporary nature.

## Shapes

The shape language of this design system is disciplined and geometric. A **Soft (0.25rem)** corner radius is applied to most UI components, such as input fields and cards. This provides just enough approachable "friendliness" to be modern, while maintaining the structured, architectural feel of a professional instrument. 

Primary buttons for critical lab actions use the same radius to maintain consistency, while specialized data badges (like "Priority" or "Urgent") may use a slightly larger radius to distinguish them from interactive buttons.

## Components

### Primary Action Buttons
The "Request a Specimen Pickup" button is the most prominent element. It uses a high-contrast Laboratory Blue background with white text, utilizing a bold weight to ensure immediate visibility. Its height is increased to 48px for a larger hit-area.

### Turnaround Time (TAT) Indicators
Data visualization for TAT uses linear progress gauges. The track is a light Slate, with the progress filled in Laboratory Blue. If a specimen is past its TAT threshold, the indicator shifts to a high-visibility Status Red to prompt immediate action.

### Input Fields & Selectors
Inputs are defined by a 1px Slate border. On focus, the border thickens slightly and transitions to Laboratory Blue. Labels always sit above the input field to ensure clarity when the field is filled.

### Specimen Cards
Cards are used to display individual patient cases. They feature a clean 1px border and use the "Label-Caps" typography for metadata (e.g., CASE ID, ACCESSION DATE).

### High-Precision Chips
Chips used for "Pending," "Processing," and "Completed" statuses utilize low-saturation background tints of their respective status colors to remain readable without becoming visually overwhelming.