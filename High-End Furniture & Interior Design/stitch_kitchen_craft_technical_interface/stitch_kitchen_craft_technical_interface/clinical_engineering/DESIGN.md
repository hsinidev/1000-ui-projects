---
name: Clinical Engineering
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
  on-surface-variant: '#44474a'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#75777a'
  outline-variant: '#c5c6ca'
  surface-tint: '#5d5e61'
  primary: '#000101'
  on-primary: '#ffffff'
  primary-container: '#1a1c1e'
  on-primary-container: '#838486'
  inverse-primary: '#c6c6c9'
  secondary: '#5b5f63'
  on-secondary: '#ffffff'
  secondary-container: '#e0e2e8'
  on-secondary-container: '#616569'
  tertiary: '#000001'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e5'
  primary-fixed-dim: '#c6c6c9'
  on-primary-fixed: '#1a1c1e'
  on-primary-fixed-variant: '#454749'
  secondary-fixed: '#e0e2e8'
  secondary-fixed-dim: '#c4c6cc'
  on-secondary-fixed: '#181c20'
  on-secondary-fixed-variant: '#44474b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  grid-unit: 8px
  gutter: 24px
  margin: 64px
  table-cell-padding: 12px
  layout-max-width: 1440px
---

## Brand & Style

This design system is built upon the principles of industrial precision and surgical cleanliness. It targets high-end culinary professionals and homeowners who value the technical "spec-sheet" beauty of a professional kitchen. The UI evokes the feeling of an architectural blueprint or a high-end appliance interface: cold, efficient, and impeccably organized.

The visual style is a hybrid of **Minimalism** and **Brutalism**, refined with a high-tech finish. It utilizes a rigorous engineering-grade grid to convey stability, while generous whitespace ensures that the high-resolution imagery of bespoke cabinetry and stainless steel remains the focal point. Every interaction must feel intentional, reinforcing the brand's commitment to bespoke craftsmanship and technical excellence.

## Colors

The palette is strictly monochromatic, drawing inspiration from high-grade alloys and stone surfaces. 

- **Bright White (#FFFFFF):** Used for the primary "sterile" background to maximize contrast.
- **Stainless Steel (#D1D5DB to #8E9196):** Applied through subtle linear gradients to simulate brushed metal textures on interactive elements.
- **Slate (#1A1C1E):** Reserved for deep contrast, technical labels, and heavy structural borders.
- **Clinical Green (#00FF41):** A high-visibility accent used sparingly for "ready" states or precise data points within technical tables.

All grays are cool-toned to maintain a "refrigerated" aesthetic. Avoid any warm hues (yellows/reds) unless indicating a critical error.

## Typography

This design system employs a strict typographic hierarchy. **Inter** provides the functional clarity required for body copy and navigation, while **Space Grotesk** is introduced for technical data, measurements, and labels to evoke an engineering aesthetic.

All labels should be set in uppercase with increased letter spacing to mimic industrial stamping or blueprint notations. Headlines are tightly tracked and bold, creating a sense of density and strength. Use monochromatic variations (Slate for text, Stainless for sub-captions) to differentiate information without breaking the clinical theme.

## Layout & Spacing

The layout is governed by a **Fixed 12-column grid** centered on the screen, reflecting the precision of a floor plan. 

- **Engineering Grid:** Every element must align to a strict 8px baseline. 
- **Gutters:** 24px gutters ensure breathing room between technical specs.
- **Margins:** Large 64px outer margins reinforce a premium, gallery-like feel.
- **Visual Rhythm:** Use spacing to group related technical data. For example, a kitchen module's dimensions, materials, and BTU ratings should be tightly packed, while the distance between different modules remains generous.

## Elevation & Depth

This design system rejects traditional shadows in favor of **Structural Depth**. 

- **Bold Borders:** Use 1px or 2px solid Slate (#1A1C1E) lines to define containers and zones. This creates a "blueprint" feel where every component has a clearly defined footprint.
- **Tonal Layers:** Elevation is communicated by switching between Bright White and ultra-light cool grays (#F8F9FA). A "raised" element doesn't cast a shadow; it simply gains a hairline metallic border and a subtle top-to-bottom brushed gradient.
- **Precision Insets:** Active states (like a clicked button or a selected field) should appear "pressed" into the surface using a slightly darker inner border rather than a drop shadow.

## Shapes

The shape language is unapologetically **Sharp (0)**. There are no rounded corners in this design system. 

The use of 90-degree angles mirrors the cabinetry, appliances, and countertops being showcased. Rectangular frames define the high-resolution image galleries. Buttons, input fields, and even hover states must maintain these hard edges to reinforce the clinical, engineered theme. Any deviation into rounded corners would soften the professional tone and is strictly prohibited.

## Components

### Buttons & Inputs
Buttons are rectangular with a 1px Slate border. Primary buttons feature a subtle vertical linear gradient from #E5E7EB to #D1D5DB (Stainless Steel). Input fields use a Bright White background with a "Label Caps" typography style floating precisely above the top-left border.

### Technical Data Tables
Tables are the backbone of the technical interface. Use 1px hairline dividers between all rows and columns. Headers should be Slate with White "Label Caps" text. Use the "data-mono" font for all numerical values, ensuring they align to the decimal point for professional readability.

### Interactive Layout Tools
Grid-based canvases for kitchen planning should feature a subtle 8px dot-matrix background. Drag-and-drop modules must be outlined in the accent Metallic color during movement, snapping to the grid with zero-latency visual feedback.

### Image Galleries
High-resolution images are framed in heavy 4px Slate borders. Captions are positioned in the bottom-right corner of the image, appearing as a "Technical Plate" using the Slate color and "label-caps" typography.

### Status Indicators
Small, square pips using "Clinical Green" signify "In Stock" or "Validated Dimension." These are the only non-monochromatic elements allowed in the component library.