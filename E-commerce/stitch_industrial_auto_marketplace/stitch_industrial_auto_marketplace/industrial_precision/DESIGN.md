---
name: Industrial Precision
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
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#f9f5f5'
  on-tertiary: '#313030'
  tertiary-container: '#dcd9d9'
  on-tertiary-container: '#605f5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
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
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  code-data:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1440px
  gutter: 16px
  sidebar-width: 320px
---

## Brand & Style

This design system is engineered for the high-performance car parts marketplace, evoking an atmosphere of mechanical reliability and technical expertise. The brand personality is utilitarian, precise, and authoritative, targeting professional mechanics and automotive enthusiasts who prioritize functional accuracy over decorative flair.

The design style leans heavily into **Brutalism** and **High-Contrast** aesthetics, utilizing sharp edges and structural grids to mimic technical blueprints and workshop manuals. It incorporates subtle metallic gradients and micro-textures to provide a tactile, industrial feel without sacrificing digital clarity. The UI communicates "Fitment Guaranteed" through a rigid visual hierarchy that feels as solid as the hardware it lists.

## Colors

The palette is anchored in a high-contrast dark mode to reduce eye strain in workshop environments and highlight critical technical data. 

- **Deep Charcoal/Black (#121212):** Used for the primary interface structure and background layers to provide maximum depth.
- **Metallic Silver (#C0C0C0):** Applied to borders, secondary surfaces, and inactive states to simulate aluminum or steel components.
- **Cyber Yellow (#FFD700):** Reserved for primary calls to action, urgent compatibility alerts, and critical navigation paths.
- **Fitment Green (#39FF14):** A high-visibility neon green used exclusively for the 'Fitment Guarantee' badge and successful system validations.

## Typography

This design system utilizes a pairing of **Space Grotesk** for headlines and **Inter** for functional data. 

Space Grotesk provides a geometric, technical edge to headers, mimicking the aesthetics of industrial signage. Inter is used for body copy and technical specifications to ensure maximum readability across varying screen qualities. Heavy use of uppercase labels and monospaced-style tracking for part numbers and SKU data reinforces the utilitarian nature of the marketplace.

## Layout & Spacing

The design system employs a **Fixed Grid** model on desktop and a high-density fluid model on mobile. A 12-column grid is used for the main content area, with a permanent 320px sidebar for "Robust Filters" on catalog pages.

Spacing follows a strict 4px base unit to maintain a "tight" technical feel. Large gutters are avoided; instead, 1px Silver borders are used to separate functional zones, creating a dense, information-rich environment reminiscent of a diagnostic tool.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Bold Borders** rather than traditional soft shadows. 

1. **Base:** Deep Charcoal (#121212) for the canvas.
2. **Surface:** Metallic Silver (#C0C0C0) at 5-10% opacity with a 1px solid border at 30% opacity to define cards and containers.
3. **Active:** Cyber Yellow (#FFD700) or pure Silver for elements that require focus.

Subtle linear gradients (top-left to bottom-right) are applied to primary containers to simulate the sheen of brushed metal. No blur effects or ambient shadows are permitted, ensuring the UI feels "flat-packed" and solid.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. Every component—from buttons to input fields and image containers—must feature 90-degree corners. This reinforces the industrial, machined aesthetic of car parts and hardware. Any deviation to rounded corners is strictly prohibited as it softens the technical authority of the interface.

## Components

- **Buttons:** Primary buttons use Cyber Yellow background with Black text. Hover states shift to a metallic gradient. Secondary buttons use a Silver border with no fill. All buttons use uppercase typography.
- **Fitment Badges:** High-visibility rectangular tags. 'Guaranteed Fit' uses a dual-tone Cyber Yellow/Green split with a "Checkmark" icon.
- **Robust Filters:** Accordion-style sidebars using 'Code-Data' typography. Active filters are highlighted with a vertical Cyber Yellow stripe on the left edge.
- **Input Fields:** Dark background with a persistent 1px Metallic Silver border. On focus, the border glows Cyber Yellow with no outer shadow.
- **Video Player:** Integrated technical player for "Install Guides." Features a custom Silver scrub bar and Cyber Yellow play icons, framed in a high-contrast border.
- **Technical Icons:** Monolinear, 2px stroke width, strictly geometric. Icons should look like CAD drawings or simplified patent illustrations.
- **Data Tables:** Zebra-striping using Deep Charcoal and Neutral levels. Headers are pinned and styled in 'Label-Caps'.