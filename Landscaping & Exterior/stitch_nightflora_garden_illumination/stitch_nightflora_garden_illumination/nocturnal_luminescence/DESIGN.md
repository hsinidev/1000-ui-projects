---
name: Nocturnal Luminescence
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#d6c3b0'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#9f8e7c'
  outline-variant: '#524535'
  surface-tint: '#ffb95a'
  primary: '#ffd7a9'
  on-primary: '#462a00'
  primary-container: '#ffb347'
  on-primary-container: '#704700'
  inverse-primary: '#845400'
  secondary: '#bec6e3'
  on-secondary: '#283046'
  secondary-container: '#3e465e'
  on-secondary-container: '#adb4d1'
  tertiary: '#dedee3'
  on-tertiary: '#2f3035'
  tertiary-container: '#c1c2c7'
  on-tertiary-container: '#4e5054'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb6'
  primary-fixed-dim: '#ffb95a'
  on-primary-fixed: '#2a1800'
  on-primary-fixed-variant: '#643f00'
  secondary-fixed: '#dae2ff'
  secondary-fixed-dim: '#bec6e3'
  on-secondary-fixed: '#131b30'
  on-secondary-fixed-variant: '#3e465e'
  tertiary-fixed: '#e2e2e8'
  tertiary-fixed-dim: '#c6c6cc'
  on-tertiary-fixed: '#1a1c20'
  on-tertiary-fixed-variant: '#45474b'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The design system is rooted in the interplay of shadow and light, designed to evoke the quiet luxury of a curated midnight garden. The brand personality is mysterious, sophisticated, and authoritative, targeting high-end homeowners and landscape architects who view lighting as an architectural element rather than a utility.

The aesthetic utilizes a blend of **Minimalism** and **Glassmorphism**. By employing deep, desaturated backgrounds and vibrant, warm accents, the UI mirrors the physical experience of architectural lighting in the dark. Content is staged like a gallery, using expansive negative space to allow high-fidelity photography and amber highlights to guide the user’s eye.

## Colors
This design system operates exclusively in a dark mode environment to maintain the atmospheric narrative. 
- **Primary (Amber Glow):** Used sparingly for interactive elements, call-to-actions, and status indicators. It represents the "light" within the dark.
- **Secondary (Midnight Blue):** Used for primary surfaces and container backgrounds to provide depth beyond flat black.
- **Tertiary (Charcoal):** The base canvas color, providing a heavy, grounded foundation.
- **Neutral (Slate/Silver):** Used for secondary text and borders, ensuring legibility without breaking the moody aesthetic.

## Typography
The typographic strategy balances the classic elegance of **Noto Serif** for editorial headlines with the technical precision of **Manrope** for functional text. Headlines should use "sentence case" to maintain a modern feel. For high-impact moments, increase the tracking on uppercase labels to reinforce the premium, spacious architectural feel.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop to maintain tight control over the visual "staging" of elements. A 12-column grid is used with generous margins to create a cinematic widescreen effect. 

Spacing is rhythmic and intentional, leaning toward larger gaps (stack-lg) between sections to prevent the interface from feeling cluttered. Content should be center-aligned in the viewport to emphasize focus and symmetry.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Ambient Shadows**. Instead of traditional drop shadows, this design system uses soft, colored glows (Amber #FFB347 at 10-15% opacity) to suggest that a component is "lit" from within.

- **Level 0 (Canvas):** Charcoal (#0F1115).
- **Level 1 (Cards/Containers):** Midnight Blue (#1A2238) with a 1px stroke of Charcoal Light (#2D343F).
- **Level 2 (Modals/Popovers):** Midnight Blue with a subtle background blur (8px) and an outer amber bloom effect.
- **Glassmorphism:** Use semi-transparent Midnight Blue (80% opacity) with a backdrop-filter blur for navigation bars to allow background content to bleed through softly.

## Shapes
The shape language is "Soft" (0.25rem). This choice maintains the sharp, architectural precision of landscape design while providing just enough radius to feel approachable and modern. Large image containers and primary buttons may use `rounded-lg` (0.5rem) to create a subtle focus on "objects," but the overall system avoids circular or pill-shaped elements to remain sophisticated.

## Components
- **Buttons:** Primary buttons are solid Charcoal with Amber text and a 1px Amber border. On hover, they should emit a soft Amber outer glow. Secondary buttons use a transparent background with a thin Slate border.
- **Input Fields:** Dark Midnight Blue backgrounds with bottom-only borders. Focus states transition the border from Slate to Amber.
- **Cards:** Use "Glassmorphism" for card overlays. Images should have a subtle dark gradient overlay at the bottom to ensure white text legibility.
- **Chips/Tags:** Small, uppercase labels with high letter spacing, enclosed in a subtle 1px stroke. No solid background fills.
- **Lighting Controls (Custom):** Use vertical sliders with a gradient track (Charcoal to Amber) to mimic the intensity of a light beam.
- **Interactive Maps:** Use a custom "Dark" map style with roads in Charcoal and water in Midnight Blue, using Amber pins to represent light fixtures.