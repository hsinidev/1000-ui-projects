---
name: Star-Gaze
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d4c5ab'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9c8f78'
  outline-variant: '#504532'
  surface-tint: '#fbbc00'
  primary: '#ffe2ab'
  on-primary: '#402d00'
  primary-container: '#ffbf00'
  on-primary-container: '#6d5000'
  inverse-primary: '#795900'
  secondary: '#c3c6d7'
  on-secondary: '#2c303d'
  secondary-container: '#454957'
  on-secondary-container: '#b5b8c9'
  tertiary: '#ffded9'
  on-tertiary: '#690100'
  tertiary-container: '#ffb8ad'
  on-tertiary-container: '#ad0100'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdfa0'
  primary-fixed-dim: '#fbbc00'
  on-primary-fixed: '#261a00'
  on-primary-fixed-variant: '#5c4300'
  secondary-fixed: '#dfe2f3'
  secondary-fixed-dim: '#c3c6d7'
  on-secondary-fixed: '#171b28'
  on-secondary-fixed-variant: '#434654'
  tertiary-fixed: '#ffdad4'
  tertiary-fixed-dim: '#ffb4a8'
  on-tertiary-fixed: '#410000'
  on-tertiary-fixed-variant: '#930100'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Hanken Grotesk
    fontSize: 64px
    fontWeight: '300'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
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
  gutter: 24px
  margin: 48px
  container-max: 1280px
---

## Brand & Style
This design system establishes a visual language centered on the intersection of elite luxury and astronomical precision. The brand personality is quiet, intellectual, and exclusive, evoking the profound stillness of a remote observatory. 

The aesthetic leverages **Technical Minimalism** combined with **Glassmorphism**. It creates a sense of looking through high-end optics—telescope lenses, cockpit HUDs, and observatory viewports. The UI must feel like a precision instrument: expensive, highly capable, and meticulously calibrated. A primary functional requirement of this design system is "Night Vision Preservation," ensuring that the interface remains a tool for discovery rather than a source of light pollution.

## Colors
The palette is rooted in the deep spectrum of the night sky. **Midnight Blue (#0A0E1A)** serves as the primary structural color, providing more depth than a standard neutral. **Matte Black (#121212)** is reserved for the deepest background layers to ensure OLED true-blacks and minimize screen glow.

**Amber (#FFBF00)** is the sole interactive color, chosen for its historical association with vintage technical gauges and its high legibility against dark backgrounds. This design system also includes a **Red-Light Mode (#FF0000)**; when toggled, all Amber and Blue values are remapped to pure red hues to maintain the user's scotopic vision during stargazing sessions.

## Typography
The typographic hierarchy relies on **Hanken Grotesk** for its clean, contemporary sans-serif profile. Headlines should use lighter weights and tighter tracking to convey sophistication. 

**Space Mono** is utilized strictly for technical data, coordinates, timestamps, and metadata. This distinction reinforces the "technical luxury" narrative, separating editorial content from scientific instrumentation. All labels should be set in uppercase with increased letter spacing to emulate etched navigational equipment.

## Layout & Spacing
This design system utilizes a **12-column fixed grid** centered within the viewport to maintain an organized, modular appearance reminiscent of star charts. The spacing rhythm is based on an **8px linear scale**, ensuring mathematical consistency across all components.

Large margins are encouraged to provide "visual silence," reflecting the vastness of space. Content modules should be grouped into logical clusters separated by generous whitespace, preventing the UI from feeling cluttered or overwhelming during low-light usage.

## Elevation & Depth
Depth is communicated through **Glassmorphism and Tonal Layers** rather than traditional drop shadows. Surfaces appear as translucent panes of dark glass with a `20px` backdrop blur.

Each elevated element features a **1px technical border** (Hex: #FFFFFF at 10% opacity) to define its edges against the void. Higher-elevation elements (such as modals or tooltips) should increase their background opacity slightly and incorporate a faint Amber inner-glow to signify their active status in the visual stack.

## Shapes
The shape language is disciplined and geometric. A **Soft (0.25rem)** corner radius is the standard for cards and containers, providing just enough refinement to feel premium without losing the "hard" edge of technical equipment. 

Interactive elements like buttons use a slightly higher radius (rounded-lg) to distinguish them as touchpoints. Iconography must follow a "Thin-Line" style (1.5px stroke), ensuring they align with the delicate aesthetic of the technical borders.

## Components
- **Buttons:** Primary actions are solid Amber with black text. Secondary actions use the "Ghost" style—thin Amber borders with monochromatic text that fills on hover.
- **Glass Cards:** Containers for observatory details and booking info. They must use the backdrop-blur effect and the 1px technical border.
- **Data Readouts:** Small panels using Space Mono to display weather conditions, light pollution scales, and celestial coordinates.
- **Night-Vision Toggle:** A prominent, persistent switch that shifts the entire UI into the Red-Light Mode. This component should be easily accessible but shielded from accidental taps.
- **The Horizon List:** A horizontal scrolling list for selecting observatory suites, using high-resolution astronomical photography framed by thin technical borders.
- **Inputs:** Fields are underlined rather than boxed, utilizing the 1px border style to maintain a lightweight, airy feel.