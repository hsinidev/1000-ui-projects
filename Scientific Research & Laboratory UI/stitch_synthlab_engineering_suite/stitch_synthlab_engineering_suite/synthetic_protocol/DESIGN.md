---
name: Synthetic Protocol
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
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#f8fafc'
  on-tertiary: '#2d3133'
  tertiary-container: '#dcdee0'
  on-tertiary-container: '#5f6264'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#79ff5b'
  primary-fixed-dim: '#2ae500'
  on-primary-fixed: '#022100'
  on-primary-fixed-variant: '#095300'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#0c1609'
  on-background: '#dae6d0'
  surface-variant: '#2d3828'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
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
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin-mobile: 20px
---

## Brand & Style

This design system embodies the persona of a sophisticated high-tech lab assistant—intelligent, precise, and anticipatory. It is designed for scientists and engineers who require high-density information without the cognitive load of traditional lab software. The aesthetic direction is a fusion of **Glassmorphism** and **Minimalism**, set against a deep technical backdrop. 

The user experience should feel like peering through a high-powered digital microscope: layers are translucent, data points are crisp, and interactions feel "liquid" and responsive. The goal is to evoke a sense of controlled experimentation and cutting-edge reliability, specifically optimized for mobile-first rapid decision-making in high-pressure laboratory environments.

## Colors

The palette is anchored in a deep **Slate** hierarchy to minimize eye strain during long-form data analysis. 
- **Primary (Neon Green):** Reserved exclusively for active states, successful protein sequences, and high-priority action triggers. 
- **Secondary (Slate Dark):** Used for the primary canvas and structural background elements.
- **Tertiary (White/Light Slate):** Utilized for "clean surfaces"—translucent card overlays that house critical data points.
- **Accent (Cyan/Teal):** Used for secondary data streams and differentiating between synthetic vs. natural biological markers.

Color application must be sparse; the dark background should dominate, allowing the Neon Green to "pop" as a functional beacon for the user's attention.

## Typography

This design system utilizes a dual-font strategy to separate interface navigation from scientific data. 
- **Space Grotesk** is used for headlines and all technical data strings (sequences, molecular weights, timestamps). Its geometric construction reinforces the "high-tech" lab aesthetic.
- **Inter** is used for body copy and instructional text, ensuring maximum readability on mobile screens where space is at a premium.

Numerical data should always utilize the monospaced qualities of Space Grotesk to ensure vertical alignment in tables and sequence comparisons.

## Layout & Spacing

The layout follows a **fluid grid** model optimized for mobile-first interaction. We employ an 8px rhythmic system, but break down to 4px increments for high-density data visualizations. 

On mobile devices, a single-column layout is standard for protein lists, while a 2-column "card" layout is used for summary metrics. Significant horizontal padding (20px) is maintained on the outer edges to ensure "thumb-friendly" interaction areas, while internal card gutters are kept tight (16px) to maximize the display of complex molecular data.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and tonal stacking rather than traditional shadows. 
- **Level 0 (Base):** Deep Slate (#0F172A).
- **Level 1 (Surface):** Lightened Slate (#1E293B) with a subtle 1px border.
- **Level 2 (Glass):** Semi-transparent white (5-10% opacity) with a `backdrop-blur` of 12px. This is used for floating action menus and high-priority modals.
- **Level 3 (Neon Glow):** Reserved for active elements. Instead of a shadow, use a subtle outer glow using the primary Neon Green color to simulate light emission from a screen or microscope.

## Shapes

The shape language is **Soft (0.25rem)**. This choice balances the precision of scientific equipment with the modern "liquid" feel of the interface. 
- Standard UI components (Inputs, Buttons) use a 4px radius.
- Interactive cards use a 8px (rounded-lg) radius to distinguish them from background containers.
- Data markers and protein sequence nodes may use full pill-shapes (rounded-full) to signify they are draggable or modular units.

## Components

- **Buttons:** Primary buttons are solid Slate with a Neon Green border and text. On hover/active, they fill with a subtle Neon Green glow.
- **Chips:** Used for biological tags (e.g., "Enzyme", "Ligand"). These use a monospaced font, no background fill, and a 1px border in a secondary accent color.
- **Protein Sequence Cards:** These are the core component. They feature a glassmorphic background, a neon-green "health" or "stability" indicator bar at the bottom, and monospaced technical specs.
- **Input Fields:** Dark, recessed backgrounds with a Neon Green bottom-border that glows when focused.
- **Liquid Transitions:** Between views, use "staggered fade-in" animations where data points appear to flow into position, mimicking a biological fluid motion.
- **Decision Toggles:** High-contrast binary switches (Green/Slate) designed for rapid thumb-taps in the field.