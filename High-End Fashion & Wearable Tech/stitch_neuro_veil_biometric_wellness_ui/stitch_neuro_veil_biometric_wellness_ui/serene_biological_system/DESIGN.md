---
name: Serene Biological System
colors:
  surface: '#f4fafd'
  surface-dim: '#d4dbdd'
  surface-bright: '#f4fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef5f7'
  surface-container: '#e8eff1'
  surface-container-high: '#e2e9ec'
  surface-container-highest: '#dde4e6'
  on-surface: '#161d1f'
  on-surface-variant: '#474552'
  inverse-surface: '#2b3234'
  inverse-on-surface: '#ebf2f4'
  outline: '#787583'
  outline-variant: '#c8c4d3'
  surface-tint: '#5952af'
  primary: '#5952af'
  on-primary: '#ffffff'
  primary-container: '#a29bfe'
  on-primary-container: '#362d8a'
  inverse-primary: '#c5c0ff'
  secondary: '#575e72'
  on-secondary: '#ffffff'
  secondary-container: '#dbe2fa'
  on-secondary-container: '#5d6478'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#a4a7a9'
  on-tertiary-container: '#393d3e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c5c0ff'
  on-primary-fixed: '#140067'
  on-primary-fixed-variant: '#413996'
  secondary-fixed: '#dbe2fa'
  secondary-fixed-dim: '#bfc6dd'
  on-secondary-fixed: '#141b2c'
  on-secondary-fixed-variant: '#3f4759'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f4fafd'
  on-background: '#161d1f'
  surface-variant: '#dde4e6'
typography:
  display-lg:
    fontFamily: Questrial
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  headline-md:
    fontFamily: Questrial
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.03em
  body-base:
    fontFamily: Questrial
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Questrial
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 0.5rem
  sm: 1rem
  md: 2rem
  lg: 4rem
  xl: 8rem
  gutter: 24px
  margin: max(5vw, 24px)
---

## Brand & Style

The design system is rooted in the concept of "biological resonance." It aims to bridge the gap between clinical precision and human empathy, creating a digital environment that actively lowers the user's cognitive load. The aesthetic is ethereal yet grounded, mimicking the soft translucency of organic membranes and the rhythmic pacing of natural breath.

This design system utilizes **Glassmorphism** as its core structural metaphor. Surfaces are treated as semi-permeable veils that allow light and color to filter through, suggesting depth without creating hard barriers. The emotional response should be one of immediate tranquility—a digital sanctuary for users managing stress. 

Key visual principles include:
- **Atmospheric Depth:** Using layered transparency to create a sense of three-dimensional space.
- **Biomorphic Motion:** Transitions should follow "slow-in, slow-out" curves that mimic natural movement.
- **Compassionate Precision:** A balance of clean, functional layouts with soft, approachable visual treatments.

## Colors

The color strategy for the design system is centered on a calming, low-vibration palette that avoids high-frequency visual noise.

- **Lavender (Primary):** Used for interactive elements, status indicators, and key focus areas. It represents serenity and cognitive balance.
- **Frost White (Backgrounds):** A high-brightness, cool-toned white used to provide a sense of expansive space and cleanliness.
- **Charcoal (Text/Depth):** A soft, desaturated dark grey used for legibility. Avoid pure black (#000) to maintain the "soft-focus" aesthetic.
- **Translucency:** Much of the palette is expressed through alpha-channels (opacity), allowing colors to blend and shift as the user scrolls, simulating a "breathing" interface.

## Typography

This design system utilizes **Questrial** for its balanced, circular geometry and open apertures, which contribute to a modern and approachable clinical feel. 

To achieve the "elegant sans-serif" look requested, typography must be given ample room to breathe. **Generous letter spacing (tracking)** is applied to all display and label styles to improve scanability and evoke a premium, editorial quality. Paragraph text should maintain a high line-height (1.6) to prevent visual density, ensuring that information feels light and manageable.

## Layout & Spacing

The layout philosophy is defined by **expansive negative space**. Elements are not crowded; they are allowed to float within the viewport, anchored by a fluid grid system.

- **Fluid Centering:** Content should primarily reside in a centralized container to focus the user's attention.
- **Asymmetric Balance:** Use organic, slightly off-center placements for decorative biological shapes to avoid a rigid, robotic feel.
- **Breathing Room:** Margins are intentionally wide. No element should sit close to the edge of the screen, reinforcing the "veil" concept where the UI is a floating layer over a peaceful background.

## Elevation & Depth

Depth in this design system is achieved through **optical physics** rather than traditional dropshadows.

1.  **Backdrop Blurs:** Use a `blur(20px)` on all glass surfaces. This creates a sense of the background "melting" into the foreground.
2.  **Soft-Shadow Diffusion:** Shadows should be extremely large, very low opacity (3-5%), and tinted with the primary Lavender color to avoid "dirty" grey shadows.
3.  **Tonal Stacking:** Higher elevation is communicated by increasing the opacity of the glass surface and the intensity of the blur, rather than adding darker borders.
4.  **Inner Glows:** A subtle 1px white inner border (semi-transparent) should be applied to the top and left edges of cards to simulate a soft light source hitting the "edge" of the glass.

## Shapes

The shape language is **organic and soft**. There are no sharp corners within the design system, as sharp angles trigger a "threat" response in the subconscious.

- **Primary Radius:** A consistent 0.5rem (8px) is used for small elements like inputs.
- **Large Radius:** Cards and containers use 1.5rem (24px) or larger to feel pill-like and soft.
- **Blob Geometry:** Background accents and decorative elements should use CSS `border-radius` with varying percentages (e.g., `60% 40% 30% 70% / 60% 30% 70% 40%`) to create shifting, biological "blobs" that can be animated to pulse slowly.

## Components

### Buttons
Buttons should be rendered as soft, pill-shaped elements. The primary button uses a subtle Lavender-to-Frost gradient. On hover, the button should "glow" slightly via an increased outer shadow diffusion rather than a color change.

### Glass Cards
The core container. Every card must have `backdrop-filter: blur()`, a semi-transparent white background, and a soft primary-tinted shadow. Cards should appear to float effortlessly.

### Breathing Indicators
A unique component for this system: a circular or organic shape that expands and contracts in size (scale 1.0 to 1.05) every 4 seconds. This acts as a passive visual pacer for the user's own breathing.

### Input Fields
Inputs are "ghost" style—highly transparent with a soft Lavender bottom border that expands into a full glow when focused. Labels float above the field with generous letter spacing.

### Fluid Sliders
Sliders for bio-feedback data should use thick, rounded tracks and a large, frosted-glass thumb. The track behind the thumb should fill with a soft gradient as it is pulled.

### Transitions
All page transitions must use a "fade and scale" motion. As a new view appears, it should softly scale up from 98% to 100% while fading in, mimicking the expansion of a lung.