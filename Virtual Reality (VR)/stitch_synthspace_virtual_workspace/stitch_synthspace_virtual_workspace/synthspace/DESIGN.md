---
name: SynthSpace
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#ccc3d3'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#958e9d'
  outline-variant: '#4a4452'
  surface-tint: '#d4bbff'
  primary: '#d4bbff'
  on-primary: '#3f0f81'
  primary-container: '#7e57c2'
  on-primary-container: '#f6ecff'
  inverse-primary: '#6f48b2'
  secondary: '#ffffff'
  on-secondary: '#003828'
  secondary-container: '#36ffc4'
  on-secondary-container: '#007255'
  tertiary: '#c8c6ca'
  on-tertiary: '#303033'
  tertiary-container: '#6d6c70'
  on-tertiary-container: '#f1eef2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ebdcff'
  primary-fixed-dim: '#d4bbff'
  on-primary-fixed: '#260058'
  on-primary-fixed-variant: '#572e99'
  secondary-fixed: '#36ffc4'
  secondary-fixed-dim: '#00e1ab'
  on-secondary-fixed: '#002116'
  on-secondary-fixed-variant: '#00513c'
  tertiary-fixed: '#e4e1e5'
  tertiary-fixed-dim: '#c8c6ca'
  on-tertiary-fixed: '#1b1b1e'
  on-tertiary-fixed-variant: '#47464a'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
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
  margin-desktop: 64px
  margin-mobile: 20px
  container-max-width: 1440px
---

## Brand & Style

This design system is engineered to evoke a sense of weightless productivity within a digital frontier. It targets forward-thinking professionals and remote teams who operate at the intersection of technology and creativity. The brand personality is ethereal yet disciplined, blending the infinite depth of virtual reality with the structured efficiency of professional SaaS.

The visual language utilizes **Glassmorphism** as its core foundation to simulate floating HUDs (Heads-Up Displays) in a 3D environment. This is complemented by **High-Contrast Neon Accents** that act as navigational beacons against **Matte Black** voids. The result is an "Airy" aesthetic that prevents the dark interface from feeling heavy, instead offering a spacious, immersive canvas for complex workflows.

## Colors

The palette is anchored by a deep **Matte Black** (#0D0D0D) which provides a non-reflective, infinite foundation. **Royal Purple** serves as the primary brand identifier, used for high-level interactive regions and brand-defining moments. **Mint** acts as a high-visibility neon accent, reserved for critical calls to action, success states, and active focus indicators.

To achieve the airy quality, the system relies on semi-transparent surface colors that allow background textures or gradients to bleed through. The "Mint" accent should be applied with a subtle outer glow (0 0 12px rgba(0, 255, 194, 0.4)) to simulate light emission in a dark environment.

## Typography

This design system uses a dual-font strategy to balance futuristic flair with long-form readability. **Space Grotesk** is utilized for headlines and labels; its geometric, technical quirks reinforce the VR/tech narrative. **Manrope** is used for all body copy and data entry, providing a refined and highly legible experience that reduces cognitive load during deep work sessions.

Headlines should be set with tight letter-spacing to feel impactful, while labels use expanded tracking and uppercase styling to mimic telemetry data found in high-tech cockpits.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model designed for responsiveness across ultra-wide monitors and mobile devices. A 12-column system is used for desktop, while a 4-column system is used for mobile.

Spacing is built on a strictly enforced 8px rhythmic scale. To maintain the "Airy" feel, excessive white space (or "black space") is encouraged between major functional blocks. Components should appear to float within their containers, utilizing generous internal padding (minimum 24px) to ensure the frosted glass backgrounds do not feel cramped.

## Elevation & Depth

Depth in this design system is communicated through **Backdrop Blurs** and **Luminous Outlines** rather than traditional drop shadows. 

1.  **Base Layer:** Solid Matte Black background.
2.  **Surface Layer:** 60% opacity matte grey with a 20px backdrop blur and a 1px solid border (white at 10% opacity).
3.  **Floating Layer:** Elements that require high priority (like Modals or Active Tools) use a 40px backdrop blur and a vibrant 1px border using the Royal Purple or Mint.

Shadows, when used, are tinted with the Primary color (#7E57C2) at very low opacity (15%) and high diffusion to create a "bloom" effect rather than a shadow.

## Shapes

The shape language is sophisticated and modern. A **Rounded (Level 2)** approach is applied to all primary UI containers and buttons to soften the high-tech aesthetic and make the environment feel approachable. 

Corner radii for standard components should be 8px (0.5rem), while larger layout cards and containers use 16px (1rem). Interactive elements like toggle switches and tags may utilize pill-shapes (full rounding) to differentiate them from structural data containers.

## Components

### Buttons
Primary buttons use a solid **Mint** fill with Matte Black text for maximum contrast. Secondary buttons utilize a **Glassmorphic** style with a Royal Purple 1px border. All buttons transition to a subtle "glow" on hover.

### Cards
Cards are the primary organizational unit. They must feature a `backdrop-filter: blur(20px)` and a top-to-bottom linear gradient stroke (from white at 15% to white at 5%) to simulate light hitting the top edge of a glass pane.

### Input Fields
Inputs are defined by a bottom-border only in their resting state (2px Royal Purple). Upon focus, they expand into a full glassmorphic container with a Mint glow.

### Chips & Tags
Used for categorization, these should be pill-shaped with a low-opacity Purple fill and Space Grotesk labels.

### Floating Navigation
The primary navigation should be a floating dock, centered at the bottom of the viewport, using the highest level of backdrop blur and a thin Mint accent line on the active state icon.