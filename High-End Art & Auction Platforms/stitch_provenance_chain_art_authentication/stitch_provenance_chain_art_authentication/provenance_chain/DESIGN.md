---
name: Provenance-Chain
colors:
  surface: '#0c1609'
  surface-dim: '#0c1609'
  surface-bright: '#323c2d'
  surface-container-lowest: '#071105'
  surface-container-low: '#141e11'
  surface-container: '#182214'
  surface-container-high: '#222d1e'
  surface-container-highest: '#2d3828'
  on-surface: '#dae6d0'
  on-surface-variant: '#baccb0'
  inverse-surface: '#dae6d0'
  inverse-on-surface: '#293324'
  outline: '#85967c'
  outline-variant: '#3c4b35'
  surface-tint: '#2ae500'
  primary: '#efffe3'
  on-primary: '#053900'
  primary-container: '#39ff14'
  on-primary-container: '#107100'
  inverse-primary: '#106e00'
  secondary: '#c9c6c5'
  on-secondary: '#313030'
  secondary-container: '#474646'
  on-secondary-container: '#b7b4b4'
  tertiary: '#f9fafa'
  on-tertiary: '#2f3131'
  tertiary-container: '#dddddd'
  on-tertiary-container: '#606162'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#79ff5b'
  primary-fixed-dim: '#2ae500'
  on-primary-fixed: '#022100'
  on-primary-fixed-variant: '#095300'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c9c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0c1609'
  on-background: '#dae6d0'
  surface-variant: '#2d3828'
typography:
  display-xl:
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
    lineHeight: '1.6'
    letterSpacing: '0'
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  grid_pattern_size: 40px
---

## Brand & Style
The design system embodies a high-fidelity, tech-forward aesthetic tailored for the intersection of fine art and blockchain security. It evokes an atmosphere of absolute precision, elite digital custody, and immutable verification. 

The visual style is a hybrid of **Glassmorphism** and **Technical Minimalism**. It utilizes translucent surfaces to create depth against a void-like background, while "Tech-Brutalism" influences the sharp, unrelenting borders and visible structural grids. The emotional response is one of entering a secure, high-end digital vault where technology serves as the ultimate arbiter of truth.

## Colors
The palette is rooted in a high-contrast, "terminal-luxe" scheme. 

- **Deep Space Black (#050505):** The foundation of the system, providing a sense of infinite depth and focus.
- **Neon Green (#39FF14):** Used exclusively for high-priority actions, active states, and successful authentication pulses. It represents the "pulse" of the blockchain.
- **Crisp White (#FFFFFF):** Reserved for high-contrast typography and iconography to ensure maximum legibility against the dark void.
- **Glow States:** Primary elements utilize a `0px 0px 15px rgba(57, 255, 20, 0.4)` outer glow to simulate light emission from a high-tech console.

## Typography
Typography in this design system emphasizes clarity and technical rigor. 

**Inter** provides the structural backbone for user-facing information, selected for its neutral, modern appearance and exceptional readability at all sizes. **JetBrains Mono** is introduced for all data-heavy, technical, or metadata-driven content, such as transaction hashes, certificate IDs, and system labels. This dual-font strategy separates "narrative" content from "technical" data, reinforcing the service's blockchain identity.

## Layout & Spacing
The layout relies on a **12-column fixed grid** with an underlying visual "Technical Grid." This background pattern consists of subtle, low-opacity lines (`rgba(255, 255, 255, 0.03)`) at 40px intervals, serving as a blueprint for component alignment.

Spacing follows a strict 4px baseline. Margins are generous to maintain a sense of gallery-like luxury, while technical data tables may use tighter densities to convey information efficiency.

## Elevation & Depth
In this design system, depth is achieved through **translucency** rather than traditional shadows. 

- **Surface Tiers:** Backgrounds use a tiered system of black shades. Floating containers use a glassmorphism effect: a semi-transparent fill (`rgba(10, 10, 10, 0.7)`) combined with a heavy `20px` backdrop blur.
- **Technical Borders:** Instead of soft shadows, elevation is defined by sharp 1px borders. Active surfaces use the Neon Green for borders, while resting surfaces use a subtle grey-scale border (`rgba(255, 255, 255, 0.1)`).
- **Light Source:** A virtual "top-down" light source creates subtle 1px highlights on the top edges of glass panels.

## Shapes
The design system utilizes **zero roundedness** to maintain a sharp, technical, and architectural feel. Every button, input field, and card features hard 90-degree angles. 

To prevent the UI from feeling dated, these sharp corners are paired with hairline borders and neon light effects. Occasional "chamfered" corners (45-degree cuts) may be used for specialized technical components like "Safe-Seal" badges or biometric scanner frames to enhance the futuristic hardware aesthetic.

## Components
- **Buttons:** Primary buttons feature a solid Neon Green fill with black text. Secondary buttons are "Ghost" style with a 1px white border. All buttons exhibit a subtle outer glow on hover.
- **Safe-Seal Badges:** Interactive verification badges. They use a CSS linear gradient to simulate a metallic/holographic sheen that shifts based on mouse movement, signifying authenticity.
- **Scanning Overlays:** Full-screen or container-based technical overlays featuring a horizontal "laser" line (Neon Green) that constantly oscillates, paired with flickering data points in JetBrains Mono.
- **Input Fields:** Bottom-border only fields to maintain a minimal look. On focus, the bottom border glows Neon Green and displays a small "READY" label in the top-right corner.
- **Biometric Login:** A centralized square frame with corner-only borders ("bracket" style). Inside, a thin-line fingerprint or iris-scan SVG pulses with a 10% opacity Neon Green fill during the authentication process.
- **Cards:** Glassmorphic containers with visible 1px borders and a small "serial number" in the bottom-left corner of every card to mimic physical art provenance records.