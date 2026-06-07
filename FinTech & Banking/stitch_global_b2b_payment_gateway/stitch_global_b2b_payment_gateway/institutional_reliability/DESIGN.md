---
name: Institutional Reliability
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e3'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3fd'
  surface-container: '#eeedf7'
  surface-container-high: '#e8e7f1'
  surface-container-highest: '#e2e1eb'
  on-surface: '#1a1b22'
  on-surface-variant: '#444653'
  inverse-surface: '#2f3037'
  inverse-on-surface: '#f1f0fa'
  outline: '#747685'
  outline-variant: '#c4c5d5'
  surface-tint: '#3056c4'
  primary: '#002576'
  on-primary: '#ffffff'
  primary-container: '#0038a8'
  on-primary-container: '#96adff'
  inverse-primary: '#b6c4ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#591400'
  on-tertiary: '#ffffff'
  tertiary-container: '#802100'
  on-tertiary-container: '#ff9474'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#00164f'
  on-primary-fixed-variant: '#093cab'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdbd1'
  tertiary-fixed-dim: '#ffb59f'
  on-tertiary-fixed: '#3a0a00'
  on-tertiary-fixed-variant: '#852402'
  background: '#faf8ff'
  on-background: '#1a1b22'
  surface-variant: '#e2e1eb'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-base:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  data-mono:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
  container-max: 1280px
---

## Brand & Style
The design system is engineered for the high-stakes environment of B2B cross-border finance. The brand personality is institutional, authoritative, and unfailingly precise. It prioritizes clarity over decoration, ensuring that users moving significant capital feel a sense of security and control.

The visual direction follows a **Corporate / Modern** style. It utilizes a restrained aesthetic that mirrors the stability of a global bank while maintaining the efficiency of a modern SaaS platform. Every element is designed to reduce cognitive load, using purposeful whitespace to separate complex data sets and ensuring that "High-Trust" moments—such as final transaction confirmations—are visually distinct and grounded.

## Colors
The palette is anchored by a deep Royal Blue, selected for its historical association with institutional banking and global commerce. This primary color is used sparingly for key actions and branding to maintain its impact.

The background is a crisp, clinical White, providing the highest possible contrast for data legibility. Accents and primary text utilize Slate, which offers a softer, more professional alternative to pure black, reducing eye strain during prolonged financial auditing. A secondary palette of Slate and light gray tones is used for structural borders and UI metadata. Semantic colors (Green for successful transfers, Red for alerts) are strictly reserved for status communication.

## Typography
This design system utilizes **Public Sans**, an institutional-grade typeface designed for clarity and neutrality. It excels in financial interfaces where tabular figures and technical labels must be scanned rapidly without ambiguity.

A strict hierarchy is maintained: Headings use a heavier weight and tighter tracking to feel "anchored" to the page. Body text is optimized for readability with a generous line height. For financial figures and exchange rates, we use a medium weight with slightly increased letter spacing to ensure each digit is distinct, preventing errors in data entry or interpretation.

## Layout & Spacing
The layout follows a **Fixed Grid** model for the main dashboard to ensure that data tables and financial modules maintain predictable widths across desktop environments. A 12-column grid is used, with generous 24px gutters to prevent information density from feeling overwhelming.

Spacing is governed by an 8px linear scale. We prioritize "Ample Whitespace" to group related financial information, using larger gaps (40px+) to separate distinct functional sections like "Current Balances" from "Recent Transactions." This spatial breathing room is critical for error prevention in B2B workflows.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and subtle **Ambient Shadows**. Instead of aggressive floating effects, the design system uses surface-on-surface separation. 

The primary background is White, while secondary modules or navigation sidebars use a very light Slate tint (#F8FAFC). When depth is required—such as for modal dialogs or dropdown menus—we use a soft, large-radius shadow with a low-opacity Slate tint (Alpha 8-12%). This "diffused" look ensures the UI feels modern and light rather than heavy or dated. Borders are thin (1px) and use a low-contrast Slate-200 color to define boundaries without adding visual noise.

## Shapes
The shape language is defined as **Soft**. UI elements utilize a 4px (0.25rem) corner radius. This subtle rounding softens the "brutality" of a pure corporate grid while maintaining a precise, engineering-led aesthetic.

Larger components, like cards containing financial summaries, may use the `rounded-lg` (8px) token to feel more approachable as container elements. Buttons and input fields must strictly adhere to the 4px standard to ensure they look functional and efficient. Circles are reserved exclusively for avatars or status indicators to provide a sharp contrast to the predominantly rectangular UI.

## Components
Consistent application of these components ensures the interface feels like a professional financial instrument:

- **Professional Data Tables:** These are the core of the system. They feature a "Slate-50" header background, no vertical borders, and a 1px Slate-200 bottom border for rows. Hover states use a subtle tint to aid tracking across wide screens.
- **Buttons:** Primary buttons are solid Royal Blue with white text. Secondary buttons use a Slate-100 ghost style. The shape is strictly 4px rounded.
- **Secure Badges:** Trust elements (e.g., "SSL Encrypted" or "Verified Recipient") use a small "label-caps" font with a tiny shield icon and a soft blue background tint.
- **Clear Fee Breakdowns:** These are styled as "Summary Cards" with a light Slate background, using distinct line items and a bold Royal Blue total to ensure total transparency before any funds are moved.
- **Input Fields:** These have a 1px Slate-300 border that thickens and changes to Royal Blue on focus. Use placeholder text sparingly to keep the interface clean; prioritize persistent labels.
- **Status Chips:** High-contrast text on low-contrast backgrounds (e.g., dark green text on light green background) for "Completed," "Pending," or "Flagged" states.