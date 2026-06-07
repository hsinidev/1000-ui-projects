---
name: Command-Wall Design System
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
  on-surface-variant: '#c5c6d2'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e909c'
  outline-variant: '#444650'
  surface-tint: '#b3c5ff'
  primary: '#b3c5ff'
  on-primary: '#0d2c6e'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#435b9f'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#282828'
  on-tertiary-container: '#918f8f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Montserrat
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for executive-level presence and mission-critical communication. The brand personality is authoritative, precise, and uncompromising, mirroring the high-stakes environments of corporate boardrooms and strategic command centers. 

The aesthetic leverages a **Modern Executive** style—a fusion of structured Bento-box layouts and sophisticated glassmorphism. It prioritizes clarity and status through high-contrast interfaces that feel both grounded and technologically advanced. Visual interest is generated through subtle radial gradients that mimic high-end lighting, while "glass" panels provide a sense of layered depth without sacrificing the "Graphite" foundation's solidity.

## Colors

The palette is strictly professional, utilizing a "Dark Mode by Default" strategy to reduce eye strain during long-form video sessions and to emphasize the "Sleek" aesthetic.

- **Graphite (#1C1C1C):** The primary canvas color. It provides a deep, non-distracting background that allows video feeds and data to pop.
- **Royal Blue (#002366):** Used for primary actions, focus states, and authoritative branding elements. It signals trust and stability.
- **Silver (#C0C0C0):** Employed for secondary text, iconography, and subtle borders. It provides the "high-end metal" feel.
- **Interactive States:** High-contrast vibrance is achieved by shifting Royal Blue toward a more luminous #0047D4 for active/hover states to ensure no ambiguity in user intent.

## Typography

This design system utilizes a high-contrast typographic pairing to balance modern utility with executive weight. 

**Montserrat** is reserved for headlines and display elements. Its geometric construction conveys confidence and architectural strength. Use tight letter-spacing for large display sizes to maintain a "locked-in" professional look.

**Inter** serves as the workhorse for body copy and data visualization. Its exceptional legibility ensures that participants, names, and technical metadata remain clear even at smaller sizes. For data points (e.g., bitrates, participant counts), use the "data-mono" style to ensure alignment and numerical clarity.

## Layout & Spacing

The layout philosophy follows a **Bento-box grid** model—a series of modular, rectangular containers that organize complex information into digestible, high-contrast visual blocks.

- **Grid System:** A 12-column fluid grid. Elements should snap to containers.
- **Bento Modules:** Use varying aspect ratios (1:1, 2:1, 1:2) to house video feeds, chat, and data visualizations.
- **Rhythm:** An 8px base unit drives all padding and margins. Larger gaps (24px+) are used between major functional modules to maintain an "executive" feel of openness and organization.
- **Visual Hierarchy:** Primary video content should occupy the largest Bento-box, with secondary data and controls clustered in smaller, peripheral modules.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** and **Tonal Layering** rather than traditional drop shadows.

1.  **Base Layer:** Solid Graphite (#1C1C1C).
2.  **Middle Layer (Bento Cards):** A darker, slightly elevated neutral (#2A2A2A) with a thin 1px Silver (#C0C0C0) border at 10% opacity.
3.  **Floating Layer (Glassmorphism):** Used for overlays, control bars, and modals. These use a background blur (20px - 40px) and a semi-transparent surface (White at 5% opacity).
4.  **Interactive Depth:** On hover, cards should increase in border brightness (Silver at 40% opacity) and display a subtle, deep-blue glow (#002366 at 20% spread) to simulate "active power."

## Shapes

To maintain an "Authoritative and Sleek" look, the design system employs a **Soft** roundedness level. Sharp corners feel too aggressive for a premium product, while fully rounded corners feel too consumer-grade.

- **Standard Containers:** 4px (0.25rem) radius for a precise, "machined" appearance.
- **Large Bento Modules:** 8px (0.5rem) radius to define major layout areas.
- **Buttons & Pills:** 4px radius, maintaining the consistent geometric language.
- **Video Feeds:** Keep strictly at 4px radius to maximize screen real estate and mimic high-end hardware monitors.

## Components

- **Buttons:** Primary buttons use solid Royal Blue with white text. Secondary buttons are "Ghost" style with Silver borders and no fill. High-contrast hover states are mandatory.
- **Bento Cards:** The foundational container. Must include a subtle inner glow on the top edge to simulate overhead lighting.
- **Glass Control Bar:** A bottom-anchored floating bar with a 40px background blur. Icons are Silver, turning Royal Blue when active.
- **Data Visualizations:** Charts must use high-contrast strokes. Use Royal Blue for positive trends and a stark Silver for baselines.
- **Input Fields:** Darker than the background (#121212) with a 1px Silver bottom-border that transforms into a Royal Blue border on focus.
- **Participant Chips:** Small, dark-grey translucent pills with a Silver "active" indicator for the current speaker.
- **Status Indicators:** Use "Live" pulsing animations for active streams, utilizing a high-brightness version of Royal Blue.