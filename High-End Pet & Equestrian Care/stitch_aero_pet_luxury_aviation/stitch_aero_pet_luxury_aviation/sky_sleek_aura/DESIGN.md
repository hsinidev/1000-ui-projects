---
name: Sky-Sleek Aura
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#43474e'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#476083'
  primary: '#000613'
  on-primary: '#ffffff'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#afc8f0'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#040607'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1f21'
  on-tertiary-container: '#848789'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  headline-display:
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
    fontWeight: '500'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
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
  container-max: 1280px
  gutter: 32px
  margin-page: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style

The design system is engineered for the ultra-high-net-worth segment, specifically focusing on the intersection of luxury aviation and high-value animal care. The brand personality is poised, serene, and uncompromisingly premium. It evokes the quiet confidence of a private terminal lounge.

The visual style follows a **Modern Minimalist** movement with **Glassmorphism** accents. It prioritizes vast negative space to communicate exclusivity and breathing room. By utilizing a "Sky-Sleek" aesthetic, the interface avoids clutter, instead relying on precision-aligned elements, thin gold strokes, and ethereal gradients that mimic the atmosphere at high altitudes. The emotional goal is to provide peace of mind to owners, ensuring their companions are traveling in a "sanctuary in the sky."

## Colors

The palette is anchored by **Deep Navy Blue**, representing the depth of the sky and institutional trust. **Champagne Gold** serves as the primary accent, used sparingly to denote luxury, interactive states, and premium features. **Cloud White** provides a crisp, airy base for the interface.

- **Primary:** Deep Navy Blue is used for primary backgrounds, heavy typography, and foundational navigation elements.
- **Secondary:** Champagne Gold is reserved for "hero" actions, thin-line iconography, and decorative borders.
- **Backgrounds:** Use a soft gradient transition from Cloud White to a very pale blue-grey to create depth.
- **Functional Colors:** Success, warning, and error states should be muted and desaturated to maintain the "Sky-Sleek" composure.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage with modern utility. **Noto Serif** (as a high-quality alternative to Playfair Display) is the voice of the brand, used for large-scale editorial moments and section headers. Its elegant serifs suggest a history of excellence.

**Inter** provides the functional backbone of the system. It is used for all transactional data, body copy, and UI controls. The combination ensures that while the brand feels aspirational, the booking experience remains precise and highly readable. Use generous line heights (1.5+) to maintain the airy, spacious aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with significantly wider-than-standard margins. This "letterboxed" feel creates a sense of luxury and focus. 

- **Grid:** A 12-column grid with a wide 32px gutter.
- **Rhythm:** An 8px linear scale governs all padding and margin decisions.
- **Whitespace:** Emphasize vertical rhythm with large "stack-lg" gaps between major content blocks to prevent visual crowding.
- **Alignment:** Content should predominantly be center-aligned or staggered to mimic a premium brochure layout.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Glassmorphism** rather than heavy shadows. 

- **Surface Levels:** The base is Cloud White. Floating cards use a semi-transparent "Frosted Glass" effect (background blur: 20px) with a subtle 1px white inner stroke.
- **Shadows:** When shadows are necessary, use "Atmospheric Shadows"—extremely diffused, low-opacity (5-8%), and tinted with Deep Navy Blue rather than pure black.
- **Depth:** Elements should appear to float on different atmospheric planes. Use thin Gold-line dividers (0.5px) to separate sections without adding visual weight.

## Shapes

The shape language is restrained and architectural. This design system uses **Soft (0.25rem)** corners for standard UI components like inputs and buttons to maintain a professional, sharp-edged sophistication. 

Larger containers or hero images may use **rounded-lg (0.5rem)** to slightly soften the composition. Avoid pill-shapes or high-radius curves, as they feel too "consumer-tech" and lack the elite, established feel required for private aviation.

## Components

- **Buttons:** Primary buttons are Deep Navy with white text. Secondary buttons use a transparent background with a thin (1px) Champagne Gold border. Hover states should include a subtle gold glow or a shift in background opacity.
- **Inputs:** Clean, bottom-border-only or very subtle outlined fields with high-contrast labels in `label-caps`. 
- **Icons:** Custom 1px weight Champagne Gold vector icons. Icons should be encased in a subtle circular "halo" when used as primary navigational triggers.
- **Cards:** Use "The Lounge Card"—a white surface with a very subtle gold top-border and an atmospheric shadow. 
- **Progress Indicators:** Use thin, horizontal gold lines to indicate booking steps, avoiding bulky "stepper" components.
- **Pet Profiles:** High-fidelity circular avatars with a gold-leaf border treatment.