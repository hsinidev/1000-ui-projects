---
name: Nordic Soul
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
  on-surface-variant: '#444748'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#111111'
  on-primary: '#ffffff'
  primary-container: '#262626'
  on-primary-container: '#8e8d8c'
  inverse-primary: '#c8c6c5'
  secondary: '#695c4e'
  on-secondary: '#ffffff'
  secondary-container: '#f1e0cd'
  on-secondary-container: '#6f6254'
  tertiary: '#101110'
  on-tertiary: '#ffffff'
  tertiary-container: '#252625'
  on-tertiary-container: '#8d8d8b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1b1c1c'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#f1e0cd'
  secondary-fixed-dim: '#d5c4b2'
  on-secondary-fixed: '#231a0f'
  on-secondary-fixed-variant: '#504537'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  caption:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 8px
  margin-page: 64px
  gutter: 32px
  section-gap: 128px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
This design system is anchored in the principles of Scandinavian functionalism and the emotional warmth of *Hygge*. It evokes a sense of stillness, clarity, and intentionality, targeting an audience that appreciates quiet luxury and editorial craftsmanship. 

The visual style is **Minimalist and Editorial**, characterized by expansive white space—often used as a structural element rather than a void—and a meticulous attention to typographic hierarchy. The UI should feel like a high-end coffee-table book: breathable, tactile, and permanent. Every element must earn its place on the screen, favoring thin-line aesthetics and a monochromatic foundation over decorative flourishes.

## Colors
The palette is a curated selection of natural, desaturated tones designed to minimize cognitive load. 
- **White (#FFFFFF):** The primary canvas color, used to create the "Airy" feel.
- **Pale Oak (#BCAC9B):** A warm, wood-inspired secondary tone used for subtle backgrounds, dividers, and low-priority interactive states.
- **Charcoal (#262626):** The primary color for text and icons, providing high contrast and an "ink-on-paper" feel.
- **Snow (#F9F8F6):** A soft tertiary off-white used for container surfaces to differentiate from the global white background without adding visual weight.

## Typography
Typography is the primary vehicle for the editorial narrative. This design system pairs **Noto Serif** for headlines—providing a timeless, literary authority—with **Manrope** for body and interface text to maintain modern readability and a clean, geometric feel.

Headlines should use generous leading and occasionally negative letter-spacing for large display sizes to mimic premium print layouts. All-caps labels in Manrope should be used for navigation and categorization to provide a structured, architectural rhythm.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model within a maximum container width of 1440px to ensure an editorial composition. The spacing rhythm is intentionally oversized to create the "Airy" aesthetic. 

Key layout principles include:
- **Maximum White Space:** Content should occupy no more than 60-70% of the horizontal viewport on desktop.
- **The "Breath" Rule:** Use `section-gap` between major content blocks to force a pause in the user's journey.
- **Asymmetric Balance:** Align text to the left with wide right margins to mimic magazine column layouts.

## Elevation & Depth
Depth is conveyed through **Low-Contrast Outlines** and **Tonal Layers** rather than shadows. In keeping with the flat, paper-like aesthetic of a coffee-table book:
- Avoid drop shadows entirely. 
- Use 1px solid borders in `Pale Oak` to define boundaries when necessary.
- Use the `Snow` (#F9F8F6) surface to lift content blocks from the `White` (#FFFFFF) background.
- Subtle backdrop blurs may be used for navigation overlays, but they should be nearly transparent, maintaining the "Airy" feel.

## Shapes
The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to preserve the architectural and structural integrity of the editorial grid. Every element—from buttons to image containers—should have crisp, right-angled corners, echoing the edges of a printed page.

## Components
- **Buttons:** Primary buttons are solid Charcoal with White text. Secondary buttons are 1px Charcoal outlines with no fill. All buttons use the `label-caps` typography style.
- **Icons:** Use ultra-thin line icons (0.5px - 1px stroke weight). Icons should never be filled; they function as subtle wayfinding signals.
- **Input Fields:** Minimalist under-lines (bottom border only) rather than enclosed boxes. Labels sit above the line in `label-caps`.
- **Cards:** No borders or shadows. Cards are defined by their internal padding and the use of the `Snow` background color.
- **Chips/Tags:** Small, rectangular boxes with a 1px `Pale Oak` border and `label-caps` text.
- **Imagery:** Photography should be desaturated, high-key, and occupy full-bleed widths or specific grid spans with generous margins.
- **Dividers:** Horizontal lines should be 1px thick in `Pale Oak`, used sparingly to separate distinct editorial chapters.