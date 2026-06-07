---
name: Terra & Tide
colors:
  surface: '#fff8f3'
  surface-dim: '#e0d9d2'
  surface-bright: '#fff8f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf2eb'
  surface-container: '#f4ede5'
  surface-container-high: '#eee7e0'
  surface-container-highest: '#e9e1da'
  on-surface: '#1e1b17'
  on-surface-variant: '#434842'
  inverse-surface: '#33302b'
  inverse-on-surface: '#f7efe8'
  outline: '#747872'
  outline-variant: '#c4c8c0'
  surface-tint: '#516351'
  primary: '#4f604f'
  on-primary: '#ffffff'
  primary-container: '#677966'
  on-primary-container: '#f7fff2'
  inverse-primary: '#b8ccb6'
  secondary: '#8c4e2e'
  on-secondary: '#ffffff'
  secondary-container: '#feae87'
  on-secondary-container: '#793f21'
  tertiary: '#5e5c55'
  on-tertiary: '#ffffff'
  tertiary-container: '#77746d'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e8d1'
  primary-fixed-dim: '#b8ccb6'
  on-primary-fixed: '#0f1f11'
  on-primary-fixed-variant: '#3a4b3a'
  secondary-fixed: '#ffdbcb'
  secondary-fixed-dim: '#ffb692'
  on-secondary-fixed: '#341100'
  on-secondary-fixed-variant: '#6f3819'
  tertiary-fixed: '#e7e2d9'
  tertiary-fixed-dim: '#cac6be'
  on-tertiary-fixed: '#1d1c16'
  on-tertiary-fixed-variant: '#494740'
  background: '#fff8f3'
  on-background: '#1e1b17'
  surface-variant: '#e9e1da'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
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
  unit: 8px
  container-max: 1280px
  gutter: 32px
  section-padding: 120px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built upon a philosophy of "Organic Minimalism." It targets a high-end clientele seeking professional landscaping services that harmonize with the natural world. The aesthetic is serene and grounded, avoiding the sterile coldness of traditional corporate design in favor of an airy, breathable interface.

The style leverages **Minimalism** with a **Tactile** edge—using vast amounts of whitespace to evoke the feeling of an open garden, while utilizing subtle textures and soft color shifts to maintain a sense of physical, earthy presence. The emotional response is one of tranquility, trust, and refined craftsmanship.

## Colors

The palette is derived directly from botanical and geological elements. 
- **Primary (Sage Green):** Used for main actions and brand identifiers, symbolizing growth and stability.
- **Secondary (Warm Terracotta):** An accent color used sparingly for calls-to-action or to highlight premium service tiers, providing a warm, human contrast to the greens.
- **Tertiary (Sandy Beige):** The foundational surface color, replacing pure white to reduce eye strain and add a sophisticated, parchment-like quality.
- **Neutral (Earth Charcoal):** Used for typography and iconography to ensure high legibility while remaining softer than pure black.

Large expanses of the Tertiary shade should be used to create the "airy" feel requested, acting as the canvas for all other elements.

## Typography

The typography strategy pairs the timeless elegance of **Noto Serif** for headers with the modern, balanced clarity of **Manrope** for functional text. 

Headers should be treated with generous leading (line height) to maintain the airy aesthetic. For small labels or overlines, use Manrope in all-caps with increased letter spacing to create a professional, "architectural" feel. Avoid bold weights for serif headers to maintain a high-end, editorial look; instead, use weight sparingly in the sans-serif body text for emphasis and hierarchy.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for desktop, centered within the viewport to create a composed, gallery-like experience. The spacing rhythm is intentionally "loose," utilizing 8px increments but leaning toward the larger end of the scale to ensure the "airy" aesthetic.

- **Section Padding:** Extremely generous vertical padding (120px+) is used to separate different service offerings, allowing each "garden" of content to breathe.
- **The 60/40 Rule:** When pairing imagery with text, prioritize a 60% whitespace/image to 40% text ratio to prevent the UI from feeling cluttered or overly commercial.

## Elevation & Depth

To maintain a grounded, serene feel, this design system avoids heavy drop shadows. Depth is instead communicated through:
- **Tonal Layering:** Using slight variations of the "Sandy Beige" and "Sage" to indicate hierarchy.
- **Ambient Shadows:** When elevation is necessary (e.g., for hovering over a service card), use very soft, long-range shadows with a low-opacity tint of the Primary color (Sage) rather than grey. This creates a "glow" rather than a "weight."
- **Low-Contrast Outlines:** Use 1px borders in a shade just slightly darker than the background to define input fields and containers, keeping the visual noise to a minimum.

## Shapes

The shape language is defined by **Rounded** geometry, mirroring the organic curves found in nature—river stones, leaves, and rolling hills. 

- **Containers:** Use `rounded-lg` (1rem) for most content blocks and cards.
- **Interactive Elements:** Use `rounded-xl` (1.5rem) for buttons to make them feel tactile and inviting.
- **Images:** Large-scale hero imagery should feature one or two rounded corners (e.g., top-left and bottom-right) to create a custom, high-end landscape feel that breaks the standard rectangular "grid."

## Components

### Buttons
Primary buttons use the Sage Green background with Noto Serif text for a distinctive, premium look. Secondary buttons use a Terracotta outline. All buttons feature high horizontal padding and a minimum height of 56px to feel substantial and grounded.

### Input Fields
Fields are styled with a subtle Sandy Beige fill and a thin Earth Charcoal bottom-border only, or a fully rounded border-box with 12px padding. Focus states should transition the border color to Sage Green.

### Cards
Service cards should be borderless with a slightly lighter background than the main page. They should utilize "Soft" rounded corners and include ample internal padding (40px) to ensure text does not feel crowded near the edges.

### Lists & Icons
Icons should be thin-stroke (Linear) and colored in Sage Green. Bulleted lists should replace standard dots with custom organic shapes, like a small stylized leaf or a soft pebble-like circle.

### Additional Components
- **The "Before & After" Slider:** A custom component with a rounded central handle to showcase landscaping transformations.
- **Seasonal Moodboard:** A masonry-style gallery layout with varying corner radii on images to display portfolio work in an organic, non-linear fashion.