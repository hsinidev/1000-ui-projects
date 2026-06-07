---
name: Aegis-IoT Core
colors:
  surface: '#161308'
  surface-dim: '#161308'
  surface-bright: '#3d392c'
  surface-container-lowest: '#110e05'
  surface-container-low: '#1f1b10'
  surface-container: '#231f14'
  surface-container-high: '#2e2a1e'
  surface-container-highest: '#393528'
  on-surface: '#eae2cf'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#eae2cf'
  inverse-on-surface: '#343024'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#f6f6f6'
  on-tertiary: '#2f3131'
  tertiary-container: '#d9dada'
  on-tertiary-container: '#5e5f60'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#161308'
  on-background: '#eae2cf'
  surface-variant: '#393528'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-fixed:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  gutter: 16px
  margin: 32px
---

## Brand & Style

The visual identity of this design system is rooted in **Industrial Brutalism**—a style that prioritizes utility, structural integrity, and mission-critical clarity. It is designed to feel like a high-end hardware interface, evoking the sensation of "machined" software. 

The brand personality is authoritative and uncompromising. It avoids decorative fluff in favor of high-contrast information density. The UI must feel like an armored shell for data: robust, secure, and ready for deployment in high-stakes industrial environments. Every element should look like it was built to withstand physical wear, using heavy strokes and technical motifs to reinforce a sense of digital "hardening."

## Colors

The palette is strictly functional, mirroring hazard signage and heavy machinery. 

- **Graphite Grey (#2E2E2E):** The primary structural color. It forms the "chassis" of the application, used for backgrounds, containers, and deep-level surfaces.
- **Hazard Yellow (#FFD700):** The primary action and attention color. Used sparingly for critical CTAs, active states, and warnings. It must always maintain high contrast against the graphite base.
- **White (#FFFFFF):** Used exclusively for high-priority data readouts and essential labeling to ensure maximum legibility.
- **System Accents:** A secondary darker background (#1A1A1A) is used to create depth, while "Signal Red" and "Signal Green" are reserved for binary status indicators (Alert/Secure).

## Typography

This design system utilizes **Space Grotesk** across all levels. Its geometric construction provides the "technical" aesthetic required, while its open apertures ensure legibility on low-resolution industrial monitors.

- **Headlines:** Use Bold weights with slight negative letter spacing to create a compact, "heavy" feel.
- **Data Display:** For sensor readings and IP addresses, use the Medium weight with increased letter spacing to mimic the rhythmic layout of monospaced code.
- **Labels:** Small caps should be applied to metadata labels to differentiate them from actionable data.
- **Utility:** All numeric data should utilize tabular lining (mono-spacing) to ensure that digits align perfectly in scanning lists and dashboards.

## Layout & Spacing

The layout is built on a **Rigid Grid System**. All components must snap to an 8px square baseline. 

- **Grid:** Use a 12-column fluid grid for primary dashboard layouts, but wrap the entire interface in a "Frame"—a fixed 32px outer margin that acts as the hardware bezel.
- **Containers:** Use 24px (md) padding for all data cards.
- **Dividers:** Instead of invisible whitespace, use visible 1px or 2px "Graphite" lines to separate modules. The layout should feel like a series of interlocking panels rather than a single flowing page.

## Elevation & Depth

Depth is conveyed through **Structural Layering** rather than light and shadow. 

- **No Shadows:** Avoid drop shadows entirely to maintain the "rugged" flat-panel aesthetic.
- **Tonal Tiers:** Use #1A1A1A for the base floor, #2E2E2E for primary containers, and #3D3D3D for elevated states or tooltips.
- **Heavy Borders:** Use a consistent 2px solid border on all interactive containers. 
- **Hazard Patterns:** Use a 45-degree diagonal stripe pattern (Hazard Yellow/Black) to indicate "Top Level" or "Emergency" states, effectively pulling those elements to the front of the visual hierarchy.

## Shapes

The shape language is strictly **Angular (0px radius)**. 

Every element—from buttons and input fields to large dashboard panels—must have sharp, 90-degree corners. This evokes the feeling of cut metal and military-grade hardware. 

- **Notched Corners:** For primary call-to-action buttons, a "clipped corner" (45-degree cut) may be used on the top-right to indicate a specialized technical function.
- **Stroke:** Use a consistent 2px stroke for all containers to ensure they feel "heavy duty."

## Components

- **Buttons:** Rectangular, sharp-edged. The "Default" state uses a White border with White text. The "Primary/Active" state is solid Hazard Yellow with Graphite Grey text. 
- **Status Indicators:** Use "LED" style components—solid 8px circles. Use a CSS 'glow' effect (box-shadow) only for these indicators to simulate a physical light-emitting diode.
- **Input Fields:** Graphite background with a 1px White bottom-border only. When focused, the border becomes Hazard Yellow and the label shifts to a small-cap header above the field.
- **Cards/Panels:** Every card must include a "Header Strip"—a 4px vertical accent line on the left side to denote the category (e.g., Yellow for 'Active', Grey for 'Standby').
- **Data Tables:** High-density. Use alternating row fills (#252525) and ensure every cell has a visible border to reinforce the grid-mesh look.
- **Progress Bars:** Segmented blocks rather than a smooth continuous fill to look like hardware power meters.