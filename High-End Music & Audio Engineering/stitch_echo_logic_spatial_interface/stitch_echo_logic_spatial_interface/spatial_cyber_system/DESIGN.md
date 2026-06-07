---
name: Spatial-Cyber System
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#b9caca'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#849495'
  outline-variant: '#3a494a'
  surface-tint: '#00dce5'
  primary: '#e9feff'
  on-primary: '#003739'
  primary-container: '#00f5ff'
  on-primary-container: '#006c71'
  inverse-primary: '#00696e'
  secondary: '#fface8'
  on-secondary: '#5e0053'
  secondary-container: '#ff24e4'
  on-secondary-container: '#520049'
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
  secondary-fixed: '#ffd7f0'
  secondary-fixed-dim: '#fface8'
  on-secondary-fixed: '#3a0033'
  on-secondary-fixed-variant: '#840076'
  tertiary-fixed: '#eddcff'
  tertiary-fixed-dim: '#d3beeb'
  on-tertiary-fixed: '#231437'
  on-tertiary-fixed-variant: '#4f4065'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  technical-mono:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 40px
---

## Brand & Style

The design system is engineered for the high-precision world of spatial audio engineering within VR/AR environments. It evokes an atmosphere of immersive technicality, blending the boundless depth of space with the sharp clarity of cybernetic interfaces. The brand personality is authoritative, innovative, and hyper-focused on data accuracy.

The visual style is a hybrid of **Glassmorphism** and **High-Contrast Futuristic** aesthetics. It utilizes multi-layered translucency to mimic HUD (Heads-Up Display) elements, creating a sense of physical depth in a 3D environment. This approach allows users to maintain spatial awareness of the underlying audio field while interacting with complex control layers. High-intensity glow effects are used sparingly to denote active states and critical data thresholds.

## Colors

The color palette of this design system is optimized for high-performance dark mode environments. 

- **Midnight Purple (#1A0B2E):** Serves as the foundation. It provides a deep, infinite canvas that minimizes eye strain during long engineering sessions while allowing vibrant accents to pop.
- **Electric Cyan (#00F5FF):** The primary functional color. It is used for interactive elements, primary data paths, and positive state indications. It mimics the luminescence of hardware interfaces.
- **Neon Magenta (#FF00E5):** The highlight and alert color. It is reserved for high-priority notifications, peak audio levels, and secondary interactive accents.
- **Surface Tints:** Use varying opacities of white (10-20%) for glass layers to create distinction without losing the deep purple background.

## Typography

This design system utilizes a dual-font approach to balance futuristic character with technical legibility. 

- **Space Grotesk** is used for headlines and UI labels where a distinctive, cutting-edge personality is required. Its geometric construction reinforces the "spatial" narrative.
- **Inter** is employed for body text, technical readouts, and high-density data visualizations. It provides the neutral, systematic clarity necessary for complex audio waveforms and coordinate lists.

All labels and technical readouts should favor uppercase styling with increased letter spacing to enhance the "instrumentation" feel of the interface.

## Layout & Spacing

The layout follows a **fluid grid** model designed to accommodate varying aspect ratios found in XR goggles and desktop workstations. A 12-column system is used for primary dashboard layouts, allowing for modular "pods" of data.

Spacing follows an 8px base rhythm to ensure mathematical precision in the UI. Components should feel airy but structured, with generous internal padding (MD) to allow the glassmorphic background blurs to feel atmospheric rather than cluttered. Margins are intentionally wide to keep critical interactive elements away from the edge of the optical periphery in spatial headsets.

## Elevation & Depth

Depth is the defining characteristic of the design system, achieved through **Glassmorphism** rather than traditional drop shadows.

- **Surface Layers:** Use `backdrop-filter: blur(24px)` combined with a subtle `1px` inner border (White at 15% opacity).
- **Z-Axis Hierarchy:** Higher elevation layers are represented by increased background opacity (from 5% to 20%) and brighter border highlights.
- **Glow Effects:** Use `box-shadow` with the Electric Cyan or Neon Magenta color at very high blur radii (20px-40px) and low opacity (30%) to simulate light emission from interactive components.
- **Parallax:** In spatial contexts, UI elements should be separated by 20mm–50mm of virtual depth to indicate hierarchy.

## Shapes

The shape language is "Soft-Technical." By using a consistent 0.25rem (4px) base corner radius, the design system avoids the aggressive feel of sharp corners while maintaining the precision of an engineered tool. 

- **Primary Containers:** 0.25rem (4px) for a crisp, machined look.
- **Interactive Elements:** Buttons and inputs follow the same 4px rule to maintain a cohesive hardware-inspired aesthetic.
- **Data Points:** Small circular elements or 45-degree chamfered edges are used in charts to signify technical nodes.

## Components

- **Translucent Cards:** The primary container. Must feature a 1px top-left highlight border and a subtle background blur to ensure legibility against complex spatial backgrounds.
- **Buttons:** 
  - *Primary:* Solid Electric Cyan with black text and an external cyan glow.
  - *Secondary:* Ghost style with an Electric Cyan border and 10% fill.
- **Inputs:** Dark purple background with a Magenta "active" bottom border. Technical readouts appear in Inter Mono.
- **Data Charts:** Use high-contrast line work. Grid lines should be Midnight Purple (lightened by 10%). Primary data lines use Electric Cyan with a subtle glow.
- **3D-Inspired Icons:** Icons are monochromatic line art but use "isometric" perspectives or multi-line thickness to imply three-dimensionality.
- **Audio Visualizers:** Dynamic components that use Neon Magenta for peak levels and Electric Cyan for steady-state frequencies, utilizing high-frequency refresh rates for a "live" technical feel.