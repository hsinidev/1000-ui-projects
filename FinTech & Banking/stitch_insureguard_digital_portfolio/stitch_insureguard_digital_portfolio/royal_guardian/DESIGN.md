---
name: Royal Guardian
colors:
  surface: '#f9f9ff'
  surface-dim: '#d2daf0'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e9edff'
  surface-container-high: '#e0e8ff'
  surface-container-highest: '#dbe2f9'
  on-surface: '#141b2c'
  on-surface-variant: '#484554'
  inverse-surface: '#293041'
  inverse-on-surface: '#edf0ff'
  outline: '#797586'
  outline-variant: '#c9c4d7'
  surface-tint: '#6042d6'
  primary: '#451ebb'
  on-primary: '#ffffff'
  primary-container: '#5d3fd3'
  on-primary-container: '#d8ceff'
  inverse-primary: '#cabeff'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#414547'
  on-tertiary: '#ffffff'
  tertiary-container: '#595c5f'
  on-tertiary-container: '#d2d5d7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e6deff'
  primary-fixed-dim: '#cabeff'
  on-primary-fixed: '#1c0062'
  on-primary-fixed-variant: '#4723be'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#44474a'
  background: '#f9f9ff'
  on-background: '#141b2c'
  surface-variant: '#dbe2f9'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.02em
  h3:
    fontFamily: Public Sans
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
  caption:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
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
  md: 24px
  lg: 40px
  xl: 64px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The brand personality for this design system is "The Guardian"—a reliable, sophisticated, and protective presence in the complex world of insurance. It prioritizes clarity and peace of mind over urgency or hype. The target audience includes modern professionals and families seeking a secure, simplified experience when comparing high-stakes financial products.

The visual style is **Corporate Modern** with a lean toward **Minimalism**. By stripping away unnecessary decorative elements and focusing on high-quality whitespace, the design system emphasizes transparency and institutional trust. The interface feels "cushioned" and safe through the use of soft shapes and a calm, curated palette.

## Colors

The palette is anchored by **Royal Purple**, a color that conveys both luxury and stability. This primary hue is used purposefully for calls to action, brand markers, and critical path highlights. 

**Crisp White** serves as the primary canvas, ensuring the interface feels open and breathable. **Soft Grey** is utilized for container backgrounds and secondary sections to create subtle depth without introducing visual noise. For functional states, use a success green (#027A48) and an error red (#D92D20), ensuring they are always paired with clear iconography to maintain the design system's commitment to accessibility.

## Typography

**Public Sans** is the exclusive typeface for this design system. Chosen for its institutional heritage and exceptional legibility, it provides a neutral yet authoritative voice. 

Headlines utilize a tighter letter-spacing and heavier weights to command attention, while body text maintains a generous line height to prevent user fatigue during policy comparisons. Consistency in font family across all levels reinforces the feeling of a unified, secure platform. All labels should be clear and descriptive, avoiding overly technical jargon.

## Layout & Spacing

This design system employs a **Fixed Grid** model to ensure a predictable and organized information hierarchy. A 12-column grid is used for desktop layouts with a maximum container width of 1280px. 

The spacing rhythm is built on an 8px base unit. Generous internal padding within cards and sections is a requirement to evoke the "Safe" aesthetic. Layouts should favor vertical stacking of information in comparison views to allow for easy scannability. Use "lg" (40px) and "xl" (64px) spacing units to separate major content blocks, creating a sense of calm and order.

## Elevation & Depth

To reinforce the protective feel, depth is conveyed through **Ambient Shadows** and **Tonal Layers**. Instead of harsh black shadows, this design system uses extra-diffused shadows with a slight Royal Purple tint (e.g., 4% opacity of the primary color) to make elements feel like they are softly resting on the surface.

Lower-level elements (like inactive cards) use a 1px Soft Grey border instead of a shadow. When an element is interacted with or highlighted, it "elevates" using a soft shadow, signaling importance. This tactile approach makes the UI feel responsive and physical, which builds user confidence during the insurance selection process.

## Shapes

The shape language is the primary driver of the "Safe" and "Approachable" UX. This design system utilizes **Pill-shaped (Level 3)** roundedness. 

All primary buttons, input fields, and tags must feature fully rounded (pill) ends. Cards and modal containers should use a 2rem (32px) radius. This rejection of sharp corners removes visual "aggression" from the interface, making the daunting task of buying insurance feel more like a guided, friendly conversation.

## Components

### Buttons
Primary buttons are pill-shaped, filled with Royal Purple, and utilize white text. Secondary buttons use a Royal Purple outline with a subtle Soft Grey background on hover. Shadows are reserved for the "active" or "hover" states to provide tactile feedback.

### Cards
Cards are the cornerstone of the aggregator experience. They feature a 2rem corner radius, a 1px Soft Grey border, and a very soft ambient shadow. Internal padding should never drop below 24px (md) to ensure content never feels cramped.

### Input Fields
Inputs follow the pill-shaped language. They use a Soft Grey background with a subtle border that transitions to Royal Purple upon focus. Placeholder text should be a mid-tone grey to ensure legibility.

### Comparison Chips
To assist in filtering insurance types, use pill-shaped chips. Inactive chips have a Soft Grey background; active chips are Royal Purple with white text.

### Trust Indicators
Include a specialized "Secure Check" component—a small, pill-shaped badge with a lock icon and the primary color—to be used near sensitive data entry points and final checkout buttons to reassure the user.