---
name: Ethereal Professionalism
colors:
  surface: '#fef7fd'
  surface-dim: '#ded8de'
  surface-bright: '#fef7fd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f2f7'
  surface-container: '#f3ecf1'
  surface-container-high: '#ede6ec'
  surface-container-highest: '#e7e1e6'
  on-surface: '#1d1b1f'
  on-surface-variant: '#4a454e'
  inverse-surface: '#322f34'
  inverse-on-surface: '#f5eff4'
  outline: '#7b757f'
  outline-variant: '#ccc4cf'
  surface-tint: '#6c538b'
  primary: '#6a5188'
  on-primary: '#ffffff'
  primary-container: '#8369a3'
  on-primary-container: '#fffbff'
  inverse-primary: '#d8bafa'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#4f5e68'
  on-tertiary: '#ffffff'
  tertiary-container: '#677782'
  on-tertiary-container: '#fcfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#eedbff'
  primary-fixed-dim: '#d8bafa'
  on-primary-fixed: '#260e43'
  on-primary-fixed-variant: '#543b71'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#d5e5f1'
  tertiary-fixed-dim: '#b9c9d5'
  on-tertiary-fixed: '#0e1d26'
  on-tertiary-fixed-variant: '#3a4953'
  background: '#fef7fd'
  on-background: '#1d1b1f'
  surface-variant: '#e7e1e6'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.5'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  section-padding: 80px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built upon a philosophy of "Grounded Spirituality." It bridges the gap between the ethereal nature of energy healing and the structured reliability of professional wellness services. The aesthetic is a blend of **Minimalism** and **Glassmorphism**, emphasizing negative space to allow the interface to "breathe," mirroring the meditative state of Reiki.

The visual direction uses fluid motion and translucent layers to evoke a sense of energy flow. It avoids sharp, aggressive corners in favor of soft transitions and organic movement. The emotional response should be one of immediate relief—a digital sanctuary that feels premium, quiet, and deeply restorative.

## Colors

The palette is anchored by **Soft Lavender**, used to signify healing and intuition. **Gold** is employed sparingly as an accent to denote premium quality and the "golden light" of energy work. **Charcoal** provides the necessary grounding, used for text and structural elements to maintain professional authority.

Gradients are central to this design system. Use a "Linear Flow" gradient transitioning from Soft Lavender (at 10% opacity) to a Pure White or a very soft Charcoal tint to create depth without weight. Backgrounds should never be flat; they should possess subtle radial shifts in tone to suggest a living energy field.

## Typography

The typographic scale contrasts the timeless elegance of **Noto Serif** for headings with the functional, modern clarity of **Manrope** for functional text. 

Headings should be treated with generous leading (line height) to maintain the "Ethereal" aesthetic. For the most premium feel, use "label-caps" for small eyebrows or category tags above headlines, which adds a layer of curated, editorial structure to the spiritual content.

## Layout & Spacing

This design system utilizes a **Fixed Grid** for desktop (12 columns) and a **Fluid Grid** for mobile. The layout philosophy is "Centering"—key content is often placed in the center columns to create a focal point for the eye, much like a mandala.

Whitespace is treated as a functional element, not a void. Large vertical gaps (80px+) between sections are encouraged to prevent the user from feeling overwhelmed. Elements should never feel "packed"; if in doubt, increase the padding to allow the energy of the layout to flow.

## Elevation & Depth

To achieve the "floating" effect, this design system rejects heavy, dark shadows. Instead, it uses:

1.  **Ambient Glows:** Soft, Lavender-tinted shadows with a very high blur radius (40px-60px) and low opacity (5-8%).
2.  **Backdrop Blurs:** Using Glassmorphism for navigation bars and overlays (12px to 20px blur) to maintain a sense of translucency.
3.  **Z-Axis Floating:** Elements in a "floating" state should have a subtle Y-offset of -8px to -16px compared to their resting state, paired with a soft shadow to suggest they are hovering over the surface.

## Shapes

The shape language is organic and soft. Standard containers use a 0.5rem (8px) radius, but featured elements like "Energy Cards" or "Session Modalities" should utilize `rounded-xl` (1.5rem/24px) or even fully organic, asymmetrical blob shapes for background decorations. 

Buttons should be pill-shaped or have a high degree of roundedness to ensure they feel inviting and safe to touch. Sharp 90-degree angles should be avoided in all customer-facing components.

## Components

### Buttons
Primary buttons use a Lavender-to-Gold subtle linear gradient or a solid Charcoal for high-contrast professional actions. They feature a slight hover lift and a soft lavender glow. Text is always Manrope Semibold.

### Cards
Cards are "Floating Glass" surfaces. They feature a 1px border of 10% white (to catch the light), a soft backdrop blur, and a Lavender-tinted ambient shadow. Content within cards is centered.

### Input Fields
Inputs are minimalist, utilizing a bottom-border only or a very soft grey-filled background with rounded-lg corners. The focus state transitions the border to Gold.

### Chips & Tags
Used for session types (e.g., "Distance Healing," "Chakra Balancing"). These are pill-shaped with a Soft Lavender background at 15% opacity and Charcoal text.

### Floating Action Elements
Small, decorative "orb" elements (subtle gradients) should be placed behind key components to guide the eye and reinforce the "Energy Flow" narrative.