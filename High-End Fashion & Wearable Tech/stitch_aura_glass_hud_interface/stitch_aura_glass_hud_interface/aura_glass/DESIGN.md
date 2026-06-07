---
name: Aura-Glass
colors:
  surface: '#0b112e'
  surface-dim: '#0b112e'
  surface-bright: '#323756'
  surface-container-lowest: '#060b29'
  surface-container-low: '#141937'
  surface-container: '#181d3b'
  surface-container-high: '#232846'
  surface-container-highest: '#2e3352'
  on-surface: '#dee0ff'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dee0ff'
  inverse-on-surface: '#292e4d'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f9f6ff'
  on-tertiary: '#2b2f49'
  tertiary-container: '#d6d9fb'
  on-tertiary-container: '#5a5e7b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#dee0ff'
  tertiary-fixed-dim: '#c1c4e6'
  on-tertiary-fixed: '#161a33'
  on-tertiary-fixed-variant: '#414561'
  background: '#0b112e'
  on-background: '#dee0ff'
  surface-variant: '#2e3352'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-main:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.2em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  safe-margin: 64px
  hud-gutter: 12px
---

## Brand & Style

This design system embodies the intersection of high-fashion luxury and bleeding-edge augmented reality. The aesthetic, **Futuristic-Chic**, focuses on a "Heads-Up Display" (HUD) experience that feels like a digital extension of the user's vision rather than a traditional screen interface. It targets an affluent, tech-forward audience that values both precision and elegance.

The UI leverages **Glassmorphism** to maintain environmental awareness, ensuring that digital elements feel like they are floating in the physical world. Visuals are characterized by ultra-thin linework, subtle luminous glows, and a sense of weightlessness. Motion and transitions are instantaneous and evocative of digital overlays, utilizing "flicker-in" or "scan-line" effects to reinforce the AR narrative.

## Colors

The palette is rooted in deep space and electric luminescence. 

- **Primary (Cyan Glow):** Used exclusively for interactive states, critical HUD data, and focal points. It should always appear "illuminated."
- **Secondary (Crisp White):** Used for primary typography and high-contrast iconography to ensure legibility against complex real-world backgrounds.
- **Tertiary (Deep Indigo):** Serves as the base "void." In a glassmorphic context, this color provides the tint for semi-transparent surfaces.
- **Neutral:** A slightly desaturated version of the base used for secondary containers and subtle separators.

Backgrounds should utilize varying levels of opacity (10-40%) of the Deep Indigo base to create the glass effect, while borders should use the Cyan Glow or White at 20-30% opacity.

## Typography

The typography system balances the elegance of modern sans-serifs with the technicality of monospaced fonts.

- **Geist** is the workhorse for all primary communication. It provides a clean, neutral, and highly legible foundation for the AR environment.
- **JetBrains Mono** is utilized for "Technical Data Overlays"—coordinates, battery percentages, biometric readings, and HUD labels. This font should often be paired with a slight Cyan Glow or used in all-caps to denote system-level information.

Text rendering should prioritize clarity. On thin glass surfaces, apply a subtle drop shadow to text to ensure it remains legible against light-colored physical environments.

## Layout & Spacing

The design system uses a **No Grid** contextual layout model, optimized for a field of view (FOV). Layouts are anchored to the corners and center of the vision field, utilizing "Safe Margins" to prevent interface elements from encroaching on the user's primary line of sight.

- **Rhythm:** An 8px base unit is used for component sizing, but a 4px "micro-unit" is permitted for tight technical HUD elements.
- **HUD Anchoring:** Elements are grouped in floating "clusters." These clusters use dynamic padding that expands or contracts based on the data density.
- **Safe Areas:** Critical information is placed in the lower-third or peripheral corners (upper-left/right), leaving the center clear for world viewing.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and light-based hierarchy rather than traditional shadows.

- **Z-Axis Layers:** Elements closer to the user are more opaque (60-80%) and have a more pronounced Cyan outer glow. Elements further away are more transparent (10-20%) and slightly blurred.
- **Backdrop Blur:** All containers must apply a `backdrop-filter: blur(12px)` to simulate the refractive property of high-end lenses.
- **HUD Borders:** Use 1px "Retina-thin" borders. Active elements feature a dual-border: a base white border at 10% opacity and a primary Cyan "focus" border that appears only on the corners (bracket-style).
- **Luminous Glow:** Interactive components emit a soft, diffused `0px 0px 15px` Cyan shadow to simulate light projecting onto the eye or lens.

## Shapes

The shape language is precise and architectural. 

- **Primary Shapes:** Elements use "Soft" (0.25rem) corner radii for a modern look that isn't overly organic. 
- **HUD Brackets:** For a technical feel, many containers do not have full borders; instead, they use L-shaped corner brackets.
- **Circular Elements:** Biometric scanners and status indicators (like battery or signal) use perfect circles to contrast against the mostly rectangular data blocks.
- **Clipping:** Use 45-degree chamfered corners for "Action" buttons to reinforce the futuristic, high-tech aesthetic.

## Components

### Buttons
Actionable elements are "ghost" style. They consist of a 1px Cyan border with a subtle gradient fill (Cyan to Transparent at 5%). On hover or focus, the button fills with a 20% Cyan tint and the text gains a neon glow.

### HUD Data Chips
Small, monospaced labels used for metadata. These are often enclosed in "brackets" rather than full boxes. Example: `[ 42.0 N ]`.

### Lists
Lists are vertical stacks of transparent glass cards. Each list item is separated by a 1px horizontal line that fades out at the edges (radial gradient).

### Input Fields
Inputs are represented as a single underlined 1px stroke. When active, the stroke transforms into a thin Cyan rectangle that "scans" from left to right.

### Cards
Glass containers with a 1px White (20% opacity) border. They feature a "Header" section separated by a thin line and often include a monospaced "Serial Number" in the top right corner for technical flair.

### Reticles & Crosshairs
Specialized components for AR-integration. These are circular or bracketed UI elements that track real-world objects, utilizing the Primary Cyan color and pulse animations to indicate "Lock-on" or "Analyzing" states.