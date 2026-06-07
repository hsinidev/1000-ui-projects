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
  on-surface-variant: '#434653'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#2559bd'
  primary: '#00327d'
  on-primary: '#ffffff'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#b1c5ff'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#33373a'
  on-tertiary: '#ffffff'
  tertiary-container: '#4a4e51'
  on-tertiary-container: '#bcbfc2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c3c7ca'
  on-tertiary-fixed: '#181c1e'
  on-tertiary-fixed-variant: '#43474a'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: '0'
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: -0.01em
---

## Brand & Style

The design system is engineered for the intersection of biotechnology and high-stakes law. The brand personality is authoritative, cold, and meticulously accurate. It aims to evoke the emotional response of a sterile laboratory environment—where every detail is scrutinized and compliance is absolute. 

The visual style is a hybrid of **Minimalism** and **Technical/Brutalist** influences. It prioritizes clarity over ornamentation, utilizing a strict structural framework to convey reliability. Visual elements are reduced to their functional essence, emphasizing that in the world of bio-legalities, there is no room for ambiguity. The aesthetic is "medical-grade," suggesting a platform that is as much a specialized tool as it is an information resource.

## Colors

The palette for this design system is intentionally restricted to maintain a sterile, clinical atmosphere. **Sterile White** serves as the primary canvas, providing maximum contrast and a sense of cleanliness. **Laboratory Blue** is reserved for primary actions and brand-critical indicators, signifying trust and scientific depth. 

**Silver** is utilized for structural elements, hairline borders, and secondary metadata, creating a metallic, high-tech feel. For status indicators, we use highly saturated, standard-compliant tones that stand out against the monochrome background without compromising the professional integrity of the UI.

## Typography

Typography is used as a tool for hierarchy and information density. **Space Grotesk** is chosen for headlines and labels to provide a geometric, technical "engineered" feel. Its unique letterforms suggest innovation and scientific precision.

**Inter** is utilized for all body copy and long-form legal text. Its neutral, systematic design ensures maximum legibility during intense periods of document review. To emphasize compliance and technical categorization, a "Label Caps" style is used for section headers and metadata. This design system treats text as data; therefore, alignment and line height are strictly enforced to maintain a rhythmic, grid-based reading experience.

## Layout & Spacing

This design system employs a **Fixed Grid** model. The layout is structured on a 12-column grid with a 4px base unit, ensuring every element is mathematically aligned. Consistency in spacing is paramount to convey the "Clinical" aesthetic.

Horizontal rhythm is dictated by the 24px gutter, while vertical rhythm is maintained through standardized "stack" units. High margins (48px+) are used to frame content, creating a sense of focus and eliminating visual clutter. Layouts should prioritize top-down hierarchy, using whitespace not just for aesthetics, but as a functional separator between complex legal clauses and data points.

## Elevation & Depth

Depth in this design system is achieved through **Low-contrast outlines** and tonal layering rather than traditional shadows. Shadows are largely avoided to maintain a flat, technical document feel. 

When separation is required, use 1px Silver (#C0C0C0) borders or subtle shifts in background tone (moving from #FFFFFF to #F4F7FA). For modal overlays or high-priority alerts, a "Systematic Stack" approach is used: elements do not "float," they are placed on a higher logical plane indicated by a single, sharp 1px border with a slightly darker neutral tint. This reinforces the perception of the UI as a precise instrument.

## Shapes

The shape language of this design system is strictly **Sharp (0px)**. All containers, buttons, and input fields must have square corners. This zero-radius approach reinforces the "Clinical & Precise" aesthetic, echoing the sharpness of medical instruments and the rigidity of legal frameworks. 

The use of 90-degree angles ensures that the UI feels architectural and structural. Circular shapes are permitted only for specific status pips or specialized iconography where a round form is technically required (e.g., a "live" recording indicator or biological cell representation).

## Components

### Buttons
Buttons are rectangular with sharp 0px corners. The primary button uses a solid Laboratory Blue background with White text. Secondary buttons utilize a 1px Silver border with Blue or Black text. Hover states must be a simple shift in value (darker blue) without any transition animation—action and response should be instantaneous and precise.

### Input Fields
Inputs are defined by a 1px Silver bottom-border or full-border depending on context. Labels use the `label-caps` style and sit strictly above the input. Focus states are indicated by a change in border color to Laboratory Blue.

### Cards & Containers
Cards do not use shadows. They are defined by a 1px #E1E4E8 border. For high-density data, use "Divided Lists" where each row is separated by a 1px Silver hairline.

### Iconography
Icons must be monolinear, 1.5px stroke width, and adhere to a strict 24x24px grid. They should mimic technical drawings or medical diagrams. Avoid "friendly" or rounded icon sets.

### Data Tables
In a bio-legal context, tables are critical. They should feature "Sticky Headers" in Laboratory Blue or Silver, with high-contrast cell text. Use alternating row tints (#F4F7FA) only when necessary for extreme horizontal data sets.

### Compliance Badges
Status indicators for legal compliance should be small, rectangular chips using the `label-caps` typography, with background colors mapped to success, warning, or error states.