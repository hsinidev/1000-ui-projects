---
name: Abyss-Sonar
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
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#ffdb9d'
  on-secondary: '#412d00'
  secondary-container: '#feb700'
  on-secondary-container: '#6b4b00'
  tertiary: '#ffb3ae'
  on-tertiary: '#68000b'
  tertiary-container: '#280002'
  on-tertiary-container: '#e5383b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#ffdea8'
  secondary-fixed-dim: '#ffba20'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5e4200'
  tertiary-fixed: '#ffdad7'
  tertiary-fixed-dim: '#ffb3ae'
  on-tertiary-fixed: '#410004'
  on-tertiary-fixed-variant: '#930014'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-gauge:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-readout:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin-edge: 32px
  panel-gap: 24px
---

## Brand & Style

The design system is engineered for high-stakes, deep-sea exploration, where technical precision meets luxury. The brand personality is clinical, commanding, and ultra-premium—evoking the feeling of a multi-million dollar submersible cockpit. The emotional response is one of controlled intensity: the user must feel absolute confidence in the instrument's accuracy while maintaining night vision and situational awareness in pitch-black environments.

The visual style is a specialized evolution of **Glassmorphism**. Instead of the traditional "frosted" look, it utilizes high-clarity, dark-tinted glass layers with ultra-fine luminous borders. Elements appear as if projected onto pressurized glass surfaces. This is paired with a **Tactile Technical** approach, where digital readouts mimic high-end physical instrumentation through glow effects and monospaced data grids.

## Colors

The color strategy is strictly functional, designed to protect the pilot's scotopic vision. 

- **Primary Background (Midnight Blue):** Used for the base canvas to provide more depth and "infinite" space than pure black.
- **Depth (Matte Black):** Reserved for recessed areas, camera "dead zones," and the most background-level UI containers to create a sense of physical thickness.
- **UI & Alerts (Amber Glow):** The primary interactive and informational color. Amber is chosen for its superior legibility in low-light environments without causing the eye fatigue associated with white light.
- **Critical (Crimson Red):** Exclusively for life-support failures, structural integrity warnings, and depth-limit alerts.
- **Sub-Text (Slate Grey):** Used for non-essential technical metadata and unit labels (e.g., "m", "hPa") to keep the hierarchy focused on the numbers.

## Typography

This design system utilizes a dual-font approach to balance futuristic aesthetics with mission-critical legibility. 

**Space Grotesk** is used for structural headings and navigation titles, providing a geometric, "space-age" luxury feel. 

**JetBrains Mono** is the workhorse of the system. It is used for all telemetry, data readouts, and body text. The monospaced nature ensures that jumping numbers in vertical gauges and circular progress bars do not cause layout shifts, maintaining a steady visual anchor for the pilot. All numerical data should utilize tabular figures to ensure decimal points align perfectly in data grids.

## Layout & Spacing

The layout follows a **Fixed HUD (Heads-Up Display)** philosophy. Because the UI is often viewed on high-resolution integrated consoles, it utilizes a 12-column fluid grid that prioritizes peripheral vision. 

- **The Peripheral Zone:** Critical gauges (Depth, Oxygen, Battery) are pinned to the extreme left and right margins.
- **The Central Viewport:** Reserved for camera feeds and sonar mapping, utilizing a grid-based layout that can switch between a "Full immersion" single-feed and a "Multi-angle" quad-view.
- **Spacing Rhythm:** Based on a strict 4px baseline. Components are separated by generous gaps (24px+) to prevent accidental touches in turbulent waters.

## Elevation & Depth

Hierarchy is established through **Luminous Stacked Layers**. 

1. **The Abyss (Base):** Midnight Blue (#0A0E1A).
2. **The Hull (Container):** Matte Black (#050505) with 0.5px Amber borders at 20% opacity.
3. **The Glass (Interactive):** Semi-transparent surfaces with a 12px Backdrop Blur. 
4. **The Projection (Active):** UI elements that "glow." These do not use shadows; instead, they use an "Outer Glow" (drop shadow with 0px offset and high spread) in Amber or Crimson to simulate light emission.

Higher elevation is indicated by increased border brightness and a stronger backdrop blur, making the element appear "closer" to the pilot's eyes.

## Shapes

The design system adopts a **Sharp (0px)** corner radius for all primary containers and data modules to reinforce the "technical instrument" aesthetic. 

Subtle exceptions:
- **Circular Indicators:** Used strictly for cyclical data (Oxygen levels, Scrubber status, Thruster rotation).
- **Beveled Edges:** Larger panels may use 45-degree chamfered corners instead of rounding to maintain a rugged, machined appearance.

## Components

### Technical Gauges
- **Vertical Depth Gauge:** A primary vertical scale on the left axis. The current depth is highlighted by a high-intensity Amber glow and a horizontal needle. 
- **Circular Progress (Oxygen):** A 270-degree ring. The stroke width is thick (12px) with a "ghost" track behind it. The color transitions from Amber to Crimson when levels drop below 15%.

### Camera Grids
- Video feeds are contained in Matte Black frames with ultra-thin Amber crosshairs centered on the feed. Metadata (ISO, Depth, Temp) is overlaid in the corners using `label-caps`.

### Controls & Inputs
- **Buttons:** Low-profile rectangles with an "Active Glow" state. There is no fill in the default state—only a border. Upon press, the button fills with a 10% Amber tint.
- **Critical Switches:** Require a "Slide to Confirm" interaction, styled as a horizontal track with a Crimson glow.

### Telemetry Lists
- Data rows use zebra-striping with subtle 2% opacity shifts. Each row is separated by a dotted 1px line to maintain horizontal eye-tracking across wide screens.