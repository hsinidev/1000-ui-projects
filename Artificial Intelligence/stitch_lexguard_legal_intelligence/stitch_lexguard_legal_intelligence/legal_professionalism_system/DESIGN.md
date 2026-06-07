---
name: Legal Professionalism System
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#44474e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#0b0c02'
  on-tertiary: '#ffffff'
  tertiary-container: '#212313'
  on-tertiary-container: '#898b75'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
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
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  code-snippet:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style

This design system is built to evoke the gravitas of a centuries-old law firm while delivering the frictionless efficiency of modern artificial intelligence. The brand personality is authoritative, archival, and precision-oriented. It targets legal professionals who require high-density information without sacrificing clarity.

The aesthetic follows a **Corporate / Modern** approach with an emphasis on **Editorial Minimalism**. It prioritizes structured data and "document-first" interfaces. Every interaction is designed to feel deliberate and secure, moving away from "playful" tech trends toward a "Legacy" feel—characterised by thin hairlines, generous margins, and a texture reminiscent of high-quality physical stationery.

## Colors

The color palette centers on Deep Navy, representing institutional trust and stability. Silver is utilized for structural elements, dividers, and secondary actions, providing a metallic, professional edge. Parchment serves as the primary surface color for document views and backgrounds, reducing eye strain and mimicking physical legal paper.

For risk assessment, the design system employs a "Risk Highlight" spectrum. High-risk clauses use a deep Oxblood red; medium-risk items use a warm Amber; and low-risk or cautionary notes use a subtle, desaturated Yellow. These colors should be used sparingly as background tints or left-hand border accents to maintain the professional sobriety of the interface.

## Typography

Typography is the cornerstone of this design system’s authority. **Newsreader** is the primary choice for headings and legal text blocks, providing a literary and traditional feel that signals expertise. Its high x-height and classic serifs ensure that even long-form AI summaries feel like official documentation.

**Work Sans** is used for the functional interface, including navigation, buttons, and metadata. This provides a clean, neutral contrast to the serif headings, ensuring the "tech speed" aspect of the product is represented through highly legible, contemporary sans-serif letterforms. All labels and secondary metadata should be set in Work Sans with increased letter spacing for a structured, organized appearance.

## Layout & Spacing

The layout philosophy utilizes a **Fixed Grid** for desktop environments to maintain a "centered document" focus, while transitioning to a **Fluid Grid** for mobile. The design system uses an 8px base unit for all spacing decisions.

On desktop, the primary workspace should mirror a standard 8.5x11 page layout, with AI analysis tools appearing in a secondary side panel. On mobile, the layout shifts to a single-column stack, prioritizing "scannable summaries" at the top of the view. Spacing should be generous to avoid the cluttered look of legacy legal software, favoring white space to emphasize the "Modern Tech" speed and efficiency.

## Elevation & Depth

To maintain the "Legacy" feel, this design system avoids heavy shadows and floating elements. Instead, it utilizes **Tonal Layers** and **Sophisticated Borders**. Depth is established by placing parchment-colored document containers on slightly darker silver or navy backgrounds.

Structural hierarchy is reinforced through 1px solid borders using the Silver (#C0C0C0) palette. Subtle inset shadows may be used for input fields to suggest a "pressed" paper effect, but primary elevation is achieved through color contrast. High-priority AI insights can use a subtle "glow" or soft ambient shadow (15% opacity Navy) to distinguish them from the static document background.

## Shapes

The shape language is conservative and disciplined. A **Soft** roundedness (0.25rem) is applied to buttons and form fields to ensure the UI feels modern and accessible on touch devices. However, larger structural containers, such as document cards and analysis modules, should maintain sharper corners to preserve the formal, institutional look of legal filings.

Buttons should never be fully rounded (pill-shaped), as this contradicts the "Authoritative" brand pillar. Instead, maintain a structured, rectangular form with just enough corner softening to feel refined.

## Components

### Buttons & Inputs
Primary buttons are solid Deep Navy with white Work Sans text. Secondary buttons utilize a Silver hairline border with Navy text. Input fields should have a distinct Silver bottom border or a full-frame 1px border on Parchment backgrounds, moving to a Navy border on focus to signal "Modern Tech" responsiveness.

### Risk Highlight Chips
These are document-centric components used to flag clauses. They should feature a low-opacity background tint (e.g., 10% Risk High Red) with a 2px left-accent border of the solid risk color. The text inside should remain high-contrast for legibility.

### Document-Centric UI
AI summaries are presented as "briefs" with a Newsreader headline and Work Sans bullet points. On mobile, the "Camera-First" component is a prominent, center-aligned action bar that allows for instant scanning of physical documents.

### Scannable AI Summaries
These cards use a split layout: a Silver-tinted header for metadata (Date, Case ID) and a Parchment body for the AI-generated executive summary. Important terms within the summary should be bolded in Deep Navy to facilitate rapid scanning.