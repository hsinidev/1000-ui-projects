---
name: Celestial-Luxe
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#313031'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#0c0f10'
  on-tertiary-container: '#797c7d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style
This design system embodies the pinnacle of orbital luxury, catering to an elite demographic that seeks the mystery of the cosmos without sacrificing the comforts of high-end terrestrial hospitality. The aesthetic—Celestial-Luxe—merges the vast, silent beauty of deep space with the tangible opulence of precious metals and refined textures.

The style is defined by **Glassmorphism** and a **Cinematic** approach to visual storytelling. Every interface element acts as a lens, utilizing frosted transparency and subtle light refraction to mimic the viewing ports of a luxury spacecraft. Ample whitespace is used not just for clarity, but to evoke the existential scale and "breathability" of the universe, ensuring the user feels unhurried and prioritized.

## Colors
The palette is rooted in the "Void and Vessel" concept. 

- **Deep Midnight Blue (#0A0E1A)** serves as the infinite canvas, providing a sense of depth and stability. It is the primary background color for all core surfaces.
- **Metallic Gold (#D4AF37)** is used sparingly for interactive highlights, key visual anchors, and status symbols, representing the "human" luxury within the void.
- **Silk White (#F8F9FA)** provides high-contrast legibility for body text and secondary icons, offering a crisp, sterile, and premium feel.

The default color mode is strictly dark to maintain the immersive space-voyage narrative.

## Typography
The typographic hierarchy creates a dialogue between the classical and the futuristic. 

**Playfair Display** is reserved for display headers and evocative titles. Its high-contrast serifs convey a sense of heritage, travel history, and prestige. 

**Inter** provides a utilitarian, high-precision contrast for all UI controls, navigational elements, and long-form content. Its geometric neutrality ensures that the interface remains functional and readable even against complex, astronomical backgrounds. 

Use `label-caps` for all navigational metadata and sub-headings to create a structured, "flight-deck" instrumentation feel.

## Layout & Spacing
The layout follows a **Fixed Grid** model on desktop to preserve the compositional integrity of high-end cinematic imagery. A 12-column grid is used with generous margins to allow content to "float" centrally. 

Spacing is intentionally oversized. Between major sections, a gap of 120px is standard to prevent visual clutter and maintain the luxury of space. The spacing rhythm is based on an 8px scale, ensuring consistent alignment of glassmorphic cards and gold accents.

## Elevation & Depth
Depth is achieved through **Glassmorphism and Tonal Layering** rather than traditional drop shadows.

1.  **Base Layer:** Solid Deep Midnight Blue or full-screen high-resolution imagery.
2.  **Mid Layer (Cards):** 40-60% opacity Midnight Blue with a `backdrop-filter: blur(20px)`. These surfaces should have a 1px solid border at 10% Silk White opacity to catch the "light" from the stars.
3.  **Top Layer (Active/Hover):** Elements utilize a subtle Gold-tinted glow (`accent_glow_hex`) to indicate interactivity.

Avoid harsh black shadows; instead, use inner glows and thin, luminous borders to define edges against the dark background.

## Shapes
The design system utilizes **Rounded** shapes to soften the technical nature of space travel. 

Corners are set to `0.5rem` (8px) for standard components and `1rem` (16px) for larger cards. This "Soft Geometric" approach suggests the ergonomic engineering found in luxury habitats. Circular shapes are used exclusively for avatars and specific orbital-themed progress indicators.

## Components
- **Buttons:** Primary buttons feature a solid Metallic Gold background with Silk White text, utilizing a slight outer glow on hover. Secondary buttons are "Ghost" style with a gold border and transparent center.
- **Translucent Cards:** The core container for content. Must include a `backdrop-filter: blur` and a subtle 1px Silk White top-border to simulate light hitting the edge of glass.
- **Input Fields:** Minimalist design with only a bottom border in Silk White (30% opacity). When focused, the border transitions to Metallic Gold with a faint glow.
- **Chips/Badges:** Small, high-radius (pill-shaped) elements with a 10% Silk White fill and Silk White text for metadata like "Available" or "Premium Class."
- **Immersive Imagery:** Full-bleed imagery should be treated as a component, often placed behind glassmorphic layers to create a sense of looking through a window.
- **Navigation:** A top-aligned, fixed bar with a heavy blur and no background color, allowing the voyage imagery to bleed through the UI.