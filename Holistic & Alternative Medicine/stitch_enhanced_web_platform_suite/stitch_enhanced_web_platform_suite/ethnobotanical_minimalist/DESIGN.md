---
name: Ethnobotanical Minimalist
colors:
  surface: '#fcf9f5'
  surface-dim: '#dcdad6'
  surface-bright: '#fcf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ef'
  surface-container: '#f0ede9'
  surface-container-high: '#ebe8e4'
  surface-container-highest: '#e5e2de'
  on-surface: '#1c1c19'
  on-surface-variant: '#45483c'
  inverse-surface: '#31302e'
  inverse-on-surface: '#f3f0ec'
  outline: '#75796b'
  outline-variant: '#c5c8b8'
  surface-tint: '#50652a'
  primary: '#3e5219'
  on-primary: '#ffffff'
  primary-container: '#556b2f'
  on-primary-container: '#d0eba1'
  inverse-primary: '#b6d088'
  secondary: '#7d562f'
  on-secondary: '#ffffff'
  secondary-container: '#ffcb9a'
  on-secondary-container: '#79542c'
  tertiary: '#584a32'
  on-tertiary: '#ffffff'
  tertiary-container: '#716148'
  on-tertiary-container: '#f4debf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d2eca2'
  primary-fixed-dim: '#b6d088'
  on-primary-fixed: '#131f00'
  on-primary-fixed-variant: '#394d14'
  secondary-fixed: '#ffdcbe'
  secondary-fixed-dim: '#efbd8d'
  on-secondary-fixed: '#2c1600'
  on-secondary-fixed-variant: '#623f1a'
  tertiary-fixed: '#f6dfc0'
  tertiary-fixed-dim: '#d9c4a5'
  on-tertiary-fixed: '#251a07'
  on-tertiary-fixed-variant: '#53452e'
  background: '#fcf9f5'
  on-background: '#1c1c19'
  surface-variant: '#e5e2de'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 4.5rem
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 2.5rem
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.1em
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
  margin-edge: 48px
  section-gap: 120px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is built upon the intersection of clinical precision and organic serenity. The brand personality is authoritative yet nurturing—a digital apothecary that prioritizes the sensory experience of the user. The target audience seeks both the scientific efficacy of aromatherapy and the luxury of a self-care ritual.

The visual style employs a **Minimalist** foundation enriched with **Tactile** and **Organic** elements. It utilizes high-quality whitespace to create "lungs" for the interface, allowing large-scale botanical photography to drive the immersive experience. Transitions must be fluid and eased, mimicking the slow diffusion of essential oils, ensuring that every interaction feels intentional and calming.

## Colors

The palette is derived from natural, earthy pigments that evoke a sense of grounding and health.
- **Olive Green (Primary):** Represents the clinical/botanical expertise. Used for primary actions and structural emphasis.
- **Peach (Secondary):** Injects warmth and human connection. Used for sensory highlights and soft calls to action.
- **Sand (Tertiary):** Provides a natural, textured alternative to flat greys. Used for secondary surfaces and subtle borders.
- **Bone/Alabaster (Neutral):** The canvas of the application, ensuring the clinical cleanliness is maintained without the harshness of pure white.

Color application should follow a 60-30-10 distribution, where the neutral sand/bone tones dominate the space to allow the botanical imagery and olive accents to resonate.

## Typography

This design system uses a sophisticated typographic pairing to balance its clinical and organic dualities. **Newsreader** brings a literary, authoritative serif quality to headlines, evoking the feel of a high-end medical journal or a luxury editorial. **Manrope** provides a clean, modern sans-serif contrast for functional UI elements, ensuring maximum readability and a contemporary feel.

Type should be set with generous line heights to promote a sense of ease. Headlines should often be paired with significant top-margin spacing to maintain the "airy" aesthetic.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to preserve the intentionality of the whitespace, centered within the viewport. A 12-column grid is used, but content typically occupies the central 8 or 10 columns to allow the edges to breathe.

Spacing is aggressive in its use of vertical rhythm. Large "section gaps" (120px+) are used to separate different botanical stories or product categories, preventing the UI from feeling cluttered. Elements should feel like they are floating in a structured, calm environment rather than being packed into containers.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layers** and **Glassmorphism**, rather than traditional drop shadows. 

1. **Surface Tiers:** Backgrounds use the neutral Bone tone, while interactive cards or panels use a slightly lighter Alabaster or a translucent Sand.
2. **Soft Blurs:** Overlays (such as navigation bars or modal backdrops) utilize a heavy backdrop blur (20px+) with a 60% opacity fill of the Sand color. This keeps the focus on the content while maintaining a sensory connection to the imagery behind it.
3. **Ambient Glows:** Where shadows are necessary for functional depth, they are extremely diffused, low-opacity, and tinted with Olive Green to feel like natural shadows cast in a forest or garden, rather than sterile grey shadows.

## Shapes

The shape language is **Rounded (Level 2)**. A base radius of 0.5rem (8px) provides a soft, approachable feel that avoids the clinical coldness of sharp corners. Larger containers like product cards or imagery masks should utilize `rounded-xl` (1.5rem) to emphasize the organic nature of the brand. 

Interactive elements like "Add to Cart" or "Discover" buttons may use pill-shaped (rounded-full) geometry to invite touch and reinforce the sensory-first approach.

## Components

- **Buttons:** Primary buttons are solid Olive Green with Manrope Bold text. Secondary buttons use a Peach background with dark text for a "warm" call to action. Ghost buttons use a fine 1px Sand border.
- **Chips & Tags:** Small, pill-shaped elements using the Tertiary Sand color for categories like "Calming," "Organic," or "Clinical Grade."
- **Cards:** Cards for products or botanical articles feature high-aspect-ratio imagery with a "soft-reveal" animation on hover. The text content is tucked into a subtle Sand-tinted footer with a 1px top border.
- **Input Fields:** Fields are minimal, using a soft Sand background and a bottom-border only approach for a clean, clinical look. On focus, the border transitions to Olive Green.
- **Botanical Hero:** A bespoke component that pairs a large-scale, high-resolution plant image with a Display-level headline. The image should have a subtle parallax effect to enhance the immersive feel.
- **Sensory Sliders:** Customized sliders for dosage or intensity that use organic shapes for the thumb and a soft Peach-to-Olive gradient for the track.