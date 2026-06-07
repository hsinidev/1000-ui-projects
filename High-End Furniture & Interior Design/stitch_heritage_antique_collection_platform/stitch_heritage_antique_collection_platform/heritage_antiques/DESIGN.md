---
name: Heritage Antiques
colors:
  surface: '#fff8f7'
  surface-dim: '#f3d3d0'
  surface-bright: '#fff8f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff0ef'
  surface-container: '#ffe9e7'
  surface-container-high: '#ffe1df'
  surface-container-highest: '#fcdbd9'
  on-surface: '#281716'
  on-surface-variant: '#504443'
  inverse-surface: '#3f2b2a'
  inverse-on-surface: '#ffedeb'
  outline: '#827472'
  outline-variant: '#d4c3c1'
  surface-tint: '#795553'
  primary: '#321716'
  on-primary: '#ffffff'
  primary-container: '#4a2c2a'
  on-primary-container: '#bd928f'
  inverse-primary: '#eabcb8'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#231f0e'
  on-tertiary: '#ffffff'
  tertiary-container: '#383422'
  on-tertiary-container: '#a39c84'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#eabcb8'
  on-primary-fixed: '#2e1413'
  on-primary-fixed-variant: '#5f3e3c'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fff8f7'
  on-background: '#281716'
  surface-variant: '#fcdbd9'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 42px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: notoSerif
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: notoSerif
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: newsreader
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: newsreader
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  margin-mobile: 20px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is anchored in the concept of the **Digital Atelier**—a space that feels as curated, quiet, and prestigious as a private viewing room in a high-end auction house. The brand personality is authoritative, timeless, and deeply rooted in tradition, targeting ultra-high-net-worth collectors who value provenance and craftsmanship.

The visual style is **Tactile and Skeuomorphic**, utilizing realistic textures to bridge the gap between digital convenience and physical heritage. It avoids the coldness of modern minimalism in favor of "warmth" through paper textures and wood-grain motifs. The goal is to evoke an immediate sense of trust and permanence, making the user feel they are engaging with an heirloom rather than a temporary commodity.

## Colors

The palette is restricted to a classical trio that mimics the materials of fine cabinetry and archival documents. 

- **Deep Mahogany (#4A2C2A):** Used for structural elements, heavy borders, and primary buttons. It provides the visual "weight" necessary for an elite brand.
- **Gold (#D4AF37):** Reserved for accents, interactive states, and "certification" markers. It should be used sparingly to maintain its perceived value.
- **Parchment (#F4EBD0):** The primary canvas. This off-white provides a low-strain reading environment and reinforces the antique narrative.
- **Deep Espresso (#2D1B1A):** Used for text to ensure high contrast against parchment without the harshness of pure black.

## Typography

This design system utilizes a dual-serif pairing to maintain a traditional, literary feel. 

**Noto Serif** is used for headlines and titles. Its classic proportions and elegant serifs communicate sophistication and "old world" luxury. Use tighter letter-spacing for large display text to create a more bespoke, editorial look.

**Newsreader** is selected for body text and labels. Its slightly higher x-height ensures legibility on mobile devices, even against textured backgrounds. For labels and metadata (e.g., "Circa 1850"), use the small-caps variant to simulate the look of museum placards.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with generous internal safe areas. Given the mobile-first priority, the design utilizes a 4-column grid for mobile and a 12-column grid for desktop. 

Vertical rhythm is critical to maintaining the "elite" feel; whitespace (or rather, "parchment space") is used aggressively to separate items, ensuring that each piece of furniture is treated like an individual masterpiece. Content should be centered frequently to mimic the layout of a physical invitation or a high-end gallery catalog.

## Elevation & Depth

Hierarchy in this design system is achieved through **Physical Layering** rather than modern ambient shadows.

1.  **Level 0 (The Desk):** The base background, featuring a very subtle parchment grain.
2.  **Level 1 (The Folio):** Cards and content containers. These use a slightly lighter parchment tone and a 1px Mahogany border.
3.  **Level 2 (The Inlay):** Buttons and active elements. These appear "pressed" into the paper (inset shadows) or "raised" with a thin 1px Gold foil outer stroke.
4.  **The Frame:** Primary sections or hero images are enclosed in a 4px "wood grain" border (Mahogany with a subtle linear gradient to simulate texture).

Avoid using standard drop shadows. Instead, use thin, high-contrast strokes to define edges.

## Shapes

The shape language is **Soft (0.25rem)**. While modern systems often use heavy rounding, this design system uses minimal corner radii to mimic the hand-clipped edges of vintage paper and the precision of fine woodworking. 

Interactive elements like buttons and input fields should feel like solid, tangible objects. Heavy 90-degree sharp corners should be avoided as they feel too industrial, but overly round "pill" shapes are avoided to keep the aesthetic formal and mature.

## Components

### Buttons
Primary buttons are solid Deep Mahogany with Gold Noto Serif text. They feature a 1px Gold border. Secondary buttons use a transparent background with a Mahogany border and text.

### Cards (The "Folio" Card)
Cards must have a subtle paper texture overlay. The border should be a thin 1px Deep Mahogany line. For "Featured" items, add a Gold foil corner ribbon or a 2px Gold inner-border.

### Inputs & Forms
Input fields should appear as "etched" lines or boxes on the parchment. Use a bottom-border only for a more elegant, minimalist form feel. Labels should always be in the "Label-Caps" style.

### Navigation
The mobile menu uses a full-screen overlay that mimics a physical folding menu. Use Mahogany for the background and Gold for the navigation links to create a high-contrast, premium experience.

### Imagery
All furniture photography must be framed within a "Mahogany Frame" (4px border). Use a subtle inner-glow to make the photos feel like they are recessed into a shadow box.