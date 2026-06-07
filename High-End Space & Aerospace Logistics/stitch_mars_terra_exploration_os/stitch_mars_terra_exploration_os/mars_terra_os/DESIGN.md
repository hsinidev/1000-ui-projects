---
name: Mars-Terra OS
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
  on-surface-variant: '#e0c0b5'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a78a81'
  outline-variant: '#58423a'
  surface-tint: '#ffb59c'
  primary: '#ffb59c'
  on-primary: '#5c1a00'
  primary-container: '#b7410e'
  on-primary-container: '#ffe2d9'
  inverse-primary: '#a93702'
  secondary: '#e1c299'
  on-secondary: '#402d10'
  secondary-container: '#5b4526'
  on-secondary-container: '#d2b48c'
  tertiary: '#abcdcd'
  on-tertiary: '#143535'
  tertiary-container: '#4e6e6e'
  on-tertiary-container: '#ccefef'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59c'
  on-primary-fixed: '#380c00'
  on-primary-fixed-variant: '#822800'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#c6e9e9'
  tertiary-fixed-dim: '#abcdcd'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#2c4c4c'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-mono-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 24px
  data-mono-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  panel-padding: 24px
---

## Brand & Style

This design system is engineered for long-range planetary exploration, prioritizing survival-critical information and hardware-software integration. The brand personality is **Earthy-Rugged** and **Authoritative**, evoking the feeling of a field-tested tool that has weathered Martian dust storms and extreme temperature fluctuations.

The visual style is a fusion of **Tactile/Skeuomorphism** and **Brutalism**. It avoids the polished, fragile aesthetic of consumer electronics in favor of "Rough-Material" textures, simulated physical toggles, and heavy structural reinforcements. The UI should feel like it is etched into or projected onto ruggedized hardware, providing a sense of permanence and reliability in a hostile environment.

## Colors

The color palette is grounded in the Martian landscape and industrial utility.

- **Primary (Rust Red - #B7410E):** Reserved for high-priority status indicators, critical alerts, and active mission paths. It represents the planetary surface and urgent communication.
- **Secondary (Sand - #D2B48C):** Used for primary UI text, icons, and interactive elements. It provides a natural, high-legibility contrast against dark backgrounds.
- **Tertiary (Dark Slate - #2F4F4F):** Utilized for secondary data, non-critical telemetry, and structural accents. It provides a cool, technical balance to the warmer tones.
- **Neutral (Deep Charcoal - #1A1A1A):** The foundation for all interface surfaces. It minimizes light pollution in low-visibility environments and reduces eye strain during long-range shifts.

The system uses a high-contrast ratio to ensure visibility through visor HUDs or dust-coated displays.

## Typography

The typography system differentiates between operational UI and telemetry data. 

**Space Grotesk** is the primary typeface for headers and body text. Its geometric yet industrial nature provides the "rugged" look required for Martian OS operations while maintaining modern legibility.

**JetBrains Mono** is utilized for all "Mission Critical Data"—telemetry, coordinates, oxygen levels, and technical logs. The monospaced nature ensures that fluctuating digits do not cause layout shifts, allowing for precise, rapid monitoring. All labels and technical data points should be rendered in uppercase to emphasize the authoritative, military-spec nature of the system.

## Layout & Spacing

This design system employs a **Fixed, Modular Grid** resembling the compartmentalized bulkheads of a spacecraft. The spacing rhythm is tight and efficient, maximizing data density without sacrificing clarity.

- **Grid Model:** A 12-column grid for desktop with 16px gutters. Elements are often "slapped" into rigid, heavy-bordered panels.
- **Breakpoints:** 
    - Mobile (0-599px): 4 columns, minimal margins, full-width data modules.
    - Tablet (600-1199px): 8 columns, side-car navigation panels.
    - Desktop (1200px+): 12 columns, persistent telemetry sidebar and central operation stage.
- **Philosophy:** Components should feel bolted together. Negative space is used sparingly, primarily to separate distinct functional zones (e.g., Life Support vs. Navigation).

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layering** and **Heavy Outlines** rather than soft shadows. 

1.  **Base Surface:** Deep Charcoal (#1A1A1A) with a subtle "noise" or "grit" texture.
2.  **Panels/Containers:** Slightly lighter Dark Slate (#2F4F4F) with 2px solid borders in Sand (#D2B48C).
3.  **Active Elements:** Outlined with high-contrast Rust Red (#B7410E) or Sand, giving them a "raised" appearance through visual prominence.
4.  **Weathering:** Distressed edges and "scuff" overlays are applied to container corners to simulate wear on physical hardware interfaces.

No ambient shadows are permitted; all depth is "mechanical" and structural.

## Shapes

The shape language is strictly **non-geometric and sharp**. To reflect hardware integration, corners use 0px roundedness or diagonal "clipped" chamfers.

- **Chamfered Edges:** Instead of rounded corners, use 45-degree angled cuts on the corners of cards and buttons to evoke machined metal.
- **Organic Distortions:** Status indicators and data visualizations may use "rough" edges or jagged lines to simulate analog signal interference or weathered physical plates.
- **Heavy Borders:** Every major container must feature a minimum 2px border, reinforcing the "mission-critical" containment of data.

## Components

- **Buttons:** Rectangular with 2px borders. The default state is a Dark Slate background with Sand text. The "Active" state is Rust Red with high-contrast Sand text. Buttons should include "bracket" icons `[ ]` at the corners to signify touch targets.
- **Telemetry Chips:** Small, monospaced data blocks with a solid Sand background and Charcoal text. Used for status tags like `[ O2: OK ]` or `[ RAD: HIGH ]`.
- **Lists:** Data-heavy, separated by 1px horizontal dividers. Each list item should have a "scanning" indicator (a small vertical bar) to show active updates.
- **Input Fields:** Styled like old-school terminal prompts. A subtle flickering cursor and underline-only border style emphasize the "command line" influence.
- **Cards:** Heavy-duty containers with "scuffed" texture overlays. Headers are visually separated by a solid horizontal bar in Rust Red.
- **Status Indicators:** High-contrast, glowing dots. "Critical" states should use a slow pulse animation in Rust Red to draw attention without being distracting.
- **Additional Components:**
    - **Topographic Maps:** Wireframe-style terrain renders using Sand lines on Charcoal backgrounds.
    - **Telemetry Gauges:** Radial or linear progress bars with segmented "notches" rather than smooth fills.