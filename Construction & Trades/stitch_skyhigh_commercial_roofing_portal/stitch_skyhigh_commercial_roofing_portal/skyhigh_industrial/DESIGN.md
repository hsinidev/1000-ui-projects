---
name: SkyHigh Industrial
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e0'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f9'
  surface-container: '#efedf3'
  surface-container-high: '#e9e7ee'
  surface-container-highest: '#e3e2e8'
  on-surface: '#1a1b20'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3035'
  inverse-on-surface: '#f1f0f6'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#121515'
  on-tertiary: '#ffffff'
  tertiary-container: '#272929'
  on-tertiary-container: '#8f9090'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#faf8ff'
  on-background: '#1a1b20'
  surface-variant: '#e3e2e8'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
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
    lineHeight: '1.6'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The design system is built on the pillars of structural integrity, precision, and urgency. It targets commercial property managers and industrial developers who value reliability and technical expertise. The aesthetic is "Technical Minimalism"—a style that prioritizes clarity and high-contrast legibility over decorative elements. 

The visual language utilizes sharp geometric shapes and a restricted palette to evoke a sense of architectural blueprints and industrial engineering. By stripping away soft shadows and rounded corners, this design system establishes a high-trust, authoritative presence that communicates durability and "zero-error" performance.

## Colors
The palette is rooted in Royal Blue to symbolize corporate stability and professionalism. Graphite is utilized for primary text and structural borders, providing a softer but still high-contrast alternative to pure black. White is the primary canvas, ensuring maximum "breathability" and a clean, sterile environment for technical data.

An auxiliary Emergency Red is introduced specifically for critical service triggers, maintaining high visibility against the neutral and blue backgrounds. All interactions must pass WCAG AAA contrast ratios to ensure accessibility in high-glare outdoor environments often encountered by field specialists.

## Typography
Inter is selected for its exceptional legibility and neutral, utilitarian character. The type system employs a tight scale with generous line heights for body copy to ensure technical reports are easy to scan. 

Headlines use a bold weight and slight negative letter-spacing to appear "dense" and structured, like industrial signage. Labels and small metadata should utilize uppercase styling with increased letter spacing to differentiate technical specs from standard prose.

## Layout & Spacing
This design system employs a rigid 8px grid system. Layouts are strictly aligned to a 12-column fixed grid for desktop, ensuring that information is segmented into logical, digestible modules. 

The "Rule of Alignment" is paramount: all elements must snap to the grid to maintain the "Technical" aesthetic. Vertical rhythm is established through 48px and 80px section padding, creating clear separation between different service tiers or technical case studies.

## Elevation & Depth
Depth is conveyed through **Bold Borders** and **Tonal Layering** rather than shadows. Surfaces are kept flat to reinforce the "sharp edge" philosophy. 

1.  **Level 0 (Base):** White (#FFFFFF) background.
2.  **Level 1 (Sub-section):** Graphite (#383838) or Royal Blue (#002366) containers with white text.
3.  **Borders:** 2px solid borders in Graphite are used to define interactive cards and input fields.
4.  **Overlays:** High-contrast modal overlays use a 90% opacity Graphite fill to maintain focus on the technical content.

## Shapes
The shape language is strictly orthogonal. All buttons, cards, and input fields feature 0px border radius (Sharp). This reinforces the brand's connection to industrial roofing materials and structural beams. Diagonal lines (45-degree angles) may be used sparingly in iconography or section dividers to imply "High" elevation or roof pitches, but containers must always remain rectangular.

## Components

### Buttons & Inputs
Buttons use 2px solid strokes or solid fills. The **Primary Button** is a solid Royal Blue block with White uppercase text. The **Secondary Button** is a Graphite outline. All input fields must have a 2px Graphite border that thickens to 3px on focus.

### High-Contrast Navigation
The navigation utilizes a "Command Center" approach: large, thick-stroke icons (2.5pt stroke weight) paired with `label-bold` typography. Active states are indicated by a solid Royal Blue bottom-bar (4px thick) rather than a color change of the icon itself.

### Sticky Emergency Button
The "Emergency Leak Response" button is a persistent UI element. 
- **Style:** Fixed position (bottom-right), solid Red (#D32F2F) background.
- **Shape:** Rectangular (Sharp), not circular.
- **Content:** A "Flash" or "Warning" icon followed by "EMERGENCY REPAIR". 
- **Animation:** A subtle, 2-second interval pulse of the border weight (not the opacity) to draw attention without appearing unprofessional.

### Technical Cards
Cards for roofing systems or project specs use a 1px Graphite border. Headers within cards should have a light grey (#F5F5F5) background to separate the "Label" area from the "Data" area.