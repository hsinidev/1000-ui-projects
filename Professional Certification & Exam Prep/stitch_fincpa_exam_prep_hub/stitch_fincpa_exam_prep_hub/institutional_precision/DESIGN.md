---
name: Institutional Precision
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#444653'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#747684'
  outline-variant: '#c4c5d5'
  surface-tint: '#3557bc'
  primary: '#002068'
  on-primary: '#ffffff'
  primary-container: '#003399'
  on-primary-container: '#8aa4ff'
  inverse-primary: '#b5c4ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#4f1100'
  on-tertiary: '#ffffff'
  tertiary-container: '#751d00'
  on-tertiary-container: '#ff8561'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b5c4ff'
  on-primary-fixed: '#00164e'
  on-primary-fixed-variant: '#153ea3'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdbd1'
  tertiary-fixed-dim: '#ffb59f'
  on-tertiary-fixed: '#3a0a00'
  on-tertiary-fixed-variant: '#832707'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  table-data:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
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
  xl: 48px
  xxl: 80px
---

## Brand & Style

The brand personality is rooted in institutional reliability and intellectual rigor. This design system is built for the aspiring professional, evoking the focused atmosphere of a high-stakes accounting firm or a secure testing center. The aesthetic balances the warmth of a mentor with the exacting standards of an auditor.

The chosen style is **Corporate / Modern**, leaning heavily into **Minimalism**. By prioritizing whitespace and structural alignment over decorative elements, the UI minimizes cognitive load during intense study sessions. The visual language conveys security through stability, using a rigid grid and clear information architecture to ensure the platform feels organized and unbreakable.

## Colors

The palette is anchored by a commanding **Royal Blue**, a color synonymous with financial stability and authority. This is used for primary actions, progress indicators, and key navigational landmarks. 

The neutral scale is composed of **Slate Grey**, moving from deep charcoal for text to airy silvers for borders and backgrounds. This cool-toned neutral palette avoids the "muddy" feel of warmer greys, maintaining the "crisp white" environment required for long-form reading. Functional colors (Success/Error) are dialed back in saturation to remain professional while providing clear feedback during practice exams.

## Typography

**Public Sans** was selected for its institutional heritage and exceptional clarity in data-dense environments. It is a neutral, systematic face that performs well in the complex tables typical of CPA financial statements.

To maintain an "audit-ready" feel, use **tabular figures** (monospaced numbers) for all financial data to ensure columns of figures align perfectly. Headlines should use tighter letter-spacing for a sophisticated, editorial look, while body copy maintains a generous line height (1.6) to reduce eye strain during multi-hour study sessions.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to ensure content feels anchored and intentional. The layout is centered on a 12-column grid with a maximum width of 1280px, providing a stable frame for complex dashboards and exam modules.

The spacing rhythm is strictly derived from a 4px baseline. Use `md (16px)` for standard padding within components and `lg (24px)` for gutters between major UI sections. Large vertical gaps `xxl (80px)` should be used to separate distinct stages of a user's workflow, reinforcing the sense of an organized, step-by-step preparation process.

## Elevation & Depth

To maintain a "structured" and "precise" aesthetic, this design system avoids heavy, ambient shadows. Instead, it relies on **Low-contrast outlines** and **Tonal layers**.

Hierarchy is established through surface color shifts and subtle 1px borders. A "Secondary" surface might be a light Slate Grey (#F8FAFC) against the "Primary" white background. When depth is absolutely necessary (such as for a dropdown or a modal), use a "Technical Shadow": a sharp, 1px-2px blur with very low opacity (10%), mimicking the look of stacked paper rather than floating elements. This keeps the UI grounded and "audit-ready."

## Shapes

The shape language is conservative and geometric. A **Soft (Level 1)** roundedness is applied to ensure the UI feels modern and approachable without losing its professional edge. 

Corners for primary components like buttons and input fields are set to 4px. This small radius provides just enough softness to be comfortable on the eyes while retaining the rigid, boxy structure expected in financial and government-adjacent platforms. Larger containers, like cards or panels, should use the same 4px radius to maintain a consistent "modular" look.

## Components

### Buttons
Buttons are strictly rectangular with 4px corners. Primary buttons use the Royal Blue background with white text. Secondary buttons use a Slate Grey border (1px) with Royal Blue text. Text within buttons should be semi-bold and center-aligned.

### Input Fields & Selects
Inputs must have a clearly defined 1px border using Slate Grey. Labels should always be visible (never floating) and positioned above the field in `body-sm` weight for maximum legibility. The active state is indicated by a 2px Royal Blue border—no glow.

### Audit Tables
The centerpiece of this design system. Tables feature a Slate-50 background for headers and a subtle 1px bottom border for rows. There is no zebra-striping; instead, use vertical cell dividers for data-heavy financial statements. All numerical data must be right-aligned and use tabular figures.

### Progress Indicators
Preparation progress should be shown via "Segmented Progress Bars"—discrete blocks that fill with Royal Blue. This visualizes the exam sections as individual modules that have been "verified" or "audited."

### Chips & Badges
Used for status (e.g., "Correct", "Flagged", "Under Review"). These use a subtle tonal fill (10% opacity of the accent color) and a bold version of the text color to ensure they are legible but not distracting from the primary content.