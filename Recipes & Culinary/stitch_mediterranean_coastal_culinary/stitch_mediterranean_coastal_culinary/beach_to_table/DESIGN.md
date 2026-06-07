---
name: Beach-to-Table
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#414750'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#727781'
  outline-variant: '#c1c7d1'
  surface-tint: '#1a619d'
  primary: '#003e6b'
  on-primary: '#ffffff'
  primary-container: '#005691'
  on-primary-container: '#a0cbff'
  inverse-primary: '#9ecaff'
  secondary: '#695c50'
  on-secondary: '#ffffff'
  secondary-container: '#f2dfd0'
  on-secondary-container: '#706256'
  tertiary: '#3b3d3d'
  on-tertiary: '#ffffff'
  tertiary-container: '#525454'
  on-tertiary-container: '#c7c8c8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e4ff'
  primary-fixed-dim: '#9ecaff'
  on-primary-fixed: '#001d36'
  on-primary-fixed-variant: '#00497c'
  secondary-fixed: '#f2dfd0'
  secondary-fixed-dim: '#d5c3b5'
  on-secondary-fixed: '#231a11'
  on-secondary-fixed-variant: '#51453a'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-desktop: 64px
---

## Brand & Style

The brand personality of this design system is "Coastal Sophistication"—a bridge between the raw, rhythmic beauty of the Mediterranean coast and the refined precision of high-end culinary arts. It targets a discerning audience of seafood enthusiasts, professional chefs, and luxury travelers who value transparency, freshness, and elegance. The UI should evoke a sense of calm, airiness, and premium quality.

The chosen style is **Minimalism with a Tactile twist**. We leverage heavy whitespace and high-quality photography to let the "beach-to-table" narrative breathe. Subtle glassmorphism and soft, tinted shadows are employed to give the interface a layered, organic feel, mimicking the play of light on water and sand.

## Colors

The palette is derived directly from the Mediterranean coastline.
- **Mediterranean Blue (#005691)**: Used for primary actions, deep headlines, and structural emphasis. It represents the depth and reliability of the ocean.
- **Sand (#F4E1D2)**: Used for subtle background sections, secondary buttons, and decorative elements to provide warmth against the white.
- **Crisp White (#FFFFFF)**: The primary canvas. It ensures the "airy" feel and allows food photography to remain the focal point.
- **Surface Accents**: Semi-transparent versions of Mediterranean Blue (5-10% opacity) are used for hover states and subtle Dividers to maintain a soft, fluid appearance.

## Typography

This design system utilizes a high-contrast typographic pairing to balance tradition and modernity.
- **Headlines**: Use **Noto Serif**. Its elegant, high-contrast strokes provide an editorial, authoritative feel suitable for high-end culinary content.
- **Body & Interface**: Use **Plus Jakarta Sans**. Its soft, rounded terminals and open apertures maintain legibility and a welcoming, contemporary atmosphere. 
- **Hierarchy**: Large margins between headlines and body text are essential to maintain the "airy" aesthetic.

## Layout & Spacing

This design system uses a **Fluid Grid** model to accommodate the expansive nature of coastal imagery. 
- **The 12-Column System**: Elements should align to a 12-column grid with a 24px gutter. However, container widths for text-heavy content are constrained to 8 columns (centered) to ensure readability.
- **Rhythm**: We utilize an 8px baseline grid. Spacing between major sections should favor the `xl` (80px) or `lg` (48px) units to create the signature "airy" feel.
- **Fluidity**: Card layouts for recipes should transition from 3-column to 2-column to 1-column layouts based on viewport width, maintaining generous edge margins of at least 64px on large displays.

## Elevation & Depth

To create a sophisticated, high-end feel, we avoid heavy drop shadows in favor of **Ambient, Tinted Shadows**.
- **Shadow Profile**: Shadows should use a very low-opacity Mediterranean Blue (#005691 at 8-12%) rather than pure black. This keeps the shadows "cool" and integrated with the brand colors.
- **Tonal Layers**: The "Sand" color is used as a base layer for cards or call-out sections, creating a subtle step-up from the white background without requiring a border.
- **Glassmorphism**: Interactive tool overlays and navigation bars use a backdrop blur (20px) with a 70% white tint, mimicking the appearance of sea glass.

## Shapes

The shape language is **Organic and Rounded**, avoiding the clinical feel of sharp corners.
- **Base Components**: Buttons and input fields use a 0.5rem (8px) radius.
- **Cards & Containers**: Recipe cards and map interface modules use a 1rem (16px) radius to feel approachable and high-end.
- **Imagery**: Photography should occasionally use asymmetrical rounded corners (e.g., top-left and bottom-right only) to mimic the irregular beauty of coastal landscapes.

## Components

### Cards
Recipe cards are the cornerstone of this design system. They feature full-bleed imagery at the top with a subtle "Sand" colored content area below. Shadows are only applied on hover to simulate the card lifting off the page.

### Buttons
Primary buttons are solid Mediterranean Blue with white text. Secondary buttons use a Sand background with Blue text. Both feature a subtle transition: on hover, the background opacity softens, and the shadow deepens slightly.

### Interactive Tool Interfaces
Tools (like portion calculators or seasonal charts) utilize the glassmorphism effect. Sliders and toggles use Mediterranean Blue for the active state and Sand for the track.

### Map Interface
The sophisticated map interface uses a customized monochromatic style: water is rendered in Mediterranean Blue, and land is rendered in Sand or White. Markers are custom-shaped icons (minimalist anchors or fish) in high-contrast Blue.

### Inputs & Selects
Form fields use a soft, 1px Mediterranean Blue border at 20% opacity. Upon focus, the border becomes 100% opaque, and a subtle blue-tinted outer glow is applied.