---
name: Chrono-Tactile
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
  on-surface-variant: '#c4c7ca'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9194'
  outline-variant: '#44474a'
  surface-tint: '#c3c7cb'
  primary: '#d0d4d8'
  on-primary: '#2c3134'
  primary-container: '#b4b8bc'
  on-primary-container: '#44494c'
  inverse-primary: '#5a5f63'
  secondary: '#ffb77b'
  on-secondary: '#4d2700'
  secondary-container: '#7a4100'
  on-secondary-container: '#ffb270'
  tertiary: '#d5d3d2'
  on-tertiary: '#313030'
  tertiary-container: '#b9b7b7'
  on-tertiary-container: '#494848'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe3e7'
  primary-fixed-dim: '#c3c7cb'
  on-primary-fixed: '#181c1f'
  on-primary-fixed-variant: '#43474b'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ffb77b'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6d3a00'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  gauge-value:
    fontFamily: JetBrains Mono
    fontSize: 42px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: -0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
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
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  component-gap: 12px
---

## Brand & Style
The design system embodies the spirit of "Horological Engineering," translating the intricate, high-mechanical world of luxury watchmaking into a functional automotive interface. It targets an audience that values mechanical permanence over disposable digital trends—emphasizing artisanal precision, tactile feedback, and structural integrity.

The aesthetic is heavily **Skeuomorphic and Tactile**, utilizing physical metaphors of milled titanium, machined copper, and deep-set mechanical assemblies. Every interaction should feel like operating a calibrated instrument. The visual tone is ultra-precise and premium, evoking the emotional response of sitting inside a master-crafted mechanical timepiece where every gear and surface serves a dedicated purpose.

## Colors
The palette is rooted in the materials of haute horlogerie. The primary surface language uses **Brushed Titanium** (cool, anisotropic greys) to provide a sense of weight and structural durability. **Copper** serves as the sole accent color, used exclusively for indicators, needles, and critical interactive states, mimicking the internal gears and conductive elements of a movement.

The background is a **Matte Black** obsidian, providing a high-contrast foundation that allows the metallic textures to pop. Neutral tones are strictly cool-shifted to maintain the "milled metal" feel, avoiding warm greys to ensure the copper accents remain the distinct focal point of the hierarchy.

## Typography
The typographic strategy balances modern legibility with mechanical soul. **Hanken Grotesk** is utilized for primary interface labels and headings, chosen for its sharp apertures and contemporary, engineered feel. 

For all numerical data, telemetry, and gauge readouts, **JetBrains Mono** is employed to simulate the fixed-width character spacing of physical date wheels and mechanical counters. This monospaced approach ensures that "rolling" numbers do not cause layout shift and reinforces the "instrument cluster" aesthetic. All labels should be treated with generous tracking (letter-spacing) and often set in all-caps to mimic engraved plates.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy, reminiscent of a dashboard where every instrument has a designated, permanent housing. Elements are organized into "Modules" that feel bolted or machined into the interface. 

The spacing rhythm is based on a 4px increment, but emphasizes "Negative Space as Mass." Instead of airy whitespace, this design system uses the "void" of the matte black background to frame recessed metallic components. In automotive contexts, critical controls are placed within ergonomic reach (F-pattern), with telemetry grouped in the central visual axis. Padding within components is tight and disciplined, reflecting the high-tolerance assembly of a watch movement.

## Elevation & Depth
Depth is the defining characteristic of this design system. It moves away from "shadows" toward **Physical Relief**. 

1.  **Recessed Dials (In-set):** Gauges and secondary controls must appear deeply milled *into* the titanium surface using inner shadows and bezel highlights (top-left light source).
2.  **Raised Knobs (Out-set):** Primary interactive elements like dials or "crowns" use multi-layered gradients and sharp rim-lighting to appear extruded from the surface.
3.  **Brushed Textures:** Surfaces are never flat; they feature subtle directional "brushing" (linear gradients with fine noise) to simulate titanium.
4.  **The "Glow":** Light does not diffuse; it reflects. Use sharp, high-opacity "glints" on the edges of copper elements to simulate metallic luster.

## Shapes
The shape language is dominated by **Geometric Rigidity**. While dials are perfectly circular (the geometry of a gear), the containers are strictly rectangular or octagonal with very subtle rounding. 

A `roundedness` of 1 (Soft) is used only to prevent the UI from feeling "digitally sharp," simulating the way a CNC machine leaves a slightly eased edge on a piece of milled metal. Any circular element (buttons, dials) should be treated as a true 50% radius "Coin" shape, often featuring a knurled or coin-edge texture on its perimeter.

## Components
-   **Rotary Selectors:** The core interaction. These appear as raised metallic cylinders with knurled edges. They respond to touch with a visual "click" or rotation animation.
-   **Physical Toggles:** Switches should mimic "flip" or "plunger" toggles found in chronographs. Copper is used for the "on" state filament.
-   **Recessed Cards:** Content containers are not floating; they are "pockets" milled into the dashboard, defined by a 1px metallic bevel highlight on the bottom edge and an inner shadow on the top.
-   **The Needle Indicator:** Used for progress or gauges. A razor-sharp copper line with a circular pivot point.
-   **Status Chips:** These should resemble small, inset LED indicators or engraved brass plates.
-   **Buttons:** Must feature a "Tactile Press." On interaction, the element physically shifts its inner shadows to appear depressed into the frame.