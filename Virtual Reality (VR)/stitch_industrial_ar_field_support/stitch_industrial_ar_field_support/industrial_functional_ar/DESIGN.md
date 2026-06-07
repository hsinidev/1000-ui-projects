---
name: Industrial-Functional AR
colors:
  surface: '#021525'
  surface-dim: '#021525'
  surface-bright: '#293b4d'
  surface-container-lowest: '#000f1e'
  surface-container-low: '#091d2e'
  surface-container: '#0e2132'
  surface-container-high: '#192b3d'
  surface-container-highest: '#243648'
  on-surface: '#d1e4fb'
  on-surface-variant: '#cfc6ae'
  inverse-surface: '#d1e4fb'
  inverse-on-surface: '#203243'
  outline: '#98907a'
  outline-variant: '#4c4634'
  surface-tint: '#e7c433'
  primary: '#ffeebb'
  on-primary: '#3b2f00'
  primary-container: '#f4d03f'
  on-primary-container: '#6c5900'
  inverse-primary: '#705d00'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#ffebe0'
  on-tertiary: '#4f2500'
  tertiary-container: '#ffc7a1'
  on-tertiary-container: '#8e4700'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe174'
  primary-fixed-dim: '#e7c433'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#554500'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdcc5'
  tertiary-fixed-dim: '#ffb783'
  on-tertiary-fixed: '#301400'
  on-tertiary-fixed-variant: '#713700'
  background: '#021525'
  on-background: '#d1e4fb'
  surface-variant: '#243648'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 30px
  body-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  label-xl:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '700'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 18px
  status-code:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '800'
    lineHeight: 24px
    letterSpacing: 0.05em
spacing:
  touch-target-min: 3.5rem
  gutter: 1.5rem
  margin-edge: 2rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

This design system is engineered for high-stakes field environments where clarity and speed of interaction are non-negotiable. The brand personality is authoritative, resilient, and purely utilitarian, drawing from **Industrial Brutalism** and **High-Contrast** design movements. It prioritizes data legibility over aesthetic flourish, ensuring that field technicians can operate complex AR interfaces under direct sunlight or in low-light industrial settings.

The UI evokes the feeling of professional-grade hardware—rugged, reliable, and precise. By utilizing heavy borders and a limited, high-impact palette, the system minimizes cognitive load, allowing the user to focus on the task at hand rather than the interface itself.

## Colors

The palette is optimized for a **Dark Mode** default to reduce glare and preserve the technician's night vision while providing a deep canvas for AR overlays.

*   **Primary (Safety Yellow):** Reserved strictly for primary action buttons, critical warnings, and active state indicators. It is the highest-visibility element in the UI.
*   **Neutral (Charcoal):** Used for the base UI chrome, persistent status bars, and background panels to ensure high contrast against the real-world AR view.
*   **Secondary (White):** Used for primary text and secondary iconography to maintain maximum readability.
*   **Tertiary (Industrial Orange):** Utilized for non-critical alerts or specialized technical status updates to differentiate from the "Safety Yellow" primary actions.

## Typography

The design system utilizes **Inter** for its exceptional legibility and systematic structure. Every typeface weight is bumped up by one level (e.g., standard body text uses Medium instead of Regular) to counteract "washout" in outdoor field conditions.

Vertical rhythm is strictly maintained to ensure large tap targets. Headlines are tight and aggressive to maximize screen real estate, while labels use all-caps and increased letter spacing to clearly distinguish metadata from dynamic content.

## Layout & Spacing

This system employs a **Contextual Layout** model optimized for AR safe zones. Components are anchored to the edges of the display to keep the center clear for the AR field of view.

*   **Safe Areas:** A mandatory 32px (2rem) margin is applied to all screen edges to account for hardware bezels and protective cases.
*   **Touch Targets:** A minimum 56px (3.5rem) touch target is enforced for all interactive elements to allow for glove-friendly use.
*   **Vertical Stacking:** Elements are stacked using a rigid 8px baseline grid, with 16px (1rem) being the standard gap between related functional blocks.

## Elevation & Depth

To maintain the rugged, industrial aesthetic, this design system rejects soft shadows and ambient light. Depth is communicated through **Bold Borders** and **Tonal Layers**.

*   **Primary Surface:** Semi-transparent Charcoal (#2C3E50 at 85% opacity) to allow the real-world environment to remain visible.
*   **Raised Elements:** Use 2px solid White or Safety Yellow borders to indicate "top-level" interactive components.
*   **Inactive States:** Lower opacity (40%) and removed borders signify elements that are not currently interactable.
*   **Overlay Modals:** Use a solid, non-transparent Charcoal background to force focus during critical safety checklists.

## Shapes

The shape language is strictly **Sharp (0)**. Right angles reinforce the industrial nature of the app and maximize the usable internal area of every button and container. This geometric rigidity ensures that the UI feels like an integrated part of the technician’s physical toolset. Beveled corners are permitted only for specialized "Status Indicators" to mimic physical LED cutouts.

## Components

### Buttons
Primary buttons are solid Safety Yellow with Charcoal text. They must span at least 50% of the screen width for one-handed thumb access. Secondary buttons use a 2px White border with transparent centers.

### Persistent Status Indicators
Top-level bars that house battery life, connectivity, and GPS signal. These are always visible and use high-contrast iconography. If a critical failure occurs, the entire status bar background flashes Safety Yellow.

### Information Cards
Cards use a Charcoal fill with a 1px White border. Header sections within cards are separated by a solid 1px horizontal rule. All data points within cards must use the `label-md` and `body-lg` typography scales.

### Lists
Lists are "High-Density" with 56px minimum row heights. Each row is separated by a 1px White divider. Active or selected rows are highlighted with a Safety Yellow left-edge accent (4px width).

### Checkboxes & Inputs
Inputs use a solid Charcoal background with a 2px White border that turns Safety Yellow on focus. Checkboxes are oversized (32px x 32px) to ensure accuracy when the user is in motion.

### AR Wayfinders
Floating directional arrows and distance markers. These must use Safety Yellow for the arrow geometry and White for the accompanying text to ensure they do not get lost against complex real-world textures.