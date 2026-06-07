---
name: Aura-Living
colors:
  surface: '#fbf9f2'
  surface-dim: '#dbdad3'
  surface-bright: '#fbf9f2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f4ed'
  surface-container: '#efeee7'
  surface-container-high: '#e9e8e1'
  surface-container-highest: '#e4e3dc'
  on-surface: '#1b1c18'
  on-surface-variant: '#414846'
  inverse-surface: '#30312c'
  inverse-on-surface: '#f2f1ea'
  outline: '#727976'
  outline-variant: '#c1c8c5'
  surface-tint: '#49645d'
  primary: '#49645d'
  on-primary: '#ffffff'
  primary-container: '#a7c4bc'
  on-primary-container: '#37524c'
  inverse-primary: '#afcdc5'
  secondary: '#5e5f5a'
  on-secondary: '#ffffff'
  secondary-container: '#e3e3dc'
  on-secondary-container: '#64655f'
  tertiary: '#59605e'
  on-tertiary: '#ffffff'
  tertiary-container: '#b9bfbd'
  on-tertiary-container: '#484e4d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cbe9e0'
  primary-fixed-dim: '#afcdc5'
  on-primary-fixed: '#04201b'
  on-primary-fixed-variant: '#314c46'
  secondary-fixed: '#e3e3dc'
  secondary-fixed-dim: '#c7c7c0'
  on-secondary-fixed: '#1b1c18'
  on-secondary-fixed-variant: '#464742'
  tertiary-fixed: '#dee4e2'
  tertiary-fixed-dim: '#c2c8c6'
  on-tertiary-fixed: '#171d1c'
  on-tertiary-fixed-variant: '#424847'
  background: '#fbf9f2'
  on-background: '#1b1c18'
  surface-variant: '#e4e3dc'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The brand personality for this design system is serene, exclusive, and effortless. It targets high-net-worth residents who value tranquility and seamless technological integration. The UI evokes a sense of "digital breathing room"—a calm sanctuary that mirrors the physical luxury of the residential complex.

The chosen style is **Neomorphism (Soft-UI)**, refined for a luxury context. Unlike early iterations of the trend, this design system uses extremely subtle transitions between highlights and shadows to create "molded" surfaces rather than aggressive extrusions. The aesthetic is clean and airy, utilizing a monochromatic-adjacent palette with organic undertones to maintain a sophisticated, non-industrial feel.

## Colors

The palette is anchored by **Cream (#F9F8F1)**, which serves as the primary canvas color to ensure an airy, warm atmosphere. **Soft Sage (#A7C4BC)** is used sparingly for primary actions and status indicators, providing a natural, calming focal point. 

**Charcoal (#2D3332)** is reserved strictly for high-contrast elements: primary typography, iconography, and deep accents that anchor the layout. To achieve the Soft-UI effect, a slightly darker neutral tone (**#E9E8E1**) is used for background layers to allow white highlights and soft shadows to remain visible and effective.

## Typography

The typography utilizes **Manrope** for its modern, balanced, and geometric properties. It provides the "sophisticated sans-serif" look required for a luxury residential brand while maintaining exceptional legibility on mobile screens.

Layouts should prioritize a generous vertical rhythm. Headlines use a lighter weight (`300`) at larger scales to feel elegant and airy, while labels use a heavier weight (`600`) and slight letter spacing to maintain clarity at small sizes. All text color should default to Charcoal to ensure high contrast against the Cream backgrounds.

## Layout & Spacing

This design system employs a **Fixed Grid** model for mobile devices, centered on a 4-column structure with 24px outer margins to provide a spacious, "gallery-like" feel. 

The spacing rhythm follows an 8px base unit. To maintain the "Airy" aesthetic, vertical spacing between disparate sections (e.g., Temperature Controls vs. Light Scenes) should be aggressive, erring on the side of more whitespace rather than less. Content should never feel cramped; every interactive element requires a significant touch target buffer.

## Elevation & Depth

Depth is achieved through **Soft-UI Neomorphism**. Instead of traditional drop shadows that sit "under" an object, surfaces appear to be molded from the background itself.

- **Raised Elements:** Use a dual shadow approach. A light highlight (`#FFFFFF`) on the top-left and a soft, diffused shadow (`#D1D0C8`) on the bottom-right.
- **Sunken Elements (Inputs/Active States):** Reverse the shadows. The shadow moves to the inner top-left, and the highlight moves to the inner bottom-right.
- **Shadow Quality:** Shadows must be extremely diffused (blur radius 12px-20px) and low opacity (15-20%) to avoid a muddy or "dirty" look. This creates a tactile, premium feel similar to high-end architectural finishes.

## Shapes

The shape language is consistently **Rounded**. A 0.5rem (8px) base radius is applied to standard components, while large containers and feature cards use a 1.5rem (24px) radius. This softness mitigates the technical nature of "smart home" controls, making the interface feel more organic and approachable. Avoid sharp 90-degree corners entirely to maintain the gentle aesthetic.

## Components

- **Buttons:** Primary buttons use the Soft Sage background with a very subtle raised neomorphic effect. Text is Charcoal for legibility. Secondary buttons are "molded" directly from the Cream background with no fill color, defined only by their shadows.
- **Cards:** Large containers for "Room" or "Device" groups. These should feature the highest level of neomorphic depth (rounded-xl) and include ample internal padding (24px).
- **Inputs & Sliders:** Use "Sunken" (inset shadow) patterns. Sliders for brightness or temperature should have a Charcoal track and a Soft Sage thumb that appears "Raised."
- **Chips:** Used for quick scene selection (e.g., "Evening," "Away"). These should be pill-shaped. When active, they transition from a "Raised" state to a "Sunken" state.
- **Smart Icons:** Line-based icons with a 1.5pt stroke width in Charcoal. Icons are never filled unless they represent an "On" state, in which case they may take on a Soft Sage glow.
- **Glass Overlays:** For critical alerts or modals, use a light backdrop blur (Glassmorphism) with 80% opacity Cream to maintain the airy feel without losing the soft-ui context.