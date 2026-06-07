---
name: Rugged-Luxe Technical System
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#46352e'
  surface-container-lowest: '#170b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362620'
  surface-container-highest: '#42312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#b9c9d5'
  on-secondary: '#23323c'
  secondary-container: '#3c4b55'
  on-secondary-container: '#abbbc7'
  tertiary: '#c8c6c7'
  on-tertiary: '#303031'
  tertiary-container: '#999798'
  on-tertiary-container: '#303031'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#d5e5f1'
  secondary-fixed-dim: '#b9c9d5'
  on-secondary-fixed: '#0e1d26'
  on-secondary-fixed-variant: '#3a4953'
  tertiary-fixed: '#e5e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474647'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#42312a'
typography:
  display-lg:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
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
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 40px
  container-max: 1440px
---

## Brand & Style

This design system targets high-end expedition professionals who require the precision of a laboratory instrument with the durability of tactical gear. The brand personality is "Indestructible Sophistication"—a fusion of raw utilitarianism and luxury engineering.

The visual style is a hybrid of **High-Contrast Tactical** and **Glassmorphism**. It utilizes deep, matte surfaces to ground the experience, while technical glass layers provide depth and a sense of "heads-up display" (HUD) intelligence. A signature "Energy Flow" element uses glowing, kinetic lines to represent data movement or battery life, ensuring the interface feels alive and responsive to real-time environmental telemetry.

## Colors

The palette is anchored in high-visibility functionality. 
- **Matte Black (#1A1A1B)** serves as the primary canvas, reducing glare and maximizing contrast for outdoor legibility. 
- **Charcoal (#36454F)** is used for elevated containers and interactive surfaces, providing a subtle tonal shift from the background. 
- **Safety Orange (#FF6700)** is reserved strictly for primary actions, critical alerts, and active states, mimicking the high-visibility markers found on expedition hardware.
- **Flow Accents**: A secondary, more luminous orange gradient is used for "Energy Flow" lines to indicate active processes and data streams.

## Typography

Typography functions as a data readout. **JetBrains Mono** is employed for headlines, labels, and numeric data to reinforce the "precision instrument" aesthetic, ensuring characters are distinct and legible in low-light or high-vibration scenarios. **Inter** provides a highly legible, neutral foundation for long-form technical descriptions and body content.

All labels should utilize uppercase styling with increased letter spacing to emulate etched serial numbers on hardware. Headings should be kept concise. Numerical data should always use the monospaced font to prevent "jumping" during real-time value updates.

## Layout & Spacing

This design system utilizes a **Fixed Grid** within a fluid container. A strict 4px baseline grid ensures every element feels engineered rather than "placed." 

- **Desktop**: 12-column grid with 24px gutters. Content is centered with wide margins to create a focused "cockpit" feel.
- **Tablet**: 8-column grid with 16px gutters.
- **Mobile**: 4-column grid with 16px margins. 

Layouts should prioritize vertical density for data-heavy views, using "staggered" modularity to separate different sensor readouts or equipment statuses. High-priority telemetry should occupy the top-left quadrant or the center-focus "HUD" area.

## Elevation & Depth

Depth is achieved through **Technical Layering** rather than traditional soft shadows. 

1. **Floor (Level 0)**: Matte Black (#1A1A1B) base surface.
2. **Plates (Level 1)**: Charcoal (#36454F) containers with a 1px inner stroke of 10% white to create a "milled edge" effect.
3. **Glass (Level 2)**: For overlays or modal elements, use Charcoal with 60% opacity and a 20px backdrop blur. 
4. **Energy Flow**: "Flow" lines sit on Level 1.5, appearing to move beneath the glass layers but above the base plates. Use an outer glow (0px 0px 8px) in Safety Orange to simulate luminosity.

Avoid drop shadows. Use high-contrast borders and tonal shifts to define hierarchy.

## Shapes

The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to maintain a rugged, machined-tool aesthetic. 

Structural elements should use 45-degree chamfered corners on decorative accents or primary action buttons to reinforce the "ruggedized hardware" theme. All borders, dividers, and container edges must be crisp and pixel-perfect.

## Components

- **Primary Buttons**: Solid Safety Orange background with Matte Black typography. No rounded corners. Hover state: add a subtle orange outer glow.
- **Secondary Buttons**: Charcoal background with a 1px Safety Orange border.
- **Input Fields**: Matte Black background with a 1px Charcoal border. On focus, the border changes to Safety Orange with a glowing "Flow" line underneath the field.
- **Telemetry Chips**: Small, high-contrast labels with JetBrains Mono. Use Charcoal backgrounds with Orange text for "Active" states.
- **Data Cards**: Charcoal surfaces with 1px milled edges. Headers are separated by a 1px horizontal line.
- **Flow Indicators**: Kinetic linear progress bars that use a pulsing orange gradient to indicate data transmission or energy consumption.
- **Status Lights**: Small square indicators (4x4px). Steady for "OK," pulsing for "Warning," and rapid-flash for "Critical."