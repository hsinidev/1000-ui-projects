---
name: Aerospace Industrial
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e4e2e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#fbf7f8'
  on-tertiary: '#313031'
  tertiary-container: '#dedbdc'
  on-tertiary-container: '#616061'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1c1b1c'
  on-tertiary-fixed-variant: '#474647'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353437'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  data-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  grid-overlay-size: 40px
---

## Brand & Style

This design system is engineered for mission-critical environments where precision and rapid data processing are paramount. The brand personality is authoritative, cold, and hyper-functional, drawing heavy influence from aerospace telemetry and modern cockpit interfaces. 

The aesthetic is a hybrid of **Industrial Minimalism** and **High-Contrast HUD** design. It prioritizes information density without sacrificing clarity. Visual interest is generated through light—specifically neon luminescence—against an obsidian void, simulating the experience of a pilot or specialized technician monitoring high-stakes systems in deep space. Every element must feel intentional, calibrated, and necessary.

## Colors

The palette is strictly functional, utilizing a high-contrast dark mode foundation. 

- **Deep Space Black (#0A0A0B):** The primary surface color, used to eliminate visual noise and provide infinite depth.
- **Neon Cyan (#00F3FF):** The primary action and "active system" color. It represents energy, data flow, and interactive states.
- **Pure White (#FFFFFF):** Reserved for primary labels and high-priority data points to ensure maximum legibility.
- **Support Tones:** Semantic colors for error, warning, and success are desaturated until active, at which point they utilize the same glow intensity as the primary cyan.

## Typography

The typography strategy employs a dual-font system to distinguish between interface controls and raw telemetry.

- **UI/Headlines (Hanken Grotesk):** A sharp, contemporary sans-serif used for structure and navigation. Headlines should use uppercase styling sparingly for section headers to maintain an "official" tone.
- **Data/Monospace (JetBrains Mono):** Used for all dynamic values, coordinates, timestamps, and technical readouts. The fixed-width nature ensures that fluctuating numbers do not cause layout shifts, maintaining the "precision instrument" feel.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model based on a 4px baseline shift. 

- **Grid Overlay:** A subtle, 5% opacity cyan grid should be visible in the background of main content areas, mimicking a drafting board or radar screen.
- **Modular Blocks:** Content is housed in "Modules." These modules should be separated by 16px or 24px gutters.
- **Data Density:** Spacing within components is tight (8px to 12px) to maximize the amount of information visible at a single glance. 
- **Responsive Behavior:** On mobile, the 12-column desktop grid collapses to a 4-column vertical stack, but the grid overlay remains constant in scale to suggest the user is "panning" across a larger instrument panel.

## Elevation & Depth

Depth is conveyed through **chromatic layering** rather than traditional shadows.

- **Base Layer:** Deep Space Black (#0A0A0B).
- **Floor Grid:** The 5% Neon Cyan grid overlay provides the initial sense of scale.
- **Container Layer:** Modules are defined by 1px solid borders (#1A1A1C). 
- **Interactive Elevation:** When an element is focused or active, it does not "rise" toward the user; instead, it "powers on." This is achieved through a 1px Neon Cyan border and a subtle outer glow (`box-shadow: 0 0 12px rgba(0, 243, 255, 0.4)`).
- **Scanning Effects:** Use horizontal "scan lines" (semi-transparent gradients) on larger panels to imply active data processing.

## Shapes

The shape language is strictly **Geometric and Sharp**. 

- **Corners:** All corners are 90-degree angles (0px radius). This reinforces the industrial, machined aesthetic.
- **Angle Accents:** Where visual interest is needed, use "clipped" corners (45-degree chamfers) at 4px or 8px on buttons or status indicators to mimic aerospace hardware.
- **Line Weight:** Borders must consistently remain at 1px. Thicker lines are reserved only for structural dividers or progress bars.

## Components

- **Buttons:** Rectangular with 1px borders. Default state is a White border; Hover/Active state is a Cyan border with a matching text glow. No solid backgrounds except for "Critical" actions, which use a solid Cyan background with Black text.
- **Inputs:** Underlined or fully boxed in 1px borders. Include a "bracket" detail at the corners to emphasize the frame. Use monospaced font for input text.
- **Cards/Modules:** Must include a "Header" area with a label in `label-caps`. Often includes a small "ID number" in the top right corner for added realism.
- **Iconography:** Use "Stroke" icons only. Icons should be technical and skeletal, avoiding filled shapes. Use 1px line weights to match the UI borders.
- **Telemetry Visuals:** Progress bars should be segmented (stepped) rather than smooth. Charts should use thin lines with small circular "nodes" at data points.
- **Status Indicators:** Small 8px squares. When "Online," they pulse with a Cyan glow. When "Error," they pulse Red.