---
name: Herpetological Utility Interface
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#594139'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#8d7167'
  outline-variant: '#e1bfb4'
  surface-tint: '#a93700'
  primary: '#973100'
  on-primary: '#ffffff'
  primary-container: '#c04000'
  on-primary-container: '#ffe9e3'
  inverse-primary: '#ffb59b'
  secondary: '#3f6833'
  on-secondary: '#ffffff'
  secondary-container: '#bdedaa'
  on-secondary-container: '#436d37'
  tertiary: '#465569'
  on-tertiary: '#ffffff'
  tertiary-container: '#5f6d83'
  on-tertiary-container: '#e7efff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59b'
  on-primary-fixed: '#380d00'
  on-primary-fixed-variant: '#812800'
  secondary-fixed: '#c0f0ad'
  secondary-fixed-dim: '#a4d393'
  on-secondary-fixed: '#022100'
  on-secondary-fixed-variant: '#28501e'
  tertiary-fixed: '#d5e3fd'
  tertiary-fixed-dim: '#b9c7e0'
  on-tertiary-fixed: '#0d1c2f'
  on-tertiary-fixed-variant: '#3a485c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-main:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  body-compact:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
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
  unit-1: 0.25rem
  unit-2: 0.5rem
  unit-4: 1rem
  unit-6: 1.5rem
  gutter: 16px
  margin: 24px
  max-width: 1440px
---

## Brand & Style
The design system is engineered for the specialist—herpetologists, professional breeders, and dedicated hobbyists. It prioritizes high-utility over decorative flourishes, evoking the feel of a laboratory instrument or a precision field kit. 

The visual style is **Modern / Corporate** with a heavy emphasis on **High-Density Data**. It utilizes a structured grid and crisp containment to organize complex environmental variables. The emotional response is one of reliability, precision, and clinical expertise. Interaction states are clear and binary, mirroring the technical nature of habitat management and biological tracking.

## Colors
The palette is grounded in an "Earth-Technical" aesthetic. 

- **Terracotta (#C04000)**: Reserved for primary call-to-actions, critical biological alerts, and heat-related indicators. Its high energy signals importance against the neutral backdrop.
- **Moss Green (#4F7942)**: Used for secondary actions, confirmation states, and "Optimal" status indicators for health and humidity.
- **Slate Grays**: Utilized for the structural framework, borders, and secondary text to maintain a professional, de-saturated environment.
- **Off-Whites**: Used for background surfaces to reduce eye strain during long sessions of data entry or monitoring.

## Typography
The system employs a dual-font strategy to separate narrative UI from technical telemetry. 

**Inter** provides a highly legible, neutral foundation for all navigation, form labels, and general interface text. Its high x-height ensures readability in high-density layouts. 

**Space Grotesk** is used exclusively for numeric data points, telemetry (temperature, humidity, weight), and technical identifiers. The geometric, monospaced nature of the font ensures that changing values do not cause layout shifts and provides a "scientific instrument" aesthetic to the data cards.

## Layout & Spacing
The design system utilizes a **Fixed Grid** model for desktop dashboards and a fluid 1-column stack for mobile devices. 

- **Grid**: A 12-column grid with 16px gutters allows for flexible data-heavy layouts. 
- **Density**: The spacing rhythm is tight (4px base) to maximize information density, allowing specialists to view multiple habitats or species on a single screen without excessive scrolling.
- **Alignment**: All elements align to a strict vertical and horizontal rhythm. Data columns in tables must use tabular figures and right-alignment for numerical comparison.

## Elevation & Depth
Depth is achieved through **Tonal Layering** and **Crisp Borders** rather than aggressive shadows. 

1. **Base Level**: The background is the neutral off-white.
2. **Surface Level**: Cards and containers use a pure white background with a 1px border (#E2E8F0).
3. **Interactive Level**: Buttons and active toggles use a subtle 2px bottom "drop" shadow with 5% opacity to indicate pressability.
4. **Overlay Level**: Modals and dropdowns use a sharp 4px shadow with 10% opacity, maintaining the technical, clean-edged look.

Avoid the use of blurs or gradients; depth should feel structural and mechanical.

## Shapes
The shape language is **Soft (0.25rem)**. This slight rounding takes the "edge" off the technical data without making the UI feel overly consumer-grade or playful. 

- **Inputs & Small Buttons**: 4px radius.
- **Data Cards**: 8px (rounded-lg) to provide clear visual containment for grouped metrics.
- **Status Tags**: Semi-pill (rounded-xl) to distinguish them from interactive buttons.
- **Charts/Sparklines**: Use 2px stroke widths with no smoothing on data points to emphasize raw accuracy.

## Components
- **Buttons**: Primary buttons are solid Terracotta with white text. Secondary buttons are outlined in Moss Green or Slate Gray.
- **Data Cards**: Feature a headline, a primary Mono-spaced metric (e.g., 88°F), and a background sparkline showing the 24-hour trend.
- **Control Panels**: Heavy use of custom toggle switches for hardware control (lights, misters, heat mats). Toggles show a Moss Green "on" state.
- **Input Fields**: Crisp, rectangular fields with 1px borders. Focus states use a 2px Terracotta outline.
- **Icon-based Nav**: Thin-line icons (1.5px stroke) representing species (Serpentes, Sauria, Testudines) or system functions (Climate, Feeding, Logs).
- **Status Badges**: Small, high-contrast badges used within lists to indicate "In Shed," "Gravid," or "Feeding Required."
- **Sparklines**: Integrated into list rows and cards to provide context without taking up dedicated chart space.