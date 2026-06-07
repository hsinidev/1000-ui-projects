---
name: Industrial Stewardship
colors:
  surface: '#f7faf9'
  surface-dim: '#d7dbda'
  surface-bright: '#f7faf9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f3'
  surface-container: '#ebeeed'
  surface-container-high: '#e6e9e8'
  surface-container-highest: '#e0e3e2'
  on-surface: '#181c1c'
  on-surface-variant: '#3e4a3c'
  inverse-surface: '#2d3131'
  inverse-on-surface: '#eef1f0'
  outline: '#6e7b6b'
  outline-variant: '#bdcab9'
  surface-tint: '#006e25'
  primary: '#006e25'
  on-primary: '#ffffff'
  primary-container: '#28a745'
  on-primary-container: '#00330d'
  inverse-primary: '#66df75'
  secondary: '#4e6073'
  on-secondary: '#ffffff'
  secondary-container: '#cfe2f9'
  on-secondary-container: '#526478'
  tertiary: '#006877'
  on-tertiary: '#ffffff'
  tertiary-container: '#11a0b6'
  on-tertiary-container: '#003038'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#83fc8e'
  primary-fixed-dim: '#66df75'
  on-primary-fixed: '#002106'
  on-primary-fixed-variant: '#00531a'
  secondary-fixed: '#d1e4fb'
  secondary-fixed-dim: '#b5c8df'
  on-secondary-fixed: '#091d2e'
  on-secondary-fixed-variant: '#36485b'
  tertiary-fixed: '#a4eeff'
  tertiary-fixed-dim: '#62d6ed'
  on-tertiary-fixed: '#001f25'
  on-tertiary-fixed-variant: '#004e5a'
  background: '#f7faf9'
  on-background: '#181c1c'
  surface-variant: '#e0e3e2'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
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
    fontWeight: '700'
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
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 20px
  container-max: 1440px
---

## Brand & Style
The ethos of this design system is "Industrial Stewardship." It bridges the gap between heavy-duty municipal operations and environmental responsibility. The UI must feel like a precision tool—reliable, resilient, and authoritative. 

We utilize a **High-Contrast / Bold** style influenced by modern architectural wayfinding. The aesthetic prioritizes rapid information retrieval and operational clarity. By stripping away decorative flourishes and focusing on structural integrity, the design system evokes a sense of efficiency and civic duty. It is designed for users who manage complex logistics and require a "no-nonsense" interface that performs under high-pressure, data-heavy environments.

## Colors
The palette is rooted in functional realism. **Leaf Green** serves as the primary action color, symbolizing growth and ecological health; it is used exclusively for primary "go" actions and successful system statuses. **Charcoal** provides the structural depth, used for typography and heavy borders to ensure maximum legibility and a grounded, industrial feel. 

Backgrounds utilize a sterile **White** or a very light cool-gray to keep the workspace clean and focused. Status colors follow a strict high-contrast convention: vibrant ambers for caution and signal reds for system alerts, ensuring they are unmistakable against the charcoal-and-white framework.

## Typography
This design system employs **Inter** for its exceptional legibility and systematic performance. Headlines use a heavy weight and tight letter-spacing to mimic industrial signage and give the interface a "robust" presence. 

For data-heavy views, we utilize "tabular num" settings to ensure columns of figures align perfectly, maintaining the grid's integrity. Labels are frequently set in uppercase with slight tracking to distinguish them from interactive body text, creating a clear hierarchy between metadata and actionable content.

## Layout & Spacing
The layout follows a **fixed-fluid hybrid grid**. Main dashboard containers are capped for readability, while data tables and monitoring maps are allowed to span the full width of the viewport. We use an 8px base unit (with a 4px half-step for tight data density) to ensure every element feels mathematically aligned.

The layout philosophy emphasizes "Information Density without Clutter." Sidebars are collapsible to prioritize the workspace, and modular "cards" use consistent 24px margins to create a rhythmic, structured flow.

## Elevation & Depth
In keeping with the industrial aesthetic, this design system avoids soft, ambient shadows. Depth is instead communicated through **Tonal Layers** and **Bold Borders**. 

We use a 1px or 2px Charcoal border to define interactive containers. Elevation is achieved by shifting background values—for example, a "raised" card will sit on a slightly lighter gray background than the main canvas. When shadows are necessary for critical overlays (like modals), they are sharp and high-opacity, emphasizing a physical "stacking" effect rather than a digital glow.

## Shapes
The shape language is "Functional-Soft." We use a 4px (`0.25rem`) corner radius as the standard for all buttons, input fields, and containers. This slight rounding prevents the UI from feeling aggressive or dated while maintaining the "machined" look of industrial hardware. Larger components like cards use an 8px radius to subtly distinguish them from smaller UI controls.

## Components
### Buttons
Primary buttons are solid Leaf Green with White text, using bold weights. Secondary buttons utilize a Charcoal border with no fill. All buttons feature a 2px offset focus state for accessibility.

### Waste Type Icons
Icons must be high-contrast and encapsulated in geometric containers. Use specific color-coding for waste streams: Blue for paper/cardboard, Yellow for plastics, Green for organics, and Charcoal for general landfill.

### Data-Dense Charts
Charts should utilize the primary and secondary colors, avoiding gradients. Use hairline strokes and "Inter" in its tabular-number format for all axes and legends. Interaction states (hover/tooltips) should be instantaneous and use high-contrast Charcoal backgrounds.

### Municipal-Grade Inputs
Form fields use a thick 2px Charcoal border when focused. Error states use a high-visibility Red border with a corresponding icon. Labels sit outside the field to ensure they are always visible during data entry.

### Status Indicators
Status chips are rectangular with a solid color bar on the left edge. This provides a "military-grade" classification look that is easily scannable in long lists.