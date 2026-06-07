---
name: Vitality-Glow Aesthetic
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e9bcb9'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#b08784'
  outline-variant: '#5f3e3d'
  surface-tint: '#ffb3af'
  primary: '#ffb3af'
  on-primary: '#68000e'
  primary-container: '#ff5357'
  on-primary-container: '#5c000b'
  inverse-primary: '#bf0024'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410006'
  on-primary-fixed-variant: '#930019'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-hero:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 100%
    letterSpacing: -0.04em
  metric-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 110%
    letterSpacing: -0.02em
  metric-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 120%
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 150%
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 140%
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 100%
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 100%
spacing:
  unit: 4px
  gutter: 12px
  margin: 20px
  container-padding: 16px
  grid-cols: '12'
---

## Brand & Style

The design system is engineered for high-performance health optimization, moving away from the "calm wellness" of competitors toward an aggressive, medical-grade "bio-hacking" aesthetic. It targets elite athletes and data-driven individuals who view health as a performance metric rather than a state of relaxation.

The visual style combines **Brutalism** and **High-Contrast Neon** aesthetics. It utilizes a modular, high-density grid system that prioritizes information velocity. The emotional response is one of urgency, precision, and vital energy, achieved through pitch-black backgrounds contrasted against visceral neon red accents and kinetic typography that pulses with the user's biological data.

## Colors

The palette is strictly nocturnal to maximize the impact of the "Vitality Glow." The foundation is built on `#000000` (Pitch Black) for deep immersion, with `#121212` (Deep Charcoal) used to define modular containers.

**Neon Red (#FF0033)** is the singular high-octane accent. It is reserved for critical biometrics, active states, and "live" data streams. In high-performance contexts, this red is paired with a glow effect to simulate thermal energy or laser precision. Secondary neutrals are muted greys to ensure the red remains the primary focal point for the eye.

## Typography

The typography strategy employs a "Technical Sans" approach. **Space Grotesk** is used for headlines and primary metrics; its geometric quirks provide a futuristic, lab-grade feel. For high-density data and body text, **Inter** is utilized for its exceptional legibility and tabular numeric properties.

Kinetic typography should be applied to the `display-hero` and `metric-xl` levels, where numbers may "shiver" or pulse slightly in sync with a detected heart rate. Use `data-mono` (Inter with tabular figures enabled) for all real-time changing values to prevent layout shift during data refreshes.

## Layout & Spacing

This design system utilizes a **High-Density Modular Grid**. Unlike consumer health apps that use generous whitespace, this system packs information into tight, technical clusters. 

The layout is built on a 4px baseline shift. Modules are separated by "Subtle Borders" (1px width) rather than wide gutters to mimic a cockpit or medical dashboard. Elements should be aligned to a strict 12-column grid for desktop/tablet and a 4-column grid for mobile, emphasizing verticality and technical rigor.

## Elevation & Depth

Depth is achieved through **Tonal Layering and Glow**, not traditional shadows. 

1.  **Base:** `#000000` (Pitch Black) is the furthest layer.
2.  **Surfaces:** `#121212` (Deep Charcoal) modules sit directly on the base.
3.  **Active Depth:** Elements do not "lift" with shadows; instead, they "ignite." When a module is focused or contains critical data, it gains a 1px inner stroke of Neon Red and an outer `accent_glow` (diffused neon blur).
4.  **Glassmorphism:** Use sparingly for overlays. Apply a heavy background blur (20px+) with a 10% opacity white tint to simulate high-tech polycarbonate screens.

## Shapes

The shape language is **Sharp and Aggressive**. A `0` roundedness (90-degree angles) is the default for all primary data modules and buttons, reinforcing the brutalist, medical-grade hardware aesthetic.

Small exceptions (radius 2px-4px) may be made for internal UI elements like checkboxes or progress bar caps to prevent visual vibrating at small scales, but the primary silhouette of the design system must remain rectangular and rigid.

## Components

**Buttons:** High-contrast blocks. Primary buttons use a solid Neon Red background with black text. Secondary buttons are outlined in 1px grey with a red hover state that triggers a glow effect.

**Data Cards:** Modular rectangles with a 1px border (`#1A1A1A`). Title labels are always `label-caps`. The primary metric is centered or top-aligned in `metric-xl`.

**Kinetic Sparklines:** Real-time data visualizations use a 2px Neon Red stroke. Area charts under the sparkline should use a vertical gradient from `accent_glow` to transparent.

**Chips:** Small, rectangular tags with monochromatic backgrounds and `label-caps` text. When a status is "Critical," the chip pulses with a red glow.

**Input Fields:** Ghost-style inputs with only a bottom border. On focus, the bottom border turns Neon Red and expands to 2px.

**Medical-Grade Sliders:** Thin horizontal tracks with a square, Neon Red thumb. Values are displayed in `data-mono` above the thumb during interaction.