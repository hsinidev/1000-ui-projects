---
name: Soft-Luxe Tactility
colors:
  surface: '#fff7ff'
  surface-dim: '#e0d7e2'
  surface-bright: '#fff7ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf1fc'
  surface-container: '#f4ebf6'
  surface-container-high: '#eee5f1'
  surface-container-highest: '#e8e0eb'
  on-surface: '#1e1a22'
  on-surface-variant: '#48464e'
  inverse-surface: '#332f37'
  inverse-on-surface: '#f7eef9'
  outline: '#78767f'
  outline-variant: '#c9c5cf'
  surface-tint: '#5e5983'
  primary: '#5e5983'
  on-primary: '#ffffff'
  primary-container: '#d6cfff'
  on-primary-container: '#5c5780'
  inverse-primary: '#c8c1f0'
  secondary: '#516161'
  on-secondary: '#ffffff'
  secondary-container: '#d4e6e5'
  on-secondary-container: '#576867'
  tertiary: '#5e5e5d'
  on-tertiary: '#ffffff'
  tertiary-container: '#d5d4d2'
  on-tertiary-container: '#5b5c5a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5deff'
  primary-fixed-dim: '#c8c1f0'
  on-primary-fixed: '#1b163b'
  on-primary-fixed-variant: '#474269'
  secondary-fixed: '#d4e6e5'
  secondary-fixed-dim: '#b8cac9'
  on-secondary-fixed: '#0e1e1e'
  on-secondary-fixed-variant: '#3a4a49'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#fff7ff'
  on-background: '#1e1a22'
  surface-variant: '#e8e0eb'
typography:
  headline-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: notoSerif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: plusJakartaSans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: plusJakartaSans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: plusJakartaSans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-lg:
    fontFamily: plusJakartaSans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-md:
    fontFamily: plusJakartaSans
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
This design system centers on a "Soft-Luxe" aesthetic, merging the high-end exclusivity of limited-edition designer textiles with a cozy, approachable interface. The brand personality is premium yet comforting, evoking the sensation of touching a high-quality plush toy. 

The visual style is rooted in Neumorphism (Soft-UI), utilizing subtle light and shadow play to create an interface that feels physically extruded from the screen. The target audience values craftsmanship and sensory experiences; therefore, the digital environment must feel as "squishy" and tactile as the physical products it showcases. The emotional response should be one of calm, indulgence, and tactile delight.

## Colors
The palette is inspired by high-end natural fibers and pastel dyes. 
- **Primary (Lavender):** Used for key interactive elements and soft accents. It should feel airy, not electric.
- **Secondary (Mint):** Provides a fresh, organic contrast, used for success states or supportive callouts.
- **Tertiary (Silk White):** The foundational surface color. It is a warm, slightly off-white that prevents screen glare and feels more "fabric-like" than pure hex white.
- **Neutral:** A deep, desaturated plum-grey used for typography to maintain high legibility without the harshness of pure black.

Shadows and highlights are derived from these base tones: highlights are pure white (#FFFFFF), while shadows are a slightly darker, more saturated version of the background color to maintain a clean, "soft-glow" appearance.

## Typography
The typographic hierarchy relies on the contrast between an elegant, literary serif and a friendly, rounded sans-serif. 

**notoSerif** is utilized for all editorial headlines. Its refined stems and classic proportions signal "Limited Edition" quality and tradition. 

**plusJakartaSans** is the workhorse for body and functional text. Its naturally rounded terminals complement the organic shape language of this design system and ensure that even the smallest labels feel soft and approachable. All labels should be set in uppercase with slight tracking to increase breathability.

## Layout & Spacing
The layout follows a fluid grid with generous, "airy" margins to reinforce the premium feel. Rather than packing information tightly, this design system prioritizes whitespace to let product imagery breathe.

A 12-column grid is standard for desktop, but spacing is driven by a soft 8px rhythm. Components should use large internal padding (md or lg) to enhance the "squishy" tactile feel—elements should look like they have physical volume. Section transitions should be wide (xl) to create a sense of calm during the browsing experience.

## Elevation & Depth
Depth is the defining characteristic of this design system. We move away from traditional "Z-index" stacking and toward "surface deformation."

1.  **Extrusion (Raised):** Used for primary buttons and interactive cards. This is achieved through dual shadows: a light highlight (#FFFFFF) at -6px, -6px and a soft tint-shadow (15% opacity of the background’s darker variant) at 6px, 6px.
2.  **Depression (Inset):** Used for input fields and active button states. This creates the illusion of the surface being pressed inward.
3.  **Soft Diffusion:** Shadows must have a high blur radius (typically 2x the offset) to ensure the edges feel pillowy rather than sharp or "plastic."

## Shapes
The shape language is organic and soft. There are no sharp corners in this design system. 

Base components like cards and containers use a 0.5rem (8px) radius, while "high-touch" elements like buttons and chips utilize even more aggressive rounding (up to pill-shaped) to invite interaction. Containers that house textile swatches or plush photography should use "super-ellipses" or organic rounded corners to mimic the irregular, soft nature of fabric.

## Components
- **Buttons:** Primary buttons must appear "raised" from the surface. Upon hover, the elevation should slightly increase; upon click, the button should transition to an "inset" state, providing a physical-feeling click response.
- **Cards:** Product cards use the silk-white background with a soft, raised elevation. They should have no visible border; depth alone defines the boundary.
- **Input Fields:** Search bars and form fields should be "recessed" (inset shadow) into the background, making them look like soft indentations ready to be filled.
- **Chips/Tags:** Used for "Limited Edition" or "In Stock" labels, these should be fully pill-shaped with a very subtle secondary-color (mint) glow.
- **Textile Swatches:** Large, rounded squares with a subtle inner stroke to define texture boundaries, using the same "raised" elevation as buttons to make them feel like they can be grabbed.
- **Navigation:** Top-level navigation is minimalist, relying on typography rather than boxes, to maintain a clean, editorial aesthetic.