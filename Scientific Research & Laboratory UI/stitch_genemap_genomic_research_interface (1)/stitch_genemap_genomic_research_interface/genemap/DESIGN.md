---
name: GeneMap
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
  on-surface-variant: '#434656'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004dea'
  primary: '#0041c8'
  on-primary: '#ffffff'
  primary-container: '#0055ff'
  on-primary-container: '#e3e6ff'
  inverse-primary: '#b6c4ff'
  secondary: '#545f73'
  on-secondary: '#ffffff'
  secondary-container: '#d5e0f8'
  on-secondary-container: '#586377'
  tertiary: '#1f44b9'
  on-tertiary: '#ffffff'
  tertiary-container: '#3e5ed2'
  on-tertiary-container: '#e3e6ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#001551'
  on-primary-fixed-variant: '#0039b3'
  secondary-fixed: '#d8e3fb'
  secondary-fixed-dim: '#bcc7de'
  on-secondary-fixed: '#111c2d'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#dde1ff'
  tertiary-fixed-dim: '#b7c4ff'
  on-tertiary-fixed: '#001453'
  on-tertiary-fixed-variant: '#0f3ab0'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  data-mono:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
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
  unit: 4px
  gutter: 16px
  margin: 24px
  density: compact
---

## Brand & Style

The design system is anchored in the concept of **Clinical Precision**. It targets a high-utility environment where researchers and bioinformaticians interact with massive datasets. The visual language must evoke a sense of absolute accuracy, sterility, and professional reliability. 

The chosen style is a hybrid of **Minimalism** and **Corporate/Modern**, characterized by high-density layouts that do not sacrifice clarity. By using a "Laboratory Blue" against a "Sterile White" canvas, the design system creates a vacuum-sealed environment where data is the focal point. Elements are defined by razor-sharp borders and subtle depth rather than expressive ornamentation, ensuring the interface feels like a sophisticated medical instrument.

## Colors

This design system utilizes a palette engineered for a high-tech clinical atmosphere. 

- **Primary (Laboratory Blue):** Used for primary actions, active states, and highlighting critical data paths.
- **Secondary (Graphite):** Provides the structural backbone for text, iconography, and navigation headers.
- **Neutral (Sterile White/Slate):** The background (#F8FAFC) and surface (#FFFFFF) colors are designed to minimize eye strain during long sequencing reviews.
- **Nucleotide Palette:** Dedicated, high-contrast tokens for genomic markers (A, C, G, T) are provided to ensure immediate pattern recognition within dense sequences.

## Typography

The design system relies exclusively on **Inter** for its neutral, systematic character. The typographic hierarchy is optimized for technical data visualization.

- **Headlines:** Use tighter letter spacing and semi-bold weights to anchor page sections.
- **Data Display:** For genomic sequences and coordinate data, use the `data-mono` variant or Inter with tabular lining figures to ensure vertical alignment across rows.
- **Labels:** Small, all-caps labels are used for metadata and table headers to distinguish them from editable content and primary readings.

## Layout & Spacing

This design system employs a **Fluid Grid** model with a 12-column structure, allowing the dashboard to scale from tablet screens to ultra-wide laboratory monitors. 

- **Density:** We utilize a 4px baseline grid. Padding and margins are kept tight (compact density) to maximize the "above-the-fold" data visibility.
- **Gutters:** A consistent 16px gutter ensures that while the layout is dense, data sets remain distinct and readable.
- **Alignment:** All elements must snap to the 4px grid to maintain the "precise" clinical aesthetic.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and **Low-contrast Outlines** rather than heavy shadows.

- **Surface Levels:** The base background is #F8FAFC. Active workspaces and cards use #FFFFFF with a 1px border (#E2E8F0).
- **Shadows:** When necessary for modals or dropdowns, use a "Hard Minimalist" shadow: a 2px offset with very low opacity (5-8%) to maintain the sterile, flat appearance.
- **Interactivity:** Elements "lift" slightly on hover using a subtle change in border color (from #E2E8F0 to #0055FF) rather than an increase in shadow depth.

## Shapes

The shape language of the design system is **Soft-Technical**. We avoid 0px sharp corners to prevent the UI from feeling dated or overly "brutalist," but we keep the radius tight to maintain a professional, instrument-like feel.

- **Primary Radius:** 4px (0.25rem) for buttons, input fields, and small cards.
- **Large Components:** 8px (0.5rem) for main content containers or modal windows.
- **Nucleotide Markers:** 2px radius for sequence blocks to keep them legible at very small sizes within high-density tables.

## Components

- **Data-Rich Tables:** The core component. Headers must be "Graphite" with 11px uppercase labels. Rows should use alternating zebra-striping (#F8FAFC) for readability. Cell padding should be fixed at 8px vertical.
- **Nucleotide Markers (A, C, G, T):** Small, rectangular badges using the status colors defined in the palette. Text must be high-contrast (white on color).
- **Interactive Chromosome Visualizations:** Use a 1px "Graphite" stroke for the chromosome outline. Hotspots for sequencing errors should use the "Thymine" red as a pulsating indicator.
- **Buttons:** Primary buttons are solid "Laboratory Blue" with white text. Secondary buttons use a 1px "Graphite" border with no fill.
- **Input Fields:** Use 1px "Graphite" borders (#334155 at 20% opacity). Focus states transition the border to "Laboratory Blue" with a 1px solid outer glow.
- **Action Chips:** Used for filtering genomic markers. These should be pill-shaped to differentiate them from the rectangular nucleotide badges.