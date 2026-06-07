---
name: Atmospheric Sound Healing
colors:
  surface: '#0c1320'
  surface-dim: '#0c1320'
  surface-bright: '#323948'
  surface-container-lowest: '#070e1b'
  surface-container-low: '#151c29'
  surface-container: '#19202d'
  surface-container-high: '#232a38'
  surface-container-highest: '#2e3543'
  on-surface: '#dce2f5'
  on-surface-variant: '#c6c6cc'
  inverse-surface: '#dce2f5'
  inverse-on-surface: '#2a303e'
  outline: '#909096'
  outline-variant: '#45474c'
  surface-tint: '#c1c6d6'
  primary: '#c1c6d6'
  on-primary: '#2b303d'
  primary-container: '#060b16'
  on-primary-container: '#757a88'
  inverse-primary: '#595e6c'
  secondary: '#ffb958'
  on-secondary: '#462b00'
  secondary-container: '#c78202'
  on-secondary-container: '#3d2500'
  tertiary: '#bac7dd'
  on-tertiary: '#253142'
  tertiary-container: '#010c1b'
  on-tertiary-container: '#6e7b8e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dee2f3'
  primary-fixed-dim: '#c1c6d6'
  on-primary-fixed: '#161c27'
  on-primary-fixed-variant: '#414754'
  secondary-fixed: '#ffddb5'
  secondary-fixed-dim: '#ffb958'
  on-secondary-fixed: '#2a1800'
  on-secondary-fixed-variant: '#643f00'
  tertiary-fixed: '#d6e3f9'
  tertiary-fixed-dim: '#bac7dd'
  on-tertiary-fixed: '#0f1c2c'
  on-tertiary-fixed-variant: '#3b4859'
  background: '#0c1320'
  on-background: '#dce2f5'
  surface-variant: '#2e3543'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
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
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
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
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

This design system is built to evoke the sensation of a quiet, moonlit sanctuary. The brand personality is ethereal, tranquil, and premium, targeting individuals seeking a high-end auditory escape from digital noise. The emotional response is one of immediate decompression—shifting the user from a state of "doing" to "being."

The visual style merges **Minimalism** with elements of **Glassmorphism**. By prioritizing expansive negative space and utilizing translucent layers, the interface feels weightless and expansive, much like the night sky. High-contrast accents are used sparingly to guide the eye without breaking the meditative immersion, ensuring the UI remains "soft" even while being functionally distinct.

## Colors

The palette is centered on a **Midnight Blue** base, providing a deep, non-distracting canvas that mimics the infinite depth of space. **Amber** serves as the primary action color, chosen for its warmth and its symbolic connection to candlelight or distant stars; it provides high-contrast visibility against the dark background. 

**Smoke** is utilized for secondary information and structural borders, ensuring that the hierarchy is maintained without the harshness of pure white. Gradients should transition from Midnight Blue to slightly lighter navies to create a sense of atmospheric volume rather than flat surfaces.

## Typography

This design system utilizes a sophisticated typographic pairing to balance heritage and modernity. **Noto Serif** is used for all headlines, providing an editorial, luxurious feel that slows the reader down and encourages a sense of calm. 

**Manrope** is used for all functional and body text. Its geometric yet approachable structure ensures high legibility on dark backgrounds. For interactive labels, Manrope is used in uppercase with slight tracking (letter-spacing) to create a distinct, modern contrast against the fluid serif headlines.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Tonal Layers** rather than traditional drop shadows. Surfaces closer to the user are rendered with a lighter Midnight Blue tint and a subtle backdrop blur (12px to 20px). 

Depth is enhanced by "Auditory Glows"—soft, radial Amber gradients behind key elements that mimic the diffusion of sound waves. Borders should be used sparingly, primarily as 1px "Smoke" outlines at 20% opacity to define the edges of glass containers without creating hard visual breaks.

## Shapes

The shape language is **Rounded**, favoring organic, soft edges that feel comfortable and safe. Sharp corners are avoided to maintain the "soft on the eyes" requirement. 

Standard components use a 0.5rem radius, while larger cards and modal containers use 1.5rem to emphasize their "contained" nature. Interactive elements like play buttons or active chips may use pill-shaped (fully rounded) geometry to signify their role as tactile touchpoints in the ethereal space.

## Components

**Buttons:** Primary buttons are solid Amber with Noto Serif text for a premium feel. They should feature a soft outer glow in the same hue. Secondary buttons are "ghosted" with a Smoke border.

**Cards:** Containers for soundscapes or meditation sessions use a backdrop blur effect. They should have no solid background, only a subtle Midnight Blue tint (50-70% opacity) to ensure the background "night sky" remains visible.

**Waveform Visualizers:** Unique to this design system, sound waveforms should be rendered as soft, blurred Amber lines rather than jagged peaks, reinforcing the "ethereal" atmosphere.

**Input Fields:** Minimalist design with only a bottom border in Smoke. When focused, the border transitions to Amber with a subtle upward glow.

**Progress Bars:** Seek bars and volume sliders use a thin Smoke track with a glowing Amber thumb, mimicking a star moving across a horizon.