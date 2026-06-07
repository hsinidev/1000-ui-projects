---
name: Industrial Audio System
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
  on-surface-variant: '#e4beba'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#ab8985'
  outline-variant: '#5b403d'
  surface-tint: '#ffb3ac'
  primary: '#ffb3ac'
  on-primary: '#680008'
  primary-container: '#d32f2f'
  on-primary-container: '#fff2f0'
  inverse-primary: '#ba1a20'
  secondary: '#c7c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#707070'
  on-tertiary-container: '#f7f5f4'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb3ac'
  on-primary-fixed: '#410003'
  on-primary-fixed-variant: '#930010'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e2e2'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
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
  container-max: 1280px
---

## Brand & Style

The design system is engineered to evoke the raw, uncompromising durability of high-end analog hardware. It targets professional musicians and audio engineers who value precision, tactile feedback, and "overbuilt" aesthetics. The brand personality is rugged, authoritative, and technical, bridging the gap between vintage studio equipment and modern industrial machinery.

The visual style is a hybrid of **Tactile Skeuomorphism** and **Brutalism**. It utilizes heavy-duty borders, metallic surface treatments, and a "signal path" logic where elements are connected by visible conduits. The emotional response should be one of confidence and physical reliability—as if every button on the screen would make a satisfying mechanical "clunk" if pressed.

## Colors

The palette is strictly functional, drawing inspiration from workshop machinery and circuit boards. 

- **Deep Graphite (#1A1A1A):** The foundation. Used for backgrounds to simulate the powder-coated chassis of a guitar pedal.
- **Brushed Steel (#A0A0A0):** Used for primary surfaces, control panels, and "faceplates." This color should often carry a subtle vertical linear gradient to mimic brushed metal.
- **Signal Red (#D32F2F):** Reserved for primary actions, critical alerts, and active "ON" states (mimicking an LED).
- **Secondary Grays:** Used for internal housing, dividers, and inactive states, maintaining a high-contrast environment.

## Typography

This design system uses a high-contrast typographic pairing to balance heritage and technology.

- **Headings:** Utilizes **Noto Serif** in its heaviest weights (Bold to Black). This simulates the stamped or engraved slab-serif lettering found on vintage amplifier plates. Headlines should be tightly tracked and impactful.
- **Body Text:** Uses **Inter** for maximum legibility against dark, textured backgrounds. It provides a clean, neutral counterpoint to the aggressive headings.
- **Technical Labels:** **Space Grotesk** is used for all UI labels, knob values, and "stamped" instructions. Its geometric, slightly quirky construction reinforces the engineered, futuristic nature of the signal path.

## Layout & Spacing

The layout is governed by a **fixed 12-column industrial grid**. This system prioritizes structural integrity over fluid airiness.

- **Grid:** All components must align to a strict 8px baseline. Elements should feel "bolted" into place.
- **Margins/Gutters:** Generous 40px outer margins provide a sense of a physical object sitting in space, while 24px gutters separate distinct functional modules (e.g., the "EQ section" vs the "Gain section").
- **Signal Path Aesthetic:** Use 2px thick lines (Signal Red or Steel) to connect related modules, visually representing the flow of audio from input to output. Lines should only move at 90-degree angles.

## Elevation & Depth

Depth in this design system is achieved through mechanical layering rather than light-source shadows.

- **Tonal Layering:** The background is the chassis (Deep Graphite). Surfaces placed upon it (Brushed Steel) use 2px solid borders (#4D4D4D) to create a "milled" look.
- **Inner Shadows:** Use subtle inner shadows on input fields and "wells" to suggest they are recessed into the metal faceplate.
- **High-Contrast Borders:** Instead of drop shadows, use 1px or 2px solid strokes. A light top border and dark bottom border on buttons creates a "stamped" 3D effect.
- **Tactile Indicators:** Active states should use a "glow" effect (box-shadow: 0 0 10px Signal Red) to mimic an illuminated incandescent bulb or LED.

## Shapes

The shape language is predominantly **Sharp**, with very slight rounding to mimic "eased" machined edges.

- **Components:** Buttons and cards use a 4px (Soft) corner radius. This prevents the UI from feeling dangerously sharp while maintaining a rigid, industrial silhouette.
- **Knobs:** Interactive dials are the only perfectly circular elements, providing a clear visual distinction between "toggle/switch" actions and "variable" adjustments.
- **Encapsulation:** Grouped controls should be enclosed in "frames"—high-contrast bordered containers with notched corners or visible "screw" icons in the four corners.

## Components

### Buttons & Switches
- **Primary Action:** Signal Red background, white Noto Serif Bold text. Use a 2px bottom border of a darker red to create a "stomp-switch" appearance.
- **Toggle Switches:** Vertical sliders that mimic physical metal toggles. Use high-contrast "ON/OFF" labels in Space Grotesk.

### Knobs & Dials
- Dial components should have a visible "pointer" or indicator line in Signal Red. Use a conical gradient to simulate a metallic, radial finish.

### Input Fields
- Recessed into the surface with an inner shadow. Use the technical font (Space Grotesk) for user input to look like printed data.

### Signal Lines
- Use 2px strokes to connect components. Use "Jack" icons (circles with a center dot) at the start and end of these lines to indicate connection points.

### Cards & Modules
- Modules should have a "Faceplate" look: Brushed Steel surface, 2px graphite border, and visible "mounting screw" assets in the corners to reinforce the industrial hardware metaphor.

### Alerts & Indicators
- Indicators should resemble LEDs. An inactive state is a dark, recessed circle; an active state is a vibrant Signal Red with a soft outer glow.