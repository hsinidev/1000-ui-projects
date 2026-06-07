---
name: Bio-Scan Design System
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
  on-surface-variant: '#434654'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#737685'
  outline-variant: '#c3c6d6'
  surface-tint: '#0c56d0'
  primary: '#003d9b'
  on-primary: '#ffffff'
  primary-container: '#0052cc'
  on-primary-container: '#c4d2ff'
  inverse-primary: '#b2c5ff'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#7b2600'
  on-tertiary: '#ffffff'
  tertiary-container: '#a33500'
  on-tertiary-container: '#ffc6b2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#ffdbcf'
  tertiary-fixed-dim: '#ffb59b'
  on-tertiary-fixed: '#380d00'
  on-tertiary-fixed-variant: '#812800'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  numeric-data:
    fontFamily: geist
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-margin: 40px
  gutter: 24px
  section-gap: 64px
  stack-sm: 12px
  stack-md: 24px
---

## Brand & Style

This design system embodies "Clinical-Chic"—a high-end aesthetic tailored for biometric security environments where precision meets luxury. The interface must feel as sterile and reliable as a surgical suite, yet as intuitive and fluid as premium consumer electronics. 

The target audience consists of high-security facility managers and elite end-users. The emotional response should be one of absolute trust and effortless control. To achieve this, the system utilizes a "Glassmorphism" approach, layering semi-transparent surfaces over a pure, expansive white void. This creates a sense of depth and technological sophistication without sacrificing the "medical" cleanliness required by the brand narrative.

## Colors

The palette is anchored by **Pure White (#FFFFFF)**, serving as the sterile canvas. **Medical Blue (#0052CC)** is used exclusively for primary actions, secure states, and brand reinforcement, ensuring high-contrast legibility. 

**Glass-Cyan (#E0F7FA)** acts as the atmospheric layer, appearing in semi-transparent states to provide a "frosted glass" effect. This cyan tint should be used for background blurs and subtle highlights, mimicking the look of laboratory glassware. All interactive glass surfaces should utilize a 70% opacity with a heavy backdrop blur to maintain readability against moving "liquid" background elements.

## Typography

This design system utilizes a tiered font strategy to balance authority and technical precision. **Metropolis** is used for headlines to provide a geometric, structured feel. **Inter** serves as the workhorse for body copy, chosen for its exceptional legibility in high-stress security contexts. 

**Geist** is introduced for labels and technical data displays, providing a "developer-centric" precision that reinforces the advanced nature of biometric scanning. For all numerical readouts—such as scan percentages or timestamps—always use Geist with tabular lining enabled to prevent layout shift during real-time data updates.

## Layout & Spacing

The layout philosophy follows a strict 12-column fixed grid for desktop and tablet interfaces, emphasizing symmetry and order. A generous 40px outer margin ensures the UI never feels cramped, maintaining the "Professional" and "Sterile" mood.

Spacing follows an 8px base unit. Vertical rhythm is critical; use large `section-gap` units to separate distinct biometric processes (e.g., Enrollment vs. Verification) to prevent cognitive overload. Elements should be grouped in logical "pods" using the `stack-md` unit to reinforce the modularity of the system.

## Elevation & Depth

Hierarchy is established through a combination of backdrop blurs and "Ambient Shadows." Instead of traditional dark shadows, this design system uses highly diffused, low-opacity shadows tinted with **Medical Blue** (e.g., 8% opacity of #0052CC) to create a subtle glow rather than a heavy drop.

1.  **Base Layer:** Pure White (#FFFFFF).
2.  **Surface Layer:** Glass-Cyan (#E0F7FA) with 70% opacity and 20px blur. 
3.  **Active Layer:** Medical Blue accents or high-contrast white text.

Edges of glass panels must have a 1px "inner-glow" stroke (Pure White at 40% opacity) on the top and left sides to simulate light catching the edge of a physical glass pane.

## Shapes

The shape language is "Rounded"—soft enough to feel approachable but precise enough to maintain a professional medical aesthetic. Standard components use a 0.5rem radius, while larger containers and cards utilize 1.5rem (`rounded-xl`). 

For "liquid" transitions, shapes should morph using cubic-bezier curves (`0.4, 0.0, 0.2, 1`), giving the impression of fluid movement between states. Scanning frames and focus brackets should use the "Sharp" (0px) or very small (2px) radius to denote technical precision.

## Components

### Buttons
*   **Primary:** Solid Medical Blue with White text. High-fidelity "liquid" hover state where the blue subtly expands.
*   **Secondary/Glass:** Frosted Glass-Cyan background with Medical Blue text and a 1px Blue border.

### Biometric Pulse (Custom Component)
A central scanning element consisting of concentric circular rings with varying opacities of Glass-Cyan. It should use a breathing animation (scale 1.0 to 1.05) when idle.

### Input Fields
Minimalist bottom-border only or fully enclosed glass fields. The focus state should trigger a "liquid" fill animation where the Glass-Cyan tint creeps up from the bottom of the field.

### Status Chips
Small, pill-shaped indicators. For "Secure" states, use a Medical Blue pulse. For "Warning," use a soft yellow glow without harsh black borders.

### Cards & Modals
All containers must use the backdrop blur effect. Modals should appear to float above the interface with a 40px blur radius shadow, ensuring the underlying "Pure White" context remains visible but out of focus.