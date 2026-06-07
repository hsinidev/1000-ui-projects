---
name: Aura-Mirror
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#4b463d'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#7d766c'
  outline-variant: '#cec5ba'
  surface-tint: '#685d4a'
  primary: '#685d4a'
  on-primary: '#ffffff'
  primary-container: '#f7e7ce'
  on-primary-container: '#726753'
  inverse-primary: '#d3c5ad'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5d5e64'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e8ef'
  on-tertiary-container: '#66686e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0e0c8'
  primary-fixed-dim: '#d3c5ad'
  on-primary-fixed: '#221b0b'
  on-primary-fixed-variant: '#4f4533'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e2e2e9'
  tertiary-fixed-dim: '#c5c6cd'
  on-tertiary-fixed: '#191c20'
  on-tertiary-fixed-variant: '#45474c'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  gesture-indicator:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin-desktop: 80px
  container-margin-mobile: 24px
  gutter: 24px
  glass-padding: 32px
---

## Brand & Style

This design system is engineered for a high-end, luxury fashion smart mirror experience. It centers on the concept of "The Digital Atelier"—an environment that feels premium, weightless, and highly responsive. The brand personality is sophisticated and avant-garde, targeting a discerning audience that values both couture aesthetics and cutting-edge technology.

The visual language utilizes **Glassmorphism** as its primary driver. UI elements should never compete with the user's reflection or the high-fidelity fashion photography; instead, they should appear as frosted, ethereal overlays that float on the glass surface. The emotional response is one of calm, effortless luxury, achieved through generous whitespace, high-performance motion, and tactile gesture-based interactions.

## Colors

The palette is a curated selection of "Soft Champagne," "Slate," and "Silk White." 

*   **Soft Champagne (#F7E7CE)**: Used for primary accents, active states, and call-to-action borders. It provides a warm, metallic glow against the cool mirror surface.
*   **Slate (#708090)**: Used for secondary UI elements, iconography, and text that requires a softer contrast than pure black.
*   **Silk White (#F8F8FF)**: The base for all glass surfaces and primary typography. It ensures maximum legibility against varying reflections.
*   **Glass Layers**: Surfaces use a semi-transparent Silk White with a backdrop-filter (blur) to create the frosted glass effect.

## Typography

The typography strategy balances the editorial elegance of fashion magazines with the functional clarity of a smart interface.

*   **Headlines**: Playfair Display is utilized for all editorial content, product names, and section headers. It should be typeset with tight tracking to emphasize its high-contrast strokes.
*   **UI & Body**: Inter provides the functional backbone. It is chosen for its exceptional legibility at small scales and its neutral, modern character which doesn't distract from the photography.
*   **Specialty**: Small-caps labels in Inter are used for "Gesture-Control" hints and technical metadata (e.g., fabric composition, sizing).

## Layout & Spacing

The layout is a **Fixed Grid** system designed to sit within the peripheral view of the mirror, keeping the center clear for the user's reflection. 

*   **Desktop (Mirror Aspect)**: A 12-column grid with wide 80px margins. Primary UI controls are docked to the lower third or the sides for easy reach during gesture interaction.
*   **Mobile (Companion App)**: A 4-column fluid grid that mirrors the mirror's aesthetic but optimizes for touch.
*   **Spacing Rhythm**: An 8px base unit drives all padding and margins. Vertical rhythm is generous to maintain the minimalist, airy feel of a luxury boutique.

## Elevation & Depth

Depth is conveyed through optical physics rather than heavy shadows.

*   **Backdrop Blur**: All primary surfaces use a `32px` to `48px` backdrop-filter blur. This separates the UI from the reflection without using opaque colors.
*   **Layering**: Content is organized in "Z-space." Base informational cards sit at a lower blur level, while active interactive elements (like gesture menus) have a higher blur and a subtle Soft Champagne inner-glow.
*   **Shadows**: Use highly diffused, low-opacity Slate-tinted shadows (`rgba(112, 128, 144, 0.1)`) to provide a "lift" from the glass surface. Avoid hard edges or heavy blacks.

## Shapes

The shape language is "Softly Architectural." 

*   **Corners**: A default radius of `0.5rem` (8px) is applied to all glass cards and input fields to soften the technological feel. 
*   **Large Containers**: Product modules and video draping overlays use `1rem` (16px) for a more organic, inviting appearance.
*   **Interactive Targets**: Gesture-control rings and circular buttons use a full pill/circle shape to signify "touchless" interaction zones.

## Components

### Buttons & Interaction
Buttons are "Ethereal Tactile." They feature a Silk White glass base with a 1px Soft Champagne border. On hover or gesture focus, the border thickness increases, and the backdrop blur intensifies. 

### Gesture-Control Indicators
A unique component to this system: a pulsing, semi-transparent ring that follows the user's hand position. It changes color from Silk White to Soft Champagne when a "select" gesture is detected.

### Glass Cards
Cards for fashion photography should have no solid background. They use a frosted glass effect with a subtle "inner-sheen" (a 1px top-left gradient stroke) to mimic the edge of a physical mirror.

### Video Draping Overlays
When viewing video draping (AR clothing), UI controls are minimized to the bottom edge. Labels use the "label-caps" typography to remain unobtrusive.

### Input Fields
Minimalist underlines or very light glass-frosted troughs. The focus state transitions the underline from Slate to Soft Champagne with a soft outer glow.