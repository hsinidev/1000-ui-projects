---
name: Cellar-Chic Educational Platform
colors:
  surface: '#191211'
  surface-dim: '#191211'
  surface-bright: '#403736'
  surface-container-lowest: '#130c0c'
  surface-container-low: '#221a19'
  surface-container: '#261e1d'
  surface-container-high: '#312827'
  surface-container-highest: '#3c3332'
  on-surface: '#efdfdd'
  on-surface-variant: '#dac1bf'
  inverse-surface: '#efdfdd'
  inverse-on-surface: '#372e2d'
  outline: '#a28c8a'
  outline-variant: '#544341'
  surface-tint: '#ffb3ad'
  primary: '#ffb3ad'
  on-primary: '#5a1a19'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#954742'
  secondary: '#b9c9d3'
  on-secondary: '#23323a'
  secondary-container: '#3c4b53'
  on-secondary-container: '#abbbc5'
  tertiary: '#abc9ee'
  on-tertiary: '#113250'
  tertiary-container: '#002643'
  on-tertiary-container: '#708eb0'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#d5e5ef'
  secondary-fixed-dim: '#b9c9d3'
  on-secondary-fixed: '#0e1d25'
  on-secondary-fixed-variant: '#3a4951'
  tertiary-fixed: '#d0e4ff'
  tertiary-fixed-dim: '#abc9ee'
  on-tertiary-fixed: '#001d35'
  on-tertiary-fixed-variant: '#2a4968'
  background: '#191211'
  on-background: '#efdfdd'
  surface-variant: '#3c3332'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Noto Serif
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

The design system embodies a "Cellar-Chic" aesthetic, blending the traditional gravitas of an underground wine cellar with modern editorial precision. The brand personality is scholarly yet accessible, targeting connoisseurs and aspiring professionals who value heritage and artisanal quality. 

The visual style is **Minimalist-Tactile**. It utilizes heavy whitespace to create a sense of premium luxury, punctuated by subtle textures like aged vellum and cold slate. The emotional response should be one of quiet confidence, intellectual curiosity, and sensory richness. The UI avoids flashy animations in favor of smooth, deliberate transitions that mirror the pouring of a vintage wine.

## Colors

This design system utilizes a dark-mode-first approach to simulate the dim, atmospheric lighting of a private cellar. 

- **Primary (Deep Burgundy):** Used for brand moments, primary calls to action, and highlighting active educational modules.
- **Secondary (Slate):** Used for structural depth, secondary containers, and backgrounds where burgundy would be too heavy.
- **Accent (Gold):** Reserved for "premium" signals—achievements, sommelier-level content, and thin decorative trims.
- **Neutral/Base:** The background is a near-black charcoal to ensure the burgundy and gold pop. Text is off-white (#F5F5F0) to reduce eye strain and mimic the color of high-quality book paper.

## Typography

The typography strategy relies on high-contrast pairings to balance tradition with modernity.

- **Headlines:** Uses **Noto Serif** for an authoritative, literary feel. Large display sizes should use tighter letter spacing to feel like a premium editorial masthead.
- **Body & Interface:** Uses **Manrope** for its clean, balanced geometry. It provides the necessary functional clarity for educational reading without distracting from the serif accents.
- **Micro-copy:** Small labels and "Eyebrow" headers should be set in uppercase Manrope with increased letter spacing to denote categorization and hierarchy.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to maintain the feel of a structured textbook or luxury catalog. Elements are arranged on a 12-column grid with generous 64px outer margins to provide "breathing room."

Spacing follows an 8px rhythmic scale. However, for content-heavy educational sections, vertical rhythm is expanded to prevent the UI from feeling cramped. White space is treated as a design element itself, used to separate distinct "tasting notes" or chapters.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. 

1. **Base Layer:** The darkest neutral, representing the "floor" of the cellar.
2. **Surface Layer:** Slate (#2F3E46) or a slightly lighter charcoal, used for cards and modules.
3. **Interactive Layer:** Elements that sit "above" the surface use a very subtle 1px border in Gold or a semi-transparent white.
4. **Shadows:** When used, shadows are "Ambient"—extremely soft, elongated, and tinted with the Slate color to avoid looking "dirty" on the dark background.

## Shapes

The shape language is **Soft (0.25rem)**. This design system avoids fully sharp corners to remain approachable, but rejects overly rounded or pill-shaped elements to maintain a sophisticated, architectural silhouette. 

Buttons and input fields use the 4px (0.25rem) radius. Large image containers or cards may use the `rounded-lg` (8px) setting to provide a gentle frame for high-quality photography.

## Components

- **Buttons:** Primary buttons are solid Deep Burgundy with a 1px Gold internal border. Secondary buttons are "Ghost" style with a thin Slate border that transitions to Gold on hover.
- **Input Fields:** Dark backgrounds with a 1px Slate border. On focus, the border glows subtly in Gold.
- **Cards:** Use a "Slate" surface. Featured cards for premium courses include a Gold-trimmed top edge (2px).
- **Progress Indicators:** Educational tracks use a thin Gold line to indicate completion, contrasting against a Slate track.
- **Chips/Tags:** Small, rectangular chips with 0px roundedness and high-letter-spacing uppercase text, used for wine regions or flavor profiles.
- **Specialty Component - The "Tasting Note":** A unique component style that uses an "Aged Paper" subtle texture background with Noto Serif typography, styled to look like a physical card resting on a slate table.