---
name: Zen-Room OS
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c5c7c8'
  on-secondary: '#2e3132'
  secondary-container: '#494c4d'
  on-secondary-container: '#babcbd'
  tertiary: '#e7bf99'
  on-tertiary: '#432b10'
  tertiary-container: '#281400'
  on-tertiary-container: '#9d7b5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e1e3e4'
  secondary-fixed-dim: '#c5c7c8'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#454748'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#e7bf99'
  on-tertiary-fixed: '#2b1701'
  on-tertiary-fixed-variant: '#5d4124'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
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
  container-padding: 40px
  gutter: 24px
  card-gap: 16px
---

## Brand & Style

The design system is centered on the concept of "Digital Silence." It aims to reduce cognitive load for users within smart acoustic pods, providing a high-tech interface that feels as quiet as the physical space itself. The brand personality is sophisticated and unobtrusive, catering to professionals who require deep focus.

The style leverages **Glassmorphism** as its primary visual driver. By using translucent layers and soft background blurs, the UI feels lightweight and integrated into the pod’s environment rather than a flat overlay. Depth is communicated through light refraction rather than heavy shadows, evoking a sense of calm and premium technology.

## Colors

This design system utilizes a deep, monochromatic base to reinforce the "Midnight" atmosphere. 

- **Primary (Midnight Blue):** Used for the deep background environment, creating an infinite sense of space.
- **Secondary (Off-White):** Reserved for high-priority typography and essential iconography to ensure legibility against dark backgrounds.
- **Accent (Cyan Glow):** A high-tech "status" color used sparingly for active indicators, glowing sliders, and focused states.
- **Translucent Layers:** Multi-layered whites with varying opacities (5% to 15%) are used to create the signature frosted-glass effect.

## Typography

The typography strategy balances modern approachability with technical precision. 

**Manrope** is used for headlines to provide a soft, balanced feel that prevents the UI from appearing too "cold." **Geist** handles body copy with its mono-influenced clarity, ideal for displaying environmental data. **Space Grotesk** is used for labels and technical readouts (like decibel levels or temperature), leaning into the futuristic nature of the acoustic pod.

Maintain high contrast for all text. Use "Off-White" at 100% opacity for headings and 70% opacity for secondary body text to establish a clear hierarchy.

## Layout & Spacing

This design system employs a **Fixed Grid** model for centralized control panels and a **Fluid Grid** for secondary dashboard views. 

The layout relies on generous "Safe Zones" to prevent the interface from feeling cramped. A strict 8px rhythmic grid governs all padding and margins. Use wide gutters (24px+) between glass cards to allow the background midnight blue to "breathe" through the gaps, enhancing the feeling of physical space.

## Elevation & Depth

In this design system, elevation is not achieved through shadows, but through **Backdrop Saturation and Blur**. 

1.  **Level 0 (Base):** Midnight Blue solid background.
2.  **Level 1 (Cards):** 20px Backdrop Blur, 10% White opacity, 1px solid border (12% White).
3.  **Level 2 (Modals/Pop-overs):** 40px Backdrop Blur, 15% White opacity, 1px solid border (20% White).

To simulate "Glow," active elements (like status dots) should have an outer glow using the Accent color with a 15px spread and 40% opacity, suggesting a light source within the frosted glass.

## Shapes

The shape language is "Soft-Modern." All glass containers use a consistent **1rem (16px)** corner radius to soften the high-tech aesthetic, making the environment feel more organic and inviting. Small interactive elements like chips or toggle handles should use the **Pill (fully rounded)** style to differentiate them from structural layout cards.

## Components

- **Frosted Cards:** These are the primary containers. They must have a `backdrop-filter: blur(20px)` and a subtle top-down linear gradient (White 10% to White 2%) to simulate light hitting the top edge.
- **Glowing Status Indicators:** Small circular pips that use a CSS `box-shadow` glow. Green for "Available," Pulse-Amber for "Occupied," and Blue for "Focus Mode."
- **Sleek Sliders:** Environment controls (Lighting, Fan, Sound Masking) use a thin 4px track. The handle is a larger, frosted circle that "glows" when dragged.
- **Environment Toggles:** High-contrast switches that, when active, fill with a subtle cyan gradient and increase the backdrop blur of the entire card.
- **Quick-Action Chips:** Pill-shaped, semi-transparent buttons for one-touch settings like "Deep Work" or "Video Call," using **Space Grotesk** labels.