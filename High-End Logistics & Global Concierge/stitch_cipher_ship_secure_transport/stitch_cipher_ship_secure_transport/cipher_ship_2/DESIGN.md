---
name: Cipher-Ship
colors:
  surface: '#0a1420'
  surface-dim: '#0a1420'
  surface-bright: '#303a47'
  surface-container-lowest: '#050f1a'
  surface-container-low: '#121c28'
  surface-container: '#16202d'
  surface-container-high: '#212b37'
  surface-container-highest: '#2c3542'
  on-surface: '#d9e3f4'
  on-surface-variant: '#c5c6ca'
  inverse-surface: '#d9e3f4'
  inverse-on-surface: '#27313e'
  outline: '#8f9194'
  outline-variant: '#44474a'
  surface-tint: '#c4c7ca'
  primary: '#ffffff'
  on-primary: '#2d3134'
  primary-container: '#e0e2e6'
  on-primary-container: '#626568'
  inverse-primary: '#5c5f62'
  secondary: '#bdc2ff'
  on-secondary: '#1b247f'
  secondary-container: '#343d96'
  on-secondary-container: '#a8afff'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e2e6'
  primary-fixed-dim: '#c4c7ca'
  on-primary-fixed: '#191c1f'
  on-primary-fixed-variant: '#44474a'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bdc2ff'
  on-secondary-fixed: '#000767'
  on-secondary-fixed-variant: '#343d96'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#0a1420'
  on-background: '#d9e3f4'
  surface-variant: '#2c3542'
typography:
  display-secure:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-vault:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Geist
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: 0.15em
  data-point:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  grid_opacity: '0.05'
---

## Brand & Style

This design system embodies an industrial security aesthetic, prioritizing the visual language of high-fidelity vault systems and deep-space cargo manifests. The brand personality is disciplined, impenetrable, and technologically superior. It targets high-stakes environments where data integrity is paramount, evoking an emotional response of absolute safety and cold precision.

The design style is a hybrid of **Industrial Minimalism** and **Tactile Security**. It utilizes "Vault-Secure" metaphors through the use of metallic textures, hairline precision, and a heavy emphasis on structural integrity. Surfaces are not merely containers but armored plates, reinforced by subtle scanning grid patterns that suggest a continuous state of active monitoring and encryption.

## Colors

The palette is anchored in a high-contrast trinity: **Platinum Silver** for interactive elements and data, **Black** for the structural foundation, and **Deep Indigo** for active security states and primary accents.

- **Primary (Platinum Silver):** Used for maximum legibility of high-value data and primary icons. It should feel cold and metallic.
- **Secondary (Deep Indigo):** Reserved for "Active Encryption" states, primary action buttons, and focused borders.
- **Neutral (Slate/Iron):** Used for structural lines, grid patterns, and secondary metadata.
- **Background (Black/Void):** Pure `#000000` or deep `#0A0A0A` to ensure the "Vault" feel and maximize the contrast of scanning patterns.
- **Status Indicators:** Use hyper-saturated greens, reds, and ambers to mimic industrial LED hardware.

## Typography

This design system utilizes **Geist** exclusively to leverage its technical, developer-centric DNA. The typographic hierarchy is designed to mimic technical specifications and manifests.

- **Headlines:** Should be tight and impactful, often used in uppercase for section headers to denote "Sector" or "Vault" designations.
- **Body Text:** Maintains a comfortable reading rhythm but favors a slightly condensed feel to maximize information density on desktop.
- **Labels:** Always set in Uppercase with high letter-spacing to emulate stamped industrial serial numbers.
- **Numerical Data:** Should feel tabular and aligned, emphasizing the "Precise" nature of the system.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop, centered on a 12-column system. This creates a sense of "Constructed Architecture" rather than fluid movement. 

- **The Scanning Grid:** A persistent 24px background grid pattern is visible at 5% opacity. All components must snap to this grid.
- **Density:** Information density is high. Padding is used strategically to separate "Data Modules" rather than to create decorative whitespace.
- **Gutters:** 24px gutters ensure that even in dense data views, there is a clear "Structural Failure" line between modules.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Material Simulation** rather than traditional shadows.

- **Stacking:** Surfaces closer to the user are lighter (Graphite) than the base background (Black). 
- **Bevels:** Instead of drop shadows, use 1px inner highlights on the top and left edges of components to simulate a "Brushed Metal" bevel.
- **Active Scanning:** Use a semi-transparent Deep Indigo overlay with a horizontal "scanning line" (1px high-intensity line) for elements that are currently being processed or "unlocked."
- **Borders:** Use 1px solid borders in Platinum Silver (low opacity) for containers. Active elements gain a secondary 1px glow effect using the Indigo accent.

## Shapes

The shape language is strictly **Sharp (0px)**. Any degree of roundedness compromises the industrial, secure aesthetic of the system. 

- **Chipped Corners:** For primary call-to-action buttons, use a 45-degree "clipped corner" (dog-ear) on the top-right to suggest a technical schematic or a physical key-card.
- **Connectors:** Use 90-degree hair-lines to connect related data points, reinforcing the "Hardware Circuitry" metaphor.

## Components

- **Buttons:** Rectangular with 0px radius. Primary buttons use the clipped corner. State changes are indicated by a "shutter" animation (color filling from left to right) rather than a simple fade.
- **Status Indicators:** Small, circular LEDs. For "Secure" states, use a breathing glow effect in Deep Indigo. For "Breach" states, use a rapid flickering in Error Red.
- **Input Fields:** Styled as "Data Slots." No bottom border only; full 1px frames with a subtle Platinum Silver gradient. Labels are always positioned top-left in small-caps.
- **Cards/Modules:** Referred to as "Vaults." These feature a header bar with a specific serial number or ID. The background should have the subtle scanning grid pattern.
- **Scanning Progress:** Use a monospaced percentage counter accompanied by a thin, non-rounded progress bar that fills with a metallic texture.
- **Lists:** Data rows separated by 1px dotted lines. Hovering over a row should trigger a "Laser Sight" horizontal line that extends across the entire container.