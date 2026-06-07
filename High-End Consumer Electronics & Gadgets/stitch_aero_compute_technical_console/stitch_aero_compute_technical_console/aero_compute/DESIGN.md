---
name: Aero-Compute
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1c1c1c'
  on-primary-container: '#858484'
  inverse-primary: '#5f5e5e'
  secondary: '#c7c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#2ae500'
  on-tertiary: '#053900'
  tertiary-container: '#022200'
  on-tertiary-container: '#199900'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#79ff5b'
  tertiary-fixed-dim: '#2ae500'
  on-tertiary-fixed: '#022100'
  on-tertiary-fixed-variant: '#095300'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-md:
    fontFamily: metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-lg:
    fontFamily: jetbrainsMono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  data-sm:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.2'
  label-caps:
    fontFamily: jetbrainsMono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 16px
  margin-desktop: 48px
  margin-mobile: 16px
  grid-line: 1px
---

## Brand & Style

This design system embodies the ethos of high-performance hardware engineering. The brand personality is authoritative, cold, and uncompromisingly precise. It targets elite professionals—engineers, data scientists, and digital architects—who view their workstation as a high-caliber instrument rather than a consumer appliance.

The visual style is a hybrid of **Industrial Brutalism** and **Tactile Mechanical-Tech**. It rejects the soft, organic trends of modern SaaS in favor of hard edges, visible structural components, and a "form follows function" utility. The interface should feel like a digital twin of a physical server rack or a cockpit instrument panel. Every pixel serves a structural purpose, evoking an emotional response of absolute reliability and military-grade power.

## Colors

The palette is strictly functional, utilizing high-contrast transitions to signal hierarchy.

*   **Primary (Graphite):** The foundation. Used for deep backgrounds to minimize eye strain during long-form technical work.
*   **Secondary (Brushed Steel):** Used for structural elements, borders, and disabled states. It mimics the physical chassis of the workstation.
*   **Tertiary (Neon Mint):** The "Active" state. Reserved exclusively for critical data points, primary calls to action, and live telemetry. It must be used sparingly to maintain its impact.
*   **Neutral (Carbon):** Used for surface elevation and container backgrounds to differentiate layers from the primary base.

## Typography

The typographic system bifurcates between **Instructional UI** and **Technical Data**.

**Industrial Sans-Serif (Metropolis):** Chosen for its geometric purity and architectural stability. It handles all structural labeling, navigation, and marketing copy. Headlines should be set with tight tracking to feel dense and "heavy."

**Monospaced (JetBrains Mono):** Reserved for technical specifications, performance metrics, and code. This font signifies "raw data" and should always be used when displaying CPU temperatures, clock speeds, or SKU identifiers.

All labels should be treated as engineering annotations—small, often all-caps, and highly legible.

## Layout & Spacing

This design system employs a **Strict Engineering Grid**. Unlike fluid layouts that prioritize white space, this layout prioritizes density and alignment.

*   **Visible Grid:** Backgrounds should feature a subtle 1px grid (Graphite-Light) at 32px increments, mimicking a technical blueprint.
*   **The 4px Rule:** All spacing between elements must be a multiple of 4px.
*   **Column Structure:** A 12-column grid on desktop with 16px gutters. Elements should be "boxed in" by visible borders rather than floating.
*   **Responsive Reflow:** On mobile, the 12-column grid collapses to a 4-column stack. Heavy data tables should switch to a horizontal scroll or a simplified "Key: Value" list format to maintain precision.

## Elevation & Depth

Depth is conveyed through **Physical Materiality** rather than light and shadow.

1.  **Structural Layering:** No soft shadows are permitted. Elevation is achieved by changing the background hex from Graphite (#1C1C1C) to Carbon (#2A2A2A) and adding a 1px "Brushed Steel" border.
2.  **Inset States:** Buttons and input fields should appear "machined" into the interface using subtle inner shadows or darkened top-left borders.
3.  **Textures:** Use a CSS noise filter or a micro-pattern SVG to simulate brushed metal on secondary surfaces and carbon fiber on primary cards.
4.  **Glassmorphism (Restricted):** Use only for tactical overlays or "Heads-Up Display" (HUD) elements, with a heavy blur (20px+) and a Neon Mint tint.

## Shapes

The shape language is strictly **Angular**. 

*   **0px Radius:** All buttons, cards, and containers must have square corners. This reinforces the industrial, military-grade aesthetic.
*   **Chiseled Accents:** Use 45-degree "clipped corners" for decorative elements or primary action buttons to evoke the look of specialized hardware components.
*   **Stroke Weight:** Use a consistent 1px or 2px stroke for all borders. Never use "soft" or "faded" edges.

## Components

**Buttons:**
*   **Primary:** Solid Neon Mint background with black text (#000000). 0px corner radius.
*   **Secondary:** Ghost style with 1px Brushed Steel border. Text in Steel.
*   **Active State:** Add a "glow" (outer neon mint shadow) to simulate a powered LED.

**Data Displays (Telemetry):**
*   Use JetBrains Mono for all numbers. 
*   Incorporate small "Bar Graphs" or "Sparklines" in Neon Mint to show performance trends.
*   Label every data point with an uppercase sub-label (e.g., "CORE_TEMP_01").

**Inputs:**
*   Input fields must look like terminal command lines. 
*   The cursor should be a solid Neon Mint block.
*   Borders turn Neon Mint when focused.

**Cards:**
*   Include a "Serial Number" or "Reference ID" in the top right corner of every card to enhance the industrial feel.
*   Use visible "screws" (small circular icons in the corners) for high-level container components.

**Navigation:**
*   Vertical sidebar navigation, resembling a rack-mount system. 
*   Active links are marked with a vertical Neon Mint bar on the left edge.