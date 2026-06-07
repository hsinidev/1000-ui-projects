---
name: Haptic-Luxe
colors:
  surface: '#fbf8fb'
  surface-dim: '#dcd9dc'
  surface-bright: '#fbf8fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f5'
  surface-container: '#f0edef'
  surface-container-high: '#eae7ea'
  surface-container-highest: '#e4e2e4'
  on-surface: '#1b1b1d'
  on-surface-variant: '#4d4635'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f2'
  outline: '#7f7663'
  outline-variant: '#d0c5af'
  surface-tint: '#735c00'
  primary: '#735c00'
  on-primary: '#ffffff'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#e9c349'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5d5f5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#b2b3af'
  on-tertiary-container: '#444543'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e2e3df'
  tertiary-fixed-dim: '#c6c7c3'
  on-tertiary-fixed: '#1a1c1a'
  on-tertiary-fixed-variant: '#454745'
  background: '#fbf8fb'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  body-rg:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-xs:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
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
  container-max: 1440px
  gutter: 24px
  margin-edge: 40px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style
The design system centers on the intersection of high-end craftsmanship and digital intimacy. It targets a discerning clientele who values the "Digital Touch"—the tactile sensation of jewelry even through a screen. The style is a hybrid of **Minimalism** and **Tactile Refinement**, utilizing heavy whitespace to frame high-resolution macro photography of gold grains, stone settings, and polished surfaces.

The emotional response is one of absolute trust, serenity, and weight. Every interaction should feel intentional and dampened, avoiding jarring transitions in favor of soft-glow "aura" effects that simulate the warmth of light reflecting off precious metals.

## Colors
The palette is anchored by **Champagne Gold**, used sparingly for high-value actions and focal points. **Pearl** serves as the primary canvas color, providing a warmer, more organic foundation than pure white. **Slate** is utilized for supportive elements and secondary text, grounding the airiness of the Pearl with a metallic, cool-toned weight.

- **Primary:** Champagne Gold (#D4AF37) — Reserved for "Touch" states and luxury accents.
- **Secondary:** Slate (#708090) — Used for icons and secondary buttons.
- **Surface:** Pearl (#F5F5F1) — The primary background for all layouts.
- **Text:** Deep Charcoal (#2C2C2E) — For maximum legibility against Pearl surfaces.

## Typography
The typographic hierarchy contrasts the classical elegance of **EB Garamond** with the precision of **Manrope**. 

Headlines utilize EB Garamond with tight letter-spacing to evoke the feeling of a bespoke editorial. Body copy is set in Manrope to ensure effortless readability across all device sizes. Functional labels and small metadata use increased letter-spacing and uppercase styling to provide a modern, architectural counterpoint to the fluid serif headers.

## Layout & Spacing
This design system employs a **Fixed Grid** model for desktop to maintain the integrity of macro-photography crops, while transitioning to a fluid model for mobile. 

A 12-column grid is used with generous 40px external margins to create a sense of "gallery space." The vertical rhythm is governed by a strict 8px baseline, but large-scale components should utilize the "stack-lg" (64px) spacing to prevent the UI from feeling cluttered, emphasizing the minimalist brand pillar.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** and **Luminous Layers**. Rather than harsh drop shadows, this design system uses highly diffused, low-opacity shadows (Blur: 30px, Opacity: 4%) to simulate objects resting on a soft surface.

The "Digital Touch" is represented by a **Soft-Glow Effect**. When an element is hovered or focused, a subtle Champagne Gold outer glow (#D4AF37 at 20% opacity) emanates from the object, suggesting a physical energy or connection. Semi-transparent Pearl overlays are used for modals to maintain a sense of material continuity.

## Shapes
Shapes are **Organic and Rounded**. Sharp corners are avoided to mirror the natural ergonomics of fine jewelry. 

Standard components (buttons, inputs) use a 0.5rem radius, while large "Collection Cards" and image containers utilize 1.5rem to create a softer, more inviting visual flow. Circular containers are reserved specifically for interactive "Touch points" or gemstone selectors.

## Components

- **Primary Buttons:** High-contrast Slate background with Pearl text. Upon interaction, the button develops a soft Champagne Gold glow.
- **Digital Touch Chips:** Used for tactile feedback points. These are circular, featuring a faint ripple animation that triggers when the user's cursor or finger dwells on the element.
- **Input Fields:** Minimalist "Underline" style with a Pearl-weighted background. The label floats upward and shifts to Champagne Gold when focused.
- **Product Cards:** Borderless designs that rely on ambient shadows and generous padding. Photography should bleed to the top and sides, with text centered at the bottom.
- **Craftsmanship Lists:** Used for detailing materials (e.g., 18k Gold). Each list item is separated by a faint Slate hairline and features a macro-thumbnail of the material.
- **Haptic Feedback Indicator:** A specialized UI element (a small, glowing dot) that follows the cursor or appears on tap to acknowledge the "Digital Touch" interaction.