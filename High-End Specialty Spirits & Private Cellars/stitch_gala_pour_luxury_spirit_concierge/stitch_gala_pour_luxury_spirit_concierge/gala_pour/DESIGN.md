---
name: Gala-Pour
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#b9c7e4'
  on-secondary: '#233148'
  secondary-container: '#3c4962'
  on-secondary-container: '#abb9d6'
  tertiary: '#c0d0e2'
  on-tertiary: '#223240'
  tertiary-container: '#a5b5c6'
  on-tertiary-container: '#374755'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#d4e4f6'
  tertiary-fixed-dim: '#b8c8da'
  on-tertiary-fixed: '#0d1d2a'
  on-tertiary-fixed-variant: '#394857'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 80px
  margin-tablet: 40px
  margin-mobile: 20px
---

## Brand & Style

This design system embodies the "Grand & Atmospheric" aesthetic, targeting a discerning audience seeking exclusivity in luxury spirit gifting and concierge services. The brand personality is authoritative yet welcoming, evocative of a high-end private lounge at midnight. 

The visual style is a hybrid of **Minimalism** and **Glassmorphism**, elevated by **Tactile** accents. It relies on heavy atmospheric depth, where content emerges from a dark, expansive void. High-contrast elements and premium textures (such as brushed metal and grain) create a sense of physical permanence. The emotional response should be one of quiet confidence, prestige, and seamless indulgence.

## Colors

The palette is anchored by **Midnight Blue**, which serves as the deep, immersive foundation for all interfaces. **Rich Gold** is used sparingly but impactfully for primary actions, signatures, and decorative accents, often applied as a subtle metallic gradient to simulate the reflection of light on premium hardware. 

**Smoke** provides the necessary mid-tones for secondary text and borders, bridging the gap between the dark background and light content. The color mode is strictly dark, ensuring that imagery of amber liquids and crystalline glassware glows against the interface. High-contrast white is reserved for maximum legibility in body copy.

## Typography

The typography strategy emphasizes contrast between heritage and modernity. **Playfair Display** is utilized for headlines to convey a sense of editorial prestige and tradition. Large display sizes should use tighter letter spacing to maintain a cohesive, "locked-in" look.

**Montserrat** provides a clean, functional counterpoint for body text and navigation. For labels and micro-copy, increased letter spacing and uppercase styling are used to evoke the feeling of luxury watch faces or high-end bottle engravings. Line heights are generous to ensure an airy, unhurried reading experience.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop and tablet, centered within the viewport to create a cinematic framed effect. A 12-column grid is used for desktop (1440px max-width), while mobile transitions to a 4-column fluid layout.

Spacing is governed by an 8px base unit, but layouts should prioritize "breathtaking" whitespace—large margins and generous vertical gaps between sections to allow high-quality imagery to dominate the visual field. Elements should often overlap or bleed into margins to break the rigidity of the grid and create an immersive, layered depth.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Tonal Layers** rather than traditional shadows. Surfaces closer to the user appear more translucent with a high-density background blur (30px+), mimicking the look of frosted heavy-bottomed glassware.

1.  **Base:** The Midnight Blue void (#050D19).
2.  **Floating Panels:** 40% opacity Midnight Blue with a subtle 1px inner Gold border (0.2 opacity) and heavy backdrop blur.
3.  **Interaction:** Elements "lift" using a soft Gold outer glow (0.15 opacity, 40px blur) to simulate light reflecting off a surface.

Avoid harsh drop shadows. Instead, use soft, tinted ambient occlusion in the Smoke color to ground physical objects like bottle renders.

## Shapes

The shape language is architectural and "Soft" (0.25rem). While circular elements are used for specific iconography, the primary containers and buttons utilize subtle rounding to maintain a sophisticated, masculine edge. 

Large image containers may use a `rounded-lg` (0.5rem) to soften the impact of high-contrast photography. Interactive chips and tags should remain sharp or minimally rounded to differentiate them from more organic, lifestyle content.

## Components

**Buttons:** Primary buttons feature a solid Rich Gold background with dark Midnight Blue text. Secondary buttons are "ghost" style with a 1px Gold border and high-blur glass background. Hover states should trigger a subtle shimmer effect.

**Glass Overlays:** Used for concierge chat windows, filter menus, and product quick-views. These must utilize `backdrop-filter: blur(20px)` to maintain legibility against complex background textures.

**Input Fields:** Minimalist design with only a bottom border in Smoke. On focus, the border transitions to Gold with a soft vertical glow. Labels sit above the field in uppercase Montserrat.

**Cards:** Product cards are borderless, relying on the high-quality imagery of the spirit bottle to define the space. The bottle should appear to "sit" on a glass shelf, with a faint reflection beneath it.

**Iconography:** Use ultra-thin, linear icons (stroke weight 1px or 1.5px) in Gold or Smoke. Icons should be elegant and literal, avoiding overly playful or rounded metaphors.

**Transitions:** All state changes must be "seamless"—using 400ms ease-in-out durations. Page transitions should incorporate a subtle scale-down and fade of the background imagery to maintain the atmospheric immersion.