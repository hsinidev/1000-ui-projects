---
name: Galaxy-Concierge
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e4e2e3'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e4e2e3'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bec6dc'
  primary: '#bec6dc'
  on-primary: '#283041'
  primary-container: '#020817'
  on-primary-container: '#71798c'
  inverse-primary: '#565e71'
  secondary: '#c5c7c8'
  on-secondary: '#2e3132'
  secondary-container: '#494c4d'
  on-secondary-container: '#babcbd'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#070909'
  on-tertiary-container: '#787979'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe2f8'
  primary-fixed-dim: '#bec6dc'
  on-primary-fixed: '#131c2b'
  on-primary-fixed-variant: '#3f4758'
  secondary-fixed: '#e1e3e4'
  secondary-fixed-dim: '#c5c7c8'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#454748'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131315'
  on-background: '#e4e2e3'
  surface-variant: '#353436'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
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
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
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
  container-max: 1440px
  gutter: 32px
  margin-desktop: 80px
  margin-tablet: 40px
  margin-mobile: 24px
---

## Brand & Style
The brand personality is defined by an air of "Cosmic Quiet"—a sophisticated, elite assistant that operates with effortless precision. The target audience includes ultra-high-net-worth orbital travelers and interstellar commuters who value serenity and clarity over complexity. 

The UI adopts a **Minimalist-Refined** style with heavy influences from **Glassmorphism**. The visual narrative is built on the concept of "weightlessness," achieved through generous negative space, hair-line strokes, and subtle translucent layers. The emotional response is one of safety, luxury, and expansive calm, mirroring the vastness of space but filtered through a lens of high-end terrestrial hospitality.

## Colors
This design system utilizes a deep, immersive palette. **Midnight Blue (#020817)** serves as the primary canvas, providing a sense of depth and infinite space. **Silk White (#F8F9FA)** is used for primary text and high-contrast surfaces, ensuring legibility against the dark background. 

**Silver (#C0C0C0)** acts as the functional accent color, reserved for thin-line borders, vector iconography, and secondary metadata. For interactive glass elements, a nearly transparent white fill is paired with a faint silver border to simulate the glint of a spacecraft viewport.

## Typography
The typography strategy prioritizes architectural structure and breathability. **Space Grotesk** is used for headings to introduce a subtle technical edge that feels both futuristic and premium; its letter spacing is intentionally widened to evoke a sense of scale. 

**Manrope** provides a balanced, calming experience for body copy, ensuring long-form itinerary details are easy to digest. For technical readouts and labels, **Geist** offers a precise, monospaced-adjacent aesthetic that reinforces the "concierge" aspect of the service. All uppercase labels should utilize increased tracking (0.1em) to maintain the refined minimalist feel.

## Layout & Spacing
This design system employs a **Fixed Grid** model on desktop to maintain a sense of curated, editorial control, transitioning to a fluid model for mobile. The layout is defined by exceptionally "Wide Margins" (80px on desktop) to ensure content never feels cramped, mirroring the luxury of open space.

A 12-column grid is utilized for data visualization, while single-column centered layouts are preferred for personal assistant interactions. Spacing rhythm follows an 8px base unit, but emphasizes large vertical gaps (64px+) between major sections to allow the user's eye to rest.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and tonal stacking rather than traditional shadows. Surfaces are layered as follows:
- **Base Level:** Midnight Blue background.
- **Surface Level:** 3% white fill with a 24px backdrop blur and a 0.5px silver stroke.
- **Interactive Level:** 6% white fill, increasing the "glow" of the silver border.

Shadows, when used, are "Ambient Glows"—extremely diffused (40px-60px blur) with 5% opacity, using the primary background color to subtly lift elements without creating harsh edges.

## Shapes
The shape language is "Soft-Precision." We use a conservative roundedness level (0.25rem) to maintain a crisp, professional appearance that isn't as aggressive as sharp corners nor as casual as pill shapes. This precision reflects the engineering excellence of space travel. Larger containers like "Data Cards" may scale up to `rounded-lg` (0.5rem) to soften the overall interface.

## Components
- **Buttons:** Ghost-style by default with a 0.5px Silver border. Hover states trigger a subtle internal Silk White glow. Text is always `label-sm` for an understated look.
- **Data Cards:** Sophisticated containers using the Glassmorphism specification. They feature no fill, relying entirely on the backdrop blur and the thin silver stroke to define their boundaries.
- **Progress Trackers:** Horizontal 1px Silver lines. Completed stages are marked by a 4px Silk White dot; the current stage features a soft 12px radial glow.
- **Timelines:** Vertical 0.5px Silver strokes with "Silk White" typography aligned to the left. Elegant and sparse, using `label-sm` for timestamps.
- **Input Fields:** Bottom-border only (1px Silver). Focus states animate the border to Silk White. Placeholder text uses `Manrope` at 40% opacity.
- **Vector Icons:** Custom 1px weight stroke icons. No fills are allowed; all icons must be open-path to maintain the "weightless" aesthetic.