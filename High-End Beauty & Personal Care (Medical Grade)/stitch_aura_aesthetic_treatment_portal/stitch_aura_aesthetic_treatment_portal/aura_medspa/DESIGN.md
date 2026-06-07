---
name: Aura-MedSpa
colors:
  surface: '#f7f9ff'
  surface-dim: '#d4dbe4'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#edf4fe'
  surface-container: '#e8eef8'
  surface-container-high: '#e2e9f2'
  surface-container-highest: '#dce3ec'
  on-surface: '#151c23'
  on-surface-variant: '#4b463d'
  inverse-surface: '#2a3138'
  inverse-on-surface: '#ebf1fb'
  outline: '#7d766c'
  outline-variant: '#cec5ba'
  surface-tint: '#685d4a'
  primary: '#685d4a'
  on-primary: '#ffffff'
  primary-container: '#f7e7ce'
  on-primary-container: '#726753'
  inverse-primary: '#d3c5ad'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#e9e9e9'
  on-tertiary-container: '#676969'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0e0c8'
  primary-fixed-dim: '#d3c5ad'
  on-primary-fixed: '#221b0b'
  on-primary-fixed-variant: '#4f4533'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f7f9ff'
  on-background: '#151c23'
  surface-variant: '#dce3ec'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-padding: 80px
---

## Brand & Style

The design system is engineered to evoke a sense of serene luxury and clinical excellence. It targets a discerning clientele seeking high-end aesthetic treatments within a digital environment that feels as premium as a physical spa. The brand personality is poised, exclusive, and calming.

The chosen design style is **Minimalism** blended with **Tonal Layers**. This approach prioritizes generous negative space to reduce cognitive load and emphasize the high-quality imagery of treatments. The UI relies on a restricted, sophisticated palette and precise typography to convey authority and elegance, ensuring the portal feels like a secure, high-end sanctuary rather than a standard medical application.

## Colors

The color strategy for this design system utilizes a "Silk White" base to maintain a clean, clinical feel. "Soft Champagne" is used as the primary accent for highlights, primary actions, and decorative elements to inject warmth and luxury. "Slate" provides the necessary contrast for secondary UI elements, iconography, and navigational cues, ensuring accessibility while maintaining a sophisticated tone.

Neutral tones are derived from the Slate spectrum, moving toward a deep charcoal for text to ensure legibility without the harshness of pure black. Backgrounds should primarily utilize the Silk White or very light Champagne tints to create a soft, "glowy" atmosphere.

## Typography

This design system pairs the timeless elegance of **Noto Serif** for headlines with the modern, rhythmic clarity of **Manrope** for body and functional text. 

Headlines should be treated with generous leading and occasional tracking adjustments for a "boutique" editorial feel. Body text is optimized for readability within a portal context, utilizing a slightly wider line height to maintain the feeling of openness. Labels and small navigational elements use Manrope in uppercase with increased letter spacing to provide a refined, organized structure to the information hierarchy.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on desktop to ensure content remains focused and premium, preventing line lengths from becoming unreadable. A 12-column grid is used with wide 64px outer margins to enforce the "luxury of space."

Vertical rhythm is based on an 8px base unit. Section spacing is intentionally aggressive (80px+) to allow the eye to rest and to separate different treatment categories or portal functions. Components within cards or containers should use consistent internal padding (24px or 32px) to maintain a sense of airiness.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layers** rather than heavy borders. Surfaces should feel like they are floating slightly above the Silk White background.

Shadows must be extremely diffused with low opacity (3-5%), utilizing a hint of the Slate color in the shadow mix to avoid a "dirty" look. Surfaces can utilize subtle 1px borders in a light Champagne or Slate tint to define boundaries without adding visual weight. When elements are interactive, such as treatment cards, a subtle increase in shadow spread or a slight shift in background tint (from White to a faint Champagne) should be used to indicate state changes.

## Shapes

The shape language of this design system is **Soft**. It avoids the clinical coldness of sharp corners while steering clear of the overly "bubbly" appearance of fully rounded/pill-shaped components. 

A standard 0.25rem (4px) or 0.5rem (8px) radius is applied to buttons, input fields, and treatment cards. This subtle rounding suggests comfort and organic beauty, aligning with the wellness narrative. Large imagery containers may occasionally use a larger radius (up to 12px) to soften the visual impact of high-contrast photography.

## Components

### Buttons
Primary buttons use the Soft Champagne background with Slate or deep Neutral text. They feature a 4px corner radius and 16px horizontal padding. Hover states should involve a gentle shift in saturation or a subtle upward elevation.

### Treatment Cards
Cards are the primary vehicle for content. They feature a high-aspect-ratio image at the top, followed by a Noto Serif heading. The card container has a 1px Slate-tinted border and a soft ambient shadow. Internal padding is generous (minimum 24px).

### Input Fields
Forms should feel secure and elegant. Use Silk White backgrounds with a subtle Slate border (1px). Focus states should transition the border to Soft Champagne. Labels are positioned above the field in uppercase Manrope.

### Imagery
All photography must be high-resolution with a soft-focus aesthetic, favoring natural light and a warm color temperature. Images should have a subtle 4px corner radius to match the component architecture.

### Portal Navigation
The sidebar or top navigation uses a minimalist approach with Slate-colored icons and Manrope labels. Active states are indicated by a Soft Champagne underline or a subtle background tint.