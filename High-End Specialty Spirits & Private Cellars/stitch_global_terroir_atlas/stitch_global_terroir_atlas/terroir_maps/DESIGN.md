---
name: Terroir-Maps
colors:
  surface: '#fcf9f0'
  surface-dim: '#dddad1'
  surface-bright: '#fcf9f0'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ea'
  surface-container: '#f1eee5'
  surface-container-high: '#ebe8df'
  surface-container-highest: '#e5e2da'
  on-surface: '#1c1c17'
  on-surface-variant: '#46483d'
  inverse-surface: '#31312b'
  inverse-on-surface: '#f4f1e8'
  outline: '#77786c'
  outline-variant: '#c7c7b9'
  surface-tint: '#5b6239'
  primary: '#272e0a'
  on-primary: '#ffffff'
  primary-container: '#3d441e'
  on-primary-container: '#a9b181'
  inverse-primary: '#c3cb99'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#39270f'
  on-tertiary: '#ffffff'
  tertiary-container: '#513d23'
  on-tertiary-container: '#c5a887'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dfe7b3'
  primary-fixed-dim: '#c3cb99'
  on-primary-fixed: '#181e00'
  on-primary-fixed-variant: '#434a23'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#fdddb9'
  tertiary-fixed-dim: '#e0c29f'
  on-tertiary-fixed: '#281803'
  on-tertiary-fixed-variant: '#584329'
  background: '#fcf9f0'
  on-background: '#1c1c17'
  surface-variant: '#e5e2da'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  data-tabular:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The design system centers on a "Modern Organic" aesthetic, blending the precision of cartography with the warmth of the natural world. It targets oenophiles and researchers who value both data accuracy and the tactile heritage of winemaking.

The style is characterized by **Tactile Minimalism**. It avoids the sterile coldness of typical SaaS platforms by using subtle paper-like grain textures and soft, layered depth. The interface should feel like a premium, digital field guide—authoritative yet inviting. Key visual drivers include organic curvature, map-inspired linework, and a "low-ink" digital footprint that prioritizes readability over flashy effects.

## Colors
The palette is grounded in the "Sand" neutral, used for large surface areas to mimic high-quality heavy-stock paper. **Olive Green** serves as the primary action color, representing growth and the vineyard landscape; it should be used for primary buttons, active states, and branding elements. 

**Slate** provides the structural contrast, used for all primary typography and complex data visualizations (such as soil composition charts or elevation lines). A tertiary **Earth Brown** is reserved for highlights or specific map markers. Color usage should remain restrained, letting the content and the cartographic data provide the visual richness.

## Typography
This design system employs a sophisticated typographic pairing to balance heritage with utility. **Libre Caslon Text** is used for headings to evoke the "atlas" feel—it is high-contrast, elegant, and scholarly. 

**Work Sans** is used for all body copy and data-heavy components. Its neutral, grotesque construction ensures that complex vineyard data remains legible even at small sizes. For data visualizations and wine statistics, use the `data-tabular` style to ensure vertical alignment of numbers. All labels should use the `label-caps` style with increased letter spacing to provide a clear hierarchy against body text.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop to maintain the feel of a curated book or map, while transitioning to a fluid model for mobile. 

A 12-column grid is used for desktop (1280px max-width) with wide 24px gutters to allow the earthy background to breathe. Vertical rhythm is strictly enforced using 8px increments. Content should be grouped in "plates" or "leafs"—contained areas that use the `stack` variables to separate sections of data. Maps should either be fully contained within a card or "bleed" to the edges of the viewport to create an immersive experience.

## Elevation & Depth
Elevation is achieved through **Tonal Layers** and **Ambient Shadows**. Instead of harsh black shadows, this design system uses soft, diffused shadows tinted with Olive or Slate (e.g., `rgba(61, 68, 30, 0.08)`).

1.  **Base (Level 0):** The Sand background with a subtle paper texture.
2.  **Raised (Level 1):** Cards and surfaces using a slightly lighter Sand shade with a 4px blur shadow. This is for standard content modules.
3.  **Floating (Level 2):** Critical UI elements like navigation bars or map tooltips, featuring an 8px blur shadow and a 1px solid border in `sand-300` for definition.

Avoid heavy blurs; the goal is to make elements look like they are resting on the paper, not hovering far above it.

## Shapes
Shapes in the design system are **Rounded**, reflecting organic forms found in nature—grapes, hillsides, and riverbeds. 

Standard components like buttons and input fields use a 0.5rem radius. Larger containers, such as feature cards or map overlays, use 1rem (`rounded-lg`) or 1.5rem (`rounded-xl`). High-priority callouts may occasionally use asymmetrical rounding (e.g., top-left and bottom-right only) to mimic the irregular shapes of topographic map legends.

## Components
-   **Buttons:** Primary buttons use a solid `olive-600` fill with white text. Secondary buttons use a `slate-600` outline with a subtle `sand-300` hover state. All buttons should have a slightly increased horizontal padding for a premium feel.
-   **Chips:** Use for grape varieties or soil types. These should be pill-shaped with a `sand-300` background and `slate-900` text.
-   **Input Fields:** Borders should be `slate-400` with a 1px width. Upon focus, the border transitions to `olive-600` and the background shifts slightly to a brighter cream.
-   **Cards:** Use `sand-100` for the background. Incorporate a 1px `sand-300` border. Cards should often feature a subtle "topographic line" vector pattern in the background (at 5% opacity) to reinforce the atlas theme.
-   **Data Visualization:** Use `slate` for axes and primary data, with `olive` and `earth brown` for categorical differentiation. Avoid neon or overly bright "digital" colors.
-   **Map Markers:** Custom SVG pins that resemble traditional surveyor marks or stylized grape clusters.