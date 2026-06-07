---
name: Mediterranean Breeze
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#434653'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#2559bd'
  primary: '#00327d'
  on-primary: '#ffffff'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#b1c5ff'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#6a1909'
  on-tertiary: '#ffffff'
  tertiary-container: '#892f1e'
  on-tertiary-container: '#ffa896'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdad3'
  tertiary-fixed-dim: '#ffb4a5'
  on-tertiary-fixed: '#3e0500'
  on-tertiary-fixed-variant: '#802918'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: 32px
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '300'
    lineHeight: 28px
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '300'
    lineHeight: 24px
  label-caps:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 24px
  gutter: 16px
  section-gap: 64px
  touch-target: 48px
---

## Brand & Style

This design system captures the essence of a high-end coastal lifestyle, evoking the feeling of a sun-drenched villa overlooking the Mediterranean. The brand personality is aspirational, serene, and curated, targeting a discerning audience that values luxury, craftsmanship, and architectural beauty.

The design style is a refined **Minimalism** blended with **Tactile** elements. It prioritizes emotional resonance through high-resolution, full-bleed imagery treated with a "Daylight" filter—increasing brightness and warmth to mimic natural sun exposure. The interface remains intentionally understated to act as a gallery-like frame for the interior design photography, utilizing expansive whitespace to create a sense of airiness and calm.

## Colors

The palette is anchored by a high-contrast relationship between **Cobalt Blue** and **Crisp White**, reflecting the iconic architecture of coastal estates. 

- **Primary (Cobalt Blue):** Used for key brand moments, primary actions, and elegant typography accents. It represents the depth of the sea and high-end sophistication.
- **Secondary (Crisp White):** The foundational canvas. It provides the "airy" feel and ensures a clean, clinical yet warm backdrop for imagery.
- **Tertiary (Terra Cotta):** A warm, earthy accent used sparingly for notifications, specific interactive highlights, or to draw attention to architectural details.
- **Neutrals:** A spectrum of soft greys and "Sand" off-whites are used for subtle borders and secondary backgrounds to prevent the high contrast from becoming jarring.

## Typography

The typography strategy pairs the timeless elegance of **Noto Serif** with the modern, approachable clarity of **Be Vietnam Pro**. 

Headlines utilize Noto Serif to evoke the editorial feel of luxury travel magazines. The weight is kept light to medium to maintain a sense of grace. Body text uses Be Vietnam Pro with increased line height and light weights (300) to ensure the interface feels "breathable" and easy to navigate on mobile devices. Navigation and small labels utilize uppercase Be Vietnam Pro with generous letter spacing to provide a modern, structural contrast to the serif headings.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for mobile-first immersion. On mobile, margins are generous (24px) to frame content, while full-bleed imagery is utilized to break the grid and create an immersive, tactile experience.

Spacing is governed by an 8px rhythmic scale. However, the design system emphasizes "Macro-spacing"—purposefully large gaps (section-gap) between content blocks to ensure the user never feels overwhelmed. This whitespace is essential to the "Breeze" narrative, allowing the high-end interior photography to "breathe" and stand as the focal point.

## Elevation & Depth

Visual hierarchy is achieved through **Ambient Shadows** and **Tonal Layers** rather than heavy borders. 

Shadows are extremely diffused, low-opacity, and slightly tinted with Cobalt Blue to keep them cool and integrated with the palette. Surfaces utilize a subtle "Daylight" elevation where the primary background is Pure White (#FFFFFF), and elevated cards or menus use a slightly tinted "Sand" or "Sea Foam" off-white to create soft depth. On imagery, text overlays should use a subtle gradient scrim to ensure legibility while maintaining the sun-drenched aesthetic.

## Shapes

The shape language is **Soft (0.25rem)**, mirroring the architectural curves found in Mediterranean villas—where stone edges are softened by time and sea air. 

While the containers for full-bleed imagery remain sharp to maximize impact, UI components like buttons, input fields, and cards utilize subtle rounding. This creates a tactile, approachable feel that prevents the minimalist aesthetic from appearing too clinical or harsh.

## Components

- **Buttons:** Primary buttons are solid Cobalt Blue with White text, using the "Soft" corner radius. Secondary buttons are outlined (Ghost) with a 1px Cobalt border. 
- **Cards:** Used for product listings or villa portfolios. They feature full-bleed imagery at the top, followed by Noto Serif titles. Shadows are only applied on hover or active states to maintain a flat, editorial look.
- **Input Fields:** Minimalist design with only a bottom border in a light grey, which transitions to Cobalt Blue upon focus. Labels are always "Label-Caps" style.
- **Chips/Filters:** Used for categorization (e.g., "Coastal," "Rustic," "Modern"). These should be Pill-shaped to contrast against the mostly rectangular grid.
- **Navigation:** A persistent, transparent-to-white header that accommodates the high-resolution background imagery. Icons should be thin-stroke (lightweight) to match the typography.
- **Immersive Carousel:** A custom mobile component allowing for edge-to-edge swiping of interior photography, utilizing a Terra Cotta accent color for the active slide indicator.