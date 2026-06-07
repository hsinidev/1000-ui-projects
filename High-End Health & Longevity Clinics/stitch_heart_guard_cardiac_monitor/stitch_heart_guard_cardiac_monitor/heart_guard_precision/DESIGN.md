---
name: Heart-Guard Precision
colors:
  surface: '#f5fafc'
  surface-dim: '#d6dbdd'
  surface-bright: '#f5fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4f6'
  surface-container: '#eaeff1'
  surface-container-high: '#e4e9eb'
  surface-container-highest: '#dee3e5'
  on-surface: '#171c1e'
  on-surface-variant: '#5d3f3d'
  inverse-surface: '#2c3133'
  inverse-on-surface: '#ecf1f3'
  outline: '#926e6c'
  outline-variant: '#e7bcba'
  surface-tint: '#bf0022'
  primary: '#ac001e'
  on-primary: '#ffffff'
  primary-container: '#d90429'
  on-primary-container: '#ffeae8'
  inverse-primary: '#ffb3af'
  secondary: '#5b5d74'
  on-secondary: '#ffffff'
  secondary-container: '#ddddf9'
  on-secondary-container: '#5f6178'
  tertiary: '#495567'
  on-tertiary: '#ffffff'
  tertiary-container: '#616d81'
  on-tertiary-container: '#e8efff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410005'
  on-primary-fixed-variant: '#930018'
  secondary-fixed: '#e0e0fc'
  secondary-fixed-dim: '#c4c4df'
  on-secondary-fixed: '#181a2e'
  on-secondary-fixed-variant: '#43455b'
  tertiary-fixed: '#d7e3fa'
  tertiary-fixed-dim: '#bbc7dd'
  on-tertiary-fixed: '#101c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f5fafc'
  on-background: '#171c1e'
  surface-variant: '#dee3e5'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Inter
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
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
  data-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1440px
  gutter: 16px
---

## Brand & Style
The design system is engineered for life-critical environments where every millisecond and every pixel counts. The brand personality is **authoritative, vigilant, and clinical**. It operates on a "Zero-Failure" philosophy, prioritizing rapid information retrieval and absolute clarity over decorative trends.

The visual style is **High-Fidelity Medical Minimalism**. It blends the density of professional diagnostic equipment with the clean legibility of modern SaaS. The interface communicates urgency through high-contrast accents of Signal Red while maintaining a professional calm through expansive use of Silk White and deep Slate. Interaction models are deliberate and precise, designed to evoke the feeling of a high-end physical medical monitor.

## Colors
This design system utilizes a high-contrast palette to distinguish between operational states and clinical data.

- **Signal Red (#D90429):** Reserved strictly for critical alerts, "Live" status indicators, and mission-critical action buttons. It must never be used for decorative elements.
- **Slate (#2B2D42):** Used for primary text, deep headers, and high-contrast sidebars. It provides the "weight" and authority of the interface.
- **Silk White (#EDF2F4):** The primary surface color. It provides a sterile, clean background that reduces eye strain during long monitoring sessions.
- **Support Greys:** A range of Slate-based tints used for borders and secondary information to maintain a monochrome hierarchy that allows the Red alerts to pop instantly.

## Typography
Typography is split into two distinct functional roles: **Information** and **Data**.

- **Information (Inter):** Used for navigation, labels, and instructional text. It is set with tight tracking in headlines for a "compact" feel and standard tracking in body text for maximum legibility.
- **Data (JetBrains Mono):** Used for all medical readouts, timestamps, heart rates, and technical metrics. The monospaced nature ensures that fluctuating numbers do not cause horizontal layout shifts (jitter) during live updates.

All typography must adhere to a strict vertical rhythm to ensure data density remains readable.

## Layout & Spacing
The layout follows a **Fixed-Modular Grid**. While the main container can scale, the internal modules (cards and data-grids) adhere to strict proportions to mimic hardware displays.

- **Grid:** A 12-column grid with a 16px gutter.
- **Density:** High density is preferred. Padding within components should be kept to the minimum required for visual separation (`md: 16px`), allowing more data to be visible on-screen at once.
- **Alignment:** All elements must align to a 4px baseline grid. Text should be strictly left-aligned or right-aligned for data comparisons; center-alignment is prohibited in data-heavy views.

## Elevation & Depth
In this design system, depth is used to communicate **layering of importance**, not physical realism.

- **Surface Layering:** Use Silk White for the base. Use subtle 1px borders in a light Slate tint (#D1D5DB) to define module boundaries rather than heavy shadows.
- **Soft Elevation:** When a component is active or "on top" (like a modal or a floating alert), use a very diffused, low-opacity Slate shadow (Blur: 12px, Opacity: 8%). 
- **Tonal Depth:** Use Slate (#2B2D42) for sidebars to create a "command center" anchor on the left side of the screen, visually separating navigation from the diagnostic workspace.

## Shapes
The shape language is **geometric and rigid**. 

- **Primary Radius:** A 4px (0.25rem) radius is used for all standard components (buttons, input fields, cards). This "Soft" edge prevents the UI from feeling aggressive while maintaining the precision of a professional tool.
- **Sharp Containers:** Large layout sections and main page containers should remain at 0px radius to emphasize the structural integrity of the grid.
- **Iconography:** Icons must be stroke-based (2px weight) with sharp terminals, avoiding overly rounded or "friendly" styles.

## Components
Consistent styling across components reinforces the system's reliability.

- **Buttons:** Primary buttons use a solid Slate background with Silk White text. "Alert" buttons use Signal Red. All buttons feature a 4px radius and high-contrast labels.
- **Data Cards:** Modules containing telemetry data must feature a "Label Header" in `label-caps` typography with a 1px bottom border. 
- **Status Indicators:** Use a "Pill" shape for status tags. A Signal Red pill indicates "Critical," while a Slate pill indicates "Stable."
- **Input Fields:** Use 1px Slate borders. Upon focus, the border weight increases to 2px. No glowing shadows; use a sharp color shift for focus states.
- **Live Waveforms:** ECG and heart-rate graphs should be rendered in Signal Red against the Silk White background, with a 10% opacity Red fill under the curve for visual volume.
- **Medical Chips:** Small, non-intrusive data markers used to categorize patient history. These should have no background fill, only a 1px Slate-tinted border.