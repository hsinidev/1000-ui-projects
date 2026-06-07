---
name: NomadProtect
colors:
  surface: '#fbf8ff'
  surface-dim: '#d5d8f9'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f2ff'
  surface-container: '#ececff'
  surface-container-high: '#e5e6ff'
  surface-container-highest: '#dee0ff'
  on-surface: '#161a32'
  on-surface-variant: '#414754'
  inverse-surface: '#2b2f48'
  inverse-on-surface: '#f0efff'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005cbc'
  primary: '#005ab7'
  on-primary: '#ffffff'
  primary-container: '#0072e5'
  on-primary-container: '#fefcff'
  inverse-primary: '#abc7ff'
  secondary: '#6b5c4c'
  on-secondary: '#ffffff'
  secondary-container: '#f4dfcb'
  on-secondary-container: '#716252'
  tertiary: '#5a5c5d'
  on-tertiary: '#ffffff'
  tertiary-container: '#737576'
  on-tertiary-container: '#fcfdfe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#004590'
  secondary-fixed: '#f4dfcb'
  secondary-fixed-dim: '#d7c3b0'
  on-secondary-fixed: '#241a0e'
  on-secondary-fixed-variant: '#524436'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fbf8ff'
  on-background: '#161a32'
  surface-variant: '#dee0ff'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
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

The design system is anchored in the concept of "Atmospheric Safety"—merging the high-stakes reliability of health insurance with the weightless freedom of global travel. The aesthetic leverages a refined **Soft-UI (Neumorphism)** approach to create a tactile, interface-as-object experience that feels both innovative and familiar.

By utilizing generous whitespace and a "travel-driven" airy layout, the UI mimics the clarity of an open horizon. The brand personality is defined by three pillars:
*   **Trustworthy:** Professionalism conveyed through precise geometry and clear typography.
*   **Fluid:** Seamless transitions and soft edges that adapt to the nomadic lifestyle.
*   **Adventurous:** A palette and iconography set inspired by natural elements like sand and sky.

## Colors

The palette is derived from coastal landscapes to evoke a sense of calm and exploration.

*   **Azure Blue (Primary):** Used for primary actions, progress indicators, and links. It represents the sky and the dependable nature of the insurance coverage.
*   **Sand Beige (Secondary):** Used for background accents and tactile surfaces. It grounds the UI and provides a warm, organic contrast to the digital blue.
*   **White & Off-White:** The core canvas. Surfaces use a slightly tinted white to allow for the highlights of the neumorphic shadows to remain visible.
*   **Deep Slate (Neutral):** Reserved for high-readability text and structural icons, ensuring accessibility against the softer background tones.

## Typography

The design system utilizes **Plus Jakarta Sans** for all levels of hierarchy. This typeface was selected for its modern, friendly apertures and its geometric clarity, which complements the soft, rounded UI elements.

Headlines should use a tighter letter-spacing and heavier weights to establish authority. Body text maintains a generous line height (1.6) to ensure legibility during travel or high-stress situations (e.g., viewing policy details). Labels utilize uppercase styling with slight letter spacing for distinct categorization and "passport-stamp" aesthetics.

## Layout & Spacing

This design system employs a **Fluid Grid** model with an 8px baseline rhythm. The layout is designed to feel "airy," meaning margins and paddings are intentionally larger than standard corporate SaaS to reduce cognitive load.

The 12-column grid is used for desktop, collapsing to 4 columns for mobile. Elements should often "float" within their containers, using the `xl` spacing for vertical section breaks to maintain the travel-inspired openness. Avoid crowding elements; if a section feels dense, increase the internal padding by one step in the scale.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. We use a refined **Soft-UI Neumorphism** approach:

*   **Positive Elevation (Extruded):** Created using two shadows. A light shadow (White, #FFFFFF at 80% opacity) on the top-left and a soft dark shadow (Sand Beige or Light Azure, 20% opacity) on the bottom-right. This makes elements appear to emerge from the background.
*   **Negative Elevation (In-set):** Used for input fields and active button states. The shadows are reversed and placed inside the element’s border, creating a "pressed" or "hollow" effect.
*   **Atmospheric Blur:** For modal overlays or navigation bars, a subtle backdrop blur (12px) is used to maintain the "Airy" feel without losing the context of the travel imagery beneath.

## Shapes

The shape language is defined by significant roundedness to reinforce the "Fluid" brand personality. 

*   **Base Elements:** Standard cards and containers use a 1rem (`rounded-lg`) corner radius.
*   **Interactive Elements:** Buttons and tags often lean toward pill-shaped (`rounded-xl`) geometry to feel more "squishy" and tactile.
*   **Avoidance of Sharpness:** 0px corners are strictly prohibited as they conflict with the soft-UI aesthetic and the welcoming nature of the service.

## Components

*   **Buttons:** Must feature the dual-shadow neumorphic effect. The primary button uses Azure Blue with a subtle inner glow. The "pressed" state must transition to an in-set shadow to provide physical feedback.
*   **Cards:** Should appear to float. Use a Sand Beige background color slightly different from the main canvas to make the white highlights pop.
*   **Input Fields:** Utilize the in-set (concave) shadow style to indicate "receptacle" areas for data. Use a 2px Azure Blue border only when the field is focused.
*   **Chips/Badges:** Pill-shaped with very soft color fills. Use these for travel destinations or insurance coverage types (e.g., "Dental," "Adventure Sports").
*   **Progress Trackers:** Vertical lines with soft, glowing nodes, mimicking a travel itinerary or flight path.
*   **Policy Toggles:** Large, tactile switches that look like physical sliders on a high-end travel gadget.