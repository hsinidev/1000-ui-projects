---
name: Institutional-Future
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#424654'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#737785'
  outline-variant: '#c3c6d6'
  surface-tint: '#0056d2'
  primary: '#0040a1'
  on-primary: '#ffffff'
  primary-container: '#0056d2'
  on-primary-container: '#ccd8ff'
  inverse-primary: '#b2c5ff'
  secondary: '#516169'
  on-secondary: '#ffffff'
  secondary-container: '#d2e2ec'
  on-secondary-container: '#55656d'
  tertiary: '#444749'
  on-tertiary: '#ffffff'
  tertiary-container: '#5c5f60'
  on-tertiary-container: '#d7d9da'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001847'
  on-primary-fixed-variant: '#0040a1'
  secondary-fixed: '#d5e5ef'
  secondary-fixed-dim: '#b9c9d3'
  on-secondary-fixed: '#0e1d25'
  on-secondary-fixed-variant: '#3a4951'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c4c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#444748'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1280px
  density-compact: 4px
  density-comfortable: 16px
---

## Brand & Style
This design system establishes a visual language of "Institutional-Future," blending the unwavering stability of legacy financial institutions with the transparency and speed of decentralized governance. The aesthetic is rooted in the **Corporate / Modern** movement, prioritized for professional trust and high-stakes decision-making.

The brand personality is authoritative yet accessible. It evokes a sense of permanence and accountability, essential for users managing significant capital and protocol direction. The interface avoids "crypto-native" playfulness in favor of a rigorous, data-centric environment that feels like a modern central bank's command center.

## Colors
The palette is dominated by a high-contrast relationship between **White** and **Slate Grey (#2F3E46)** to define structural boundaries and hierarchy. **Royal Blue (#0056D2)** is utilized exclusively as the "Action and Trust" color—signifying primary interactions, active proposals, and verified states.

For data visualization and status indicators, the design system employs a secondary spectrum of muted semantic tones: emerald for "Passed," crimson for "Defeated," and amber for "Pending." Neutral greys are used to manage information density, ensuring that background elements recede while critical data points remain prominent.

## Typography
**Public Sans** is the sole typeface for this design system. Its origins in government and institutional design provide an immediate sense of officiality and neutrality. 

The typographic scale is optimized for reading long-form governance proposals and complex financial tables. Large displays use tighter letter-spacing and heavier weights to project authority, while labels utilize uppercase tracking to differentiate metadata from body content. Monospaced alternatives should be used strictly for wallet addresses and transaction hashes to ensure character-level clarity.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model to create a sense of grounded structure. A 12-column grid is centered within the viewport, with generous 40px outer margins to provide visual breathing room in a high-density information environment.

The spacing rhythm follows an 8px base unit. To facilitate complex governance activities, the layout favors vertical stacks for proposals and horizontal alignment for data comparison. Component padding is kept "compact" for data-heavy tables and "comfortable" for narrative-driven content like proposal descriptions.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. This maintains the "Institutional" aesthetic by making the UI feel constructed and architectural.

- **Level 0 (Base):** The primary background color (White).
- **Level 1 (Surface):** Subtle grey fills (#F8FAFB) used to group related content or define sidebar areas.
- **Level 2 (Plates):** White cards with a 1px border (#E2E8F0). This is the primary container for proposal content.
- **Level 3 (Interactive):** Only modals and dropdowns receive a soft, 10% opacity Slate Grey shadow to indicate temporary placement above the main workflow.

## Shapes
The shape language is disciplined and professional. **Soft (Level 1)** roundedness is applied consistently across the system. This 0.25rem (4px) radius softens the "Brutalist" edge of a sharp-cornered grid while remaining far more serious than the pill-shaped aesthetics common in consumer apps.

Buttons, input fields, and cards all share this uniform radius. The only exception is the "Status Tag," which may use a slightly larger radius (0.5rem) to distinguish it as a non-interactive label.

## Components
- **Buttons:** Primary buttons use a solid Royal Blue fill with white text. Secondary buttons use a Slate Grey outline. Tertiary actions use text-only with the Royal Blue color and 700 weight.
- **Proposals Cards:** These are the centerpiece. They must feature a 1px border, a clear "Status Badge" in the top-right, and a progress bar indicating quorum or vote distribution.
- **Data Tables:** High-density rows with 1px horizontal dividers. Alternating row colors are discouraged; use hover-states to highlight active rows instead.
- **Input Fields:** Minimalist design with a 1px Slate Grey border that thickens and turns Royal Blue on focus. Labels are always positioned above the field in the "label-bold" type style.
- **Voting Sliders:** Custom components that allow users to distribute voting power across multiple options, featuring clear numerical readouts and Royal Blue active tracks.
- **Governance Badges:** Small, high-contrast indicators for "Voted," "Multisig Signer," or "Proposer" to build social proof and trust within the platform.