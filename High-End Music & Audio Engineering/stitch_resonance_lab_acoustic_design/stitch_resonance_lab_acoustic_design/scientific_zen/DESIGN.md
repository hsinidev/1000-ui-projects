---
name: Scientific-Zen
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#434844'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#737874'
  outline-variant: '#c3c8c2'
  surface-tint: '#506357'
  primary: '#506357'
  on-primary: '#ffffff'
  primary-container: '#879b8e'
  on-primary-container: '#213329'
  inverse-primary: '#b7ccbd'
  secondary: '#635e51'
  on-secondary: '#ffffff'
  secondary-container: '#e7dfcf'
  on-secondary-container: '#686255'
  tertiary: '#515f74'
  on-tertiary: '#ffffff'
  tertiary-container: '#8997ad'
  on-tertiary-container: '#212f42'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d9'
  primary-fixed-dim: '#b7ccbd'
  on-primary-fixed: '#0d1f16'
  on-primary-fixed-variant: '#384b40'
  secondary-fixed: '#eae1d2'
  secondary-fixed-dim: '#cec6b6'
  on-secondary-fixed: '#1f1b12'
  on-secondary-fixed-variant: '#4b463b'
  tertiary-fixed: '#d5e3fc'
  tertiary-fixed-dim: '#b9c7df'
  on-tertiary-fixed: '#0d1c2e'
  on-tertiary-fixed-variant: '#3a485b'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-reg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-page: 64px
  section-gap: 128px
---

## Brand & Style

The design system is anchored in the "Scientific-Zen" aesthetic, a philosophy that bridges the gap between cold laboratory precision and the warmth of organic architecture. It is designed for architects, acoustic engineers, and audiophiles who require high-fidelity data presented with meditative clarity.

The visual style is a hybrid of **Minimalism** and **Tactile Modernism**. It prioritizes extreme legibility and generous whitespace to reduce cognitive load while introducing "pale wood" textures to provide a grounding, human element. This prevents the interface from feeling purely clinical, moving it instead toward a "medical-grade" premium experience where every pixel serves a functional and aesthetic purpose.

## Colors

The palette for this design system is meticulously balanced to evoke a sense of quiet authority. 

- **Primary (Sage Green):** Used for primary actions and active acoustic states. It symbolizes growth and balance.
- **Secondary (Pale Wood):** Applied sparingly as a background texture or as a surface for "organic" containers, providing warmth against the clinical white.
- **Tertiary (Slate Grey):** Reserved exclusively for technical data, charts, and monospaced readings to ensure high contrast and separation from the UI chrome.
- **Neutral (White/Off-White):** The foundation of the system, providing the "sterile" environment necessary for precision.

Color should be used functionally rather than decoratively. Use the Slate Grey for all mathematical values to signify "raw data" vs "interpreted design."

## Typography

Typography in this design system follows a dual-path hierarchy. **Inter** is utilized for the primary interface—navigation, body copy, and headlines—to ensure a neutral, utilitarian feel that disappears into the layout.

**Space Grotesk** is introduced for all technical readings, decibel levels, and frequency data. This typeface provides the "Scientific" edge, with its geometric construction and technical flair. Use uppercase for labels with increased letter spacing to mimic the engraved labels found on high-end audio equipment. All numerical values must be set in Space Grotesk to distinguish "data" from "description."

## Layout & Spacing

This design system employs a **Fixed Grid** model to maintain the integrity of complex acoustic charts. A 12-column grid is standard for desktop, with a preference for centering content to create an architectural "gallery" feel.

The spacing rhythm is governed by a 4px base unit, but the defining characteristic is the **Generous Margins**. Large sections of the interface should remain empty to symbolize the "silence" required for acoustic treatment. Use a minimum of 64px for page margins and 128px for vertical separation between major modules to ensure the user never feels overwhelmed by the technical density of the data.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. 

1. **Base:** The primary canvas is #FAFAFA.
2. **Surface Containers:** Used for charts and data groups, these use a subtle 1px border (#E2E8F0) or a soft wood-textured background for organic contrast.
3. **Floating Elements:** Modals and tooltips utilize an "Ambient Shadow"—an extra-diffused, low-opacity shadow (4% opacity Slate Grey) with a large blur radius to mimic natural light falling on a physical architectural model.

Avoid layering more than three levels deep to maintain the "Zen" simplicity. Use background blurs (10px) behind navigation bars to provide a sense of depth without adding visual noise.

## Shapes

The shape language is "Soft-Precision." We utilize a **Level 1 (Soft)** approach. A 0.25rem (4px) radius is applied to standard UI components like buttons and input fields to maintain a professional, "medical-grade" sharpness.

Larger cards and architectural diagrams may use **rounded-lg** (8px) to feel more approachable and organic, particularly when using the Pale Wood texture. All interactive elements should feel deliberate and structural, avoiding the playfulness of highly rounded "pill" shapes.

## Components

- **Buttons:** Primary buttons use the Sage Green background with white Inter medium text. Secondary buttons are "ghost" style with a 1px Slate Grey border. 
- **Medical-Grade Iconography:** Use ultra-thin (1pt stroke) icons. Icons should be functional indicators of acoustic properties (e.g., sound waves, absorption coefficients) rather than decorative.
- **Precise Charts:** Line charts should use 1.5pt strokes in Slate Grey, with the area under the curve filled with a 5% opacity Sage Green. Grid lines must be faint (2% opacity).
- **Wood Surface Cards:** For highlights or specialized "Room Treatment" recommendations, use the Pale Wood color with a subtle grain texture as the card background.
- **Input Fields:** Minimalist under-line inputs or very light grey (#F1F5F9) filled containers with 4px rounding. Focus states should be indicated by a Sage Green bottom border.
- **Data Chips:** Small, monospaced labels in Slate Grey with a light Sage background, used for displaying metadata like "RT60" or "NRC Ratings."