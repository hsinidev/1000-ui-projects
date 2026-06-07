---
name: Agave-Elite
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
  on-surface-variant: '#55423d'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#89726c'
  outline-variant: '#dcc1b9'
  surface-tint: '#9b4428'
  primary: '#6f240a'
  on-primary: '#ffffff'
  primary-container: '#8e3a1f'
  on-primary-container: '#ffb8a3'
  inverse-primary: '#ffb59f'
  secondary: '#2a6769'
  on-secondary: '#ffffff'
  secondary-container: '#aeeaec'
  on-secondary-container: '#2f6b6d'
  tertiary: '#3d3d3a'
  on-tertiary: '#ffffff'
  tertiary-container: '#545451'
  on-tertiary-container: '#cac8c4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#ffb59f'
  on-primary-fixed: '#3a0a00'
  on-primary-fixed-variant: '#7c2d13'
  secondary-fixed: '#b1edef'
  secondary-fixed-dim: '#96d1d3'
  on-secondary-fixed: '#002021'
  on-secondary-fixed-variant: '#084f51'
  tertiary-fixed: '#e4e2dd'
  tertiary-fixed-dim: '#c8c6c2'
  on-tertiary-fixed: '#1b1c19'
  on-tertiary-fixed-variant: '#474744'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  bento-gap: 16px
---

## Brand & Style

This design system is built on the intersection of ancient artisanal tradition and modern architectural precision. It caters to a discerning audience that appreciates the "slow luxury" of premium agave spirits. The visual language is grounded in **Modern Minimalism** with a **Tactile** edge, utilizing heavy structural lines and high-contrast photography to evoke the feel of a high-end lifestyle magazine.

The emotional response should be one of curated sophistication—feeling like an exclusive gallery rather than a standard e-commerce shop. Every interaction is intentional, mirroring the deliberate process of harvesting and distilling agave.

## Colors

The palette is derived from the Oaxacan landscape and the tools of the trade. 

- **Deep Terracotta (Primary):** Representing the earth and fired clay ovens. Used for key brand moments, primary CTAs, and structural accents.
- **Teal (Secondary):** A sophisticated nod to the blue-green hue of the Agave Tequilana. Used for interactive elements, highlights, and subtle depth.
- **Off-White (Background):** A clean, "paper-stock" finish that provides a premium, breathable canvas for high-contrast photography.
- **Obsidian (Neutral):** A near-black used for typography and sharp architectural borders to ensure maximum legibility and structural integrity.

## Typography

The typographic hierarchy balances heritage and precision. 

**Libre Caslon Text** is used for all headlines and display copy. Its elegant serifs evoke the history of Mexican distilleries and the "Elite" boutique nature of the brand. For mobile, display sizes are reduced significantly to maintain a magazine-style density without overwhelming the screen.

**Metropolis** provides a stark, geometric contrast for all body text, navigation, and functional labels. Its minimalist, architectural construction ensures the interface feels modern and efficient. Use `label-caps` for secondary metadata and category tags to reinforce the structured, curated feel.

## Layout & Spacing

This design system utilizes a **Bento-box layout** philosophy. Content is organized into distinct, rectangular modules with rigid alignment, creating a sense of architectural order.

- **Desktop:** A 12-column grid with wide margins (64px) to allow the high-contrast imagery to breathe. 
- **Mobile:** A 2-column fluid grid. The "Lifestyle Magazine" feel is achieved through full-bleed vertical imagery and asymmetrical bento blocks where one item might span 2 columns while others span 1.
- **Rhythm:** Use a 4px baseline grid. Padding within bento boxes should be generous (min 24px) to maintain a premium feel. Structural lines (1px weight) should be used to separate sections rather than relying solely on whitespace.

## Elevation & Depth

To maintain the architectural and artisanal aesthetic, this design system avoids traditional drop shadows. Depth is achieved through:

1.  **Tonal Layering:** Using the Primary Terracotta or Secondary Teal as background fills for specific "cells" in the bento layout to create a stacked effect.
2.  **Bold Outlines:** 1px or 2px solid borders in Obsidian or Terracotta define the boundaries of containers.
3.  **High-Contrast Overlays:** Text placed directly over high-contrast photography using semi-transparent dark scrims (20-40% opacity) to ensure legibility while maintaining a flat, modern profile.
4.  **Architectural Textures:** Subtle grain or concrete-like textures applied to container backgrounds to simulate physical materials like stone or clay.

## Shapes

The shape language is strictly **Sharp (0)**. 

To reinforce the architectural theme, all containers, buttons, and images utilize 90-degree corners. This creates a sense of strength, precision, and "crafted" construction. Circular elements are reserved strictly for iconography or small decorative "seal" motifs to mimic wax bottle seals, providing a rare but impactful break from the rigid geometry.

## Components

- **Buttons:** Rectangular with no radius. Primary buttons are solid Terracotta with White text. Secondary buttons use a Teal 1px border with Teal text (Ghost style). All buttons use `label-caps` typography.
- **Bento Cards:** The core container. These should have a 1px Obsidian border. Photography inside cards should be "cover" fit, often with a slight zoom hover effect.
- **Product Chips:** Small, rectangular tags using the Secondary Teal background with White text, used for "Añejo," "Joven," or "Limited Release" indicators.
- **Input Fields:** Bottom-border only (architectural style) in Obsidian, with labels floating above in `label-caps`.
- **Interactive Lifestyle Feed:** On mobile, implement a vertical "snap-to-card" scrolling mechanism similar to a digital lookbook, where each bento module occupies the majority of the viewport.
- **Interactive Map/Terroir Selector:** A custom component using clean lines to show the Highlands vs. Lowlands regions, utilizing the Teal and Terracotta palette.