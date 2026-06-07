---
name: LabNetwork Research Framework
colors:
  surface: '#f6faf9'
  surface-dim: '#d7dbda'
  surface-bright: '#f6faf9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f4'
  surface-container: '#ebefee'
  surface-container-high: '#e5e9e8'
  surface-container-highest: '#dfe3e3'
  on-surface: '#181c1c'
  on-surface-variant: '#3e4949'
  inverse-surface: '#2d3131'
  inverse-on-surface: '#eef1f1'
  outline: '#6e7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#00696b'
  primary: '#005f61'
  on-primary: '#ffffff'
  primary-container: '#007a7c'
  on-primary-container: '#b3feff'
  inverse-primary: '#7ad5d7'
  secondary: '#5b5f60'
  on-secondary: '#ffffff'
  secondary-container: '#e0e3e4'
  on-secondary-container: '#616566'
  tertiary: '#525656'
  on-tertiary: '#ffffff'
  tertiary-container: '#6a6e6e'
  on-tertiary-container: '#eef1f1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#97f2f3'
  primary-fixed-dim: '#7ad5d7'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f51'
  secondary-fixed: '#e0e3e4'
  secondary-fixed-dim: '#c4c7c8'
  on-secondary-fixed: '#181c1d'
  on-secondary-fixed-variant: '#434748'
  tertiary-fixed: '#e0e3e3'
  tertiary-fixed-dim: '#c4c7c7'
  on-tertiary-fixed: '#181c1d'
  on-tertiary-fixed-variant: '#434748'
  background: '#f6faf9'
  on-background: '#181c1c'
  surface-variant: '#dfe3e3'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1440px
  bento-gap: 16px
---

## Brand & Style

The design system is engineered for the intersection of high-level academic research and corporate efficiency. It evokes a "Scientific-Corporate" personality: precise, authoritative, and clinical yet accessible. The target audience includes principal investigators, grant administrators, and laboratory technicians who require a high-density information environment that minimizes cognitive load.

The visual style is a refined **Minimalism** blended with **Corporate Modernism**. It prioritizes clarity through a bento-box structural logic, utilizing subtle borders and generous whitespace to segment complex data sets. The aesthetic response should be one of "structured discovery"—where the user feels the platform is as organized and rigorous as the scientific methods they employ.

## Colors

The color palette is anchored by **Teal**, representing the precision of scientific inquiry and institutional trust. **Charcoal** provides professional depth, used primarily for typography and structural elements to ensure high legibility. 

The background architecture utilizes a layered approach of **White** and **Light Grey** to create natural containment for bento-style modules. An **Aqua/Mint accent** is reserved strictly for interactive highlights, status indicators, and progress tracking, ensuring these elements "pop" against the more sober primary palette. High-contrast ratios are maintained throughout to meet accessibility standards for data-heavy views.

## Typography

This design system utilizes a dual-font strategy to balance technical innovation with readability. **Space Grotesk** is used for headlines to provide a subtle "lab-tech" and geometric edge, reinforcing the scientific nature of the platform. **Inter** serves as the primary workhorse for body copy and UI elements due to its exceptional legibility in data-heavy contexts.

For specialized data views, such as grant IDs or equipment serial numbers, a monospace fallback is specified to ensure character alignment and a "data-first" feel. Hierarchy is established through weight and color (Charcoal for headers, Mid-Grey for secondary labels) rather than excessive size variation.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop views, centering content within a 1440px container to ensure focus. The structural foundation is the "Bento-Box" layout—a modular grid where content is housed in discrete, rectangular containers of varying sizes.

A 12-column grid system is used, with a standard 24px gutter. Modules should snap to grid increments, using a 16px gap between adjacent boxes. Whitespace is treated as a functional tool; generous internal padding (minimum 24px) within modules prevents the UI from feeling claustrophobic, despite the high density of scientific data.

## Elevation & Depth

To maintain a clean, "sterile" laboratory aesthetic, this design system rejects heavy shadows. Depth is achieved through **Tonal Layering** and **Subtle Borders**. 

1.  **Background:** The lowest layer is the light grey neutral base.
2.  **Bento Modules:** These sit on the background, filled with solid white and defined by a 1px subtle border (#E5E7EB).
3.  **Active States:** Only active or hovered elements receive a very soft, ambient shadow (6% opacity Charcoal) to indicate interactivity.
4.  **Overlays:** Modals and tooltips use a slightly more pronounced shadow with a tight blur radius to maintain the crisp, professional look.

## Shapes

The shape language is "Soft-Technical." Elements use a consistent **0.25rem (4px)** corner radius. This small radius softens the "brutalist" edge of a pure grid while maintaining a rigorous, institutional appearance. 

Buttons and input fields follow this 4px rule, while larger bento containers may scale up to a **0.5rem (8px)** radius to better frame their internal content. Circular shapes are reserved exclusively for avatars and status pips to create a clear visual distinction from structural UI elements.

## Components

**Buttons:** 
Primary buttons use the Teal base with white text. Secondary buttons use a ghost style with a Charcoal border. Both feature 4px corners and Inter Medium typography.

**Bento Cards:** 
The core container. Must include a consistent header area with a "Label-Caps" title and an optional icon slot. Icons for equipment, grants, and publications should be thin-stroke (1.5pt) and monochromatic.

**Data Tables:** 
High-density tables with no vertical borders. Row zebra-striping uses the tertiary light-teal tint on hover. Column headers use the "Label-Caps" typography style.

**Chips & Status:** 
Used for "Publication Status" or "Grant Type." These are small, pill-shaped elements with low-saturation background tints (e.g., soft mint for 'Active', soft charcoal for 'Archived').

**Input Fields:** 
Standardized with a 1px border. On focus, the border transitions to Primary Teal with a subtle 2px outer glow of the Accent Aqua.

**Institutional Accents:** 
Incorporate small "breadcrumb" trails and metadata strings at the bottom of cards to provide persistent context without cluttering the primary view.