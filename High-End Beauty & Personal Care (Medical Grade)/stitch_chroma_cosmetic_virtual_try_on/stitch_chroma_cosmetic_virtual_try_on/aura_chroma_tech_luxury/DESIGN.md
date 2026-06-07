---
name: Aura-Chroma Tech-Luxury
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d7c1c3'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9f8c8e'
  outline-variant: '#524345'
  surface-tint: '#ffb2bc'
  primary: '#ffb2bc'
  on-primary: '#551e29'
  primary-container: '#c77b86'
  on-primary-container: '#4c1722'
  inverse-primary: '#8c4b55'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#909191'
  on-tertiary-container: '#282a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

The brand identity sits at the intersection of avant-garde artistry and scientific precision. This design system bridges the gap between high-fashion editorial aesthetics and high-tech performance. The target audience is the discerning, tech-savvy consumer who views makeup as an extension of their digital and physical identity.

The visual style is **Artistic Minimalism** infused with **Glassmorphism**. We utilize expansive whitespace (or "blackspace") to create a gallery-like environment, where products are treated as masterpieces. Surfaces are layered using translucent materials and subtle refractive effects to evoke a sense of depth, transparency, and technological sophistication. The overall emotional response should be one of "exclusive access"—a feeling of being inside a high-end, futuristic studio.

## Colors

The palette is anchored by the tension between **Deep Black** and **Pure White**, creating a high-contrast foundation that feels both authoritative and clean. **Rose Gold** serves as the primary accent, used intentionally to highlight points of interaction and luxury brand moments. 

While the default mode is dark to emphasize the "night-out" glamour of the brand, white is used for high-legibility content and secondary containers. Rose Gold should be applied not just as a flat color, but as a metallic element—often expressed through linear gradients that simulate light hitting a polished surface.

## Typography

This design system employs a sophisticated typographic hierarchy that balances classic elegance with a futuristic edge. **Noto Serif** is used for headlines to provide a high-contrast, editorial feel reminiscent of luxury fashion magazines. It should be typeset with tight letter-spacing for large headlines to maximize visual impact.

**Space Grotesk** serves as the functional workhorse for UI elements and body copy. Its geometric structure and unique "tech" character reflect the brand's technologically advanced personality. For labels and small callouts, we utilize uppercase styling with generous tracking to maintain a premium, airy feel.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to ensure a controlled, curated experience across desktop and tablet, transitioning to a fluid model for mobile. We utilize a 12-column grid with a substantial 80px side margin to create an "inner stage" for content.

Spacing is generous. We use large vertical gaps (80px+) between sections to allow the eye to rest and to emphasize individual product stories. The rhythm is based on an 8px scale, but we lean towards the larger end of that scale (24px, 48px) to maintain a sense of luxury and avoid visual clutter.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Glassmorphism** and **Tonal Layering**. Rather than traditional heavy shadows, we use background blurs (30px+) and 1px borders with low-opacity Rose Gold or White to define surfaces.

1.  **Base Layer:** Solid Deep Black (#000000).
2.  **Surface Layer:** High-blur glass with 5% white opacity, creating a "frosted" effect.
3.  **Floating Elements:** Elements like modals or popovers use a slightly higher opacity (10%) and a subtle Rose Gold outer glow (#B76E79 at 15% opacity) to simulate a soft light source.
4.  **Gradients:** Subtle linear gradients (top-left to bottom-right) are applied to Rose Gold surfaces to give them a metallic, three-dimensional quality.

## Shapes

The shape language is architectural and precise. We utilize a **Soft (0.25rem)** roundedness for standard UI elements like buttons and input fields to maintain a modern, approachable feel without losing the "sharpness" of luxury branding. 

Large containers and cards may use a slightly larger radius (0.75rem) to soften the overall composition, but sharp 0px corners are reserved for decorative architectural elements or large-scale imagery to keep the design feeling bold and intentional.

## Components

**Buttons:** The primary button is a solid Rose Gold gradient with black text, using the `label-caps` typography. Secondary buttons are "ghost" style with a 1px Rose Gold border and a glass background blur.

**Cards:** Product cards are borderless with a subtle glass effect. The image should appear to "float" above the glass surface. On hover, the glass opacity increases, and the Rose Gold glow intensifies.

**Inputs:** Input fields are minimal, consisting only of a bottom border (1px white at 20% opacity). Upon focus, the border transitions to solid Rose Gold, and a faint Rose Gold glow appears beneath the line.

**Chips/Tags:** Used for "Limited Edition" or "New Arrival" labels, these are pill-shaped with high-contrast White text on a Black background, featuring a thin Rose Gold stroke.

**Navigation:** The header should be persistent and utilize a high-blur backdrop. Menu items use `label-caps` and exhibit a subtle "fade-in" transition when hovered.