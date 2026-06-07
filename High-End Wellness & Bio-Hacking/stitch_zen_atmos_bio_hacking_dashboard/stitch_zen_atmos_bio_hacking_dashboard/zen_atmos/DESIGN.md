---
name: Zen-Atmos
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
  on-surface-variant: '#45474c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#76777c'
  outline-variant: '#c6c6cc'
  surface-tint: '#585e6d'
  primary: '#1a202c'
  on-primary: '#ffffff'
  primary-container: '#2f3542'
  on-primary-container: '#989dad'
  inverse-primary: '#c1c6d7'
  secondary: '#7c5730'
  on-secondary: '#ffffff'
  secondary-container: '#fdcb9b'
  on-secondary-container: '#79542d'
  tertiary: '#1d2022'
  on-tertiary: '#ffffff'
  tertiary-container: '#323538'
  on-tertiary-container: '#9b9ea0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde2f3'
  primary-fixed-dim: '#c1c6d7'
  on-primary-fixed: '#161c28'
  on-primary-fixed-variant: '#414754'
  secondary-fixed: '#ffdcbd'
  secondary-fixed-dim: '#eebd8e'
  on-secondary-fixed: '#2c1600'
  on-secondary-fixed-variant: '#61401b'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#44474a'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-base:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  container-padding: 32px
  gutter: 24px
  section-gap: 64px
---

## Brand & Style

The design system is centered on the intersection of biological well-being and high-end technological precision. It targets a discerning audience that views health as the ultimate luxury, requiring an interface that feels more like a high-end sanctuary than a laboratory.

The aesthetic utilizes a refined **Neumorphic (Soft-UI)** approach. Unlike the early, heavy versions of this style, this design system uses extremely subtle tonal shifts and soft, diffused shadows to create the illusion that elements are physically molded from the interface surface. The atmosphere is professional, calming, and deeply intentional, prioritizing "digital silence" to reduce cognitive load and promote physiological regulation.

## Colors

The palette is anchored by a sophisticated Slate Grey for critical data and Pure White for clinical clarity. The Warm Wood accent provides a biological connection, preventing the interface from feeling sterile.

### Night-Mode (Circadian Optimization)
A core feature of this design system is the "Circadian Mode." When active, the palette shifts entirely to eliminate blue light. All neutrals transition to deep ambers and soft ochres, and the Slate Grey is replaced with a warm charcoal.

### Surface Tones
Because Neumorphism requires a mid-tone background to allow for both "light" and "dark" shadows, the primary background is a very pale, cool grey (#F0F2F5), rather than pure white. Pure White is reserved for high-intensity highlights or text on dark backgrounds.

## Typography

The design system utilizes **Manrope** for its exceptional balance between geometric precision and humanist warmth. 

- **Headlines:** Use lighter weights (300) for large display text to emphasize elegance, and medium weights (500) for section headers to ensure hierarchy.
- **Data Points:** Air quality indices and EMF readings should use a slightly increased letter-spacing to improve legibility at a glance.
- **Labels:** Small labels use an uppercase treatment with generous tracking to provide a technical, high-end instrument feel.

## Layout & Spacing

The layout philosophy emphasizes "Breatheability." It uses a **fixed-grid system** on desktop and a **fluid-margin system** on mobile. 

Generous negative space is mandatory to prevent the Neumorphic shadows from feeling cluttered. Elements are grouped into soft-edged containers with significant internal padding (32px) to maintain the "luxury" feel. Layouts should be center-aligned and symmetrical where possible to evoke a sense of balance and zen.

## Elevation & Depth

This design system eschews traditional stacking. Instead, depth is created through "Extrusion" and "Inclusion."

- **Extruded (Raised):** Created using two shadows: a light shadow (Pure White, -5px -5px, 15px blur) on the top-left and a dark shadow (Slate Grey at 10% opacity, 5px 5px, 15px blur) on the bottom-right.
- **Inset (Recessed):** Used for input fields and active button states. This is the inverse of the extruded shadow, placed inside the element's border.
- **Glass Blur:** Only used for persistent navigation bars, employing a high-intensity backdrop blur (20px) to maintain context without visual noise.

## Shapes

The design system uses highly organic, rounded surfaces. Sharp corners are avoided entirely as they trigger a "threat" response in the subconscious; instead, 16px to 24px corner radii (Level 2) are standard for all containers. 

Interactive elements like toggles and chips should use "Squircle" shapes—mathematically smoothed rounding—to reinforce the premium, custom-engineered feel of the product.

## Components

### Buttons & Controls
Buttons appear as "molded" parts of the background. In their default state, they are extruded. On tap, they transition to an inset (sunken) state. The Warm Wood (#A67C52) color is used sparingly for primary actions, applied as a glowing text color or a soft inner-glow rather than a solid flat block.

### Bio-Metric Cards
Cards for Air Quality and EMF Shielding should include "Status Halos"—thin, soft-glowing rings around the card perimeter that shift from Warm Wood (Optimal) to a muted Slate (Neutral).

### Environment Toggles
Switches for EMF shielding or Air Purification should be tactile, resembling high-end physical hardware. Use the Neumorphic inset style for the track and the extruded style for the thumb.

### Gauges
Environmental data is visualized through "Atmospheric Gauges"—circular rings that use soft blurs instead of hard lines to represent data ranges, maintaining the calming aesthetic even when reporting sub-optimal levels.