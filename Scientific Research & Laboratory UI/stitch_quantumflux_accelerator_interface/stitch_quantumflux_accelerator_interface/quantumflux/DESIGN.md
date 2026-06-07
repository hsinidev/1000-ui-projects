---
name: QuantumFlux
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
  on-surface-variant: '#b9ccb2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#84967e'
  outline-variant: '#3b4b37'
  surface-tint: '#00e639'
  primary: '#ebffe2'
  on-primary: '#003907'
  primary-container: '#00ff41'
  on-primary-container: '#007117'
  inverse-primary: '#006e16'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#fcf8f8'
  on-tertiary: '#313030'
  tertiary-container: '#dfdcdb'
  on-tertiary-container: '#626060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#72ff70'
  primary-fixed-dim: '#00e639'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#00530e'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-lg:
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
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

The brand personality of this design system is defined by clinical precision, raw energy, and intellectual authority. It is designed for a target audience of research scientists, data engineers, and high-level stakeholders who require an environment that feels both cutting-edge and mathematically rigorous. The UI should evoke a sense of "observing the invisible"—the feeling of looking through a high-powered lens into the subatomic world.

The visual style is a fusion of **Glassmorphism** and **Brutalism**. It utilizes the structural rigidity of a laboratory grid system while overlaying translucent, ethereal data layers. Mathematical textures—such as coordinate planes, vector fields, and schematic blueprints—are integrated into the background to reinforce the scientific context. The aesthetic is unapologetically dark, mirroring the vacuum of deep space where light and matter are the only protagonists.

## Colors

The palette is anchored by **Deep Space Black**, providing a high-contrast foundation that eliminates visual noise. **Laser Green** serves as the primary action and state color, representing ionized energy and active data streams. **Silver** is used for structural elements and secondary metadata, providing a metallic, hardware-inspired feel.

The color system relies on luminosity rather than hue. Instead of standard grays, the design system uses varying opacities of Silver and Green to create "glowing" hierarchies. Backgrounds are strictly #050505 to ensure the OLED-black depth required for the particle-trace animations to pop visually.

## Typography

This design system employs a dual-font strategy to balance character with legibility. **Space Grotesk** is used for headlines and technical labels; its geometric quirks suggest a futuristic, scientific apparatus. **Inter** is utilized for body copy and dense data displays, ensuring that complex research papers and mathematical proofs remain highly readable at any scale.

Data-heavy screens should prioritize the "Label-Mono" style for metadata, timestamps, and coordinate values to maintain an authoritative, machine-readable aesthetic. All caps and increased letter spacing are used sparingly for navigational headers to mimic cockpit instrumentation.

## Layout & Spacing

The layout is built upon a **12-column rigid grid** that is often rendered visible as a subtle background overlay. This "Mathematical Grid" uses 1px Silver lines at 10% opacity to provide a sense of architectural structure. 

The spacing rhythm is strictly based on a 4px base unit. Components should align to the grid intersections, creating a modular feel. Margin and padding should be generous between functional blocks to prevent the high-contrast elements from overwhelming the user, while internal data clusters use tight, dense spacing to maximize information density.

## Elevation & Depth

In this design system, depth is not conveyed through shadows, but through **light and transparency**. 

1.  **Backdrop Blurs:** High-elevation elements like modals and dropdowns use a 20px blur with a 5% Silver fill, creating a frosted-glass effect that allows underlying particle animations to remain visible as blurred shapes.
2.  **Luminous Outlines:** Instead of drop shadows, active elements use a 1px inner stroke of Laser Green and an outer 4px soft glow (box-shadow: 0 0 8px rgba(0, 255, 65, 0.3)).
3.  **Tonal Stacking:** The background is the lowest layer. Grid lines sit above the background. "Particle-Trace" animations flow between the grid and the interactive components.

## Shapes

The shape language is defined by **mathematical absolute precision**. All primary components—buttons, cards, and input fields—utilize sharp 0px corners. This reinforces the brutalist, high-tech nature of a particle physics lab where there is no room for "softness."

For specific "high-energy" interactive elements, a 45-degree chamfer (clipped corner) can be used on the top-right and bottom-left to suggest movement and directional flow.

## Components

### Buttons & Controls
Buttons are transparent with a 1px Silver border by default. On hover, they "ionize," filling with Laser Green and switching text to Deep Space Black. Every interaction should feel like a state change in a physical machine.

### Neon-Bordered Cards
Cards utilize a 1px border. Under normal states, the border is a low-opacity Silver. Under "Active" or "Alert" states, the border glows in Laser Green. The background of the card is a semi-transparent Deep Space Black (#050505 at 80% opacity) with a backdrop blur.

### Particle-Trace Animations
Loading states and data transitions should use "Particle-Trace" styles: thin, high-speed lines that follow SVG paths, mimicking the tracks left by subatomic particles in a cloud chamber. These lines should fade in opacity along their length.

### Data Visualizations
Charts should avoid solid fills. Use line graphs with "glow" effects and scatter plots where each data point is a small, pulsing Laser Green dot. Grid lines within charts must align perfectly with the global layout grid.

### Input Fields
Inputs are underlined rather than boxed, featuring a "Scan-line" animation—a horizontal green line that sweeps vertically across the field when it receives focus.