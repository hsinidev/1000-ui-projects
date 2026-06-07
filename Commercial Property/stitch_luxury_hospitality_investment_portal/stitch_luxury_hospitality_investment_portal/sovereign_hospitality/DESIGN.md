---
name: Sovereign Hospitality
colors:
  surface: '#0a1420'
  surface-dim: '#0a1420'
  surface-bright: '#303a47'
  surface-container-lowest: '#050f1b'
  surface-container-low: '#121c28'
  surface-container: '#17202d'
  surface-container-high: '#212b37'
  surface-container-highest: '#2c3543'
  on-surface: '#d9e3f4'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#d9e3f4'
  inverse-on-surface: '#27313e'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#e9c176'
  on-secondary: '#412d00'
  secondary-container: '#604403'
  on-secondary-container: '#dab36a'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#1d1f1f'
  on-tertiary-container: '#858687'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0a1420'
  on-background: '#d9e3f4'
  surface-variant: '#2c3543'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  title-sm:
    fontFamily: notoSerif
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: inter
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
  container-padding: 24px
  gutter: 16px
  section-gap: 48px
  element-gap: 12px
---

## Brand & Style

The design system is engineered to evoke an atmosphere of "Quiet Luxury"—an aesthetic that prioritizes heritage, precision, and exclusivity. The target audience consists of ultra-high-net-worth investors and institutional resort brokers who demand institutional-grade reliability presented through a bespoke, high-end editorial lens.

The visual style is a hybrid of **Minimalism** and **Tactile Sophistication**. It leverages vast amounts of negative space to signify premium value, while using subtle textures and high-precision borders to ground the digital experience in physical reality. The interface must feel less like a software tool and more like a private concierge desk: authoritative, hushed, and meticulously organized.

## Colors

This design system utilizes a "Midnight & Gold" palette to establish an immediate sense of prestige. 

- **Primary Background:** Deep Navy (#001F3F) serves as the canvas, providing a stable, institutional foundation that reduces eye strain during deep financial analysis.
- **Accents:** Gold (#C5A059) is used sparingly for primary actions, critical data highlights, and brand flourishes. It should never overwhelm the layout.
- **Secondary Surfaces:** A light Marble (#F8F9FA) is utilized for specific modal overlays or secondary sections to provide a high-contrast break from the navy, suggesting the architectural materiality of luxury lobbies.
- **Semantic Colors:** Success and warning states should be muted (e.g., Sage Greens and Burnt Ochre) to ensure they do not clash with the primary gold accent.

## Typography

The typographic hierarchy relies on the tension between the classicism of **Noto Serif** and the industrial precision of **Inter**.

- **Headings:** Use Noto Serif for all editorial content, property names, and section headers. This establishes a "journal-style" authority.
- **Body & Data:** Inter is used for all functional text. For financial figures, use a slightly tighter tracking and medium-to-bold weights to ensure legibility on mobile devices.
- **Labels:** Small-cap Inter is the standard for micro-copy, status indicators, and metadata labels to maintain an organized, ledger-like appearance.

## Layout & Spacing

This design system follows a **Fluid Grid** with a mobile-first philosophy. On mobile, margins are set to a generous 24px to prevent the UI from feeling cramped. 

- **Rhythm:** An 8px linear scale is used for structural spacing, while a 4px scale is reserved for tight internal component alignment.
- **Whitespace:** Use "excessive" whitespace between major sections to signify luxury. No two primary modules should feel crowded.
- **Mobile Alignment:** All financial tables must support horizontal scrolling with the first column (Property/Asset name) pinned to the left to ensure context is never lost.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Ambient Shadows** rather than heavy color blocking.

- **The Base:** The Deep Navy background is the lowest level.
- **Surface Elevation:** Cards and containers use a slightly lighter navy tint with a 1px "Gold Dust" border (opacity 15%) to define edges without adding visual weight.
- **Shadows:** Use extremely soft, long-range shadows (Blur: 30px, Opacity: 20%, Color: Black) to make property cards appear to float slightly above the marble or navy surfaces.
- **Glassmorphism:** Use a subtle backdrop blur on top-level navigation bars to allow property imagery to peak through as the user scrolls.

## Shapes

The shape language of the design system is disciplined and architectural. 

- **Corners:** A "Soft" approach (4px-8px radius) is applied to all buttons and cards. This provides enough modernization to feel current while maintaining the sharp professional edge required for a brokerage platform.
- **Refined Borders:** All containers should feature a 0.5px or 1px stroke. Avoid thick borders which can appear "cheap" or "cartoonish."
- **Interactive Elements:** Buttons should maintain a consistent height (minimum 48px for mobile) to ensure ease of use for the high-level executive user.

## Components

- **Primary Buttons:** Solid Gold (#C5A059) with white or navy text. On hover/active, the gold should deepen slightly. No gradients.
- **Property Cards:** Feature high-resolution photography with a subtle vignette. Data overlays (Price, Yield, Location) should use Inter for maximum clarity.
- **Input Fields:** Minimalist design with only a bottom border that illuminates Gold when focused. Placeholder text should be a muted slate blue.
- **Financial Tickers:** A specialized component for scrolling market data or currency conversions, styled with monospaced-adjacent Inter for high readability.
- **Progressive Disclosure:** Use elegant accordions for detailed asset disclosures to keep the initial view uncluttered.
- **Chips/Badges:** Use "Outlined" styles for status (e.g., "Under Contract") to keep the UI light.