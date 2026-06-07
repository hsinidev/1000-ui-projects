---
name: Celestial-Luxe System
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#313031'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c4c4e2'
  on-tertiary: '#2d2f46'
  tertiary-container: '#0a0c22'
  on-tertiary-container: '#787994'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e0e0ff'
  tertiary-fixed-dim: '#c4c4e2'
  on-tertiary-fixed: '#181a30'
  on-tertiary-fixed-variant: '#43455e'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  headline-xl:
    fontFamily: Sora
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Sora
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  telemetry-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  telemetry-label:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  container-max: 1440px
---

## Brand & Style

This design system targets an ultra-high-net-worth audience seeking the ultimate frontier of luxury: orbital and lunar travel. The brand personality is "Transcendent Engineering"—blending the cold, precise reality of aerospace technology with the ethereal, awe-inspiring beauty of the cosmos. 

The UI style is a sophisticated evolution of **Glassmorphism**. It utilizes multi-layered translucent surfaces to mimic spacecraft viewing ports and advanced HUDs (Heads-Up Displays). Depth is achieved through background blurs and glowing, sharp-edged borders rather than traditional shadows. The emotional goal is to make the user feel secure yet exhilarated, as if they are already seated within a premium observation deck overlooking the Earth’s curve.

## Colors

The palette is anchored in **Midnight Blue (#0A0E1A)**, representing the infinite void. This serves as the primary canvas for all layouts. **Silver (#C0C0C0)** is used for structural iconography and secondary text, providing a metallic, machined feel.

Iridescent accents are applied through gradients and light-leaks rather than flat fills. Use the **Cyan** and **Purple** accents specifically for interactive states and data visualizations to simulate glowing gas nebulae or plasma thrusters. **Pearl** is reserved for high-contrast highlights and primary calls to action, mimicking the glint of sunlight on titanium.

## Typography

The typographic hierarchy distinguishes between "The Experience" and "The Data." 

- **Headlines:** Use **Sora** for its futuristic, wide geometric stance. It should feel architectural and commanding.
- **Body:** **Inter** provides maximum legibility against complex cosmic backgrounds, maintaining a clean, neutral tone.
- **Telemetry:** All technical specs, coordinates, and pricing should use **JetBrains Mono**. This font family conveys precision and evokes high-end aerospace instrumentation. Ensure all telemetry labels are set in uppercase with increased letter spacing for a "read-out" aesthetic.

## Layout & Spacing

This design system employs a **12-column fixed grid** for desktop, centered on the viewport to maintain a cinematic focus. Content should be treated as "modules" floating in space. 

Generous margins (**80px**) on desktop are essential to allow the cosmic background textures to breathe, creating a sense of vastness. On mobile, the grid collapses to 4 columns with tighter margins. Use an 8px base unit for all internal component spacing to maintain a mathematical, engineered rhythm.

## Elevation & Depth

Depth is not communicated through shadows, but through **optical density and luminosity**.

1.  **Level 0 (Deep Space):** Full-screen cinematic backgrounds (starfields, nebulae).
2.  **Level 1 (The Hull):** Large, semi-transparent glass containers with a `backdrop-filter: blur(20px)` and a subtle `1px` inner border of Silver at 20% opacity.
3.  **Level 2 (Flight Deck):** Active panels and modal overlays with higher opacity and a "glowing" border (0.5px solid Cyan or Pearl with a 4px outer bloom).
4.  **Level 3 (Controls):** Fully opaque or high-luminosity interactive elements that appear to sit "on top" of the glass.

## Shapes

The shape language is "Soft-Industrial." Components use a **Soft (0.25rem)** base radius to feel like machined parts. 

Avoid perfectly round circles for buttons; instead, use slightly chamfered corners or very subtle rounding to maintain the technical, aerospace feel. Larger containers should use `rounded-lg` (0.5rem) to suggest the structural integrity of a pressurized cabin.

## Components

### Buttons
Primary buttons should be "Luminous Ghost" style: a transparent center with a 1px Silver border that glows Cyan on hover. Text must be Telemetry-style (JetBrains Mono, Uppercase).

### Cards / Modules
Use the "Glassmorphism" elevation rules. Every card must have a subtle top-left light highlight to simulate a cockpit light source. Title sections should be separated by a 1px line with 10% opacity.

### Telemetry Readouts
Small groupings of data (e.g., "Velocity," "Apogee") should be enclosed in a thin, 4-corner bracket system rather than a full box. This reinforces the HUD/Instrumentation aesthetic.

### Inputs
Input fields are "Underlined" style rather than boxes, using a Silver base line that illuminates to Cyan when focused. The cursor should be a solid block rather than a line, leaning into the technical mono-spaced theme.

### Additional Components
- **Progress Gauges:** Circular or arc-based SVG strokes to represent flight readiness or oxygen levels.
- **Star-Map Navigation:** A custom interactive element for selecting destinations, utilizing iridescent glow-points.