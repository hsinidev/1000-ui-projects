---
name: Vista-AR
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4b463d'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
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
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  section-gap: 120px
  container-padding: 40px
  element-gap: 24px
  grid-columns: '12'
  grid-gutter: 32px
---

## Brand & Style
This design system is engineered for the ultra-luxury real estate market, where the interface must act as a silent, sophisticated gallery for high-fidelity property photography. The aesthetic is **Minimalist-Refined**, emphasizing curation over clutter. 

The visual narrative is driven by **Glassmorphism**, utilizing layered transparency to create a sense of depth and lightness. By mimicking the properties of frosted glass, the UI feels airy and ethereal, allowing property visuals to bleed through the interface without sacrificing legibility. Every interaction should feel intentional, calm, and exclusive, evoking the emotional response of entering a high-end architectural space.

## Colors
The palette is rooted in a "Silk and Stone" philosophy. 
- **Silk White (#F8F8F8):** Serves as the primary canvas, providing a crisp, expansive background that feels more premium than standard white.
- **Soft Champagne (#F7E7CE):** Used sparingly as a signature accent for primary calls-to-action, active states, and highlights. It represents warmth and exclusivity.
- **Slate (#708090):** The primary color for secondary text, borders, and iconography, providing a softer alternative to black for a refined contrast.
- **Surface Neutrals:** Deep charcoal (#2C2C2C) is reserved for high-contrast typography and primary navigation to ensure authority and legibility.

## Typography
The typographic hierarchy relies on the contrast between the heritage of **Playfair Display** and the modern precision of **Manrope**.

- **Serif (Headings):** Use Playfair Display for all editorial moments and property titles. It should feel like a luxury magazine masthead.
- **Sans-serif (Body & UI):** Use Manrope for all functional text, data, and body copy. Its balanced proportions maintain clarity at smaller scales.
- **Labeling:** Small labels and utility text should use Manrope with increased letter spacing and uppercase styling to denote a "curated" architectural detail.

## Layout & Spacing
The layout follows a **Fixed Grid** model centered on the screen, creating a focused, "boutique" browsing experience. 

- **Whitespace:** Implement generous margins (120px+ between sections) to allow the design to breathe.
- **Grid:** A 12-column grid with wide gutters (32px) ensures that content never feels cramped.
- **Photography:** Property images should often break the grid or bleed to the edges to create an immersive, high-fidelity experience.

## Elevation & Depth
Depth is achieved through the intersection of light and transparency rather than heavy shadows.

- **The Glass Layer:** Overlays use a backdrop-filter (blur: 20px) with a semi-transparent white background (`rgba(248, 248, 248, 0.6)`). 
- **Borders:** "Ghost Borders" are essential—1px solid white with 40% opacity—to define the edges of glass panels without adding visual weight.
- **Shadows:** Use only one "Signature Shadow": a very soft, highly diffused ambient occlusion (Blur: 40px, Y: 10px, Color: `rgba(112, 128, 144, 0.08)`).

## Shapes
This design system utilizes **Rounded** (Level 2) geometry. 

- **Standard Elements:** Buttons and input fields use a 0.5rem (8px) radius.
- **Cards & Overlays:** Larger containers like property cards or glass modals use 1rem (16px) or 1.5rem (24px) for a softer, more organic architectural feel.
- **Imagery:** Large property hero shots should remain sharp or have a very subtle 4px radius to maintain a professional, architectural edge.

## Components
- **Glass Buttons:** Primary buttons use a solid Soft Champagne fill. Secondary buttons use a glass background (frosted) with a Silk White semi-transparent border and Slate text.
- **Property Cards:** High-fidelity images act as the card background. Text information is housed in a glassmorphic footer at the bottom of the card, blurring the image beneath it.
- **Inputs:** Ultra-minimalist bottom-border-only or very light Silk White fills with subtle Slate labels. Focus states should gently transition the border color to Soft Champagne.
- **Floating Navigation:** A fixed-position glass header that blurs property content as the user scrolls, creating a seamless sense of place.
- **Chips:** Small, pill-shaped tags with a Silk White background and Slate text, used for property features (e.g., "5 BEDS," "POOLSIDE").