---
name: LumenCity Digital Identity
colors:
  surface: '#0f1030'
  surface-dim: '#0f1030'
  surface-bright: '#353658'
  surface-container-lowest: '#090a2a'
  surface-container-low: '#171838'
  surface-container: '#1b1c3c'
  surface-container-high: '#262748'
  surface-container-highest: '#303253'
  on-surface: '#e1e0ff'
  on-surface-variant: '#c8c5cf'
  inverse-surface: '#e1e0ff'
  inverse-on-surface: '#2c2d4e'
  outline: '#918f99'
  outline-variant: '#47464e'
  surface-tint: '#c2c2f2'
  primary: '#c2c2f2'
  on-primary: '#2b2d53'
  primary-container: '#1a1b41'
  on-primary-container: '#8283af'
  inverse-primary: '#5a5b84'
  secondary: '#ffd086'
  on-secondary: '#432c00'
  secondary-container: '#f8ad00'
  on-secondary-container: '#664500'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#1e2020'
  on-tertiary-container: '#868788'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c2c2f2'
  on-primary-fixed: '#16173d'
  on-primary-fixed-variant: '#42436b'
  secondary-fixed: '#ffdead'
  secondary-fixed-dim: '#ffba3b'
  on-secondary-fixed: '#281900'
  on-secondary-fixed-variant: '#604100'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0f1030'
  on-background: '#e1e0ff'
  surface-variant: '#303253'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is engineered to evoke a sense of nocturnal safety, urban intelligence, and high-performance utility. It targets municipal stakeholders and tech-savvy citizens who value both infrastructure reliability and cutting-edge connectivity. 

The visual style is **Atmospheric Modernism**, blending elements of **Glassmorphism** with a high-tech utility aesthetic. The interface should feel like a premium command center—dark, focused, and luminous. By utilizing deep indigo as a structural base and amber as a functional highlight, the design system mimics the experience of a city street at night, where light signifies activity, safety, and connection. Interactive elements leverage soft-glow effects to simulate physical light sources, creating a tactile "electric" feel.

## Colors

The palette is anchored by **Deep Indigo**, used for primary backgrounds and structural surfaces to minimize light pollution and eye strain during "Night" mode. **Amber Glow** serves as the primary accent color, reserved for critical information, active states, and interactive triggers, mirroring the warmth of modern street lighting. **Crisp White** is used sparingly for high-priority typography and icons to ensure maximum contrast.

In "Night" mode, surfaces use varying shades of indigo to create depth. In "Day" mode, the Deep Indigo transitions to a clean neutral slate, while Amber Glow remains the focal point for connectivity indicators. All interactive states must incorporate a secondary glow effect using the specified RGBA variables to maintain the atmospheric theme.

## Typography

This design system utilizes **Space Grotesk** for headlines and data visualizations to reinforce a technical, futuristic edge. Its geometric terminals pair perfectly with the "Smart City" narrative. For utility, body text, and complex data tables, **Inter** is employed for its exceptional legibility and neutral character, ensuring that dense technical information remains accessible.

Weight is used to establish hierarchy: use SemiBold or Bold for headers to create a strong anchor against the dark background, and Regular for body content to maintain breathability. The `data-mono` style is specifically intended for coordinate readouts, Wi-Fi speeds, and sensor ID tags.

## Layout & Spacing

The design system employs a **Fluid Grid** model with a 12-column structure for desktop and a 4-column structure for mobile. A strict 8px spacing rhythm ensures alignment across all dashboard components. 

Layouts should favor wide margins to prevent the interface from feeling cramped. Content is organized into modular "nodes" (cards), which should be separated by standard `lg` (24px) gutters. In technical views, use `md` (16px) padding inside containers to maximize data density while maintaining clear visual grouping.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Tonal Layering**. Surfaces do not use traditional drop shadows; instead, they utilize backdrop blurs (12px to 20px) and semi-transparent indigo fills.

1.  **Base Layer:** Solid Deep Indigo (#1A1B41).
2.  **Surface Layer:** 60% opacity Indigo with a 1px inner border (10% White) to define edges.
3.  **Active Layer:** Elements that are "On" or "Selected" receive a dual-layered `box-shadow`: a tight 4px amber glow and a diffused 15px amber bloom.
4.  **Overlay Layer:** Modals and tooltips use a darker, 80% opaque indigo with a more pronounced backdrop blur to isolate the user's focus.

## Shapes

The shape language is disciplined and professional. **Soft (0.25rem)** roundedness is the standard for most functional UI elements like input fields and buttons, providing a modern feel without losing the "industrial" precision of city infrastructure. 

Larger containers and cards use `rounded-lg` (0.5rem) to soften the overall dashboard. Interactive "status" pips and iconography circles are the only elements permitted to be fully rounded (pill-shaped) to distinguish them from structural components.

## Components

**Buttons:** 
Primary buttons feature a solid Amber Glow background with black or deep indigo text. They must include a `transition` effect that intensifies the amber box-shadow glow on hover. Secondary buttons are "ghost" style with a 1px indigo-light border.

**Cards:** 
Cards are the primary container for streetlight data. They use a semi-transparent background blur. When a streetlight is "active" or "selected," the card's border changes to Amber Glow.

**Chips:** 
Used for Wi-Fi status (e.g., "High Traffic," "Offline"). These use a small, 8px circular indicator next to the text. The indicator pulses slightly for live data streams.

**Input Fields:** 
Dark-themed inputs with a subtle 1px border. On focus, the border transitions to Amber Glow with a soft external bloom.

**Data Visualizations:** 
Charts should use gradients that transition from Deep Indigo to Amber Glow. Avoid multi-color rainbows; use opacity and shades of amber to represent different data intensities.

**Additional Components:** 
*   **Connectivity Gauge:** A circular or radial progress bar showing Wi-Fi signal strength using the glowing amber effect.
*   **Map Markers:** Custom icons representing streetlights with a radial "light cast" effect on the map surface.