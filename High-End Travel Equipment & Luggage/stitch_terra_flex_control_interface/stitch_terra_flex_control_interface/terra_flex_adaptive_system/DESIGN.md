---
name: Terra-Flex Adaptive System
colors:
  surface: '#fbf8ff'
  surface-dim: '#dbd9e1'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f2fa'
  surface-container: '#efedf4'
  surface-container-high: '#e9e7ef'
  surface-container-highest: '#e4e1e9'
  on-surface: '#1b1b21'
  on-surface-variant: '#454651'
  inverse-surface: '#303036'
  inverse-on-surface: '#f2eff7'
  outline: '#767682'
  outline-variant: '#c6c5d3'
  surface-tint: '#4b57aa'
  primary: '#142175'
  on-primary: '#ffffff'
  primary-container: '#2e3a8c'
  on-primary-container: '#9ea9ff'
  inverse-primary: '#bcc3ff'
  secondary: '#575f6a'
  on-secondary: '#ffffff'
  secondary-container: '#d8e0ee'
  on-secondary-container: '#5b636f'
  tertiary: '#2a2d2f'
  on-tertiary: '#ffffff'
  tertiary-container: '#404346'
  on-tertiary-container: '#adb0b2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dfe0ff'
  primary-fixed-dim: '#bcc3ff'
  on-primary-fixed: '#000d60'
  on-primary-fixed-variant: '#333f91'
  secondary-fixed: '#dbe3f0'
  secondary-fixed-dim: '#bfc7d4'
  on-secondary-fixed: '#141c26'
  on-secondary-fixed-variant: '#3f4752'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#44474a'
  background: '#fbf8ff'
  on-background: '#1b1b21'
  surface-variant: '#e4e1e9'
typography:
  display-lg:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  status-number:
    fontFamily: Metropolis
    fontSize: 14px
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
  unit-xs: 4px
  unit-sm: 8px
  unit-md: 16px
  unit-lg: 24px
  unit-xl: 40px
  unit-fluid: clamp(16px, 4vw, 32px)
---

## Brand & Style
The design system embodies "Kinetic Sophistication." It bridges the gap between high-end industrial design and digital fluidity, mirroring the physical properties of the smart expandable luggage. The aesthetic is technical yet organic, utilizing soft transitions and "elastic" motion to communicate the product's adaptability.

The UI should feel lightweight and responsive, moving away from rigid boxes toward a more "stretched" and pressurized visual language. Interaction design must prioritize smooth, non-linear easing functions that mimic the tension and release of high-performance fabric.

## Colors
The palette is rooted in **Indigo** (Primary) and **Ash Grey** (Secondary), conveying trust and technical precision. **White** is the foundational canvas, providing the high-end, airy feel required for a premium travel experience.

Functional color tokens are introduced to represent the physical state of the luggage:
- **Indigo Tints:** Used to represent expansion depth; darker saturations indicate higher volume.
- **Ash Grey Scale:** Used for structural elements, borders, and inactive states.
- **Vibrant Indigo:** Reserved for active compression states and primary calls to action.

## Typography
The system utilizes **Metropolis** for headlines to provide a geometric, architectural foundation. **Hanken Grotesk** is used for body copy and labels, offering a contemporary, high-readability experience that feels technical yet approachable. 

Negative letter-spacing is applied to larger display types to increase the "tightness" and premium feel of the interface. Labels use increased tracking and all-caps styling to differentiate technical metadata from narrative content.

## Layout & Spacing
The layout follows a **Fluid Grid** philosophy. Padding and margins should expand and contract based on the viewport, mirroring the luggage's expansion. 

- **Containers:** Utilize dynamic padding (`unit-fluid`) to ensure content breathes on larger screens while remaining efficient on mobile.
- **Rhythm:** An 8px baseline grid maintains technical alignment.
- **Gaps:** Gutters should be generous (24px minimum on desktop) to preserve the high-end, minimalist aesthetic.

## Elevation & Depth
Depth is created through **Ambient Shadows** and **Tonal Layering**. Unlike harsh shadows, the shadows in this design system are highly diffused with a slight Indigo tint (`rgba(46, 58, 140, 0.08)`), suggesting that elements are hovering just above a soft surface.

- **Level 1 (Base):** White background.
- **Level 2 (Cards):** Subtle 1px Ash Grey border with a 4px blur shadow.
- **Level 3 (Modals/Expansion Panels):** 16px blur shadow with 0.12 opacity, creating a sense of "inflated" volume.
- **Glassmorphism:** Use backdrop blurs (20px) on navigation bars to maintain the fluid, modern context of the background content.

## Shapes
The shape language is defined by **Soft Roundedness (0.5rem base)**. This mimics the rounded corners of soft-side luggage. 

A unique "Elastic" property is applied to interactive elements: when hovered or pressed, buttons and cards should slightly "stretch" (scale slightly on one axis) before settling into their active state. This reinforces the "Terra-Flex" identity of a material that adapts to pressure.

## Components
### Expansion Toggles
Segmented controllers that use Indigo color fills to represent 25%, 50%, and Max levels. Transitioning between states must use the `expansion_bezier` to create a "pop" effect.

### Status Indicators
- **Durability Meter:** A slim, horizontal bar using a gradient from Ash Grey to Ash Grey 800, with a needle indicator.
- **Compression Active:** A pulsing glow effect around the primary Indigo button when the smart compression feature is engaged.

### Cards & Containers
Cards should have no harsh borders; instead, use a subtle inner stroke (0.5px) in Ash Grey to define the edges against the white background.

### Buttons
Primary buttons are Indigo with White text. Secondary buttons use a "Ghost" style with a 1.5px Ash Grey stroke. All buttons should have a minimum touch target of 48px and feature the "elastic" hover state.

### Input Fields
Inputs are bottom-bordered only in the default state, expanding to a full soft-rounded enclosure upon focus, visually representing the "flex" of the system.