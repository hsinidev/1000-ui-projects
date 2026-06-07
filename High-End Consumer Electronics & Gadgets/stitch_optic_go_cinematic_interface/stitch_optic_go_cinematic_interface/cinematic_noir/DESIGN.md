---
name: Cinematic Noir
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#dac1bf'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#a28c8a'
  outline-variant: '#544341'
  surface-tint: '#ffb3ad'
  primary: '#ffb3ad'
  on-primary: '#5a1a19'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#954742'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#242424'
  on-tertiary-container: '#8d8b8b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-md:
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
    letterSpacing: 0.1em
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
  gutter: 24px
  margin: 40px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of a private luxury screening room. It targets cinephiles and professionals who value high-performance hardware and boutique aesthetics. The personality is sophisticated, mysterious, and authoritative.

The style is a hybrid of **Glassmorphism** and **Tactile Minimalism**. It utilizes deep, layered backgrounds to simulate physical depth, while frosted glass overlays provide a sense of lightness and modernity. Every interaction is designed to feel intentional and premium, utilizing high-quality shadows and subtle metallic accents to ground the digital interface in the physical world of high-end optics.

## Colors

The palette is strictly dark to preserve the user's "dark-room" vision and maintain 4K contrast integrity. 

- **Deep Burgundy (#4A0E0E):** Used sparingly for primary brand moments, active states, and velvet-like background washes.
- **Gold (#D4AF37):** Reserved for critical interactive elements, focal points, and premium highlights. It should be treated as a metallic finish rather than a flat color.
- **Smoke (#1A1A1A / #2C2C2C):** The foundation of the UI. The darker shade acts as the base canvas, while the lighter shade defines containers and surfaces.
- **Accents:** Use low-opacity white (10-20%) for glass borders to simulate light catching the edge of a lens.

## Typography

This design system utilizes **Inter** for its exceptional legibility in low-light environments and its modern, neutral character that allows the content to remain the star.

Hierarchy is established through extreme weight contrast and generous letter spacing on labels. Headlines should feel architectural and bold. Captions and labels use an all-caps treatment with increased tracking to mimic the engraving found on professional camera equipment. High-contrast white text is used against dark backgrounds, but never at 100% opacity for body text—85% opacity is preferred to reduce "halation" or visual glow in a dark room.

## Layout & Spacing

The layout follows a **Fixed Grid** model to ensure the UI feels grounded and intentional, like a physical control panel. A 12-column grid is used for main navigation and content galleries, while a centered, focused layout is used for playback controls.

Spacing is generous to promote a "boutique" feel; density is the enemy of luxury. A 8px rhythmic system governs all margins and paddings. Use "safe zones" around the edges of the screen to account for projection overscan, ensuring no critical controls are lost at the periphery of the frame.

## Elevation & Depth

Depth is communicated through **Glassmorphism** and **Tonal Layering**. 

1.  **The Canvas:** The deepest layer (#1A1A1A) is static and matte.
2.  **The Containers:** Floating cards (#2C2C2C) use subtle, large-radius shadows (0px 20px 40px rgba(0,0,0,0.5)) to appear lifted.
3.  **The Glass Overlays:** Modals and temporary menus use a background blur (20px to 40px) with a semi-transparent Deep Burgundy or Smoke fill.
4.  **The Edge Light:** To define shapes without heavy borders, a 1px "inner stroke" is applied to the top and left sides of elements using a low-opacity Gold or White, simulating a light source from the upper-left.

## Shapes

The shape language is **Rounded**, striking a balance between the precision of professional gear and the approachability of a consumer device. 

Standard components use a 0.5rem (8px) radius. Larger cards and main containers use the "rounded-lg" (1rem) or "rounded-xl" (1.5rem) settings to feel softer and more premium. Circular shapes are reserved strictly for playback controls (Play/Pause) and profile avatars, creating a visual distinction between "Navigation" (rectilinear) and "Action" (circular).

## Components

### Buttons
Primary buttons use a solid Deep Burgundy fill with Gold text. Secondary buttons are "Ghost" style with a 1px Gold border. Hover states should include a subtle Gold outer glow to simulate a light being switched on.

### Cards
Cards feature the glassmorphism effect. The background is a blurred Smoke with a very thin (0.5px) border. Images within cards should have a slight vignette to pull the eye toward the center.

### Inputs & Sliders
Sliders (for brightness/focus) are critical for a projector. The track should be Smoke, and the handle should be a tactile, Gold "knob" with a subtle drop shadow to make it feel grabbable.

### Focus States
Since this is a cinema UI, the focus state is paramount. The focused element should be encased in a 2px Gold ring with a soft outer "bloom" effect, ensuring high visibility from across a room.

### Navigation List
Vertical lists should use generous vertical padding (16px+). The active item is indicated by a Deep Burgundy "velvet" background pill that slides vertically to follow the user's selection.