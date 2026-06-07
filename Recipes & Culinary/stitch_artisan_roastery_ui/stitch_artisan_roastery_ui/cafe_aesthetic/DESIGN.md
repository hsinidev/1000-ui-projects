---
name: Cafe Aesthetic
colors:
  surface: '#faf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#444748'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#735a31'
  on-secondary: '#ffffff'
  secondary-container: '#fddba7'
  on-secondary-container: '#785f35'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#2c160e'
  on-tertiary-container: '#9f7c71'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffdeac'
  secondary-fixed-dim: '#e3c290'
  on-secondary-fixed: '#281900'
  on-secondary-fixed-variant: '#59431c'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#e7bdb1'
  on-tertiary-fixed: '#2c160e'
  on-tertiary-fixed-variant: '#5d4037'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
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
  margin-mobile: 20px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

The design system is rooted in the "Slow Coffee" movement—emphasizing intentionality, craftsmanship, and sensory experience. The personality is quiet yet confident, avoiding loud marketing tropes in favor of editorial elegance. It targets a discerning audience that values the origin of the bean as much as the aesthetic of the brewing ritual.

The visual style is a hybrid of **Minimalism** and **Tactile** design. It leverages expansive whitespace to create a sense of calm and "breathability," while introducing organic depth through subtle textures and wood-toned accents. This approach ensures the digital interface feels as grounded and premium as a physical boutique roastery.

## Colors

The palette for the design system is strictly curated to evoke the materials of a specialty café. 
- **Primary (Ink):** A deep, near-black charcoal used for high-contrast typography and primary actions.
- **Secondary (Oak):** A warm, desaturated gold-tan used for accents, active states, and highlighting premium details.
- **Tertiary (Walnut):** A rich, dark brown used sparingly for deep grounding elements or secondary decorative borders.
- **Neutral (Paper & Stone):** A range of off-whites and cool grays that provide a soft, non-reflective canvas, reducing eye strain and mimicking high-quality stationery.

Color should be applied with restraint; the "wood" tones (Oak and Walnut) function more as physical materials than digital colors.

## Typography

Typography in this design system creates a rhythmic contrast between the traditional and the modern. 
- **Noto Serif** provides an editorial, sophisticated authority for headlines. It should be typeset with generous leading to allow the letterforms to breathe.
- **Work Sans** offers a clean, architectural counterpoint for body text and functional UI elements. 

To maintain a premium feel, body text is never pure black; it uses a slightly softened charcoal to ensure a smooth reading experience against the off-white backgrounds. Label styles use increased letter-spacing and uppercase styling to denote metadata and small functional cues without cluttering the visual field.

## Layout & Spacing

The design system employs a **Fixed Grid** philosophy for desktop to maintain an editorial composition, while transitioning to a fluid model for mobile. 

A strict 8px baseline grid governs all vertical rhythm. However, the defining characteristic of the layout is the **Section Gap**. Large-scale components and narrative blocks are separated by significant whitespace (120px+) to force a slower pace of interaction. Gutters are kept wide to prevent content density, ensuring that every image and block of text feels curated and essential.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Organic Textures** rather than heavy z-axis layering. 
- **Surfaces:** Most containers use a flat, "paper" aesthetic. Depth is suggested by very soft, diffused shadows (15% opacity, 20px blur) that make cards appear to float slightly above a textured background.
- **Grain:** A subtle, low-opacity noise texture should be applied to the background to mimic the feel of unrefined paper or stone, breaking the clinical perfection of digital screens.
- **Overlays:** Modals and menus utilize a light backdrop blur (Glassmorphism) combined with a soft wood-toned tint to maintain warmth even when obscuring content.

## Shapes

The design system uses a **Soft (0.25rem)** roundedness as the default. This subtle rounding removes the harshness of geometric precision, making the UI feel more approachable and hand-finished. 

Cards and primary containers utilize `rounded-lg` (0.5rem) to suggest a sturdier, more tactile presence. Large imagery and hero sections may use sharp corners (0px) to lean into a high-fashion editorial aesthetic, while interactive elements like buttons maintain the soft rounding for a comfortable touch target.

## Components

### Buttons
Buttons in the design system are designed to look **Tactile**. Primary buttons use a solid Walnut or Black fill with a very subtle inner-shadow to suggest they can be physically pressed. Secondary buttons utilize a thin, 1px border in Oak with no fill, emphasizing a "ghost" aesthetic.

### Cards
Cards are minimalist and borderless. They rely on generous internal padding (32px+) and the ambient shadow defined in the Elevation section. Product cards should prioritize high-quality photography, with text treated as a caption rather than a label.

### Input Fields
Inputs are underlined with a 1px solid stroke rather than enclosed in a box. This reinforces the "handwritten/stationery" theme. The active state transforms the stroke to Oak.

### Iconography
Icons must be refined, thin-stroke (1px or 1.5px), and strictly monochromatic. They should be used sparingly as "punctuation" rather than as a primary means of navigation.

### Additional Components
- **Origin Labels:** Small, pill-shaped chips with a Walnut background and white text to denote coffee origins or roast levels.
- **Texture Overlays:** A component that applies a CSS grain filter to imagery to ensure a consistent, film-like quality across all visual assets.