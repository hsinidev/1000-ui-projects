---
name: GRC Institutional System
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
  on-surface-variant: '#44474c'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#75777d'
  outline-variant: '#c5c6cd'
  surface-tint: '#515f74'
  primary: '#1d2b3e'
  on-primary: '#ffffff'
  primary-container: '#334155'
  on-primary-container: '#9eadc5'
  inverse-primary: '#b9c7e0'
  secondary: '#516072'
  on-secondary: '#ffffff'
  secondary-container: '#d2e1f7'
  on-secondary-container: '#556477'
  tertiary: '#262b2e'
  on-tertiary: '#ffffff'
  tertiary-container: '#3c4144'
  on-tertiary-container: '#a8adb1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3fd'
  primary-fixed-dim: '#b9c7e0'
  on-primary-fixed: '#0d1c2f'
  on-primary-fixed-variant: '#3a485c'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
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
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  status-indicator:
    fontFamily: Public Sans
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base-unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  bento-gap: 16px
  container-padding: 24px
---

## Brand & Style

The design system is engineered to project **Institutional Trust** and **Operational Calm**. In the high-stakes environment of Governance, Risk, and Compliance, the UI must act as a stabilizing force, reducing cognitive load through rigid organization and a "Corporate Modern" aesthetic.

The visual direction centers on a **Bento-Box layout philosophy**, which partitions complex datasets into digestible, high-contrast modules. This ensures that users—ranging from compliance officers to executive stakeholders—can scan for anomalies without being overwhelmed by "data noise." The emotional response is one of reliability, precision, and systematic control.

## Colors

This design system utilizes a **Calm-Centric palette** dominated by Slate Blue and Silver tones. The primary Slate Blue (#334155) provides a grounded, authoritative base for navigation and primary actions, while varying shades of Silver and White create the "layered" effect necessary for bento-style information architecture.

Color is used sparingly and functionally:
- **Slate Blue:** Reserved for high-level hierarchy and primary buttons.
- **Silver/Slate-Light:** Used for borders and secondary text to maintain a low-contrast, non-aggressive environment.
- **Semantic Accents:** Success, Warning, and Error colors are desaturated to fit the corporate aesthetic while remaining distinct enough for real-time status indicators.

## Typography

**Public Sans** is the sole typeface for this design system. Chosen for its institutional clarity and roots in government-standard accessibility, it provides the "no-nonsense" professional tone required for GRC.

The typographic scale emphasizes vertical rhythm and scannability. **Label-caps** are utilized for bento-box headers to provide a clear distinction between container titles and the data within. Weight is used as a primary tool for hierarchy: Semi-bold for actionable data and Regular for descriptive text.

## Layout & Spacing

The layout is built on a **12-column Fixed Grid** for desktop, transitioning to a flexible single-column stack for mobile. The hallmark of the design system is the **Modular Bento Grid**, where every piece of information is housed in a distinct container.

Key Spacing Rules:
- **Bento Gaps:** A consistent 16px gap is maintained between all dashboard modules to ensure visual breathing room.
- **Internal Padding:** Containers use a generous 24px internal padding to prevent data from feeling cramped, reinforcing the "calm" objective.
- **Mobile Checklist View:** On mobile, margins are reduced to 16px to maximize the touch target area for checklist completion.

## Elevation & Depth

This design system avoids heavy shadows to maintain a clean, professional profile. Depth is instead conveyed through **Tonal Layers** and **Low-Contrast Outlines**.

- **Level 0 (Background):** The default neutral light (#F8FAFC).
- **Level 1 (Bento Containers):** Pure White (#FFFFFF) with a 1px border in Silver (#E2E8F0).
- **Level 2 (Active/Hover):** A subtle, diffused shadow (0px 4px 12px rgba(51, 65, 85, 0.05)) to indicate interactivity without breaking the flat aesthetic.

This "stacked paper" approach ensures that the UI feels physical and organized without the clutter of traditional skeuomorphism.

## Shapes

The shape language is **Soft (Level 1)**. Elements utilize a 0.25rem (4px) base radius, providing a precise, geometric feel that leans toward "Sharp."

Large bento containers may scale up to a 0.5rem (8px) radius to soften the overall dashboard view, but input fields, buttons, and checkboxes remain at the base 4px radius to reinforce a sense of rigorous, systematic structure. This balance ensures the platform feels modern but retains its corporate edge.

## Components

### Bento Cards
The primary organizational unit. Each card must have a `label-caps` title and an optional top-right action icon. Cards are white with a slate-light border.

### Status Indicators
Real-time status is indicated by "Pill" badges. These use a 10% opacity background of the semantic color (Success/Warning/Error) with high-contrast text of the same hue. On mobile, these indicators are pinned to the top-right of checklist items.

### Checklist Items
Optimized for mobile "thumb-taps." Each item features a large hit area (minimum 48px height), a custom Slate Blue checkbox, and a progress bar that updates in real-time as items are validated.

### Buttons
- **Primary:** Solid Slate Blue with white text. No gradient.
- **Secondary:** Transparent background with a Silver border and Slate Blue text.
- **Ghost:** No border or background, used for low-priority actions in footer regions.

### Data Tables
Tables within bento modules should use "Zebra Striping" with the tertiary color (#F1F5F9) and avoid vertical grid lines to maintain horizontal scannability.