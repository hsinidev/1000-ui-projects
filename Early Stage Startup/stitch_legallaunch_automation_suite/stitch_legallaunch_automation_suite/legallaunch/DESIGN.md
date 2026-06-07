---
name: LegalLaunch
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
  on-surface-variant: '#444653'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#747684'
  outline-variant: '#c4c5d5'
  surface-tint: '#3456c1'
  primary: '#00216e'
  on-primary: '#ffffff'
  primary-container: '#0033a0'
  on-primary-container: '#8ea6ff'
  inverse-primary: '#b6c4ff'
  secondary: '#5d5e66'
  on-secondary: '#ffffff'
  secondary-container: '#e3e1ec'
  on-secondary-container: '#63646c'
  tertiary: '#23292f'
  on-tertiary: '#ffffff'
  tertiary-container: '#393f45'
  on-tertiary-container: '#a4aab2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#001550'
  on-primary-fixed-variant: '#133ca8'
  secondary-fixed: '#e3e1ec'
  secondary-fixed-dim: '#c6c5cf'
  on-secondary-fixed: '#1a1b22'
  on-secondary-fixed-variant: '#46464e'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
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
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  button:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max-width: 1280px
  gutter: 24px
  margin: 32px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The brand personality is anchored in **Institutional Modernism**. This design system balances the gravitas of a traditional law firm with the velocity of a tech startup. It aims to evoke an emotional response of "controlled progress"—where the user feels the security of legal compliance and the momentum of automation.

The visual style is **Corporate / Modern** with a heavy influence from **Minimalism**. By prioritizing high contrast and generous whitespace, the interface removes cognitive load, allowing the "Progress-driven" layout to guide users through complex legal workflows with precision. The aesthetic is clean, sharp, and uncompromisingly professional.

## Colors

The palette utilizes a high-contrast foundation to ensure readability and authority. **Royal Blue** serves as the primary driver for action and identity, symbolizing stability and trust. **Silver** is utilized through a range of cool greys and slates for borders, dividers, and disabled states, providing a metallic, "structured" feel without cluttering the view.

- **Primary:** Royal Blue (#0033A0) for core CTAs and brand presence.
- **Background:** Pure White (#FFFFFF) to maintain a pristine, document-like environment.
- **Accents:** Silver/Slate (#E2E8F0) for structural accents and subtle depth.
- **Status Colors:** Success (Emerald), Warning (Amber), and Error (Crimson) are used sparingly but with high saturation to ensure critical compliance information is never missed.

## Typography

This design system employs **Public Sans** across all levels. Chosen for its origins in government and institutional design, it conveys a sense of officiality and accessibility. 

The type hierarchy is strictly enforced to create a "Document-First" experience. Headlines use a heavier weight and tighter letter-spacing to command authority, while body text uses a generous line-height to ensure legal jargon remains legible. Small uppercase labels are used for metadata and status indicators to differentiate administrative information from core content.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model to provide a sense of stability and containment. Content is centered within a 1280px container, mirroring the structured nature of legal filings. 

A 12-column grid system is used for dashboard layouts, while specialized "Step-based" forms utilize a narrow 6-column centered column to maintain focus. The spacing rhythm is based on an 8px baseline, ensuring that every element—from the height of an input field to the padding within a document card—feels mathematically precise and intentional.

## Elevation & Depth

To maintain a minimalist and secure aesthetic, this design system avoids heavy, ambient shadows. Instead, it relies on **Low-contrast outlines** and **Tonal layering**.

- **Level 0 (Base):** White background.
- **Level 1 (Cards/Sections):** A 1px border in Silver (#E2E8F0) with no shadow. 
- **Level 2 (Interactive):** On hover, elements gain a very subtle, tight "Security Shadow" (0px 2px 4px rgba(0, 0, 0, 0.05)) to indicate interactivity without breaking the flat, professional plane.
- **Overlays:** Modals and dropdowns use a sharp 1px border and a medium-diffused shadow to suggest they are sitting directly on top of the workspace.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding of corners takes the edge off the "Brutalist" coldness while remaining significantly more formal and "buttoned-up" than rounded or pill-shaped designs. It suggests precision, like the clipped corner of a professional document.

- **Buttons & Inputs:** 4px (0.25rem) radius.
- **Cards & Containers:** 8px (0.5rem) radius for a slightly softer frame around large content blocks.
- **Status Badges:** Completely square or minimal 2px radius to emphasize their "stamped" or "official" nature.

## Components

### Buttons
Primary buttons are solid Royal Blue with white text. Secondary buttons use the Silver border with Royal Blue text. All buttons use a fixed height (44px) and bold, uppercase labels to signal intent and confidence.

### Document Preview Cards
These cards feature a 1px Silver border and a "Progress Header"—a thin 2px colored line at the top indicating status (e.g., Blue for "In Review", Green for "Executed"). They include a dedicated area for file-type icons and metadata labels.

### Status Badges
High-contrast, rectangular badges. They do not use pastel backgrounds; instead, they use a light grey background with a 2px colored left-border and matching colored text to maintain a serious, dashboard-centric look.

### Structured Forms
Inputs are characterized by top-aligned labels in `label-caps`. Focus states use a 2px Royal Blue border. Errors are shown via a red border and a small icon, ensuring that compliance issues are immediately visible.

### Secure Navigation
The sidebar uses a dark-themed neutral (#0F172A) to contrast against the white content area, creating a "frame" that suggests a secure environment. Icons are thin-stroke and geometric, emphasizing precision.