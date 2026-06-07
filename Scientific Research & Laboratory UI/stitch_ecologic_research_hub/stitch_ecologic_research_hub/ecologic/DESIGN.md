---
name: EcoLogic
colors:
  surface: '#faf9f7'
  surface-dim: '#dadad8'
  surface-bright: '#faf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1b'
  on-surface-variant: '#42493e'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#313d2b'
  on-tertiary: '#ffffff'
  tertiary-container: '#475441'
  on-tertiary-container: '#b9c7b0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#d9e7ce'
  tertiary-fixed-dim: '#bdcbb3'
  on-tertiary-fixed: '#131e0f'
  on-tertiary-fixed-variant: '#3e4a38'
  background: '#faf9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e3e2e0'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
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
  data-mono:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  section-gap: 64px
---

## Brand & Style

This design system is built on the principles of environmental stewardship, precision, and tactile grounding. It targets scientists, field researchers, and environmental analysts who require a high-density data environment that doesn't feel clinical or cold. 

The aesthetic is **Modern Organic**. It blends the structural clarity of modern minimalism with the warmth of tactile materials. The UI should evoke the feeling of high-end field journals and sustainable laboratory equipment. Visual elements utilize subtle grain overlays to mimic natural paper textures, reducing screen glare and providing a comfortable long-form reading experience for complex research data.

## Colors

The palette is derived from the natural world to reinforce the "Sustainable & Grounded" narrative. 
- **Forest Green** is used for primary actions, brand presence, and success states.
- **Earthy Brown** provides a grounding force for secondary navigation, iconography, and deep structural elements.
- **Crisp White** and a secondary **Neutral Linen** (#F9F8F6) serve as the primary canvas, providing the "Airy" feel requested.

For data visualization, use a palette of muted clay, slate blue, and ochre to maintain the organic tone while ensuring high contrast for scientific legibility.

## Typography

The typographic system utilizes a "Scientific Editorial" pairing.
- **Headings (Newsreader):** A professional serif that brings academic authority and a literary feel to the research hub. It should be used for page titles, article headers, and significant callouts.
- **Body & Data (Work Sans):** Chosen for its exceptional legibility in technical contexts. The slight optimization for data-heavy tables ensures that sensor readings and coordinates remain clear. 

Use sentence case for most UI labels to maintain a friendly, approachable tone, reserving uppercase only for small "label-caps" used in table headers or category tags.

## Layout & Spacing

This design system employs a **Fluid Grid** model with a focus on "Breathable Density." While scientific data can be overwhelming, the layout uses generous outer margins (32px+) and significant gaps between major sections (64px+) to prevent cognitive fatigue.

Grid sections should follow a 12-column structure for the main dashboard, but components like GIS maps should often "break the grid" to go full-bleed, providing an immersive experience for spatial analysis. Vertical rhythm is strictly managed on an 8px baseline to ensure alignment across multi-column data sheets.

## Elevation & Depth

To maintain the grounded aesthetic, avoid deep, dramatic shadows. Instead, use **Tonal Layers** and **Subtle Materiality**:
- **Layering:** Backgrounds use the Neutral Linen (#F9F8F6), while active cards and surfaces use Crisp White (#FFFFFF).
- **Depth:** Use very soft, low-opacity umber shadows (e.g., `rgba(93, 64, 55, 0.08)`) to give the impression of paper resting on a wooden desk.
- **Texture:** Apply a global CSS `noise` filter at 2-3% opacity to all primary surfaces to create a tactile, non-digital feel that reduces eye strain during field research.

## Shapes

The shape language is **Organic & Geometric**. While the grid remains structured, individual components like buttons, input fields, and cards use "Rounded" (0.5rem) corners to mimic the soft edges found in nature (smoothed river stones, leaf silhouettes). 

Interactive elements should never have sharp 90-degree angles, as the goal is to feel accessible and harmonious with the environment being studied.

## Components

### Buttons & Inputs
- **Primary Buttons:** Solid Forest Green with Crisp White text. Use a slight "squish" animation (scale 0.98) on click to reinforce the tactile nature.
- **Field Data Inputs:** Robust, thick-bordered fields with Earthy Brown labels. Focus states should use a soft Forest Green glow.

### Data & Maps
- **GIS Map Overlays:** Use glassmorphic panels (frosted white with 80% opacity) for map controls to ensure the topography remains visible beneath the UI.
- **Data-Heavy Tables:** High-density rows using Work Sans. Use alternating row fills of Neutral Linen instead of hard grid lines to maintain the "Airy" feel.
- **Analytic Charts:** Use a custom "Earth-tone" color scale. Lines should be slightly smoothed (interpolation) to feel more organic and less jagged.

### Specialized Components
- **Sensor Status Chips:** Use pill-shaped indicators with subtle pulsing animations for live field sensors.
- **Paper Cards:** Content containers that feature a very subtle grain texture and a thin 1px border in a slightly darker neutral shade.