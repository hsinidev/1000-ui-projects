---
name: Modern Studio Audio
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#d8c3b4'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#a08d80'
  outline-variant: '#524439'
  surface-tint: '#ffb77b'
  primary: '#ffb77b'
  on-primary: '#4d2700'
  primary-container: '#c8803f'
  on-primary-container: '#432100'
  inverse-primary: '#8c4f10'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc2'
  primary-fixed-dim: '#ffb77b'
  on-primary-fixed: '#2e1500'
  on-primary-fixed-variant: '#6d3a00'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
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
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 64px
---

## Brand & Style

This design system is built for an elite tier of audio enthusiasts and professional installers. It evokes the feeling of a private, high-end recording studio at midnight: focused, powerful, and impeccably engineered. The brand personality is authoritative yet understated, prioritizing technical precision over flashy ornamentation.

The visual style is a fusion of **Minimalism** and **Modern Studio** aesthetics. It utilizes deep blacks and charcoal tones to create a sense of infinite depth, allowing the hardware and interface elements to emerge through sharp lines and high-contrast copper accents. The emotional response should be one of "immersion"—the interface should feel as high-fidelity as the audio equipment it controls.

## Colors

The palette is strictly nocturnal. The foundation is **Deep Black (#000000)** for primary backgrounds to ensure absolute contrast with copper elements. **Charcoal (#121212)** is used for surface containers and interactive components to provide subtle separation without breaking the dark-room immersion.

**Copper (#B87333)** is the sole highlight color, used sparingly for critical actions, active states, and technical data points. To enhance the "premium" feel, copper elements are often accompanied by a subtle 10-20px radial blur (glow) to simulate the warmth of vacuum tubes or indicator lights in a darkened studio.

## Typography

The typographic hierarchy relies on the tension between the technical, geometric nature of **Space Grotesk** and the refined, Swiss-inspired legibility of **Manrope**.

Headings are set in Space Grotesk with tight letter-spacing to create a "machined" look. H1 and H2 levels should be used to anchor the page, often in pure white against the black background. Body text uses Manrope to ensure effortless readability of technical specifications and long-form brand stories. High-contrast is key: use pure white for primary content and a muted silver-grey for secondary metadata.

## Layout & Spacing

This design system employs a **Fixed Grid** model (12 columns) for desktop experiences to maintain the "Letterboxed" cinematic feel. Content is centered with generous outer margins, forcing the user's focus toward the core interactive elements.

Spacing follows a strict 8px rhythmic unit. While spacing between disparate sections is large (80px+) to allow the design to "breathe," internal component spacing is kept tight (12px-24px) to emphasize technical precision and hardware-inspired density.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** rather than traditional drop shadows. In a premium audio context, we avoid "floating" elements. Instead, surfaces feel nested or machined into one another.

- **Level 0 (Floor):** Deep Black (#000000) for the main viewport background.
- **Level 1 (Plinth):** Charcoal (#121212) for primary cards or section blocks.
- **Level 2 (Control):** Tertiary Gray (#1A1A1A) for interactive inputs and hover states.

Visual separation is achieved using **Low-contrast outlines** (1px borders in #2A2A2A) or **Copper Glows**. A 1px copper top-border can be used on active cards to simulate light catching the edge of a metallic chassis.

## Shapes

The shape language is dominated by **sharp lines** and architectural geometry. We use a "Micro-Radius" approach—a very subtle 4px (Soft) roundedness on buttons and cards to prevent them from feeling "hostile," while maintaining a predominantly rectangular, engineered silhouette.

Circular shapes are reserved exclusively for dial-style controls and speaker driver representations, creating a clear visual distinction between structural containers and functional audio components.

## Components

### Buttons & Controls
Primary buttons are solid Copper (#B87333) with black text. Secondary buttons utilize a ghost style: a 1px copper border with a subtle inner glow on hover. Interactive states should feel "mechanical"—instant transitions with no easing for "clicks," but soft fades for "glows."

### Audio-Visualizer Style
The visualizer component consists of vertical bars of varying widths (2px, 4px, 8px). 
- **Animation:** Use a staggered `scaleY` CSS transform with a `linear` timing function to mimic real-time frequency analysis.
- **Color:** Gradient from Charcoal at the base to Copper at the peak.
- **Effect:** Each bar should have a `box-shadow: 0 0 15px rgba(184, 115, 51, 0.5)` to simulate light emission.

### High-Fidelity Imagery
Photography must be "Low-Key." Focus on macro shots of hardware: the weave of a speaker grille, the brushed texture of a copper knob, or the soft glow of an amp. Backgrounds in photos should always fade into Deep Black to integrate seamlessly with the UI.

### Cards & Inputs
Cards use the Charcoal (#121212) surface with 0px or 4px corner radii. Form inputs are "Underline" style rather than boxed, using a 1px copper bottom border that expands on focus to emphasize the "technical drawing" aesthetic.