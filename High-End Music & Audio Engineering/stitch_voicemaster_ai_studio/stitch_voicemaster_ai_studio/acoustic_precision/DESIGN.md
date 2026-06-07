---
name: Acoustic Precision
colors:
  surface: '#0e0e36'
  surface-dim: '#0e0e36'
  surface-bright: '#35355e'
  surface-container-lowest: '#090831'
  surface-container-low: '#17173e'
  surface-container: '#1b1b43'
  surface-container-high: '#25264e'
  surface-container-highest: '#303059'
  on-surface: '#e2dfff'
  on-surface-variant: '#c8c5ce'
  inverse-surface: '#e2dfff'
  inverse-on-surface: '#2c2c55'
  outline: '#928f98'
  outline-variant: '#47464d'
  surface-tint: '#c4c3ea'
  primary: '#c4c3ea'
  on-primary: '#2d2d4d'
  primary-container: '#0f0f2d'
  on-primary-container: '#7b7a9e'
  inverse-primary: '#5b5b7d'
  secondary: '#ffdf9e'
  on-secondary: '#3f2e00'
  secondary-container: '#fabd00'
  on-secondary-container: '#6a4e00'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#111313'
  on-tertiary-container: '#7c7e7e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c4c3ea'
  on-primary-fixed: '#181836'
  on-primary-fixed-variant: '#444464'
  secondary-fixed: '#ffdf9e'
  secondary-fixed-dim: '#fabd00'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5b4300'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0e0e36'
  on-background: '#e2dfff'
  surface-variant: '#303059'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  code-snippet:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  unit-1: 0.25rem
  unit-2: 0.5rem
  unit-4: 1rem
  unit-8: 2rem
  unit-12: 3rem
  gutter: 24px
  margin-page: 40px
---

## Brand & Style

The design system is built for a "Tech-Professional" environment, targeting developers, audio engineers, and content producers. It evokes a sense of high-fidelity precision, reliability, and premium technological craft. 

The style is **Corporate / Modern** with a heavy influence from **Minimalism**. It utilizes a dark-mode first approach where depth is created through subtle layering rather than aggressive shadows. The interface feels like a high-end recording studio console: dark, focused, and utilitarian, yet polished with high-contrast accents to guide the user's workflow. Visual interest is maintained through crisp 1px borders and purposeful gradients that simulate the movement of sound and light.

## Colors

The palette is anchored by **Deep Indigo**, serving as the foundational canvas for all interfaces. This creates a low-strain environment for long-form editing and coding. 

**Gold** is reserved strictly for primary actions, critical status indicators, and active states in phonetic waveforms. It should be used sparingly to maintain its "premium" impact. **White** and high-transparency whites provide the typographic hierarchy and secondary iconography. 

Subtle secondary colors include a desaturated indigo for container backgrounds to provide separation from the primary canvas.

## Typography

This design system utilizes **Inter** for all UI elements to ensure maximum legibility and a neutral, systematic aesthetic. High contrast is achieved through dramatic weight shifts—using Bold (700) for displays and Regular (400) for body copy. 

For the API portal and technical documentation, **Space Grotesk** is introduced to provide a distinctive, geometric "tech" feel that distinguishes code from natural language. All labels should lean towards a tighter tracking when in uppercase to mimic professional hardware labeling.

## Layout & Spacing

The system follows a **Fixed Grid** model for the main dashboard (1280px max-width) and a **Fluid Grid** for the API documentation to accommodate side-by-side code blocks. 

The spacing rhythm is based on a 4px baseline grid. Components like audio controls and filter chips use tight internal padding (unit-2) to maintain a "dense" professional feel, while page headers and sections utilize generous external margins (unit-12) to prevent visual clutter and maintain the premium tone.

## Elevation & Depth

Elevation is primarily communicated through **Tonal Layers** and **Low-contrast Outlines**. Because the background is a Deep Indigo, elevation is simulated by lightening the fill of the container (e.g., the primary background at #0F0F2D, the card surface at #1E1E46).

Borders are the primary differentiator. Use a 1px solid border with a low-opacity white (12%) for most containers. For active or "focused" cards, the border can transition to a subtle Gold gradient. Shadows are rarely used, but when necessary, they are highly diffused and tinted with the primary Indigo color to maintain a clean, flat appearance.

## Shapes

The design system adopts a **Soft** shape language. This creates a professional balance—sharp enough to feel technical and precise, but rounded enough to feel modern and accessible. 

Standard components (buttons, input fields) use a 0.25rem radius. Larger surfaces like audio waveform containers or code blocks use a 0.5rem radius. Filter chips are the exception, utilizing a fully pill-shaped (rounded-full) geometry to distinguish them as interactive metadata elements.

## Components

### Audio & Voice Elements
- **Phonetic Waveforms:** Visualized as vertical bars. The "played" portion of the waveform uses the Gold primary color; the "unplayed" portion uses a 20% opacity white. On hover, show a vertical 1px gold line (the playhead).
- **Audio Player Controls:** Center-aligned controls. Use high-contrast white for play/pause icons. Volume sliders should be thin 2px tracks with a Gold thumb.

### Navigation & Interaction
- **Primary CTA Buttons:** Solid Gold fill with black (#000000) text for maximum legibility. No box shadow; instead, use a 2px inner-glow on hover.
- **Filter Chips:** Deep Indigo background with a 1px White (20%) border. Active chips switch to a Gold border and Gold text.
- **Input Fields:** Dark background (#0A0A1F) with bottom-only borders for a sleek "terminal" look, or 4-sided borders for high-density forms.

### Technical Elements
- **Code Blocks:** Background color should be slightly darker than the primary background. Use syntax highlighting that favors Gold, Cyan, and White. 
- **API Portal Cards:** Use a 1px border that glows (increased opacity) when the user hovers over a developer endpoint or documentation link.