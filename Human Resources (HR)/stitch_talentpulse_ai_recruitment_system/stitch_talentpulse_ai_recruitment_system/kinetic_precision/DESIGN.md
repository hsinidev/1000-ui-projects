---
name: Kinetic Precision
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#47464f'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#787680'
  outline-variant: '#c8c5d0'
  surface-tint: '#5b598c'
  primary: '#070235'
  on-primary: '#ffffff'
  primary-container: '#1e1b4b'
  on-primary-container: '#8683ba'
  inverse-primary: '#c4c1fb'
  secondary: '#006d36'
  on-secondary: '#ffffff'
  secondary-container: '#6dfe9c'
  on-secondary-container: '#007439'
  tertiary: '#02003c'
  on-tertiary: '#ffffff'
  tertiary-container: '#09007e'
  on-tertiary-container: '#767aff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c4c1fb'
  on-primary-fixed: '#181445'
  on-primary-fixed-variant: '#444173'
  secondary-fixed: '#6dfe9c'
  secondary-fixed-dim: '#4de082'
  on-secondary-fixed: '#00210c'
  on-secondary-fixed-variant: '#005227'
  tertiary-fixed: '#e1e0ff'
  tertiary-fixed-dim: '#c0c1ff'
  on-tertiary-fixed: '#07006c'
  on-tertiary-fixed-variant: '#2f2ebe'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 32px
  gutter: 16px
---

## Brand & Style

This design system is engineered for the intersection of human capital and artificial intelligence. The aesthetic direction is **Modern Tech**, characterized by high-performance clarity and a sophisticated "intelligence layer." It prioritizes speed and cognitive efficiency for recruiters managing high volumes of data.

The visual style blends **Minimalism** with selective **Glassmorphism**. By using a deep, authoritative foundation of indigo and punctuating it with vibrant mint green, the interface feels both institutional and cutting-edge. The emotional response is one of "calm control"—the user should feel empowered by the AI's precision rather than overwhelmed by its complexity.

## Colors

The palette is anchored by **Deep Indigo (#1E1B4B)**, which provides the structural weight necessary for a professional ATS. This is contrasted against a clean **White (#FFFFFF)** workspace to ensure maximum legibility. **Mint Green (#4ADE80)** serves as the "action" color, representing growth, success, and AI-validated matches. 

A specialized "Shield-Blue" (#6366F1) is used as a tertiary accent to distinguish security and privacy features, such as the Bias-Shield, from standard operational actions. Surfaces utilize varying levels of transparency to maintain a sense of depth and layering without sacrificing performance.

## Typography

The typography system uses a dual-font approach to balance personality with utility. **Space Grotesk** is used for headings and key data points, providing a technical, geometric edge that reinforces the AI-driven nature of the product. **Inter** is utilized for all body copy, forms, and high-density lists to ensure maximum readability and a neutral, professional tone.

Letter spacing is slightly tightened on headings to maintain a modern "impact" look, while smaller labels utilize increased tracking for clarity in high-density data environments.

## Layout & Spacing

This design system employs a **12-column fluid grid** with a tight 8px base unit. The philosophy is "density without clutter." By utilizing 16px gutters, we allow for substantial data visualization while maintaining distinct visual groupings.

Margins are generous at the edges (32px) to frame the application, but internal spacing between related data elements is kept tight (4px to 8px) to minimize eye travel. Vertical rhythm is strictly enforced to ensure that complex dashboards feel organized and intentional.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional heavy shadows. Surfaces use a `backdrop-filter: blur(12px)` to create a layered, modern tech stack feel. 

- **Level 1 (Base):** Solid White or Neutral Gray backgrounds.
- **Level 2 (Cards):** Glass surfaces with a 70% white opacity and a 1px semi-transparent white border. This creates a "frosted" effect that feels light and premium.
- **Level 3 (Modals/Popovers):** Deeper backdrop blurs (24px) with a very subtle Deep Indigo-tinted shadow (0 10px 30px rgba(30, 27, 75, 0.08)) to indicate priority.

## Shapes

The shape language is precise and professional. A **Soft (0.25rem)** border radius is the standard for primary UI elements like input fields and buttons, maintaining a crisp, geometric aesthetic. 

Larger containers and glass cards use a slightly increased radius (0.75rem) to feel more approachable and modern. Circular "pill" shapes are reserved exclusively for status badges and the Bias-Shield toggle to make them instantly recognizable as interactive, non-structural elements.

## Components

### Glass Cards
Cards are the primary container. They must feature a `1px` border of `rgba(255, 255, 255, 0.4)` and a background of `rgba(255, 255, 255, 0.7)` with a background blur. This ensures that even in high-density views, the interface feels airy and sophisticated.

### Bias-Shield Toggle
A signature component. The 'Bias-Shield' toggle uses the **Shield-Blue (#6366F1)** for its 'On' state track. When active, the toggle thumb features a tiny Mint Green dot or a subtle shield icon. The track should have a soft outer glow (`box-shadow: 0 0 8px rgba(99, 102, 241, 0.4)`) to visually signal that an "Active Protection" layer is running over the data.

### Buttons & Chips
- **Primary Button:** Deep Indigo with White text. High contrast, sharp, and authoritative.
- **Success Action:** Mint Green with Deep Indigo text for maximum energy and visibility.
- **Status Chips:** Pill-shaped with low-opacity backgrounds (10%) and high-opacity text of the same color.

### Input Fields
Inputs use a "Flat-Tech" style: 1px Deep Indigo borders at 10% opacity, which transition to a 2px Mint Green border on focus. Typography within inputs should be `body-sm` for space efficiency.

### AI-Match Indicator
A specialized component—a circular progress ring using Mint Green, placed next to candidate names to show the AI's confidence score. It should utilize the same glassmorphism principles when appearing in expanded views.