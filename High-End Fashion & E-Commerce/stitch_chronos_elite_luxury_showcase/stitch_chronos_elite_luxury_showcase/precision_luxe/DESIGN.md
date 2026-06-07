---
name: Precision-Luxe
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#bfc2ff'
  on-secondary: '#181d8c'
  secondary-container: '#3239a3'
  on-secondary-container: '#a9afff'
  tertiary: '#c0d1dd'
  on-tertiary: '#23323c'
  tertiary-container: '#a5b5c1'
  on-tertiary-container: '#384751'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#d5e5f1'
  tertiary-fixed-dim: '#b9c9d5'
  on-tertiary-fixed: '#0e1d26'
  on-tertiary-fixed-variant: '#3a4953'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  h1:
    fontFamily: notoSerif
    fontSize: 4.5rem
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: notoSerif
    fontSize: 3rem
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: notoSerif
    fontSize: 2rem
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: manrope
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: manrope
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1440px
  gutter: 2rem
  margin: 4rem
  unit: 8px
  section-gap: 8rem
---

## Brand & Style

This design system is engineered for the high-end horology market, targeting affluent collectors and enthusiasts. The brand personality is authoritative yet understated, reflecting the "Precision-Luxe" aesthetic where mechanical mastery meets timeless elegance. The UI should evoke an emotional response of exclusivity, calm, and meticulous craftsmanship.

The visual style merges **Minimalism** with **Glassmorphism**. High-contrast photography of watch movements and dial textures serves as the primary visual driver, while the interface acts as a sophisticated lens. Generous whitespace is used strategically to signal luxury, ensuring the user never feels rushed or overwhelmed. The interface relies on translucent layers and subtle reflections to mimic the sapphire crystal of a luxury timepiece.

## Colors

The palette is anchored in a dark, nocturnal environment to allow the metallic and gemstone details of the watches to shine. 

- **Primary (Champagne Gold):** Reserved for accentuation, highlights, and primary calls to action. It represents the value and prestige of the collection.
- **Secondary (Deep Navy):** Used for deep backgrounds and subtle gradients, providing a more regal alternative to pure black.
- **Tertiary (Charcoal):** Utilized for structural elements, secondary backgrounds, and text variations.
- **Neutral (Off-White/Silver):** Used for body text and iconography to ensure high legibility against the dark backgrounds.

## Typography

The typographic hierarchy balances heritage and modernity. **notoSerif** (replacing Playfair Display) provides the editorial authority expected in luxury commerce, used primarily for headlines and evocative quotes. **manrope** (replacing Montserrat) offers a more refined, contemporary sans-serif experience for technical specifications and body copy. 

Key interactions use uppercase labels with increased letter-spacing to mimic the engravings found on watch case backs. Line heights are kept generous to maintain the "airy" feel of the layout.

## Layout & Spacing

This design system utilizes a **fixed grid** approach for large displays to maintain a curated, gallery-like feel. A 12-column grid is employed with significant margins (64px+) to create a frame around the content. 

The spacing rhythm is intentional and expansive. Components are separated by large gaps to prevent visual clutter. "The Golden Ratio" should guide the relationship between imagery and text blocks, ensuring that photography always has "room to breathe."

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces appear as semi-transparent panes of polished glass.

- **Surface Tiers:** Backgrounds are Deep Navy; cards use a semi-transparent Charcoal fill (40-60% opacity) with a `backdrop-filter: blur(20px)`.
- **Borders:** "Micro-borders" are used to define edges. These are 1px solid strokes with a low-opacity Gold or Silver tint, simulating the light catch on a chamfered edge.
- **Interactions:** Hover states should increase the backdrop blur and slightly brighten the border intensity, rather than lifting the element with a shadow.

## Shapes

The shape language is "Soft" (0.25rem to 0.75rem), mirroring the subtle curves of a watch lugs and crystals. Sharp corners are avoided to prevent the UI from feeling aggressive, while overly rounded "pill" shapes are avoided to maintain a serious, architectural tone. Decorative elements may use circular geometry to reference watch dials and gears.

## Components

- **Buttons:** Primary buttons feature a solid Champagne Gold background with Deep Navy text. Secondary buttons are "ghost" style with a 1px Gold border and glassmorphism background.
- **Glass Cards:** Used for product listings and specs. Must include a subtle inner glow on the top-left edge to simulate a light source.
- **High-Resolution Galleries:** Immersive, full-bleed images with minimal UI overlays. Navigation should be "invisible," appearing only on interaction.
- **Interactive Specs:** A grid-based component using `label-caps` for headers and `body-md` for technical data, separated by hairline horizontal rules.
- **Refined Multi-step Forms:** Progress is indicated by a minimalist thin gold line. Input fields use a "bottom-border-only" style when inactive, transitioning to a full glassmorphism focus state.
- **Horology Chips:** Small, semi-transparent badges used for "Complications" (e.g., Tourbillon, Chronograph) with monochromatic iconography.