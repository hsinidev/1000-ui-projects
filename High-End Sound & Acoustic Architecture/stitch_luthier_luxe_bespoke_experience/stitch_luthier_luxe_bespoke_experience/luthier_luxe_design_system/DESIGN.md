---
name: Luthier-Luxe Design System
colors:
  surface: '#fff8f6'
  surface-dim: '#f2d4ca'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ec'
  surface-container: '#ffe9e2'
  surface-container-high: '#ffe2d8'
  surface-container-highest: '#fadcd2'
  on-surface: '#271812'
  on-surface-variant: '#514440'
  inverse-surface: '#3e2c26'
  inverse-on-surface: '#ffede7'
  outline: '#83746f'
  outline-variant: '#d5c2bd'
  surface-tint: '#7f5445'
  primary: '#35160b'
  on-primary: '#ffffff'
  primary-container: '#4e2a1e'
  on-primary-container: '#c4907f'
  inverse-primary: '#f2baa8'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#1e2010'
  on-tertiary: '#ffffff'
  tertiary-container: '#333524'
  on-tertiary-container: '#9d9e88'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#f2baa8'
  on-primary-fixed: '#311308'
  on-primary-fixed-variant: '#643d30'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fff8f6'
  on-background: '#271812'
  surface-variant: '#fadcd2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 3rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 2.25rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 2rem
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Source Sans 3
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Source Sans 3
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Source Sans 3
    fontSize: 0.75rem
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
  margin-desktop: 80px
  margin-mobile: 20px
  max-width: 1280px
---

## Brand & Style
The brand personality is that of a master artisan: patient, precise, and deeply rooted in heritage. It targets discerning collectors and professional musicians who value the "human touch" and the tactile nature of high-end instruments.

The design system adopts a **Tactile / Skeuomorphic** style refined for the modern web. It mimics the physical experience of leafing through a bespoke workshop catalog. The UI should evoke a sense of quiet luxury through the use of organic textures (wood grain, heavy paper stock), gold leaf detailing, and a layout that breathes with generous whitespace. Every element should feel weighted and deliberate, as if it were handcrafted from physical materials.

## Colors
The palette is inspired by the luthier’s workshop—shavings of spruce, aged varnish, and polished mahogany. 

- **Primary (Deep Mahogany):** Used for primary headers, navigation backgrounds, and high-impact structural elements. It provides the "weight" of a solid wood instrument.
- **Secondary (Rich Gold):** Reserved for interactive accents, "Gold Foil" borders, and premium signifiers. It represents the quality of the hardware and the brand's prestige.
- **Tertiary (Aged Parchment):** Used for card backgrounds and secondary surfaces to provide a subtle contrast against the main background.
- **Backgrounds:** Use a soft cream/off-white (`#FAF9F6`) to prevent the starkness of pure white and maintain a vintage, paper-like feel.
- **Typography:** Headlines utilize the primary mahogany for depth, while body text uses a slightly softened near-black for maximum legibility without harsh contrast.

## Typography
The typographic hierarchy establishes a dialogue between the artisanal (Serif) and the functional (Sans-Serif).

**Playfair Display** is used for all headings. Its high stroke contrast and elegant serifs mirror the delicate curves of a cello or guitar body. Large display sizes should be set with tighter letter spacing to emphasize their editorial quality.

**Source Sans 3** provides a clean, modern counterpoint for body copy and UI labels. It ensures that technical specifications and instrument details are highly legible. Use wider letter spacing and uppercase styling for small labels to create a "technical blueprint" aesthetic.

## Layout & Spacing
This design system utilizes a **Fixed Grid** approach for desktop to simulate the structured pages of a physical catalog. 

- **Desktop:** A 12-column grid with a maximum width of 1280px. Margins are generous (80px) to frame the content like a matte-mounted photograph.
- **Mobile:** A 4-column fluid grid with 20px margins.
- **Rhythm:** An 8px base unit drives all padding and margins. Vertical rhythm is intentionally loose; content should feel airy and unhurried. Use larger vertical gaps (80px–120px) between major sections to denote a change in "chapter."

## Elevation & Depth
Depth is created through "Material Stacking." Rather than abstract shadows, the system uses **Ambient Shadows** that suggest a physical object resting on a flat surface.

- **Surface Layers:** The base layer is the Parchment background. Cards and sections sit on top of this with extremely soft, wide-dispersion shadows (`box-shadow: 0 10px 30px rgba(78, 42, 30, 0.08)`).
- **Textural Depth:** Headers and primary sections may feature a subtle, low-opacity wood-grain overlay to give the mahogany color a material quality.
- **Gold Accents:** Use a 1px inner glow or "foil" stroke on primary buttons and dividers to suggest metallic inlay.

## Shapes
The shape language is **Soft (0.25rem)**. While instruments are curved, the catalog aesthetic relies on the structure of the page and the wood block. 

Corners should not be overly rounded or "bubbly," as this detracts from the serious, high-end nature of the brand. Small radii on buttons and cards provide just enough softness to feel "finished" and "sanded" rather than industrial or sharp.

## Components
- **Buttons:** Primary buttons use the Deep Mahogany background with Rich Gold text and a subtle 1px gold foil border. Hover states should include a slight lift (elevation increase) rather than a color change.
- **Cards:** Product cards should feature the Aged Parchment background, a soft shadow, and a "spec label" at the bottom using the small, uppercase label font.
- **Input Fields:** Use a "minimalist ledger" style—only a bottom border in Mahogany, which becomes a 2px Gold line upon focus.
- **Dividers:** Use horizontal lines that transition from transparent to Rich Gold and back to transparent, mimicking a fine metallic wire.
- **Navigation:** The top header should be treated as a "Header Bar" of dark wood, with navigation items set in the high-contrast Serif at a small scale.
- **Interactive Woodgrain:** For larger interactive elements (like hero section buttons or decorative panels), apply a CSS mask or subtle background image of dark grain to reinforce the luthier theme.