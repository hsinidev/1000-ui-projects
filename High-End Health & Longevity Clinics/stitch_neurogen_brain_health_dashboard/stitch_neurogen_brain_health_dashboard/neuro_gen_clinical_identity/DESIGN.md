---
name: Neuro-Gen Clinical Identity
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1c1b1d'
  surface-container: '#201f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e5e1e4'
  on-surface-variant: '#b9caca'
  inverse-surface: '#e5e1e4'
  inverse-on-surface: '#313032'
  outline: '#849495'
  outline-variant: '#3a494a'
  surface-tint: '#00dce5'
  primary: '#e9feff'
  on-primary: '#003739'
  primary-container: '#00f5ff'
  on-primary-container: '#006c71'
  inverse-primary: '#00696e'
  secondary: '#dab9ff'
  on-secondary: '#470083'
  secondary-container: '#8f03ff'
  on-secondary-container: '#f0ddff'
  tertiary: '#fff8fe'
  on-tertiary: '#38294d'
  tertiary-container: '#e9d6ff'
  on-tertiary-container: '#6b5a81'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#63f7ff'
  primary-fixed-dim: '#00dce5'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#efdbff'
  secondary-fixed-dim: '#dab9ff'
  on-secondary-fixed: '#2b0053'
  on-secondary-fixed-variant: '#6500b8'
  tertiary-fixed: '#eddcff'
  tertiary-fixed-dim: '#d3beeb'
  on-tertiary-fixed: '#231437'
  on-tertiary-fixed-variant: '#4f4065'
  background: '#131315'
  on-background: '#e5e1e4'
  surface-variant: '#353437'
typography:
  display-lg:
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
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: JetBrains Mono
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
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

This design system establishes a **Cyber-Biological** aesthetic, merging the cold precision of advanced computing with the organic fluidity of human neurology. The brand personality is authoritative, cutting-edge, and elite, aimed at a demographic that values high-science and life-extending technologies. 

The visual style is a hybrid of **Glassmorphism** and **High-Contrast Data Visualization**. It utilizes deep, immersive backgrounds to represent the "inner space" of the mind and genome, contrasted by vibrant, luminous interactive elements that represent clinical intervention. The emotional response should be one of profound trust in technology and awe at the biological potential.

## Colors

The palette is anchored in a dark-mode-only environment to ensure maximum contrast for medical data and luminous accents. 

- **Base Layers:** Use `Deep Charcoal (#0A0A0C)` for global backgrounds. `Midnight Purple (#1A0B2E)` is reserved for large container fills and gradient transitions to add depth.
- **Action & Data:** `Glass-Cyan (#00F5FF)` is the primary interaction color, used for CTA buttons, active states, and primary neural pathways.
- **Secondary Accents:** `Electric Violet (#8F00FF)` denotes secondary genomic data, rare findings, and sophisticated medical insights.
- **Surface:** Surfaces are defined by semi-transparent layers (10-40% opacity) that allow "Neural-Path" background patterns to bleed through.

## Typography

The typography system balances futuristic character with clinical legibility. 

- **Headlines:** `Space Grotesk` provides a geometric, technical feel that suggests innovation without sacrificing readability.
- **Body:** `Inter` is used for all medical summaries and patient descriptions, ensuring high comprehension during critical data review.
- **Technical Data:** `JetBrains Mono` is used for genomic sequences, coordinates, and raw neurological output, providing a monospaced "lab-grade" precision to technical readouts.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model within a 1440px max-width container, transitioning to a fluid model for smaller viewports. 

- **Grid:** A 12-column grid with 24px gutters. Elements should align strictly to the grid to maintain a "calculated" clinical appearance.
- **Rhythm:** An 8px base unit drives all padding and margin decisions. 
- **Density:** Medical dashboards should utilize tighter vertical spacing (16px - 24px) to allow for high-density data viewing, while marketing and brand pages should increase spacing (64px+) to create a premium, "breathable" feel.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and light-based layering rather than traditional drop shadows.

- **The Z-Axis:** Higher elevation is represented by increased background blur (from 10px to 40px) and lighter border-opacities.
- **Luminous Borders:** Use 1px internal borders with a 20% opacity Cyan or White stroke to define the edges of "glass" containers.
- **Glows:** Primary interactive elements should cast a soft `Glass-Cyan` outer glow (blur: 15px, spread: -5px) to simulate a light-emitting interface.
- **Background Patterning:** Place "Neural-Path" SVG patterns on a layer between the base background and the glass surfaces to create parallax effects during scroll.

## Shapes

The shape language is **Soft (0.25rem)**, emphasizing precision. 

While the biological elements (brain models, neural paths) are organic and fluid, the UI containers that hold them are strictly geometric. This creates a "specimen under glass" effect. Avoid full circles for buttons; use slightly rounded rectangles to maintain the technical, scientific aesthetic. Larger containers (cards) may use `rounded-lg` (0.5rem) to soften the overall interface.

## Components

- **Buttons:** Primary buttons feature a solid `Glass-Cyan` fill with `Deep Charcoal` text. Secondary buttons use a transparent background with a 1px `Glass-Cyan` border and glowing hover states.
- **Glass Cards:** The foundational container. Must feature `backdrop-filter: blur(20px)` and a thin semi-transparent Cyan border. 
- **Data Chips:** Small, pill-shaped indicators for genomic markers. Use `Electric Violet` for positive findings and `Glass-Cyan` for neutral/reference data.
- **Neural Inputs:** Text fields should have a dark, recessed appearance with a bottom-only Cyan border that pulses when focused.
- **3D Viewports:** Dedicated containers for brain models. These should have no background fill, only a subtle vignette to focus the eye on the 3D asset.
- **Data Visualizations:** High-contrast line charts using `Glass-Cyan` for active trends and `Electric Violet` for historical benchmarks. Avoid fills; use glowing paths.