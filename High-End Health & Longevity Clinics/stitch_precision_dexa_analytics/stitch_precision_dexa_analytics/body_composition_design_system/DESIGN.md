---
name: Body Composition Design System
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#444748'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5e5e5e'
  primary: '#333434'
  on-primary: '#ffffff'
  primary-container: '#4a4a4a'
  on-primary-container: '#bbb9b9'
  inverse-primary: '#c8c6c6'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#283637'
  on-tertiary: '#ffffff'
  tertiary-container: '#3f4d4d'
  on-tertiary-container: '#aebdbd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4e2e2'
  primary-fixed-dim: '#c8c6c6'
  on-primary-fixed: '#1b1c1c'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#d6e6e5'
  tertiary-fixed-dim: '#bac9c9'
  on-tertiary-fixed: '#101e1e'
  on-tertiary-fixed-variant: '#3b494a'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  container-max: 1280px
---

## Brand & Style

The design system is engineered to evoke a sense of scientific rigor, anatomical precision, and clinical authority. Designed for a body composition facility, the aesthetic avoids the "wellness" tropes of soft gradients and organic shapes, favoring a technical, medical-grade interface that mirrors high-end laboratory equipment. 

The style is a fusion of **Industrial Minimalism** and **Technical Structuralism**. It utilizes a strict, visible grid to communicate stability and accuracy. The user experience is designed to feel like operating a precision instrument—objective, grounded, and high-performance. This approach builds trust with users by treating their physiological data with the same seriousness as a diagnostic medical report.

## Colors

The palette is restricted to a professional, desaturated range to maintain a clinical focus. 

- **Cool White (#F8F9FA):** Serves as the primary canvas, providing a sterile, high-clarity environment.
- **Slate (#2D3436):** Used for primary text and structural boundaries to ensure maximum legibility and deep contrast.
- **Earthy Grey (#4A4A4A):** Applied to secondary UI elements and iconography, grounding the design in a tactile, hardware-like feel.
- **Silver (#C0C0C0):** Utilized for borders, dividers, and inactive states, mimicking the brushed metal of medical machinery.
- **Muted Sage (#829191):** Reserved strictly for data accents, progress indicators, and "normal" range visualizations. It provides a calm, biological counterpoint to the industrial grays.

## Typography

This design system employs a dual-font strategy to balance readability with a technical aesthetic.

**Inter** is the workhorse for all prose and primary interface headings. Its neutral character allows information to be presented without bias, while its high x-height ensures clarity in high-density data views.

**JetBrains Mono** (or Roboto Mono) is used exclusively for technical data, labels, and status readouts. The monospaced nature of the font ensures that numerical values align vertically in tables and reports, reinforcing the engineering-grade feel of the facility’s output. All technical labels should be set in uppercase with increased letter-spacing for a "blueprint" specification look.

## Layout & Spacing

The layout is governed by a **strict 12-column fixed grid** with visible or implied structural lines. The rhythm is based on a 4px baseline, ensuring that every element—from the height of a button to the padding of a card—is mathematically consistent.

Margins are generous (48px) to provide "breathing room" within a dense technical environment. Gutters are kept at a rigid 24px. Layouts should prioritize vertical stacking and clear modularity, mimicking the compartments of a professional tool chest or a medical dashboard. Grouping related metrics within "data modules" is required to prevent cognitive overload.

## Elevation & Depth

Depth in this design system is achieved through **structural layering and perspective** rather than soft ambient shadows. 

- **3D-Perspective Containers:** Primary data modules utilize a "slight-inset" or "slight-outset" effect created via 1px borders of varying tones (e.g., a Slate top border and a White bottom border). This creates a machined, embossed appearance.
- **Tonal Layers:** The Slate (#2D3436) background is used for the deepest layer, with Cool White (#F8F9FA) panels "floating" on top using crisp, 1px Silver (#C0C0C0) outlines.
- **Zero Shadows:** Traditional drop shadows are avoided. Instead, depth is communicated through the contrast of stacked containers and the use of the Silver/Grey tones to create "grooved" intersections between UI sections.

## Shapes

The shape language is **strictly geometric and sharp (0px)**. 

Every UI element—from buttons and input fields to the containers themselves—features 90-degree corners. This reinforces the "clinical" and "engineering" narrative, as sharp corners suggest precision and structural integrity. Any use of curves would soften the medical-grade intent of the system and is therefore prohibited. Subtle internal lines (1px) should be used within containers to bifurcate data without adding unnecessary bulk.

## Components

- **Buttons:** Rectangular with 1px solid borders. Primary buttons use a Slate background with White text; secondary buttons use a Silver border with Earthy Grey text. Hover states utilize a subtle shift in background tone (e.g., Sage for success actions).
- **Data Containers:** The hallmark of the design system. These use the 3D-perspective technique with a monospaced header label in a contrasting top-bar. 
- **Input Fields:** Minimalist boxes with 1px Silver borders that turn Slate on focus. Labels sit atop the border in a small monospaced font.
- **High-Precision Visualizations:** Charts must use thin (1px) strokes. The Sage (#829191) color is used for "optimal" ranges, while Earthy Grey is used for baseline data. Grid lines in charts should be visible but low-opacity.
- **Status Chips:** Small, rectangular tags using Sage for "In-Range" and Earthy Grey for "Out-of-Range," always accompanied by monospaced text.
- **Measurement Readouts:** Large numerical displays should be paired with a smaller unit label (e.g., "kg" or "%") in the same monospaced typeface to maintain a laboratory-report aesthetic.