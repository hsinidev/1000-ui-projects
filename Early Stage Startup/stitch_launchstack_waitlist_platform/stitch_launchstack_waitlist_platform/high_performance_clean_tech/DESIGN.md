---
name: High-Performance Clean-Tech
colors:
  surface: '#fbf8ff'
  surface-dim: '#d9d9e7'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f2ff'
  surface-container: '#ededfb'
  surface-container-high: '#e7e7f5'
  surface-container-highest: '#e1e1ef'
  on-surface: '#191b25'
  on-surface-variant: '#434656'
  inverse-surface: '#2e303a'
  inverse-on-surface: '#f0effe'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004ced'
  primary: '#003ec7'
  on-primary: '#ffffff'
  primary-container: '#0052ff'
  on-primary-container: '#dfe3ff'
  inverse-primary: '#b7c4ff'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#952200'
  on-tertiary: '#ffffff'
  tertiary-container: '#bf3003'
  on-tertiary-container: '#ffddd5'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b7c4ff'
  on-primary-fixed: '#001452'
  on-primary-fixed-variant: '#0038b6'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#ffdbd2'
  tertiary-fixed-dim: '#ffb4a1'
  on-tertiary-fixed: '#3c0800'
  on-tertiary-fixed-variant: '#891e00'
  background: '#fbf8ff'
  on-background: '#191b25'
  surface-variant: '#e1e1ef'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  button:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  container-max: 1280px
---

## Brand & Style

This design system is engineered for **LaunchStack**, a SaaS tool that demands an atmosphere of precision, velocity, and reliability. The aesthetic is rooted in **Minimalism** with a **Tech-Forward** edge, utilizing high-contrast visuals to guide users toward conversion.

The brand personality is professional and elite, catering to developers and founders who value efficiency over decoration. The emotional response should be one of "industrial clarity"—where every pixel serves a functional purpose. The UI utilizes expansive white space to reduce cognitive load, while sharp borders and a focused palette create a disciplined, high-performance environment.

## Colors

The palette is strictly limited to ensure maximum impact for conversion elements. 

- **Primary (Electric Blue):** Used exclusively for high-priority actions, interactive states, and critical data points. It represents energy and the "launch" phase.
- **Secondary (Slate/Navy):** Used for primary text and deep-contrast accents. It provides the "anchor" for the design.
- **Background (Pure White):** All surfaces begin at #FFFFFF to maintain a clinical, clean-tech feel.
- **Neutral/Borders (Slate-200):** Used for structural definition and subtle iconography.

Avoid gradients. Use solid fills to maintain the sharp, high-contrast integrity of the design.

## Typography

The typography system relies on **Inter**, a high-performance sans-serif designed for screen readability. 

Headlines utilize tight tracking and heavy weights to command attention, mirroring the "Bold/Minimalist" style. Body copy is optimized for clarity with generous line heights. The system includes a specific `label-caps` style for metadata and small headers to maintain a technical, "instrument-panel" aesthetic. All type should be rendered with `antialiased` smoothing for a premium feel.

## Layout & Spacing

This design system uses a **12-column fixed grid** for desktop, centered within the viewport. The layout philosophy is built on an **8pt grid system**, ensuring consistent vertical rhythm.

Whitespace is used as a structural tool rather than a luxury. High-conversion sections (like the waitlist signup) are isolated with `xl` (40px) or greater margins to draw focus. Gutters are kept tight at 24px to maintain a sense of technical density and precision.

## Elevation & Depth

To maintain the "Clean-Tech" aesthetic, elevation is achieved primarily through **Low-contrast outlines** rather than heavy shadows. 

- **Surface Layer:** All main content sits on a pure white background.
- **Sectioning:** Use 1px solid borders in Slate-200 to separate modules.
- **Interactive Depth:** Only the primary CTAs and active cards may use a very subtle, tight shadow (0px 2px 4px rgba(15, 23, 42, 0.05)) to suggest "lift." 
- **Z-Index:** Modals and dropdowns use a sharp 1px border and a medium ambient shadow to appear floating over the grid without breaking the minimalist feel.

## Shapes

The shape language is defined by **Precision**. 

We use a "Soft" roundedness level (0.25rem/4px) which provides just enough comfort to be modern while remaining sharp and "engineered." Circles are used only for status indicators or avatars. All structural elements—buttons, input fields, and cards—must adhere to the 4px radius to ensure a cohesive, architectural look across the entire application.

## Components

### Buttons
- **Primary:** Solid Electric Blue fill, White text. No border. High-contrast hover state (slight darken).
- **Secondary:** White fill, 1px Slate-200 border, Slate-900 text.
- **Size:** Large (48px height) for main CTAs to ensure high conversion.

### Input Fields
- **Default:** White background, 1px Slate-200 border, Slate-400 placeholder.
- **Focus:** 1px Electric Blue border with a 2px soft blue outer glow. 
- **Labels:** Use the `label-caps` typography style positioned strictly above the field.

### Cards & Containers
- Minimalist containers with 1px Slate-200 borders. No background tint. 
- Use internal padding of `lg` (24px) for data visualizations.

### Data Visualizations
- Charts should use Electric Blue for the primary data series and Slate-200 for grid lines. 
- Avoid area fills; use clean, 2px stroke lines to emphasize precision.

### Chips & Badges
- Used for status (e.g., "Active," "Verified"). Small 2px radius, light gray background, Slate-700 text. Small, centered, and unobtrusive.