---
name: Bubbly Modernism
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
  on-surface-variant: '#3c4948'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6c7a78'
  outline-variant: '#bbc9c7'
  surface-tint: '#006a65'
  primary: '#006a65'
  on-primary: '#ffffff'
  primary-container: '#2ebab2'
  on-primary-container: '#004541'
  inverse-primary: '#59dad1'
  secondary: '#78555b'
  on-secondary: '#ffffff'
  secondary-container: '#ffd2d8'
  on-secondary-container: '#7a585d'
  tertiary: '#516161'
  on-tertiary: '#ffffff'
  tertiary-container: '#9aabaa'
  on-tertiary-container: '#30403f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#78f6ed'
  primary-fixed-dim: '#59dad1'
  on-primary-fixed: '#00201e'
  on-primary-fixed-variant: '#00504c'
  secondary-fixed: '#ffd9de'
  secondary-fixed-dim: '#e7bcc1'
  on-secondary-fixed: '#2d1419'
  on-secondary-fixed-variant: '#5e3e43'
  tertiary-fixed: '#d4e6e5'
  tertiary-fixed-dim: '#b8cac9'
  on-tertiary-fixed: '#0e1e1e'
  on-tertiary-fixed-variant: '#3a4a49'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
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
  md: 20px
  lg: 32px
  xl: 48px
  margin: 24px
  gutter: 16px
---

## Brand & Style

This design system is built to evoke the joyful, splashing energy of a fresh pet bath. The brand personality is unapologetically friendly, nurturing, and approachable, targeting pet owners who view grooming as an act of love rather than a chore. 

The aesthetic style merges **Minimalism** with **Tactile** elements. It utilizes heavy white space to maintain a sense of "clean" and "airy" professionalism, while employing "bubbly" UI elements that feel soft to the touch. The interface should feel as light as sea foam, using gentle motion and rounded forms to create a stress-free environment for users managing their pets' care.

## Colors

The palette is anchored by a refreshing **Teal**, symbolizing cleanliness and professional care. This is balanced by **Soft Pink** accents that inject warmth and a playful, "puppy-friendly" vibe. 

The background remains predominantly **White** to ensure the app feels airy and clinical in its hygiene, but never cold. A very pale mint (Tertiary) is used for secondary containers to provide subtle depth without breaking the high-key, bright atmosphere. High-contrast dark teal is used for typography to ensure legibility while remaining softer than pure black.

## Typography

**Plus Jakarta Sans** is the sole typeface for this design system, chosen for its naturally rounded terminals and optimistic character. 

Headlines use heavy weights (Bold and ExtraBold) with tighter letter spacing to create "bubbly" headers that feel like physical objects. Body text maintains a Medium weight where possible to ensure the "friendly" weight is carried throughout the experience. Labels and buttons use SemiBold to Bold weights to ensure they stand out against soft-colored backgrounds.

## Layout & Spacing

The layout follows a **fluid grid** model optimized for mobile handsets, utilizing a generous **24px side margin** to push content inward and create an airy, focused feel. 

A strict **8pt spacing rhythm** governs the vertical flow. Generous padding within containers (specifically 20px or 32px) is encouraged to give UI elements "room to breathe," mimicking the lightness of bubbles. Avoid cramped layouts; if a screen feels busy, increase the whitespace between sections rather than reducing font sizes.

## Elevation & Depth

Visual hierarchy is achieved through **ambient shadows** and **tonal layering**. Shadows are never neutral grey; they are tinted with the primary Teal or secondary Pink at very low opacities (8-12%) and high blur radii (20px+) to create a soft, "floating" appearance.

The design uses **surface-container tiers**: 
- **Level 0:** Pure White background.
- **Level 1:** Soft Pink or Pale Teal containers for grouping content.
- **Level 2:** Floating White cards with soft, colored shadows for interactive elements.

This creates a sense of tactile depth, where elements appear to be gently resting on a bed of foam.

## Shapes

The shape language is the core of this design system's "bubbly" identity. Everything is highly rounded. 

- **Level 3 (Pill-shaped):** All primary buttons, input fields, and tags utilize a full corner radius to appear like smooth pebbles or bubbles.
- **Cards:** Use the `rounded-xl` (3rem/48px) setting for large surface areas to maintain the friendly, non-aggressive profile. 
- **Icons:** Must be enclosed in circular or squircle containers with background tints to maintain the "bubble" motif.

## Components

- **Buttons:** Large, pill-shaped, and high-contrast. The primary button uses the Teal background with White text and a soft Teal shadow. Secondary buttons use the Soft Pink background.
- **Cards:** White surfaces with a large corner radius and a 1px soft Teal border or a deep ambient shadow. No sharp corners allowed.
- **Chips:** Small, pill-shaped tags used for "Pet Type" or "Service" (e.g., "Nail Trim"). Use Soft Pink for active states and Pale Teal for inactive.
- **Input Fields:** Thick, rounded borders (2px) in Pale Teal. When focused, the border transitions to Primary Teal with a soft glow effect.
- **Progress Bars:** Represented as "filling bubbles" or thick, rounded bars that use a gradient of Teal to represent water levels.
- **Checkboxes/Radios:** Circular by default. When selected, they should "pop" slightly in size with a spring animation to reinforce the bubbly theme.
- **Pet Profiles:** Circular avatars with a thick Soft Pink ring to denote a "happy" or "active" status.