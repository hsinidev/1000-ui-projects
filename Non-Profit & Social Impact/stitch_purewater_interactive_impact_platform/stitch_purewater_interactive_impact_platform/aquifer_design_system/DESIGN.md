---
name: Aquifer Design System
colors:
  surface: '#f7fafd'
  surface-dim: '#d7dadd'
  surface-bright: '#f7fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f7'
  surface-container: '#ebeef1'
  surface-container-high: '#e5e8eb'
  surface-container-highest: '#e0e3e6'
  on-surface: '#181c1e'
  on-surface-variant: '#444650'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f4'
  outline: '#757681'
  outline-variant: '#c5c6d1'
  surface-tint: '#455c99'
  primary: '#000d2f'
  on-primary: '#ffffff'
  primary-container: '#00205b'
  on-primary-container: '#738aca'
  inverse-primary: '#b2c5ff'
  secondary: '#006875'
  on-secondary: '#ffffff'
  secondary-container: '#00e3fd'
  on-secondary-container: '#00616d'
  tertiary: '#0e1010'
  on-tertiary: '#ffffff'
  tertiary-container: '#232525'
  on-tertiary-container: '#8b8c8c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001849'
  on-primary-fixed-variant: '#2d447f'
  secondary-fixed: '#9cf0ff'
  secondary-fixed-dim: '#00daf3'
  on-secondary-fixed: '#001f24'
  on-secondary-fixed-variant: '#004f58'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f7fafd'
  on-background: '#181c1e'
  surface-variant: '#e0e3e6'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 20px
  section-padding: 120px
---

## Brand & Style

The design system is anchored in the concept of "Life in Motion." It translates the mission of global water access into a digital experience that feels as essential and transparent as water itself. The brand personality is **empathetic, urgent yet optimistic, and profoundly clear.**

The visual style utilizes a refined blend of **Minimalism and Glassmorphism**. By using translucent layers and soft, light-refracting surfaces, the UI mimics the physical properties of water—clarity, depth, and fluidity. Organic, non-geometric "blob" shapes serve as containers for high-quality humanitarian photography, ensuring the human element is always framed by the life-giving nature of the work. The overall emotional response should be one of refreshment and renewed hope.

## Colors

The palette is a high-contrast triad designed to evoke the deep ocean and pure, filtered drinking water.

*   **Deep Cobalt Blue (#00205B):** Used for primary typography, deep backgrounds, and high-authority elements. It provides the grounding "depth" of the brand.
*   **Crystal Cyan (#00E5FF):** Used for calls to action, progress indicators, and interactive highlights. It represents the "sparkle" and vitality of clean water.
*   **White (#FFFFFF):** The primary canvas color, ensuring an airy, sterile, and hopeful environment.
*   **Surface Accents:** Soft, desaturated blue-greys are used for subtle backgrounds to prevent optical fatigue while maintaining a "cool" temperature.

## Typography

This design system utilizes **Plus Jakarta Sans** for its modern, friendly, and inherently "liquid" feel. The rounded terminals of the glyphs echo the organic shapes of the visual style. 

Headlines are set with tight tracking and heavy weights to create an impactful editorial feel, especially when overlaid on photography. Body text maintains generous line height to preserve the "airy" layout requirement. All interactive labels use a bold, slightly tracked-out style to ensure clarity against glassmorphic backgrounds.

## Layout & Spacing

The layout philosophy is **Immersive & Fluid**. It utilizes a 12-column flexible grid that prioritizes whitespace to let the photography breathe.

Key layout principles:
*   **Generous Verticality:** Large 120px padding between sections to create a sense of calm and unhurried exploration.
*   **Asymmetric Offsets:** Elements often break the grid slightly or use organic SVG masks to overlap sections, mimicking the flow of water.
*   **Mobile-First Immersion:** On smaller screens, the system transitions to a single-column stack with full-width "liquid" imagery and sticky, glassmorphic navigation to maintain accessibility.

## Elevation & Depth

Depth in this design system is achieved through **optical refraction rather than traditional shadows.**

*   **Glassmorphic Surfaces:** Floating panels use a `backdrop-filter: blur(12px)` with a semi-transparent white fill (opacity 40–70%). 
*   **Inner Glow:** Instead of drop shadows, cards use a 1px solid white border at 20% opacity to define their edges, creating a "glass edge" effect.
*   **Ambient Depth:** When shadows are necessary for accessibility, they are highly diffused and tinted with the Primary Cobalt color (#00205B) at a very low 5-8% opacity, preventing a "dirty" look on the clean white canvas.

## Shapes

The shape language is strictly **non-linear and organic.** 

While the fundamental UI components use a "Pill-shaped" (Level 3) roundedness to feel soft and safe, larger decorative elements use custom SVG "liquid blobs." Sharp corners are entirely avoided in this design system to maintain the "Fluid & Hopeful" aesthetic. Buttons, input fields, and tags should always utilize maximum corner radius to appear approachable and friendly.

## Components

### Buttons
Primary buttons are pill-shaped with a gradient fill moving from Deep Cobalt to a slightly lighter indigo. Secondary buttons use the Crystal Cyan for high visibility. All buttons feature a subtle "shimmer" hover effect.

### Cards
Cards are the primary vehicle for humanitarian photography. They feature glassmorphic footers where text is overlaid on a blurred section of the image, ensuring legibility without obscuring the visual content.

### Progress Indicators
Used for fundraising goals, these are styled as "water levels" within a container, using a subtle wave animation at the fill line.

### Input Fields
Inputs are minimalist with a soft Cyan bottom border that "flows" into a full border highlight upon focus.

### Interactive "Liquid" Blobs
Decorative background elements that move slightly on scroll or mouse-move, creating a sense of a living, breathing environment.