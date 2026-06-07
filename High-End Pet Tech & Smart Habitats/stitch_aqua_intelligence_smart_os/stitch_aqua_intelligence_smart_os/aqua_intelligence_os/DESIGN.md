---
name: Aqua-Intelligence OS
colors:
  surface: '#0c1324'
  surface-dim: '#0c1324'
  surface-bright: '#33394c'
  surface-container-lowest: '#070d1f'
  surface-container-low: '#151b2d'
  surface-container: '#191f31'
  surface-container-high: '#23293c'
  surface-container-highest: '#2e3447'
  on-surface: '#dce1fb'
  on-surface-variant: '#b9cbc2'
  inverse-surface: '#dce1fb'
  inverse-on-surface: '#2a3043'
  outline: '#83958d'
  outline-variant: '#3a4a44'
  surface-tint: '#00e0b3'
  primary: '#fdfffc'
  on-primary: '#00382b'
  primary-container: '#00ffcc'
  on-primary-container: '#00725a'
  inverse-primary: '#006b54'
  secondary: '#aac7ff'
  on-secondary: '#003064'
  secondary-container: '#3e90ff'
  on-secondary-container: '#002957'
  tertiary: '#fffeff'
  on-tertiary: '#263143'
  tertiary-container: '#d7e2fa'
  on-tertiary-container: '#596479'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#24ffcd'
  primary-fixed-dim: '#00e0b3'
  on-primary-fixed: '#002118'
  on-primary-fixed-variant: '#00513f'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#aac7ff'
  on-secondary-fixed: '#001b3e'
  on-secondary-fixed-variant: '#00468d'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#0c1324'
  on-background: '#dce1fb'
  surface-variant: '#2e3447'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Space Grotesk
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 1.25rem
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  sidebar_width: 280px
  container_max_width: 1600px
  gutter: 24px
  margin_edge: 40px
---

## Brand & Style

This design system is engineered for the elite aquarist, blending the precision of high-tech laboratory software with the immersive, serene aesthetics of the deep ocean. The brand personality is authoritative yet fluid, evoking a sense of calm control over complex biological systems. 

The visual style is **Fluid-Modern**, utilizing "liquid" glassmorphism to mimic the refractive properties of water and glass tanks. It prioritizes high-density data visualization without sacrificing the premium, spacious feel of a luxury OS. Every interaction should feel frictionless and biological, moving away from rigid, static blocks toward breathing, translucent containers.

## Colors

The palette is anchored in **Obsidian Black**, providing a high-contrast foundation that makes the biological colors of an aquarium pop. **Deep Azure Blue** serves as the primary surface color, used in semi-transparent layers to create depth. 

**Neon Mint (#00FFCC)** is the critical action and "life-sign" color. It is used sparingly for active states, healthy metric indicators, and primary call-to-actions, cutting through the dark background with medicinal precision. A secondary **Azure Blue** is used for interactive elements that are not mission-critical, maintaining a professional, calm hierarchy.

## Typography

This design system exclusively employs **Space Grotesk** to maintain a technical, avant-garde aesthetic across all touchpoints. The typeface’s geometric construction and unique apertures provide the "scientific" clarity required for chemical and temperature monitoring.

**Display** scales are used for hero metrics (e.g., pH levels or Water Temp). **Label-caps** are utilized for technical metadata and sidebar categories to ensure high legibility at small sizes. All typography should be rendered with slightly increased tracking for headers to enhance the premium, airy feel of the interface.

## Layout & Spacing

The design system uses a **Fluid Grid** model optimized for desktop viewing. The primary navigation is a **fixed left-side sidebar** (280px), allowing the main stage to breathe and expand based on the user's monitor size.

A 12-column grid system governs the placement of data cards, with a standard 24px gutter. Large-scale layouts for admin panels should favor generous margins (40px+) to prevent the high-tech data from feeling cluttered. Spacing follows a strict 8px rhythmic scale to maintain mathematical consistency in the technical interface.

## Elevation & Depth

Hierarchy is established through **Liquid Glassmorphism**. Surfaces do not use traditional drop shadows; instead, they rely on background blurs (20px to 60px) and subtle inner "sheen" borders.

1.  **Floor Level:** Pure Obsidian Black background.
2.  **Card Level:** Semi-transparent Deep Azure (10-15% opacity) with a 1px solid border (20% opacity) to simulate glass edges.
3.  **Floating Level:** Active overlays and modals use a higher saturation of Azure with intense background blurs to appear as if they are floating just beneath the surface of the water.
4.  **Glow:** High-priority status elements (Neon Mint) use a soft outer "aqua-glow" rather than a shadow to indicate bioluminescence.

## Shapes

The shape language is **Rounded (Level 2)**. A standard 0.5rem (8px) radius is applied to smaller interactive elements like buttons and inputs, while larger data cards and containers utilize a 1rem (16px) or 1.5rem (24px) radius. 

This creates a "pebble" effect—smooth, organic, and professional. Sharp corners are avoided to maintain the fluid theme, while full pills are reserved exclusively for status badges and toggles to differentiate them from structural layout elements.

## Components

### Buttons & Inputs
Buttons utilize a high-gloss finish. Primary buttons are solid Neon Mint with black text for maximum visibility. Secondary buttons are "ghost" style with a mint border. Input fields are dark, recessed wells with a 1px Mint bottom-border on focus.

### Data Cards
The "Liquid" card is the hero component. It features a subtle linear gradient (Top-Left: Deep Azure to Bottom-Right: Obsidian) with a `backdrop-filter: blur(20px)`. Text inside cards must be high-contrast white or mint.

### Sidebar Navigation
The sidebar is semi-transparent with a blurred background. Navigation items use an "active indicator" that is a vertical Neon Mint line on the left edge, coupled with a soft gradient hover state that mimics water ripples.

### Status & Gauges
Live telemetry components (e.g., Salinity, Nitrates) should use circular progress rings with a Neon Mint stroke. When a value is out of range, the stroke transitions to a pulsing amber or soft red, though the primary aesthetic remains cool and azure-focused.

### Additional Components
- **Waveform Charts:** Real-time data should be displayed using smooth, anti-aliased splines rather than jagged lines.
- **Toggle Switches:** Custom-designed to look like physical high-end aquarium equipment toggles—tactile, glowing, and responsive.