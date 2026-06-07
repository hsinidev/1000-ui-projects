---
name: Muse-Board
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#cfc4c5'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#988e90'
  outline-variant: '#4c4546'
  surface-tint: '#c6c6c6'
  primary: '#c6c6c6'
  on-primary: '#303030'
  primary-container: '#000000'
  on-primary-container: '#757575'
  inverse-primary: '#5e5e5e'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c6c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#000000'
  on-tertiary-container: '#757575'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Montserrat
    fontSize: 80px
    fontWeight: '800'
    lineHeight: 88px
    letterSpacing: -0.04em
  h1:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  h2:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  body-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 30px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  bento-gap: 2px
  container-padding: 32px
---

## Brand & Style

This design system is engineered for high-end digital collaboration, blending the raw utility of a professional drafting table with the sleek aesthetics of a modern art gallery. The brand personality is unapologetically bold and high-fidelity, designed to feel responsive and premium on large-scale 4K touch displays.

The visual language utilizes a "Bento-box" structural philosophy—organizing complex toolsets and canvases into clean, modular compartments. The aesthetic merges **Glassmorphism** for floating interface elements with **High-Contrast Minimalism**. By using a foundation of absolute blacks and whites punctuated by neon-electric accents, the system ensures that user content remains the focal point while the interface feels like a sophisticated instrument.

## Colors

The palette is anchored by a "True Dark" foundation, utilizing **Deep Black (#000000)** as the primary canvas color to maximize contrast and depth on high-resolution panels. **Pure White (#FFFFFF)** is reserved for primary structural boundaries, typography, and iconography.

Accents are used surgically to denote interaction and ownership:
- **Electric Blue:** Primary action states and tool highlights.
- **Acid Green:** Positive states, active collaborations, and "Go" signals.
- **Hot Pink:** User-specific cursors and secondary selection highlights.
- **Bright Orange:** Critical alerts and technical annotations.

The interface utilizes a "Glass" layer for floating toolbars, allowing background content to remain partially visible via a highly refined backdrop blur.

## Typography

The typographic hierarchy distinguishes between creative expression and technical precision. **Montserrat** is used for high-impact headings, providing a geometric, urban weight that feels architectural. **Inter** handles standard UI labels and body text for maximum legibility at various viewing distances.

For technical metadata, coordinate systems, and drafting specs, **JetBrains Mono** is employed. This monospaced font ensures that numerical data is perfectly aligned and distinct from the creative labels, reinforcing the "professional tool" aesthetic.

## Layout & Spacing

This design system uses a **Bento-box layout** model. Content is organized into rigid, high-contrast rectangular containers that sit flush against one another or with minimal "micro-gutters" (2px). On a 4K display, the layout operates on a 12-column fluid grid, but components within the grid behave as independent "tiles."

Padding within tiles is generous (24px - 40px) to accommodate touch interaction, ensuring that targets are easily tappable without visual clutter. The "Tactile" feel is achieved through consistent 8px increments, creating a rhythmic, structured environment for professional drafting.

## Elevation & Depth

Hierarchy is established through a combination of **High-Contrast Outlines** and **Fluid Shadows**.

1.  **Base Layer:** Deep Black (#000000) canvas.
2.  **Container Layer:** Outlined with a 1px Pure White border at 20% opacity.
3.  **Floating Toolbars:** These utilize Glassmorphism (20px backdrop blur) with a 1px solid Pure White border.
4.  **Active Elevation:** When an element is picked up or "active," it casts a large, fluid, low-opacity shadow (40px blur, 10% opacity) and increases its border opacity to 100%.

Depth is not simulated through gradients but through the stacking of translucent materials and crisp, luminous boundaries.

## Shapes

The shape language is "Soft-Technical." We avoid aggressive rounding to maintain a professional, drafting-software feel. A base radius of **4px (0.25rem)** is applied to all standard Bento boxes and input fields. 

Larger containers or "Hero" tiles may use an **8px (0.5rem)** radius. Interactive cursors and "Pill" labels are the only elements allowed to be fully circular, providing a visual distinction between the "content containers" (square-ish) and the "interaction agents" (round).

## Components

### Buttons & Inputs
Buttons are rendered as high-contrast blocks. The primary action button is Pure White with Deep Black text. Secondary buttons are "Ghost" style with 1px white borders. Input fields are Deep Black with a 1px bottom-border, switching to an Electric Blue border on focus.

### Cursors & Active States
In a collaborative environment, each user is assigned one of the accent colors. Their cursor, selection boxes, and "Currently Editing" outlines adopt that specific accent color (e.g., Hot Pink or Acid Green).

### Bento Tiles
Tiles act as the primary organizational unit. Each tile should have a `mono-label` in the top-left corner, providing a technical name for the module (e.g., "LAYER_01" or "COLOR_PICKER").

### Toolbars
Floating toolbars use the glassmorphic style. Icons within toolbars are stroke-based (1.5px weight) and Pure White. When a tool is selected, the icon container fills with the Electric Blue accent.

### Chips & Badges
Small, monospaced badges used for status or tagging. These should be framed in a 1px border with no fill, using the accent colors to denote category or priority.