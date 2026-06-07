---
name: EquityFlow
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#464651'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#777682'
  outline-variant: '#c7c5d3'
  surface-tint: '#5156a7'
  primary: '#15196c'
  on-primary: '#ffffff'
  primary-container: '#2d3282'
  on-primary-container: '#999ff5'
  inverse-primary: '#bfc2ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#232628'
  on-tertiary: '#ffffff'
  tertiary-container: '#393c3e'
  on-tertiary-container: '#a4a6a8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bfc2ff'
  on-primary-fixed: '#070963'
  on-primary-fixed-variant: '#393e8e'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  h1:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  mono-data:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 24px
  margin: 32px
  density-tight: 8px
  density-comfy: 16px
---

## Brand & Style

This design system is built for the high-stakes environment of cap-table management and venture equity. It reflects a brand personality that is authoritative, mathematically precise, and technologically forward-thinking. The target audience—founders, legal counsel, and investors—requires a UI that prioritizes clarity over decoration and speed over flourish.

The visual style is **Corporate / Modern** with a lean towards **Minimalism**. It utilizes high-contrast boundaries and a rigid structural grid to convey a sense of stability and legal rigor. The emotional response should be one of "effortless control"—transforming complex financial data into actionable, legible insights.

## Colors

The palette is anchored by **Deep Indigo**, used to establish institutional trust and hierarchy in navigation and primary actions. **Mint** serves as a high-visibility accent, reserved specifically for growth indicators, positive equity shifts, and success states, ensuring it remains a meaningful "signal" in a data-heavy environment.

The background is a crisp **White**, providing the necessary canvas for high-contrast text. A secondary neutral scale of slates and grays is employed to manage data density, helping to separate tiers of information in tables and charts without adding visual noise.

## Typography

The design system utilizes **Inter** for all UI elements to maximize legibility at small scale. The typographic hierarchy is designed for **data density**, utilizing a tighter line-height for tables and labels to allow more information to be visible above the fold. 

Headlines use a semi-bold weight and slight negative letter-spacing for a modern, "tech" appearance. For numerical equity values and share counts, a monospaced alternative or tabular figures (tnum) must be used to ensure columns of numbers align perfectly for easy comparison.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop dashboards, centering content within a 1440px max-width container to maintain ocular comfort. A 12-column system is used to organize complex dashboards, with elements spanning 3, 4, 6, or 12 columns.

The spacing rhythm is based on a 4px baseline. To achieve high data density, internal padding within data tables and sidebars should adhere to the `density-tight` scale, while primary page sections use `density-comfy` to provide breathing room between distinct functional blocks.

## Elevation & Depth

Visual hierarchy in the design system is achieved through **low-contrast outlines** and **tonal layers** rather than heavy shadows. Surfaces are separated by 1px borders in a light slate gray (#E2E8F0), creating a blueprint-like precision.

When depth is required for interactive overlays (like modals or dropdowns), the design system uses **ambient shadows**: extra-diffused, 10-15% opacity shadows with a slight indigo tint. This prevents the UI from feeling flat while avoiding the "fuzzy" look of traditional skeuomorphism. Background blurs are used sparingly on sticky headers to maintain context during scrolling.

## Shapes

The shape language is disciplined and professional. A **Soft (0.25rem)** roundedness is applied to standard components like buttons and input fields to prevent the UI from feeling aggressive. Larger containers, such as data cards and document viewers, use a slightly more pronounced **0.5rem (rounded-lg)** to soften the overall layout. 

Interactive nodes in timelines and status indicators may use pill-shaped (fully rounded) geometry to distinguish them from structural, rectangular elements.

## Components

### Buttons & Inputs
Buttons use solid Deep Indigo for primary actions and Mint for positive outcomes (e.g., "Issue Shares"). Inputs feature a 1px border that shifts to Indigo on focus, with labels always positioned above the field in the `label-sm` style for maximum clarity.

### Interactive Charts
Charts must prioritize accuracy over aesthetics. Use Mint for "Active/Vested" lines and Indigo for "Total Diluted" views. Tooltips should have a dark neutral background with white mono-spaced text for precise data reading.

### Timelines
Equity events are displayed on a vertical timeline. Each node is a 12px Mint circle. Connecting lines are thin 2px slate. This vertical orientation allows for infinite scrolling of a company's historical cap table changes.

### Document Viewers
For legal contracts and option agreements, the viewer uses a "Paper" container style—a white surface with a subtle 1px border, centered on a light gray background. This provides high contrast for long-form reading of legal text.

### Data Tables
Tables are the heart of the design system. They feature sticky headers, alternating row stripes (zebra striping) using the tertiary color, and right-aligned numerical columns to ensure mathematical legibility.