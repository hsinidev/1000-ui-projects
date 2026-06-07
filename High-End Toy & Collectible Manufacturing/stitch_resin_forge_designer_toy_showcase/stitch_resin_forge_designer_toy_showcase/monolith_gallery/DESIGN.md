---
name: Monolith Gallery
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#4c4546'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-xl:
    fontFamily: Epilogue
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  gallery-margin: 80px
  gutter: 32px
  section-gap: 160px
  element-gap: 24px
---

## Brand & Style
The brand personality is that of an elite, quiet observer—authoritative yet restrained. It targets high-end collectors who view designer toys as fine art rather than playthings. The emotional response is one of reverence, evoking the hushed, expansive atmosphere of a modern art gallery.

The design style is **Minimalism** with a heavy emphasis on **High-Contrast**. The UI is secondary to the "exhibit" (the product photography). Surfaces are matte and non-reflective, avoiding any gloss or trendy gradients to ensure a timeless, architectural feel. Layouts are intentionally sparse, using negative space as a luxury commodity to frame content.

## Colors
The palette is restricted to a triad of Stark White, Matte Black, and Slate. 

- **Primary (Matte Black):** Used for typography, structural borders, and primary calls to action. It should feel dense and heavy.
- **Secondary (Slate):** Employed for secondary UI elements, meta-data, and subtle dividers to prevent the interface from feeling too "flat."
- **Tertiary (Stark White):** The base of the canvas. It provides the "void" that allows product photography to breathe.
- **Background (Off-White):** A very slight neutral tint is used for background sections to distinguish the pure white of a product "pedestal" (card) from the gallery floor.

Photography should be treated with high-contrast, moody lighting and desaturated environments to align with this palette.

## Typography
This design system utilizes a dual-font strategy to balance architectural impact with functional clarity.

- **Headlines:** Epilogue is chosen for its geometric, bold, and editorial presence. Large display sizes should use tight tracking to feel like structural elements.
- **UI & Body:** Inter provides a neutral, grotesque foundation that stays out of the way of the artwork. It ensures maximum legibility for specifications, prices, and shipping details.
- **Labels:** Small labels and "tags" should always be uppercase with generous letter spacing to mimic museum plaque formatting.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy with extreme margins to create a "frame" around the content.

- **The Gallery Frame:** A minimum 80px outer margin is maintained on all desktop views to ensure the content never feels crowded by the browser edge.
- **Vertical Rhythm:** A massive 160px gap is used between major sections to force a slow, deliberate scrolling pace.
- **The Pedestal Grid:** Content is organized on a 12-column grid. Product cards should often span 4 or 6 columns to maintain a sense of scale and importance.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and **Bold Borders** rather than shadows. This maintains the "Matte" aesthetic.

- **Surfaces:** Products are placed on Stark White (#FFFFFF) containers over a subtle Off-White (#F8FAFC) background, creating a "pedestal" effect.
- **Lines:** 1px solid Matte Black borders are used to define boundaries. These should be used sparingly to frame images or separate navigation.
- **Interaction:** Depth is signaled by inversion. A white button becomes solid black on hover; a black element may shift to Slate. Avoid all drop shadows to keep the UI feeling "flush" and architectural.

## Shapes
The design system utilizes **Sharp (0px)** corners exclusively. This reinforces the architectural, "forged" nature of the products. Any rounding would soften the elite, high-contrast aesthetic and is strictly prohibited. Every button, input field, and image container must maintain a crisp 90-degree angle.

## Components
- **Buttons:** Primary buttons are solid Matte Black with White text, rectangular, and oversized. Secondary buttons are "Ghost" style with a 1px Black border.
- **Input Fields:** Minimalist 1px bottom-border only. Labels use the `label-caps` typography style, positioned above the field. 
- **Product Cards:** No borders or shadows. The image should be full-bleed to the edges of the card container, using a light slate background for the "studio" shot of the statue.
- **Chips/Status:** Rectangular blocks of Slate with White text. No rounded corners.
- **Interactive Exhibit (Custom Component):** A full-screen horizontal scroll component for high-resolution close-ups of statue textures, featuring a progress bar at the bottom consisting of a single 1px line.
- **The Pedestal (Custom Component):** A specialized layout block for product specs (material, weight, edition size) that uses a two-column definition list with architectural spacing.