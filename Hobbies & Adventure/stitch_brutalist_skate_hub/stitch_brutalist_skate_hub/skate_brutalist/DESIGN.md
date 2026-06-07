---
name: Skate Brutalist
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cfc4c5'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
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
  tertiary: '#ffb4a8'
  on-tertiary: '#690100'
  tertiary-container: '#000000'
  on-tertiary-container: '#ec0000'
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
  tertiary-fixed: '#ffdad4'
  tertiary-fixed-dim: '#ffb4a8'
  on-tertiary-fixed: '#410000'
  on-tertiary-fixed-variant: '#930100'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Epilogue
    fontSize: 96px
    fontWeight: '900'
    lineHeight: 90%
    letterSpacing: -0.05em
  h2:
    fontFamily: Epilogue
    fontSize: 64px
    fontWeight: '800'
    lineHeight: 100%
    letterSpacing: -0.03em
  h3:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 110%
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Epilogue
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 150%
    letterSpacing: '0'
  body-sm:
    fontFamily: Epilogue
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 160%
    letterSpacing: '0'
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 120%
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-page: 32px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 64px
---

## Brand & Style

This design system is built on the raw, unpolished energy of street skateboarding and industrial urbanism. It rejects the "clean" corporate aesthetic in favor of **Brutalism**, prioritizing structural honesty, heavy visual weight, and high-impact communication. The brand personality is aggressive, authentic, and unapologetic. 

The aesthetic is characterized by "glitch" elements, overlapping containers, and a total absence of traditional ornamentation like soft shadows or gradients. Every element serves a functional purpose, rendered with a ruggedness that mirrors the concrete environments where skate culture thrives. The UI should feel like a physical fanzine or a high-end streetwear editorial—bold, loud, and tactile.

## Colors

The palette is strictly high-contrast monochrome, utilizing a pure black base for a "void" effect and stark white for structural elements. 

- **Primary & Background:** Solid #000000. Large blocks of black create the "industrial floor" for the design.
- **Contrast & Text:** Solid #FFFFFF. Used for primary legibility and heavy borders.
- **The "Vandal" Red:** #FF0000 is used exclusively for calls to action, critical alerts, and brand accents. It should feel like spray paint on concrete—jarring and impossible to ignore.
- **Industrial Grey:** #1A1A1A is used sparingly for subtle depth or to distinguish between adjacent black containers without sacrificing the high-contrast feel.

## Typography

This design system uses **Epilogue** for its aggressive weight and editorial presence. Headings are massive, often breaking standard margin rules or overlapping imagery. Tight line-height and negative letter-spacing on display text create a sense of density and "block" structure.

**Space Grotesk** provides the technical, industrial counterpoint. It is used for all metadata, labels, and system data. These labels should always be rendered in uppercase with generous letter-spacing to mimic industrial stencil markings or technical blueprints.

## Layout & Spacing

The layout is a **12-column fluid grid** but used asymmetrically. Elements should rarely be centered; instead, they should "crash" into the edges of the viewport or stack with intentional misalignment. 

- **Gutter Logic:** Gutters are kept tight (16px) to maintain a sense of structural density.
- **Asymmetry:** Large-scale headlines should often span across 8-10 columns, leaving the remaining columns for technical "data" labels or vertical navigation elements.
- **Negative Space:** Use massive vertical gaps (64px+) between sections to allow the heavy typography room to breathe, contrasted by very tight internal padding within containers.

## Elevation & Depth

This design system completely avoids the Z-axis. Depth is conveyed through **overlapping layers** and **heavy borders**, not shadows or blurs.

- **Hard Borders:** Every container must have a minimum 2px or 4px solid border. 
- **Offsets:** To indicate "active" or "raised" states, components use a physical offset (e.g., a button moving 4px down and right) rather than a shadow.
- **High-Contrast Layering:** White containers sit directly on black backgrounds. If a secondary layer is needed, use a solid #FF0000 block offset behind the primary container to create a "shadow" effect using a solid color.

## Shapes

The shape language is strictly **geometric and sharp**. No border-radii are permitted. Every corner is a 90-degree angle to reinforce the industrial, architectural feel of the brand.

Containers should often feature "cut" corners or stepped edges (using clip-paths) to mimic the appearance of industrial metal plating or photocopied "zine" cutouts. Use 45-degree angles sparingly for specific UI accents or directional arrows.

## Components

### Buttons
Buttons are solid blocks. The primary state is a white background with black text. On hover, the button flashes to #FF0000. For an "industrial" feel, use a 4px black border with a 4px white offset to create a faux-3D effect that collapses when clicked.

### Input Fields
Fields are defined by a 2px white bottom border only, or a full 2px border box with no rounded corners. Labels sit above the field in the Space Grotesk "label-mono" style. Error states are signaled by the entire border and text turning #FF0000.

### Cards
Cards use a black background with a 2px white border. Imagery within cards should use a high-contrast, grainy black-and-white filter. Titles should overlap the card's edge, breaking the border containment.

### Chips & Tags
Rendered as small, rectangular boxes with "label-mono" text. They should look like physical labels or stickers stuck onto the UI.

### Icons
Icons must be stroke-based, using a consistent 2px weight with sharp caps and joins. Avoid "cute" or rounded iconography; prioritize symbols that feel like industrial stencils or warning signs.