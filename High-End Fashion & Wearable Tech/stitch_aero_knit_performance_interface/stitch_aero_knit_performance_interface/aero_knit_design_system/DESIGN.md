---
name: Aero-Knit Design System
colors:
  surface: '#111508'
  surface-dim: '#111508'
  surface-bright: '#373b2c'
  surface-container-lowest: '#0c0f04'
  surface-container-low: '#1a1d10'
  surface-container: '#1e2113'
  surface-container-high: '#282b1d'
  surface-container-highest: '#333627'
  on-surface: '#e2e4cf'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e2e4cf'
  inverse-on-surface: '#2f3223'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#abd600'
  primary: '#ffffff'
  on-primary: '#283500'
  primary-container: '#c3f400'
  on-primary-container: '#556d00'
  inverse-primary: '#506600'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c3f400'
  primary-fixed-dim: '#abd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#111508'
  on-background: '#e2e4cf'
  surface-variant: '#333627'
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
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-margin: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
This design system centers on the intersection of biological performance and textile engineering. The aesthetic is "Kinetic & Technical," evoking the feeling of a laboratory-grade interface used to monitor high-output physical activity. 

The brand personality is aggressive, precise, and futuristic. It avoids soft, organic shapes in favor of sharp lines and structural grids. The UI should feel like a "heads-up display" (HUD) for the body, emphasizing "Phase-Change" material properties through shifting gradients and thermal-inspired visuals. 

Key visual drivers include:
*   **Kinetic Motion:** Elements should feel like they are in a state of high-velocity transition.
*   **Technical Precision:** Data-heavy overlays, monospaced accents, and micro-interactions that mimic sensor readouts.
*   **Thermal Regulation:** Use of glowing accents to represent heat management and breathability.

## Colors
The palette is dominated by **Carbon Black (#101010)** to provide a deep, high-contrast foundation that allows technical data to pop. **Neon Mint (#CCFF00)** serves as the primary "kinetic" color, used for active states, vital data points, and glowing accents that represent energy flow. 

**Silver (#C0C0C0)** is utilized for structural elements, secondary labels, and to simulate the metallic sheen of smart-fiber components. 

**Thermal Visualization:** For "Phase-Change" and temperature regulation features, the system employs a supplemental thermal spectrum (Thermal Hot and Thermal Cold) to visualize heat distribution across the fabric or body. Use gradients sparingly to show material transitions.

## Typography
The typography strategy balances high-tech character with absolute legibility. 

*   **Headlines:** **Space Grotesk** provides a geometric, futuristic feel for large display text and section titles.
*   **Body:** **Inter** is the workhorse for all long-form descriptions and settings, ensuring clarity against dark backgrounds.
*   **Technical Data:** **JetBrains Mono** (or any high-quality monospaced font) must be used for all numerical data, sensor readouts, and "Phase-Change" status indicators to reinforce the technical narrative.
*   **Accents:** Use uppercase labels with increased letter-spacing to create a "technical blueprint" aesthetic.

## Layout & Spacing
The layout follows a **Rigid Technical Grid**. Use a 12-column system for desktop and a 4-column system for mobile. 

Spacing should be mathematical and consistent, based on a 4px baseline. Elements should feel "slotted" into the grid rather than floating freely. Use wide horizontal margins to create a focused, vertical central "core" for performance data, or utilize the full width for immersive thermal maps.

Incorporate **Technical Overlays**: Use thin (1px) Silver lines to subdivide sections, mimicking the look of blueprints or integrated circuits.

## Elevation & Depth
Elevation is achieved through **Glassmorphism** and **Luminescent Glow** rather than traditional shadows.

*   **Backdrop Blurs:** High-level containers (modals, floating cards) use a 20px blur with a 5% white tint and a 1px Silver border at 20% opacity.
*   **Luminous Depth:** Instead of shadows, use "Neon Mint" outer glows (0px blur, 4-8px spread, low opacity) to indicate that an element is active or powered on.
*   **Tonal Layering:** The background is #101010. Primary surfaces are #1A1A1A. This slight contrast creates a subtle sense of physical layers without breaking the dark-mode immersion.

## Shapes
The shape language is strictly **Sharp**. 

Rounded corners are avoided to maintain the aggressive, technical aesthetic of high-performance engineering. Every button, input field, and card should have 0px corner radii. 

For a "clipped" technical look, use 45-degree chamfered corners on primary call-to-action buttons or header containers. This reinforces the "Aero" narrative of aerodynamics and precision cutting.

## Components
This design system prioritizes components that visualize material science and performance data.

*   **Buttons:** Primary buttons are Neon Mint with black text. Use a 45-degree chamfer on the top-right corner. On hover, apply a high-intensity Neon Mint glow.
*   **Thermal Cards:** Glassmorphic containers used to display "Phase-Change" status. They should feature a background noise texture to simulate fabric weave.
*   **Input Fields:** Ghost-style inputs with a 1px Silver bottom border. The label sits above in JetBrains Mono. On focus, the bottom border turns Neon Mint.
*   **Status Chips:** Small, rectangular tags. If a material is "Active," the chip pulses with a Neon Mint glow.
*   **Thermal Toggle:** A specialized switch that transitions between "Heat Retention" (Orange glow) and "Ventilation" (Cyan glow) modes.
*   **Technical Overlays:** Crosshair elements at the corners of images or maps to simulate a viewfinder or scanning interface.
*   **Gauges:** Circular or linear "bio-feedback" bars that fill with Neon Mint as performance or heat intensity increases.