---
name: ZenWorker
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0058be'
  on-secondary: '#ffffff'
  secondary-container: '#2170e4'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#171c1f'
  on-tertiary-container: '#808488'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-display:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  max-width: 1440px
---

## Brand & Style

The design system is engineered to project a synthesis of clinical precision and empathetic modernism. It targets a B2B audience where trust, security, and data integrity are paramount, while maintaining a sense of "calm technology" appropriate for mental health and wellness contexts.

The visual style is **Corporate Modern** with strategic **Glassmorphism**. This combination balances the structural reliability of traditional enterprise software with the breathable, light-filled aesthetics of modern health tech. The interface evokes a sense of clarity and focus, minimizing cognitive load for employees while providing high-density data visualizations for HR administrators.

## Colors

The palette is anchored by **Deep Navy**, signifying authority and professional stability. **Electric Blue** is utilized as the primary action color and brand accent, providing a vibrant, tech-forward energy that guides the user’s eye to key interactions. 

Backgrounds utilize a tiered system of soft greys and pure white to create a layered environment. Transparency plays a critical role; the design system uses semi-transparent white overlays (60-80% opacity) against subtle gradients to create the signature glassmorphic effect without sacrificing WCAG 2.1 accessibility standards.

## Typography

This design system utilizes **Inter** exclusively to leverage its exceptional legibility in data-heavy environments. The typographic scale is designed for high-contrast hierarchy, ensuring that critical wellness metrics and corporate insights are immediately scannable. 

Headlines use tighter letter spacing and heavier weights to feel "anchored" and authoritative. Body text prioritizes a generous line height (1.6) to reduce visual crowding, promoting a calmer reading experience. Labels and metadata utilize uppercase styling with increased letter spacing to differentiate them from actionable content.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop, centered within a 1440px container to maintain a controlled, professional presentation on large monitors. A 12-column grid provides the structural foundation for the dashboard layouts.

Spacing follows an 8px base-unit rhythm. Strategic "negative space" is used to group related metrics and prevent the UI from feeling overwhelming—a critical requirement for a mental health platform. Large sections are separated by 48px or 64px gaps, while internal card components use 24px padding to create a breathable, "premium" feel.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Glassmorphism** and **Ambient Shadows**. Instead of traditional solid-color elevation, surfaces use backdrop-blur filters (12px to 20px) and semi-transparent white fills.

Depth is categorized into three levels:
1.  **Base Layer:** Solid light grey (#F8FAFC) background.
2.  **Surface Layer:** Glassmorphic cards with a subtle 1px white border (20% opacity) and a soft, diffused shadow (0px 10px 30px rgba(15, 23, 42, 0.05)).
3.  **Overlay Layer:** Modals and tooltips with higher backdrop-blur and more pronounced shadows to signify immediate focus and temporary interaction.

## Shapes

The design system adopts a **Rounded** shape language to soften the corporate aesthetic and appear more approachable. A base radius of 8px (0.5rem) is applied to most UI components, including input fields and small buttons. 

Larger containers and data visualization cards use a 16px (1rem) radius to emphasize the "glass pane" metaphor. This consistent rounding strategy helps the software feel human-centric and safe, contrasting with the sharp angles often found in rigid, legacy B2B tools.

## Components

**Buttons:** 
- *Primary:* Solid Deep Navy with white text for maximum authority.
- *Secondary:* Electric Blue outlines or transparent fills for secondary actions.
- *Shape:* 8px corners, with height tiers of 40px (default) and 48px (hero).

**Cards:**
- The primary vehicle for data visualization. They must utilize the glassmorphic style: semi-transparent white background, backdrop-blur, and a subtle 1px inner border to simulate a light-catching edge.

**Inputs & Forms:**
- Form fields utilize a light grey background (#F1F5F9) that transitions to a white background with an Electric Blue border on focus. Labels are always positioned above the field for clarity.

**Data Visualization:**
- Charts should use the Electric Blue as the primary data point, complemented by a palette of cool-toned secondary colors (Teals, Indigos). Use soft, rounded ends on bar charts and smooth tension on line graphs to maintain the "calm" personality.

**Wellness Specifics:**
- *Pulse Indicators:* Softly glowing Electric Blue dots to indicate active sessions or live metrics.
- *Progress Rings:* Large-scale circular trackers for daily wellness goals, utilizing the secondary color palette.