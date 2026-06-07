---
name: Biological Asset Management Interface
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#baccb0'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#85967c'
  outline-variant: '#3c4b35'
  surface-tint: '#2ae500'
  primary: '#efffe3'
  on-primary: '#053900'
  primary-container: '#39ff14'
  on-primary-container: '#107100'
  inverse-primary: '#106e00'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#fdf9f9'
  on-tertiary: '#313030'
  tertiary-container: '#e0dddc'
  on-tertiary-container: '#626161'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#79ff5b'
  primary-fixed-dim: '#2ae500'
  on-primary-fixed: '#022100'
  on-primary-fixed-variant: '#095300'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.2em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 16px
  margin: 32px
---

## Brand & Style

This design system is engineered to evoke a sense of absolute security and clinical precision. The brand personality is immutable, expert, and ultra-high-tech, mirroring the sensitive nature of private bio-banking. It targets high-net-worth individuals and medical professionals who require an interface that feels less like a consumer app and more like a hardened laboratory terminal.

The aesthetic follows a **High-Contrast / Bold** direction with elements of **Brutalism**. It prioritizes structural integrity over decorative softness. Visuals are grounded in a "Dark Room" medical environment, using extreme contrast to direct focus toward critical biological data. The user should feel that their assets are being monitored by a system that is both vigilant and technologically superior.

## Colors

The palette is restricted to a triad of functional tones to maintain high-security legibility.

*   **Deep Space Black (#000000):** The primary canvas. It eliminates distractions and establishes the foundation for medical-grade focus.
*   **Neon Green (#39FF14):** Used exclusively for "Active" states, successful bio-auth, and critical data points. It represents vitality and system health.
*   **Crisp White (#FFFFFF):** The primary typographic and structural color. It provides the "Clinical" feel against the black void.
*   **System Gray (#1A1A1A):** Used for subtle container definitions where absolute black borders would be too harsh for information hierarchy.

All interactive elements must maintain a minimum 7:1 contrast ratio to ensure accessibility in high-pressure medical environments.

## Typography

Typography is used as a tool for differentiation between "Interface" and "Data."

*   **Inter** serves as the UI anchor. It is utilized for all navigation, instructions, and headlines. It provides a modern, neutral clarity that suggests institutional reliability.
*   **JetBrains Mono** is reserved for all variable biological data, specimen IDs, timestamps, and security codes. Its monospaced nature emphasizes the technical, calculated aspect of the service, making data feel "scanned" and precise.

All headers should be set in sentence case to maintain a professional, matter-of-fact tone. Avoid italics; use weight changes for emphasis to maintain the "Hardened" aesthetic.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to mimic high-tech instrumentation panels. Layouts are constructed on a strict 12-column grid with no gutters between primary layout blocks, creating a "modular hull" feel.

Spacing is calculated in multiples of 4px. Internal component padding should be tight (8px to 16px) to maximize information density, while the "Margin" (32px+) is used to isolate the central "Safe Area" of the interface from the browser or screen edges. All elements should be snapped to the grid to maintain the architectural rigidity of the design.

## Elevation & Depth

Depth in this design system is not conveyed through shadows, which are considered too "organic" and soft for this application. Instead, it uses **Tonal Layers** and **Bold Borders**.

*   **Level 0 (Floor):** Pure Black (#000000).
*   **Level 1 (Panels):** Defined by 1px solid White (#FFFFFF) or Gray (#1A1A1A) borders.
*   **Scanning Overlays:** A semi-transparent green (#39FF14 at 5% opacity) gradient that moves vertically to indicate active data processing.
*   **Active State:** Elements in focus gain a 2px Neon Green border and a subtle "outer glow" (the only exception to the no-shadow rule) to simulate a backlit LED monitor.

Hierarchy is strictly 2D; if an element is "above" another, it simply occludes it with a solid black fill and a sharp white border.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. 

Every button, input field, card, and modal must utilize 90-degree corners. This "Hardened" approach reinforces the feeling of structural security and medical precision. It rejects the friendly, consumer-grade trend of rounded corners in favor of a specialized, industrial aesthetic. 

Small decorative "corner snips" or 45-degree chamfers may be used on primary containers to further the "military-grade hardware" metaphor.

## Components

### Buttons
Buttons are strictly rectangular.
*   **Primary:** Solid Neon Green background with Black text (JetBrains Mono).
*   **Secondary:** Ghost style with 1px White border and White text.
*   **Action:** On hover, primary buttons should invert or trigger a rapid "flicker" animation.

### Input Fields
Inputs are defined by a bottom-only 2px White border. When focused, the border turns Neon Green and a "Scanning" line pulses through the field background. Label text must be in JetBrains Mono at a small scale above the input.

### Cards & Containers
Cards do not use background fills that differ from the page background. They are defined solely by their 1px White or Gray borders. Each card should feature a small "Specimen ID" or "Serial Number" in the top-right corner in monospaced type.

### UI Animation: The "Scanner"
All loading states and data transitions must use a horizontal or vertical "scanning line" effect. This is a 1px Neon Green line that sweeps across the component, signaling that the system is actively verifying or analyzing biological data.

### Additional Components
*   **Security Badge:** A persistent, 1px bordered box in the corner of the UI displaying the current "Encryption Status" and "System Pulse" in monospaced data.
*   **Bio-Status Indicator:** A specialized progress bar that uses segmented blocks rather than a smooth fill, representing cellular integrity levels.