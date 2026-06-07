---
name: Lunar Habitat OS
colors:
  surface: '#f6f9ff'
  surface-dim: '#d6dae0'
  surface-bright: '#f6f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f4fa'
  surface-container: '#eaeef4'
  surface-container-high: '#e5e8ee'
  surface-container-highest: '#dfe3e9'
  on-surface: '#171c20'
  on-surface-variant: '#44474c'
  inverse-surface: '#2c3136'
  inverse-on-surface: '#edf1f7'
  outline: '#75777c'
  outline-variant: '#c5c6cc'
  surface-tint: '#555f6f'
  primary: '#0a1422'
  on-primary: '#ffffff'
  primary-container: '#1f2937'
  on-primary-container: '#8690a1'
  inverse-primary: '#bdc7d9'
  secondary: '#9d4300'
  on-secondary: '#ffffff'
  secondary-container: '#fd761a'
  on-secondary-container: '#5c2400'
  tertiary: '#00171f'
  on-tertiary: '#ffffff'
  tertiary-container: '#002d39'
  on-tertiary-container: '#249cbd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e3f6'
  primary-fixed-dim: '#bdc7d9'
  on-primary-fixed: '#121c2a'
  on-primary-fixed-variant: '#3d4756'
  secondary-fixed: '#ffdbca'
  secondary-fixed-dim: '#ffb690'
  on-secondary-fixed: '#341100'
  on-secondary-fixed-variant: '#783200'
  tertiary-fixed: '#b7eaff'
  tertiary-fixed-dim: '#6cd3f7'
  on-tertiary-fixed: '#001f28'
  on-tertiary-fixed-variant: '#004e61'
  background: '#f6f9ff'
  on-background: '#171c20'
  surface-variant: '#dfe3e9'
typography:
  display-critical:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  header-section:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1.2'
  data-point:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
  body-standard:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is engineered for mission-critical reliability in off-world environments. The aesthetic is defined as **Technical Utilitarian**, prioritizing rapid information processing and high legibility under the fluctuating lighting conditions of a lunar habitat. It avoids all decorative flourishes in favor of a sterile, functional interface that mirrors the precision of aerospace hardware.

The brand personality is cold, authoritative, and precise. It targets habitat engineers and mission commanders who require a zero-latency mental model of life-support systems, resource management, and structural integrity. The emotional response is one of controlled stability—intended to reduce cognitive load during high-stress operational anomalies.

## Colors

The palette is derived from the lunar environment and industrial safety standards.

*   **Lunar Grey (#D1D5DB):** The primary surface color. It provides a neutral, low-glare canvas that maintains visibility in both low-light and high-direct-light scenarios.
*   **Graphite (#1F2937):** Used for structural elements, primary headers, and high-density text. It provides the "anchor" for the UI, ensuring clear boundaries.
*   **Safety Orange (#F97316):** Reserved strictly for alerts, warnings, and critical status changes. It must be used sparingly to maintain its psychological impact.
*   **Technical Cyan (#0891B2):** The operational accent. It denotes active data streams, normal functioning status, and interactive navigational elements.

Color application must follow a high-contrast ratio to ensure accessibility through visor glare or environmental dust.

## Typography

The typography system utilizes two distinct typefaces to separate administrative content from technical data.

*   **Inter (Geometric Sans):** Utilized for structural UI, instructions, and primary headers. It provides a clean, modern clarity that remains legible at small scales.
*   **JetBrains Mono (Monospaced):** Utilized for all dynamic telemetry, coordinate systems, and operational logs. The fixed character width ensures that changing data values do not cause visual jitter in the layout.

All headers should lean towards heavy weights to establish a clear hierarchy against the grey background. Data points should prioritize the monospaced font to evoke a sense of machine-calculated precision.

## Layout & Spacing

This design system employs a **Fixed Modular Grid** based on a 4px base unit. 

*   **Grid Model:** A 12-column system for workstation displays, transitioning to a single-column stack for handheld diagnostic tablets.
*   **Modular Cards:** All content must be housed in modular containers. This allows the UI to be reconfigured based on the mission profile (e.g., swapping a Life Support module for a Navigation module).
*   **Gutters:** Consistent 16px gutters ensure that distinct data modules remain visually separated, even during rapid scanning.
*   **Information Density:** High. Use the 8px (sm) and 16px (md) spacing units for internal card padding to maximize the data visible on a single screen.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layering and Utilitarian Borders** rather than shadows. 

1.  **Base Layer:** Lunar Grey (#D1D5DB) represents the "floor" of the interface.
2.  **Intermediate Layer:** Graphite (#1F2937) containers used for headers or sidebars to provide deep structural contrast.
3.  **Active Layer:** Elements are highlighted with 1px or 2px solid borders using the Graphite or Technical Cyan colors.
4.  **No Shadows:** Light sources in a habitat are often artificial or harsh; ambient shadows are omitted to maintain the "flat-screen" technical readout aesthetic.

Depth is strictly functional: an element is "above" another only if it is an overlay (like an emergency override modal), indicated by a 2px Safety Orange border.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. 

Right angles reinforce the industrial, architectural nature of the habitat management software. Every button, card, and input field must utilize 90-degree corners. This evokes the feeling of panels bolted into a bulkhead. Beveled edges or "notched" corners may be used for specific "Action" buttons to distinguish them from data cards, but circular or rounded elements are prohibited to maintain the sterile, technical tone.

## Components

### Buttons
*   **Primary:** Solid Graphite background with Lunar Grey text. No rounded corners.
*   **Action:** Technical Cyan border (1px) with Monospaced text.
*   **Critical:** Solid Safety Orange background with Graphite text. Reserved for irreversible actions.

### Cards & Modules
All cards utilize a 1px Graphite border. Cards containing critical status updates feature a 4px "Emergency Protocol" header strip in Safety Orange. 

### Input Fields
Inputs are Lunar Grey with a 1px Graphite bottom-border only, mimicking technical forms. Focus state is indicated by a Technical Cyan bottom-border (2px).

### Emergency Protocol Styling
When a system failure occurs, the affected module triggers a "Hazard State." This includes a 45-degree diagonal stripe pattern in Safety Orange and Graphite for the header, and high-frequency flashing for the primary data point.

### Technical Readouts
Lists of telemetry should be displayed in monospaced font, aligned to a strict vertical axis. Use subtle Graphite horizontal dividers (0.5px) between rows to assist in horizontal scanning across wide data tables.