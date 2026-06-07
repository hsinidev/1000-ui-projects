---
name: Scientific Longevity
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#47464e'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#77767f'
  outline-variant: '#c8c5cf'
  surface-tint: '#5a5b84'
  primary: '#020229'
  on-primary: '#ffffff'
  primary-container: '#1a1b41'
  on-primary-container: '#8283af'
  inverse-primary: '#c2c2f2'
  secondary: '#006b58'
  on-secondary: '#ffffff'
  secondary-container: '#63fbd7'
  on-secondary-container: '#00725e'
  tertiary: '#050809'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c2022'
  on-tertiary-container: '#848889'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c2c2f2'
  on-primary-fixed: '#16173d'
  on-primary-fixed-variant: '#42436b'
  secondary-fixed: '#63fbd7'
  secondary-fixed-dim: '#3edebb'
  on-secondary-fixed: '#002019'
  on-secondary-fixed-variant: '#005142'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#181c1e'
  on-tertiary-fixed-variant: '#434749'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-display:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.03em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The design system is engineered to bridge the gap between rigorous genomic science and the emotional bond of pet ownership. The brand personality is authoritative, precise, and forward-thinking, yet remains accessible to non-scientists. It evokes a sense of "clinical optimism"—the feeling that advanced data can lead to a longer, healthier life for a pet.

The visual style follows a **Modern Corporate** aesthetic with **Glassmorphism** influences. It utilizes a high-density information architecture to convey scientific depth, balanced by generous white space to maintain clarity. Decorative "Double-Helix" patterns are used as subtle background textures or masking paths for imagery, reinforcing the DNA focus without cluttering the interface.

## Colors

The palette is rooted in **Deep Indigo**, used for primary navigation, headings, and heavy structural elements to establish trust and authority. **Mint** serves as the primary action color, symbolizing health, vitality, and biological growth; it is used exclusively for interactive elements, success states, and key health metrics.

Backgrounds primarily utilize **White** and very light cool grays to maintain a clinical, clean environment. Data visualizations should leverage high-contrast pairings: Deep Indigo for baselines and Mint for positive growth or "bio-hacked" optimizations. Subtle gradients are applied to cards and progress rings to add depth and a sense of premium technology.

## Typography

This design system utilizes a dual-type approach to balance modern geometry with technical precision. **Space Grotesk** is the primary heading face, chosen for its "tech-forward" geometric apertures that suggest innovation.

**Inter** is utilized for all body copy and data representation. For health metrics and DNA sequences, Inter is used with tighter letter-spacing and heavier weights to mimic the look of laboratory reports. Labels and secondary data points should use the uppercase style to differentiate categorical information from narrative content.

## Layout & Spacing

The layout philosophy is based on a **12-column fluid grid** for web and a single-column stack for mobile. Spacing follows a 4px baseline shift to ensure mathematical precision in high-density data views. 

Data-rich environments, such as genetic markers or longevity timelines, should use "Compact" spacing (8px-12px) to allow for side-by-side comparisons. Marketing and landing pages should utilize "Expansive" spacing (40px+) to allow the minimal, clean aesthetic to breathe.

## Elevation & Depth

This design system uses **Tonal Layers** and **Glassmorphism** to define hierarchy. Backgrounds are strictly flat, while interactive cards and data modules use a subtle white-transparency fill with a `backdrop-filter: blur(12px)`.

Shadows are avoided in favor of **Low-contrast outlines**. Elements are separated by 1px borders in a semi-transparent version of the primary Indigo (e.g., Indigo at 10% opacity). For active or "elevated" states, a soft ambient glow using the Mint color is used to indicate health or focus, rather than traditional drop shadows.

## Shapes

The shape language is **Soft** and controlled. A standard corner radius of 4px (`0.25rem`) is applied to buttons and inputs to maintain a scientific, precise feel. Larger containers and cards use an 8px radius. 

The only exception to this rule is the "Bio-Hacking" toggle and progress rings, which use full saturation (pill-shapes/circles) to represent the organic nature of biological data.

## Components

### Buttons & Toggles
- **Primary Action:** Solid Mint background with Deep Indigo text for maximum legibility. 
- **Secondary Action:** Ghost style with 1px Deep Indigo border.
- **Bio-Hacking Toggles:** Large, tactile switches that use a Mint glow when active, signifying a health optimization is "on."

### High-Density Data Cards
Cards feature a 1px internal divider. The top section contains the metric name in `label-caps`, and the main body features the metric value in `data-display`. Backgrounds use the Glassmorphism blur to allow decorative helix patterns to peek through from the layer below.

### Progress Rings
Circular health metrics use a 10% Indigo track with a Mint "Health" fill. Use a stroke-cap of "round" to add a slight organic touch to the technical data.

### Double-Helix Elements
Used as a non-interactive decorative motif. These should be rendered as vector paths with a 0.5px stroke in Deep Indigo at 15% opacity, appearing to float behind data cards.

### Input Fields
Strictly rectangular with a 4px radius. Labels are always persistent and positioned above the field in `label-caps` to ensure users never lose context in complex DNA data entry forms.