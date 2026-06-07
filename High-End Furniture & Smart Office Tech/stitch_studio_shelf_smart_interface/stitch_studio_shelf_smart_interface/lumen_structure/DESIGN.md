---
name: Lumen & Structure
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
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#ebbe9b'
  on-secondary: '#462a12'
  secondary-container: '#624228'
  on-secondary-container: '#dcb08e'
  tertiary: '#d0cdcd'
  on-tertiary: '#303030'
  tertiary-container: '#b4b2b2'
  on-tertiary-container: '#454545'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ebbe9b'
  on-secondary-fixed: '#2d1602'
  on-secondary-fixed-variant: '#5f4026'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
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
  margin-mobile: 20px
  margin-desktop: 64px
  gutter: 16px
---

## Brand & Style

This design system embodies an **Architectural-Luxe** aesthetic, specifically tailored for a high-end modular furniture experience. The visual language balances the cold precision of structural engineering with the organic warmth of artisanal materials. It targets a discerning audience—architects, interior designers, and luxury homeowners—who value both modular flexibility and permanent quality.

The emotional response should be one of "Structured Serenity." The UI utilizes a **Minimalist-Tactile** style, where clean lines and generous whitespace meet rich textures. To differentiate from standard flat minimalism, this design system incorporates subtle light-leak gradients and "LED glows" that mimic the brand’s physical lighting products, creating a sense of depth and atmosphere. High-contrast imagery showcasing macro wood grains and polished metallic joints is central to the visual narrative.

## Colors

The palette is rooted in a deep, sophisticated **Charcoal (#2F2F2F)** base, establishing a dark-mode-first environment that allows lighting effects to pop. **Champagne Gold (#D4AF37)** is used as the primary interaction color, reserved for calls to action, active states, and focal points. **Warm Oak (#BC9373)** serves as a secondary tone, primarily used for background surfaces and UI containers to introduce organic warmth.

The "LED glow" is achieved through a specific variable—an ultra-soft radial gradient of Champagne Gold with high transparency. Text colors follow a strict hierarchy of "Pure Off-White" for readability and "Muted Gold" for secondary metadata.

## Typography

This design system uses a high-contrast typographic pairing to signal luxury. **Playfair Display** is the primary serif for all headlines and editorial moments; its high-stroke contrast mirrors the elegance of metallic accents. **Inter** provides a functional, neutral counterpoint for all UI elements, navigation, and body copy, ensuring legibility across technical specifications.

Editorial sections should utilize the "Display XL" size with tight letter-spacing to create a "fashion-magazine" feel. Labels and buttons should always be set in Inter, using uppercase styling and increased letter-spacing to emphasize the architectural, blueprint-inspired nature of the brand.

## Layout & Spacing

A **Fixed Grid** approach is utilized to maintain the "modular" theme of the physical product. On mobile, the design system employs a 4-column grid with generous 20px side margins. For desktop, it expands to a 12-column grid. 

Spacing is intentionally expansive. The "XL" spacing unit (80px) is used between major sections to allow the imagery to breathe, mimicking a gallery or high-end showroom experience. Vertical rhythm is strictly enforced in 8px increments, mirroring the precise measurements used in architectural shelving systems.

## Elevation & Depth

Hierarchy is conveyed through **Tonal Layers** and light rather than heavy shadows. In this dark-themed system, "elevation" means an element becomes slightly lighter or gains a "glow" effect.

1.  **Base:** Charcoal (#2F2F2F).
2.  **Raised:** Warm Oak surfaces or slightly lighter Charcoal variations.
3.  **Illuminated:** Elements that "emit light" (like active modules) feature a 20px-40px soft radial blur of Champagne Gold behind them, mimicking integrated LED strips.
4.  **Glassmorphism:** Navigation bars and selection overlays use a 20px backdrop blur with a 10% white tint to maintain a sense of translucency and "lightweight" luxury.

## Shapes

The shape language is primarily linear and structured. A **Soft (0.25rem)** corner radius is applied to buttons and containers to take the edge off the "industrial" feel while maintaining an architectural silhouette. 

Large-scale image containers and high-level product cards should remain sharp (0px) to emphasize the modular, block-like nature of the shelving. Roundness is reserved strictly for interactive UI elements (buttons, inputs) to signal touchability.

## Components

### Buttons
Primary buttons use a solid Champagne Gold background with dark Charcoal text. They feature a "glow" hover state where the button emits a soft gold shadow. Secondary buttons are "Ghost" style—thin 1px gold borders with uppercase label text.

### Product Cards
Cards feature high-contrast photography that bleeds to the edges. Pricing and titles are overlaid using a semi-transparent glassmorphism bar at the bottom.

### LED Toggle / Switch
A custom component that mimics a physical light switch. When "On," the toggle thumb glows with a radial Champagne Gold gradient.

### Modular Chips
Used for material selection (e.g., "Oak", "Walnut", "Brass"). These chips should feature a small circular swatch of the actual material texture next to the label.

### Inputs
Minimalist underlines (1px) in Muted Gold rather than full boxes. On focus, the underline thickens and a subtle glow appears beneath the input field.

### Configuration Progress
A thin, linear tracker at the top of the mobile view, using a gold "light" that travels across the line as the user completes their modular shelf build.