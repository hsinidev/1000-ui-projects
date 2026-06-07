---
name: Equestrian Heritage Elite
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#404942'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#717971'
  outline-variant: '#c0c9c0'
  surface-tint: '#316948'
  primary: '#002a15'
  on-primary: '#ffffff'
  primary-container: '#004225'
  on-primary-container: '#75af89'
  inverse-primary: '#98d4ac'
  secondary: '#7c5639'
  on-secondary: '#ffffff'
  secondary-container: '#fecaa5'
  on-secondary-container: '#795336'
  tertiary: '#6a5f00'
  on-tertiary: '#ffffff'
  tertiary-container: '#bbac47'
  on-tertiary-container: '#484000'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b4f0c7'
  primary-fixed-dim: '#98d4ac'
  on-primary-fixed: '#002110'
  on-primary-fixed-variant: '#165132'
  secondary-fixed: '#ffdcc4'
  secondary-fixed-dim: '#efbc98'
  on-secondary-fixed: '#2f1501'
  on-secondary-fixed-variant: '#613f24'
  tertiary-fixed: '#f5e479'
  tertiary-fixed-dim: '#d8c860'
  on-tertiary-fixed: '#201c00'
  on-tertiary-fixed-variant: '#504700'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Newsreader
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
  label-caps:
    fontFamily: Work Sans
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 40px
  section-gap: 64px
---

## Brand & Style

This design system embodies the "Equestrian Heritage" aesthetic, blending the prestige of elite horse racing with the precision of modern performance management. The brand personality is authoritative and reliable, designed for an elite clientele that values tradition as much as data-driven results.

The visual style is **Tactile / Skeuomorphic** refined through a lens of modern luxury. It avoids the clutter of old-school skeuomorphism in favor of high-end textures—specifically pebble-grain leather and brushed brass—used as strategic accents. The layout is highly structured and symmetrical, evoking the feeling of a bespoke leather-bound ledger or a private clubhouse interior. The UI should feel grounded, established, and permanent.

## Colors

The palette is rooted in the "Deep Racing Green," which serves as the primary anchor for headers, primary actions, and status indicators. "Tan Leather" is used for secondary accents, interactive states, and containers that require a tactile feel. "Metallic Brass" is reserved for high-level emphasis, decorative dividers, and "Elite" status tiers.

The background uses a "Parchment" neutral (#F9F7F2) rather than a pure white to maintain the heritage feel. Accessibility is maintained by using the Racing Green for all primary text against the parchment background.

## Typography

This design system utilizes **Newsreader** for all editorial and heading elements to convey a sense of literary authority and historical weight. Headlines should be set with tighter letter spacing to maintain a premium, customized look.

For functional UI components and dense data management, **Work Sans** provides a neutral, highly legible contrast. Small labels and metadata should frequently use the `label-caps` style to mimic the stamping found on high-end leather goods.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, centering content within a sophisticated 12-column structure. Generous margins and section gaps ensure the UI never feels crowded, reflecting the "Elite" nature of the product. 

Symmetry is paramount. Components should be aligned to a strict 8px baseline grid. Data-heavy views should utilize "Horse Cards" that span 3 or 4 columns, while performance analytics occupy wider 8-column or 12-column containers.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and physical metaphors rather than standard drop shadows. 
- **The Base:** The Parchment background (#F9F7F2).
- **The Surface:** Containers use a subtle, 1px "Tan Leather" border or a very soft, inner-glow effect to suggest indentation.
- **Floating Elements:** Only primary modals or global navigation bars use elevation, expressed via "Deep Racing Green" tinted shadows (0px 10px 30px rgba(0, 66, 37, 0.08)) to maintain a sophisticated, heavy feel.
- **Dividers:** Use 1px linear gradients of "Metallic Brass" to separate content sections, mimicking a thin metal inlay.

## Shapes

The shape language is conservative and disciplined. A **Soft (0.25rem)** corner radius is applied to standard buttons and input fields to mimic the subtle softening of leather edges over time. Larger containers like cards may use a slightly more pronounced corner, but they should never approach "circular" or "pill" shapes, which feel too casual for this heritage brand.

## Components

- **Buttons:** Primary buttons are "Deep Racing Green" with "Metallic Brass" text. They feature a subtle 1px top-highlight to give a slightly embossed appearance. Secondary buttons use a "Tan Leather" outline.
- **Inputs:** Text fields use the Parchment background with a bottom-only border in "Tan Leather," mimicking traditional stationery. Focus states transition the border to "Metallic Brass."
- **Cards:** Profile cards for horses should feature a "Tan Leather" header strip (simulating a saddle tag) with the horse's name in Newsreader.
- **Dividers:** Horizontal rules are not gray; they are thin, brushed-brass lines (#B5A642) that fade at the edges.
- **Chips/Badges:** Status chips (e.g., "In Training," "Recovering") use Racing Green text on a very desaturated version of the Tan Leather background, looking like stitched patches.
- **Specialty Component - The "Stitch Line":** A decorative 1px dashed line used sparingly to separate vertical segments of a data table, evoking leather stitching.