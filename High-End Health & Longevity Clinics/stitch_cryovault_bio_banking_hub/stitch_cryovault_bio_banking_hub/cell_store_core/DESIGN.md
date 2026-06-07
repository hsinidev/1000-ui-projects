---
name: Cell-Store Core
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
  background: '#0c1609'
  on-background: '#dae6d0'
  surface-variant: '#2d3828'
typography:
  display-lg:
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
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
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
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is engineered to evoke an atmosphere of clinical precision, high-stakes security, and futuristic biological preservation. It represents the intersection of biotechnology and digital vaulting. The aesthetic is "Hardened Science"—a synthesis of architectural minimalism and high-tech utility. 

The visual narrative focuses on the concept of the "digital cryo-chamber." This is achieved through a high-contrast interface where the void of space meets the vitality of cellular life. Users should feel they are interacting with a sophisticated laboratory terminal that is both impenetrable and state-of-the-art. The emotional response is one of absolute trust, driven by data transparency and an uncompromising "zero-error" visual language.

## Colors

The palette for this design system is intentionally restrictive to maintain a "heads-up display" (HUD) feel. 

- **Deep Space Black (#050505):** Used as the universal canvas. It creates a sense of infinite depth and focuses all attention on the luminous data points.
- **Neon Green (#39FF14):** The "Life-Sign" accent. It is used exclusively for primary actions, active status indicators (e.g., "Cryo-Stable"), and critical data highlights. It should be used sparingly to maintain its high-impact signaling power.
- **Crisp White (#FFFFFF):** Used for maximum legibility of technical data, labels, and primary body text.
- **Surface Neutrals:** Shades of dark gray (#121212, #1A1A1A) are used for "glass" panel backgrounds and structural strokes to provide depth without breaking the dark-mode immersion.

## Typography

This design system utilizes a dual-font strategy to balance human-centric readability with machine-like precision.

**Inter** serves as the primary typeface for all structural headings and body descriptions. Its neutral, clean architecture ensures that complex medical terminology remains highly legible.

**JetBrains Mono** is utilized for "Machine Layers"—serial numbers, timestamps, cryo-temperatures, and status badges. By using a monospaced font for data-heavy elements, the design system reinforces the feeling of a real-time scientific terminal where every character occupies a precise coordinate.

## Layout & Spacing

The layout philosophy is based on a **Strict Grid System** that mimics technical schematics. 

- **Grid:** A 12-column fluid grid is used for the main dashboard, with fixed 24px gutters.
- **Rhythm:** An 8px linear scale governs all internal component spacing, ensuring vertical alignment across data columns.
- **Density:** The design system prioritizes a high-information density. Margins are kept tight (32px) to allow more room for real-time monitoring feeds.
- **Notification-Driven Layouts:** Sidebars are reserved for "Live Feeds" of bio-vault activity, using a vertical stack that pulses when new telemetry is received.

## Elevation & Depth

In this design system, depth is not conveyed through shadows, but through **Glassmorphism and Stroke Layering.**

1.  **Backdrop Blurs:** High-fidelity glass panels use a 20px blur with a 10% white opacity fill. This creates a "frosted lens" effect over the Deep Space Black background.
2.  **Hardened Borders:** All containers are defined by sharp, 2px solid strokes. Primary containers use #1A1A1A, while active or "scanning" containers use #39FF14.
3.  **Luminous Stacking:** When an element is focused, it does not lift; instead, it gains a subtle inner glow (Neon Green) to simulate a back-lit terminal screen. 
4.  **Scanning Animations:** A subtle, horizontal light sweep (linear gradient) periodically moves from top to bottom across data-heavy cards to indicate an "active monitoring" state.

## Shapes

The shape language is strictly **Rectilinear (Sharp)**. 

To maintain the "Hardened" scientific aesthetic, the border radius for all UI elements—including buttons, cards, and input fields—is set to **0px**. This sharp-edged approach communicates industrial strength and digital precision. 

The only exception to this rule is the use of circular "Cell" icons or biological visualizations, which serve as organic counterpoints to the rigid, geometric container system.

## Components

- **Buttons:** 2px solid strokes with no rounded corners. The primary button is a solid #39FF14 block with black text. Secondary buttons are ghost buttons with a white 2px stroke.
- **Cryo-Status Badges:** Small, monospaced labels encased in a 1px frame. When "Active," the frame pulses with a neon green glow.
- **Input Fields:** Bottom-border only or full-framed with a 2px stroke. Focus state triggers a vertical "scanning" pulse on the left border.
- **Data Visualizations:** High-contrast line graphs using #39FF14. Use "glitch" transitions for loading states where data points assemble into the grid.
- **Notification Feeds:** Stacked cards with a "Hardened" left-border accent. New notifications enter the screen with a subtle scan-line flicker.
- **Glass Cards:** Used for secondary information, featuring high-fidelity background blurs and white text to separate metadata from primary "Life-Sign" data.