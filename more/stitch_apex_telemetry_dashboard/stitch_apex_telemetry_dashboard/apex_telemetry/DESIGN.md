---
name: Apex Telemetry
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#ffffff'
  on-secondary: '#353100'
  secondary-container: '#f5e700'
  on-secondary-container: '#6d6600'
  tertiary: '#00dbe9'
  on-tertiary: '#00363a'
  tertiary-container: '#00a0aa'
  on-tertiary-container: '#002f33'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#f5e700'
  secondary-fixed-dim: '#d7ca00'
  on-secondary-fixed: '#1f1c00'
  on-secondary-fixed-variant: '#4d4800'
  tertiary-fixed: '#7df4ff'
  tertiary-fixed-dim: '#00dbe9'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-speed:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.04em
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  telemetry-data:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1'
  body-standard:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 100%
  grid-cols: '12'
---

## Brand & Style
The design system is engineered for high-velocity data consumption and peak performance. It evokes the atmosphere of an F1 pit wall—intense, precise, and uncompromising. The aesthetic targets professional analysts and enthusiasts who require split-second cognitive processing of complex data streams.

The visual style is a fusion of **Tactile Carbon-Fiber** and **Technical Glassmorphism**. It utilizes a "Darkroom" philosophy where the interface recedes to allow vibrant telemetry data to take center stage. Every element is designed to feel like a high-performance component: lightweight, structural, and precision-milled. The use of italics throughout the typography creates a constant sense of forward momentum and kinetic energy.

## Colors
The palette is rooted in a "Deepest Black" foundation to ensure maximum contrast for critical indicators. 

- **Ferrari Red (#FF0000):** Reserved exclusively for high-priority alerts, critical sectors, engine stress indicators, and active DRS states.
- **Renault Yellow (#FFF000):** Utilized for telemetry curves, timing data, and secondary technical highlights.
- **Charcoal/Carbon:** A range of ultra-dark grays (#0A0A0A to #1A1A1A) provides the structural base, layered with a subtle 45-degree carbon fiber weave pattern at low opacity.
- **Technical Cyan:** A tertiary accent used for non-critical "steady state" telemetry and grid alignments.

## Typography
Typography is treated as a functional readout rather than prose. **Space Grotesk** is the primary driver for technical data and headlines, utilizing its geometric, "monospaced-feel" construction to ensure numerical legibility. **Inter** provides a highly readable secondary layer for status descriptions and UI labels.

Key typographic rules:
1. **The Slant:** Headlines and numerical data must use a 12-degree italic tilt to convey speed.
2. **Weight:** Heavy weights (700+) are used for primary metrics to ensure they "punch through" the dark background.
3. **Tracking:** Labels use wide letter-spacing to mimic engineering blueprints and technical schematics.

## Layout & Spacing
This design system employs a **Modular Telemetry Grid**. The layout is strictly fluid to accommodate multi-monitor setups used in racing environments. 

The grid is built on a 4px baseline, ensuring all components align with mathematical precision. Layout sections are separated by 1px "Technical Gutters" that feature subtle glowing strokes. Data density is prioritized over whitespace; information is packed tightly into modular "pods" reminiscent of an F1 steering wheel display or a garage monitor. Margins are kept thin to maximize the real estate for live-tracking maps and telemetry graphs.

## Elevation & Depth
Depth is achieved through **Luminous Layering** rather than traditional shadows. 

1. **The Base:** A dark, carbon-fiber textured canvas (#050505).
2. **Glass Tiers:** Components use a semi-transparent background (20% opacity) with a heavy backdrop-blur (12px-20px). This "Glassmorphism" creates a sense of floating HUD elements.
3. **Inner Glow:** Instead of drop shadows, elements use 1px inner borders with varying opacities of white or the primary color to suggest light-emitting edges.
4. **Active States:** When a component is "Active" or "Critical," it gains a vibrant external bloom (outer glow) in Ferrari Red, simulating an illuminated dashboard warning light.

## Shapes
The shape language is **Precision-Sharp (0px radius)**. To reflect the "Engineered" nature of the sport, avoid rounded corners which soften the aesthetic. 

Structural elements should feature "Chamfered" corners (clipped at 45 degrees) where possible to reinforce the aerodynamic and technical feel. Buttons and input fields are strictly rectangular, emphasizing the grid-based architecture. If a container requires visual separation, use a 1px border rather than a change in corner radius.

## Components
### Buttons & Controls
Buttons are high-contrast blocks. The "Primary Action" button uses a Ferrari Red background with black, italicized text. "Secondary" buttons use a ghost style: a 1px white border with a glassmorphic background. All hover states should trigger a 100% opacity color shift and a subtle "scanline" animation.

### Telemetry Cards
The core of the UI. These cards feature a technical header with a 1px Renault Yellow underline. The content area uses a monospaced-style grid for data points. Each card has a subtle carbon-fiber texture overlay (multiply mode) to differentiate it from the base canvas.

### G-Force & Track Maps
Track maps must be rendered as thin, glowing 2px paths. The "Leader" position is marked by a pulsing Ferrari Red dot. G-force meters and throttle/brake bars use vertical "segmented" blocks rather than smooth gradients, mimicking digital cockpit readouts.

### Alerts & Indicators
Critical alerts (Yellow Flags, Red Flags, Safety Car) occupy the full width of their container with a flashing 1px border. Indicators for DRS or Pit Window should use "Light Emitter" styling—small circular or rectangular icons that appear to "glow" when active.

### Technical Grids
Every chart or data visualization must sit atop a fine 20px x 20px technical grid at 5% opacity, reinforcing the precision-engineered narrative of the design system.