---
name: Scholar-Twin
colors:
  surface: '#fcf9f5'
  surface-dim: '#dcdad6'
  surface-bright: '#fcf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ef'
  surface-container: '#f0ede9'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e5e2de'
  on-surface: '#1c1c1a'
  on-surface-variant: '#43474e'
  inverse-surface: '#31302e'
  inverse-on-surface: '#f3f0ec'
  outline: '#73777f'
  outline-variant: '#c3c6cf'
  surface-tint: '#426087'
  primary: '#002446'
  on-primary: '#ffffff'
  primary-container: '#1a3a5f'
  on-primary-container: '#87a4cf'
  inverse-primary: '#abc8f5'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#24231f'
  on-tertiary: '#ffffff'
  tertiary-container: '#393934'
  on-tertiary-container: '#a4a29c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e3ff'
  primary-fixed-dim: '#abc8f5'
  on-primary-fixed: '#001c39'
  on-primary-fixed-variant: '#2a486e'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2db'
  tertiary-fixed-dim: '#c9c6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#474742'
  background: '#fcf9f5'
  on-background: '#1c1c1a'
  surface-variant: '#e5e2de'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 42px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: EB Garamond
    fontSize: 30px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 20px
  gutter: 16px
---

## Brand & Style
The design system is rooted in a **Minimalist-Intellectual** aesthetic, designed to foster deep concentration and scholarly rigor. It targets an audience of lifelong learners and researchers who value clarity and "Deep Work" over dopamine-driven engagement. 

The visual style is a sophisticated blend of **Tactile Skeuomorphism** and **Academic Minimalism**. It leverages the warmth of physical archival materials—parchment textures and crisp ink-like strokes—balanced with modern digital layouts. The goal is to evoke the feeling of a clean, well-organized physical library or a private study, where the interface recedes to let the content lead the cognitive experience.

## Colors
The palette is restricted to a triad of meaningful tones that prioritize legibility and focus:

- **Parchment (#F4F1EA):** The foundational surface color. It reduces eye strain compared to pure white and provides the tactile warmth of high-quality paper.
- **Charcoal (#2D2D2D):** Used for typography and structural borders. It represents the "ink" of the system, providing high contrast and clarity.
- **Scholar-Blue (#1A3A5F):** Reserved exclusively for primary actions, navigational cues, and highlighting significant intellectual milestones. 
- **Functional States:** Use a muted version of Charcoal for disabled states and a desaturated Scholar-Blue for secondary interactive elements.

## Typography
This design system employs a "Traditionalist-Modernist" pairing to signal both authority and accessibility.

- **Headlines (EB Garamond):** A graceful, classical serif that provides an old-world academic feel. It is used for titles and significant thematic headers.
- **Body & Interface (Hanken Grotesk):** A sharp, contemporary sans-serif chosen for its exceptional readability in micro-learning contexts. It handles data-heavy lists and instructional text with precision.
- **Hierarchy:** Maintain generous line-heights (1.5x minimum) to ensure "breathing room" for the eyes during long reading sessions.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for mobile-first views, centering content to create a focused column of study.

- **Rhythm:** A strict 4px baseline grid ensures vertical harmony. 
- **Margins:** Standard mobile views use a 20px outer margin to prevent the parchment textures from feeling cramped.
- **Whitespace:** Use whitespace aggressively to separate distinct concepts. In "Deep Work" mode, increase vertical spacing between cards to 32px to minimize peripheral distraction.

## Elevation & Depth
Depth is created through physical metaphors rather than digital light sources.

- **Skeuomorphic Surfaces:** Backgrounds and cards utilize a very subtle noise/grain texture to mimic parchment.
- **Subtle Shadows:** Use a single, soft, low-opacity shadow (`rgba(45, 45, 45, 0.08)`) with a large blur radius to suggest a paper-on-paper stack effect.
- **Crisp Borders:** Every card and interactive container is defined by a 1px Charcoal border. This creates a "bound book" feel, providing structure that shadows alone cannot achieve in this aesthetic.

## Shapes
The shape language is conservative and disciplined. 

- **Soft Edges (0.25rem):** Corners are slightly blunted to remove the "sharpness" of digital screens, mimicking the slightly worn edge of a manuscript.
- **Strict Rectilinearity:** Avoid circles or heavy pill shapes. Buttons and inputs should remain rectangular with soft corners to maintain the architectural, serious tone of the system.

## Components
- **Buttons:** Primary buttons are solid Scholar-Blue with Parchment-colored text. Secondary buttons are Parchment-filled with a 1px Charcoal border and Charcoal text. No gradients.
- **Cards:** Utilize a subtle parchment texture. They must have a 1px Charcoal border. On tap/hover, the card "lifts" via a slightly deeper shadow, never a color change.
- **Input Fields:** Styled as "underlined" or "bracketed" fields to mimic traditional forms. Use Charcoal for the baseline.
- **Chips/Tags:** Small, rectangular labels with a 1px Charcoal border and `label-caps` typography. They should look like physical library filing tags.
- **Progress Indicators:** Use a thin, Scholar-Blue line (2px height). Avoid thick or rounded progress bars.
- **Micro-Learning Units:** Group content into "Lesson Cards" that use high-contrast Charcoal borders to separate the "Deep Work" focus area from the background.