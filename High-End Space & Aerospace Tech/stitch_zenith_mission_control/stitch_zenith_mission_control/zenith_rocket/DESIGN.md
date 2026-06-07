---
name: Zenith-Rocket
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e7bdb9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#ae8884'
  outline-variant: '#5d3f3c'
  surface-tint: '#ffb3ad'
  primary: '#ffb3ad'
  on-primary: '#680009'
  primary-container: '#e61e2a'
  on-primary-container: '#fffeff'
  inverse-primary: '#c0001a'
  secondary: '#dcfdff'
  on-secondary: '#00373a'
  secondary-container: '#00f1fd'
  on-secondary-container: '#006a6f'
  tertiary: '#c4c7c3'
  on-tertiary: '#2d312e'
  tertiary-container: '#737773'
  on-tertiary-container: '#fefffb'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#410003'
  on-primary-fixed-variant: '#930011'
  secondary-fixed: '#6ff6ff'
  secondary-fixed-dim: '#00dce6'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f53'
  tertiary-fixed: '#e0e3df'
  tertiary-fixed-dim: '#c4c7c3'
  on-tertiary-fixed: '#181d1a'
  on-tertiary-fixed-variant: '#444844'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-point:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: -0.05em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 100%
  stack-compact: 8px
  stack-loose: 32px
---

## Brand & Style

This design system is engineered for the high-stakes environment of aerospace launch operations. The brand personality is aggressive, hyper-focused, and uncompromisingly precise. It targets elite flight controllers and mission specialists who require instantaneous data recognition under pressure.

The visual style is a fusion of **Industrial Brutalism** and **High-Contrast Tactical** design. It evokes a 'command center' atmosphere through a dark, immersive interface. Key aesthetic pillars include:
- **Precision Engineering:** Every element is aligned to a rigid grid, reflecting the mechanical certainty of aerospace hardware.
- **Urgency & Action:** High-octane Racing Red accents signal critical thresholds, while Neon Cyan represents the "live" pulse of the system.
- **Tactile Technicality:** Surfaces incorporate subtle scan-line textures and brushed metallic finishes to simulate physical hardware consoles.

## Colors

The palette is anchored by **Matte Black (#121212)** to minimize eye strain and maximize the pop of functional data. 

- **Racing Red (#E61E2A):** Reserved strictly for critical warnings, ignition sequences, and primary action buttons.
- **Neon Cyan (#00F3FF):** Used for "Active State" telemetry, live data streams, and glowing indicators. It represents the "Go" status of the mission.
- **Brushed Steel (#848884):** Provides the structural framework for the UI, used for borders, inactive iconography, and secondary technical metadata.
- **Status Tints:** Success states utilize a saturated green (#00FF41), while caution states utilize a sharp amber (#FFB800).

## Typography

This design system utilizes a tiered typographic approach to separate narrative content from technical telemetry. 

**Hanken Grotesk** serves as the display typeface, providing a sharp, contemporary "aerospace" feel for headers. **Inter** handles the standard interface text for maximum legibility. **JetBrains Mono** is the critical "Data Layer" font, used for all numerical readouts, timestamps, and status labels to ensure characters remain distinct and vertically aligned in shifting data streams. 

All labels must be rendered in All-Caps with increased letter spacing to mimic military-spec instrumentation.

## Layout & Spacing

The layout philosophy follows a **Fixed-Modular Grid**. The interface is treated as a physical dashboard where every pixel of real estate is accounted for. 

- **4px Base Unit:** All spacing must be a multiple of 4px to maintain a precise, technical rhythm.
- **12-Column Grid:** Large displays use a 12-column grid with 16px gutters.
- **Data Densities:** Information density should be "High." Minimal whitespace is used; instead, structural "Steel" dividers are preferred to separate functional zones.
- **Scan-line Overlay:** A fixed background overlay of 1px horizontal lines at 4px intervals should be applied to the entire viewport at 3% opacity.

## Elevation & Depth

This design system avoids soft shadows in favor of **Structural Insets** and **Luminescent Glows**.

- **Inset Surfaces:** Deep surfaces are achieved by using a 1px border (#000000) on the top/left and a 1px steel highlight (#333533) on the bottom/right.
- **Glow Indicators:** Active elements (like the Neon Cyan indicators) do not use drop shadows. Instead, they use a "Center Glow"—an outer glow effect with a 0px offset and 8-12px blur, color-matched to the element.
- **Metallic Borders:** Cards and modules use a double-border technique: an inner 1px matte border (#121212) followed by an outer 1px "Brushed Steel" border to create a layered, plate-armor effect.

## Shapes

The shape language is strictly **Hard-Edged (0px radius)**. There are no rounded corners in this design system. 

The use of 45-degree chamfered corners is permitted for primary action buttons or top-level navigation tabs to reinforce the "machined" aesthetic. All icons should be line-based with 2px strokes and sharp miters; rounded joins or caps are prohibited.

## Components

- **Action Buttons:** Large-scale, rectangular, with a background of Racing Red or Matte Black. Active states must trigger a Neon Cyan outer stroke.
- **Telemetry Chips:** Small, monospaced data containers with a semi-transparent "Brushed Steel" background and a 1px left-hand color bar indicating status.
- **The 'Master Switch':** Checkboxes and toggles are replaced with "Safety Switches"—large, high-contrast toggles that require a double-click or "slide to arm" interaction.
- **Status Indicators:** Circular "LED" lamps. When 'Off', they are a dark desaturated grey. When 'On', they emit a high-intensity glow in their respective status color.
- **Data Tables:** Striped rows are replaced with 1px horizontal Steel dividers. Columns must be strictly aligned with no cell padding on the horizontal axis to maximize data density.
- **Crosshair Cursors:** The standard pointer is replaced with a precision crosshair when hovering over interactive telemetry charts.