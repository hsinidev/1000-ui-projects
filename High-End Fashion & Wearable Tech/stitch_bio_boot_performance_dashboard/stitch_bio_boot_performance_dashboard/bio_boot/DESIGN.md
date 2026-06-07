---
name: Bio-Boot
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
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#ffffff'
  on-secondary: '#003737'
  secondary-container: '#00fbfb'
  on-secondary-container: '#007070'
  tertiary: '#b9c9d5'
  on-tertiary: '#23323c'
  tertiary-container: '#8999a5'
  on-tertiary-container: '#22313b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#00fbfb'
  secondary-fixed-dim: '#00dddd'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#d5e5f1'
  tertiary-fixed-dim: '#b9c9d5'
  on-tertiary-fixed: '#0e1d26'
  on-tertiary-fixed-variant: '#3a4953'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.05em
spacing:
  base: 8px
  gutter: 16px
  margin: 20px
  panel-padding: 12px
  stack-gap: 4px
---

## Brand & Style

The design system is engineered for high-stakes industrial environments and biometric telemetry. The brand personality is uncompromising, precise, and utilitarian, evoking the feeling of a ruggedized tactical interface or a heavy-machinery control panel. It prioritizes rapid data legibility and operational status over decorative aesthetics.

The visual style is a fusion of **Industrial Brutalism** and **Technical Precision**. It utilizes a high-contrast dark environment to reduce eye strain in low-light industrial settings while using aggressive accent colors to highlight critical warnings and pressure points. Every element is designed to feel like a physical component—latched, bolted, or etched into the interface.

## Colors

The palette is anchored in a deep **Matte Black (#1A1A1A)** base to provide maximum contrast for data visualization. **Charcoal (#36454F)** acts as the secondary surface color, used to define structural containers and "etched" UI panels.

**Safety Orange (#FF6700)** is the primary action and alert color, serving as the "high-pressure" end of the visual spectrum. **Cyan (#00FFFF)** is introduced as the "low-pressure" or "stable" counter-point, creating a high-energy heatmap effect when used in data visualizations. Functional colors for success, warning, and danger should lean into the safety orange and cyan extremes, with white reserved exclusively for high-priority alphanumeric readouts.

## Typography

This design system utilizes a dual-font strategy to balance technical density with reading stamina. **JetBrains Mono** is the primary typeface for all technical data, headers, and UI labels, emphasizing the monospaced "code-like" precision of the interface. 

**Inter** is employed for long-form descriptions or instructional body text where variable-width characters improve rapid scanning. All labels should be treated as "tags," often appearing in all-caps with increased letter spacing to mimic industrial stamping. Data displays utilize a specialized heavy weight to ensure critical numbers are legible from a distance.

## Layout & Spacing

The layout philosophy follows a **Rigid Modular Grid**. Elements are treated as self-contained blocks that "slot" into the interface. On mobile, the system uses a single-column stack with horizontal scrolling for high-density data tables.

A strict 8px rhythmic spacing system is enforced. To emphasize the industrial aesthetic, use "Technical Borders"—1px solid lines—to separate sections rather than whitespace. Padding within components is kept tight to maximize information density, while gutters between major modules are kept wide to prevent critical data clusters from bleeding into one another.

## Elevation & Depth

In this design system, depth is conveyed through **Tonal Stacking** and **Inner Radiance** rather than traditional shadows. 
- **Base Level:** Matte Black (#1A1A1A) represents the background "chassis."
- **Level 1 (Panels):** Charcoal (#36454F) surfaces with a 1px solid border in a lighter tint of Charcoal or Safety Orange.
- **Active State:** Elements gain a 2px outer "glow" (Safety Orange) and an inner subtle "scanline" texture.

Avoid soft ambient shadows. Use high-contrast outlines and "Inset" bevel effects (1px highlights on top and left edges) to create a mechanical, recessed look.

## Shapes

The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to maintain a rugged, machined appearance. Exceptions are made only for "Status Pips" (circular indicators) which must be perfect circles to contrast against the otherwise rectilinear grid.

Structural elements should feature "Chamfered" corners (clipped at 45 degrees) for primary call-to-action buttons or header tabs, reinforcing the industrial manufacturing aesthetic.

## Components

### Buttons
Buttons are rectangular with 0px radius. The primary action button is solid Safety Orange with black monospaced text. Secondary buttons feature a Charcoal background with a 1px Safety Orange border. All buttons should have a "pressed" state that inverts the colors or adds a flickering "glow" effect.

### Input Fields
Inputs are recessed Charcoal blocks with a bottom-only 2px border in Safety Orange. The cursor should be a solid orange block, mimicking a terminal interface.

### Heatmaps & Gauges
Data visualizations utilize a "Pressure-Point" gradient. Stable data is Cyan; as values reach critical thresholds, they transition through white and finally into a pulsating Safety Orange. Use "stutter" animations (stepped transitions) rather than smooth fades.

### Technical Borders
All containers must feature 1px borders. For active containers, add "Corner Brackets"—L-shaped accents at the four corners—to simulate a targeting reticle or a mounted hardware component.

### Chips & Tags
Used for status monitoring. They should resemble "LED Indicators," consisting of a small circular pip next to a monospaced label, encased in a high-contrast border.