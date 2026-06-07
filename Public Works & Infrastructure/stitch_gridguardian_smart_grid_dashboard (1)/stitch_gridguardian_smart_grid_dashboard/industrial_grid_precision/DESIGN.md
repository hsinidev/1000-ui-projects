---
name: Industrial Grid Precision
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#b0c6ff'
  on-secondary: '#002d6f'
  secondary-container: '#568dff'
  on-secondary-container: '#002661'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#999796'
  on-tertiary-container: '#302f2f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#d9e2ff'
  secondary-fixed-dim: '#b0c6ff'
  on-secondary-fixed: '#001945'
  on-secondary-fixed-variant: '#00429c'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  data-display:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
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
  gutter: 16px
  margin: 24px
  container-max: 1440px
  density-compact: 8px
  density-comfortable: 16px
---

## Brand & Style

This design system is engineered for mission-critical reliability and high-velocity decision-making. It adopts an **Industrial-Technical** style, blending the stark functionality of **Minimalism** with the high-visibility cues of **Bold/High-Contrast** aesthetics. 

The personality is authoritative and precise, designed to instill a sense of absolute control over complex infrastructure. Every element prioritizes data density and legibility, catering to technical professionals who manage smart city energy grids. The emotional response is one of safety and technological sophistication—reassuring the user that even the most complex systems are structured, monitored, and stable.

## Colors

The palette is anchored by **Charcoal (#1A1A1A)**, providing a deep, low-fatigue background for long-duration monitoring. **Safety Orange (#FF6700)** serves as the primary action and alert color, leveraging its industrial association with caution and high importance to draw immediate attention to critical UI states. 

**Electric Blue (#0070FF)** is utilized for data visualization, active telemetry, and secondary accents, representing the flow of energy and digital intelligence. The neutral scale consists of desaturated slates and cool greys to maintain technical clarity without introducing visual noise. All color combinations are strictly checked for AA/AAA contrast ratios to ensure maximum visibility in industrial environments.

## Typography

This design system employs a dual-font strategy. **Inter** is the workhorse for all body copy and prose, chosen for its exceptional readability and neutral, systematic tone. **Space Grotesk** is used for headlines, labels, and technical data displays; its geometric, futuristic qualities reinforce the platform’s technologically advanced nature.

Data-heavy displays use the "data-display" and "label-caps" styles to ensure that metrics, coordinates, and energy readings are distinct from standard interface text. Letter spacing is slightly increased on labels to ensure legibility even at small sizes or on lower-resolution industrial displays.

## Layout & Spacing

The layout follows a **Fluid Grid** model with high-density configuration options. A 12-column grid system is used for primary dashboard structures, with a focus on maximizing screen real estate. The spacing rhythm is based on a **4px base unit**, allowing for granular control over information density.

For monitoring views, the system defaults to "compact" spacing (8px) to fit more data points on a single screen. For administrative or setup screens, "comfortable" spacing (16px) is utilized. Large-scale data visualizations should span multiple columns, while status indicators are grouped in tight clusters for rapid scanning.

## Elevation & Depth

To maintain a professional and technical feel, this design system avoids soft, naturalistic shadows. Instead, it uses **Tonal Layers** and **Bold Outlines**. 

- **Surface 0:** The base Charcoal layer.
- **Surface 1:** Elevated cards and containers using a slightly lighter grey (#262626) with a 1px solid border (#333333).
- **Surface 2:** Popovers or modal windows with a high-contrast border in Electric Blue or Safety Orange to indicate focus.

A "glowing" effect is reserved exclusively for critical status indicators or active data points, using a concentrated outer glow of the primary or secondary color to simulate high-energy LEDs on physical hardware.

## Shapes

The shape language is strictly **Soft (0.25rem)**. This slight rounding suggests precision engineering—similar to the chamfered edges of industrial machinery—without compromising the professional, rigid feel of the platform. Buttons and input fields use the base 4px radius, while larger containers (like cards) may use 8px (rounded-lg) to create clear visual containment. Full-pill shapes are forbidden to avoid an overly "consumer" or "playful" appearance.

## Components

### Buttons
- **Primary:** Solid Safety Orange with black text. High visibility for core actions.
- **Secondary:** Outlined Electric Blue with blue text. For navigation or data filtering.
- **Ghost:** Minimalist text buttons for secondary controls within high-density lists.

### Cards & Containers
- High-contrast containers with 1px borders. 
- Header areas in cards should use a darker sub-fill to separate metadata from the content area.
- Critical cards (alerts) feature a 4px thick left-accent border in Safety Orange.

### Status Indicators
- **Glow-LED:** A small circular indicator with a neon glow effect to show live connectivity or power flow.
- **Safety Badge:** High-contrast labels with heavy borders for "ACTIVE," "OFFLINE," or "ALARM" states.

### Data Inputs
- Input fields use Charcoal backgrounds with a 1px Grey-700 border that glows Electric Blue on focus.
- Monospaced fonts (Space Grotesk) are used for numerical input fields to ensure digit alignment.

### Data Visualizations
- Line charts use 2px Electric Blue strokes with no fill to maintain clarity.
- Critical thresholds are marked with dotted Safety Orange lines.