---
name: Sustainable Modernism
colors:
  surface: '#f9faf6'
  surface-dim: '#dadad7'
  surface-bright: '#f9faf6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f1'
  surface-container: '#eeeeeb'
  surface-container-high: '#e8e8e5'
  surface-container-highest: '#e2e3e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#414844'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f0f1ee'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#232628'
  on-tertiary: '#ffffff'
  tertiary-container: '#393c3e'
  on-tertiary-container: '#a4a6a8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9faf6'
  on-background: '#1a1c1a'
  surface-variant: '#e2e3e0'
typography:
  display-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 40px
  gutter: 24px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The visual identity of this design system centers on the intersection of industrial precision and environmental stewardship. It is designed for a target audience of high-level ESG executives and logistics directors who demand both high-performance data and a premium, carbon-conscious aesthetic.

The style is defined as **Minimalist-Corporate**. It leverages vast amounts of negative space to evoke a sense of cleanliness and "white-glove" service. By removing unnecessary decorative elements, the system focuses the user's attention on critical logistics metrics. The emotional response is one of calm authority—reassuring the user that while global cargo movement is complex, their impact remains sustainable and organized.

## Colors

The palette is anchored by **Forest Green**, a deep, saturated tone that represents stability and ecological commitment. This primary color is used sparingly for key actions and brand moments to maintain its premium feel.

**Slate** serves as the functional secondary color, providing high-contrast legibility for data, labels, and iconography without the harshness of pure black. The background is a crisp, bright **White**, symbolizing transparency and the "clean energy" focus of the platform. A tertiary "Ice" tint (#F8FAFC) is used for container backgrounds to subtly separate content modules from the main canvas.

## Typography

This design system utilizes **Manrope** across all levels to maintain a contemporary, balanced aesthetic. Chosen for its unique blend of geometric clarity and humanist warmth, it excels in data-heavy dashboard environments.

Headlines are set with tight tracking and bold weights to establish a hierarchy of "Luxury Logistics." Body copy remains open and airy to ensure readability during prolonged sessions. A specific "Data Mono" variant—utilizing Manrope's cleaner numerals—is reserved for shipment IDs, coordinates, and ESG metric values, ensuring no ambiguity in critical figures.

## Layout & Spacing

The system employs a **Fixed Grid** philosophy for desktop dashboards, centering content within a 1440px max-width container to preserve the premium, editorial feel. A 12-column structure is used with generous 40px outer margins to provide "breathing room" that differentiates the platform from cramped, traditional logistics software.

The spacing rhythm follows an 8px linear scale. Large-scale component stacks use "stack-lg" (48px) to separate distinct data stories (e.g., Fleet Map vs. Carbon Analytics), while internal card padding remains consistent at 24px to ensure a comfortable, high-end user experience.

## Elevation & Depth

To maintain a minimalist aesthetic while providing visual hierarchy, this design system uses **Tonal Layers** supplemented by **Ambient Shadows**. 

Depth is primarily achieved through subtle shifts in background color (White vs. Ice). When physical separation is required for floating elements like modals or dropdowns, the system utilizes an extra-diffused shadow with a 0.05 opacity Forest Green tint. This "organic glow" prevents the UI from feeling sterile and mimics the soft light found in natural environments. Borders are kept thin (1px) and rendered in a faint Slate-200 to define edges without adding visual noise.

## Shapes

The shape language is characterized by **Organic UI** curves. A standard border radius of 0.5rem (rounded-md) is applied to buttons and inputs, while larger containers like data cards use 1rem (rounded-lg) to soften the industrial nature of the platform.

A signature element of this system is the **Liquid Progress Bar**. These components use fully pill-shaped (rounded-full) containers. The "fill" of the bar should use a slight easing in its width animation and a subtle gradient to mimic the fluid movement of water or fuel, reinforcing the sustainable transport theme.

## Components

### Buttons
Primary buttons are solid Forest Green with White text, featuring a subtle hover transition that deepens the green. Secondary buttons use a ghost style with a Slate-300 border and Forest Green text. All buttons feature a minimum height of 48px to feel substantial and "premium."

### Data Cards
Cards are the primary vessel for information. They feature a White background, a 1px Slate-100 border, and no shadow unless hovered. Headers within cards are separated by a faint horizontal rule.

### Input Fields
Fields utilize a soft Slate-50 background and a 1px Slate-200 border. Upon focus, the border transitions to Forest Green with a 2px "organic" outer glow. Labels are always placed above the field in the "label-sm" typography style.

### ESG Chips
Status indicators for carbon levels or sustainability ratings use high-chroma Forest Green or Sage backgrounds with white text. They are fully pill-shaped to stand out from the more structured rectangular data table rows.

### Liquid Progress Indicators
Used for tracking cargo transit or carbon offsets. These bars must be at least 12px tall with a "liquid" fill effect—a subtle horizontal wave animation that triggers when the data loads.

### Logistics List Items
Lists feature generous vertical padding (16px) and use thin dividers. Each item should have a clear "leading" icon in Slate to denote the type of cargo or vessel.