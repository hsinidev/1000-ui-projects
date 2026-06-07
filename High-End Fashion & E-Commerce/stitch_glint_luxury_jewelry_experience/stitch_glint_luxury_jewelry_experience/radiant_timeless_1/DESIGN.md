---
name: Radiant & Timeless
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
  on-surface-variant: '#4f4442'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#817471'
  outline-variant: '#d3c3c0'
  surface-tint: '#725853'
  primary: '#725853'
  on-primary: '#ffffff'
  primary-container: '#e0bfb8'
  on-primary-container: '#654d47'
  inverse-primary: '#e0bfb8'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#c6c6c6'
  on-tertiary-container: '#515253'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fedbd4'
  primary-fixed-dim: '#e0bfb8'
  on-primary-fixed: '#291713'
  on-primary-fixed-variant: '#59413c'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.15em
  button-text:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 80px
  section-padding: 120px
---

## Brand & Style
The brand personality is rooted in quiet luxury, catering to a discerning audience that values heritage, craftsmanship, and ethereal beauty. The UI must evoke a sense of serenity and exclusivity, making the user feel as though they are stepping into a high-end physical boutique.

This design system utilizes a blend of **Minimalism** and **Glassmorphism**. The interface acts as a gallery, prioritizing generous whitespace and high-resolution macro photography of jewelry. Interactive elements use translucent, frosted layers and subtle shimmering gradients to mimic the way light interacts with precious metals and stones. The overall aesthetic is "Airy High-Fidelity," where thin lines and soft transitions create a premium, lightweight digital experience.

## Colors
The palette is centered around the "Marble White" background, providing a pristine, museum-like canvas. 

- **Primary (Rose Gold):** Used exclusively for primary calls to action, active states, and highlights. It should be treated as a precious material, used sparingly to maintain its impact.
- **Secondary (Deep Charcoal):** Provides necessary grounding and contrast for typography, iconography, and structural borders.
- **Neutral (Marble & Pure White):** Layers of off-white and pure white define the spatial structure without introducing harsh lines.
- **Accents:** A subtle shimmer effect can be applied to Rose Gold elements using a linear gradient from #E0BFB8 to #F4E4E1.

## Typography
The typographic hierarchy relies on the contrast between the authoritative, literary feel of **Noto Serif** (substitute for Playfair) and the modern, balanced clarity of **Manrope** (substitute for Montserrat).

Headings should be set with generous leading and occasional negative letter-spacing for a modern editorial feel. Body copy utilizes light weights and increased line-height to ensure the text feels "airy" and uncrowded. Labels and small metadata should always use uppercase with wide tracking to denote a premium, branded look.

## Layout & Spacing
This design system employs a **Fixed Grid** model for desktop and a **Fluid Grid** for mobile devices. The layout is defined by its extreme use of white space; sections are separated by large vertical gaps to allow each jewelry piece to breathe.

The grid is a 12-column system. Content blocks should frequently "break" the grid with asymmetrical alignments to create a more dynamic, editorial rhythm. Margins are intentionally wide (80px+) to frame the content like a piece of art.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and tonal layering rather than traditional shadows. 

- **Backdrop Blurs:** Navigation bars and modal overlays use a high-saturation blur (20px-30px) with a semi-transparent White (80% opacity) fill.
- **Shimmer Effects:** Primary buttons feature a subtle "light sweep" animation to mimic the sparkle of a gemstone.
- **Thin Outlines:** Surfaces are defined by 1px borders in a very light Rose Gold or a 10% opacity Deep Charcoal, rather than drop shadows.
- **Z-Axis:** Information is stacked in clear tiers. The base is the Marble White background, the second tier is the frosted glass container, and the top tier is the high-contrast Deep Charcoal text.

## Shapes
The shape language is strictly **Sharp (0px)**. To maintain a timeless and architectural feel, all buttons, input fields, and image containers use crisp 90-degree angles. This severity in shape contrasts beautifully with the organic, soft forms of the jewelry shown in the photography. 

The only exception to the sharp rule is the jewelry itself and circular iconography; all structural UI components must remain rectangular.

## Components
- **Buttons:** Primary buttons are solid Rose Gold with Deep Charcoal text, featuring a subtle shimmer hover effect. Secondary buttons are "ghost" style with a 1px Deep Charcoal border and no fill.
- **Inputs:** Text fields are single lines (bottom border only) to maintain a minimalist, "form-fill" aesthetic found in luxury hotels. Labels sit above in the `label-caps` style.
- **Cards:** Product cards are borderless with the jewelry piece isolated on a Marble White or very light grey background. Text is center-aligned beneath the image.
- **Chips/Filters:** Thin-bordered rectangles using `label-caps` typography. The active state fills the chip with a soft Rose Gold tint.
- **Lists:** Separated by thin, full-width 0.5px Charcoal lines with high transparency (10%).
- **Specialty Component (The Loupe):** A custom interaction for product pages where hovering over macro photography creates a high-magnification "glass" circle to inspect diamond clarity and metal texture.