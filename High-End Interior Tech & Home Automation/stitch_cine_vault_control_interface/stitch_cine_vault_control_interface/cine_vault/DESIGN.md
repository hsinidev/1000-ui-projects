---
name: Cine-Vault
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#dcc0bd'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#a38b88'
  outline-variant: '#554240'
  surface-tint: '#ffb4aa'
  primary: '#ffb4aa'
  on-primary: '#5f1410'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#9d4139'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#212121'
  on-tertiary-container: '#8a8888'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  title-sm:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  control-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  touch-target-min: 44px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is engineered to evoke the atmosphere of a high-end private screening room. It prioritizes immersion, exclusivity, and precision. The target audience consists of luxury homeowners and professional AV integrators who demand a seamless transition between the physical theater environment and the digital control interface.

The design style is a sophisticated blend of **Glassmorphism** and **Tactile Minimalism**. By utilizing translucent layers, the UI maintains a sense of depth and spatial awareness, while high-contrast tactile elements ensure that critical playback controls are immediately discoverable in low-light environments. The emotional response is one of quiet power and cinematic gravitas.

## Colors

The palette is anchored in a permanent dark mode configuration. **Deep Burgundy** serves as the primary brand expression, used sparingly for high-level surfaces and branding to maintain visual comfort. **Gold** is reserved strictly for focus states, active playback indicators, and premium call-outs, acting as a "jewelry" layer over the UI. 

**Charcoal** forms the foundation of the interface, providing a neutral backdrop that allows film poster art and media metadata to remain the focal point. Functional neutrals are kept in the off-white spectrum to prevent harsh glare while maintaining legibility for technical controls.

## Typography

The typographic hierarchy utilizes a dual-font strategy to balance editorial elegance with functional clarity. **Noto Serif** is used for movie titles, section headers, and high-level navigation, providing a classic "literary" feel associated with prestigious film institutions. 

**Manrope** is used for all functional UI elements, playback data, and technical settings. Its geometric yet open structure ensures high legibility on mobile devices and remote controls. Label styles frequently employ uppercase styling with increased letter spacing to denote secondary information or categorization without cluttering the visual field.

## Layout & Spacing

This design system employs a **Fluid Grid** model with strict adherence to an 8px spatial rhythm. Layouts are designed to be "center-out," focusing the user's eye on the media content before moving to peripheral controls. 

On mobile interfaces, the layout utilizes a "thumb-zone" priority, placing critical transport controls within the bottom third of the screen. Margins are generous to prevent the UI from feeling "crowded," maintaining the luxury of whitespace. Safe areas are strictly observed to ensure the interface feels grounded within the hardware frame of high-end tablets and dedicated cinema controllers.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and backdrop-blur effects rather than traditional drop shadows. 
- **Surface 0 (Base):** Deep Charcoal (#121212) or the blurred media artwork itself.
- **Surface 1 (Panels):** Translucent Charcoal (60% opacity) with a 20px backdrop blur and a subtle 1px inner border in Burgundy or Gold.
- **Surface 2 (Active Elements):** High-contrast buttons with a slight "inner glow" to suggest physical depth (Tactile).

Interaction is indicated by light. Focused elements should emit a soft Gold glow (#D4AF37 at 20% opacity), mimicking the way a projector light hits a surface.

## Shapes

The shape language is **Rounded**, favoring 0.5rem (8px) for standard components and 1.5rem (24px) for larger container panels. This softens the technical nature of the controller, making it feel more like a lifestyle product than a piece of industrial equipment. 

Interactive controls like the "Play/Pause" cluster may use pill-shaped containers to differentiate them from static informational cards. Media posters maintain a very slight 4px radius to preserve the classic "film cell" aesthetic while aligning with the modern system.

## Components

### Buttons
Primary action buttons use a "Tactile" style: solid Burgundy fills with Gold text or icons. Secondary buttons use the Glassmorphic style: blurred translucent backgrounds with 1px Gold outlines. The active/pressed state should involve a slight downward scale (98%) to simulate a physical click.

### Transport Controls
A specialized component set for playback. The "Play" button is consistently the largest element, highlighted with a Gold glow. Scrubbing bars use a Gold track and a high-contrast white "handle" for precision.

### Cards (Media)
Poster cards utilize a "Zero-Border" approach, relying on the glassmorphic container behind them for structure. Titles appear only on hover or when the card is focused, keeping the grid clean and visually focused on the art.

### Status Indicators
Small, pill-shaped chips used for resolution (4K), audio format (Dolby Atmos), and theater status (Lighting: Dim). These utilize Manrope in all-caps for maximum clarity.

### Sliders
Used for volume and lighting. The track is a thin Burgundy line, while the thumb is a tactile Gold circle. When adjusted, a large, translucent numerical overlay appears in the center of the screen to provide immediate feedback.