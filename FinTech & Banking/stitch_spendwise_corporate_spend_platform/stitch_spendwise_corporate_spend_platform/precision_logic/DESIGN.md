---
name: Precision Logic
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#3d4947'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#6d7a77'
  outline-variant: '#bcc9c6'
  surface-tint: '#006a61'
  primary: '#00685f'
  on-primary: '#ffffff'
  primary-container: '#008378'
  on-primary-container: '#f4fffc'
  inverse-primary: '#6bd8cb'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#545c72'
  on-tertiary: '#ffffff'
  tertiary-container: '#6c748b'
  on-tertiary-container: '#fefcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#89f5e7'
  primary-fixed-dim: '#6bd8cb'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#dae2fd'
  tertiary-fixed-dim: '#bec6e0'
  on-tertiary-fixed: '#131b2e'
  on-tertiary-fixed-variant: '#3f465c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  gutter: 20px
  margin: 32px
---

## Brand & Style

The design system is engineered for high-stakes corporate environments where precision and efficiency are paramount. The brand personality is technical, authoritative, and clinical, removing all unnecessary decorative elements to focus on data utility. 

The aesthetic follows a **Corporate Modern** style with a heavy emphasis on a **Bento-Box** layout. This approach organizes complex spend-management data into distinct, modular cells that allow for high information density without sacrificing clarity. The UI should evoke a sense of absolute control and systematic organization, making administrative tasks feel architectural and structured.

## Colors

The palette is anchored by **Teal (#0D9488)**, used strategically for primary actions and success states to provide a sense of financial health and precision. **Slate** serves as the structural backbone, with varying shades used for text hierarchy, borders, and iconography to maintain a professional, neutral tone. 

**Pure White (#FFFFFF)** is the canvas for all data containers to ensure maximum contrast for legibility. A very light Slate tint (#F8FAFC) is used for the global background to allow white "Bento" modules to visually pop. High-alert states should utilize a constrained red, while pending states use a muted amber, though these are secondary to the core Teal and Slate foundation.

## Typography

This design system utilizes **Space Grotesk** for headings and primary data visualizations to lean into the technical, geometric nature of financial management. Its unique letterforms provide a distinctive "tech" edge that differentiates the product from standard SaaS tools.

For all functional text, body copy, and dense data tables, **Inter** is the workhorse. It provides the necessary neutrality and exceptional legibility required for long-form administrative work. Numerical data should frequently use the "mono-data" style to ensure columns of figures align perfectly for easy scanning.

## Layout & Spacing

The layout utilizes a **12-column fluid grid** designed for desktop-first workflows. The primary structural motif is the **Bento Box**, where content is organized into "cells" of varying spans (e.g., a 4-column wide cell next to an 8-column wide cell).

A strict **4px baseline grid** governs all spacing units to maintain mathematical harmony. Information density is kept high by using 16px (sm) as the standard padding within modules, allowing more data to be visible above the fold. Gutters are fixed at 20px to provide clear separation between modules without wasting excessive screen real estate.

## Elevation & Depth

This design system avoids traditional heavy shadows in favor of **Tonal Layers and Low-Contrast Outlines**. Depth is communicated through surface color shifts rather than physical metaphors.

1. **Level 0 (Background):** Slate-50 (#F8FAFC).
2. **Level 1 (Bento Modules):** Pure White (#FFFFFF) with a 1px border in Slate-200.
3. **Level 2 (Active/Hover):** Pure White with a subtle, tight shadow (0px 2px 4px rgba(15, 23, 42, 0.05)) and a primary Teal border.
4. **Level 3 (Overlays/Modals):** Pure White with a medium-diffused shadow and a 1px Slate-300 border.

This approach keeps the UI feeling flat, fast, and modern, reducing visual noise for the user.

## Shapes

The shape language is disciplined and professional. A **Soft (0.25rem)** corner radius is the standard for almost all UI elements, including buttons, input fields, and small modules. This minimal rounding softens the technical edge just enough to feel modern without becoming "bubbly" or consumer-grade.

Larger bento-box containers may use **rounded-lg (0.5rem)** to define the primary layout blocks, creating a clear distinction between the container and the elements within it.

## Components

### Buttons
- **Primary:** Solid Teal (#0D9488) with white text. High-contrast, rectangular with 4px radius.
- **Secondary:** White background, Slate-200 border, Slate-700 text.
- **Ghost:** No border, Teal text. Used for low-priority actions in dense tables.

### Input Fields & Controls
- **Text Inputs:** White background, 1px Slate-300 border. Focus state uses a 1px Teal border and a faint Teal glow (2px).
- **Checkboxes:** Square with a 2px radius. When checked, solid Teal with a white tick.
- **Toggle Switches:** Small, technical profile. Slate-300 off, Teal on.

### Data Modules (Bento Cells)
- Each cell must have a clear "Label-MD" header and an optional "Actions" area in the top-right corner.
- Backgrounds are always Pure White to maintain high legibility against the Slate-50 background.

### Tables & Lists
- **Rows:** 40px height for high density. Subtle Slate-100 bottom border.
- **Header:** Slate-50 background with "Label-MD" typography for column titles.
- **Status Chips:** Small, pill-shaped tags with low-opacity Teal or Slate backgrounds and high-contrast text.

### Navigation
- A persistent left-hand sidebar in deep Slate (#0F172A) with Teal accents for active states. Icons should be stroke-based, 20px, with a technical, geometric style.