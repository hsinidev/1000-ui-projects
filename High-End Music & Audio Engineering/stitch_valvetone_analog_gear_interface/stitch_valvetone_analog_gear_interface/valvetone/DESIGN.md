---
name: ValveTone
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c6'
  primary: '#dcdcdc'
  on-primary: '#2f3131'
  primary-container: '#c0c0c0'
  on-primary-container: '#4d4e4f'
  inverse-primary: '#5d5e5f'
  secondary: '#ffe2ab'
  on-secondary: '#402d00'
  secondary-container: '#ffbf00'
  on-secondary-container: '#6d5000'
  tertiary: '#dedcdb'
  on-tertiary: '#313030'
  tertiary-container: '#c2c0bf'
  on-tertiary-container: '#4f4e4e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#464747'
  secondary-fixed: '#ffdfa0'
  secondary-fixed-dim: '#fbbc00'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5c4300'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-silk:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.02em
  readout-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
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
  component-gap: 24px
  chassis-margin: 32px
  screw-offset: 12px
---

## Brand & Style
The design system is engineered to evoke the prestige and physical presence of high-end boutique vacuum tube hardware. It targets audio professionals and enthusiasts who value the "warmth" and "soul" of analog circuitry. The brand personality is authoritative, uncompromising, and deeply tactile.

The design style is **Skeuomorphic**. It rejects flat digital trends in favor of realistic textures, physical depth, and mechanical interaction. The interface must feel like a heavy piece of rack-mounted equipment, using metallic grain, high-gloss plastic finishes, and warm incandescent light to create an immersive, high-fidelity experience.

## Colors
The palette is built on the interplay between cold metal and warm electronics.

- **Brushed Aluminum (Base):** Used for the primary chassis. Implement with a linear gradient (top-to-bottom) to simulate light falling on a vertical surface. Apply a 2% monochromatic noise grain to simulate metal texture.
- **Amber Glow (Accents):** This is the "on" state color. Use for LEDs, VU meter backlighting, and active switch positions. It must always be accompanied by a soft Gaussian outer glow.
- **Bakelite Black (Controls):** A deep, high-gloss black used for rotary knobs and toggle switches. It features sharp, white specular highlights to suggest a reflective plastic surface.
- **VU Meter Cream:** A nostalgic, slightly yellowed paper texture used exclusively for analog gauge backgrounds to ensure readability and period-accuracy.

## Typography
Typography in this design system mimics two distinct physical manufacturing processes:

1.  **Embossed Labels:** Headings utilize **Inter** (Bold) with a slight inner shadow and light "extrusion" effect to look like stamped metal or Dymo tape.
2.  **Silk-Screened Labels:** Functional labels for knobs and ports use **Inter** with a high-contrast ink-on-metal look.
3.  **Technical Readouts:** Digital displays and technical data use **Space Grotesk**. Its geometric, technical nature mimics modern-retro digital displays while maintaining the system's "engineered" feel.

Text should rarely be pure white; use a very light grey (#E0E0E0) to simulate ink aging.

## Layout & Spacing
The layout follows a **Fixed Grid** model, mimicking the standard 19-inch rack-mount format. Components are organized into logical "modules" or vertical strips. 

- **Physicality:** Layout elements are separated by subtle "seams" or grooves in the metal chassis.
- **Rhythm:** Use a strict 4px baseline, but prioritize visual centering for rotary controls.
- **Hardware Anchors:** Decorative elements like hex-head screws should be placed at the four corners of the main interface to reinforce the hardware metaphor.

## Elevation & Depth
Depth is the core of this design system. It is achieved through multi-layered lighting:

- **Recessed Areas:** VU meters and port jacks use deep inner shadows (inset) to appear "sunk" into the faceplate.
- **Extruded Controls:** Knobs and switches use a combination of drop shadows (to the bottom-right) and top-edge highlights (1px white at 40% opacity) to appear to "pop" off the surface.
- **Lighting Direction:** Maintain a consistent light source from the "top-left." This means shadows always fall to the bottom-right, and highlights hit the top-left edges of all raised elements.
- **Surface Contrast:** Use a 1px "bevel" on the edge of the chassis to distinguish the front plate from the dark background of the DAW or environment.

## Shapes
The shape language is industrial and functional. 

- **Chassis:** Low roundedness (0.25rem) to suggest heavy, machined metal plates.
- **Knobs:** Perfectly circular, with radial gradients and knurled textures on the edges.
- **Toggle Switches:** Rectangular bases with pill-shaped metal "bats."
- **Cutouts:** VU meters should have slightly rounded corners (Soft, 0.25rem) to reflect mid-century industrial design.

## Components
- **Rotary Knobs:** The primary input. Must feature a "Bakelite Black" finish with a single white indicator line. On hover, the indicator line glows faintly; on drag, the knob rotates with realistic shadow shifting.
- **Toggle Switches:** Vertical orientation (Up = On, Down = Off). "On" state activates an Amber Glow LED lamp positioned directly above the switch.
- **VU Meters:** Analog needles with high-inertia physics (overshoot and settle). The background is "VU Meter Cream" with printed black scales and a "Red Zone" starting at +3dB.
- **Input Fields:** Styled as recessed "Dymo" labels or digital nixie-tube-style readouts using Space Grotesk.
- **Buttons:** Large, tactile "stomp-box" style buttons or square backlit translucent plastic.
- **Chassis Screws:** Non-interactive decorative elements placed at the edges to ground the skeuomorphic effect.