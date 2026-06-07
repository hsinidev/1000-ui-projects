---
name: Radiant & Timeless
colors:
  surface: '#fbf9f7'
  surface-dim: '#dbdad8'
  surface-bright: '#fbf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efedec'
  surface-container-high: '#eae8e6'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1b'
  on-surface-variant: '#524345'
  inverse-surface: '#30302f'
  inverse-on-surface: '#f2f0ee'
  outline: '#857374'
  outline-variant: '#d7c1c3'
  surface-tint: '#8c4b55'
  primary: '#8a4853'
  on-primary: '#ffffff'
  primary-container: '#a6606b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dcdddd'
  on-secondary-container: '#5f6161'
  tertiary: '#5d5c5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#757474'
  on-tertiary-container: '#f7feff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#fbf9f7'
  on-background: '#1b1c1b'
  surface-variant: '#e4e2e0'
typography:
  display-hero:
    fontFamily: Noto Serif
    fontSize: 72px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
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
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.15em
spacing:
  container-max: 1440px
  gutter: 32px
  margin-edge: 80px
  section-gap: 160px
  unit: 8px
---

## Brand & Style
This design system centers on a high-end luxury experience that balances classical elegance with modern digital sophistication. The brand personality is prestigious, curated, and luminous, targeting a discerning audience that values craftsmanship and heritage.

The visual style is a blend of **Minimalism** and **Tactile/Glassmorphism**. It utilizes expansive white space to denote exclusivity, while employing subtle shimmer effects and marble textures to provide a sense of physical weight and premium materiality. The interface should feel like walking through a high-end boutique: quiet, spacious, and focused on the brilliance of the product.

## Colors
The palette is anchored by **Rose Gold** (Primary), used for calls to action and delicate accents. **Deep Charcoal** (Tertiary) provides high-contrast grounding for typography, ensuring legibility and a modern edge. 

The background strategy utilizes **Marble White** (Neutral) and soft greys. The "Marble" effect is achieved through subtle, high-resolution background patterns with low-opacity veining. To capture the "Radiant" aspect, a CSS shimmer effect is applied to metallic elements, using a moving linear gradient to simulate light reflecting off polished gold.

## Typography
The typographic hierarchy relies on the tension between the classic, editorial feel of **Noto Serif** and the clean, functional precision of **Manrope**. 

For desktop, headlines are oversized to command attention and create an "editorial spread" feel. Tracking is tightened on large displays but significantly loosened for uppercase labels to evoke the engraving found on luxury watch faces or jewelry boxes. Paragraphs use generous line heights to ensure a relaxed, effortless reading experience.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop, centered on a 1440px canvas. A 12-column grid provides the structure, but the system encourages "breaking the grid" with asymmetrical image placements to mimic luxury fashion layouts.

Whitespace (negative space) is treated as a core design element, not just a separator. Section gaps are intentionally large (160px+) to allow each product collection to breathe. For desktop optimization, content is often offset to one side of the screen, balanced by high-resolution imagery on the other.

## Elevation & Depth
Depth is achieved through **Tonal Layers** and **Glassmorphism** rather than traditional heavy shadows. 

Surface tiers are defined by subtle shifts between white and marble textures. When elements require lift (such as dropdown menus or hovering product cards), a "Backdrop Blur" (12px to 20px) is combined with a razor-thin 1px stroke in a semi-transparent Rose Gold. Shadows, where used, are "Ambient": extremely diffused (40px-60px blur), very low opacity (5%), and tinted with a hint of the Deep Charcoal or Rose Gold to maintain a natural, soft appearance.

## Shapes
The shape language is strictly **Sharp (0)**. Right angles communicate architectural precision and timelessness. Softening the corners would detract from the "high-jewelry" precision. 

Occasional use of perfect circles is permitted for specific functional elements like color swatches or image carousels, providing a geometric contrast to the dominant rectangular grid.

## Components
- **Buttons:** Primary buttons are Deep Charcoal with white text or Rose Gold with a subtle shimmer overlay. They use sharp corners, generous horizontal padding (40px+), and uppercase labels. On hover, a "Radiant" shimmer glides across the surface.
- **Product Cards:** Cards are borderless with a flat background. The image occupies 100% of the card width. Text details appear below with significant padding. On hover, the image subtly scales up (1.05x) within its container.
- **Inputs:** Text fields use a "Ghost" style—a single 1px bottom border in Deep Charcoal. Labels float above the line in uppercase Manrope.
- **Chips/Filters:** Used for material types (e.g., "18k Gold"). These are simple text links with a small underline that expands on hover.
- **Navigation:** The desktop header is transparent, turning into a blurred "Marble" glass effect on scroll. Links are centered with wide tracking.
- **Jewelry Specs:** Use a "Technical Grid" component—a 2-column list with thin charcoal dividers, presenting diamond carats, metal weight, and clarity in a clean, tabular format.