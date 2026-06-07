---
name: Serene Biological System
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
  on-surface-variant: '#414847'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717877'
  outline-variant: '#c1c8c6'
  surface-tint: '#456462'
  primary: '#456462'
  on-primary: '#ffffff'
  primary-container: '#9dbebb'
  on-primary-container: '#2f4e4c'
  inverse-primary: '#accdca'
  secondary: '#645b6b'
  on-secondary: '#ffffff'
  secondary-container: '#ebdef2'
  on-secondary-container: '#6a6171'
  tertiary: '#58605f'
  on-tertiary: '#ffffff'
  tertiary-container: '#b1b9b7'
  on-tertiary-container: '#424a49'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c7e9e6'
  primary-fixed-dim: '#accdca'
  on-primary-fixed: '#00201e'
  on-primary-fixed-variant: '#2d4c4a'
  secondary-fixed: '#ebdef2'
  secondary-fixed-dim: '#cec2d5'
  on-secondary-fixed: '#1f1926'
  on-secondary-fixed-variant: '#4c4453'
  tertiary-fixed: '#dce4e2'
  tertiary-fixed-dim: '#c0c8c6'
  on-tertiary-fixed: '#151d1c'
  on-tertiary-fixed-variant: '#404847'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
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
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  margin-page: 40px
  gutter: 24px
  section-gap: 80px
  breathing-padding: 32px
---

## Brand & Style

The design system is rooted in the intersection of neurological science and biological tranquility. It is crafted to reduce cognitive load for users undergoing rehabilitation, prioritizing a sense of safety, compassion, and progress. The brand personality is "The Gentle Guide"—authoritative yet deeply empathetic.

The visual style utilizes **Bio-Glassmorphism**: a blend of minimalism and soft, translucent layers that mimic the properties of water, leaves, and light. This approach moves away from the cold, sterile nature of traditional medical interfaces toward a "breathing" UI that feels alive and responsive. Components should appear to float within a natural environment, utilizing soft gradients and organic motion to guide the user's focus without inducing stress.

## Colors

The palette is derived from natural landscapes—specifically the muted greens of sagebrush and the soft purples of twilight flora. 

- **Soft Sage (Primary):** Used for primary actions and navigational cues. It represents growth and stability.
- **Lavender (Secondary):** Used for secondary interactions and highlighting restorative progress.
- **White & Tertiary Sage (Backgrounds):** Pure white is reserved for the base layer, while tertiary sage is used for "sunken" or secondary surface areas to provide subtle depth.
- **Natural Neutrals:** Grays are infused with a hint of green or blue to maintain the biological warmth of the design system, avoiding any harsh, mechanical tones.

## Typography

The typography in this design system uses **Plus Jakarta Sans** for its approachable, modern, and slightly rounded letterforms that mirror the "biological" aesthetic. 

Readability is paramount. The system employs generous line heights (1.6x for body text) to ensure that users with cognitive or visual fatigue can parse information easily. Headlines should remain concise, using the slightly tighter letter spacing of the display styles to create a focused, grounded appearance. All text should be rendered with high contrast against translucent backgrounds to ensure accessibility compliance.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with an emphasis on "breathing" rhythm. Content is organized into 12-column structures, but with unusually wide margins and section gaps to prevent information density from overwhelming the user.

"Breathing whitespace" is a core principle: every major functional block must be separated by at least 80px (the section-gap) to provide a clear mental break between tasks. Inter-component spacing follows an 8px base unit, favoring larger increments (24px, 32px, 48px) to reinforce the spacious, serene atmosphere of the design system.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** and **Ambient Shadows**. Instead of traditional stacking, elements in this design system feel like layers of frosted glass suspended in a bright, airy space.

- **Surface Layers:** Use a background blur of 16px to 32px with a 60% opacity white fill.
- **Shadows:** Shadows are highly diffused and tinted with the primary Sage color. Use a large blur radius (30px+) and low opacity (8-12%) to create a soft glow rather than a dark silhouette.
- **Transitions:** Depth changes should be animated with "biological" easing—slow starts and soft finishes that mimic the natural movement of a breath.

## Shapes

The shape language is organic and soft. There are no sharp corners in this design system. Standard containers use a 1rem (16px) radius, while interactive components like buttons and progress indicators utilize pill-shapes to feel more approachable and "squishy."

Organic shapes—such as asymmetrical blobs or soft-edged polygons—should be used as decorative background elements. These elements should move slightly, like microscopic life or drifting clouds, to provide a sense of life to the interface without distracting from the primary rehabilitation tasks.

## Components

Components are designed to be tactile and forgiving, catering to users who may have motor-control challenges.

- **Buttons:** Large, pill-shaped targets. The primary button uses a soft Sage gradient. Hover states should feature a "pulse" or subtle glow rather than a harsh color flip.
- **Cards:** Defined by semi-transparent glass layers and soft sage outlines (1px width, 20% opacity). They should have a slight "lift" on interaction.
- **Input Fields:** Oversized with large placeholder text. The focus state is a soft Lavender glow that gently expands the border.
- **Progress Indicators:** Use "growing" biological metaphors, such as a vine or a filling water droplet, rather than a mechanical bar.
- **Chips:** Highly rounded with 0.5rem padding. Used for filtering therapy types or mood tagging, utilizing the secondary Lavender palette.
- **Modals:** Centered with a heavy backdrop blur (20px) to completely isolate the user's focus on the task at hand, reinforcing the "serene" experience.