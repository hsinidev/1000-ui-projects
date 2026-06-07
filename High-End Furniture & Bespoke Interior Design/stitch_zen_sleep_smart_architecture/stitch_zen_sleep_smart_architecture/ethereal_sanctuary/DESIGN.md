---
name: Ethereal Sanctuary
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#46464c'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#77767d'
  outline-variant: '#c7c5cc'
  surface-tint: '#5c5d6e'
  primary: '#5c5d6e'
  on-primary: '#ffffff'
  primary-container: '#e6e6fa'
  on-primary-container: '#656677'
  inverse-primary: '#c5c5d8'
  secondary: '#725a39'
  on-secondary: '#ffffff'
  secondary-container: '#fbdbb0'
  on-secondary-container: '#765f3d'
  tertiary: '#575f65'
  on-tertiary: '#ffffff'
  tertiary-container: '#e1e9f0'
  on-tertiary-container: '#61696f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e1f5'
  primary-fixed-dim: '#c5c5d8'
  on-primary-fixed: '#191b29'
  on-primary-fixed-variant: '#444655'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#dbe4ea'
  tertiary-fixed-dim: '#bfc8ce'
  on-tertiary-fixed: '#151d22'
  on-tertiary-fixed-variant: '#40484d'
  background: '#fbf9f9'
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
  headline-lg-mobile:
    fontFamily: manrope
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: plusJakartaSans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  section-gap: 64px
---

## Brand & Style

The design system is centered on the concept of "The Sleep Sanctuary," an architectural approach to digital interface design for high-end smart bedrooms. The brand personality is serene, restorative, and profoundly compassionate. It aims to reduce cognitive load and physiological arousal before sleep, evoking a sense of weightlessness and safety.

The aesthetic blends **Minimalism** with **Glassmorphism**. By utilizing translucent layers and ethereal blurs, the UI feels less like a rigid screen and more like a projection on a soft surface. A signature "Breathing" animation cycle (4s inhale/6s exhale) is applied to ambient glows and primary status indicators to subconsciously pace the user’s respiration, reinforcing the compassionate nature of the design system.

## Colors

The palette is derived from natural twilight and organic materials. **Lavender (#E6E6FA)** serves as the primary action and state color, chosen for its psychological association with relaxation. **Frost White (#F0F8FF)** provides the ethereal, airy base for glass surfaces, while **Ash Wood (#D2B48C)** is used sparingly for grounding elements and tactile controls, mimicking high-end bedroom architecture.

The color mode is a specialized "Soft Light" mode—avoiding harsh pure whites in favor of desaturated, cool-toned neutrals to prevent blue-light strain. Gradients should be subtle and non-linear, mimicking the way light diffuses through frosted glass or thin fabric.

## Typography

This design system utilizes **manrope** for its core typography. Its geometric yet humanist proportions offer a modern, architectural feel that remains legible even at low brightness levels. Display type uses a light weight (300) with tight tracking to emphasize the "Ethereal" aesthetic.

For functional labels and interactive micro-copy, **plusJakartaSans** is employed. Its slightly rounder, friendlier terminals provide a "Compassionate" touch to technical data. All type should be rendered with high-quality anti-aliasing to maintain the soft-edged visual language.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** with an emphasis on "Negative Space as Luxury." On desktop, content is centered within a generous 1200px container. On mobile, side margins are increased to 24px to ensure the UI feels uncrowded.

Vertical spacing is intentionally oversized (using the "section-gap" variable) to allow the "Breathing" animations of various components to exist without visual interference. Elements are grouped using proximity rather than hard dividers to maintain the minimalist flow.

## Elevation & Depth

Depth is achieved through **Backdrop Blurs** and **Ambient Glows** rather than traditional shadows. 

1.  **Base Layer:** Solid desaturated off-white.
2.  **Surface Layer:** Frost White (#F0F8FF) at 60% opacity with a 20px backdrop-blur.
3.  **Active Layer:** Lavender (#E6E6FA) tint with a soft, 40px spread "breathing" outer glow (0.1 opacity) to indicate focus or activity.

Shadows, where necessary for legibility, must be tinted with the Primary Lavender color and have a blur radius of at least 32px to remain "soft-edged."

## Shapes

The shape language is consistently **Rounded** (Level 2). This eliminates "sharpness" from the environment, reinforcing the feeling of comfort and safety. 

- Large containers (cards) use `rounded-xl` (1.5rem).
- Interactive elements (buttons, sliders) use `rounded-lg` (1rem).
- Small indicators use a full pill-shape.

## Components

### Buttons & Interaction
Buttons are semi-transparent glass pills. The primary action button uses a Lavender-to-Frost gradient with a subtle 1px inner border to simulate light catching the edge of a glass pane. 

### Environmental Sliders
Sliders for light temperature and sound volume are thick, tactile tracks. The handle is an Ash Wood (#D2B48C) circle that grows slightly when touched. The track itself fills with a "breathing" Lavender glow.

### Soft-Edged Cards
Cards are the primary container. They feature a 60% Frost White opacity with a heavy background blur. No harsh borders; instead, a soft inner glow defines the edge.

### Breathing Indicators
Used for "System On" or "Sleep Monitoring" states. A soft Lavender circle that expands and contracts in a 10-second loop, serving as a biological pacer for the user.

### Lists & Labels
Lists are borderless, separated by whitespace. Iconography consists of thin-stroke (1.5px) vector lines with rounded caps to match the typography.