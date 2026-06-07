---
name: Safe-Vault Cyber-Intelligence
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#36393e'
  surface-container-lowest: '#0b0f12'
  surface-container-low: '#181c20'
  surface-container: '#1c2024'
  surface-container-high: '#272a2e'
  surface-container-highest: '#323539'
  on-surface: '#e0e2e8'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e0e2e8'
  inverse-on-surface: '#2d3135'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#050505'
  on-primary-container: '#797777'
  inverse-primary: '#5f5e5e'
  secondary: '#dfb7ff'
  on-secondary: '#4b007e'
  secondary-container: '#9d05ff'
  on-secondary-container: '#f7e6ff'
  tertiary: '#c7c6ca'
  on-tertiary: '#2f3033'
  tertiary-container: '#040507'
  on-tertiary-container: '#77777b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#f1daff'
  secondary-fixed-dim: '#dfb7ff'
  on-secondary-fixed: '#2d004f'
  on-secondary-fixed-variant: '#6b00b0'
  tertiary-fixed: '#e3e2e6'
  tertiary-fixed-dim: '#c7c6ca'
  on-tertiary-fixed: '#1a1b1e'
  on-tertiary-fixed-variant: '#46474a'
  background: '#101417'
  on-background: '#e0e2e8'
  surface-variant: '#323539'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
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
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is engineered to evoke the sensation of a high-security digital fortress. It leverages a "Safe-Vault" aesthetic that prioritizes visual density, structural integrity, and cutting-edge sophistication. The brand personality is authoritative and impenetrable, yet highly advanced.

The style combines **Glassmorphism** with **Minimalism**. UI elements appear as layered panes of reinforced synthetic glass floating over a void of deep blacks. This transparency conveys a sense of "X-ray" visibility into complex data while maintaining the premium feel of a high-tech command center. High-contrast neon accents provide the necessary "active" signals against the dark, muted backdrop, simulating a tactical heads-up display (HUD).

## Colors

The palette is strictly dark to minimize eye strain and emphasize the "void" of secure data environments. 

- **Primary (Obsidian Black):** Used for the base canvas to create infinite depth.
- **Secondary (Neon Violet):** Used sparingly for critical calls to action, active states, and data visualizations. It serves as the "pulse" of the system.
- **Tertiary (Carbon Gray):** Used for container backgrounds and structural partitioning.
- **Neutral (Steel):** Used for secondary text and subtle borders to ensure legibility without breaking the dark aesthetic.

Gradients should be used only for glass highlights—specifically, linear gradients from top-left to bottom-right with low-opacity white to represent light catching the edge of a glass pane.

## Typography

This design system utilizes a dual-font strategy to balance human readability with technical precision.

- **Space Grotesk** is the primary typeface for headlines and all technical data. Its geometric construction feels engineered and futuristic. Use uppercase transformations for labels and small metadata to mimic terminal outputs.
- **Inter** is the workhorse for body copy and general UI elements. It provides a clean, neutral balance to the more aggressive headlines, ensuring that long-form security reports remain legible.

Technical readouts, IP addresses, and hash strings must always use the `data-mono` or `label-caps` styles to distinguish machine-generated information from human-authored content.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop, ensuring the "Vault" feels stable and centered. A 12-column grid is standard, with generous margins to frame the content like a monitor within a monitor.

Spacing follows a strict 4px baseline rhythm. Information density should be high but organized; use `stack-lg` to separate major functional blocks and `stack-sm` for related data points. Containers should utilize internal padding of at least 24px to maintain the premium, spacious feel of a high-end dashboard.

## Elevation & Depth

Depth is the cornerstone of this design system, achieved through **Glassmorphism** rather than traditional drop shadows.

- **Surface 1 (Base):** Pure `#050505`.
- **Surface 2 (Glass Panes):** A semi-transparent fill (`rgba(26, 27, 30, 0.6)`) with a `backdrop-filter: blur(20px)`. This creates the frosted glass effect.
- **Surface 3 (Hover/Active):** Increase the transparency and add a subtle 1px inner border of Neon Violet at 30% opacity.

Instead of ambient shadows, use **Glows**. Critical elements should have a soft, violet outer-glow (`box-shadow: 0 0 15px rgba(157, 0, 255, 0.3)`) to simulate light emission from a high-tech interface.

## Shapes

The shape language is "Soft-Industrial." Elements use a consistent `0.25rem` (4px) corner radius. This prevents the UI from looking dated (sharp corners) or too consumer-friendly (large rounds).

The goal is to suggest precision-milled components. Buttons and input fields should maintain this subtle roundness. Larger cards or "Vault containers" may increase this to `0.5rem` to frame content more effectively, but never beyond that. Icons should follow a 2px stroke weight with slight corner rounds to match the UI.

## Components

- **Buttons:** Primary buttons are solid Neon Violet with white text. Secondary buttons are "Ghost" style—transparent with a 1px border and a subtle glass blur.
- **Input Fields:** Dark backgrounds with a bottom-only border are preferred. Upon focus, the border glows Neon Violet and a faint violet pulse ripples through the glass background.
- **Cards/Vaults:** Must include a subtle 1px border (`rgba(255, 255, 255, 0.1)`) and the standard backdrop blur. The header of a card should be separated by a thin horizontal rule.
- **Chips/Status Indicators:** Use "Pulse" icons for active monitoring. A "Secure" status is a hollow violet circle, while a "Threat" status uses a solid high-contrast red.
- **Data Tables:** High-density, no vertical borders. Use alternating row highlights with 2% opacity white to maintain the glass feel.
- **Terminal Component:** A specific block for code or logs using `data-mono` typography, with a slightly darker, non-transparent background to denote a "protected" execution environment.