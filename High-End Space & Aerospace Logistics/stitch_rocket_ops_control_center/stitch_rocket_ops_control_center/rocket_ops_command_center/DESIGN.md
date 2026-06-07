---
name: Rocket-Ops Command Center
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#e4bdbb'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#303031'
  outline: '#ab8887'
  outline-variant: '#5c403f'
  surface-tint: '#ffb3b1'
  primary: '#ffb3b1'
  on-primary: '#680010'
  primary-container: '#d72638'
  on-primary-container: '#fff2f1'
  inverse-primary: '#bd0b29'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#707070'
  on-tertiary-container: '#f7f5f4'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b1'
  on-primary-fixed: '#410007'
  on-primary-fixed-variant: '#92001b'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e2'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  display-lg:
    fontFamily: Barlow Condensed
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Barlow Condensed
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  telemetry-lg:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.02em
  telemetry-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Barlow Condensed
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  body-standard:
    fontFamily: Barlow Condensed
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  display-lg-mobile:
    fontFamily: Barlow Condensed
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
spacing:
  unit: 4px
  gutter-desktop: 16px
  margin-desktop: 24px
  gutter-mobile: 8px
  margin-mobile: 12px
  container-max: 1920px
---

## Brand & Style

The design system is engineered for high-stakes aerospace operations where split-second decisions and data density are paramount. The personality is unapologetically technical, cold, and efficient—evoking the interior of a pressurized cockpit or a launch control room. 

The aesthetic leverages **Industrial Minimalism** mixed with **Brutalist** structural elements. It prioritizes function over form, utilizing heavy borders, visible grid lines, and high-contrast telemetry to ensure legibility under stress. This is a mission-critical environment where visual "fluff" is eliminated in favor of raw data and actionable alerts. The UI should feel like a physical instrument panel: rugged, reliable, and precise.

## Colors

The palette is restricted to a high-contrast tri-color scheme to minimize cognitive load and highlight critical path information.

- **Deep Graphite (#1A1A1B):** The non-reflective base for all surfaces. It mimics the matte finish of aerospace hardware.
- **Signal Red (#D72638):** Reserved exclusively for primary calls to action, active states, and critical system alerts. Its usage must be intentional to maintain its "emergency" psychological impact.
- **Stark White (#FFFFFF):** Used for primary telemetry, data points, and labels. It provides maximum contrast against the graphite base.
- **Surface Accents (#2A2A2B / #4A4A4A):** Sub-layers and borders use muted variations of graphite to define structure without breaking the dark-mode immersion.

## Typography

This design system utilizes a dual-font strategy to distinguish between UI controls and system data.

1.  **UI & Navigation:** **Barlow Condensed** provides a rugged, industrial sans-serif feel. Its narrow width allows for high information density in sidebars and headers. Use All-Caps for labels and headers to reinforce the "instrument panel" look.
2.  **Telemetry & Data:** **JetBrains Mono** is used for all dynamic values, coordinates, and status readouts. The monospaced nature ensures that jumping numbers do not cause layout shifts and that vertical columns of data remain perfectly aligned.

All headings should be treated with tight line heights and slight tracking increases for a technical, documented appearance.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy within a modular framework. 

- **Desktop:** A 12-column grid with a 16px gutter. Panels are treated as "Modules" that can be pinned or expanded. Margin-heavy layouts are avoided; content should feel packed and efficient.
- **Mobile:** A 4-column grid with 8px gutters. Layouts reflow into a single vertical "Stream of Status," prioritizing the most critical Signal Red alerts at the top.
- **Rhythm:** All spacing must be a multiple of 4px. Use "Micro-spacing" (4px, 8px) for internal module components and "Macro-spacing" (16px, 24px) for layout sections.

Visible grid lines (1px width, #2A2A2B) should be used to separate main layout regions, mimicking technical schematics.

## Elevation & Depth

This system avoids traditional shadows to maintain a flat, industrial aesthetic. Depth is communicated through **Tonal Layers** and **Structural Outlines**:

- **Level 0 (Base):** Deep Graphite (#1A1A1B). The "hull" of the application.
- **Level 1 (Modules):** A slightly lighter #222223 with a 1px solid border of #4A4A4A. 
- **Level 2 (Pop-overs/Modals):** These use the same base color but are differentiated by a high-contrast Stark White border (1px) and a solid black backdrop dimming effect (80% opacity).
- **Active State:** Elements do not "lift"; they glow or change color. An active module may have a Signal Red top-border (2px) to indicate focus.

## Shapes

The shape language is strictly **Sharp (0px)**. 

In a mission-critical industrial environment, rounded corners are seen as inefficient use of screen real estate and too "consumer-oriented." Every button, input field, and container must have 90-degree angles. To add technical character, 45-degree "clipped corners" (chamfers) may be used on primary action buttons or large module headers to evoke CNC-machined parts.

## Components

- **Buttons:** Primary buttons are solid Signal Red with Stark White text (Bold, Caps). Secondary buttons are Ghost-style with a 1px Stark White border.
- **Telemetry Cards:** Must feature a "Header" strip with a 12px Barlow Condensed label and a JetBrains Mono "Value" in the center. 
- **Status Indicators:** Small 8x8px squares. Signal Red (Critical), Stark White (Active), and 40% Opacity White (Standby/Off).
- **Inputs:** Stark White 1px border. On focus, the border thickens to 2px. The cursor should be a solid block rather than a line.
- **Data Tables:** High-density, no row banding. Use 1px #2A2A2B horizontal dividers. Column headers must be All-Caps Barlow Condensed.
- **Alert Banners:** Full-width Signal Red background with Stark White text. Use a pulsing animation (1s interval) for "System Failure" states.
- **Scrollbars:** Custom-styled to be ultra-thin (4px), non-rounded, in Stark White against the Graphite base.