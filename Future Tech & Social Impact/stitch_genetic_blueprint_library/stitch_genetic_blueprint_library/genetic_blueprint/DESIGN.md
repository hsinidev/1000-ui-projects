---
name: Genetic Blueprint
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c4c6ce'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#8e9198'
  outline-variant: '#43474d'
  surface-tint: '#b1c8ec'
  primary: '#b1c8ec'
  on-primary: '#1a314e'
  primary-container: '#0a2440'
  on-primary-container: '#758cad'
  inverse-primary: '#49607f'
  secondary: '#d3fbff'
  on-secondary: '#00363a'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#2ae500'
  on-tertiary: '#053900'
  tertiary-container: '#032a00'
  on-tertiary-container: '#1ba000'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d3e3ff'
  primary-fixed-dim: '#b1c8ec'
  on-primary-fixed: '#011c38'
  on-primary-fixed-variant: '#314866'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#79ff5b'
  tertiary-fixed-dim: '#2ae500'
  on-tertiary-fixed: '#022100'
  on-tertiary-fixed-variant: '#095300'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  technical-label:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.1em
  code-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
spacing:
  base: 4px
  grid-unit: 32px
  gutter: 16px
  margin-edge: 48px
---

## Brand & Style

This design system is built upon the visual language of architectural drafting and technical schematics, repurposed for the high-precision world of genetic research. It evokes a sense of "work-in-progress" rigor—where every discovery is mapped, measured, and documented with absolute clarity.

The aesthetic combines **Minimalism** with **Structural Brutalism**. It prioritizes the "skeleton" of the interface, making the underlying grid and alignment guides visible to the user. This transparency fosters trust and suggests a high level of technical sophistication while remaining accessible through organized information hierarchy. The emotional response is one of intellectual calm, precision, and systemic order.

## Colors

The palette is rooted in the "Deep Blueprint Blue" which serves as the primary canvas, providing a high-contrast environment that reduces eye strain during long periods of data analysis.

*   **Primary:** A deep, authoritative navy that acts as the foundation.
*   **Secondary (Cyan):** Used for "active" drafting lines, selection states, and primary call-to-actions. It represents the "ink" of the blueprint.
*   **Tertiary (Molecular Green):** Reserved for success states, biological markers, and high-priority genetic data points.
*   **Neutral (Crisp White/Silver):** Used for primary text and structural notations to ensure maximum legibility against the dark background.
*   **Grid Color:** A muted version of the primary blue (#163A5F) used for the background graph lines and architectural guides.

## Typography

This design system utilizes a dual-font strategy to balance technical character with readability.

**Space Grotesk** is used for headlines, navigation, and technical notations. Its geometric construction mirrors the architectural aesthetic and provides a subtle "tech" feel without sacrificing clarity. All labels and metadata should be set in uppercase Space Grotesk to mimic drafting shorthand.

**Inter** is the workhorse for all body copy, documentation, and complex data descriptions. Its neutral, systematic nature ensures that dense genetic research papers remain legible and accessible.

Technical notations (e.g., coordinates, DNA sequences) should always use the `technical-label` or `code-data` styles to distinguish raw data from descriptive prose.

## Layout & Spacing

The layout is governed by a **Fixed Grid** system that is visually reinforced. A master 32px background grid is always visible, serving as the alignment anchor for all components.

*   **12-Column Structure:** Content is organized into a 12-column grid with 16px gutters.
*   **Visible Axes:** Main layout containers should feature thin (1px) border lines that extend slightly beyond the container edges, mimicking architectural "extension lines."
*   **Technical Offsets:** Small technical notations (e.g., "SEC_01", "REF_GRID_A") should be placed in the margins or at the intersection of grid lines to provide context for the data displayed.
*   **Padding:** Internal component padding should follow a strict 4px base increment to maintain rhythmic alignment with the background grid.

## Elevation & Depth

In keeping with the blueprint aesthetic, this design system avoids soft shadows and organic depth. Instead, hierarchy is conveyed through **Bold Borders** and **Tonal Layering**.

1.  **Level 0 (Floor):** The base blueprint grid (#0A2440).
2.  **Level 1 (Panels):** Slightly lighter blue surfaces (#0E2E52) with 1px solid borders (#1A4B84).
3.  **Level 2 (Modals/Overlays):** These use high-contrast white or cyan borders to "pop" from the background. 
4.  **Guides:** Non-interactive architectural guides (thin, dashed lines) are used to group related information visually without adding physical bulk to the UI.

Depth is purely structural, suggesting a flat drafting table rather than a 3D environment.

## Shapes

The shape language is strictly **Sharp (0)**. To maintain the precision of a technical drawing, all buttons, input fields, cards, and containers must have 90-degree corners.

Rounded corners are seen as "organic" and are reserved exclusively for biological data visualization (e.g., molecular diagrams, cell structures) to provide a visual distinction between the "system" and the "subject." UI elements themselves must remain architectural and rigid.

## Components

Components in this design system are treated as "schematic modules."

*   **Buttons:** Rectangular with a 1px border. Primary buttons use a solid Cyan fill with dark text. Secondary buttons are "ghost" style with Cyan borders and text. Use a "crosshair" icon on hover to reinforce the technical theme.
*   **Input Fields:** Bottom-border only, or full 1px border. Technical labels should float above the input in a smaller, uppercase `technical-label` style.
*   **Chips/Tags:** Small, sharp-edged rectangles. Use for genetic markers or status indicators. Success states use Molecular Green.
*   **Cards/Containers:** Must feature visible "corner marks" or coordinate notations (e.g., [42.01 // 88.04]) in the top-right corner to simulate data-mapping.
*   **Technical Diagrams:** Lines should be 1px thick. Use dashed lines for "projected" data and solid lines for "confirmed" data.
*   **Navigation:** A vertical "Explorer" style navigation on the left, using thin vertical rules to separate the menu from the main workspace.
*   **Data Tables:** Strict horizontal rules only. Use a hover-state that highlights the entire row in a faint Cyan tint to assist in tracking complex gene sequences.