---
name: NeuroSense
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#cbc4cc'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#958f96'
  outline-variant: '#49454b'
  surface-tint: '#cfc2d8'
  primary: '#cfc2d8'
  on-primary: '#352d3e'
  primary-container: '#120b1a'
  on-primary-container: '#82778b'
  inverse-primary: '#645b6d'
  secondary: '#ffd393'
  on-secondary: '#432c00'
  secondary-container: '#fdaf00'
  on-secondary-container: '#694600'
  tertiary: '#d3bee9'
  on-tertiary: '#39294b'
  tertiary-container: '#150627'
  on-tertiary-container: '#86749a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ebdef4'
  primary-fixed-dim: '#cfc2d8'
  on-primary-fixed: '#201828'
  on-primary-fixed-variant: '#4c4355'
  secondary-fixed: '#ffddaf'
  secondary-fixed-dim: '#ffba43'
  on-secondary-fixed: '#281800'
  on-secondary-fixed-variant: '#614000'
  tertiary-fixed: '#eedbff'
  tertiary-fixed-dim: '#d3bee9'
  on-tertiary-fixed: '#231435'
  on-tertiary-fixed-variant: '#504063'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the high-stakes, low-light environment of neurodiagnostic and sleep laboratories. The brand personality balances clinical precision with a restorative, nocturnal atmosphere. It targets specialized medical practitioners and patients who require a cognitive environment free from visual "noise" and light-induced fatigue.

The visual style is **Atmospheric Technical**. It utilizes a deep, immersive canvas to minimize photophobia while employing high-precision technical elements to convey medical authority. The aesthetic leans into a sophisticated fusion of minimalism and glassmorphism, where data is prioritized through light, not mass. The result is a UI that feels like a quiet, high-tech command center—calm, focused, and impeccably organized.

## Colors

The palette is designed for extreme comfort in dark environments. 

- **Primary (Deep Purple):** Used for the base background layers. It provides a softer alternative to pure black, reducing the "inking" effect while maintaining deep contrast.
- **Secondary (Amber):** The sole "active" color. Used for critical data points, primary actions, and notifications. It carries a natural warmth that is less disruptive to circadian rhythms than blue or white light.
- **Tertiary (Muted Violet):** Used for structural elements like dividers, inactive states, and iconography that requires subtle presence without drawing focus.
- **Neutral (Smoke):** A high-visibility off-white used for primary typography and technical readouts to ensure AA/AAA accessibility against the deep purple backgrounds.

## Typography

This design system employs a dual-font strategy to differentiate between medical narrative and technical data. 

**Space Grotesk** is used for headlines, labels, and data visualizations. Its geometric, technical construction reinforces the scientific nature of the product. Use uppercase for labels to create a distinctive, rhythmic grid feel.

**Manrope** is used for all body text, patient notes, and instructional content. Its balanced, modern proportions ensure maximum readability during long diagnostic sessions where eye strain must be minimized. 

All typography must maintain a high contrast ratio against the deep purple background. Key metrics and data points should be rendered in the Amber accent to draw immediate attention.

## Layout & Spacing

This design system utilizes a **Fixed Grid** layout for main dashboards and a flexible, modular layout for diagnostic tools. The grid is based on a 12-column system with generous 24px gutters to allow technical data to "breathe."

Vertical rhythm is strictly maintained using a 4px baseline unit. In diagnostic views, information density is high but organized through clear modular grouping. Technical checklists and charts should align to the grid to create a sense of clinical order. Horizontal scrolling is reserved exclusively for time-series medical charts and hypnograms.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Glassmorphism** rather than traditional shadows. 

1.  **Base Layer:** The deepest purple (#0D0714).
2.  **Surface Layer:** A slightly lighter purple-tinted surface with 40% opacity and a 20px background blur.
3.  **Accent Elevation:** Elements requiring focus (like active Diagnostic Cards) use a subtle Amber outer glow (`drop-shadow: 0 0 12px rgba(255, 176, 0, 0.3)`) instead of a dark shadow.

This approach creates a "backlit" feel, similar to medical lightboxes or dark-room monitors, ensuring the UI feels integrated into a low-light physical environment.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding provides a human, calming touch to an otherwise rigorous technical interface. Larger components, such as Diagnostic Cards, may use the `rounded-lg` (0.5rem) setting to create a distinct container feel. Buttons and interactive chips follow the primary soft rounding to maintain a professional, medical-instrument aesthetic. Avoid pill-shaped buttons; use rectangular shapes with soft corners to reinforce the "technical equipment" metaphor.

## Components

### Buttons & Actions
Primary buttons are solid Amber with Smoke text (high contrast). Secondary buttons use an Amber ghost-border with a subtle 10% Amber fill. On hover, primary buttons should increase their glow intensity rather than changing color.

### Medical Charts & Hypnograms
Charts utilize a Smoke-colored axis with low-opacity grid lines. Data lines for sleep stages should be color-coded with varying saturations of the primary Amber. Use 2px line weights for clarity. Hypnograms must include a semi-transparent Amber "active stage" highlight.

### Diagnostic Cards
Cards act as the primary container for patient data. They should feature a top-border accent (2px Amber) to denote active monitoring status. Use the glassmorphic surface style for the card body to maintain depth.

### Technical Checklists
Checklists use custom Amber checkbox assets. When a task is completed, the text should transition to a muted Tertiary Violet with a strikethrough, while the checkbox glows slightly to indicate "Current Status: Safe/Ready."

### Inputs & Fields
Input fields are "Underline" style with a Smoke bottom border. When focused, the border transitions to Amber with a soft glow, and the label floats above in Space Grotesk caps.

### Notifications
Critical alerts use a high-intensity Amber pulse. Non-critical system updates use a subtle Smoke-tinted glass toast that appears in the top right, ensuring it doesn't obstruct central diagnostic data.