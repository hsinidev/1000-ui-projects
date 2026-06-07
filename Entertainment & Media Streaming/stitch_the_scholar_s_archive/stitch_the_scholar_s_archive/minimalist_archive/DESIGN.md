---
name: Minimalist Archive
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#171818'
  on-primary: '#ffffff'
  primary-container: '#2c2c2c'
  on-primary-container: '#949393'
  inverse-primary: '#c8c6c5'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#181815'
  on-tertiary: '#ffffff'
  tertiary-container: '#2d2c29'
  on-tertiary-container: '#95938f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1b1c1c'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e6e2dd'
  tertiary-fixed-dim: '#c9c6c1'
  on-tertiary-fixed: '#1c1c19'
  on-tertiary-fixed-variant: '#484743'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: notoSerif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: workSans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: workSans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: workSans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  metadata:
    fontFamily: workSans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 24px
  margin: 64px
  section-gap: 120px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is built upon the "Minimalist-Archive" aesthetic, designed for a high-end documentary and educational film streaming platform. The brand personality is scholarly, authoritative, and hushed—evoking the atmosphere of a private library or a curated museum wing. It targets an intellectually curious audience that values substance, historical context, and cinematic preservation.

The visual style is a blend of **Minimalism** and **Institutional Modernism**. It prioritizes extreme clarity and spatial breathing room over decorative flourishes. The interface acts as a silent digital curator, stepping back to allow the documentary subject matter to command full attention. Every interaction is intentional, discarding the frenetic energy of typical streaming services in favor of a deliberate, archival pace.

## Colors

The palette is restricted and purposeful, utilizing a high-contrast relationship between Ivory and Charcoal to mimic the look of printed scholarly journals.

*   **Ivory (#F9F5F0):** The primary canvas. It provides a warmer, more sophisticated backdrop than pure white, suggesting aged paper or limestone gallery walls.
*   **Charcoal (#2C2C2C):** Used for primary typography, structural borders, and deep-space UI elements. It provides the "ink" that anchors the archival feel.
*   **Gold (#D4AF37):** A disciplined accent color. It is used exclusively for highlighting prestige content, active states, and markers of scholarly "excellence."
*   **Neutral Tone:** Subtle grey variations derived from the Charcoal are used sparingly for secondary metadata and disabled states to maintain the monochrome integrity.

## Typography

The typographic system utilizes a dual-engine approach to distinguish between narrative content and functional UI.

**Headings (notoSerif):** Chosen for its timeless, institutional quality. Large display sizes should feel like book titles or museum exhibition headers. Use tight tracking for larger sizes to maintain a sense of precision.

**UI & Body (workSans):** A grounded, professional sans-serif that ensures absolute legibility for film metadata, timestamps, and navigation. The "Label Caps" style is specifically intended for navigational categories and small headers, providing a crisp, architectural contrast to the fluid Serif headlines.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop viewing to mimic the structured layout of a catalog. The content container is centered with generous outer margins (64px minimum), ensuring the interface never feels crowded.

The spacing philosophy follows a "breathable museum" approach. Vertical gaps between distinct content sections (e.g., "Recently Added" vs "Curated Collections") are significantly larger than industry standards to give each film collection its own pedestal. A 12-column grid is used with wide 24px gutters, emphasizing the vertical lines and structural alignment of the UI.

## Elevation & Depth

To maintain the "Minimalist-Archive" aesthetic, traditional shadows are strictly prohibited. Depth is achieved through **Low-contrast outlines** and **Tonal Layering**.

*   **Borders:** Use 1px solid Charcoal (#2C2C2C) at varying opacities (10% to 100%) to define structural zones.
*   **Surface Tiers:** The primary background is Ivory. Secondary surfaces, such as hover states or overlay panels, should use a slightly darker "Stone" tint or a semi-transparent Charcoal wash (Archive Dark mode) to suggest stacking.
*   **Transitions:** Transitions should be "slow and cinematic"—favoring subtle fades and linear movements rather than bouncy or aggressive easing.

## Shapes

The design system uses a **Sharp (0)** roundedness level. All corners—including buttons, input fields, film posters, and modals—must have 0px radii. This creates a rigid, intentional look that reflects architectural blueprints and archival document storage. The sharp edges communicate precision, authority, and a rejection of the "softness" of contemporary consumer tech.

## Components

*   **Buttons:** Primary buttons are solid Charcoal with Ivory text. Secondary buttons are outlined with a 1px Charcoal border. All buttons use the "Label Caps" typography and have no rounded corners. Hover states trigger a subtle shift to Gold or a slight opacity change.
*   **Film Cards:** Thumbnails are sharp-edged. Metadata is positioned beneath the image using `workSans` for the title and `metadata` (italic) for the year and director. No shadows on cards; use 1px borders only if the thumbnail has a light background.
*   **Inputs:** Minimalist bottom-border only or a full 1px Charcoal frame. Labels use `label-caps` and sit outside the field. Focus states are indicated by the border color shifting to Gold.
*   **Archival Tags (Chips):** Rectangular boxes with 1px Charcoal borders. No background fill unless active. Text is small-caps.
*   **The "Curator's Note":** A unique component—a boxed area with a Gold left-border and `notoSerif` text, used for scholarly introductions to films or collections.
*   **Navigation:** A horizontal top-bar with wide letter-spacing. Active links are underlined with a 1px Gold stroke.