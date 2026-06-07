---
name: Zen & Organic Minimalist
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#181919'
  on-primary: '#ffffff'
  primary-container: '#2d2d2d'
  on-primary-container: '#959494'
  inverse-primary: '#c8c6c6'
  secondary: '#665e4b'
  on-secondary: '#ffffff'
  secondary-container: '#ebdec6'
  on-secondary-container: '#6a624f'
  tertiary: '#171917'
  on-tertiary: '#ffffff'
  tertiary-container: '#2c2d2b'
  on-tertiary-container: '#949492'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4e2e1'
  primary-fixed-dim: '#c8c6c6'
  on-primary-fixed: '#1b1c1c'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#ede1c9'
  secondary-fixed-dim: '#d1c5ae'
  on-secondary-fixed: '#211b0c'
  on-secondary-fixed-variant: '#4d4634'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c4'
  on-tertiary-fixed: '#1a1c1a'
  on-tertiary-fixed-variant: '#464745'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  headline-display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 120px
---

## Brand & Style
The design system embodies the intersection of Scandinavian functionality and Japanese rustic minimalism (Japandi). It is crafted for a discerning audience that values slow living, intentionality, and craftsmanship. The visual narrative centers on tranquility and "Ma" (the celebration of empty space), evoking an emotional response of calm, clarity, and premium understated luxury. 

The aesthetic is strictly **Minimalist**, utilizing heavy whitespace to allow high-quality furniture photography to breathe. It avoids all unnecessary ornamentation, relying instead on precise typography and organic depth to guide the user through a curated boutique experience.

## Colors
The palette is rooted in natural, earthy materials. **Linen White** (#F9F8F5) serves as the expansive canvas for all backgrounds, ensuring a warm, lived-in feel compared to clinical whites. **Pale Oak** (#E8DCC4) is used for subtle accents, secondary surfaces, and hover states to mimic light wood textures. **Charcoal** (#2D2D2D) provides the necessary grounding, used primarily for typography, iconography, and high-contrast borders to ensure legibility and a sense of architectural structure.

## Typography
This design system utilizes **Inter** for its systematic clarity and modern neutrality. To achieve the "sophisticated" boutique aesthetic, weights are kept strictly between 300 (Light) and 400 (Regular). Generous letter spacing is applied to all headings and labels to create an airy, editorial feel. Headers should be typography-led, often acting as the primary hero element alongside large imagery.

## Layout & Spacing
The layout follows a **Fixed Grid** model centered within the viewport. To maintain the Zen aesthetic, the "section-gap" is intentionally large (120px+), forcing a slow, deliberate scrolling pace. Use a 12-column grid for desktop with wide gutters (32px) to prevent visual clutter. Vertical imagery should often break the grid or span multiple rows to create an asymmetrical, organic flow reminiscent of a high-end interior design lookbook.

## Elevation & Depth
Depth is conveyed through **soft organic shadows** and **tonal layering** rather than traditional elevation.
- **Shadows:** Use extremely diffused, low-opacity shadows (e.g., `box-shadow: 0 10px 40px rgba(45, 45, 45, 0.04)`) to make cards feel like they are resting gently on a surface.
- **Dividers:** Use ultra-thin 0.5px lines in Charcoal at 15% opacity to separate content sections without creating hard visual breaks.
- **Tonal Layers:** Pale Oak surfaces can be used to distinguish secondary information areas from the main Linen White background.

## Shapes
The shape language is primarily **Sharp (0px)** to reflect the clean lines of Scandi furniture and architectural precision. However, when displaying photography of "organic" furniture pieces, the containers remain sharp while the subject matter provides the curves. This contrast between the rigid UI frame and the soft product forms is central to the design system.

## Components
- **Buttons:** Ghost-style buttons with 0.5px or 1px Charcoal borders. Text is always uppercase `label-sm` with high letter spacing. Hover states involve a subtle transition to a Pale Oak background fill.
- **Navigation:** Minimalist text-only links. No icons unless strictly necessary. The active state is indicated by a simple 0.5px underline.
- **Input Fields:** Bottom-border only (0.5px Charcoal). Labels float above the line in `label-sm`.
- **Cards:** Borderless with the "soft organic shadow" mentioned in Elevation. The focus is entirely on the large-scale vertical imagery.
- **Chips:** Small, sharp-edged rectangles with a Pale Oak background and Charcoal text.
- **Additional Components:** "Product Stories" (large-scale vertical image sliders) and "Material Swatch Pickers" (small circular or square previews of wood and fabric grains).