---
name: Zen-Den
colors:
  surface: '#faf9f8'
  surface-dim: '#dadad9'
  surface-bright: '#faf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f2'
  surface-container: '#eeeeed'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e1'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4f453b'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f0f0'
  outline: '#81756a'
  outline-variant: '#d3c4b7'
  surface-tint: '#7a582f'
  primary: '#7a582f'
  on-primary: '#ffffff'
  primary-container: '#c49a6c'
  on-primary-container: '#4f320d'
  inverse-primary: '#ecbe8e'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#535f72'
  on-tertiary: '#ffffff'
  tertiary-container: '#96a2b7'
  on-tertiary-container: '#2d394a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffddba'
  primary-fixed-dim: '#ecbe8e'
  on-primary-fixed: '#2b1700'
  on-primary-fixed-variant: '#5f401a'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#d7e3fa'
  tertiary-fixed-dim: '#bbc7dd'
  on-tertiary-fixed: '#101c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#faf9f8'
  on-background: '#1a1c1c'
  surface-variant: '#e3e2e1'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
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
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
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

The brand identity of this design system is centered on the concept of "Digital Serenity." It bridges the gap between tactile, organic living and high-tech acoustic engineering. The target audience includes high-performance professionals and wellness-conscious individuals seeking a sanctuary from sensory overload.

The design style is a hybrid of **Minimalism** and **Soft-Tactility**. It avoids the clinical coldness often associated with "smart" technology by utilizing organic textures and natural tones, while maintaining a high-end, professional edge through precise typography and sophisticated interactions. The emotional response should be one of immediate decompression—a visual "deep breath." Interactions must feel intentional and calm, utilizing "breathing" transitions (subtle scale and opacity loops) rather than jarring or snappy animations.

## Colors

The palette is anchored by three distinct pillars that represent the "Cozy & Tech" aesthetic:

*   **Warm Oak (Primary):** A rich, natural wood tone used for primary actions and highlights. It injects an organic, grounding energy into the digital interface.
*   **Slate (Secondary):** A deep, blue-toned charcoal representing the "smart" and "acoustic" technology. Used for text, iconography, and structural elements to provide high-end contrast.
*   **Off-White (Neutral):** A soft, creamy background shade that reduces eye strain compared to pure white, maintaining a clean and airy environment.

Gradients should be used sparingly and transition softly between a lightened Oak and the base Oak, or between Slate and a deep Navy, mimicking the way light hits physical furniture surfaces.

## Typography

This design system utilizes **Plus Jakarta Sans** for all levels of hierarchy. Its modern, geometric structure is softened by slightly rounded terminals, perfectly echoing the "Modern sans-serif with soft rounded edges" requirement. 

Headlines use tighter letter-spacing and heavier weights to feel authoritative and premium. Body text is prioritized for legibility with generous line heights to create a sense of openness and calm. Labels and captions are set with slight tracking to ensure clarity even at smaller scales, maintaining a professional, engineered feel.

## Layout & Spacing

The layout philosophy follows a **fixed grid** approach for desktop to maintain the composed, curated feel of a high-end interior design catalog. A 12-column grid is used with generous gutters (24px) to ensure content never feels crowded.

The spacing rhythm is built on an 8px base unit. Negative space (whitespace) is treated as a functional element—it is used aggressively to reduce cognitive load and simulate the "acoustic peace" the physical product provides. Margins are intentionally wide to draw the eye toward the center, creating a focused, meditative user experience.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layers**. Instead of harsh dropshadows, this design system uses extremely diffused, low-opacity shadows tinted with the Slate color (e.g., 5-10% opacity) to suggest that elements are gently resting on a soft surface.

To represent the tech elements, a subtle **Glassmorphism** effect is applied to overlays and floating menus. This involves a high-density backdrop blur (20px+) combined with a very thin, low-contrast Off-White border to simulate high-quality frosted glass or matte acoustic panels. This adds a sense of "tech" sophistication without sacrificing the cozy atmosphere.

## Shapes

The shape language is consistently **Rounded** (Level 2). This eliminates sharp corners that can trigger subconscious "alert" responses, replacing them with inviting, organic curves. 

Standard components (buttons, inputs) use a 0.5rem (8px) radius. Larger containers, such as product cards and feature sections, use a 1.5rem (24px) radius to mimic the steam-bent wood and molded acoustic foam of the furniture. Interactive elements should never be fully sharp, as the goal is to feel soft to the touch and compassionate in form.

## Components

*   **Buttons:** Primary buttons feature a soft linear gradient from Oak to a slightly lighter honey tone. They utilize a "breathing" hover state where the shadow diffusion expands slowly. Text is always Slate or Off-White for maximum clarity.
*   **Cards:** Use a very subtle Tonal Layer (a shade 2% darker than the background) rather than a border. This creates a "recessed" look, similar to carved wood.
*   **Input Fields:** Minimalist design with a soft-grey background and a subtle bottom-heavy focus ring in Oak. Labels are always visible to maintain a professional, accessible standard.
*   **Chips/Tags:** Pill-shaped with low-contrast fills. Used for acoustic ratings (e.g., "30dB Reduction") or material types.
*   **Progress Indicators:** Instead of spinning loaders, use "Pulse" or "Breathing" circles that expand and contract smoothly, reinforcing the anxiety-reduction theme.
*   **Acoustic Visualization:** A bespoke component for this design system—a soft, undulating waveform animation that represents real-time silence or ambient sound masking, styled in Slate and Off-White.