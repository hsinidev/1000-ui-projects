---
name: Meta-Couture
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#050505'
  on-primary-container: '#797777'
  inverse-primary: '#5f5e5e'
  secondary: '#d3fbff'
  on-secondary: '#00363a'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#ffabf3'
  on-tertiary: '#5b005b'
  tertiary-container: '#100010'
  on-tertiary-container: '#d300d3'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#ffd7f5'
  tertiary-fixed-dim: '#ffabf3'
  on-tertiary-fixed: '#380038'
  on-tertiary-fixed-variant: '#810081'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Syne
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: 0.1em
  headline-md:
    fontFamily: Syne
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-base:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  ui-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-glow:
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
  container-margin: 20px
  gutter: 12px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system embodies the intersection of high-fashion editorial aesthetics and hyper-futuristic digital environments. It is built for a mobile-first, high-performance audience that views digital garments as artifacts of status. 

The visual style is defined by **Glassmorphism** and **High-Contrast Digital Noir**. Surfaces appear as suspended sheets of obsidian or frosted crystal, catching "light" from vibrant iridescent sources. The experience should feel like navigating a premium, dark-mode terminal for a luxury atelier. Interaction is tactile and luminous, using glow-states and motion to signal premium quality.

## Colors

The palette is anchored in **Obsidian Black (#050505)** to provide a void-like depth, allowing digital garments to stand out. Iridescent accents (Cyan, Magenta, and Violet) are used sparingly for interactive triggers, status indicators, and "Glow-Intensity" highlights. 

Glassmorphism is achieved through a combination of low-opacity neutral fills and high-contrast iridescent borders. Backgrounds should utilize heavy Gaussian blurs (30px+) behind semi-transparent layers to maintain legibility while preserving the immersive, multi-layered feel of the metaverse.

## Typography

This design system utilizes a tiered typographic approach to balance editorial flair with technical precision. 

- **Headings:** Use **Syne** with wide tracking and uppercase transformations to evoke a "runway" feel.
- **Body:** Use **Plus Jakarta Sans** for high legibility on mobile screens, ensuring a contemporary and soft contrast to the sharp display type.
- **UI Elements/Data:** Use **JetBrains Mono** for all functional labels, prices, and technical specs (e.g., poly-count, rarity level). This reinforces the "digital-only" nature of the brand.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for high-end mobile devices. Use a 4-column mobile grid with generous vertical "stack" spacing to allow the imagery to breathe. 

Whitespace is treated as "negative space in the void." Avoid clutter by using the `stack-lg` spacing between major content sections. Margins are kept tight (20px) to maximize the visual impact of full-bleed iridescence and glass layers.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** and **Luminous Outlines** rather than traditional drop shadows.

- **Level 0 (Base):** Deep Charcoal (#050505) solid background.
- **Level 1 (Cards):** Semi-transparent neutral (#1A1A1A at 60% opacity) with a `backdrop-filter: blur(20px)` and a 1px iridescent stroke.
- **Level 2 (Modals/Popovers):** Higher transparency (#1A1A1A at 40% opacity) with a more intense `backdrop-filter: blur(40px)` and a vibrant glowing border.
- **Interaction:** Active elements should trigger an outer "Bloom" effect (diffused neon glow) rather than a shadow, simulating light emission from a screen.

## Shapes

The shape language is **Soft (0.25rem/4px)**, leaning toward sharp, architectural precision. Large radius curves are avoided to maintain the "Avant-Garde" edge. 

Interactive elements like buttons use the base `rounded-sm`, while larger glass containers may use `rounded-lg` (8px) to subtly differentiate the "environment" from the "tools." Interactive sliders and toggle tracks remain strictly sharp or minimally rounded.

## Components

- **Glow-Intensity Sliders:** Horizontal tracks with a 1px solid iridescent line. The thumb is a high-contrast white or iridescent circle that leaves a faint "light trail" as it moves.
- **Action Buttons:** Ghost-style buttons with 1px iridescent borders. On hover/tap, they fill with a vibrant gradient and trigger a 10px outer bloom. Text is always `ui-mono`.
- **Fashion Cards:** Full-bleed image containers with a glass overlay at the bottom. Labels are docked in the corners using `label-glow` typography.
- **Status Chips:** High-contrast capsules with no background and 1px borders. Use `ui-mono` for rarity indicators (e.g., "LEGENDARY", "1 OF 1").
- **Inputs:** Minimalist bottom-border only fields. When focused, the border transforms into a cyan-to-magenta gradient.
- **Haptic Feedback:** All primary interactions should be accompanied by short, sharp haptic pulses to mimic the feeling of interacting with high-end machinery.