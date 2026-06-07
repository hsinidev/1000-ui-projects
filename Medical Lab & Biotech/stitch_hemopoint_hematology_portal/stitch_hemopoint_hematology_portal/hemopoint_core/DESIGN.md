---
name: HemoPoint Core
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#5a403c'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#8e706b'
  outline-variant: '#e3beb8'
  surface-tint: '#b52619'
  primary: '#610000'
  on-primary: '#ffffff'
  primary-container: '#8b0000'
  on-primary-container: '#ff907f'
  inverse-primary: '#ffb4a8'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#292d2f'
  on-tertiary: '#ffffff'
  tertiary-container: '#3f4345'
  on-tertiary-container: '#acb0b2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#920703'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#181c1e'
  on-tertiary-fixed-variant: '#434749'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The brand identity centers on clinical authority and patient-centric stability. As a specialized hematology platform, the UI must balance the gravity of blood disorders with the reassurance of modern medical advancement. The aesthetic is defined as **Microscopic Minimalism**: a style that mimics the view through a high-end laboratory lens—clean, focused, and iterative.

The target audience includes hematologists, laboratory technicians, and patients managing chronic blood conditions. The UI avoids clinical coldness by utilizing organic circular motifs and soft depth, ensuring the experience feels human yet scientifically rigorous. Every interaction should evoke a sense of precision, safety, and institutional trust.

## Colors

This design system utilizes a high-contrast palette to ensure WCAG AA accessibility compliance while maintaining a sophisticated medical aesthetic.

*   **Deep Crimson (#8B0000):** Used strategically for primary actions, critical data points, and branding. It represents the biological focus of the platform but is applied with restraint to avoid alarmism.
*   **Slate Grey (#708090):** The primary functional color for secondary actions, iconography, and structural borders. It provides a grounded, neutral balance to the crimson.
*   **White (#FFFFFF) & Tertiary Ice (#F4F7F9):** The foundation of the "microscopic" look. Pure white is reserved for cards and active surfaces, while the soft ice-blue/grey is used for backgrounds to reduce eye strain.
*   **Semantic Colors:** Success states use a muted emerald; warnings use a deep ochre to maintain the "Solid & Trusted" tone without breaking the primary palette's dignity.

## Typography

The typographic scale uses a hybrid approach to blend tradition with modern utility. 

**Newsreader** is employed for headings and editorial content. Its serif construction provides the "authoritative and literary" feel necessary for medical expertise and trust. 

**Public Sans** is used for all functional UI elements, body copy, and data visualization. Its institutional clarity and neutral tone ensure that complex medical data remains highly legible and accessible. All labels utilize slightly increased letter spacing and a heavier weight to ensure clear categorization in dense information environments.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to maintain a contained, laboratory-slide feel, transitioning to a fluid model for mobile. A 12-column grid is standard, with generous gutters to prevent information density from becoming overwhelming.

The "Microscopic" theme is reinforced through the use of whitespace; elements are given ample "breathable" room, mimicking the isolation of a specimen under a lens. Vertical rhythm is strictly enforced using an 8px base unit to ensure alignment across complex clinical dashboards.

## Elevation & Depth

Visual hierarchy is achieved through **Tonal Layers** combined with **Ambient Shadows**. This design system avoids harsh dropshadows in favor of "biological" depth—soft, diffused shadows that suggest an object is gently floating just above the surface.

*   **Surface Level (L0):** Tertiary Ice background.
*   **Card Level (L1):** Pure white surfaces with a 15% opacity Slate Grey blur (20px radius, 4px offset).
*   **Overlay Level (L2):** Modals and tooltips use a slightly more pronounced shadow with a subtle Crimson tint (2% opacity) in the shadow color to tie back to the brand.
*   **Interaction:** On hover, elements do not move "up" (no Y-axis shift); instead, the shadow spread increases slightly to simulate a lens focusing on the object.

## Shapes

The shape language is the core of the 'Microscopic' aesthetic. It utilizes high roundedness to mirror the organic, cellular nature of hematology. 

*   **Primary Containers:** Use a `rounded-lg` (2rem) setting to soften the clinical edge.
*   **Interactive Elements:** Buttons, tags, and input fields utilize full pill-shaped (rounded-full) geometry.
*   **Circular Motifs:** Use perfect circles for status indicators, avatars, and data point markers in graphs to reinforce the microscopic slide metaphor.

## Components

*   **Buttons:** Primary buttons are pill-shaped, solid Deep Crimson with white text. Secondary buttons use a Slate Grey outline with a subtle 1px border.
*   **Chips (Cell Tags):** Small, fully rounded badges used for blood types or diagnosis categories. Use light Slate Grey backgrounds with dark Slate Grey text for a "label" look.
*   **Cards:** Pure white with a 32px corner radius. These should contain significant padding (24px+) to maintain the clean, structured feel.
*   **Input Fields:** Pill-shaped with a soft Slate Grey border (1px). Focus states should transition the border to Deep Crimson and add a very soft crimson glow.
*   **Lists:** Items are separated by soft grey lines that stop 16px short of the container edge, creating a floating effect.
*   **The "Lens" Toggle:** A specialized component for switching views (e.g., Patient vs. Lab View) that uses a circular sliding indicator.
*   **Data Visualization:** Charts should use rounded caps on all bars and soft, curved lines for trends, avoiding sharp angles entirely.