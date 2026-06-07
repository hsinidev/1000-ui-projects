---
name: The Amber-Rare Aesthetic
colors:
  surface: '#1c110c'
  surface-dim: '#1c110c'
  surface-bright: '#443630'
  surface-container-lowest: '#160c07'
  surface-container-low: '#251913'
  surface-container: '#291d17'
  surface-container-high: '#342721'
  surface-container-highest: '#40322b'
  on-surface: '#f5ded4'
  on-surface-variant: '#e0c0b2'
  inverse-surface: '#f5ded4'
  inverse-on-surface: '#3b2d27'
  outline: '#a78b7e'
  outline-variant: '#584238'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#562000'
  primary-container: '#ea6b1e'
  on-primary-container: '#4b1b00'
  inverse-primary: '#a04100'
  secondary: '#ffb77b'
  on-secondary: '#4d2700'
  secondary-container: '#7a4100'
  on-secondary-container: '#ffb270'
  tertiary: '#aac7ff'
  on-tertiary: '#002f64'
  tertiary-container: '#3e90ff'
  on-tertiary-container: '#002958'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ffb77b'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6d3a00'
  tertiary-fixed: '#d6e3ff'
  tertiary-fixed-dim: '#aac7ff'
  on-tertiary-fixed: '#001b3e'
  on-tertiary-fixed-variant: '#00458d'
  background: '#1c110c'
  on-background: '#f5ded4'
  surface-variant: '#40322b'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '600'
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The brand personality for this design system is rooted in the "Modern Heritage" movement—a fusion of **Minimalism** and **Tactile Luxury**. It is designed to evoke the atmosphere of a private, dimly lit whiskey library, emphasizing exclusivity, warmth, and the passage of time.

The design targets high-net-worth connoisseurs and collectors. The emotional response should be one of quiet confidence and sensory richness. Visually, the system utilizes high-contrast interfaces where dark, "moody" surfaces are punctuated by glowing metallic accents. Subtle textures, reminiscent of aged paper or brushed copper, are used sparingly to ground the digital experience in the physical world of boutique craftsmanship.

## Colors

The palette is intentionally restricted to maintain a boutique, high-end feel. 

- **Charcoal (#1A1A1A):** The foundation of the design, providing a deep, immersive background that allows imagery to pop.
- **Burnt Orange (#CC5500):** Used for primary actions and critical highlights. It represents the "heart" of the whiskey.
- **Copper (#B87333):** Reserved for secondary accents, icons, and metallic gradients. It should be applied to simulate light hitting metal surfaces.
- **Antique White (#F5F5F0):** Used for primary typography to ensure high legibility against the dark background without the harshness of pure white.

Gradients should be used subtly, transitioning from #CC5500 to #B87333 to create a "liquid amber" effect on buttons and active states.

## Typography

This design system employs a high-contrast typographic pairing to balance tradition with modernity.

**Playfair Display** is the voice of authority and heritage. It should be used for all major headings and product names. Large display sizes should use a tighter letter-spacing to emphasize the elegance of the serifs.

**Montserrat** provides a clean, functional counterpoint. It is used for all body copy, descriptions, and technical data. Labels and metadata should utilize the uppercase Montserrat with increased letter-spacing to mimic the look of premium spirits packaging.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model to create a curated, editorial experience. The layout is centered around a 12-column grid with a maximum container width of 1280px.

Generous whitespace (or "dark space") is essential to convey luxury. Vertical spacing between sections should be expansive (80px+) to allow the high-quality whiskey photography to breathe. Spacing follows an 8px rhythmic scale, ensuring that even the most complex data charts remain structured and legible within their containers.

## Elevation & Depth

Hierarchy in this design system is established through **Tonal Layering** and **Copper-rimmed Edges** rather than traditional drop shadows.

1.  **Base Layer:** The Charcoal (#1A1A1A) background.
2.  **Surface Layer:** A slightly lighter Charcoal (#242424) used for cards and containers, creating a subtle lift.
3.  **Accent Elevation:** Interactive elements may feature a "backlight" effect—a soft, Burnt Orange outer glow (15% opacity, 20px blur) to simulate warmth emanating from the product.
4.  **Metallic Strokes:** High-priority containers use 1px solid Copper (#B87333) borders or "inner-glow" gradients to define edges against the dark background, mimicking the rim of a crystal glass or the metal band of a cask.

## Shapes

The shape language is precise and architectural. A **Soft (Level 1)** roundedness is applied to UI elements to prevent the interface from feeling too industrial or sharp, while maintaining the sophisticated silhouette of boutique labels.

- **Standard Elements:** 0.25rem (4px) corner radius for buttons and input fields.
- **Large Containers:** 0.5rem (8px) corner radius for product cards and image galleries.
- **Interactive Triggers:** Small circular elements (like radio buttons or icon toggles) should maintain a perfect circle to echo the shape of a bottle cap or glass rim.

## Components

### Buttons
Primary buttons use a linear gradient (Burnt Orange to Copper) with Montserrat Bold text in uppercase. Secondary buttons are "Ghost" style with a 1px Copper border and no fill.

### Elegant Cards
Product cards feature a Charcoal-on-Charcoal look. The background of the card is #242424, featuring a 1px top-border in #B87333. Images of whiskey bottles should be high-contrast with transparent backgrounds, allowing the liquid's amber glow to merge with the card.

### Sophisticated Charts
Data visualizations for whiskey investment or flavor profiles use a monochromatic Copper palette. Grid lines in charts should be kept at 5% opacity Antique White. Points of interest on a chart are highlighted with a glowing Burnt Orange dot.

### Image Containers
Images are never presented as raw files. They are housed in containers with a subtle "vignette" overlay that darkens the edges, drawing the eye toward the center and integrating the photo into the dark UI.

### Inputs & Selectors
Input fields are underlined rather than boxed, using a 1px Copper line that expands on focus. This mimics the minimalist aesthetic of high-end menu design.