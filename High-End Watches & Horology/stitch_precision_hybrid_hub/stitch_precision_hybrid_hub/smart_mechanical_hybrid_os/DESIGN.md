---
name: Smart-Mechanical Hybrid OS
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
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#fff5de'
  on-tertiary: '#3b2f00'
  tertiary-container: '#fed639'
  on-tertiary-container: '#715d00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffe179'
  tertiary-fixed-dim: '#eac324'
  on-tertiary-fixed: '#231b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-data:
    fontFamily: Space Mono
    fontSize: 42px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-nav:
    fontFamily: Hanken Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-tech:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
  nav-item:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  safe-area: 12%
---

## Brand & Style

This design system explores the intersection of high-horology and deep-space instrumentation. It is designed for a sophisticated, tech-forward audience that values precision, legibility, and a sense of "instrument-grade" quality. The brand personality is cold, calculating, and premium—evoking the feeling of a spacecraft cockpit or a high-end mechanical timepiece.

The UI style is a fusion of **Glassmorphism** and **Technical Brutalism**. It utilizes translucent layers to simulate sapphire crystal depth, while maintaining a rigid, grid-based structure that suggests mechanical reliability. Visual interest is driven by "scanning" grid overlays and subtle glowing accents that mimic illuminated instrumentation.

## Colors

The palette is strictly limited to maintain a high-contrast, technical aesthetic. 

- **Deep Space Black (#050505)**: The foundation. Used for the base background to ensure infinite depth and battery efficiency on OLED displays.
- **Neon Cyan (#00F0FF)**: The primary functional color. It denotes active states, data progression, and critical interactive elements. It should be applied with a subtle outer glow to simulate emissive light.
- **Crisp White (#FFFFFF)**: Used for high-legibility labels, primary navigation, and mechanical tick marks.
- **Surface Accent (#1A1A1A)**: Used for glass containers and segmented bars to provide subtle separation from the pure black background.

## Typography

This design system uses a dual-font strategy to differentiate between "System Intelligence" and "User Interaction."

**Hanken Grotesk** is the navigation anchor. It provides a clean, sans-serif clarity for menus, settings, and descriptive text. It is modern, professional, and balances the technicality of the interface with human-readable warmth.

**Space Mono** is the data engine. All numerical readouts, timestamps, sensor data, and technical labels must use this monospaced font. It reinforces the mechanical precision of the watch and ensures that vertical alignment of changing numbers remains stable during high-frequency updates.

## Layout & Spacing

The layout is governed by a **Circular Fixed Grid** optimized for watch face hardware. 

- **Concentric Alignment**: Information is organized in circular rings. The outermost ring (the "Safe Area") is reserved for mechanical tick marks and hardware-aligned indicators.
- **The Central Axis**: Primary data points (time, heart rate) are centered.
- **Segmented Layouts**: When displaying lists or settings, the layout uses a 4px-based vertical rhythm with 16px gutters.
- **Safe Area**: A 12% margin is enforced at the screen edges to account for physical bezels or screen curvature.

## Elevation & Depth

Depth is achieved through **Glassmorphism and Emissive Lighting** rather than traditional shadows.

- **The Base Layer**: Pure #050505 black.
- **The Glass Layer**: Semi-transparent containers (#FFFFFF at 5-10% opacity) with a 20px backdrop blur. These "float" above the base layer.
- **The Grid Overlay**: A subtle 1px cyan grid with 5% opacity sits behind the data but above the glass, creating a "HUD" (Heads-Up Display) effect.
- **Glow Borders**: Interactive or active elements feature a 1px #00F0FF border with a 4px blurred outer glow (drop-shadow with 0 offset).
- **Scanning Line**: A vertical or horizontal gradient line (Cyan, 10% opacity) occasionally pans across the interface to suggest active background processing.

## Shapes

The design system utilizes **Sharp (0px)** geometry for structural elements and **Perfect Circles** for data indicators. 

- **Structural Elements**: Rectangular buttons and containers use 90-degree corners to emphasize the "mechanical" and "industrial" nature of the tech.
- **Circular indicators**: Progress rings, dial complications, and secondary trackers must be mathematically perfect circles.
- **Beveling**: Where depth is required, use 45-degree chamfered corners on buttons to mimic machined metal parts.

## Components

### Circular Progress Rings
Data is primarily visualized through concentric rings. Use a 2px stroke for secondary data and a 4px stroke for primary goals. The "track" should be #1A1A1A, while the "progress" is #00F0FF with a glowing cap.

### Segmented Bars
For battery and signal strength, use segmented bars (linear or curved). Each segment is a sharp rectangle or arc, separated by a 2px gap. Active segments glow cyan; inactive segments remain dark grey.

### Technical Data Readouts
Readouts must include a "label" (Space Mono, Caps, 10px) and a "value" (Space Mono, 24px-42px). Readouts should be bracketed by subtle L-shaped "corner marks" to simulate a viewfinder.

### Buttons
Buttons are strictly rectangular or chamfered. They feature a 1px cyan border and a glass background. On press, the background fill increases to 20% opacity and the border glow intensifies.

### Lists
List items are separated by thin 1px horizontal lines with a subtle gradient (Transparent -> White 20% -> Transparent). Navigation icons should be minimal, high-stroke-weight glyphs in White.

### Scanning Indicators
A slow-pulsing 1px ring or line that moves across the interface to denote "Searching" or "Measuring" states.