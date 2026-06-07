---
name: Sonic-Blueprint
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#d3c4b8'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#9c8e84'
  outline-variant: '#4f453c'
  surface-tint: '#ebbe95'
  primary: '#ebbe95'
  on-primary: '#452a0c'
  primary-container: '#b58d67'
  on-primary-container: '#42270a'
  inverse-primary: '#795736'
  secondary: '#b8c8da'
  on-secondary: '#223240'
  secondary-container: '#394857'
  on-secondary-container: '#a7b7c8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#969494'
  on-tertiary-container: '#2d2d2d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcbe'
  primary-fixed-dim: '#ebbe95'
  on-primary-fixed: '#2c1600'
  on-primary-fixed-variant: '#5f4021'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-lg:
    fontFamily: metropolis
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-lg:
    fontFamily: jetbrainsMono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 20px
  data-sm:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: jetbrainsMono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 0.1em
  headline-lg-mobile:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 48px
  margin-mobile: 16px
  grid-columns: '12'
---

## Brand & Style
The design system embodies the intersection of architectural rigor and acoustic mastery. It is designed for sound engineers, architects, and studio designers who require high-precision tools that feel authoritative and industrial. 

The aesthetic is **Minimalist-Technical**. It avoids decorative flourishes in favor of structural clarity. Drawing inspiration from blueprints and CAD software, the system utilizes "X-ray" construction details—such as visible alignment guides, subtle grid underlays, and exposed corner markers—to convey a sense of ongoing calculation and physical accuracy. The emotional response is one of calm, professional reliability and scientific exactness.

## Colors
This design system utilizes a dark-themed palette to reduce eye strain in studio environments and emphasize technical data.

- **Primary (Warm Oak):** Used sparingly for interactive focal points, success states, and indicating premium wood-based acoustic materials.
- **Secondary (Slate):** Applied to structural lines, inactive states, and secondary UI elements to provide a "blue-steel" technical feel.
- **Tertiary (Charcoal):** The foundational canvas color, providing deep contrast for technical overlays.
- **Neutral:** A high-contrast off-white/light gray used for primary text and critical data readouts to ensure maximum legibility against the charcoal background.

## Typography
The typography strategy prioritizes data density and hierarchy. 

**Metropolis** provides the geometric, architectural foundation for headlines. **Inter** is used for general interface copy for its neutral, highly legible character. **JetBrains Mono** is reserved for all technical data, measurements, and coordinate readouts, evoking the precision of code and schematics. Use all-caps labels for axis titles and structural annotations to mimic blueprint notations.

## Layout & Spacing
The layout follows a **Fixed Grid** model on desktop to preserve the integrity of acoustic 3D visualizations. A 12-column system is used with a strict 4px base-unit rhythm.

Spacing is used to create "zones" of information. Gutters are intentionally generous (24px) to prevent data-heavy panels from feeling cluttered. On mobile, the system collapses to a single-column flow with reduced margins, but maintains the 4px vertical rhythm to preserve the "engineered" feel. Alignment is always hard-edged; elements should snap to the grid to reinforce the sense of architectural precision.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. 

The base layer is Charcoal (#1A1A1A). Elevated panels use a slightly lighter shade of charcoal with a 1px solid Slate (#708090) border at 30% opacity. For "X-ray" details, use hair-line strokes (0.5pt) to show interior dimensions or hidden structural components. No ambient shadows are permitted, as the system relies on physical-line boundaries to define space, mimicking a 2D/3D blueprint environment.

## Shapes
The shape language is strictly **Sharp (0px)**. 

Every UI element—from buttons and input fields to cards and modals—utilizes 90-degree corners. This reinforces the architectural and technical nature of the software. Circles are only permitted for specific acoustic functions (e.g., omnidirectional sound source icons) or radial dials, where the geometry is a functional representation of physics, not a stylistic choice.

## Components
- **Buttons:** Rectangular with no radius. Primary buttons use Warm Oak background with black text. Ghost buttons use Slate outlines. Use subtle corner "crosshair" marks for hover states to emphasize the "target" metaphor.
- **Input Fields:** Bottom-border only or full thin Slate outline. Labels are always positioned above in `label-caps` typography. Data input should use JetBrains Mono.
- **Cards/Panels:** Defined by 1px Slate outlines. Headers are separated by a horizontal rule.
- **Chips:** Small, rectangular, with monochromatic backgrounds (Slate) and technical labels.
- **Checkboxes:** Square, sharp-edged, with a simple 'X' mark instead of a checkmark for an architectural feel.
- **Specialized Components:** 
    - *The Frequency Graph:* High-contrast line work with a faint 10dB grid overlay.
    - *Material Selector:* Swatches that use subtle grain textures to represent Oak, Foam, or Concrete, framed in technical frames.
    - *Measurement Tool:* A dynamic HUD-style component showing real-time distance and absorption coefficients.