---
name: Heritage Greens
colors:
  surface: '#f6fbf3'
  surface-dim: '#d7dbd4'
  surface-bright: '#f6fbf3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f5ed'
  surface-container: '#ebefe8'
  surface-container-high: '#e5eae2'
  surface-container-highest: '#dfe4dc'
  on-surface: '#181d18'
  on-surface-variant: '#3f4940'
  inverse-surface: '#2d322d'
  inverse-on-surface: '#edf2ea'
  outline: '#6f7a6f'
  outline-variant: '#becabd'
  surface-tint: '#006d3a'
  primary: '#00552c'
  on-primary: '#ffffff'
  primary-container: '#00703c'
  on-primary-container: '#94f0af'
  inverse-primary: '#7eda9a'
  secondary: '#465f88'
  on-secondary: '#ffffff'
  secondary-container: '#b6d0ff'
  on-secondary-container: '#3f5881'
  tertiary: '#812c37'
  on-tertiary: '#ffffff'
  tertiary-container: '#9f434d'
  on-tertiary-container: '#ffd2d3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9af6b5'
  primary-fixed-dim: '#7eda9a'
  on-primary-fixed: '#00210e'
  on-primary-fixed-variant: '#00522a'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#aec7f6'
  on-secondary-fixed: '#001b3d'
  on-secondary-fixed-variant: '#2d476f'
  tertiary-fixed: '#ffdadb'
  tertiary-fixed-dim: '#ffb2b7'
  on-tertiary-fixed: '#40000d'
  on-tertiary-fixed-variant: '#7d2934'
  background: '#f6fbf3'
  on-background: '#181d18'
  surface-variant: '#dfe4dc'
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
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
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
  gutter: 24px
  margin: 64px
  container-max: 1280px
  section-padding: 80px
---

## Brand & Style

The brand personality for this design system is rooted in the "Preppy and Precise" aesthetic—a blend of high-end athletic tradition and modern architectural clarity. It targets an elite demographic that values order, exclusivity, and the quiet luxury of a well-manicured landscape. The UI must feel like a premium clubhouse: welcoming yet strictly structured.

The chosen design style is **Minimalism with a "Clean-Line" architectural focus**. This approach prioritizes structural integrity over decorative flair. By utilizing generous white space and a rigid grid, the design system mirrors the deliberate layout of a championship golf course. The emotional response should be one of calm confidence and absolute precision, ensuring that the property listings and community lifestyle are framed as world-class assets.

## Colors

The palette is anchored by **Emerald Green**, a deep, rich hue that represents the manicured fairways and prestige of the sport. **Navy** serves as the secondary color, providing an authoritative, "Old Guard" contrast that ensures legibility and professional weight.

The background remains a **Crisp White**, acting as the canvas for the "Clean-Line" aesthetic. This high-contrast environment ensures that photography of luxury interiors and lush landscapes remains the focal point. Neutral tones are used sparingly for borders and Dividers to maintain a sense of lightness and openness without sacrificing the grid's definition.

## Typography

This design system employs a classic typographic pairing to balance tradition with modern performance. **Noto Serif** is used for all headlines; its elegant terminals and timeless structure evoke the sophisticated atmosphere of a legacy estate.

For all functional and body text, **Work Sans** provides a "precise and modern" counterpoint. Its neutral, highly-legible forms ensure that technical details—such as lot dimensions and property prices—are communicated with absolute clarity. To reinforce the preppy aesthetic, uppercase labels with increased letter spacing are used for secondary navigation and categories, mimicking the look of traditional club signage.

## Layout & Spacing

The layout philosophy is based on a **fixed 12-column grid** that centers the content, providing a focused and curated viewing experience. This system avoids cluttered, edge-to-edge layouts in favor of expansive margins that allow the high-quality imagery to "breathe."

A strict 8px rhythmic unit governs all padding and margins, ensuring "manicured" alignment across every page. Components are spaced with significant vertical gaps to prevent a crowded feel, emphasizing that in luxury real estate, space is the ultimate premium. Grid gutters are kept relatively wide (24px) to maintain distinct visual separation between content blocks and property cards.

## Elevation & Depth

To maintain the "Clean-Line" architecture, this design system avoids heavy shadows and traditional skeuomorphism. Instead, depth is conveyed through **Low-Contrast Outlines** and **Tonal Layers**.

Surfaces are predominantly flat, with hierarchy established by 1px borders in Navy or light Neutral shades. When depth is required—such as for a primary call-to-action or a featured property card—a very subtle, high-diffusion "ambient" shadow may be used, but the primary method of separation remains the rigid grid and color blocking. This keeps the interface looking sharp, crisp, and architectural.

## Shapes

The shape language is defined by **sharp, precise geometry**. To avoid an overly clinical or "harsh" feel, a very subtle rounding of `0.25rem` (Soft) is applied to primary UI elements. This keeps the corners looking "sharp" at a glance while providing a refined finish that feels intentional rather than raw.

Buttons, input fields, and image containers should all adhere to this consistent corner radius. Circular elements are reserved strictly for status indicators or small icon badges, ensuring the dominant visual motif remains one of straight lines and rectangular precision.

## Components

### Buttons
Primary buttons are solid Emerald Green with white text, featuring sharp (0.25rem) corners and no gradients. Secondary buttons use a Navy 1px outline with centered text, emphasizing the "Clean-Line" aesthetic.

### Input Fields
Forms should be minimalist, using a simple bottom-border (1px Navy) or a full thin-stroke outline. Labels are always positioned above the field in the "label-caps" typographic style for a professional, form-like appearance.

### Cards
Property cards are white with a 1px border. They feature a top-aligned image with no internal padding, allowing the "manicured fairway" photography to meet the border of the component. Text details inside cards should be aligned to a strict internal 24px padding.

### Chips & Tags
Used for "Featured" or "New Listing" badges. These should be rectangular with the system-standard 0.25rem rounding, utilizing the Navy or Emerald palette with high-contrast white text.

### Additional Components
*   **Property Detail Grid:** A specific component for displaying square-footage, bedroom count, and bath count using thin-line icons and precise Work Sans typography.
*   **Interactive Map:** A custom-styled map interface with a limited palette (Emerald and Navy) to maintain brand consistency during property searches.