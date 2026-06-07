---
name: Terra-Diver
colors:
  surface: '#111413'
  surface-dim: '#111413'
  surface-bright: '#373a38'
  surface-container-lowest: '#0c0f0e'
  surface-container-low: '#191c1b'
  surface-container: '#1d201f'
  surface-container-high: '#272b29'
  surface-container-highest: '#323534'
  on-surface: '#e1e3e0'
  on-surface-variant: '#bfc9c4'
  inverse-surface: '#e1e3e0'
  inverse-on-surface: '#2e3130'
  outline: '#89938f'
  outline-variant: '#3f4945'
  surface-tint: '#94d3c1'
  primary: '#94d3c1'
  on-primary: '#00382e'
  primary-container: '#004d40'
  on-primary-container: '#7ebdac'
  inverse-primary: '#29695b'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#444343'
  on-tertiary-container: '#b2b0af'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#afefdd'
  primary-fixed-dim: '#94d3c1'
  on-primary-fixed: '#00201a'
  on-primary-fixed-variant: '#065043'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#111413'
  on-background: '#e1e3e0'
  surface-variant: '#323534'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1-instrument:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  h2-technical:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-standard:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-bold:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.6'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  unit-xs: 4px
  unit-sm: 8px
  unit-md: 16px
  unit-lg: 24px
  unit-xl: 48px
  water-mode-gap: 20px
---

## Brand & Style

This design system embodies the precision and durability of high-performance marine horology. The brand personality is authoritative, resilient, and technical, catering to professional divers and enthusiasts who demand reliability under extreme conditions.

The aesthetic combines **Nautical-Industrial** precision with a **Tactile-High-Tech** interface. Key visual drivers include:
*   **Ruggedized Surfaces:** Use of carbon fiber textures for background depth and structural elements.
*   **Mechanical Precision:** UI elements should feel like machined components, featuring chamfered edges and subtle metallic gradients.
*   **Liquid Motion:** Micro-interactions employ "viscous" easing—smooth, slightly dampened transitions that mimic the movement of light through water.
*   **Water-Mode:** A dedicated mobile state optimized for low-visibility and high-stakes interaction, prioritizing high-contrast legibility and "glove-friendly" hit areas.

## Colors

The palette is optimized for underwater legibility and professional-grade instrumentation.

*   **Primary (Deep Teal):** Represents the abyss. Used for primary branding, key status indicators, and immersive backgrounds.
*   **Secondary (Crisp White):** High-contrast utility. Used for primary text and critical instrumentation readouts to ensure visibility in low light.
*   **Tertiary (Carbon Fiber Grey):** The structural base. Used for containers, cards, and backgrounds to provide a rugged, technical feel.
*   **Functional Accents:** A brighter "Sea-foam" teal (#00BFA5) is used for active states and "Oxygen" levels, while a high-visibility amber is reserved for decompression alerts and warnings.

**Water-Mode Override:** In Water-Mode, the UI shifts to maximum contrast. Backgrounds become pure pitch black to eliminate glow, and all interactive elements transition to Crisp White or high-intensity Teal.

## Typography

The typographic system prioritizes rapid data acquisition. 

*   **Headlines (Space Grotesk):** A technical sans-serif with geometric clarity. Headlines should feel like engravings on a watch bezel—sturdy and unmistakable.
*   **Body (Geist):** A clean, neutral typeface for documentation and technical descriptions, providing high legibility in dense layouts.
*   **Data & Labels (JetBrains Mono):** Monospaced fonts are used for all numerical data, depth readings, and timestamps. This ensures that changing digits do not cause layout shifts, maintaining a steady "instrument" feel.

In **Water-Mode**, increase all font weights by one tier and expand letter spacing on labels to prevent characters from blurring together in high-glare environments.

## Layout & Spacing

The layout is built on a 12-column fixed grid for desktop and a 4-column grid for mobile. The system uses an 8px rhythmic scale, though critical touch targets in **Water-Mode** utilize a 20px "Safety Margin" to prevent accidental triggers.

**Spacing Philosophy:**
*   **Dense Technical Views:** Standard mode uses tight spacing (8px/16px) to maximize the amount of data visible on a single screen, reminiscent of a complex chronograph dial.
*   **Water-Mode Layout:** Transition to a single-column, center-aligned layout. All interactive elements must have a minimum height of 64px to accommodate gloved interaction or high-motion environments.

## Elevation & Depth

Depth is used to simulate the layering of a watch face and the physical structure of diving gear.

*   **Base Layer:** Carbon Fiber Grey (#1A1A1A) with a subtle diagonal noise texture.
*   **Instrument Tier (Level 1):** Slightly elevated surfaces using a 1px inner stroke of Crisp White at 10% opacity to create a "milled" edge.
*   **Critical Readouts (Level 2):** These use "Glow-morphism." Elements appear to have an inner luminescence (Deep Teal glow), mimicking the phosphorescence of watch hands in the dark.
*   **No Shadows:** Avoid traditional ambient shadows. Instead, use "Inset Shadows" to make UI elements look like they are carved into the carbon fiber surface, reinforcing the industrial theme.

## Shapes

The shape language is "Precision-Softened Industrial." 

*   **Primary Radius:** A tight 4px (Soft) radius is applied to all buttons and containers to mimic machined metal. 
*   **Bezel Geometry:** Large containers or "modes" may use octagonal clipped corners to reference specialized diving watch cases.
*   **Interactive Targets:** Radio buttons and checkboxes use sharp squares with a 1px inset to maintain a professional, technical appearance.

## Components

### Buttons & Inputs
*   **Primary Button:** Deep Teal background with a 1px solid Crisp White border. Hover state triggers a "liquid fill" animation where the background color appears to rise like water.
*   **Water-Mode Button:** Full-width, 72px height, high-contrast (White background, Black text).
*   **Inputs:** Stepper-style inputs are preferred over free-text for technical data. Use large '+' and '-' increments that are easily tappable.

### Cards & Gauges
*   **Technical Cards:** Feature a "Header Bar" with monospaced metadata and a carbon fiber texture body.
*   **Analog Gauges:** Custom circular components that use the "Liquid" animation cues for needle movement—smooth, slightly elastic, and highly precise.

### Lists & Navigation
*   **Data Lists:** High-density rows with thin separators (1px, 5% White).
*   **Navigation:** Top-tier navigation uses a "Submarine Hatch" visual metaphor—iconography is encased in circular frames that glow when active.

### Feedback Systems
*   **Alerts:** Use a "Strobe" animation for critical warnings (Decompression, Low Air). The entire screen border pulses in high-visibility Amber.