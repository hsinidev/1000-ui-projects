---
name: Chrono-Tactile
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#cec5b7'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#313031'
  outline: '#979083'
  outline-variant: '#4c463b'
  surface-tint: '#dac493'
  primary: '#dac493'
  on-primary: '#3c2f0a'
  primary-container: '#b5a172'
  on-primary-container: '#453812'
  inverse-primary: '#6d5d34'
  secondary: '#c3c7c9'
  on-secondary: '#2d3133'
  secondary-container: '#484c4e'
  on-secondary-container: '#b8bcbe'
  tertiary: '#c6c6c9'
  on-tertiary: '#2f3133'
  tertiary-container: '#a2a3a5'
  on-tertiary-container: '#38393c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f7e0ad'
  primary-fixed-dim: '#dac493'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#54451f'
  secondary-fixed: '#dfe3e5'
  secondary-fixed-dim: '#c3c7c9'
  on-secondary-fixed: '#181c1e'
  on-secondary-fixed-variant: '#434749'
  tertiary-fixed: '#e2e2e5'
  tertiary-fixed-dim: '#c6c6c9'
  on-tertiary-fixed: '#1a1c1e'
  on-tertiary-fixed-variant: '#454749'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  heritage-display:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  heritage-lg:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  telemetry-num:
    fontFamily: JetBrains Mono
    fontSize: 40px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.05em
  telemetry-label:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.5'
    letterSpacing: 0.1em
  body-standard:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-edge: 48px
  component-gap: 16px
  bezel-thickness: 2px
---

## Brand & Style

The design system is a fusion of high-watchmaking (Haute Horlogerie) and avant-garde automotive engineering. It targets a demographic that values mechanical soul over generic digital convenience. The brand personality is disciplined, prestigious, and physical.

The visual style is **Hyper-Tactile Skeuomorphism**. Unlike early 2010s realism, this system uses modern rendering techniques to simulate high-end materials: brushed titanium, machined gold, and anti-reflective sapphire glass. The interface should feel like a physical instrument cluster, where every digital interaction carries the perceived weight and resistance of a precision-milled mechanical component. 

Key emotional drivers include:
- **Mechanical Integrity:** Every element feels screwed-in or machined from a solid billet.
- **Instrumental Precision:** Information is delivered with the cold accuracy of telemetry data.
- **Heritage Luxury:** Subtle nods to classic luxury through refined serif typography.

## Colors

The palette is anchored in a deep **Matte Black** universe to ensure zero-glare visibility in high-performance driving environments. 

- **Champagne Gold (Primary):** Used exclusively for high-priority interactive states, critical accents, and heritage branding elements. It should be rendered with a metallic anisotropic gradient.
- **Brushed Titanium (Secondary):** The primary structural color. It defines the "housing" of the UI, used for borders, bezels, and inactive telemetry data.
- **Deep Obsidian (Tertiary):** Used for container backgrounds to provide depth against the absolute black base.
- **Illuminated White:** A pure, high-contrast white used for active data readings to ensure maximum legibility against the dark surroundings.

## Typography

This design system utilizes a dual-font strategy to balance emotion and function.

1. **Heritage Elements (Bodoni Moda):** A high-contrast serif used for model names, drive modes (e.g., "Grand Tourer"), and luxury storytelling. It evokes the feeling of a bespoke watch face.
2. **Telemetry Data (Geist / JetBrains Mono):** Monospaced and highly technical fonts are used for all live vehicle data. **JetBrains Mono** is reserved for numeric readouts (speed, RPM, temps) to ensure tabular lining, while **Geist** provides a clean, neutral sans-serif for secondary labels and system messages.

All typography must maintain a high contrast ratio. Numerical data should feature a subtle "outer glow" to mimic self-illuminating physical gauges.

## Layout & Spacing

The layout philosophy is based on a **Radial Instrument Grid**. While the core structure follows a 12-column system for wide-screen infotainment, the primary driver display is centered around circular and semi-circular "pods."

- **Symmetry:** Layouts are strictly symmetrical or balanced across a central vertical axis to reflect automotive cockpit design.
- **The "Bezel" Rule:** Every major container is encased in a "precision-milled" bezel (2px stroke) with a 45-degree light source simulation.
- **Safe Zones:** Content must respect a 48px margin from the physical screen edge to account for the vehicle’s interior trim overlaps.
- **Interaction Spacing:** Touch targets are oversized (minimum 64x64px) to allow for use during high-vibration driving scenarios.

## Elevation & Depth

Depth is not achieved through shadows alone, but through **Material Layering**.

- **Level 0 (Base):** Matte Black. The "void" or the base chassis of the screen.
- **Level 1 (Inlay):** Deep Obsidian with a subtle inner shadow. Elements appear "milled" into the surface.
- **Level 2 (Plateau):** Brushed Titanium surfaces that sit "flush" with the frame.
- **Level 3 (Raised):** Champagne Gold accents and physical-style knobs. These use high-contrast drop shadows (80% opacity, 4px blur) to appear physically separated from the dashboard.

**Mechanical Tick Animation:** Transitions between elevations do not use smooth eases. Instead, they use a "stepped" animation style mimicking the 28,800 bph frequency of a mechanical watch movement, creating a subtle, high-frequency vibration during state changes.

## Shapes

The shape language is **Industrial and Angular**. 

- **Geometric Foundation:** Circles are perfect; rectangles use very small, tight radii (4px to 8px) to mimic the look of precision-cut metal plates. 
- **Chamfered Edges:** Instead of large organic curves, the system favors 45-degree chamfers on corners for specialized buttons. 
- **Knurling:** Vertical "precision-milled" textures (1px repeating lines) are applied to the sides of sliders and circular dials to suggest tactile grip.

## Components

- **The Chrono-Dial:** The central component. A skeuomorphic circular gauge with a physical-style needle that casts a dynamic shadow on the dial face behind it.
- **Milled Buttons:** Rectangular components with a Brushed Titanium gradient. On-press, they shift from a "raised" gradient to an "inset" gradient, accompanied by a haptic "click" simulation.
- **Telemetry Chips:** Small, monospaced data tags with a Champagne Gold left-border. Used for tire pressure, oil temp, and G-force.
- **Segmented Sliders:** Volume and climate controls are presented as segmented metal bars. As the value increases, segments light up in Champagne Gold.
- **Heritage Cards:** Used for media and navigation. These feature a subtle "frosted sapphire" overlay, allowing the Matte Black background to bleed through with a heavy blur.
- **The Gear Indicator:** A large, high-contrast Serif (Bodoni) character that appears "etched" into a metallic circular plate in the center of the display.