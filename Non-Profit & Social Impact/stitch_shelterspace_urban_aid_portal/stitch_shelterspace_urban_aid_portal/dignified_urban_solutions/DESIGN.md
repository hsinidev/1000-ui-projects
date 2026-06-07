---
name: Dignified Urban Solutions
colors:
  surface: '#fff8f6'
  surface-dim: '#e2d8d5'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fcf1ef'
  surface-container: '#f6ece9'
  surface-container-high: '#f0e6e3'
  surface-container-highest: '#eae0de'
  on-surface: '#1f1b19'
  on-surface-variant: '#56423e'
  inverse-surface: '#342f2e'
  inverse-on-surface: '#f9efec'
  outline: '#89726d'
  outline-variant: '#ddc0ba'
  surface-tint: '#9f402d'
  primary: '#9f402d'
  on-primary: '#ffffff'
  primary-container: '#e2725b'
  on-primary-container: '#5a0d02'
  inverse-primary: '#ffb4a5'
  secondary: '#635d5b'
  on-secondary: '#ffffff'
  secondary-container: '#e7dedb'
  on-secondary-container: '#67615f'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#929393'
  on-tertiary-container: '#2a2c2c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad3'
  primary-fixed-dim: '#ffb4a5'
  on-primary-fixed: '#3e0500'
  on-primary-fixed-variant: '#802918'
  secondary-fixed: '#e9e1de'
  secondary-fixed-dim: '#cdc5c2'
  on-secondary-fixed: '#1e1b19'
  on-secondary-fixed-variant: '#4b4644'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fff8f6'
  on-background: '#1f1b19'
  surface-variant: '#eae0de'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 64px
---

## Brand & Style
The design system is built upon a foundation of dignity, structure, and compassion. It targets urban stakeholders, case workers, and individuals seeking stability, requiring a UI that feels both institutional and deeply human. 

The style adopts a **Modern Corporate** approach infused with **Soft Minimalism**. By combining structured layouts with generous whitespace and organic roundedness, the interface avoids a cold, clinical feel. The aesthetic priority is to establish trust through "established" visual cues—high-quality typography and grounded colors—while maintaining an approachable atmosphere through soft shadows and tactile surfaces.

## Colors
The palette is anchored by **Terracotta (#E2725B)**, a warm, earthy tone that represents humanity and shelter. It is used sparingly for primary actions and highlights to maintain high contrast and focus. 

**Warm Grey** serves as the structural anchor, providing a grounded, professional feel for text and secondary elements. **Off-White (#F9F9F9)** acts as the primary background canvas, reducing harsh glare while maintaining a clean, open environment. High contrast is strictly maintained between text and backgrounds to ensure accessibility for all users, particularly in high-stress or outdoor environments.

## Typography
This design system utilizes a sophisticated pairing of **Newsreader** for headings and **Public Sans** for body and interface elements. 

**Newsreader** provides an editorial, authoritative, and literary quality that lends dignity to the content. It is used for all headings to feel "established." **Public Sans** was selected for its institutional heritage and exceptional clarity; its neutral, accessible letterforms ensure that critical information is legible at all sizes. Line heights are intentionally generous to improve reading comprehension and reduce cognitive load.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model. Content is contained within a 12-column grid on desktop with a maximum width of 1280px to prevent excessive line lengths. On mobile, a single-column layout with 16px side margins is standard.

Whitespace is treated as a core design element, not just a separator. Generous "breathing room" between sections (64px+) is used to create a sense of calm and order. Vertical rhythm is strictly enforced using an 8px base unit, ensuring that all elements align to a consistent visual beat.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** and tonal layering. Shadows are never harsh; they use a low-opacity, warm-grey tint to feel more natural and integrated with the background.

- **Level 0 (Floor):** The Off-White background (#F9F9F9).
- **Level 1 (Card):** White surfaces (#FFFFFF) with a soft, diffused shadow (12px blur, 4% opacity).
- **Level 2 (Interactive/Overlay):** White surfaces with a slightly tighter, more pronounced shadow (20px blur, 8% opacity) to indicate hover states or modals.

This subtle elevation system guides the user’s eye toward actionable content without creating visual noise or clutter.

## Shapes
The design system employs **Rounded** geometry (0.5rem base) to soften the "institutional" nature of the product. Larger containers, such as cards and hero sections, utilize `rounded-xl` (1.5rem) to create a friendly, protective feel—visualizing the concept of "shelter." 

Interactive elements like buttons and input fields use the standard 0.5rem radius to maintain a balance between friendliness and functional precision.

## Components
- **Buttons:** Primary buttons use a solid Terracotta fill with White text. Secondary buttons use a Warm Grey outline. High-contrast focus states are mandatory for accessibility.
- **Cards:** Cards are the primary vessel for information. They feature a white background, 1.5rem corner radii, and a soft ambient shadow. They should include generous internal padding (24px-32px).
- **Input Fields:** Fields utilize a subtle light grey border that thickens on focus. Labels are always persistent and set in Public Sans (Label-MD).
- **Chips:** Used for categorization (e.g., "Available Space," "Emergency"). Chips use a soft-tinted version of the primary color with dark text for high legibility.
- **Progress Indicators:** Essential for step-based applications. These use the Terracotta color to show completion, providing a sense of momentum and achievement.
- **Resource Lists:** Clean, separated by subtle borders (1px) with ample vertical padding to ensure each item is distinct and touch-friendly.