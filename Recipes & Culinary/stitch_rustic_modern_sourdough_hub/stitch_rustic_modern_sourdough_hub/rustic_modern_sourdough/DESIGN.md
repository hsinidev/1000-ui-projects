---
name: Rustic Modern Sourdough
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4c463c'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#7d766a'
  outline-variant: '#cfc5b8'
  surface-tint: '#6d5c3a'
  primary: '#6d5c3a'
  on-primary: '#ffffff'
  primary-container: '#f5deb3'
  on-primary-container: '#72613f'
  inverse-primary: '#dac49b'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#6c5d3b'
  on-tertiary: '#ffffff'
  tertiary-container: '#f4deb4'
  on-tertiary-container: '#71613f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f7e0b5'
  primary-fixed-dim: '#dac49b'
  on-primary-fixed: '#251a01'
  on-primary-fixed-variant: '#544525'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#f6e0b5'
  tertiary-fixed-dim: '#d9c49b'
  on-tertiary-fixed: '#241a01'
  on-tertiary-fixed-variant: '#534526'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
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
  label-lg:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-md:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is rooted in the intersection of heritage craft and modern culinary precision. It targets a discerning audience that values transparency, slow fermentation, and the tactile nature of baking. The aesthetic identity is **Rustic-Minimalism** with **Tactile** accents—stripping away digital clutter to focus on the raw materials of the product.

Visuals should evoke the sensory experience of a bakery at dawn: the smell of toasted grain, the texture of a floured banneton, and the heat of a stone hearth. This is achieved through a grounded color palette and high-quality photography that highlights crumb structure and crust crystallization. The interface acts as a silent gallery for the bread, prioritizing high functionality and clarity over ornamental flourishes.

## Colors

The palette is intentionally restrained to reflect the simplicity of sourdough's three ingredients. 

- **Warm Wheat (#F5DEB3):** The foundational background color. It provides a softer, more organic feel than pure white, mimicking unbleached flour and parchment paper.
- **Charcoal (#333333):** Used for all functional elements, including typography, icons, and structural borders. It provides a sharp, high-contrast anchor to the warmer tones.
- **Crust Accent (#5D4037):** A deep, earthy brown used sparingly for success states, active links, or secondary buttons to represent the caramelization of a well-baked loaf.
- **Secondary Wheat (#E8D3A9):** A slightly deeper shade of wheat used for hover states on primary surfaces and subtle UI layering.

## Typography

Typography in this design system balances authority with utility. 

**Newsreader** is utilized for all editorial and heading levels. Its traditional serif structure communicates heritage and the "slow" nature of sourdough. It should be typeset with tight tracking for larger headlines to emphasize a modern, high-end editorial feel.

**Work Sans** serves as the functional workhorse. It is used for body copy, navigation, and UI labels. Its neutral, open character ensures legibility at small scales, particularly in complex areas like nutritional facts or ingredient lists. Use the semi-bold weight for labels to create a clear visual hierarchy against the serif headings.

## Layout & Spacing

This design system employs a **Fixed Grid** model to maintain an editorial, magazine-like structure. The layout is built on a 12-column grid with a maximum container width of 1280px. 

Spacing follows a strict 8px base rhythm to ensure mathematical harmony. Generous whitespace (the "lg" and "xl" units) should be used between major sections to prevent the "Rustic" aesthetic from feeling cluttered or "country-kitsch." Elements should feel intentional and grounded, often aligned to the left to maintain a strong vertical axis reminiscent of a recipe card or a ledger.

## Elevation & Depth

Depth is conveyed through **Bold Borders** and **Tactile Overlays** rather than traditional drop shadows. This keeps the interface feeling "flat" like a sheet of paper on a baker’s bench.

1.  **Borders:** Use solid 1px or 2px Charcoal (#333333) lines to define containers. This creates a sturdy, architectural feel.
2.  **Grain Overlay:** A global, low-opacity noise filter (simulating flour-dusted paper) should be applied to the primary Warm Wheat background.
3.  **Tonal Stacking:** Surfaces that need to appear closer to the user should use a slightly lighter tint of the primary background or a 1px border, rather than z-axis elevation.
4.  **Tactility:** Interactive elements should feel physical. On press, buttons do not "lift" with shadows; instead, they should swap fill and stroke colors or shift 2px down and right to simulate a physical mechanical press.

## Shapes

The shape language is **Soft (0.25rem)**. While the brand is rustic, pure 0px sharp corners feel too aggressive and industrial. A subtle 4px radius on buttons, input fields, and cards suggests the organic, hand-shaped nature of a loaf of bread without becoming "bubbly" or overly digital.

Image containers for product photography may occasionally use a larger radius or organic "blob" masks to emphasize the artisanal, non-uniform nature of sourdough boules. Functional UI elements, however, must remain strictly consistent with the soft-cornered aesthetic.

## Components

### Buttons
- **Primary:** Solid Charcoal (#333333) background with Warm Wheat (#F5DEB3) text. No shadow. 1px border of the same color to maintain size during state changes.
- **Secondary:** Transparent background with a 2px Charcoal border. 

### Inputs & Forms
- **Fields:** 1px Charcoal border on Warm Wheat background. Labels use Work Sans Semi-bold in all-caps for a "stamped" look.
- **Focus State:** The border thickness increases to 2px; the background remains Warm Wheat to ensure the grain texture is still visible.

### Cards
- **Product Cards:** Minimalist containers with a 1px Charcoal border. The product name (Newsreader) should be prominent, with the weight/price (Work Sans) tucked neatly at the bottom.
- **Recipe/Article Cards:** Use the Crust Accent (#5D4037) for categories or tags to provide a small splash of warmth.

### Lists & Navigation
- **Navigation:** Clean, uppercase Work Sans labels. Use a horizontal line (1px Charcoal) to separate the navigation from the header, reinforcing the grid.
- **Product Lists:** Use generous gutters (24px) to allow each artisanal product image enough room to breathe.

### Additional Elements
- **Texture Overlays:** Apply a subtle "flour-dust" SVG mask to the corners of the main hero sections.
- **Dividers:** Use thin, solid Charcoal lines to separate content, evoking the feel of a traditional ledger or bakery menu.