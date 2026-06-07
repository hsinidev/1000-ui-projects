---
name: Spatial Narrative
colors:
  surface: '#fcf9f5'
  surface-dim: '#dcdad6'
  surface-bright: '#fcf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ef'
  surface-container: '#f0ede9'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e5e2de'
  on-surface: '#1c1c1a'
  on-surface-variant: '#444748'
  inverse-surface: '#31302e'
  inverse-on-surface: '#f3f0ec'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5f5e5c'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfdc'
  on-secondary-container: '#636260'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1c18'
  on-tertiary-container: '#86837e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e5e2df'
  secondary-fixed-dim: '#c8c6c3'
  on-secondary-fixed: '#1c1c1a'
  on-secondary-fixed-variant: '#474745'
  tertiary-fixed: '#e6e2dc'
  tertiary-fixed-dim: '#cac6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#484742'
  background: '#fcf9f5'
  on-background: '#1c1c1a'
  surface-variant: '#e5e2de'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 28px
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
    lineHeight: '1.0'
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
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

The brand personality is anchored in architectural precision and quiet luxury. It aims to evoke a sense of calm, curated space, treating the digital interface as a gallery for physical form. The target audience consists of design professionals and discerning homeowners who value intentionality over abundance.

The design style follows a **Minimalist Architectural** approach. It prioritizes structural hierarchy and significant negative space to allow high-fidelity product photography to breathe. The "Spatial UX" focus is achieved through subtle depth, overlapping layers, and a refined sense of scale, creating an immersive experience that mirrors the feeling of walking through a high-end furniture showroom.

## Colors

The palette is strictly neutral and temperature-controlled to ensure a "warm" minimalist feel. 

- **Primary (Deep Charcoal):** Used for critical typography, iconography, and structural lines. It provides the "ink" that defines the space.
- **Secondary (Soft White/Stone):** The foundational canvas. It is slightly off-white to reduce eye strain and feel more like natural plaster or textile than a digital screen.
- **Tertiary (Warm Gray):** Used for subtle UI differentiation, such as hover states or secondary containers.
- **Neutral (Muted Slate):** Reserved for metadata, disabled states, and utility text.

Backgrounds should primarily use the secondary color, with charcoal used sparingly for high-contrast call-to-action areas.

## Typography

This design system utilizes a sophisticated typographic pairing to balance heritage and modernity.

- **Headlines (Noto Serif):** Set with generous leading and occasional negative letter-spacing for large displays. The serif choice brings an editorial, premium feel that references high-end interior design journals.
- **Body & UI (Manrope):** A refined sans-serif that provides exceptional legibility and a geometric cleanliness. It acts as the functional engine of the interface.
- **Labels:** Use uppercase Manrope with increased letter-spacing to denote categories, breadcrumbs, and small utility markers, mimicking architectural blueprints.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** with an emphasis on "macro-spacing." While a 12-column grid is used for alignment, elements are often offset to create a more dynamic, editorial rhythm.

- **Vertical Rhythm:** Large gaps (section-gap) are used to separate distinct product narratives, preventing the interface from feeling cluttered.
- **Margins:** Exceptionally wide edge margins (64px+) ensure that content feels framed and intentional, like a piece of art on a wall.
- **Guttering:** 32px gutters provide a clear "air gap" between architectural elements of the page.

## Elevation & Depth

Depth in this design system is conveyed through **Tonal Layers** and **Ambient Shadows** rather than traditional skeuomorphism.

- **Surfaces:** Use subtle shifts between the secondary (Soft White) and tertiary (Warm Gray) colors to define hierarchy. Background elements remain flat, while interactive "Spatial" elements may use a slight backdrop blur (Glassmorphism) when overlapping imagery.
- **Shadows:** When used, shadows should be extremely diffused and low-opacity (2-4%), utilizing a warm tint rather than pure black to simulate natural light falling on furniture.
- **Outlines:** Low-contrast, 1px charcoal borders (at 10-15% opacity) are used to define boundaries without adding visual weight.

## Shapes

The shape language is primarily **Soft** and structured. 

A base radius of 4px (0.25rem) is used for most UI elements like input fields and buttons to take the "edge" off the minimalism without losing the architectural rigor. Large product cards or immersive containers may use up to 8px (0.5rem) to feel more approachable. Circles are used exclusively for small UI triggers (e.g., color swatches or close buttons) to contrast against the dominant rectangular grid.

## Components

Components in this design system are treated as functional sculptures.

- **Buttons:** Primary buttons are solid Charcoal with White text, using a rectangular shape with a 4px radius. Secondary buttons use a "Ghost" style with a 1px border and no fill.
- **Input Fields:** Minimalist under-line or subtle 4-sided borders with high padding. Labels are always set in the `label-caps` style for clarity.
- **Cards:** Product cards are borderless, using large-scale imagery and a subtle background fill. Text is aligned to the bottom-left or top-right to create "negative space" within the card itself.
- **Chips/Filters:** Small, pill-shaped elements with light-gray fills, used to categorize furniture by material or room.
- **Spatial Overlays:** Full-screen modal windows that use a high-blur backdrop to keep the user focused on the specific product details while maintaining a sense of the "room" behind it.
- **Navigation:** A persistent, minimal top-bar with plenty of horizontal space between links. The logo is always centered to maintain symmetry.