---
name: Luminous Velocity
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#3e484e'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#6f787f'
  outline-variant: '#bec8cf'
  surface-tint: '#006687'
  primary: '#006687'
  on-primary: '#ffffff'
  primary-container: '#70d1ff'
  on-primary-container: '#005976'
  inverse-primary: '#72d2ff'
  secondary: '#516072'
  on-secondary: '#ffffff'
  secondary-container: '#d2e1f7'
  on-secondary-container: '#556477'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#c4c6c8'
  on-tertiary-container: '#4f5254'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1e8ff'
  primary-fixed-dim: '#72d2ff'
  on-primary-fixed: '#001e2b'
  on-primary-fixed-variant: '#004d66'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

This design system is anchored in the concept of "Sustainable Futurism." It targets an audience that values environmental consciousness without sacrificing high-performance engineering or luxury. The UI must evoke a sense of weightless speed and pristine technological precision.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. By utilizing generous whitespace and translucent layers, the interface feels like a projection onto a high-end heads-up display (HUD). Every element should feel airy and illuminated, avoiding heavy shadows in favor of light-refractive properties and soft glows.

## Colors

The palette is derived from the aesthetics of cold energy and high-grade alloys. 

- **Ice Blue:** Used as the primary action color and for "energy" states. It should feel bioluminescent against white backgrounds.
- **Silver:** Serves as the structural color for borders, iconography, and subtle gradients, mimicking brushed aluminum.
- **Clean White:** The primary canvas color, providing a sterile, laboratory-grade foundation.
- **Deep Slate:** Used sparingly for high-contrast typography to ensure legibility while maintaining the "tech-forward" cool tone.

Gradients should be used to simulate light hitting metallic surfaces, moving from Ice Blue to a transparent Silver.

## Typography

This design system utilizes a dual-font strategy to balance technical precision with premium readability. 

**Space Grotesk** is the primary typeface for headlines and data points. Its geometric nature evokes a sense of engineering and innovation. Use it for speeds, battery percentages, and section headers.

**Manrope** is used for body copy and long-form information. Its balanced, modern proportions ensure that technical specifications are easy to digest. 

Maintain wide tracking on uppercase labels to reinforce the luxury aesthetic.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to ensure a curated, editorial feel. A 12-column grid is used with exceptionally wide margins (64px+) to prevent the interface from feeling cluttered.

Spacing rhythm is generous. Luxury is defined by the space *between* elements. Components should never feel cramped; use the "section-gap" (128px) to separate distinct functional areas of the ecosystem. Vertical rhythm should favor breathing room over information density.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and tonal layering rather than traditional drop shadows. 

1.  **Base Layer:** Clean White or ultra-light Silver (#F1F5F9).
2.  **Surface Layer:** Translucent white (Opacity: 40-70%) with a background blur (Backdrop-filter: blur(20px)).
3.  **Edge Definition:** Instead of shadows, use 1px solid strokes in a lighter Silver or semi-transparent Ice Blue to define the edges of floating cards.
4.  **Accent Glows:** Use soft, diffused "Atmospheric Glows" (Ice Blue at 10% opacity) behind primary components to simulate light emission.

## Shapes

The shape language is "Soft-Tech." While the brand is futuristic, it avoids sharp, aggressive corners in favor of approachable, ergonomic curves. 

Standard components use a **0.5rem (8px)** radius. Large layout cards and glass containers use a **1.5rem (24px)** radius to create a distinct visual container that feels safe and modern. Interactive elements like buttons should never be fully sharp or fully circular (pill-shaped) unless they are secondary chips.

## Components

### Glass Cards
The signature container. Apply a `backdrop-filter: blur(24px)` and a `border: 1px solid rgba(255, 255, 255, 0.5)`. The background color should be a semi-transparent White.

### Liquid Progress Bars
Used for battery and energy metrics. The progress fill should use a linear gradient from Ice Blue to a lighter cyan. The "liquid" effect is achieved through a subtle, animated wave mask at the leading edge of the progress fill, creating a sense of fluid movement within the vessel.

### High-End Buttons
Primary buttons use a solid Ice Blue fill with white text. Secondary buttons should be "Ghost" style with a Silver border and a subtle glass hover effect.

### Input Fields
Minimalist underlines or very soft-tinted containers. Focus states should be indicated by a glow effect on the border rather than a change in fill color.

### Interactive Data Chips
Small, semi-translucent capsules used for vehicle status (e.g., "Ready," "Charging"). Use Space Grotesk in all-caps for the labels within these chips.