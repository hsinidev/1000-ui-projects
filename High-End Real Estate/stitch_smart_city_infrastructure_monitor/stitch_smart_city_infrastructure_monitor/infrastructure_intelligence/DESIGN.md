---
name: Infrastructure Intelligence
colors:
  surface: '#13131b'
  surface-dim: '#13131b'
  surface-bright: '#393841'
  surface-container-lowest: '#0d0d15'
  surface-container-low: '#1b1b23'
  surface-container: '#1f1f27'
  surface-container-high: '#292932'
  surface-container-highest: '#34343d'
  on-surface: '#e4e1ed'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#e4e1ed'
  inverse-on-surface: '#303038'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#b7c8e1'
  on-secondary: '#213145'
  secondary-container: '#3a4a5f'
  on-secondary-container: '#a9bad3'
  tertiary: '#c0c6db'
  on-tertiary: '#293041'
  tertiary-container: '#8a90a4'
  on-tertiary-container: '#232a3a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#dce2f8'
  tertiary-fixed-dim: '#c0c6db'
  on-tertiary-fixed: '#151b2b'
  on-tertiary-fixed-variant: '#404758'
  background: '#13131b'
  on-background: '#e4e1ed'
  surface-variant: '#34343d'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 12px
  sidebar-width: 280px
---

## Brand & Style

The design system is engineered for civil engineers, urban planners, and data analysts who require absolute precision in high-stakes environments. The aesthetic is **Technical & Precise**, leaning into a modern industrial vibe that prioritizes utility over decoration. 

The visual language draws from **High-Contrast Modernism** with subtle **Glassmorphism** used specifically for data overlays on maps. The goal is to evoke a sense of "Mission Control"—stable, authoritative, and real-time. Interfaces are dense but organized, utilizing a strict mathematical rhythm to ensure that even the most complex infrastructure data remains legible and actionable under pressure.

## Colors

The palette is optimized for dark-mode-only environments to reduce eye strain during long monitoring sessions. **Deep Navy** (#0B1221) serves as the foundational canvas, providing a low-light base that makes data "pop." **Electric Indigo** (#6366F1) is the primary action color, used sparingly for active states, interactive nodes, and primary "Time-Travel" controls. 

**Slate** (#64748B) handles secondary information, borders, and inactive metadata, creating a clear visual hierarchy. Status indicators utilize high-chroma variants of Green, Amber, and Red to ensure critical alerts are unmissable against the dark backdrop.

## Typography

This design system employs a dual-font strategy. **Inter** is used for body copy and general UI text for its exceptional readability at small sizes. **Space Grotesk** is utilized for headlines, data readouts, and labels to inject a technical, geometric character. 

For numerical data, emphasize the use of tabular numsets (monospaced) to ensure that columns of figures align perfectly in high-density tables. Uppercase labels with increased letter spacing should be used for secondary metadata to differentiate it from actionable UI text.

## Layout & Spacing

The layout utilizes a **Fixed-Fluid Hybrid Grid**. The primary navigation and data sidebars are fixed-width to maintain consistent control positioning, while the central map/visualization area is fluid. 

A strict **4px baseline grid** governs all spacing. High-density cards use "Compact" spacing (8px internal padding) to maximize the information visible on a single screen. Margins between major modules should be 16px to maintain a sense of structured modularity without wasting screen real estate.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** rather than traditional shadows. As elements "rise" in importance or appear in the foreground, their background color becomes progressively lighter (e.g., from Deep Navy to a lighter Navy-Slate).

**Glassmorphism** is reserved for floating map controls and "Time-Travel" overlays, using a 12px background blur and a 1px border at 10% white opacity. This allows the underlying map data to remain visible while providing a clear surface for interaction. Shadows, when used for modals, are sharp and dark, intended to provide a crisp "cut-out" effect rather than a soft glow.

## Shapes

The shape language is primarily **Sharp and Technical**. A subtle 4px (Soft) radius is applied to cards and input fields to prevent the UI from feeling overly aggressive, but buttons and status tags maintain a precise, calculated feel. 

Interactive nodes on the map and data points in line graphs use geometric primitives (circles, diamonds, squares) to categorize infrastructure types without relying solely on color.

## Components

### High-Density Data Cards
Cards use a 1px Slate (#64748B) border at 20% opacity. Headers within cards use the `label-caps` typography style. Data points are paired with mini sparklines to show 24-hour trends.

### 'Time-Travel' Range Sliders
The slider track is a thin 2px Slate line, while the handle is a high-contrast Electric Indigo circle. Tick marks represent time intervals (Hourly/Daily) and glow slightly when the "Playback" mode is active.

### Status Indicators
Indicators use a "Light-Box" style: a low-opacity background tint paired with a high-intensity 100% opacity foreground dot and text. This ensures status is readable across various background map textures.

### Vector-Line Maps
Map styling is monochromatic (Navy/Slate) with infrastructure assets drawn in Electric Indigo. Line weights for "flows" (power, water, traffic) are modulated based on capacity or load, using dashed animations to indicate directionality.

### Inputs & Controls
Form fields use a solid #0B1221 background with a 1px Slate border that transitions to Electric Indigo on focus. Labels are always positioned above the input to maintain horizontal alignment in dense sidebars.