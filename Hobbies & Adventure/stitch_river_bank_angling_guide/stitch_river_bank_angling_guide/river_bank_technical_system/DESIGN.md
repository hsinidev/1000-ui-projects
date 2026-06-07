---
name: River-Bank Technical System
colors:
  surface: '#faf9f9'
  surface-dim: '#dadada'
  surface-bright: '#faf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f3'
  surface-container: '#eeeeed'
  surface-container-high: '#e9e8e8'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#47473f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f0f0'
  outline: '#78786e'
  outline-variant: '#c8c7bb'
  surface-tint: '#5d6049'
  primary: '#5d6049'
  on-primary: '#ffffff'
  primary-container: '#9c9f84'
  on-primary-container: '#333621'
  inverse-primary: '#c6c9ac'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e3e2e2'
  on-secondary-container: '#646464'
  tertiary: '#5e604d'
  on-tertiary: '#ffffff'
  tertiary-container: '#9d9e88'
  on-tertiary-container: '#343524'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e5c7'
  primary-fixed-dim: '#c6c9ac'
  on-primary-fixed: '#1a1d0b'
  on-primary-fixed-variant: '#454933'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#faf9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e3e2e2'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-main:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  technical-data:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  base: 16px
  container-max: 1200px
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system is rooted in the quiet authority of an experienced fly-fishing guide. It balances the "serene" experience of being on the water with the "technical" precision required for gear, hatch timing, and river navigation. The aesthetic is **Minimalist-Rugged**: it strips away unnecessary decoration to focus on utility, yet employs high-end typography and subtle organic textures to feel premium.

The target audience is the discerning angler who values both traditional craftsmanship and data-driven results. The UI should evoke a sense of calm reliability. Visual depth is achieved not through shadows, but through layering "stone" tones and using semi-transparent "water" overlays, creating a tactile experience that feels as grounded as a riverbed.

## Colors
The "River-Bank" palette is a sophisticated, low-chroma range designed to minimize eye strain during outdoor or high-glare use. 

- **Sand (#F5F5DC)**: Acts as the primary canvas, providing a warmer, more natural alternative to white.
- **Sage (#9C9F84)**: Used for primary actions, success states, and indicating "active" hatch periods. It represents life and growth within the river ecosystem.
- **Stone (#808080 / #A9A9A9)**: These grays handle the structural elements—borders, secondary buttons, and technical data visualizations.
- **Ink (#2C2E2A)**: A deep, near-black green used for typography to ensure high contrast against the Sand background.

## Typography
This design system utilizes a dual-font strategy to bridge the gap between tradition and technique.

- **Noto Serif**: Used for headings. Its classic proportions evoke the feel of heritage fly-fishing journals and premium guide services. It should be used sparingly for "editorial" moments.
- **Work Sans**: A neutral, highly legible sans-serif used for all functional data. For the **Hatch Calendar** and stream-flow gauges, use the Medium weight of Work Sans with increased letter spacing to ensure readability in difficult lighting conditions.

Large headings should use "Ink" (#2C2E2A), while technical labels should use "Stone" (#808080) to maintain a clear visual hierarchy.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy to maintain a structured, professional feel. A 12-column grid is used for desktop views, transitioning to a single column for mobile. 

The spacing rhythm is built on a 4px baseline, but defaults to generous "breathing room" (24px - 48px) between sections to mimic the vastness of the outdoors. Technical components, such as the Hatch Calendar, should use tighter, 8px increments to imply density and precision. Use asymmetrical whitespace to guide the eye toward key data points or call-to-action buttons.

## Elevation & Depth
In keeping with the "Rugged Minimalist" style, this design system avoids heavy shadows. Depth is communicated through **Tonal Layering** and **Subtle Textures**:

- **Tier 1 (Surface)**: The Sand (#F5F5DC) background.
- **Tier 2 (Containers)**: Soft Sage or Stone-tinted panels with 1px solid borders in a slightly darker shade.
- **Tactile Overlays**: Use a very low-opacity SVG "Topographical" pattern or "Water Ripple" texture as a background on primary containers. These should be subtle enough to be felt rather than seen.
- **Interactivity**: Active states use a slight "inset" border or a color shift rather than a lift, suggesting a physical, mechanical reliability.

## Shapes
The shape language is **Soft (0.25rem)**. While the brand is rugged, it is not aggressive. Corners are slightly blunted to feel "weathered" like river stone, but remain sharp enough to feel technical and precise. 

- Use **0px (Sharp)** corners for structural separators and grid lines.
- Use **4px (Soft)** for buttons, input fields, and cards.
- **Pill-shapes** are strictly reserved for status indicators (e.g., "In Season" or "Peak Hatch") within technical tables.

## Components
- **Buttons**: Primary buttons are solid Sage (#9C9F84) with "Ink" text. Secondary buttons are "Stone" outlines. All buttons feature a 1px border and 4px radius. 
- **Technical Cards**: Used for stream conditions. They feature a 1px Stone-600 border, no shadow, and a "Sand-Light" header area to separate meta-data from primary values.
- **Hatch Calendar**: A dense grid using Work Sans. Current date is highlighted with a Sage underline. Past dates are muted Stone.
- **Input Fields**: Minimalist. Only a bottom border (2px) that thickens and changes to Sage upon focus. No background fill unless the field is in an error state.
- **Progress Indicators**: Linear, using Sage for the fill and a Stone-200 for the track, reminiscent of a fly line or a measuring tape.
- **Interactive Maps**: Custom styled to match the River-Bank palette, removing all standard "city" colors and replacing them with the Sand and Sage theme.