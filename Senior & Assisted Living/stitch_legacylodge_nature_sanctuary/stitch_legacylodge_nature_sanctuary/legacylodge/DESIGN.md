---
name: LegacyLodge
colors:
  surface: '#fcf9f0'
  surface-dim: '#dddad1'
  surface-bright: '#fcf9f0'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ea'
  surface-container: '#f1eee5'
  surface-container-high: '#ebe8df'
  surface-container-highest: '#e5e2da'
  on-surface: '#1c1c17'
  on-surface-variant: '#45483c'
  inverse-surface: '#31312b'
  inverse-on-surface: '#f4f1e8'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#79573f'
  on-secondary: '#ffffff'
  secondary-container: '#ffd1b3'
  on-secondary-container: '#7a5840'
  tertiary: '#473e32'
  on-tertiary: '#ffffff'
  tertiary-container: '#5f5548'
  on-tertiary-container: '#d9caba'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#ffdcc6'
  secondary-fixed-dim: '#eabda0'
  on-secondary-fixed: '#2d1604'
  on-secondary-fixed-variant: '#5f402a'
  tertiary-fixed: '#efe0cf'
  tertiary-fixed-dim: '#d3c4b4'
  on-tertiary-fixed: '#221a10'
  on-tertiary-fixed-variant: '#4f4539'
  background: '#fcf9f0'
  on-background: '#1c1c17'
  surface-variant: '#e5e2da'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 60px
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 44px
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 32px
  body-md:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  label-lg:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '700'
    lineHeight: 24px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
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
  gutter: 32px
  margin-mobile: 24px
  margin-desktop: 64px
  section-gap: 80px
---

## Brand & Style

This design system is built upon the concept of "Digital Organicism," blending **Tactile Skeuomorphism** with **Minimalist** clarity. The brand personality is elder-statesman meets forest-guide: wise, calm, and deeply rooted in the natural world. It avoids the cold, clinical feel of modern healthcare in favor of a "cozy retreat" atmosphere. 

The target audience consists of seniors and their families seeking tranquility and dignity. The emotional response should be a physical sigh of relief—evoking the smell of pine needles and the texture of heavy paper. Every interaction must feel deliberate and grounded, replacing digital "snappiness" with smooth, natural transitions that respect the user's pace.

## Colors

The palette is derived directly from a forest floor at golden hour.
- **Primary (Moss Green):** Used for primary actions and navigational cues, representing growth and vitality.
- **Secondary (Earthy Brown):** Used for grounding elements, borders, and secondary buttons, evoking stability.
- **Background (Parchment):** A warm, off-white neutral that reduces eye strain and provides a tactile, paper-like foundation.
- **Tertiary (Stone):** Used for disabled states or subtle dividers to maintain a natural, non-synthetic appearance.

All color combinations must exceed WCAG 2.1 AA standards for contrast to ensure maximum legibility for senior eyes.

## Typography

This design system employs a sophisticated pairing of **Noto Serif** and **Manrope**. 
- **Noto Serif** provides the editorial authority and warmth of a printed book, used for all headlines and storytelling moments.
- **Manrope** is used for body text and functional labels; its high x-height and balanced proportions ensure exceptional readability for users with varying visual acuity. 

Text sizes are intentionally larger than standard web defaults (starting at 18px for body) to accommodate senior users. Line heights are generous to prevent "crowding" and improve focus.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to create a sense of containment and order. A 12-column grid is used for desktop, but with significantly wider gutters (32px) to allow the "Parchment" background to breathe. 

Whitespace is treated as a premium "serenity" element—elements are never cramped. The spacing rhythm is based on an 8px base unit, but primary sections should favor larger increments (64px, 80px) to maintain a slow, peaceful visual cadence. Content is centered and contained to prevent long line lengths that are difficult for seniors to track.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Physical Metaphors** rather than standard drop shadows.
- **Surface Depth:** The base layer is a textured Parchment. Interactive cards use a subtle "letterpress" effect (inward shadow) or a very soft, diffused amber-tinted shadow to appear as if resting on a wooden table.
- **Overlays:** Modals and menus utilize a "Heavy Paper" stack effect—distinct dark-brown 1px borders combined with a soft 15% opacity Moss Green shadow.
- **Texture:** Subtle grain overlays are applied to the primary Moss Green surfaces to mimic the feel of dyed linen or felt.

## Shapes

The shape language is strictly **Organic**. We avoid sharp 90-degree angles which feel industrial and aggressive.
- **Soft Corners:** A base radius of 0.5rem (8px) is applied to all standard components. 
- **Variable Radii:** To enhance the hand-crafted feel, larger containers like cards should use slightly irregular "squircle" properties where possible.
- **Hand-Drawn Icons:** Icons should feature slightly imperfect strokes and rounded terminators, as if sketched with a fine-liner pen on cotton paper.

## Components

- **Buttons:** Primary buttons are Moss Green with Earthy Brown text or white, featuring 2px solid borders. They should feel "pressable" with a slight scale-down effect on click.
- **Cards:** Use a "Pressed Flower" style—parchment-colored containers with thin Earthy Brown borders and generous 32px internal padding.
- **Inputs:** Fields are large (min-height 56px) with 2px borders. The focus state uses a soft Moss Green glow and an increased border thickness.
- **Selection (Checkboxes/Radios):** These should look like hand-inked circles or squares. The "checked" state is a simplified hand-drawn leaf or a thick ink-dot.
- **Lists:** Use custom separators like subtle horizontal "twigs" or simple Earthy Brown lines with faded ends to divide content sections.
- **Specialty Component - "The Hearth":** A prominent, high-contrast container for community news or daily schedules, always styled with a unique textured background and Noto Serif Display typography.