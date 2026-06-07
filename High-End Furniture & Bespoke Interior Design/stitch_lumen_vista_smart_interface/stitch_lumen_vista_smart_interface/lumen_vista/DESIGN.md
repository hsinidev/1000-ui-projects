---
name: Lumen-Vista
colors:
  surface: '#091421'
  surface-dim: '#091421'
  surface-bright: '#303a48'
  surface-container-lowest: '#050f1c'
  surface-container-low: '#121c2a'
  surface-container: '#16202e'
  surface-container-high: '#212b39'
  surface-container-highest: '#2b3544'
  on-surface: '#d9e3f6'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#d9e3f6'
  inverse-on-surface: '#27313f'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c3c6d7'
  on-secondary: '#2c303d'
  secondary-container: '#454957'
  on-secondary-container: '#b5b8c9'
  tertiary: '#cccfd2'
  on-tertiary: '#2d3134'
  tertiary-container: '#b1b3b7'
  on-tertiary-container: '#424549'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#dfe2f3'
  secondary-fixed-dim: '#c3c6d7'
  on-secondary-fixed: '#171b28'
  on-secondary-fixed-variant: '#434654'
  tertiary-fixed: '#e0e2e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1f'
  on-tertiary-fixed-variant: '#44474a'
  background: '#091421'
  on-background: '#d9e3f6'
  surface-variant: '#2b3544'
typography:
  display-lg:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Metropolis
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
  title-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
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
  margin-mobile: 20px
  margin-desktop: 64px
  max-width: 1440px
---

## Brand & Style

This design system targets an ultra-high-end demographic, focusing on the intersection of architectural glass technology and luxury lighting environments. The brand personality is cinematic and atmospheric, evoking the feeling of a high-tech observatory or a premium lounge at twilight.

The visual style is **Advanced Glassmorphism**. It relies on depth through translucency, utilizing multi-layered frosted surfaces that simulate thick architectural glass. The interface should feel like it is floating within the physical space, using subtle blurs and light-refracting borders to maintain a sense of lightness despite the deep, immersive color palette. Every interaction is designed to feel deliberate, quiet, and sophisticated.

## Colors

The palette is anchored in a cinematic dark mode. 

*   **Primary (Champagne Gold):** Reserved for high-intent interactive elements, active states, and focus indicators. It should be used sparingly to represent light and heat.
*   **Secondary (Deep Indigo):** The foundation of the interface. This color serves as the "infinite" backdrop, providing deep contrast for the glass layers.
*   **Tertiary (Soft Silver):** Used for primary text and iconography to ensure legibility without the harshness of pure white.
*   **Surface Layers:** Glass layers use a semi-transparent variation of the background color with high-diffusion backdrop blurs.

## Typography

The typographic scale emphasizes clarity and modern architectural precision. **Metropolis** is used for display and headline roles to provide a geometric, structured feel that echoes high-end drafting. **Inter** is utilized for body and UI labels for its exceptional legibility on translucent backgrounds.

To maintain the "luxury" feel, use generous tracking on uppercase labels and maintain light font weights for larger display text. Avoid heavy bolding; instead, use Champagne Gold to signify importance or hierarchy.

## Layout & Spacing

This design system employs a **fluid grid** with substantial safe areas to evoke a sense of "gallery" space. 

*   **Desktop:** A 12-column grid with wide 64px margins. Components should be grouped into clusters to avoid "filling" the screen, allowing the deep indigo background to breathe.
*   **Mobile:** A 4-column grid with 20px margins. Cards should span the full width to maximize the frosted glass surface area.
*   **Rhythm:** An 8px linear scale governs all padding and margins. Vertical rhythm should be loose and expansive to prevent the UI from feeling cluttered.

## Elevation & Depth

Depth is not communicated through shadows, but through **translucency and blur**. 

1.  **Base Layer:** The Deep Indigo solid background.
2.  **Surface Layer (Cards/Panels):** 40% opacity Indigo with a 20px - 40px backdrop blur. Borders are 1px solid at 15% Silver.
3.  **Interactive Layer (Hover/Active):** Surfaces receive a "inner glow" or a 1px Champagne Gold border at 50% opacity.
4.  **Floating Elements (Tooltips/Popovers):** Highest blur (60px) with a subtle drop shadow that is tinted Deep Indigo (0.6 opacity) to simulate physical presence on the glass.

Glow effects are used strategically: interactive elements like toggles should emit a soft radial gradient of Champagne Gold when active.

## Shapes

The shape language is sophisticated and "soft-geometric." 

Standard components use a **16px (1rem)** corner radius to feel approachable and modern. Larger control cards use **24px (1.5rem)** to emphasize their status as primary containers. Buttons and interactive chips use a fully rounded **pill-shape** to distinguish them from structural glass panels. Circular elements are used exclusively for dials and high-level status indicators.

## Components

*   **Translucent Control Cards:** These are the primary containers. They feature a subtle top-to-bottom linear gradient (lighter at the top to simulate overhead lighting hitting the glass) and a 1px frosted border.
*   **Glowing Toggles:** The track should be a dark, recessed glass. The handle, when active, becomes a solid Champagne Gold orb with a soft outer glow.
*   **Circular Dials:** Used for brightness and glass opacity controls. The track is a fine silver line; the indicator is a Champagne Gold "spark" that travels the perimeter.
*   **Buttons:** Secondary buttons are ghost-style with silver text. Primary buttons are Champagne Gold with dark indigo text, using a subtle inner glow to feel "lit" from within.
*   **Input Fields:** Underlined or minimally bordered glass containers. The cursor and focus state must use the Champagne Gold accent.
*   **Status Indicators:** Small, pulsing circular "pips" that represent active glass tinting or light zones.