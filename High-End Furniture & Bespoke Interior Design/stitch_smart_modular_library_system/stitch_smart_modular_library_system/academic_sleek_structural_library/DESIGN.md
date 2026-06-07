---
name: Academic & Sleek Structural Library
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c5c6ce'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#8f9098'
  outline-variant: '#44474d'
  surface-tint: '#b7c7eb'
  primary: '#b7c7eb'
  on-primary: '#20304e'
  primary-container: '#1b2b48'
  on-primary-container: '#8393b5'
  inverse-primary: '#4f5e7e'
  secondary: '#edbe8b'
  on-secondary: '#462a04'
  secondary-container: '#63421a'
  on-secondary-container: '#deb07e'
  tertiary: '#c3c7cd'
  on-tertiary: '#2c3136'
  tertiary-container: '#272c31'
  on-tertiary-container: '#8f9399'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#b7c7eb'
  on-primary-fixed: '#091b37'
  on-primary-fixed-variant: '#374765'
  secondary-fixed: '#ffddba'
  secondary-fixed-dim: '#edbe8b'
  on-secondary-fixed: '#2b1700'
  on-secondary-fixed-variant: '#604018'
  tertiary-fixed: '#dfe3e9'
  tertiary-fixed-dim: '#c3c7cd'
  on-tertiary-fixed: '#171c20'
  on-tertiary-fixed-variant: '#43474c'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
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
  structural-margin: 64px
---

## Brand & Style
The design system embodies an "Academic & Sleek" aesthetic, merging the warmth of traditional library craftsmanship with the precision of modern modular engineering. It targets an audience that values both intellectual heritage and technological advancement.

The visual style is **Tactile / Skeuomorphic**, utilizing high-fidelity textures to ground the digital experience in physical reality. Natural Oak wood grain provides a structural foundation, while polished silver hardware accents represent the "smart" modularity of the system. The interface should evoke a sense of prestige, reliability, and technical sophistication, feeling less like a standard app and more like a high-end architectural configuration tool.

## Colors
The palette is rooted in a dark, authoritative foundation. **Deep Navy (#1B2B48)** serves as the primary surface color, providing a scholarly and calm backdrop. **Oak (#B58B5C)** is reserved for structural elements, framing, and decorative dividers that require a sense of physical weight.

**Silver/Light Grey (#D1D5DB)** is utilized exclusively for technical data, measurements, and labels to ensure maximum legibility against dark backgrounds. This color also serves as the basis for metallic gradients used in interactive hardware components. High-contrast white is avoided in favor of the softer Silver to maintain the prestigious, low-glare academic feel.

## Typography
The typographic hierarchy creates a dialogue between tradition and data. **Playfair Display** is used for all editorial and structural headings, echoing the serif faces found in classical rare-book collections. It should be typeset with generous leading to maintain an airy, sophisticated feel.

**Inter** handles all functional requirements. It is used for technical specifications, modular dimensions, and UI controls. For data-heavy readouts, use the `data-mono` style to imply engineering precision. `label-caps` should be used for small metadata tags or section identifiers, always rendered in Silver to contrast against the Navy or Oak backgrounds.

## Layout & Spacing
The layout follows a **fixed grid** philosophy, mimicking the rigidity of a physical shelving unit. Content is organized within a 12-column grid with wide 32px gutters to prevent the technical data from feeling cluttered.

Margins are generous (`structural-margin`), especially on desktop, to frame the UI like a curated gallery exhibit. On mobile, the grid collapses to a single column, but maintains the "inset" look where cards appear to be tucked into a wooden frame. Spacing between modular units should be consistent, using the 8px (`sm`) and 16px (`md`) increments to reflect standard carpentry tolerances.

## Elevation & Depth
Depth is communicated through physical metaphors rather than abstract shadows. 
1.  **Recessed Depth (Inner Shadows):** Used for "Shelf Inserts" (cards) to make them appear as though they are sitting inside an Oak frame.
2.  **Raised Metallic (Beveled Edges):** Buttons and active toggles use subtle silver bevels and 1px highlights on the top edge to appear as machined hardware protruding from the surface.
3.  **Navy Translucent Overlays:** When data panels appear over the 3D shelving model, they use a heavy backdrop blur (20px) and a semi-transparent Navy tint to maintain focus while keeping the structural context visible.
4.  **Tonal Layers:** The primary Navy surface is the furthest back, Oak frames are mid-ground, and Silver text/hardware buttons occupy the foreground.

## Shapes
The shape language is primarily **Soft (0.25rem)**, reflecting the precision-cut edges of wood and metal. While "Sharp" would be too aggressive, high roundedness would break the architectural feel. Small radii are used on the corners of "Shelf" cards and "Hardware" buttons to simulate the natural softening of materials that have been sanded or machined. Circular shapes are reserved strictly for screw-head icons or status indicators.

## Components
-   **Buttons:** Styled as "Hardware." They feature a polished silver gradient, a 1px "light-catch" border on the top, and a slight inset shadow when pressed. Text inside buttons uses the `label-caps` style in Navy for maximum contrast against the silver.
-   **Cards (Shelf Inserts):** These feature a subtle Oak grain texture background. They should have a 1px dark inner-stroke to simulate the gap between a shelf and its frame.
-   **Data Overlays:** Rectangular Navy panels with 85% opacity and a subtle silver border (0.5px). These house the technical data and measurements.
-   **Inputs:** Minimalist silver underlines or recessed navy boxes with oak-colored focus states. 
-   **Modularity Toggles:** Styled to look like physical sliding bolts or metal switches.
-   **Unit Indicators:** Small, silver-on-navy tags that display dimensions (e.g., "600mm"), using the `data-mono` typeface.