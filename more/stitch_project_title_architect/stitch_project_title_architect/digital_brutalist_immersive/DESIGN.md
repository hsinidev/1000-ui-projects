---
name: Digital Brutalist Immersive
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cfc2d8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#988ca1'
  outline-variant: '#4c4355'
  surface-tint: '#dbb8ff'
  primary: '#dbb8ff'
  on-primary: '#470083'
  primary-container: '#9933ff'
  on-primary-container: '#fdf3ff'
  inverse-primary: '#850aeb'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#6f7171'
  on-tertiary-container: '#f6f6f6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#efdbff'
  primary-fixed-dim: '#dbb8ff'
  on-primary-fixed: '#2b0053'
  on-primary-fixed-variant: '#6600b7'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: epilogue
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  body-md:
    fontFamily: spaceGrotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-mono:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  metadata:
    fontFamily: spaceGrotesk
    fontSize: 10px
    fontWeight: '400'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-padding: 64px
  gutter: 24px
  section-gap: 160px
---

## Brand & Style

The design system is a sophisticated blend of raw structural integrity and ethereal digital depth. It targets high-end creative portfolios, technical showcases, and immersive web experiences where the interface acts as a high-fidelity "Heads-Up Display" (HUD) for 3D content. 

The aesthetic is driven by a "Brutalism Lite" philosophy—maintaining the starkness and grid-dependency of classic brutalism but refining it with the polish of glassmorphism and refractive light. The emotional response is intended to be one of mystery, precision, and avant-garde luxury. It prioritizes the "void" (significant black whitespace) to allow 3D focal points to emerge with maximum impact, while kinetic transitions and technical metadata overlays reinforce a sense of real-time digital craftsmanship.

## Colors

The palette is rooted in a monochromatic dark foundation, utilizing `#000000` for the absolute background to create an infinite "void" effect. The primary brand color, a vivid Violet (`#9933FF`), is reserved for high-intensity interactive states and focus elements. 

To achieve the "neon" technical look requested, the system uses high-contrast white (`#FFFFFF`) for primary typography and UI borders, ensuring maximum legibility against the dark surfaces. A secondary neutral gray (`#1A1A1A`) is used for subtle container differentiation, preventing the layout from feeling flat while maintaining the "dark mode" immersion.

## Typography

This design system employs a dual-font strategy to balance editorial impact with technical precision. **Epilogue** serves as the headline typeface; its geometric, bold weights are used in oversized formats to anchor the layout and provide a "Neue Haas Grotesk" brutalist weight.

**Space Grotesk** is utilized for all body text, labels, and metadata. Its rhythmic, technical structure mimics the appearance of monospaced fonts while maintaining superior readability. For performance metrics and coordinate trackers, the font is used at small scales with increased letter-spacing to evoke a command-line interface or a digital readout.

## Layout & Spacing

The layout follows a strict 12-column fixed grid, yet it feels fluid through the use of extreme whitespace. Large "safe zones" are established around central 3D assets to ensure the interface never crowds the artwork. 

Spacing is governed by an 8px base unit. Margins are intentionally wide (64px+) to create a gallery-like atmosphere. Elements like FPS counters and coordinate trackers are pinned to the viewport corners or edges, acting as structural "anchors" that define the digital canvas without interrupting the content flow.

## Elevation & Depth

Depth is conveyed through "Refractive Glassmorphism" rather than traditional drop shadows. Surfaces are treated as semi-transparent panels with a high-intensity backdrop blur (20px-40px). 

1.  **Base Layer:** Solid `#000000` void.
2.  **Mid Layer:** Technical wireframe overlays (0.1 opacity white) and grid lines that provide a sense of spatial orientation.
3.  **Floating Layer:** Glass containers with a 1px border (`#FFFFFF` at 0.2 opacity). These panels use additive blending modes to feel light and ethereal.
4.  **Interaction Layer:** Kinetic 3D elements that cast no shadows but instead emit a subtle Violet (`#9933FF`) outer glow (bloom) to simulate light emission in a dark space.

## Shapes

The shape language is strictly architectural and sharp. This design system uses a `0` roundedness setting to maintain the Brutalist Lite aesthetic. Every button, container, and input field features 90-degree angles to reinforce the technical, precision-engineered feel. 

The only exceptions to this rule are the 3D assets themselves (spheres, organic meshes), which provide a soft, fluid contrast to the rigid, sharp-edged interface that contains them.

## Components

### Buttons & Interaction
Buttons are constructed as transparent rectangles with a 1px white border. Upon hover, the button fills with the Primary Violet color, and the border disappears. Transitions must be "fluid and kinetic"—using custom cubic-bezier curves (e.g., `0.16, 1, 0.3, 1`) to feel snappy yet smooth.

### Metadata HUD
Small text clusters positioned at the periphery of the screen. These components include "Coordinate Trackers" (mapping mouse X/Y) and "Status Indicators" (e.g., "SYSTEM_READY"). They use the `label-mono` type style and are rendered in 50% opacity white.

### Glass Cards
Used for grouping information or settings. These cards have no background color other than the `backdrop-filter: blur()`. They are defined solely by their 1px translucent white borders.

### Wireframe Overlays
A decorative component consisting of a thin-stroke grid or a geometric wireframe mesh that sits behind the primary UI. It serves as a visual texture that emphasizes the "3D Minimalism" theme.

### Form Inputs
Minimalist underlines instead of boxes. Labels use the `metadata` style and sit exactly 8px above the input line. On focus, the underline transforms from a 1px white line to a 2px Violet line.