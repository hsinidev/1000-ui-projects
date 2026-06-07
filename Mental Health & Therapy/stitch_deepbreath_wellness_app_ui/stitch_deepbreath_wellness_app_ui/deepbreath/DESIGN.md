---
name: DeepBreath
colors:
  surface: '#f9f9fd'
  surface-dim: '#d9dade'
  surface-bright: '#f9f9fd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f7'
  surface-container: '#ededf1'
  surface-container-high: '#e8e8ec'
  surface-container-highest: '#e2e2e6'
  on-surface: '#1a1c1f'
  on-surface-variant: '#46464c'
  inverse-surface: '#2e3034'
  inverse-on-surface: '#f0f0f4'
  outline: '#77767d'
  outline-variant: '#c7c5cc'
  surface-tint: '#5c5d6e'
  primary: '#5c5d6e'
  on-primary: '#ffffff'
  primary-container: '#e6e6fa'
  on-primary-container: '#656677'
  inverse-primary: '#c5c5d8'
  secondary: '#51606b'
  on-secondary: '#ffffff'
  secondary-container: '#d2e2ee'
  on-secondary-container: '#55656f'
  tertiary: '#645883'
  on-tertiary: '#ffffff'
  tertiary-container: '#ede3ff'
  on-tertiary-container: '#6d618c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e1f5'
  primary-fixed-dim: '#c5c5d8'
  on-primary-fixed: '#191b29'
  on-primary-fixed-variant: '#444655'
  secondary-fixed: '#d5e5f1'
  secondary-fixed-dim: '#b9c9d5'
  on-secondary-fixed: '#0e1d26'
  on-secondary-fixed-variant: '#3a4953'
  tertiary-fixed: '#e9ddff'
  tertiary-fixed-dim: '#cebff1'
  on-tertiary-fixed: '#1f143b'
  on-tertiary-fixed-variant: '#4b406a'
  background: '#f9f9fd'
  on-background: '#1a1c1f'
  surface-variant: '#e2e2e6'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  section-gap: 40px
  element-gap: 12px
---

## Brand & Style

The brand personality is empathetic, tranquil, and grounding, specifically designed to reduce cognitive load for users experiencing high stress. This design system utilizes **Fluid Morphism**—a blend of glassmorphism and organic, bio-morphic shapes—to create a sense of movement and airiness. 

The visual direction avoids harsh angles and high-contrast vibrations, favoring soft transitions and depth layers that mimic the natural world. The goal is to evoke an immediate parasympathetic response, making the interface feel like a digital sanctuary rather than a tool.

## Colors

The palette is anchored by **Lavender (#E6E6FA)** to promote serenity and **Charcoal (#36454F)** for grounding structural elements and high-legibility text. Soft Purples are used for interactive states and focus areas, while Calming Grays provide neutral scaffolding. 

The color application relies heavily on transparency and tinting. Rather than solid blocks of color, surfaces often utilize the primary lavender at low opacities over blurred backgrounds to maintain the "fluid" aesthetic.

## Typography

This design system employs **Plus Jakarta Sans** for its modern, friendly, and inherently rounded letterforms. To enhance the feeling of "space" and calm, letter-spacing is slightly increased for body and label text. 

Hierarchy is established through weight transitions rather than extreme size shifts. Headlines remain soft and approachable, avoiding aggressive bold weights. Line heights are generous (1.6x for body text) to ensure high legibility and prevent the "wall of text" effect which can be overwhelming for anxious users.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** with generous safe areas. White space (or "negative space") is treated as a core functional element to provide visual breathing room. 

Margins and paddings are larger than standard utility-focused apps to emphasize the premium, meditative quality of the product. Elements are organized in organic clusters rather than rigid, dense rows.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and soft, ambient shadows. Instead of traditional drop shadows, this design system uses:
- **Backdrop Blurs:** (15px–30px) to create a sense of focus on the top layer while maintaining a connection to the background.
- **Inner Glows:** Soft white 1px borders on glass containers to simulate a light-catching edge.
- **Lavender-Tinted Shadows:** Shadows are never pure black; they are deep charcoal mixed with a hint of purple, with high diffusion (30-40px blur) and low opacity (5-10%).

## Shapes

The shape language is strictly **Pill-shaped (Level 3)**. Sharp corners are entirely absent from the system. 

Containers often use "squircle" mathematics or varied radii (e.g., top-left and bottom-right having a larger radius than the other corners) to appear more organic and less mechanical. This fluidity mirrors the movement of breath and water, reinforcing the app's core mission.

## Components

- **Buttons:** Primary buttons are pill-shaped, using a subtle gradient of Lavender to Soft Purple. Text is Charcoal for maximum contrast.
- **Glass Cards:** Cards use a semi-transparent white background with a heavy backdrop blur. They do not have heavy borders; instead, they use a 1px soft-white stroke.
- **Chips:** Highly rounded with a light charcoal tint for inactive states and a soft lavender glow for active states.
- **Input Fields:** Recessed appearance using a subtle inner shadow, giving a tactile "soft touch" feel.
- **Iconography:** Use 1.5pt stroke weights with rounded terminals. Icons are never filled; they remain ethereal and light.
- **Progress Indicators:** Fluid, non-linear animations (like a pulsing circle or expanding wave) instead of standard linear bars to guide breathing exercises.