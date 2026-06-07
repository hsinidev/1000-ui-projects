---
name: Botanical Editorial
colors:
  surface: '#fbf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#fbf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1a'
  on-surface-variant: '#434843'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ee'
  outline: '#737873'
  outline-variant: '#c3c8c1'
  surface-tint: '#516354'
  primary: '#4e6052'
  on-primary: '#ffffff'
  primary-container: '#67796a'
  on-primary-container: '#f6fff4'
  inverse-primary: '#b8ccba'
  secondary: '#5e5e5c'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdc'
  on-secondary-container: '#636360'
  tertiary: '#824c5d'
  on-tertiary: '#ffffff'
  tertiary-container: '#9e6475'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b8ccba'
  on-primary-fixed: '#0e1f14'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#e4e2de'
  secondary-fixed-dim: '#c8c6c3'
  on-secondary-fixed: '#1b1c1a'
  on-secondary-fixed-variant: '#474744'
  tertiary-fixed: '#ffd9e2'
  tertiary-fixed-dim: '#f8b4c7'
  on-tertiary-fixed: '#350d1c'
  on-tertiary-fixed-variant: '#693748'
  background: '#fbf9f6'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2e0'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 72px
    fontWeight: '400'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin-edge: 64px
  section-gap: 128px
  stack-sm: 4px
  stack-md: 16px
---

## Brand & Style
This design system is anchored in the aesthetic of high-end luxury lifestyle journalism. It targets discerning clientele who value artisanal horticulture and bespoke floral arrangements. The emotional response is one of tranquility, organic beauty, and curated sophistication.

The design style is **Editorial Minimalism**. It prioritizes vast amounts of whitespace to allow high-resolution macro photography to serve as the primary visual driver. Elements are characterized by thin, intentional borders, deliberate asymmetrical layouts, and a sophisticated interplay between traditional serif elegance and modern functionalism.

## Colors
The palette is rooted in a "Garden-to-Table" philosophy. The base of the interface is the Cream background (#FDFBF7), providing a warmer, more organic feel than pure white. Sage Green (#7A8D7D) acts as the primary brand anchor, used for structural elements and key actions.

A multi-color floral palette provides vibrant accents for categorization and visual interest:
- **Peony Pink (#E8A5B8):** Used for romantic and seasonal highlights.
- **Lavender (#A5A6D8):** Reserved for fragrance or wellness-themed content.
- **Marigold (#F2AF5C):** High-energy accents for sun-loving plants or warnings.
- **Cornflower Blue (#7DA7D9):** Cool-toned accents for winter blooms or water-related data.

## Typography
The typographic hierarchy relies on the high-contrast elegance of **Noto Serif** for all headlines and display text, evoking the masthead of a boutique magazine. This is balanced by **Inter**, a clean and utilitarian sans-serif, to ensure maximum readability for body copy and metadata.

Large "Display" sizes should be used sparingly for hero sections, often overlapping photography. "Label-caps" are utilized for category tags and small navigation elements to provide a structured, architectural feel to the page.

## Layout & Spacing
The design system utilizes a **Fixed 12-Column Grid** for desktop, centered within the viewport. To maintain the luxury editorial feel, extremely wide margins (64px+) are used to frame content.

Spacing rhythm is generous; vertical "Section Gaps" of 128px are used to separate distinct stories or collections, preventing the interface from feeling cluttered. Elements within cards or widgets use a tight 4px or 16px stack to maintain internal cohesion while floating within the larger whitespace of the page.

## Elevation & Depth
Depth in this design system is achieved through **Tonal Layering** and **Low-Contrast Outlines** rather than shadows. To maintain a flat, printed-page aesthetic:
- Surfaces are differentiated by slight shifts in background color (e.g., a Sage-tinted container on a Cream background).
- Borders are consistently thin (1px) using the `neutral_border` color.
- No drop shadows are permitted, ensuring the UI feels grounded and tactile like high-quality stationery.
- Macro photography provides the only true sense of depth through natural bokeh and depth-of-field.

## Shapes
This design system uses **Sharp (0)** roundedness. Every container, button, and image frame features crisp 90-degree angles. This sharp geometry contrasts with the organic, fluid shapes found in the floral photography, reinforcing the curated, "designed" nature of the boutique's offerings.

## Components
- **Minimalist Navigation:** A top-aligned bar with a centered logo and text-only links. Hover states utilize a simple 1px underline in Sage Green.
- **'The Cutting Garden' Cards:** Large-scale image containers with 1px borders. Text is placed either entirely below the image or in a small floating cream box that overlaps the bottom-left corner of the photo.
- **'What's in Bloom' Calendar:** A sophisticated, minimal grid. Current dates are highlighted with a soft Peony Pink or Sage Green circular wash (the only exception to the sharp-corner rule), and "Bloom Events" are marked with thin colored vertical lines corresponding to the floral palette.
- **Buttons:** Ghost-style buttons with 1px Sage Green borders and `label-caps` typography. Solid buttons use a Sage Green fill with Cream text for primary calls to action.
- **Input Fields:** Single-line inputs with no background fill, only a bottom border. Labels float above in a small sans-serif font.
- **Photography Frames:** Always use a 1px border with a 12px internal padding (the "Passé-partout" effect) to treat every image as a gallery piece.