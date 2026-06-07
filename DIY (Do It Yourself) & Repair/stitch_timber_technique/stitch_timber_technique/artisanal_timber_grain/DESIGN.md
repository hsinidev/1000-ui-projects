---
name: Artisanal Timber & Grain
colors:
  surface: '#fff8f5'
  surface-dim: '#dfd9d6'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f2f0'
  surface-container: '#f3ecea'
  surface-container-high: '#eee7e4'
  surface-container-highest: '#e8e1df'
  on-surface: '#1d1b1a'
  on-surface-variant: '#4f453f'
  inverse-surface: '#33302e'
  inverse-on-surface: '#f6efed'
  outline: '#81756e'
  outline-variant: '#d2c4bc'
  surface-tint: '#705a4c'
  primary: '#26170c'
  on-primary: '#ffffff'
  primary-container: '#3d2b1f'
  on-primary-container: '#ac9181'
  inverse-primary: '#dec1af'
  secondary: '#5f5e5b'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2dd'
  on-secondary-container: '#656461'
  tertiary: '#1a1a1a'
  on-tertiary: '#ffffff'
  tertiary-container: '#2f2f2f'
  on-tertiary-container: '#989696'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fbddca'
  primary-fixed-dim: '#dec1af'
  on-primary-fixed: '#28180d'
  on-primary-fixed-variant: '#574335'
  secondary-fixed: '#e5e2dd'
  secondary-fixed-dim: '#c9c6c2'
  on-secondary-fixed: '#1c1c19'
  on-secondary-fixed-variant: '#474743'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#fff8f5'
  on-background: '#1d1b1a'
  surface-variant: '#e8e1df'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 3rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 2rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The design system is rooted in the tactile honesty of the workshop. It targets a demographic that values craftsmanship, heritage, and the "slow-made" movement—ranging from custom furniture collectors to dedicated DIY hobbyists. The emotional response is one of warmth, reliability, and high-end approachability.

The visual style is **Tactile / Skeuomorphic**, blending the precision of modern editorial design with the organic imperfections of wood. It rejects the sterility of flat design in favor of physical metaphors: surfaces that look like they could be touched, buttons that feel like they have weight, and a layout that breathes like a well-organized studio.

## Colors

The palette is derived from natural timber and traditional workshop materials.
- **Walnut Wood (Primary):** A deep, rich brown used for primary actions, navigation headers, and structural emphasis.
- **Cream (Background):** A soft, warm off-white that replaces the harshness of pure white, providing a "paper-like" or "unfinished maple" softness to the canvas.
- **Charcoal (Typography/Accents):** A grounded near-black for maximum legibility and industrial-grade contrast.
- **Burnished Oak (Accent):** A mid-tone brown used for hover states and subtle highlights to simulate wood depth.

Apply a subtle, low-opacity wood grain texture overlay (multiply mode) to the Walnut and Cream surfaces to enhance the tactile quality.

## Typography

This design system utilizes a classic editorial pairing to signal premium quality.
- **Headings:** **Noto Serif** is used to convey elegance and tradition. Use high-contrast sizing to create a clear visual hierarchy, reminiscent of high-end lifestyle magazines.
- **Body & Interface:** **Work Sans** provides a grounded, industrial clarity. Its neutral character ensures that complex DIY instructions and material lists remain highly legible across all devices.
- **Utility:** Small caps are utilized for labels, categories, and "Skill Level" badges to maintain a clean, organized look without competing with headlines.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to maintain the structured feel of a blueprint or architectural drawing. A 12-column grid is used for the main content, with generous outer margins to let the imagery breathe.

Spacing is used to create "zones" of focus. Large sections of whitespace (xl spacing) should separate different furniture collections or major DIY steps. Components within a card or list should use the base-8 rhythm (sm, md) to keep information dense and professional.

## Elevation & Depth

This design system uses **Ambient Shadows** and **Tonal Layers** to simulate physical objects sitting on a workbench. 

- **Shadows:** Use multi-layered, soft shadows with a slight brown tint (`rgba(61, 43, 31, 0.08)`) instead of pure gray. This makes elements feel like they are naturally casting shadows onto the Cream background.
- **Depressions:** Input fields and secondary containers should use a subtle inner shadow to look "routed" or "carved" into the surface.
- **Layers:** Use the Cream background as the base, with Walnut or textured overlays as the elevated "material" layer.

## Shapes

The shape language is **Soft (0.25rem)**, echoing the "eased edges" of finished timber. Pure sharp corners feel too clinical, while pill-shapes feel too digital. 

The slight rounding suggests a hand-sanded finish. Apply this consistently to buttons, cards, and input fields. Large image containers for gallery views may use a slightly larger radius (0.5rem) to soften the impact of high-contrast photography.

## Components

- **Textured Buttons:** Primary buttons use the Walnut Wood color with a subtle noise/grain texture overlay. They feature a 1px top highlight and a 2px bottom shadow to create a tactile, "pressable" feel.
- **Material Cards:** Used for DIY plans and wood types. These cards should feature a large image header, a "Skill Level" label in small caps, and a "Required Tools" icon list. The card background should be a slightly lighter shade of Cream or a very subtle wood-grain pattern.
- **Input Fields:** Styled as "routed" elements with a 1px Charcoal border at 20% opacity and an inner shadow. Focus states use a 2px Walnut border.
- **Imagery:** Photos should be high-resolution with warm white balance. Use "Close-up" shots for material details and "Environmental" shots for finished shop pieces.
- **Progress Steppers:** For DIY plans, use a vertical line-and-node system that resembles a ruler or measuring tape, using Charcoal and Walnut accents.
- **Chips/Badges:** Small, rounded-sm containers with a light timber tint or Charcoal outline to categorize wood species (Hardwood, Softwood, Reclaimed).