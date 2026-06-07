---
name: Gala-Pour
colors:
  surface: '#0d1225'
  surface-dim: '#0d1225'
  surface-bright: '#33384d'
  surface-container-lowest: '#080d20'
  surface-container-low: '#161b2e'
  surface-container: '#1a1f32'
  surface-container-high: '#24293d'
  surface-container-highest: '#2f3448'
  on-surface: '#dde1fc'
  on-surface-variant: '#d1c5b4'
  inverse-surface: '#dde1fc'
  inverse-on-surface: '#2b2f44'
  outline: '#9a8f80'
  outline-variant: '#4e4639'
  surface-tint: '#e9c176'
  primary: '#e9c176'
  on-primary: '#412d00'
  primary-container: '#c5a059'
  on-primary-container: '#4e3700'
  inverse-primary: '#775a19'
  secondary: '#c3c6d7'
  on-secondary: '#2c303d'
  secondary-container: '#454957'
  on-secondary-container: '#b5b8c9'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#a4a5a5'
  on-tertiary-container: '#393b3b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdea5'
  primary-fixed-dim: '#e9c176'
  on-primary-fixed: '#261900'
  on-primary-fixed-variant: '#5d4201'
  secondary-fixed: '#dfe2f3'
  secondary-fixed-dim: '#c3c6d7'
  on-secondary-fixed: '#171b28'
  on-secondary-fixed-variant: '#434654'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0d1225'
  on-background: '#dde1fc'
  surface-variant: '#2f3448'
typography:
  display-xl:
    fontFamily: Bodoni Moda
    fontSize: 72px
    fontWeight: '600'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '500'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '300'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.15em
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
  gutter: 32px
  margin-desktop: 80px
  section-padding: 120px
---

## Brand & Style

This design system is built upon the concept of "The Grand Sommelier"—a presence that is knowledgeable, invisible until needed, and profoundly sophisticated. The brand personality is rooted in heritage and exclusivity, targeting a discerning clientele that values rarity and seamless service.

The design style is a hybrid of **Minimalism** and **Tactile Luxury**. It prioritizes a high-ratio of whitespace (negative space) to focus the eye on the product as a piece of art. Immersiveness is achieved through atmospheric depth—using subtle grain textures and smooth transitions that mimic the slow pour of a vintage spirit. Every interaction must feel intentional, avoiding unnecessary clutter to maintain an aura of "Grand & Atmospheric" prestige.

## Colors

The palette is anchored in **Deep Midnight Blue (#0A0E1A)**, which serves as the infinite background, providing more depth than a standard black. **Burnished Gold (#C5A059)** is used sparingly for primary actions, accents, and iconography, functioning as a "light source" within the dark environment. 

**Smoke (#E5E5E5)** provides high-contrast legibility for typography and fine-line borders, ensuring the interface remains accessible despite the dark mode default. A secondary neutral, **Midnight Navy (#161B2E)**, is utilized for surface elevation and container backgrounds to differentiate between the base environment and interactive elements.

## Typography

The typography in this design system creates an editorial rhythm. **Bodoni Moda** is the voice of the brand, used for large display headers and section titles; it should frequently be used in its italic variant to denote "concierge notes" or exclusive labels.

**Manrope** provides a technical, clean counterpoint for all functional text. For body copy, a light weight (300) is preferred to maintain a sense of airy elegance. Labels and navigational items should utilize the "label-caps" style with wide letter spacing to evoke the feeling of a premium watch face or luxury spirit label.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to ensure a curated, gallery-like presentation that doesn't feel stretched or diluted. A 12-column grid is used with generous 32px gutters to prevent content density from feeling "crowded."

Vertical rhythm is defined by massive "whitespace blocks" between sections (120px+), allowing each product or service offering to stand alone as a singular focus. On mobile, margins should never drop below 24px to maintain the "expansive" brand feel even on smaller viewports.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Atmospheric Blurs** rather than traditional drop shadows. Surfaces are stacked using color:
1. **Level 0 (Base):** Deep Midnight Blue (#0A0E1A) with a subtle noise texture (2% opacity).
2. **Level 1 (Surface):** Midnight Navy (#161B2E) for cards and modals.
3. **Level 2 (Active):** Translucent Smoke overlays with a 20px backdrop blur (Glassmorphism), used for navigation bars and sticky headers.

Borders are the primary tool for definition. Use ultra-thin (1px) lines in Burnished Gold or Smoke at 20% opacity to define shapes without creating visual "noise." Shadows, when used for buttons, should be "Glows"—soft, diffused #C5A059 shadows with 0px offset and 15px blur.

## Shapes

The shape language is **Architectural and Precise**. A "Soft" roundedness (0.25rem) is applied to buttons and inputs to prevent the UI from feeling sharp or aggressive, while maintaining a structured, formal appearance. 

Product imagery should remain strictly sharp-cornered (0px) to mimic the look of framed photography or premium invitations. Circular elements are reserved strictly for avatars or "Seal of Authenticity" badges.

## Components

### Buttons
Primary buttons use a **Burnished Gold fill** with Midnight Blue text in all-caps. Secondary buttons use a **1px Smoke border** with a "Ghost" background. On hover, buttons should subtly expand (1.02x scale) with a soft gold outer glow.

### Input Fields
Inputs are "Minimalist Underlines." Instead of boxes, use a 1px Smoke bottom border. Labels should sit above in the "label-caps" style. On focus, the bottom border transitions to Burnished Gold.

### Cards
Cards for spirits or gifting packages use the Level 1 Surface color. They feature no visible border by default; depth is created by the contrast against the Level 0 Base. On hover, a 1px Gold border fades in.

### Concierge Chat & Lists
Lists use 1px Smoke separators with 24px of vertical padding per item. The Concierge Chat bubble is a floating, glassmorphic element with a Gold icon, signifying a premium human-led service.

### Additional Elements
*   **Monograms:** Every gift package display should include a placeholder for a custom gold-foiled monogram.
*   **Texture Overlays:** A subtle, non-tiling film grain should be applied to the entire viewport to give the Midnight Blue a "paper-like" quality.