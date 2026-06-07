---
name: Spectrum Resonance
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#464652'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#777683'
  outline-variant: '#c7c5d4'
  surface-tint: '#4f54b4'
  primary: '#15157d'
  on-primary: '#ffffff'
  primary-container: '#2e3192'
  on-primary-container: '#9da1ff'
  inverse-primary: '#c0c1ff'
  secondary: '#006970'
  on-secondary: '#ffffff'
  secondary-container: '#7af1fc'
  on-secondary-container: '#006e75'
  tertiary: '#24292c'
  on-tertiary: '#ffffff'
  tertiary-container: '#3a3f42'
  on-tertiary-container: '#a6aaae'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#04006d'
  on-primary-fixed-variant: '#373a9b'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#5dd8e2'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  section-padding: 80px
---

## Brand & Style

The brand personality is a harmonious blend of clinical reliability and celebratory belonging. It targets the LGBTQ+ community, specifically individuals seeking a safe, affirming space for mental health support. The UI evokes a sense of "Safe Vibrancy"—it is professional enough to trust with one's deepest vulnerabilities, yet expressive enough to affirm one's identity.

This design system utilizes a **Modern Corporate** style infused with **Vibrant Accents**. It leverages heavy whitespace and high-quality typography to ensure readability and accessibility, while using rainbow gradients sparingly as "points of joy" to signify inclusivity. The aesthetic avoids clinical coldness by prioritizing soft edges and human-centric imagery.

## Colors

The palette is anchored by a deep Indigo primary color to establish authority, trust, and security. A vibrant Teal serves as the secondary color, representing health, vitality, and growth. 

The background is a clean, paper-white to maximize legibility and reduce cognitive load. The "Pride Gradient" is used strictly as a decorative accent—such as a thin top-border on cards, a progress bar, or a subtle underline—to ensure the interface remains professional and accessible without becoming visually overwhelming. Neutral greys are tinted slightly with blue to maintain a cohesive, calming atmosphere.

## Typography

This design system uses a dual-font strategy to balance character with clarity. **Plus Jakarta Sans** is used for headlines; its soft, rounded terminals feel welcoming and modern. **Inter** is used for all body text, navigation, and form labels to ensure maximum legibility across different devices and for users with varying visual needs.

Line heights are intentionally generous (1.6x for body text) to provide a "breathable" reading experience, which is critical for a portal handling sensitive therapeutic information.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop, centered with a 1280px maximum width. A 12-column system is used with generous 24px gutters to prevent information density from feeling claustrophobic. 

The spacing rhythm is built on an 8px base unit. Section-level vertical padding is kept high (80px+) to maintain the "plenty of whitespace" requirement. Elements should be grouped logically using "Proximity Principles," where related items are held within containers with 24px-32px of internal padding.

## Elevation & Depth

This design system uses **Ambient Shadows** to create a sense of depth and organization without appearing heavy. Shadows should be highly diffused (large blur radius) with very low opacity (5-8%) and a subtle tint of the primary indigo color to prevent them from looking "dirty."

The hierarchy is further defined through **Tonal Layers**. The main background is white, while secondary functional areas (like sidebars or background sections) use a very soft tertiary blue-grey. Cards use the lightest shadow level to "float" above the background, signaling they are interactive containers.

## Shapes

The shape language is defined by **Rounded** corners. This approach removes the "sharp edges" often associated with clinical or cold environments, replacing them with a softer, more organic feel. 

- Standard components (Inputs, Buttons) use a **0.5rem (8px)** radius.
- Large containers and cards use **1rem (16px)** to emphasize their role as supportive "buckets" of content.
- Profile pictures and certain status indicators may use a full pill/circle shape for a friendly, person-first aesthetic.

## Components

### Buttons
Primary buttons are solid Indigo with white text. Secondary buttons use a Teal outline. For "Celebratory" actions (like completing a milestone or joining a community), a gradient-border button or a subtle gradient hover effect may be used.

### Inclusive Form Elements
Form inputs are tall (48px-56px) with clear, persistent labels. Pronoun selectors and gender identity fields must be implemented as multi-select chips or open-text fields rather than restrictive dropdowns. Support text should be positioned directly below inputs to provide immediate guidance.

### Cards
Cards are the primary content vehicle. They feature a white background, a 1px soft-grey border, and a subtle ambient shadow. A "Pride Accent" can be applied as a 4px top-border to indicate featured content or community-sourced stories.

### Navigation
The navigation bar is clean and sticky, utilizing a high-contrast Indigo logo against a white background. Active states are indicated by a teal underline or a subtle background tint, ensuring the user always knows their location within the portal.

### Supportive Imagery
Imagery should feature diverse individuals in natural, bright settings. Illustrations should use the secondary Teal and tertiary shades to maintain a calm, professional, and cohesive visual language.