---
name: Zen & Serene
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#42474d'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#72787d'
  outline-variant: '#c2c7cd'
  surface-tint: '#3e627c'
  primary: '#3e627c'
  on-primary: '#ffffff'
  primary-container: '#a2c7e5'
  on-primary-container: '#2e546d'
  inverse-primary: '#a6cbe9'
  secondary: '#735664'
  on-secondary: '#ffffff'
  secondary-container: '#fed8e9'
  on-secondary-container: '#795c6a'
  tertiary: '#595f68'
  on-tertiary: '#ffffff'
  tertiary-container: '#bec3cd'
  on-tertiary-container: '#4b5059'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#a6cbe9'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#244a64'
  secondary-fixed: '#fed8e9'
  secondary-fixed-dim: '#e1bdcd'
  on-secondary-fixed: '#2a1520'
  on-secondary-fixed-variant: '#593f4c'
  tertiary-fixed: '#dee3ed'
  tertiary-fixed-dim: '#c1c7d1'
  on-tertiary-fixed: '#161c24'
  on-tertiary-fixed-variant: '#414750'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 16px
  margin: 24px
---

## Brand & Style

The brand personality is rooted in emotional safety and quiet encouragement. Designed for children navigating Social-Emotional Learning (SEL), the aesthetic avoids the over-stimulation common in kids' apps. Instead, it prioritizes a "digital exhale."

The style merges **Minimalism** with **Tactile** influences. By stripping away non-essential decorations and focusing on organic, pill-like shapes, the design system creates a sense of physical softness. The goal is to make the interface feel like a supportive companion—non-judgmental, patient, and breathable. Every visual choice is made to lower the user's heart rate and reduce cognitive load, ensuring that the focus remains on mindfulness and self-reflection.

## Colors

The palette is intentionally low-vibrancy to prevent visual fatigue. 
- **Soft Blue (Primary):** Used for primary actions and focus states, representing the sky and calmness.
- **Pale Pink (Secondary):** Used for supportive elements and "soft" highlights, representing compassion and warmth.
- **White & Soft Grey (Neutrals):** The primary canvas color is a pure or slightly tinted off-white to maintain a sense of infinite space and cleanliness.

Avoid high-contrast black; use a deep, desaturated blue-grey for text to keep the reading experience gentle on the eyes.

## Typography

This design system utilizes two distinct fonts to balance character with accessibility. **Plus Jakarta Sans** is used for headlines; its naturally rounded terminals feel friendly and non-threatening. **Lexend** is employed for all body copy and labels. Originally designed to reduce visual stress and improve reading speed, Lexend's expanded character spacing is ideal for children and those with neurodiverse learning needs. 

Keep line lengths short and line heights generous to ensure the text feels "airy" and easy to track.

## Layout & Spacing

The layout follows a **fluid grid** model with exaggerated margins to create a "sanctuary" for the content. We utilize an 8px rhythmic scale, but lean heavily into the larger increments (24px, 48px, 80px) to enforce whitespace.

Elements should never feel cramped. Vertical rhythm is established through generous padding within cards and containers, ensuring that the child’s focus is isolated to one concept or interaction at a time. On mobile devices, side margins should be a minimum of 24px to prevent the UI from feeling pinched.

## Elevation & Depth

Visual hierarchy is achieved through **Ambient Shadows** and **Tonal Layers** rather than harsh borders. This design system avoids pure black shadows, instead using "colored shadows"—soft blurs with a 10-15% opacity tint of the primary Soft Blue. This makes elements appear to float gently above the surface like clouds.

Depth is used sparingly to signify interactable elements. Backgrounds use the Neutral or Tertiary colors, while active cards sit on the highest "elevation" with the softest, most diffused shadows.

## Shapes

The shape language is defined by high roundedness and organic curves. There are no sharp corners in this design system. By using **Pill-shaped (Level 3)** roundedness, we evoke feelings of safety and comfort. 

Buttons, input fields, and containers should all utilize large corner radii. This approach mirrors physical objects designed for children—soft, smooth, and easy to hold—creating a digital environment that feels "squishy" and tactile.

## Components

- **Buttons:** Use pill-shaped containers with a slight bottom-heavy shadow to create a "pressable" feel. Transitions should be slow and ease-in-out to maintain the calm mood.
- **Cards:** Large, white surfaces with `rounded-xl` corners and ambient blue shadows. Cards should have generous internal padding (min 24px).
- **Chips:** Used for mood selection or tagging, these should be Pale Pink or Tertiary Blue with no border, using `rounded-full` corners.
- **Inputs:** Fields should be oversized with a soft grey background that shifts to Soft Blue on focus. Use friendly, rounded icons to provide visual cues.
- **Progress Indicators:** Avoid thin, clinical bars. Use "Cloud Paths" or organic, thick lines that fill with a soft gradient to show progress in a journey.
- **Modals:** These should slide up gently from the bottom (Sheet style) with a heavy backdrop blur to keep the user grounded in the current context while focusing on the new task.