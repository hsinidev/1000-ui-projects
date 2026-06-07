---
name: Digital Vellum & Steel
colors:
  surface: '#fff8f7'
  surface-dim: '#e6d7d5'
  surface-bright: '#fff8f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff0ef'
  surface-container: '#faeae9'
  surface-container-high: '#f5e5e3'
  surface-container-highest: '#efdfdd'
  on-surface: '#221a19'
  on-surface-variant: '#544341'
  inverse-surface: '#372e2d'
  inverse-on-surface: '#fdedeb'
  outline: '#877270'
  outline-variant: '#dac1bf'
  surface-tint: '#954742'
  primary: '#2a0002'
  on-primary: '#ffffff'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#ffb3ad'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#001401'
  on-tertiary: '#ffffff'
  tertiary-container: '#002c06'
  on-tertiary-container: '#589b55'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#acf4a4'
  tertiary-fixed-dim: '#91d78a'
  on-tertiary-fixed: '#002203'
  on-tertiary-fixed-variant: '#0c5216'
  background: '#fff8f7'
  on-background: '#221a19'
  surface-variant: '#efdfdd'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  section-gap: 64px
---

## Brand & Style

The brand personality of this design system is defined by the intersection of institutional prestige and algorithmic precision. It serves a target audience of high-stakes legal professionals who require the reliability of tradition combined with the efficiency of modern AI. The UI evokes a sense of "digital vellum"—the interface should feel like a living document that is both archival and actionable.

The chosen design style is **Minimalist / Corporate** with an **Editorial** influence. It avoids trendy "bubbly" elements in favor of a structured, grid-heavy layout that mimics the composition of formal legal filings. The visual language emphasizes architectural stability through vertical lines, generous margins, and a strict adherence to typographic hierarchy, ensuring that high-density contract data remains legible and authoritative.

## Colors

The palette is rooted in the "Authoritative Legacy" concept. The primary **Deep Burgundy** is used for high-level navigation, headers, and primary actions to establish brand gravity. **Parchment** serves as the universal background color, reducing eye strain and providing a sophisticated alternative to stark white, reinforcing the "document" feel.

**Refined Gold/Brass** is used sparingly as an accent for focus states, active tab indicators, and premium features. For semantic clarity, this design system employs a high-contrast **Risk Red** and a **Deep Emerald** (Safe) to categorize clauses. These colors should be applied with high saturation to ensure they stand out against the muted parchment and burgundy tones, allowing for rapid visual scanning of contract health.

## Typography

This design system utilizes a dual-font strategy to balance heritage and utility. **Newsreader** is the voice of authority, used for all headings and serif-based displays. It provides the intellectual, "literary" quality necessary for a platform dealing with complex legal text. 

**Inter** is used for all functional body copy, data tables, and interface labels. Its neutral, systematic design ensures "modern speed" by providing maximum legibility at small sizes and high-speed information processing. Small caps and increased letter spacing should be used for labels (e.g., table headers) to create a clear distinction between the "user interface" and the "document content."

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on desktop to mimic the proportions of physical paper (A4/Letter), transitioning to a fluid layout for mobile devices. A 12-column grid is used for dashboard views, while a centered, single-column "Reading Mode" is used for contract analysis.

Spacing is generous, utilizing "White Space as a Luxury." Components should never feel cramped; the layout uses an 8px base unit to maintain a rigorous mathematical rhythm. Sections of contracts should be separated by clear vertical gaps to allow the AI-generated highlights room to breathe without overlapping the primary text.

## Elevation & Depth

To maintain the "Modern Speed" and professional aesthetic, this design system avoids heavy shadows or neomorphic effects. Instead, it utilizes **Low-Contrast Outlines** and **Tonal Layers**. 

Hierarchy is established by layering: 
- **Level 0 (Background):** Parchment (#F9F7F2).
- **Level 1 (Cards/Content Blocks):** Crisp White (#FFFFFF) with a 1px border in a muted brass or light gray tint.
- **Level 2 (Popovers/Modals):** Crisp White with a sharp, low-opacity ambient shadow (Blur: 8px, Y: 4px, Color: #4A0E0E at 5% opacity).

Depth is communicated through the "stacking" of paper-like surfaces rather than 3D extrusion. All interactive elements should feel physically anchored to the grid.

## Shapes

In keeping with the "Authoritative" requirement, the design system utilizes **Soft** corners (0.25rem/4px) for most UI elements. This provides a subtle modern touch without the "bubbly" or "playful" connotations of fully rounded corners. 

Buttons, input fields, and "Risk Highlight" containers should maintain these disciplined corners. Larger containers like cards or modals may use the `rounded-lg` (8px) setting, but never higher. The goal is to feel architectural and precise, like a well-tailored suit.

## Components

### Buttons & Inputs
- **Primary Action:** Solid Deep Burgundy with white text. Sharp corners.
- **Secondary Action:** Ghost style with 1px Burgundy or Brass borders.
- **Inputs:** Crisp White background with 1px borders. Use "Floating Labels" in Inter for a modern feel.

### Specialized Risk Highlights
- **Risk Box:** A background tint of Risk Red at 10% opacity, a 2px left-accent border of solid Risk Red, and a small badge in the top right indicating the AI's confidence level.
- **Safe Clause:** A subtle emerald underline or "highlighter" effect behind text.

### Mobile & Biometric Capture
- **Biometric Prompt:** A bottom-sheet component that appears for document signing. It should use a backdrop blur to focus the user on the fingerprint/face ID interaction.
- **Approval Footer:** A persistent, high-contrast mobile footer with a "Slide to Approve" mechanic to prevent accidental legal commitments.

### Tables & Data
- All tables should use the parchment background for rows, with Deep Burgundy for the header row and Gold/Brass for sort indicators. Lines should be thin and subtle (0.5px).