---
name: Industrial Precision
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#303031'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  headline-xl:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-technical:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.02em
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
  grid-line-weight: 1px
---

## Brand & Style

This design system is built on the principles of **Tactical Luxury**. It merges the raw, uncompromising durability of armored engineering with the refined precision of high-end vehicle management. The aesthetic is heavily influenced by **Technical Brutalism**—utilizing visible structural grids, blueprint-inspired overlays, and high-contrast interfaces that prioritize data density and immediate legibility.

The atmosphere should evoke the feeling of a mission-critical command center. Surfaces are dark and non-reflective, mimicking matte carbon fiber and treated steel, while interactive elements carry a metallic sheen or a high-visibility alert status. Every design decision must communicate security, weight, and mechanical excellence.

## Colors

The palette is strictly functional, utilizing a high-contrast triad to define hierarchy and urgency.

*   **Matte Black (#1A1A1A / #0D0D0D):** The primary environment color. It provides a deep, non-distracting background that emphasizes "stealth" and premium quality.
*   **Chrome / Silver (#E0E0E0):** Used for primary text, iconography, and structural borders. It represents the "armor" and technical components.
*   **Racing Red (#FF0000):** A high-intensity accent reserved for critical data, active states, and security alerts. It must be used sparingly to maintain its psychological impact.

Gradient use is limited to subtle metallic "brushed" effects on headers or primary containers to simulate physical hardware.

## Typography

The typographic system utilizes three distinct typefaces to separate intent:

1.  **Geist:** Used for headlines and primary UI headers. It provides a sharp, modern, and technical foundation.
2.  **Inter:** Used for long-form body text and descriptions. Its neutrality ensures readability against high-contrast backgrounds.
3.  **JetBrains Mono:** Reserved for data readouts, technical labels, coordinates, and status indicators. The monospaced nature reinforces the blueprint/industrial aesthetic.

All labels and technical data should favor uppercase styling to enhance the "industrial documentation" feel.

## Layout & Spacing

This design system employs a **Rigid Technical Grid**. The layout philosophy is built on a 12-column system where the grid lines are often visually represented as subtle 1px borders or "blueprint" crosshairs.

*   **Rhythm:** A 4px baseline grid ensures all elements align with mechanical precision.
*   **Padding:** Generous internal padding within cards (24px or 32px) prevents the industrial aesthetic from feeling cluttered.
*   **The "Technical Underlay":** Backgrounds should feature a repeating 40px grid pattern in a low-opacity gray (#262626) to simulate drafting paper. Elements should "snap" to these lines visually.

## Elevation & Depth

In this design system, depth is achieved through **Structural Layering** rather than traditional shadows.

*   **Tonal Stacking:** Higher-level elements (modals, active cards) use a slightly lighter shade of black/gray (#262626) to pull forward.
*   **Beveled Edges:** Use 1px internal strokes (top and left) in #FFFFFF at 10% opacity to create a "machined" beveled edge.
*   **Metallic Textures:** Use subtle linear gradients (45 degrees) on buttons and active headers to simulate brushed aluminum or matte steel.
*   **Glassmorphism:** Reserved exclusively for "HUD" (Heads-Up Display) elements that overlay vehicle maps or camera feeds. Use a heavy backdrop blur (20px) with a Chrome (#E0E0E0) 1px border.

## Shapes

The shape language is **Strictly Orthogonal**. 

*   **Sharp Corners:** All primary buttons, cards, and containers must have 0px roundedness. This reinforces the "armored" and "rugged" nature of the hardware.
*   **Chamfered Accents:** For secondary elements like chips or status badges, use a 45-degree clipped corner (chamfer) instead of a radius to mimic heavy machinery parts.
*   **Strokes:** Use consistent 1px or 2px "Technical Borders." Interactive elements should feel like they were milled from a single block of material.

## Components

### Buttons
Primary buttons are solid Racing Red (#FF0000) with black text. Secondary buttons are outlined in Chrome (#E0E0E0) with a 1px border. Hover states should include a "scanning" line animation or a slight metallic glint.

### Input Fields
Inputs should look like data entry terminals. Use a Matte Black background with a 1px Silver border. On focus, the border turns Racing Red, and a subtle "Technical Drawing" crosshair appears in the corners of the field.

### Status Chips
Chips represent vehicle health and security status. They should use the monospaced font and include a small "LED" dot indicator that pulses when the status is "Active" or "Warning."

### Cards
Cards are the primary organizational unit. Each card should feature a "Header Bar" with a metallic gradient and a "Serial Number" (a unique identifier in monospaced font) in the top-right corner to simulate industrial parts labeling.

### Data Visualization
Charts and graphs should mimic oscilloscopes or diagnostic readouts. Use thin lines, no fills (unless low-opacity Red), and sharp vertices. Avoid rounded line caps.

### Innovative Components
*   **The "Armory Toggle":** A heavy-duty switch for critical system overrides, requiring a "long-press" or "slide-to-unlock" interaction.
*   **System Coordinates:** A persistent HUD element in the corner of screens showing "System Uptime" and "Lat/Long" in JetBrains Mono.