---
name: Clinical Precision
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
  on-surface-variant: '#42474d'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#73777e'
  outline-variant: '#c2c7ce'
  surface-tint: '#406180'
  primary: '#315371'
  on-primary: '#ffffff'
  primary-container: '#4a6b8a'
  on-primary-container: '#d8eaff'
  inverse-primary: '#a8caed'
  secondary: '#565f69'
  on-secondary: '#ffffff'
  secondary-container: '#d7e1ec'
  on-secondary-container: '#5a646d'
  tertiary: '#4a5157'
  on-tertiary: '#ffffff'
  tertiary-container: '#626970'
  on-tertiary-container: '#e3e9f1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cee5ff'
  primary-fixed-dim: '#a8caed'
  on-primary-fixed: '#001d32'
  on-primary-fixed-variant: '#274967'
  secondary-fixed: '#dae4ef'
  secondary-fixed-dim: '#bec8d3'
  on-secondary-fixed: '#131d25'
  on-secondary-fixed-variant: '#3e4851'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
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
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is anchored in the concept of "Clinical Precision." It is designed to evoke immediate trust, conveying the authority of a medical institution with the accessibility of a premium wellness brand. The target audience seeks expertise and results for sensitive health concerns; therefore, the UI must feel sterile but not cold, and professional but not intimidating.

The design style utilizes a refined **Minimalism** blended with **Corporate Modern** sensibilities. It prioritizes heavy whitespace to symbolize hygiene and clarity. Visual elements are governed by a strict mathematical order, ensuring that information architecture is the hero. Every interaction should feel deliberate and high-functioning, mirroring the accuracy of medical diagnostics.

## Colors

The palette is restricted to a professional, medical-grade spectrum. 

*   **Steel Blue (Primary):** Used for primary actions, navigation markers, and brand-critical information. It provides the "trust" anchor.
*   **Crisp White (Background):** The canvas is pure white to maximize the perception of hygiene and space.
*   **Silver (Accents):** Used for secondary UI elements, dividers, and decorative strokes, adding a metallic, high-tech sheen that suggests modern equipment and precision instruments.
*   **Neutral Slate:** Reserved for typography and deep structural elements to ensure high legibility against white surfaces.

## Typography

This design system uses a dual-sans-serif approach to balance modern aesthetics with systematic utility. 

**Manrope** is used for headlines to provide a refined, balanced, and authoritative voice. Its geometric yet humanistic qualities make medical headers feel modern and approachable. 

**Inter** is utilized for all body copy and UI labels. Chosen for its exceptional legibility in technical contexts, it ensures that dosage instructions, clinical data, and scalp health reports are perfectly readable. High-contrast weights and generous line heights are mandatory to prevent visual fatigue.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on desktop (12 columns) and a fluid model on mobile. This provides a stable, "locked-in" feeling that suggests reliability. 

A strict 8px spacing rhythm governs all elements, ensuring mathematical consistency throughout the interface. Margins and gutters are generous to avoid information density that could overwhelm the user. Vertical rhythm is emphasized to guide the eye through clinical processes—from assessment to treatment plans—in a linear, logical fashion.

## Elevation & Depth

To maintain the sterile, high-end medical aesthetic, this design system avoids heavy shadows or distracting gradients. Instead, it utilizes **low-contrast outlines** and **tonal layers**.

Depth is created by stacking surfaces: the primary background is Pure White, while container elements (like medical cards or data blocks) use a subtle Slate-50 (#F8FAFC) background with a 1px Silver (#E2E8F0) border. This "flat-depth" approach conveys a sense of architectural structure and engineering precision without the "fuzzy" feel of traditional shadows.

## Shapes

The shape language is conservative and professional. A "Soft" roundedness level (4px) is applied to buttons, input fields, and cards. This slight radius removes the aggressive "sharpness" of a purely clinical environment while maintaining a disciplined, engineered appearance. Pill-shaped elements are reserved exclusively for status indicators (e.g., "Active Treatment" or "Healthy") to distinguish them from actionable buttons.

## Components

Components in this design system must prioritize clarity and precision:

*   **Buttons:** Primary buttons are Solid Steel Blue with white text, utilizing a subtle 4px radius. Secondary buttons use a Silver outline with Steel Blue text. 
*   **Input Fields:** Borders are Silver (#E2E8F0) and turn Steel Blue on focus. Labels use the `label-sm` typographic style, placed strictly above the field for maximum clarity.
*   **Cards:** Used for treatment plans and diagnostic results. They feature a 1px Silver border, no shadow, and a Surface-White background to differentiate from the page background.
*   **Progress Indicators:** Linear, thin bars using Steel Blue to show treatment progress or hair growth cycles, reinforcing the data-driven nature of the brand.
*   **Iconography:** Use medical-grade, monolinear stroke icons. Avoid filled or "cutesy" illustrations. Strokes should be consistent with the 1px Silver border style used elsewhere.
*   **Chips:** Used for medical tags or ingredients (e.g., "Minoxidil," "Scalp Health"). These use a light Silver background with Dark Slate text.