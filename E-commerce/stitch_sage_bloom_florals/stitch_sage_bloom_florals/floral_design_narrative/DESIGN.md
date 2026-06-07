---
name: Floral Design Narrative
colors:
  surface: '#fff9e8'
  surface-dim: '#e0dac4'
  surface-bright: '#fff9e8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf4dd'
  surface-container: '#f4eed8'
  surface-container-high: '#eee8d2'
  surface-container-highest: '#e9e2cd'
  on-surface: '#1e1c0e'
  on-surface-variant: '#4f453d'
  inverse-surface: '#333122'
  inverse-on-surface: '#f7f1da'
  outline: '#80756c'
  outline-variant: '#d2c4b9'
  surface-tint: '#74593f'
  primary: '#74593f'
  on-primary: '#ffffff'
  primary-container: '#ffdab9'
  on-primary-container: '#795e44'
  inverse-primary: '#e3c0a0'
  secondary: '#635f40'
  on-secondary: '#ffffff'
  secondary-container: '#e8e0ba'
  on-secondary-container: '#686344'
  tertiary: '#60603e'
  on-tertiary: '#ffffff'
  tertiary-container: '#e5e3b8'
  on-tertiary-container: '#656542'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdcbe'
  primary-fixed-dim: '#e3c0a0'
  on-primary-fixed: '#2a1704'
  on-primary-fixed-variant: '#5a422a'
  secondary-fixed: '#eae3bc'
  secondary-fixed-dim: '#cec7a2'
  on-secondary-fixed: '#1f1c04'
  on-secondary-fixed-variant: '#4b472b'
  tertiary-fixed: '#e6e5b9'
  tertiary-fixed-dim: '#cac99f'
  on-tertiary-fixed: '#1d1d03'
  on-tertiary-fixed-variant: '#484828'
  background: '#fff9e8'
  on-background: '#1e1c0e'
  surface-variant: '#e9e2cd'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
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
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
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
  container-max: 1280px
  gutter: 24px
  margin-edge: 40px
  section-gap: 80px
---

## Brand & Style
This design system is crafted for a high-end artisanal florist, emphasizing the ephemeral beauty of nature through a digital medium. The brand personality is serene, nurturing, and sophisticated—moving away from the frantic pace of traditional e-commerce toward a curated, editorial experience. 

The visual style is a blend of **Minimalism** and **Tactile Softness**. By utilizing generous white space and a "breathable" layout, the product photography is allowed to take center stage. The interface avoids harsh lines in favor of organic forms and soft, diffused depth, creating an atmosphere that feels as premium and well-composed as a bespoke bouquet.

## Colors
The palette is rooted in botanical tones to evoke a sense of organic luxury. 
- **Cream (#FFFDD0)** serves as the primary canvas, providing a warmer, more inviting foundation than pure white.
- **Peach (#FFDAB9)** is reserved exclusively for primary call-to-actions and conversion points, acting as a soft yet visible beacon for user intent.
- **Sage Green (#B2AC88)** is utilized for borders, decorative accents, and secondary interaction states, grounding the design in a natural aesthetic.
- **Neutral (#4A4737)** is a deep, warm olive-toned charcoal used for typography to ensure legible contrast while maintaining the soft color harmony of the system.

## Typography
The typographic hierarchy relies on the contrast between a classic serif and a modern sans-serif. **Noto Serif** is used for all headings to convey heritage and elegance; its high-contrast letterforms should be set with generous leading to maintain an editorial feel. 

**Plus Jakarta Sans** provides a clean, airy counterpoint for functional text. It features slightly rounded terminals that complement the organic shape language of the design system. Labels and navigation items should utilize increased letter spacing and medium weights to ensure clarity against the soft background colors.

## Layout & Spacing
The layout follows a **Fixed Grid** model centered within the viewport, utilizing a 12-column structure for desktop. To emphasize the premium nature of the brand, "generous whitespace" is quantified through large section gaps and wide horizontal margins. 

Internal padding within cards and containers should be expansive (minimum 32px) to prevent the UI from feeling cluttered. Elements should feel "placed" rather than "packed," with a clear vertical rhythm based on an 8px base unit.

## Elevation & Depth
Depth is communicated through **Ambient Shadows** and **Tonal Layers** rather than sharp borders. Surfaces should appear to float gently above the Cream background. 

Shadows are exceptionally soft, using a multi-layered approach with low opacity (5-10%) and a slight color tint derived from the Sage Green palette (#B2AC88) to maintain warmth. For interactive elements, a subtle "lift" effect (increasing shadow blur) is preferred over high-contrast color changes. Low-contrast Sage Green outlines (1px) are used sparingly to define boundaries of input fields and decorative containers.

## Shapes
The shape language is defined by large, organic radii that mirror the softness of flower petals. All primary containers and buttons use a **Rounded** (Level 2) logic. 

- **Standard Buttons & Inputs:** 0.5rem (8px) radius.
- **Cards & Modal Containers:** 1rem (16px) radius.
- **Feature Images & Promotional Banners:** 1.5rem (24px) radius for a distinctively friendly and soft aesthetic.
- **Chips & Tags:** Fully pill-shaped to differentiate them from functional inputs.

## Components
- **Buttons:** Primary CTAs use the Peach background with Neutral text; no borders. Secondary buttons use a Sage Green outline with a transparent background.
- **Cards:** Product cards use a subtle ambient shadow and no border. The image should occupy the top 70% of the card, featuring a large 16px corner radius.
- **Inputs:** Text fields use a 1px Sage Green border with a 0.5rem radius. Focus states are indicated by a soft Peach outer glow.
- **Chips:** Used for flower categories (e.g., "Lilies," "Spring Collection"). These should be pill-shaped with a light Sage tint (#E8E6D9) and dark Sage text.
- **Navigation:** Top-tier navigation uses Plus Jakarta Sans in all-caps for labels, with a 2px Sage Green underline for active states.
- **Floral Accent:** A custom "floating" cart button or floating action button (FAB) should be used for "Build a Bouquet" features, utilizing the Peach primary color to drive engagement.