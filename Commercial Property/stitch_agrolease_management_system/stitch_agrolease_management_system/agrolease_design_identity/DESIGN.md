---
name: AgroLease Design Identity
colors:
  surface: '#fafaec'
  surface-dim: '#dadbcd'
  surface-bright: '#fafaec'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4e7'
  surface-container: '#eeefe1'
  surface-container-high: '#e9e9db'
  surface-container-highest: '#e3e3d6'
  on-surface: '#1a1c14'
  on-surface-variant: '#414844'
  inverse-surface: '#2f3128'
  inverse-on-surface: '#f1f2e4'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#262621'
  on-tertiary: '#ffffff'
  tertiary-container: '#3c3c36'
  on-tertiary-container: '#a8a69e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#e5e2da'
  tertiary-fixed-dim: '#c9c6be'
  on-tertiary-fixed: '#1c1c17'
  on-tertiary-fixed-variant: '#474741'
  background: '#fafaec'
  on-background: '#1a1c14'
  surface-variant: '#e3e3d6'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
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
  margin-edge: 48px
  container-max: 1440px
---

## Brand & Style

The design system is built upon a "Legacy-Modern" framework, merging the heritage of agricultural land ownership with the precision of contemporary GIS and financial technology. The personality is authoritative and institutional, aiming to evoke the same level of trust as a multi-generational land deed.

The visual style leans into a refined **Corporate / Modern** aesthetic, utilizing high-density information layouts balanced by vast "Parchment" white space to ensure legibility. We use high-resolution drone photography not just as decoration, but as primary data sources, framing them within structured containers that suggest order and stewardship. The emotional response should be one of stability, permanence, and professional capability.

## Colors

The palette is derived from the natural environment of large-scale farming. 
- **Primary (Forest Green):** A deep, saturated green used for primary actions, navigation headers, and signifying growth and health. 
- **Secondary (Earthy Brown):** Used for accents, borders of land-based data modules, and specific UI status indicators related to soil or foundation.
- **Background (Parchment):** A warm, off-white tactile base that reduces eye strain during long data-entry sessions and differentiates the product from sterile white SaaS competitors.
- **Neutral:** A dark olive-grey used for high-contrast text and iconography to maintain a grounded feel.

## Typography

The typographic strategy balances editorial tradition with institutional clarity. 
- **Headings:** We utilize **Newsreader** for all top-level headings. Its serif structure conveys a literary and legal authority, essential for high-value leasing contracts.
- **UI & Data:** **Public Sans** is used for all functional elements, data tables, and GIS overlays. Its neutral, "institutional" character ensures that complex agricultural metrics remain highly legible and objective. 
- **Data Visualization:** Use the 'data-mono' weight for coordinates, acreage figures, and financial values to provide a rhythmic, tabular appearance.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop experiences to maintain a sense of structured "ledger" layouts. The primary container is a 12-column grid with a generous 24px gutter, allowing for complex data visualizations to sit side-by-side with map interfaces.

Spacing follows a strict 8px base unit. Larger vertical gaps (64px+) should be used between major content sections to allow the Parchment background to "breathe," reinforcing a premium, unhurried user experience. For GIS components, the layout should switch to a full-bleed edge-to-edge view, anchored by a floating sidebar for controls.

## Elevation & Depth

To maintain a grounded feel, this design system avoids floating effects. Instead, it uses **Tonal Layers** and **Low-contrast Outlines**. 

- **Surfaces:** Depth is created by stacking Parchment shades. The base layer is the warmest, while active cards or modals use a slightly brighter, "cleaner" version of the surface color.
- **Borders:** We prioritize 1px solid borders in a muted Earthy Brown (at 20% opacity) over shadows. 
- **Shadows:** When necessary (e.g., for global navigation or high-priority modals), use a "Soil Shadow"—a very soft, diffused brown-tinted shadow with a large blur (20px+) and very low opacity (10%), suggesting the element is resting gently on the surface rather than hovering high above it.

## Shapes

The shape language is **Soft**. We use a 0.25rem (4px) base radius for buttons and input fields. This provides a subtle nod to modern UI expectations while maintaining the crispness of a professional document. 

Large containers, such as land-detail cards or map overlays, use a slightly larger radius (8px) to soften the overall interface. Interactive GIS map markers should remain circular to stand out against the geometric grid of the farmland photography.

## Components

- **Buttons:** Primary buttons are solid Forest Green with Parchment text. Secondary buttons use a Forest Green outline with a subtle Earthy Brown hover state.
- **Cards:** Cards should have no shadow by default, utilizing a 1px Earthy Brown border. Header areas within cards should have a subtle parchment-tinted background to separate metadata from content.
- **Input Fields:** Use "filled" style inputs where the background is a 5% darker shade of Parchment, with a bottom-border only, mimicking traditional ledger lines.
- **GIS Overlays:** Controls for map layers should be semi-transparent Parchment with high-contrast neutral icons. Use a "Glassmorphism" effect specifically for map-based HUDs to ensure the drone photography remains visible beneath the UI.
- **Data Visualization:** Charts should use a palette of Sage, Clay, and Slate to ensure they feel part of the natural environment rather than neon-digital.
- **Chips/Status:** Use muted, earthy tones for status (e.g., "Leased" in Forest Green, "Available" in a soft Moss, "Pending" in Clay).