---
name: Terra-Firm
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353536'
  on-surface: '#e4e2e3'
  on-surface-variant: '#c7c6ca'
  inverse-surface: '#e4e2e3'
  inverse-on-surface: '#303031'
  outline: '#909094'
  outline-variant: '#46474a'
  surface-tint: '#c8c6c7'
  primary: '#c8c6c7'
  on-primary: '#303031'
  primary-container: '#1a1a1b'
  on-primary-container: '#848283'
  inverse-primary: '#5f5e5f'
  secondary: '#ccc6b9'
  on-secondary: '#333027'
  secondary-container: '#4d493f'
  on-secondary-container: '#beb8ab'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#191b1b'
  on-tertiary-container: '#828383'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e3'
  primary-fixed-dim: '#c8c6c7'
  on-primary-fixed: '#1b1b1c'
  on-primary-fixed-variant: '#474647'
  secondary-fixed: '#e9e2d4'
  secondary-fixed-dim: '#ccc6b9'
  on-secondary-fixed: '#1e1b13'
  on-secondary-fixed-variant: '#4a463d'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131314'
  on-background: '#e4e2e3'
  surface-variant: '#353536'
typography:
  h1:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: EB Garamond
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.08em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

This design system is defined by architectural precision and engineering-grade clarity. It targets a sophisticated audience that values structural integrity, high-end materials, and technical transparency. The aesthetic is a fusion of **Structural Minimalism** and **Technical Glassmorphism**, evoking the feeling of an architect’s blueprint or a precision-machined instrument. 

The emotional response should be one of absolute reliability and understated luxury. Every element is intentionally placed, adhering to a rigorous mathematical order while maintaining an air of lightness through translucent layers. The UI is not just an interface; it is a digital manifestation of "terra firma"—solid ground.

## Colors

The palette is derived from natural, high-performance building materials: Graphite, Pale Oak, and White. 

- **Graphite (#1A1A1B):** The foundational base. Used for backgrounds and primary containers to create a sense of depth and density.
- **Pale Oak (#D9D2C5):** The humanizing element. Used for highlights, active states, and secondary accents to provide a warm, organic contrast against the cold technicality of graphite.
- **White (#FFFFFF):** The source of clarity. Reserved for high-priority typography, iconography, and critical UI strokes.

The default color mode is dark, maximizing the "engineering-grade" feel and allowing the glassmorphism effects to shine. High-contrast ratios are strictly maintained to ensure professional-level legibility.

## Typography

This design system utilizes a high-contrast typographic pairing to distinguish between narrative authority and technical precision.

- **Headings (EB Garamond):** An elegant, literary serif that provides a sense of history and premium craft. Used for page titles and section headers. It should be typeset with tight tracking to maintain a modern, editorial look.
- **Data & UI (Geist):** A sharp, mono-inspired sans-serif that embodies engineering and developer-centric toolsets. Used for all functional UI components, data visualizations, and body copy.
- **Technical Labels:** All labels and data-heavy strings should utilize the `data-mono` style to emphasize the architectural nature of the content.

## Layout & Spacing

The layout philosophy is built on a **Strict Fixed Grid**. Every element must align to a 4px baseline grid to ensure mathematical consistency.

- **Mobile (Base):** A 4-column grid with 16px gutters and 20px side margins. Elements should stack vertically, prioritizing data density and readability.
- **Desktop:** A 12-column grid with a maximum width of 1440px. The grid should be visible through subtle 0.5px Graphite-light lines in technical views to emphasize the "engineering" aesthetic.
- **Spacing Rhythm:** Use the 8px increment rule (8, 16, 24, 40, 64) for all padding and margins to maintain a predictable visual cadence.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Structural Layering**. Depth is communicated through translucency and stroke:

1.  **Backdrop Blurs:** Overlays and modal components use a high-density backdrop blur (20px+) with a 40% opacity White or Pale Oak fill.
2.  **Ghost Outlines:** Instead of shadows, use 1px or 0.5px solid strokes. Top-level surfaces should use White at 15% opacity; active components use Pale Oak at 100% opacity.
3.  **Tonal Stacking:** Surfaces deeper in the hierarchy use the base Graphite (#1A1A1B), while elevated surfaces use a slightly lighter Graphite tint (#2A2A2B) to create a subtle "stepped" effect.

## Shapes

The shape language is **Zero-Radius (Sharp)**. To reflect architectural blueprints and engineering precision, all buttons, containers, and input fields must have 0px corner radii. 

The only exception to this rule is for iconography or circular status indicators. The sharp edges reinforce the brand’s commitment to discipline and structural rigidity.

## Components

- **Buttons:** Sharp-edged, high-contrast blocks. Primary buttons use Pale Oak with Graphite text. Secondary buttons are transparent with a 1px White stroke.
- **Inputs:** Minimalist fields using only a bottom border (1px White) and a technical label above. On focus, the border transitions to Pale Oak.
- **Cards:** Use the Tonal Stacking method. No shadows. A 0.5px Graphite-light border is required for definition.
- **Technical Diagrams:** Use thin, 1px White or Pale Oak lines. Data points should be represented by small square markers, never circles.
- **Chips/Status:** Small, sharp rectangles with `label-sm` typography. Status is indicated by the fill color of the text, rather than a background bubble.
- **Navigation:** A strict vertical or horizontal rail with monospaced labels. Active states are marked by a 2px Pale Oak line directly adjacent to the menu item.