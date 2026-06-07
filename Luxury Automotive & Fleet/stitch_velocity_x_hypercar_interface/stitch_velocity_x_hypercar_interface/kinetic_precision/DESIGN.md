---
name: Kinetic Precision
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#ffffff'
  on-secondary: '#283500'
  secondary-container: '#c3f400'
  on-secondary-container: '#556d00'
  tertiary: '#c1c7cf'
  on-tertiary: '#2b3137'
  tertiary-container: '#050b10'
  on-tertiary-container: '#747a81'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#c3f400'
  secondary-fixed-dim: '#abd600'
  on-secondary-fixed: '#161e00'
  on-secondary-fixed-variant: '#3c4d00'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
  telemetry-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 64px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system targets an elite demographic of automotive enthusiasts and high-performance engineers. The brand personality is aggressive, technical, and uncompromisingly premium. It evokes the sensation of being inside a $3M hypercar—a space where every millisecond and every micron matters.

The visual style is a hybrid of **Glassmorphism** and **Tactile Engineering**. It utilizes deep, layered backgrounds with carbon fiber textures to ground the interface, while interactive elements float on semi-transparent, frosted glass panels. The UI mimics a high-resolution heads-up display (HUD), using precision lines and glowing indicators to guide the user through a high-velocity digital experience. The emotional response is one of total control and sensory heightening.

## Colors

The palette is anchored by a sophisticated **Matte Black** (#0A0A0A), which serves as the canvas for all interfaces, ensuring maximum contrast and a "stealth" aesthetic. **Electric Lime** (#CCFF00) is the high-visibility tactical color, reserved exclusively for call-to-actions, active telemetry, and glowing trend lines. 

**Silver** (#E2E8F0) and metallic grays provide the structural framework, appearing in typography and micro-borders to simulate machined aluminum components. Accent colors are used sparingly to maintain a focused, cockpit-like atmosphere where information density is high but visual noise is low.

## Typography

The typography strategy prioritizes legibility under "high-speed" scanning. **Space Grotesk** is used for headlines and data labels, providing a technical, geometric edge that feels like a precision instrument. For long-form content and technical specifications, **Inter** provides a clean, neutral balance that ensures readability against dark, textured backgrounds.

Large display type should utilize tight letter spacing to feel "compressed" and powerful. Labels and small telemetry data points should be set in uppercase with increased tracking to mimic the engraving found on performance automotive parts.

## Layout & Spacing

The layout follows a rigorous **12-column fluid grid** with generous outer margins to evoke a sense of luxury and exclusivity. Elements are organized into modular "units" that snap to a 4px baseline grid, ensuring mathematical precision in every view.

Spacing is used to create distinct "zones" of information, similar to a dashboard cluster. High-priority telemetry is centered or placed in the primary line of sight, while secondary controls are pushed to the peripheries. Use heavy padding within containers to maintain the premium feel of "air" around critical components.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and light-emissive properties rather than traditional shadows. This design system uses three primary tiers of elevation:

1.  **The Base Layer:** Matte black with a subtle carbon-fiber weave pattern (low-opacity overlay).
2.  **The Mid Layer:** Semi-transparent "dark glass" panels (background-blur: 20px) with 1px silver inner-borders to define edges.
3.  **The Active Layer:** Elements that "glow." These use Electric Lime box-shadows with a high blur radius and low opacity to simulate neon light reflecting off a dark surface.

Interaction is signaled through "illumination" rather than physical lifting; when a user interacts with a component, its borders should transition from Silver to a glowing Electric Lime.

## Shapes

The shape language is defined by **Precision Geometry**. While the base roundedness is set to "Soft" (4px), this is intended to mimic the look of CNC-machined metal—edges that are technically rounded for safety but appear sharp and exact to the eye.

Interactive elements like buttons or input fields may occasionally use "clipped corners" (45-degree chamfers) to reinforce the aeronautical engineering vibe. Containers and cards should maintain a consistent, subtle radius to contrast against the sharp, needle-like lines of the data visualizations.

## Components

### Buttons
Primary buttons are high-impact: Solid Electric Lime background with black text. Secondary buttons are "Ghost" style: Silver 1px borders that glow lime upon hover. All buttons use uppercase labels for a technical feel.

### Cards & Containers
Cards utilize a "Glass-Fiber" effect: a semi-transparent dark fill over the carbon fiber background. They feature a 1px silver top-border to catch the "overhead light" of the digital cockpit.

### Inputs & Controls
Input fields are minimalist—bottom borders only until focused, at which point the entire perimeter glows. Selection controls (radio/checkbox) should resemble toggle switches found in racing cockpits.

### Performance Gauges
A custom component unique to the design system, these are radial or linear indicators using thin, glowing lines to represent speed, torque, or battery deployment. 

### Data Chips
Small, pill-shaped tags used for status indicators (e.g., "STABLE", "NITROUS READY"). These use a dark gray background with telemetry-style typography.