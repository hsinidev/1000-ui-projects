---
name: Zenith-Hab OS
colors:
  surface: '#f3fbfb'
  surface-dim: '#d3dcdc'
  surface-bright: '#f3fbfb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#edf5f6'
  surface-container: '#e7eff0'
  surface-container-high: '#e1eaea'
  surface-container-highest: '#dce4e5'
  on-surface: '#151d1e'
  on-surface-variant: '#3b494b'
  inverse-surface: '#2a3233'
  inverse-on-surface: '#eaf2f3'
  outline: '#6a7a7b'
  outline-variant: '#b9cacb'
  surface-tint: '#006970'
  primary: '#006970'
  on-primary: '#ffffff'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#00dbe9'
  secondary: '#5f5e60'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfe1'
  on-secondary-container: '#636264'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#d9d9d9'
  on-tertiary-container: '#5d5f5f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e4e2e4'
  secondary-fixed-dim: '#c8c6c8'
  on-secondary-fixed: '#1b1b1d'
  on-secondary-fixed-variant: '#474649'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f3fbfb'
  on-background: '#151d1e'
  surface-variant: '#dce4e5'
typography:
  headline-lg:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.2em
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
  margin-mobile: 24px
  margin-desktop: 64px
  grid-columns: '12'
---

## Brand & Style

The design system is engineered for the elite inhabitants of a luxury orbital habitat. It balances the uncompromising precision of aerospace engineering with the serene, high-end comfort of a private sanctuary. The aesthetic is "Sterile-Futuristic"—a high-fidelity environment where clinical cleanliness meets cutting-edge technology.

The UI utilizes a "Liquid Glassmorphism" style: surfaces appear as hyper-polished, semi-transparent layers that seem to float within the station's pressurized environment. Visual density is high but meticulously organized through modular grids, evoking a sense of total control and absolute safety. The emotional response is one of calm, crystalline clarity, and technological omnipotence.

## Colors

This design system utilizes a high-key, clinical palette designed to maintain mental alertness and reflect the sterile environment of the station.

- **Clinical White:** The foundational background. It is not a pure #FFFFFF, but a slightly blue-tinted, crisp white that feels architectural.
- **Oxygen Blue:** A luminous, vibrant cyan used exclusively for active life-support systems, vitals, and primary interactions.
- **Charcoal:** Used for text and structural UI borders to provide deep contrast and groundedness.
- **Alert Tones:** Warning Amber and Critical Red are reserved strictly for 'Seal-Integrity' or hardware failures, ensuring immediate visual hijacking of the user's attention.
- **Circadian Shift:** The background temperature shifts from a cool 6500K (Day) to a warm 2700K (Night) tone, lowering the overall luminance to assist the crew's natural sleep cycles.

## Typography

The typography strategy emphasizes wide-set, geometric forms to suggest space and technological sophistication. 

- **Display & Headlines:** Sora is used for its wide proportions and futuristic geometry. It should be typeset with generous letter spacing to evoke a premium, airy feel.
- **Body & Content:** Hanken Grotesk provides a sharp, contemporary professional feel that remains legible in high-density data views.
- **Data Readouts:** JetBrains Mono is utilized for all telemetry, coordinates, and life-support metrics. It provides the "Precision UI" feel required for space-flight operations.

## Layout & Spacing

This design system employs a rigid 4px baseline grid and a 12-column modular layout. All spacing is derived from 4px increments to ensure mathematical precision across the interface.

- **Desktop:** A fixed-width container centered within the viewport, utilizing 64px margins. Content is organized into modular "pods."
- **Tablet/Onboard Terminals:** Fluid 12-column grid with 16px gutters to maximize information density on smaller mounted screens.
- **Mobile/Wearable:** A single-column flow with 24px side margins, optimized for one-handed operation during zero-G transit.

## Elevation & Depth

Hierarchy is achieved through "Tonal Stacking" rather than traditional heavy shadows. 

1. **Floor (Level 0):** Clinical White background, matte.
2. **Plates (Level 1):** Semi-transparent glass panels with a 20px backdrop blur and a 0.5px Charcoal stroke at 10% opacity.
3. **Active Elements (Level 2):** Elements with an inner-glow of Oxygen Blue to indicate focus or active processing.
4. **Floating Overlays (Level 3):** High-blur surfaces with a subtle drop shadow: `0px 20px 40px rgba(0,0,0,0.05)`.

This creates a sense of "suspended" interface components, mimicking the weightlessness of the environment.

## Shapes

The shape language is "Soft-Technical." While the layout is rigid and modular, corners are subtly softened to avoid a harsh, aggressive military look.

- **Standard Containers:** 0.25rem (4px) corner radius. This is the "Soft" setting, providing a precise but sophisticated edge.
- **Data Points:** Small circular pips are used for status indicators.
- **Buttons:** Follow the standard 4px radius, maintaining a structural, architectural appearance.

## Components

- **Buttons:** Primary buttons are outlined in 1px Charcoal with an Oxygen Blue glow on hover. Text is always uppercase JetBrains Mono for a command-line aesthetic.
- **Status Chips:** Small, pill-shaped indicators. "System OK" chips use a faint Oxygen Blue background; "Warning" chips use a high-contrast Amber pulse animation.
- **Cards/Pods:** Modular glass containers with thin, 0.5px borders. Headers are separated by a hairline divider.
- **Input Fields:** Minimalist underlines rather than boxes. On focus, the underline expands into an Oxygen Blue glowing bar.
- **Life Support Gauges:** Circular or linear progress bars using Oxygen Blue. The "glow" intensity should modulate slowly to mimic a breathing rhythm.
- **Telemetry Lists:** High-density rows with monospaced data on the right and Hanken Grotesk labels on the left, separated by a dotted leader line.