---
name: AvionicsSync
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#fff6ed'
  on-tertiary: '#412d00'
  tertiary-container: '#ffd58c'
  on-tertiary-container: '#7e5900'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdea8'
  tertiary-fixed-dim: '#ffba20'
  on-tertiary-fixed: '#271900'
  on-tertiary-fixed-variant: '#5e4200'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '300'
    lineHeight: '1.2'
  data-display:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '200'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 1px
  margin: 24px
  container-padding: 16px
---

## Brand & Style

The design system is engineered for mission-critical aerospace environments where cognitive load must be minimized and data legibility is paramount. It evokes the atmosphere of a modern glass cockpit—precise, technical, and high-stakes. The brand personality is authoritative and tactical, favoring functional utility over decorative flair.

The visual style is a fusion of **Technical Minimalism** and **Brutalism**. It relies on rigid structural grids, thin linework, and high-contrast optics. Every element serves a modular purpose, mimicking the instrumentation found in multi-function displays (MFDs). The UI is designed to feel like an illuminated overlay on a matte surface, prioritizing rapid scanning and error-free interaction.

## Colors

The color palette is strictly functional, utilizing a high-contrast dark mode to preserve night vision and reduce eye strain in low-light environments. 

- **Primary (Neon Cyan):** Reserved for active data, telemetry, and interactive states. It represents the "live" pulse of the system.
- **Secondary (Pure White):** Used for static labels, secondary data, and high-priority reading. 
- **Warnings (Amber):** Used for non-critical alerts, cautions, and status changes that require attention but not immediate action.
- **Critical (Red):** Exclusively for system faults and terminal errors. 
- **Background (Matte Black):** A deep, non-reflective base that allows neon accents to pop without causing chromatic aberration.

## Typography

This design system utilizes thin font weights to mimic the etched appearance of light-tube displays. 

- **Space Grotesk** is used for headlines and primary data readouts. Its geometric construction provides a technical, futuristic edge that remains legible at high speeds.
- **Inter** is the workhorse for body copy and system labels. It is utilized in its thinnest weights (100–300) to maintain the HUD aesthetic.

Text should be set with generous tracking for uppercase labels to ensure individual characters remain distinct even in vibrating or high-motion environments.

## Layout & Spacing

The layout is governed by a **Strict Fluid Grid**. The screen is treated as a single unified instrument panel, partitioned by 1px borders rather than negative space.

- **Grid:** A 12-column layout where elements are "locked" into their respective cells. 
- **Gutters:** 1px width, typically rendered as a visible dim-grey or cyan line to reinforce the structural integrity of the display.
- **Rhythm:** All margins and internal padding follow a 4px baseline shift. 

Avoid centering content; prioritize top-left alignment for tactical data density. Use semi-transparent overlays (background-blur is not required, only alpha transparency) to stack information without losing sight of the underlying system state.

## Elevation & Depth

This design system rejects the concept of shadows and organic depth. Hierarchy is established through **Tonal Layering** and **Luminance**.

1.  **Base Layer:** The Matte Black foundation.
2.  **Structural Layer:** 1px borders that define containers and data modules.
3.  **Active Layer:** Elements with a 1px Neon Cyan border and a subtle exterior glow (0px blur, 1-2px spread) suggest focus or "on" status.
4.  **Overlay Layer:** Semi-transparent black surfaces (85-90% opacity) that sit on top of the base layer for transient information like menus or modal alerts.

Depth is perceived as a stack of transparent glass plates rather than physical objects in a 3D space.

## Shapes

The shape language is strictly **Sharp (0px)**. 

Every component—from buttons to cards to input fields—must feature hard 90-degree angles. This reinforces the tactical, military-grade nature of the interface. In rare cases where a "corner cut" is needed for specialized data indicators, use a 45-degree chamfer rather than a radius. Icons should also follow a rigid, stroke-based construction with no rounded caps or joins.

## Components

### Buttons
Buttons are 1px outlined rectangles. In their default state, they use White or Cyan text. In the active or "pressed" state, the background fills with 20% Cyan opacity, and the border gains a 1px glow. Avoid solid fills unless it is a critical "Action" button.

### Input Fields
Inputs consist of a 1px bottom border or a full 1px box. The cursor is a solid Cyan block. Technical units (e.g., knots, alt, mhz) should be permanently visible as right-aligned labels within the field using the `label-caps` style.

### Lists & Data Tables
Lists are separated by 1px horizontal lines. Each row should have a "hover" state that activates a thin Cyan bracket on the left and right edges. 

### Chips & Status Tags
Small, rectangular containers with high-contrast text. Use the Amber palette for "STANDBY" and Red for "FAULT." Active statuses use Cyan with a "pulse" animation on the border.

### Tactical HUD Overlays
Use crosshairs, bracketed corners, and coordinate pips to frame critical data points. These elements are non-interactive but provide visual anchors for the eye in high-density data views.