---
name: Ether-Home
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3f484c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6f787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0c6780'
  primary: '#0c6780'
  on-primary: '#ffffff'
  primary-container: '#87ceeb'
  on-primary-container: '#005870'
  inverse-primary: '#89d0ed'
  secondary: '#585e6d'
  on-secondary: '#ffffff'
  secondary-container: '#dadff0'
  on-secondary-container: '#5d6371'
  tertiary: '#5a5f62'
  on-tertiary: '#ffffff'
  tertiary-container: '#c1c5c9'
  on-tertiary-container: '#4d5255'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#baeaff'
  primary-fixed-dim: '#89d0ed'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d62'
  secondary-fixed: '#dde2f3'
  secondary-fixed-dim: '#c1c6d7'
  on-secondary-fixed: '#161c28'
  on-secondary-fixed-variant: '#414754'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Manrope
    fontSize: 22px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
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
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  container-margin: 24px
  gutter: 16px
  touch-target: 48px
---

## Brand & Style

The design system is centered on the concept of "Atmospheric Intelligence." It prioritizes serenity and spatial depth to transform complex estate management into a tranquil, effortless experience. By utilizing a **Glassmorphic** style, the interface feels lightweight and integrated into the user's environment rather than a heavy digital overlay.

The aesthetic combines **Minimalism** with high-end digital craftsmanship. The goal is to evoke a sense of clarity and breathability. Surfaces are not solid; they are semi-translucent, allowing the underlying environment or wallpapers to bleed through, suggesting that the OS is a living part of the home. The emotional response is one of calm control—never overwhelming the user with data, but inviting them through soft textures and gentle transitions.

## Colors

The palette for this design system is airy and high-contrast. **Sky Blue** serves as the primary functional color, reserved strictly for active states, primary call-to-actions, and "on" status indicators. **Soft Charcoal** provides the necessary grounding, used for high-readability text and deep contrast elements to ensure the UI remains accessible against translucent backgrounds.

The core of the interface relies on a "Frosted Base"—a translucent white or very light gray that allows for a backdrop blur effect. This creates a multi-layered environment where hierarchy is defined by opacity and blur rather than just flat color. Status colors (Success, Warning, Error) should follow a muted, pastel-tinted logic to maintain the "Calm" aesthetic.

## Typography

This design system utilizes **Manrope** as the primary typeface for headlines and body copy. Its balanced, modern geometric shapes provide the "refined" feel necessary for a smart estate OS. Headlines use a tighter letter-spacing and heavier weights to establish a clear hierarchy against the soft glass backgrounds.

**Inter** is utilized for functional labels and micro-copy. Its utilitarian nature and high legibility at small sizes make it ideal for technical status indicators, timestamps, and sensor data. All typography must maintain high contrast against the frosted glass containers, primarily using Soft Charcoal (#2F3542) or a pure white when placed over darker image-based backgrounds.

## Layout & Spacing

The layout philosophy follows a **fluid grid** model with mobile-first density. Given the "estate" context, the design system assumes use on both wall-mounted tablets and handheld mobile devices. It utilizes a 12-column system for desktop/tablet and a 4-column system for mobile.

Spacing is generous, prioritizing "breathable" touch targets. A minimum touch target of 48px is enforced for all interactive elements. Content is grouped into logical "zones" using significant white space (the `xxl` unit) to prevent the visual clutter often associated with home automation. Margins are fixed at a minimum of 24px to ensure UI elements do not feel cramped against the edges of the physical hardware.

## Elevation & Depth

Elevation in this design system is communicated through **Glassmorphism** and spatial layering rather than traditional drop shadows. Depth is created by stacking semi-transparent surfaces with varying levels of `backdrop-filter: blur()`.

1.  **Base Layer:** The background (usually a high-quality, calm nature scene or architectural photo).
2.  **Level 1 (Panels):** Frosted glass cards with a 20px–30px blur and a 1px semi-transparent white border to define the edge.
3.  **Level 2 (Modals/Pop-overs):** Increased opacity and a deeper, highly diffused ambient shadow (0px 20px 40px rgba(0,0,0,0.05)) to signify the highest priority.

Shadows are never harsh or black; they are "Ambient Shadows"—diffused, low-opacity, and slightly tinted by the background colors to maintain the "Calm" aesthetic.

## Shapes

The shape language is defined by extreme softness and organic curves. The standard radius for primary containers and cards is **24px**, creating a friendly and approachable silhouette that mimics high-end modern furniture and hardware.

Secondary elements like buttons use a slightly smaller radius for a tighter appearance, while interactive controls such as toggles and sliders utilize fully rounded (pill-shaped) caps. Sharp corners are entirely avoided in the design system to reinforce the "Calm" narrative. Every container edge should feel smooth and safe to the touch.

## Components

### Buttons & Interaction
Buttons are either "Glass-Filled" (semi-transparent white with a subtle border) or "Primary" (Sky Blue). They feature a subtle scale-down effect (98%) on press to provide tactile feedback without the need for heavy skeuomorphic textures.

### Frosted Cards
The fundamental building block. Every card must feature a `backdrop-filter: blur(20px)` and a `1px` inner stroke of `rgba(255,255,255,0.5)`. Content inside cards should have a standard padding of `lg` (24px).

### Interactive Sliders & Toggles
Used for dimmers, volume, and temperature. Sliders feature a thick, pill-shaped track and a larger, circular thumb to ensure ease of use on mobile. Toggles use the Sky Blue primary color for the "On" state, accompanied by a soft glow effect to indicate active power.

### Status Indicators
Small, glowing dots or subtle icons that use Sky Blue to show activity. These should be placed consistently in the top-right of cards or adjacent to labels to provide a quick visual scan of the home's state.

### Layout Modules
*   **Quick Actions:** A horizontal scroll of pill-shaped chips for one-touch scenes (e.g., "Arriving Home," "Sleep Mode").
*   **Sensor Grid:** A dense collection of cards showing temperature, humidity, and security status.