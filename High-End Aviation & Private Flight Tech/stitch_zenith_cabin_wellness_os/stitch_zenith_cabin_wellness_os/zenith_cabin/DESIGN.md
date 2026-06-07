---
name: Zenith-Cabin
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#40484d'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#70787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0d6683'
  primary: '#0d6683'
  on-primary: '#ffffff'
  primary-container: '#89cff0'
  on-primary-container: '#005974'
  inverse-primary: '#8ad0f1'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#5d5e60'
  on-tertiary: '#ffffff'
  tertiary-container: '#c5c6c8'
  on-tertiary-container: '#515254'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bee9ff'
  primary-fixed-dim: '#8ad0f1'
  on-primary-fixed: '#001f2a'
  on-primary-fixed-variant: '#004d65'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e4'
  tertiary-fixed-dim: '#c6c6c8'
  on-tertiary-fixed: '#1a1c1d'
  on-tertiary-fixed-variant: '#454749'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: manrope
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-md:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: manrope
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter-desktop: 32px
  margin-desktop: 64px
  gutter-mobile: 16px
  margin-mobile: 24px
  container-max: 1440px
---

## Brand & Style
The brand personality is sentient, restorative, and ethereal. This design system serves as a high-end wellness operating system that feels less like a computer interface and more like a digital extension of a physical sanctuary. 

The aesthetic is **Minimalist-Refined** blended with **Glassmorphism**. It prioritizes a sense of "air" and "weightlessness." The UI must evoke an emotional response of immediate serenity and effortless control. By utilizing liquid-inspired motion and translucent layering, the interface feels alive and responsive to the user's presence without being intrusive.

## Colors
The palette is monochromatic and airy, designed to reduce cognitive load and visual noise.

- **Silk White (#F9F9FB):** Used as the foundational surface color, providing a crisp, high-end base.
- **Soft Azure (#89CFF0):** Reserved for interactive states, biological feedback, and "active" environment triggers. It represents the "sentience" of the OS.
- **Silver (#C0C0C0):** Used for refined borders, subtle iconography, and secondary metadata to provide structure without creating heavy visual breaks.
- **Background Tints:** Always use a subtle gradient or a blurred "aura" of Soft Azure behind glass layers to maintain the futuristic, atmospheric depth.

## Typography
The typography system uses **Manrope** for high-level headings to inject a modern, balanced, and premium feel. **Inter** is utilized for body text and labels due to its exceptional clarity and systematic nature.

Text should be treated with generous tracking on labels to enhance the "refined" feel. For biological data and numerical readouts, use medium weights to ensure legibility against translucent backgrounds. Contrast should be maintained through weight and spacing rather than aggressive color shifts.

## Layout & Spacing
This design system utilizes a **fluid grid** with expansive margins to maintain the minimalist atmosphere. 

- **Desktop:** 12-column grid with 32px gutters. Content is often centered in a "hero" container to evoke a sense of focus.
- **Mobile:** 4-column grid with 16px gutters. Elements should occupy full-width glass cards to maximize touch targets for "Instant-Comfort" triggers.
- **Rhythm:** Use an 8px base unit. Component padding should be generous (typically 24px or 32px) to allow the "Glass" effect to breathe.

## Elevation & Depth
Depth is created through **Glassmorphism** and **Ambient Shadows** rather than traditional z-index stacking.

- **Surface Layers:** All primary containers use a 60% opacity Silk White background with a `backdrop-filter: blur(20px)`.
- **Borders:** Containers must feature a 1px solid border using a gradient of Silver to transparent to simulate light hitting the edge of glass.
- **Shadows:** Use extremely diffused, low-opacity shadows (Color: #89CFF0 at 10% opacity, Blur: 40px, Spread: -10px) to give components a soft "glow" instead of a heavy drop-shadow.
- **Interaction:** When touched or hovered, the backdrop blur intensity should increase, and the Azure glow should subtly expand.

## Shapes
The shape language is defined by **Rounded (0.5rem base)** geometry. This provides a balance between the precision of high-end technology and the softness of a wellness environment.

- **Cards & Triggers:** Use `rounded-xl` (1.5rem) to make large interaction areas feel safe and approachable.
- **Interactive Elements:** Buttons and sliders should use fully rounded (pill) ends to mimic the "liquid" design narrative.
- **Fluidity:** Elements representing biometrics or environmental flow (air, light) should utilize organic, non-perfectly-circular blobs in the background to reinforce the "Sentient" aspect of the OS.

## Components
- **Instant-Comfort Triggers:** Large-scale, glass cards with centered icons and labels. These act as "one-tap" scenes (e.g., "Deep Sleep," "Focus"). Upon activation, the Azure glow pulses slowly like a heartbeat.
- **Fluid Progress Bars:** Used for biometric data (Heart Rate, Hydration). These are not static bars but "liquid" fills that have a slight wave animation at the leading edge.
- **Elegant Sliders:** For lighting and temperature. The track is a thin Silver line, while the thumb is a larger, glowing Soft Azure glass sphere.
- **Biological Feedback Loops:** Small, pulsing orbital rings that sit near the corners of the screen, indicating the OS is actively monitoring and adjusting the environment.
- **Input Fields:** Minimalist underlines with Soft Azure focus states. Floating labels are used to keep the interface clean when empty.