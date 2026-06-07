---
name: Serene Biological System
colors:
  surface: '#fcf8ff'
  surface-dim: '#dcd8e1'
  surface-bright: '#fcf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f2fb'
  surface-container: '#f0ecf5'
  surface-container-high: '#ebe6ef'
  surface-container-highest: '#e5e1ea'
  on-surface: '#1c1b21'
  on-surface-variant: '#474552'
  inverse-surface: '#313036'
  inverse-on-surface: '#f3eff8'
  outline: '#787583'
  outline-variant: '#c8c4d3'
  surface-tint: '#5952af'
  primary: '#5952af'
  on-primary: '#ffffff'
  primary-container: '#a29bfe'
  on-primary-container: '#362d8a'
  inverse-primary: '#c5c0ff'
  secondary: '#5a5f62'
  on-secondary: '#ffffff'
  secondary-container: '#dce0e4'
  on-secondary-container: '#5e6367'
  tertiary: '#586062'
  on-tertiary: '#ffffff'
  tertiary-container: '#a1a8aa'
  on-tertiary-container: '#363d3f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c5c0ff'
  on-primary-fixed: '#140067'
  on-primary-fixed-variant: '#413996'
  secondary-fixed: '#dfe3e7'
  secondary-fixed-dim: '#c3c7cb'
  on-secondary-fixed: '#171c1f'
  on-secondary-fixed-variant: '#43474b'
  tertiary-fixed: '#dde4e6'
  tertiary-fixed-dim: '#c1c8ca'
  on-tertiary-fixed: '#161d1f'
  on-tertiary-fixed-variant: '#41484a'
  background: '#fcf8ff'
  on-background: '#1c1b21'
  surface-variant: '#e5e1ea'
typography:
  display-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.0'
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
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built at the intersection of medical science and empathetic wellness. The brand personality is deeply compassionate, positioning the product not just as a wearable, but as a calming extension of the user’s own nervous system. The UI must evoke a sense of immediate relief—a digital deep breath.

The visual style blends **Minimalism** with **Glassmorphism**. By using translucent layers and soft, diffused light, the interface feels weightless and "breathable," mimicking the physical properties of light-weight textiles. The aesthetic is "Serene & Biological," utilizing organic curves and motion that follows a rhythmic, pulmonary tempo to reassure the user during moments of high stress.

## Colors

The color palette is designed to lower cortisol levels through low-vibration hues. 

- **Lavender** serves as the primary focal point, symbolizing tranquility and neurological care. 
- **Frost White** provides the "air" within the design, used for expansive backgrounds and breathable negative space.
- **Charcoal** is reserved for high-contrast typography and grounding structural elements, providing a sense of stability and scientific authority. 

Gradients should be used sparingly but effectively, transitioning softly between Lavender and Frost White to simulate the shifting textures of biological membranes.

## Typography

**Manrope** is the chosen typeface for its modern, balanced, and highly legible characteristics. It bridges the gap between a clinical/scientific sans-serif and a soft, approachable lifestyle font. 

To enhance the feeling of "breathability," this design system employs generous letter spacing (tracking) in body copy and labels. Headlines should remain slightly more compact but never crowded. Line heights are intentionally tall to ensure the content never feels dense or overwhelming to a user in a stressed state.

## Layout & Spacing

The design system utilizes a **Fluid Grid** with significantly wider margins and gutters than standard applications. This "wide-set" layout prevents information density, which is critical for stress-responsive design.

Spacing follows an 8px rhythmic scale, but the implementation favors "macro-spacing"—using the `lg` and `xl` units to separate distinct functional areas. This creates a gallery-like experience where every piece of data has room to exist without competing for the user’s limited cognitive load.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces do not "hover" over a background; they "float" within it.

- **Surface Layers:** Use a backdrop-filter (blur: 12px to 20px) with a semi-transparent Frost White fill (opacity: 60-80%).
- **Boundaries:** Instead of hard shadows, use "Inner Glows" or ultra-fine 1px borders in a lighter shade of the primary lavender to define edges.
- **Z-Axis:** Higher elevation is communicated through increased blur intensity and higher transparency, making the element appear closer and lighter.

## Shapes

The shape language is "Biological." Avoid sharp 90-degree angles entirely. The standard radius is set to **Rounded (0.5rem)** for basic components, but containers and larger cards should utilize the `rounded-xl` (1.5rem) setting to mimic the soft contours of pebbles or organic cells.

Interactive elements like buttons can occasionally use pill-shaped (fully rounded) geometry to emphasize their tactile, "squishy" nature, making the interface feel friendly and safe to touch.

## Components

### Buttons & Interaction
Buttons feature a "breathing" state: a very subtle, infinite scale animation (1% growth) that mimics a slow respiratory rate. Primary buttons use a solid Lavender fill, while secondary buttons utilize a glassmorphic Ghost style.

### Glassmorphic Cards
All content containers must use the frost-white translucent background with a subtle backdrop blur. This ensures that even when the background features organic biological textures, the text remains perfectly legible without feeling disconnected from the environment.

### Progress & Bio-Feedback
Indicators for stress levels should avoid "harsh" meters. Instead, use soft, pulsing organic blobs that change color and opacity based on the intensity of the reading—shifting from a clear Mint to a soft Lavender.

### Input Fields
Inputs are minimalist, defined only by a bottom border and a soft Lavender focus state. Labels should use the `label-sm` style, floating above the input to maintain a sense of lightness.

### Tactical Breathing Guide
A specialized component featuring a large, expanding and contracting circular shape that guides the user through calming breath cycles, synchronized with the system's global motion tokens.