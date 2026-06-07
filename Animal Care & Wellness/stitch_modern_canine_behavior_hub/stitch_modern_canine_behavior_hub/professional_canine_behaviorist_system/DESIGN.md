---
name: Professional Canine Behaviorist System
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#795900'
  on-secondary: '#ffffff'
  secondary-container: '#ffc329'
  on-secondary-container: '#6f5100'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#0d1c2f'
  on-tertiary-container: '#76859b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#ffdf9f'
  secondary-fixed-dim: '#f9bd22'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5c4300'
  tertiary-fixed: '#d5e3fd'
  tertiary-fixed-dim: '#b9c7e0'
  on-tertiary-fixed: '#0d1c2f'
  on-tertiary-fixed-variant: '#3a485c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
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
    lineHeight: '1.5'
  label-sm:
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
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is anchored in the balance between clinical expertise and empathetic coaching. It targets pet owners seeking high-level behavioral intervention without the coldness of a medical facility. The visual style is **Corporate / Modern** with a focus on high-quality, video-first storytelling. 

By utilizing generous whitespace and a "human-centric" layout, the interface avoids the cluttered look of many pet-service websites. The emotional response is one of immediate relief and confidence: "I have found an expert who understands both my dog’s biology and my personal frustration." The design avoids "childish" tropes (like paw-print patterns or cartoonish illustrations) in favor of sleek, professional aesthetics that treat dog behavior as a serious, science-led discipline.

## Colors

The palette is built on a foundation of **Deep Navy Blue**, representing authority and psychological stability. This is countered by a vibrant **Sunflower Yellow**, used sparingly to highlight calls to action, progress indicators, and "aha!" moments in training.

- **Primary (Navy):** Used for headers, footers, and primary text to establish a sense of grounded expertise.
- **Accent (Yellow):** Used for interactive elements and high-energy touchpoints. It provides a visual "spark" that represents the energy of a well-behaved dog.
- **Neutrals:** A range of soft, cool greys and off-whites ensure the interface remains airy. These neutrals provide the necessary "quiet" space for video content to stand out.

## Typography

This design system utilizes a dual-sans-serif approach to maximize both personality and accessibility. 

**Plus Jakarta Sans** is used for headlines. Its rounded terminals and open apertures feel inherently friendly and optimistic, preventing the Navy Blue from feeling too heavy or intimidating.

**Lexend** is used for all body copy and instructional text. Originally designed to improve reading proficiency, its hyper-legible character spacing and geometric clarity ensure that complex behavioral advice is easy to digest, even on mobile devices during a training session.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to maintain a premium, "editorial" feel, transitioning to a fluid single-column for mobile. A 12-column grid is used to organize content, with video assets typically spanning 8 columns to ensure they remain the focal point.

Spacing follows an 8px rhythmic scale. We prioritize "breathability"—larger vertical stacks (48px+) are used between major content blocks to prevent the user from feeling overwhelmed by information. Video-first layouts should utilize an aspect ratio of 16:9 for instructional content, framed with generous padding to create a "gallery" effect.

## Elevation & Depth

To maintain the "Modern & Approachable" vibe, the design system avoids heavy shadows in favor of **Ambient Shadows**. Surfaces feel like they are floating just above the background, with soft, high-diffusion blurs (e.g., 20px blur, 4% opacity) tinted slightly with the Navy primary color.

**Tonal Layers** are used to differentiate "learning zones" from "action zones." Instructional cards sit on the highest elevation, while background containers use subtle shifts in neutral greys to create a nested hierarchy. This prevents the clinical look of high-contrast borders while maintaining a clear structural order.

## Shapes

The shape language is consistently **Rounded**. By using a 0.5rem (8px) base radius, we soften the "professional" edges of the navy palette, making the interface feel tactile and safe. 

Video players and primary containers should use `rounded-xl` (24px) to create a soft, modern frame for visual content. Buttons and input fields use `rounded-lg` (16px) to invite interaction without becoming "pill-shaped," which can often look too casual or "childish" for an expert-led brand.

## Components

- **Buttons:** Primary buttons use the Sunflower Yellow background with Navy text for maximum contrast. They feature a subtle "lift" on hover via an increased ambient shadow.
- **Cards:** Used primarily for "Training Modules" or "Behavior Tips." Cards should have a white background, a soft ambient shadow, and a top-aligned video or high-quality image.
- **Chips:** Small, rounded labels (using `label-sm`) that categorize dog behaviors (e.g., "Anxiety," "Aggression," "Puppy Basics"). These use the Navy color at 10% opacity with solid Navy text.
- **Inputs:** Clean, outlined fields with 2px borders in a soft neutral. On focus, the border transitions to Navy to signal "expert mode" and concentration.
- **Video Player:** Custom-skinned with a Sunflower Yellow progress bar. Play buttons are large and centered to encourage the "video-first" consumption model.
- **Success States:** Checkboxes and progress indicators use a soft green (to signify safety/success) but maintain the rounded corner language of the rest of the system.