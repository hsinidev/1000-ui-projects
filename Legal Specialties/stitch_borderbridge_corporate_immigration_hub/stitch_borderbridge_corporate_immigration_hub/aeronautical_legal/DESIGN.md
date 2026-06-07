---
name: Aeronautical Legal
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
  on-surface-variant: '#444653'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#747685'
  outline-variant: '#c4c5d5'
  surface-tint: '#3056c4'
  primary: '#002576'
  on-primary: '#ffffff'
  primary-container: '#0038a8'
  on-primary-container: '#96adff'
  inverse-primary: '#b6c4ff'
  secondary: '#6a5d43'
  on-secondary: '#ffffff'
  secondary-container: '#f0debc'
  on-secondary-container: '#6e6147'
  tertiary: '#0e2965'
  on-tertiary: '#ffffff'
  tertiary-container: '#29407d'
  on-tertiary-container: '#98aef2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#00164f'
  on-primary-fixed-variant: '#093cab'
  secondary-fixed: '#f3e0bf'
  secondary-fixed-dim: '#d6c5a5'
  on-secondary-fixed: '#231a06'
  on-secondary-fixed-variant: '#51452d'
  tertiary-fixed: '#dbe1ff'
  tertiary-fixed-dim: '#b3c5ff'
  on-tertiary-fixed: '#00174a'
  on-tertiary-fixed-variant: '#2d4481'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
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
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1280px
---

## Brand & Style

The brand personality for this design system is rooted in **Navigational Authority**. It positions the immigration process not as a bureaucratic hurdle, but as a flight path managed with technical precision. The target audience includes high-stakes corporate relocations and individuals seeking a secure passage to new opportunities.

The UI utilizes a **Corporate Modern** style with a high-fidelity, technical edge. It mimics the clarity of aviation instrumentation—where every element has a purpose and information density is balanced by extreme legibility. The emotional response is one of "ordered calm"—the feeling of a pilot confidently navigating a complex global network. White space is used intentionally to simulate the "open skies," while structured elements provide the "ground control" reliability.

## Colors

The color palette is built on a foundation of **Royal Blue**, representing the deep authority of international law and the vastness of the global horizon. This is supported by **Sand**, a warm, tactile accent that evokes the physical nature of documents, passports, and the literal "grounding" of a successful immigration journey.

- **Primary (Royal Blue):** Used for primary actions, navigational headers, and brand-heavy components.
- **Secondary (Sand):** Used for "high-trust" moments—notices, document upload areas, and subtle background highlights to soften the coldness of the blue.
- **Surface:** A crisp White is the primary background to ensure maximum readability and a sterile, professional environment.
- **Functional Greys:** Cool-toned greys are utilized for technical details and grid lines, reinforcing the aviation aesthetic.

## Typography

This design system utilizes **Inter** exclusively to maintain a utilitarian and systematic feel. Inter’s tall x-height and excellent legibility at small sizes make it the ideal candidate for a platform that handles complex legal data.

Headlines are tight and authoritative, while labels use slightly increased letter spacing and occasional uppercase transformations to mimic the "wayfinding" signage found in international airports. Body text is optimized for long-form legal reading with generous line heights. All typographical elements are aligned to a strict baseline to reinforce the sense of order and precision.

## Layout & Spacing

The layout is governed by a **12-column fixed grid** on desktop, transitioning to a fluid model for smaller breakpoints. This design system relies on a strict 8px spatial scale to ensure every component feels mathematically aligned.

A distinctive feature is the use of **subtle grid overlays** in the background of hero sections or dashboard headers, reminiscent of longitude/latitude lines or aeronautical charts. Gutters are kept wide to prevent information density from feeling overwhelming, ensuring that the "flight path" of the user's eye remains clear and unobstructed.

## Elevation & Depth

Depth in this design system is achieved through **low-contrast outlines** and **tonal layering** rather than heavy shadows. This maintains a "flat-panel" aesthetic similar to modern cockpit displays.

- **Level 0 (Base):** White background.
- **Level 1 (Sub-surface):** Subtle 1px borders in a light cool-grey (#E2E8F0) to define containers.
- **Level 2 (Active):** Very soft, diffused shadows (0px 4px 12px rgba(0, 56, 168, 0.05)) are used only for floating elements like dropdowns or active cards to suggest they are "in flight" above the page.
- **Interactive:** Hover states utilize a subtle shift in background tone (e.g., White to a very pale Blue-Grey) rather than an increase in shadow depth.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding prevents the UI from feeling sharp or aggressive while maintaining the structural integrity of a professional legal firm.

Buttons and input fields use the base 4px (0.25rem) radius. Large containers or "Information Panels" can scale up to a 0.5rem radius to create a more approachable, modern feel for client-facing dashboards. Progress indicators and waypoint markers may use "Pill" shapes (100px radius) to differentiate them from functional containers.

## Components

### Buttons
Primary buttons are solid Royal Blue with white text, featuring a subtle 1px inset border for a "pressed" look on active states. Secondary buttons use the Sand accent or a ghost style (Royal Blue outline) for less critical actions.

### Waypoint Progress Indicators
Standard progress bars are replaced by "Flight Paths." These feature waypoint icons (small hollow circles) connected by dashed lines. The current step is marked by a solid Royal Blue circle with a "signal" pulse effect.

### Input Fields
Fields are defined by crisp 1px borders. When focused, the border transitions to Royal Blue with a subtle outer glow. Labels are placed above the field in a small, bold, uppercase "Wayfinding" style.

### Cards
Cards are the primary organizational unit. They use a Level 1 border (light grey) and no shadow by default. A "Sand" colored top-border (2px) is used for cards that contain high-priority document status or official notifications.

### Aviation-Inspired Icons
Icons must be monoline and geometric. Waypoint-style indicators should be used for list bullets. Directional cues (arrows) should mimic the styling of heading indicators on an altimeter.

### Data Tables
Tables should be clean with no vertical borders, using subtle horizontal strokes. The header row should be a pale Sand or Light Grey to distinguish "Header Data" from "Entry Data."