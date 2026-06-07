---
name: Equilibrium
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
  tertiary: '#924628'
  on-tertiary: '#ffffff'
  tertiary-container: '#b05e3d'
  on-tertiary-container: '#fffbff'
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
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#ffb59a'
  on-tertiary-fixed: '#370e00'
  on-tertiary-fixed-variant: '#773215'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 28px
  body-base:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
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
  xl: 40px
  container-max: 1440px
  gutter: 20px
---

## Brand & Style

The design system is engineered for the intersection of high-frequency Web3 data and institutional accounting standards. The brand personality is clinical, authoritative, and frictionless, aimed at CFOs, tax professionals, and high-net-worth crypto investors who require absolute precision.

The style is **Corporate-Modern Minimalism**. It avoids the "gamified" tropes of consumer crypto apps, opting instead for a structured, grid-based aesthetic that prioritizes information density without sacrificing clarity. Visual interest is generated through perfect alignment, purposeful whitespace, and a disciplined application of the primary accent color. The goal is to evoke a sense of calm reliability amidst the volatility of blockchain data.

## Colors

The palette is restricted to ensure focus on financial figures. 
- **Teal (Primary):** Used exclusively for primary actions, active states, and interactive data points. It represents growth and precision.
- **Slate (Secondary/Text):** Provides a high-contrast, professional reading experience. Deep slate is used for headings, while medium slate handles metadata.
- **Pure White (Background):** The canvas for all operations. Using white instead of off-white maintains a clinical, "paper-like" compliance feel.
- **Surface Neutrals:** Cool grays (Slate-50) are used to define table headers and sidebar backgrounds to subtly separate the navigation from the workspace.

## Typography

**Inter** is selected for its exceptional legibility in data-heavy environments and its extensive support for tabular numerals—critical for aligning currency values and wallet addresses.

Headings use a semi-bold weight with tight tracking to feel "architectural." Body copy is kept at 14px to maximize information density on dashboard views. For financial tables, the `tnum` (tabular numbers) OpenType feature must be enabled to ensure that columns of figures align vertically, allowing users to scan for discrepancies instantly. Label styles use uppercase tracking to differentiate metadata from primary data points.

## Layout & Spacing

This design system utilizes a **Fixed-Fluid Hybrid Grid**. The main content area is capped at 1440px to prevent excessive line lengths in data tables, while the navigation remains anchored. 

A strict 4px baseline grid ensures vertical rhythm. Padding within data cells is kept tight (8px vertical) to maximize the "above-the-fold" visibility of transactions. Large margins (40px+) are used only to separate high-level functional blocks (e.g., the transition from a summary header to the main ledger). Use "Negative Space" as a structural tool to group related data without the need for heavy lines.

## Elevation & Depth

To maintain a "Corporate-Clean" aesthetic, depth is achieved through **Low-contrast outlines** and **Tonal layering** rather than heavy shadows. 

- **Level 0 (Base):** Pure White (#FFFFFF).
- **Level 1 (Surface):** Slate-50 (#F8FAFC) used for sidebars and header backgrounds.
- **Level 2 (Cards/Containers):** Pure White with a 1px border in Slate-200. No shadow is applied to cards in their default state.
- **Interactions:** A subtle, highly diffused shadow (0px 4px 12px rgba(15, 23, 42, 0.05)) is reserved exclusively for dropdown menus and active modal dialogs to "lift" them above the data grid.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding takes the "edge" off the data-dense UI, making it feel modern and accessible, while the relatively sharp corners maintain a professional, institutional character.

- **Standard Buttons & Inputs:** 4px radius.
- **Data Tags/Chips:** 4px radius (never fully rounded pills, to maintain the architectural feel).
- **Selection Indicators:** Vertical bars (4px wide) on the left edge of active list items.

## Components

- **Buttons:** Primary buttons use a solid Teal fill with white text. Secondary buttons use a Slate-200 border and Slate-700 text. Use "Ghost" buttons for tertiary actions within tables to reduce visual noise.
- **Data Tables:** The core component. Rows must have a subtle hover state (#F8FAFC). Borders should be horizontal-only to emphasize the flow of data across the screen. Use a monospaced-adjacent font setting for transaction hashes.
- **Input Fields:** Use a 1px Slate-200 border. On focus, the border transitions to Teal with a 2px "glow" (not a shadow, but a soft outer stroke).
- **Status Chips:** Small, square-cornered labels. Use low-saturation backgrounds (e.g., light green background with dark green text) for "Synced," "Taxable," or "Flagged" states.
- **Summary Cards:** Large-format numbers (KPIs) should be displayed in Semi-Bold Slate-900 with a subtle Teal bottom-border (2px) to denote importance.
- **Audit Logs:** Use a specialized list component with timestamps in 11px Label-Caps to provide a non-intrusive trail of automated accounting actions.