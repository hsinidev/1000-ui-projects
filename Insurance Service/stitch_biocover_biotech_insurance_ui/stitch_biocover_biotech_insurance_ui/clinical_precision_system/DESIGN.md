---
name: Clinical Precision System
colors:
  surface: '#fcf8fa'
  surface-dim: '#dcd9db'
  surface-bright: '#fcf8fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f5'
  surface-container: '#f0edef'
  surface-container-high: '#eae7e9'
  surface-container-highest: '#e4e2e4'
  on-surface: '#1b1b1d'
  on-surface-variant: '#45464d'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f2'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#271901'
  on-tertiary-container: '#98805d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#fcdeb5'
  tertiary-fixed-dim: '#dec29a'
  on-tertiary-fixed: '#271901'
  on-tertiary-fixed-variant: '#574425'
  background: '#fcf8fa'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
typography:
  h1:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
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
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 16px
  gutter: 12px
---

## Brand & Style

The brand identity centers on "Technical Authority." It is designed to resonate with clinical researchers, underwriters, and biotech executives who operate in environments where precision is non-negotiable. The aesthetic reflects a sterile laboratory environment—efficient, organized, and high-stakes.

This design system utilizes a **Corporate / Modern** style with a heavy emphasis on **Minimalism**. By prioritizing structured white space and a restricted color palette, the UI directs focus toward critical data points and risk assessments. The visual language conveys the same level of rigor found in a peer-reviewed clinical trial, ensuring that complex insurance documents feel accessible and trustworthy.

## Colors

The color strategy mimics the visual atmosphere of a modern life-sciences facility. 

- **Primary (Deep Laboratory Blue):** Used for primary actions and navigation to establish a foundation of reliability and institutional depth.
- **Secondary (Slate):** Employed for supporting text and non-interactive iconography, maintaining a neutral, professional tone.
- **Background (Sterile White):** A cooling, slightly blue-tinted white is used to prevent eye strain and maintain a clinical "cleanroom" feel.
- **Accents (Mint/Teal):** Reserved strictly for "Compliance," "Verified," and "Active" states. This distinct color signals safety and regulatory approval without the alarming nature of standard green.

## Typography

The design system utilizes **Inter** for its systematic, utilitarian clarity. It provides the necessary neutrality for a technical platform where legibility is the primary requirement. 

To handle dense biotech data, the system introduces a "Data Mono" variant (Space Grotesk) for policy numbers, chemical identifiers, and trial phases, ensuring these strings are distinct from narrative text. Tight letter spacing is used on headlines to maintain a structured, "locked-in" appearance, while body text uses standard tracking for high readability during long-form risk documentation review.

## Layout & Spacing

This design system follows a strict **8px grid system** (with a 4px sub-grid for micro-adjustments) to ensure mathematical alignment. 

On mobile, the layout shifts to a **Fluid Grid** model with high data density. To avoid clutter while maintaining information richness, padding is reduced in data-heavy tables and certificate lists, but increased around primary "Call to Action" areas. Margin widths are kept narrow (16px) to maximize the horizontal real estate for policy tables and risk matrices.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Low-contrast outlines** and **Tonal layers** rather than traditional drop shadows. This maintains a flat, technical aesthetic.

- **Level 0 (Surface):** Sterile White background.
- **Level 1 (Cards/Sections):** Defined by a 1px border in `border_color` (Slate-200).
- **Level 2 (Modals/Popovers):** A very soft, 10% opacity Slate shadow with 0px offset and 8px blur, used only when an element must physically float above the data layer.
- **State Changes:** Hover states use subtle gray fills (#F1F5F9) rather than lifting the element, keeping the user grounded in the grid.

## Shapes

The shape language is **Soft (0.25rem)**. The intention is to avoid the "playfulness" of highly rounded corners while steering clear of the "aggressive" feel of perfectly sharp edges. 

This subtle rounding mimics the industrial design of medical hardware and laboratory instruments. It suggests precision engineering. Action buttons use this standard rounding, while status chips for "Compliance" use a pill-shape to distinguish them from interactive buttons.

## Components

- **Buttons:** Primary buttons are solid Deep Laboratory Blue with white text. Secondary buttons are outlined in Slate. Labels must be concise (e.g., "Issue Certificate").
- **Data Tables:** High-density rows with 1px horizontal dividers. Alternating row colors are avoided; use hover highlights instead.
- **Risk Indicator Chips:** Small, uppercase labels with a subtle mint background and dark teal text for "Compliant" or "Active" states.
- **Input Fields:** Rectangular with a 1px Slate border. On focus, the border thickens and changes to Deep Laboratory Blue.
- **Policy Cards:** Contain three key data points—Policy ID, Renewal Date, and Compliance Status. They feature a prominent "Download PDF" icon button in the top right for quick access to certificates.
- **Medical Icons:** Use thin-stroke (1.5pt) icons. Avoid filled icons unless indicating an active toggle state. Use standard medical symbols (cross, beaker, document, shield) interpreted in a minimalist style.