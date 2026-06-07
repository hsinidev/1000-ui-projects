---
name: Glacial Precision
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#404753'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#707785'
  outline-variant: '#c0c7d5'
  surface-tint: '#0060ab'
  primary: '#005da7'
  on-primary: '#ffffff'
  primary-container: '#0076d1'
  on-primary-container: '#fdfcff'
  inverse-primary: '#a3c9ff'
  secondary: '#516072'
  on-secondary: '#ffffff'
  secondary-container: '#d2e1f7'
  on-secondary-container: '#556477'
  tertiary: '#565d63'
  on-tertiary: '#ffffff'
  tertiary-container: '#6f757c'
  on-tertiary-container: '#fcfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e3ff'
  primary-fixed-dim: '#a3c9ff'
  on-primary-fixed: '#001c39'
  on-primary-fixed-variant: '#004883'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base-unit: 8px
  gutter: 24px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

The design system is engineered to evoke the sensation of controlled thermal environments—crisp, clean, and perfectly regulated. It serves a primary audience of HVAC engineers and facility managers who require high-density data visualization without cognitive overload. 

The aesthetic is a fusion of **Minimalism** and **Glassmorphism**, specifically tailored into a "Frost" style. By utilizing translucency and subtle background blurs, the interface feels lightweight and layered rather than heavy or cluttered. The visual narrative emphasizes transparency and "airiness," mimicking the properties of air and cooling systems. Every element is governed by mathematical precision, ensuring that the technical complexity of the mechanical data is balanced by a serene, professional atmosphere.

## Colors

The palette is rooted in the "Frost" concept, using temperature-coded neutrals and cool accents. 

- **Primary (Active Ice):** A vibrant blue used sparingly for interactive states, key data highlights, and active status indicators.
- **Secondary (Silver):** Used for structural elements, inactive states, and secondary iconography to provide a metallic, engineered feel.
- **Tertiary (Slate Grey):** Reserved for technical text and data labels to ensure high contrast against the lighter "ice" backgrounds.
- **Surface Gradients:** The "Frost" effect is achieved through linear gradients transitioning from a highly desaturated Ice Blue to a pure, translucent white.

The default color mode is light, maximizing the "airy" quality of the design system and allowing the glass effects to appear more natural and refreshing.

## Typography

This design system utilizes **Inter** for its entire type scale. Inter provides the neutral, systematic clarity required for high-precision engineering software. 

The typographic hierarchy is structured to prioritize legibility of numerical values. For technical readouts and sensor data, the "data-mono" style leverages Inter's tabular lining features to ensure that fluctuating numbers do not cause layout shifts. Headlines are set with tighter letter spacing to maintain a compact, "engineered" look, while body copy utilizes generous line heights to preserve the airy feel of the overall aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** system based on an 8px spatial rhythm. This ensures that technical dashboards can scale across various monitor sizes while maintaining a strict structural alignment.

Components are organized within a 12-column grid. To maintain the "airy" aesthetic, padding within technical cards is generous (24px or 32px), preventing data points from feeling cramped. Negative space is used strategically to group related sensor clusters, reducing the need for heavy dividers.

## Elevation & Depth

In this design system, depth is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces are layered using "frost" techniques:

1.  **Backdrop Blur:** All container surfaces apply a 16px to 24px blur to the content beneath them.
2.  **Translucency:** Backgrounds use semi-transparent white or ice-blue fills (60-80% opacity).
3.  **Frost Borders:** A 1px solid border in a semi-transparent bright white (50% opacity) is applied to the top and left edges to simulate a light source catching the edge of a glass pane.
4.  **Tonal Stacking:** Higher-priority elements (like tooltips or active modal windows) use a slightly higher opacity and a more pronounced white border to appear "closer" to the user.

## Shapes

The shape language is defined by **Rounded** geometry (0.5rem base radius). This specific level of roundedness softens the technical nature of the HVAC data, making the interface feel modern and approachable without losing the sense of professional precision associated with sharp-edged engineering drawings. 

Internal elements like status pips and small toggle switches use circular or pill shapes to distinguish them from the structural rectangular cards.

## Components

### Technical Cards
The foundational element of the design system. Cards use the "Frost" effect with a 1px internal white border. Headers within cards are separated by a subtle 1px silver line at 20% opacity.

### High-Precision Charts
Charts utilize thin line weights (1.5px) and soft area gradients that fade into transparency. Data points feature "glow" effects when hovered, utilizing the Primary Blue color. Grid lines in charts are Slate Grey with 10% opacity to remain unobtrusive.

### Status Indicators
Indicators use a "LED" metaphor. Instead of flat circles, they use a soft radial gradient with a glow effect (filter: drop-shadow) to indicate active machinery or alert states.
- **Normal:** Ice Blue Glow
- **Warning:** Amber Glow (Softened)
- **Critical:** Crisp Red Glow

### Buttons
Primary buttons are solid Ice Blue with a subtle inner white glow on the top edge. Secondary buttons use a "Ghost Glass" style: no fill, with a 1px white border and a backdrop blur, becoming semi-opaque on hover.

### Input Fields
Inputs are styled as recessed glass panes, using a slightly darker translucent fill than the cards they sit on, creating a "carved" effect that guides the user's eye to data entry points.