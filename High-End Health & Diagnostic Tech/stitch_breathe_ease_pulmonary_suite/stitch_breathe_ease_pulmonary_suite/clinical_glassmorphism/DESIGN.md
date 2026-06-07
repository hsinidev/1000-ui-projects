---
name: Clinical Glassmorphism
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
  on-surface-variant: '#3e4850'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6e7881'
  outline-variant: '#bdc8d1'
  surface-tint: '#00658d'
  primary: '#00658d'
  on-primary: '#ffffff'
  primary-container: '#00aeef'
  on-primary-container: '#003e58'
  inverse-primary: '#82cfff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#595f66'
  on-tertiary: '#ffffff'
  tertiary-container: '#9ea4ab'
  on-tertiary-container: '#343a40'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c6e7ff'
  primary-fixed-dim: '#82cfff'
  on-primary-fixed: '#001e2d'
  on-primary-fixed-variant: '#004c6b'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
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
    lineHeight: '1.5'
  label-md:
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
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  card-padding: 32px
---

## Brand & Style

This design system is built for the high-precision world of pulmonary diagnostics, balancing the sterile requirements of a medical environment with the airy, lightweight feel of modern smart technology. The aesthetic centers on "breathable space"—utilizing transparency and depth to prevent the interface from feeling heavy or clinical in a restrictive sense. 

The style utilizes a sophisticated **Glassmorphism** approach. By layering translucent surfaces over soft, shifting backgrounds, the UI maintains a high-end, futuristic feel that remains approachable and human. The core personality is professional and reliable, emphasizing clarity and ease of use for healthcare providers while providing a calming visual experience for patients.

## Colors

The palette is intentionally limited to reinforce a sterile and focused environment. **Pure White** serves as the primary canvas, ensuring maximum luminosity and an "airy" feel. **Sky Blue** is the functional lead color, used for primary actions, data highlights, and branding accents, symbolizing oxygen and clarity. 

**Soft Slate** provides the necessary grounding for secondary information and borders, offering a gentler contrast than pure black. Backgrounds should utilize very subtle gradients of sky blue and slate to create the necessary "depth" behind frosted glass layers.

## Typography

This design system utilizes **Inter** for its exceptional legibility and systematic, clinical feel. High-contrast scales are employed to ensure critical medical data is instantly scannable. 

Headlines are set with tight letter spacing and heavy weights to create a sense of authority. Body text maintains generous line heights to enhance the "airy" quality of the interface. For data-heavy labels, a medium-to-semibold weight is used to ensure visibility against translucent glass backgrounds.

## Layout & Spacing

The layout follows a **fluid grid** model with significant negative space. To maintain the "airy" aesthetic, containers and sections are separated by wide gutters, preventing any sense of visual congestion. 

Information is organized into distinct glass modules. Spacing inside these modules is generous, typically starting at a 32px base padding to ensure that even complex diagnostic data feels approachable. Horizontal margins on desktop are expansive, centering the focus on the diagnostic content.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and multi-layered translucency rather than traditional heavy shadows.

1.  **Backdrop Blur:** All primary cards and overlays must utilize a `backdrop-filter: blur(20px)` to create separation from the background.
2.  **Surface Opacity:** Glass cards should have a white fill at 60–80% opacity to maintain readability while appearing lightweight.
3.  **Soft Shadows:** Use extremely diffused, low-opacity shadows (Color: Soft Slate at 10% opacity, Blur: 40px, Y-Offset: 20px) to give the "hovering" effect to active glass elements.
4.  **Edge Highlights:** A 1px translucent border (White at 40% opacity) should be applied to all glass cards to define their edges against light backgrounds.

## Shapes

The shape language is defined by ultra-soft, **pill-shaped** geometry. Large radii (minimum 24px) are applied to all cards and interactive containers to evoke an organic, "inflated" feel. This softness mitigates the clinical nature of the tool, making it feel more like a wellness companion than a rigid medical device. Buttons and small inputs utilize a fully rounded (pill) radius.

## Components

### Glass Cards
The primary container for all data. These feature a frosted-glass texture, 24px+ rounded corners, and a 1px inner glow/border to ensure they pop against the white-washed background.

### Liquid Progress Bars
Used for pulmonary capacity and breath-monitoring. These are not static bars; they utilize a fluid, easing animation that mimics the flow of air. The fill should have a slight gradient from Sky Blue to a more vibrant cyan, with a "wave" or "blob" shaped leading edge.

### Buttons
Primary buttons are solid Sky Blue with high-contrast white text, featuring a subtle outer glow rather than a shadow. Secondary buttons are "ghost-glass"—completely transparent with a 1px border and a blur effect that intensifies on hover.

### Inputs & Selectors
Fields are rendered as translucent troughs with soft internal shadows. Upon focus, the border transitions to a glowing Sky Blue.

### Diagnostic Gauges
Circular indicators that use varying stroke weights and "breath" animations (pulsing) to visualize lung function in real-time. All gauges must maintain the high-contrast Inter typography for numerical values.