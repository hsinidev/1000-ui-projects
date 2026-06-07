---
name: Clinical Precision
colors:
  surface: '#f9f9ff'
  surface-dim: '#d8d9e5'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3fe'
  surface-container: '#ecedf9'
  surface-container-high: '#e6e8f3'
  surface-container-highest: '#e0e2ed'
  on-surface: '#181c23'
  on-surface-variant: '#414755'
  inverse-surface: '#2d3039'
  inverse-on-surface: '#eef0fc'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc1'
  primary: '#0058bc'
  on-primary: '#ffffff'
  primary-container: '#0070eb'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#5d5e63'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfe4'
  on-secondary-container: '#626267'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9ff'
  on-background: '#181c23'
  surface-variant: '#e0e2ed'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  mono-technical:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: '0'
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
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system is engineered for the high-stakes environment of augmented reality surgical training. The brand personality is rooted in **trustworthiness, technical mastery, and sterile clarity**. It must evoke a sense of professional calm, allowing the surgeon-in-training to focus on procedural accuracy without cognitive overload.

The aesthetic merges **Modern Corporate** reliability with **Glassmorphism** to suit the AR context. By using semi-transparent "floating" surfaces, the UI maintains a spatial relationship with the real-world environment (or digital anatomical models) while ensuring that data remains legible against varying backgrounds. The style is unapologetically high-fidelity, emphasizing thin strokes, precise alignments, and a medical-grade finish.

## Colors
The palette is intentionally restrained to reflect a sterile clinical environment. **Medical Blue (#007AFF)** serves as the primary action color, signifying technology and intelligence. **Sterile White (#FFFFFF)** provides the foundation for all UI surfaces, ensuring maximum contrast and a "clean" feel. **Precision Grey (#8E8E93)** is utilized for secondary information, borders, and disabled states, maintaining a sophisticated hierarchy.

In the AR space, "Sterile White" should be implemented with varying levels of opacity (Glassmorphism) to prevent the UI from occluding critical visual fields of the patient or anatomical model. High-saturation semantic colors (Red, Green, Orange) are reserved strictly for critical alerts and procedural feedback.

## Typography
This design system utilizes **Inter** for its exceptional legibility and neutral, systematic character. The typographic scale is optimized for rapid scanning during procedures. 

- **Display & Headlines:** Used for patient names or surgical phases, emphasizing weight for clear hierarchy.
- **Body Text:** Standardized for instructional steps and medical data.
- **Label Caps:** Reserved for metadata, sensor readings, or non-interactive labels to distinguish them from actionable text.
- **Mono Technical:** (Optional secondary) Used for live vitals or coordinate data where character alignment is necessary for quick interpretation.

## Layout & Spacing
The layout relies on a **Contextual Grid** optimized for 3D space. While a standard 12-column grid governs traditional 2D dashboard screens, the AR interface utilizes "Anchored Layouts" where UI cards orbit the user's focal point. 

A strict **4px baseline grid** ensures technical precision. Information density is kept moderate to high; however, generous outer margins (32px) are maintained to prevent UI elements from creeping into the user's peripheral vision. Interactive elements must have a minimum target size of 44px to accommodate "air tap" gestures.

## Elevation & Depth
Depth is the primary navigator in this design system. We use a three-tier elevation model:

1.  **Base Layer:** The real world/AR background.
2.  **Glass Layer:** Floating UI panels using a backdrop blur (20px-30px) and a semi-transparent white fill (85% opacity). These panels feature a thin, 1px internal "shine" border (White @ 20%) to define edges against bright backgrounds.
3.  **Active Layer:** High-contrast elements like buttons or active tooltips that use soft, highly-diffused ambient shadows (Color: Medical Blue @ 10% opacity, 20px blur) to appear "closer" to the user.

Avoid heavy black shadows; instead, use tinted shadows that match the primary brand color to maintain a high-tech, clinical feel.

## Shapes
The shape language is **Soft (0.25rem)** to balance clinical coldness with modern accessibility. 
- **Small elements (buttons, inputs):** 4px radius.
- **Large elements (cards, overlays):** 8px or 12px radius.

The "Soft" approach ensures that corners do not feel "sharp" or aggressive in a virtual space, while remaining significantly more professional and technical than "Pill-shaped" or highly rounded alternatives.

## Components
- **Floating Cards:** The primary container. Must include a backdrop-filter: blur() and a subtle 1px border (#8E8E93 at 20% opacity). 
- **Buttons:** 
  - *Primary:* Solid Medical Blue with white text. 
  - *Secondary:* Ghost style with a Medical Blue outline and glass background.
- **Medical Iconography:** Icons must be "Line" style, 2px stroke weight, non-rounded ends. They should be strictly functional (e.g., scalpel, heart rate, anatomy toggle).
- **Vitals Monitors:** Specialized list items with live-sparklines and large-format numeric data using the 'Mono' font variant.
- **Progress Steppers:** Thin horizontal lines at the top of the viewport indicating the current stage of the surgery (e.g., "Incision," "Realignment," "Suture").
- **Inputs:** Minimalist fields with bottom-borders only or very light glass fills, emphasizing the data entered rather than the container.