---
name: Nomadic-Chef
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#d8c3b4'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#a08d80'
  outline-variant: '#524439'
  surface-tint: '#ffb77b'
  primary: '#ffb77b'
  on-primary: '#4d2700'
  primary-container: '#c8803f'
  on-primary-container: '#432100'
  inverse-primary: '#8c4f10'
  secondary: '#77dd6a'
  on-secondary: '#003a03'
  secondary-container: '#027910'
  on-secondary-container: '#9dff8d'
  tertiary: '#74d4ea'
  on-tertiary: '#00363f'
  tertiary-container: '#359db2'
  on-tertiary-container: '#002f37'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc2'
  primary-fixed-dim: '#ffb77b'
  on-primary-fixed: '#2e1500'
  on-primary-fixed-variant: '#6d3a00'
  secondary-fixed: '#92fa83'
  secondary-fixed-dim: '#77dd6a'
  on-secondary-fixed: '#002201'
  on-secondary-fixed-variant: '#005307'
  tertiary-fixed: '#a8edff'
  tertiary-fixed-dim: '#74d4ea'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5b'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: EB Garamond
    fontSize: 3.5rem
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: EB Garamond
    fontSize: 2.5rem
    fontWeight: '400'
    lineHeight: '1.2'
  h3:
    fontFamily: EB Garamond
    fontSize: 1.75rem
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  margin-page: 64px
  gutter: 24px
  section-gap: 120px
---

## Brand & Style

The brand identity centers on the intersection of raw wilderness and culinary mastery. This design system communicates "Luxury through the lens of the elements," prioritizing a sensory, high-contrast experience that feels like a private dinner in a remote forest at dusk. 

The aesthetic style is **Tactile Minimalism**. It leverages the starkness of modern editorial design while incorporating physical metaphors—specifically the warmth of embers and the resilience of cast iron. The UI should feel grounded, expensive, and intentional. Every interaction should evoke the quiet confidence of a professional chef working over an open flame: precise, rugged, and unhurried. 

Key visual drivers include:
- **Atmospheric Contrast:** Deep shadows pitted against warm, metallic highlights.
- **Natural Integrity:** Rough, organic textures used sparingly as backgrounds or dividers.
- **Architectural Stillness:** Large areas of negative space to mirror the solitude of the outdoors.

## Colors

This design system utilizes a **Dark Mode** default to maintain a moody, campfire-adjacent atmosphere.

- **Charcoal (#2F2F2F):** Used as the primary surface color. It provides a softer, more organic dark base than true black, suggesting stone and cooling ash.
- **Copper (#B87333):** The primary action and highlight color. It represents fire, heat, and high-end cookware. Use this for CTA buttons, active states, and iconography.
- **Forest Green (#228B22):** A secondary accent used for status indicators, nature-related tags, or subtle environmental cues. It should be used with restraint to prevent the UI from feeling "bright."
- **Typography & Details:** Use a range of warm grays (from the Copper family) for secondary text to maintain a low-strain reading experience against the dark background.

## Typography

The typographic hierarchy relies on the tension between the classic, literary heritage of the serif and the utilitarian clarity of the sans-serif.

- **Headlines:** `EB Garamond` is used for all display and heading levels. It conveys the sophistication of a printed menu or a leather-bound travelogue. For H1 elements, use italic styles sparingly to highlight specific words for an artisanal touch.
- **Body & UI:** `Work Sans` provides a grounded, legible counterpoint. Its neutral, professional character ensures that functional information—like ingredients, logistics, and booking details—is processed without distraction.
- **Labels:** Small caps and increased letter-spacing should be applied to `Work Sans` for category labels and utility headers to differentiate them from prose.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with an emphasis on "Editorial Breathing Room." 

Content should be centered within a max-width container (typically 1280px) with generous lateral margins. This creates a focused, high-end "magazine" feel. Spacing between major sections should be aggressive—allowing the eye to reset between the "The Expedition," "The Chef," and "The Menu."

Use an 8px baseline grid, but prioritize visual balance over strict adherence. Grid items should use asymmetric layouts occasionally to mimic the organic unpredictability of nature.

## Elevation & Depth

This design system eschews traditional soft shadows in favor of **Tonal Layers and Metallic Accents**.

- **Surfaces:** Depth is created by layering different shades of Charcoal. Backgrounds are the darkest level (#1A1A1A), while cards and interactive surfaces sit at #2F2F2F.
- **Borders:** Instead of shadows, use 1px solid borders in low-opacity Copper or Forest Green to define edges. This mimics the "tool-like" precision of culinary equipment.
- **Metallic Glow:** For primary interactive elements, use a very subtle "outer glow" (a diffuse, low-opacity Copper drop shadow) to suggest the warmth of a nearby fire.
- **Texture Overlays:** Use a subtle "grain" or "noise" overlay on primary containers to give the digital surface a paper or stone-like tactile quality.

## Shapes

The shape language is primarily **Sharp (0)**. 

Straight edges and 90-degree corners communicate stability, precision, and an architectural aesthetic. In a field often filled with soft, rounded consumer "foodie" apps, sharp corners distinguish the brand as professional and rugged. 

Exceptions:
- **Circle treatments:** Use for chef avatars or specific circular ingredients to break the monotony of the grid.
- **Subtle Rounding:** A 2px radius may be applied to small input fields or buttons if purely sharp edges interfere with tap-target affordance in mobile contexts, but the visual goal remains "precision-cut."

## Components

### Buttons
- **Primary:** Solid Copper background with Charcoal text. No border. Sharp corners.
- **Secondary:** Transparent background with a 1px Copper border. Copper text.
- **Hover States:** Primary buttons shift to a slightly brighter metallic tint; secondary buttons fill with a low-opacity copper wash.

### Cards & Containers
Containers should have no shadow. Use a 1px border (#3F3F3F) or a slight tonal shift from the background. Large imagery should be the focal point, often bleeding to the edges of the card.

### Inputs & Forms
Input fields are "Underline" style or fully framed with 1px dark borders. Use `Work Sans` for all input text. Focus states are indicated by the underline turning from gray to Copper.

### Chips & Tags
Used for "Dietary Specs" or "Terrain Type." These should be Forest Green with low-opacity backgrounds and sharp corners, using the `label-caps` typography style.

### Unique Components
- **The Expedition Timeline:** A vertical line component using the Copper color, connecting "Phase" nodes (e.g., Foraging, Preparation, Feast).
- **Texture Dividers:** Horizontal rules that aren't just lines, but subtle, high-resolution textures of slate or charred wood.