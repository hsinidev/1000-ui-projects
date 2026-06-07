---
name: Optic-Luxe
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadad9'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f3'
  surface-container: '#eeeeed'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3f4848'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f0'
  outline: '#6f7978'
  outline-variant: '#bfc8c8'
  surface-tint: '#296767'
  primary: '#003434'
  on-primary: '#ffffff'
  primary-container: '#004d4d'
  on-primary-container: '#80bdbc'
  inverse-primary: '#94d1d1'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#2b2f2f'
  on-tertiary: '#ffffff'
  tertiary-container: '#424545'
  on-tertiary-container: '#b0b2b2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b0eeed'
  primary-fixed-dim: '#94d1d1'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#044f4f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e3'
  tertiary-fixed-dim: '#c4c7c7'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#444748'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1280px
  gutter: 24px
  margin: 48px
  section-gap: 120px
  element-gap: 16px
---

## Brand & Style

The brand personality centers on the intersection of medical rigor and high-fashion aesthetics. This design system must evoke a sense of "clinical luxury"—the feeling of entering a high-end boutique that possesses the technological precision of a world-class surgical suite. The emotional response is one of absolute trust, clarity, and exclusivity.

The design style is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes expansive "Sterile White" environments to suggest cleanliness and professional focus, while layers of translucent, "optical-clear" surfaces mimic the appearance of high-quality lenses and glass instrumentation. The visual language is defined by sharp precision, fine-gauge linework, and a sophisticated interplay between matte surfaces and metallic accents.

## Colors

The palette is engineered to reflect medical authority and premium craftsmanship. 

- **Primary (Deep Teal):** Used for primary actions, brand presence, and representing the "depth" of clinical expertise. It provides a heavy, grounding contrast against the lighter elements.
- **Secondary (Metallic Silver):** Used for decorative accents, fine borders, and subtle icon details to suggest surgical-grade steel and luxury hardware.
- **Background (Optical White):** A specialized off-white (#F8FAFA) that prevents eye strain while maintaining a sterile, bright atmosphere.
- **Neutral:** A deep carbon black used exclusively for typography to ensure maximum legibility against the light backgrounds.

## Typography

This design system utilizes **Space Grotesk** for headings to introduce a technical, geometric edge that feels innovative and precise. It is paired with **Inter** for body text to ensure clinical-grade readability and a systematic feel. 

Headlines should be set with tight letter-spacing to appear as cohesive units of information. The `label-caps` style is reserved for categorizations, navigation eyebrows, and small technical metadata, emphasizing the "instrumentation" feel of the UI.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model within a maximum container width of 1280px, centered on the viewport. This creates a focused, "editorial" feel that mimics a premium magazine or luxury lookbook.

Generous whitespace is the primary luxury indicator. Section gaps are intentionally large (120px+) to allow the eye to rest and to emphasize the "clarity" of the service. Internal component spacing follows a 4px baseline grid, ensuring that even dense medical data is presented with rigorous alignment.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and layering rather than heavy shadows.

- **Surface Levels:** The base layer is the Sterile White background. Floating elements (cards, menus) use a semi-transparent white (80-90% opacity) with a high-density backdrop blur (20px-40px).
- **Fine Lines:** Instead of shadows, use 1px "Metallic Silver" strokes to define the edges of containers. 
- **Internal Depth:** Subtle "inner glows" or 0.5px white highlights on the top edge of dark Teal elements create a polished, lens-like finish.
- **Shadows:** When necessary for functional depth (e.g., active dropdowns), use a single, highly diffused ambient shadow: `0 20px 40px rgba(0, 77, 77, 0.05)`, tinting the shadow with the primary Deep Teal to maintain color harmony.

## Shapes

The shape language is disciplined and professional. **Soft (0.25rem)** roundedness is used for most UI elements, providing just enough approachability to avoid feeling sharp or aggressive, while maintaining a structural, architectural integrity. 

- **Containers:** 4px radius for standard components, 8px for large cards.
- **Interactive Elements:** Buttons and input fields use a consistent 4px radius.
- **Geometric Accents:** Square-off decorative elements or use perfect circles for iconography to lean into the "optical" theme.

## Components

- **Buttons:** Primary buttons are solid Deep Teal with white text, using a subtle metallic silver hover state. Secondary buttons use a fine 1px Silver border with a transparent background.
- **Cards:** Glassmorphic backgrounds with a 1px Silver stroke. Content should have generous internal padding (32px+) to maintain the premium feel.
- **Input Fields:** Minimalist design with only a bottom border in Silver, transitioning to Deep Teal on focus. Use Space Grotesk for floating labels.
- **Chips/Tags:** Small, pill-shaped elements with light Teal backgrounds and Deep Teal text, used for service categories or medical certifications.
- **Progressive Disclosure:** Use fine vertical lines to connect related medical steps or "journey" items, reinforcing the precision of the optometry process.
- **Additional Suggestion:** **Comparison Sliders.** A custom component for showing "Before/After" cosmetic results or "Blur vs. Clear" vision simulations, featuring a thin Silver handle.