---
name: Biological Modernism
colors:
  surface: '#faf8ff'
  surface-dim: '#d6d9ef'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f2ff'
  surface-container: '#ebedff'
  surface-container-high: '#e4e7fe'
  surface-container-highest: '#dee1f8'
  on-surface: '#171b2b'
  on-surface-variant: '#484552'
  inverse-surface: '#2c3041'
  inverse-on-surface: '#eff0ff'
  outline: '#797583'
  outline-variant: '#c9c4d3'
  surface-tint: '#6050af'
  primary: '#6050af'
  on-primary: '#ffffff'
  primary-container: '#9d8df1'
  on-primary-container: '#331f80'
  inverse-primary: '#c9beff'
  secondary: '#386752'
  on-secondary: '#ffffff'
  secondary-container: '#b8ebd0'
  on-secondary-container: '#3d6c56'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#9a9b9b'
  on-tertiary-container: '#313333'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e6deff'
  primary-fixed-dim: '#c9beff'
  on-primary-fixed: '#1b0062'
  on-primary-fixed-variant: '#483795'
  secondary-fixed: '#bbeed3'
  secondary-fixed-dim: '#9fd1b7'
  on-secondary-fixed: '#002114'
  on-secondary-fixed-variant: '#204f3b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#faf8ff'
  on-background: '#171b2b'
  surface-variant: '#dee1f8'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
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
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is engineered for the high-precision world of neuroscience research, balancing clinical rigor with an organic, biological fluidity. It evokes a sense of "technological empathy"—the interface feels advanced and digital yet soft and human-centric. The target audience includes neuroscientists, data analysts, and medical professionals who require long-term focus without visual fatigue.

The style is a hybrid of **Soft-UI (Neumorphism)** and **Glassmorphism**. Neumorphic principles are used to create a tactile, physical environment where UI elements appear to be molded from the surface itself, while Glassmorphism is reserved for high-level data overlays and 3D brain visualizations to maintain depth and context. The result is a clean, professional environment that feels significantly more modern and approachable than traditional clinical software.

## Colors

The palette is anchored by **Soft Purple**, symbolizing cognitive activity and innovation, and **Mint**, used as a functional secondary color for "success" states, signal stability, and positive data trends. The background is not a stark white, but a very subtle off-white/cool grey to facilitate the dual-shadow neumorphic effect. 

**Deep Indigo** serves as the high-contrast foundation for all typographic data, ensuring legibility against the soft-hued background. Primary actions utilize the purple, while the mint is used sparingly to highlight biological markers or system "ready" states. Use the shadow tokens specifically for the concave and convex surface effects that define the soft-UI aesthetic.

## Typography

This design system utilizes **Inter** for all interface levels to maintain a systematic, utilitarian clarity essential for medical software. The typographic hierarchy is designed with high contrast in mind; while UI elements are soft, the text remains sharp and authoritative in Deep Indigo.

Special attention is given to "data-mono" styling (using Inter with specific spacing) for EEG readings and coordinate data. Headlines should remain tight and bold to anchor the soft-edged containers they inhabit. All body text should adhere to a generous line height to prevent fatigue during long research sessions.

## Layout & Spacing

The design system employs a **Fixed Grid** model for main dashboard views to ensure that complex EEG data visualizations maintain a predictable aspect ratio across professional displays. A 12-column grid is used with 24px gutters. 

Margins are generous (32px+) to provide "breathing room" around data-heavy modules. Spacing follows an 8px rhythmic scale, though softer, larger paddings are preferred within cards to accommodate the soft-UI shadows without crowding the content. Use "lg" and "xl" spacing for section separations to maintain the "clean, clinical" aesthetic.

## Elevation & Depth

Hierarchy is established through **Soft-UI Neumorphism** and **Glassmorphism**:

1.  **Level 0 (Background):** The base layer is a flat, neutral surface (#F5F6FA).
2.  **Level 1 (Surface Containers):** Cards and modules use two shadows: a light shadow (top-left) and a dark shadow (bottom-right) to appear "extruded" from the background.
3.  **Level 2 (Interactive/Sunken):** Inputs and pressed buttons use "inner shadows" to appear recessed into the surface.
4.  **Level 3 (Overlays):** For 3D brain maps or floating analysis tools, use a glassmorphic layer with a 20px backdrop blur, 40% opacity White fill, and a 1px solid White border (0.2 opacity).

Avoid traditional black shadows. All "dark" shadows should be a tinted version of the background color (#D1D9E6) to maintain the biological, soft feel.

## Shapes

The shape language is consistently **Rounded**. This mirrors biological structures and counters the clinical coldness often found in research tools. 

- **Standard Elements:** Buttons, inputs, and small cards use a 0.5rem (8px) radius.
- **Large Modules:** Main data containers and dashboard cards use a 1rem (16px) radius.
- **Data Markers:** Points on a graph or EEG peaks should use circular (pill-shaped) markers to maintain the organic feel.

## Components

### Buttons
Primary buttons are convex (neumorphic) with Soft Purple backgrounds and white text. Secondary buttons are the same color as the background, distinguished only by their extruded neumorphic shape and Deep Indigo text.

### Inputs & Search
Input fields must appear recessed (concave) with an inner shadow. When focused, the border glows with a soft 2px Soft Purple stroke.

### Cards
Cards are the primary organizational unit. They must feature the dual-shadow neumorphic lift. Header areas within cards should be separated by a subtle, low-opacity line or a change in surface height.

### Glass Overlays
For 3D content or modal dialogues, use the glassmorphic style. This allows the EEG waveforms or 3D brain models to remain visible underneath, maintaining the researcher's context.

### EEG Waveform Containers
These containers should be flat or slightly recessed to emphasize that the data is "contained" within the instrument. Use high-contrast lines for the waveforms (Purple and Mint) against the neutral background.

### Status Chips
Use Mint for "Active/Stable" and Soft Purple for "Processing." Chips should be pill-shaped with a subtle 1px border.