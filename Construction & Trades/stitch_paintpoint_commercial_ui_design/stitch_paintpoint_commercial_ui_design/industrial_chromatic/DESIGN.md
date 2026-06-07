---
name: Industrial Chromatic
colors:
  surface: '#fff8f6'
  surface-dim: '#f0d4cd'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ed'
  surface-container: '#ffe9e4'
  surface-container-high: '#ffe2db'
  surface-container-highest: '#f9dcd5'
  on-surface: '#271814'
  on-surface-variant: '#5a4139'
  inverse-surface: '#3d2c28'
  inverse-on-surface: '#ffede8'
  outline: '#8f7068'
  outline-variant: '#e3beb5'
  surface-tint: '#b02f00'
  primary: '#ac2e00'
  on-primary: '#ffffff'
  primary-container: '#d3400d'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb5a0'
  secondary: '#115cb9'
  on-secondary: '#ffffff'
  secondary-container: '#659dfe'
  on-secondary-container: '#003370'
  tertiary: '#006b24'
  on-tertiary: '#ffffff'
  tertiary-container: '#008730'
  on-tertiary-container: '#f7fff2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a0'
  on-primary-fixed: '#3b0a00'
  on-primary-fixed-variant: '#862200'
  secondary-fixed: '#d7e2ff'
  secondary-fixed-dim: '#acc7ff'
  on-secondary-fixed: '#001a40'
  on-secondary-fixed-variant: '#004491'
  tertiary-fixed: '#83fc8e'
  tertiary-fixed-dim: '#66df75'
  on-tertiary-fixed: '#002106'
  on-tertiary-fixed-variant: '#00531a'
  background: '#fff8f6'
  on-background: '#271814'
  surface-variant: '#f9dcd5'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  block-padding: 120px
---

## Brand & Style

The brand personality of the design system is authoritative, energetic, and meticulous. It is designed for a commercial painting firm that balances heavy-duty industrial capability with precision and aesthetic mastery. The target audience includes property developers, facility managers, and architects who value reliability and high-standard finishes.

The design style is a hybrid of **High-Contrast Bold** and **Modern Corporate**. It utilizes architectural "color blocking" to mimic the physical act of painting large surfaces. By using heavy-weight typography and crisp, unyielding edges, the UI evokes a sense of structural integrity and professional confidence. The interface stays out of the way of high-resolution industrial imagery, acting as a clean frame for large-scale project photography.

## Colors

The palette is built on a foundation of "Safety and Precision." 

- **Primary (Vibrant Orange):** Used for primary actions and highlights, representing safety equipment and high-visibility energy.
- **Secondary (Structural Blue):** Used for navigation and corporate elements, representing trust and the architectural nature of commercial work.
- **Tertiary (Industrial Green):** Reserved for success states, sustainability initiatives, and "ready" indicators.
- **Neutral Tones:** A range of professional greys (from slate to silver) provides a sophisticated backdrop.
- **Backgrounds:** Pure, clean white is the default state to ensure that color accents and photography "pop" with maximum contrast.

Color is applied in large, solid blocks rather than gradients to maintain the "crisp edge" aesthetic.

## Typography

The typography strategy leverages **Space Grotesk** for headlines to provide a technical, geometric edge that feels engineered. These should be set with tight letter spacing to emphasize their "structured" nature.

**Work Sans** is used for body text and labels to ensure maximum readability across technical specifications and service descriptions. It provides a grounded, neutral balance to the aggressive headline style. All labels should be highly legible, often utilizing all-caps for a blueprint-inspired look.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model on desktop (12 columns) and a **Fluid Grid** on mobile. The spacing rhythm is strictly based on an 8px base unit, ensuring every element aligns to a rigorous mathematical grid.

To achieve the "Color Block" style, sections should have significant vertical padding (`block-padding`), creating distinct "zones" of information. Gutters are kept wide to prevent the high-contrast elements from feeling cluttered. Alignment should prioritize left-justification to reinforce a sense of order and blueprints.

## Elevation & Depth

This system rejects soft shadows and ambient blurs in favor of **Structural Stacking** and **Bold Borders**. 

Depth is communicated through high-contrast layering:
- **Level 0:** Pure white background.
- **Level 1:** Light grey (`#F4F5F7`) surface areas to define content zones.
- **Level 2:** High-contrast color blocks (Primary/Secondary) that sit flush against surfaces.
- **Outlines:** Use 2px solid strokes in neutral-dark tones instead of shadows to define interactive elements like cards or inputs. This maintains the "crisp edge" requirement.

## Shapes

The shape language is strictly **Sharp (0)**. There are no rounded corners in the design system. This choice reflects the hard edges of industrial architecture, steel beams, and precision masking in professional painting. Every button, input field, and image container must have 90-degree angles to maintain the structured, professional aesthetic.

## Components

### Buttons
Primary buttons are solid blocks of the primary orange with white text, utilizing no rounding and a 2px black bottom-border for a subtle "pressed" tactile feel. Secondary buttons use heavy 2px strokes with no fill.

### Cards
Cards are defined by a 1px or 2px solid neutral border. They do not use shadows. Headlines within cards should be set in the secondary blue to create a clear hierarchy against the white background.

### Input Fields
Inputs are rectangular with a 2px grey border that shifts to the primary orange upon focus. Labels are always positioned above the field in all-caps `label-caps` style.

### Chips
Used for project categories (e.g., "Industrial," "Warehousing"). These are small, sharp-edged rectangles with solid color fills and high-contrast white text.

### Industrial Image Frames
Images should always be full-bleed within their containers. When text overlays imagery, use a solid color block behind the text rather than a gradient overlay to maintain the "structured block" theme.

### Progress Indicators
Linear bars only. Use a thick stroke (8px) for progress bars to mimic a paint stroke, utilizing the tertiary green to show completion.