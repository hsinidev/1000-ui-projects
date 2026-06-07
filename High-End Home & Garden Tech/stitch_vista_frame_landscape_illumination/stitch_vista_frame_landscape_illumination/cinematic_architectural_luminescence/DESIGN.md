---
name: Cinematic Architectural Luminescence
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#ccc3d1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#968e9b'
  outline-variant: '#4a4450'
  surface-tint: '#d8b9ff'
  primary: '#d8b9ff'
  on-primary: '#3f1d6b'
  primary-container: '#310a5d'
  on-primary-container: '#9d7acd'
  inverse-primary: '#6f4e9d'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#d0bcff'
  on-tertiary: '#3b0191'
  tertiary-container: '#2b006f'
  on-tertiary-container: '#9874f1'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#eddcff'
  primary-fixed-dim: '#d8b9ff'
  on-primary-fixed: '#290055'
  on-primary-fixed-variant: '#573583'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e9ddff'
  tertiary-fixed-dim: '#d0bcff'
  on-tertiary-fixed: '#23005c'
  on-tertiary-fixed-variant: '#522aa7'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 64px
---

## Brand & Style

The design system is engineered to evoke the immersive, high-stakes atmosphere of a cinematic production. It targets a discerning audience of luxury homeowners and architects who view lighting not merely as a utility, but as a form of architectural storytelling. The emotional response is one of awe, precision, and exclusivity.

The visual style is a sophisticated fusion of **Glassmorphism** and **High-Contrast Modernism**. By leveraging semi-transparent layers and deep, tonal backgrounds, the interface mimics the behavior of light passing through optical lenses. Every element is designed to feel like a high-end control console, emphasizing depth through subtle gradients and sharp, luminous accents that guide the user through complex spatial configurations with ease.

## Colors

The palette is anchored in a foundation of "Obsidian Black," providing a vacuum-like depth that allows light-based elements to pop. The primary "Royal Amethyst" serves as the core brand color, used in large-scale gradients to suggest the transition from dusk to night.

Gold is utilized exclusively as a functional accent—denoting active states, premium features, and high-value interactions. To maintain the cinematic aesthetic, warm highlights (Amber and Gold) are applied sparingly to simulate the "glow" of real-world landscape lighting. Surface colors are never pure black but rather deep indigos and charcoals to ensure the glassmorphic blurs remain visible and rich.

## Typography

The typography in the design system utilizes **Metropolis** for its geometric precision and architectural clarity. Headings utilize tighter tracking and heavier weights to command attention, while body copy is set with generous line height to ensure legibility against dark, textured backgrounds.

A specialized "Label-Caps" style is used for technical metadata and navigation hints, providing a structured, "blueprint" feel to the interface. The contrast between bold displays and delicate labels reinforces the premium nature of the hardware being controlled.

## Layout & Spacing

The layout follows a mobile-first, fluid grid philosophy. On mobile devices, a 4-column system is used with 24px outer margins to provide "breathing room" for high-resolution imagery. For larger viewports, the system expands to a 12-column grid.

Spacing follows a strict 8px rhythmic scale. We prioritize "Optical Weighting," where interactive elements are surrounded by significant whitespace to prevent accidental triggers in low-light environments. Vertical stacking is aggressive, ensuring that text never competes with the dramatic architectural photography that defines the brand experience.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. We move away from traditional drop shadows in favor of **Glassmorphism and Tonal Layering**.

1.  **Base Layer:** Solid Obsidian Black (#0D0D0D).
2.  **Surface Layer:** Semi-transparent Deep Purple (20% opacity) with a 20px backdrop blur.
3.  **Elevation Highlights:** Top-edge "inner glows" in Gold (10% opacity) create a sense of light hitting the edge of a glass pane.
4.  **Active State:** Increased saturation of the background blur and a subtle 1px Gold border.

This stacking method ensures that the UI feels integrated into the environment rather than sitting on top of it.

## Shapes

The shape language balances organic landscape forms with architectural precision. The standard `rounded-md` (0.5rem) is applied to all primary containers and cards to soften the dark aesthetic and make it feel more approachable. 

Buttons and interactive chips use a higher degree of roundedness (`rounded-xl` or pill-shaped) to clearly distinguish them from structural layout elements. Selection indicators and status pips use perfect circles, mimicking the appearance of light apertures.

## Components

### Buttons
*   **Primary:** Solid Gold background with Black text. No shadow; instead, a faint outer glow using the primary purple.
*   **Secondary:** Glass background (70% blur) with a 1px Gold border.

### Cards & Containers
*   Cards must feature a "Light Leak" gradient—a subtle Purple-to-Transparent linear gradient starting from the top-left corner.
*   Content within cards should be padded at 24px to maintain the premium feel.

### Input Fields
*   Underline-style inputs with floating labels. When active, the underline transforms into a Gold-to-Purple gradient.
*   Mobile sliders (for brightness/warmth) feature a thick, tactile track with a Gold "glow" thumb.

### Additional Components
*   **Scene Selector:** Horizontal scrolling glass chips with high-resolution thumbnail backgrounds.
*   **Projection Map Overlay:** A specialized toggle component that uses a wireframe icon style to represent technical mapping features.
*   **Lume-Slider:** A custom vertical slider for dimming, where the background of the slider itself increases in vibrance as the value rises.