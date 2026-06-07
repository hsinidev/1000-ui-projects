---
name: Elite Viticulture Interface
colors:
  surface: '#f8f9ff'
  surface-dim: '#cfdbf0'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dde9fe'
  surface-container-highest: '#d7e3f8'
  on-surface: '#101c2b'
  on-surface-variant: '#444749'
  inverse-surface: '#253141'
  inverse-on-surface: '#eaf1ff'
  outline: '#74777a'
  outline-variant: '#c4c7c9'
  surface-tint: '#5c5f60'
  primary: '#5c5f60'
  on-primary: '#ffffff'
  primary-container: '#f7f8fa'
  on-primary-container: '#6f7274'
  inverse-primary: '#c5c7c8'
  secondary: '#515f78'
  on-secondary: '#ffffff'
  secondary-container: '#d2e0fe'
  on-secondary-container: '#55637d'
  tertiary: '#5d5e5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#f9f8f8'
  on-tertiary-container: '#717272'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e2e4'
  primary-fixed-dim: '#c5c7c8'
  on-primary-fixed: '#191c1e'
  on-primary-fixed-variant: '#444749'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#f8f9ff'
  on-background: '#101c2b'
  surface-variant: '#d7e3f8'
typography:
  display-xl:
    fontFamily: ebGaramond
    fontSize: 64px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: ebGaramond
    fontSize: 40px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: ebGaramond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  title-lg:
    fontFamily: manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
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
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style

This design system is engineered for an elite clientele of wine collectors and connoisseurs. The brand personality is **Human & Sophisticated**, striking a balance between the warmth of a personal consultation and the precision of high-end asset management.

The visual style is **Neumorphism-lite**. It evolves the soft-UI aesthetic by utilizing subtle, dual-toned shadows and gentle gradients to create "extruded" surfaces that feel tactile and premium. By prioritizing maximum white space and a restricted color palette, the interface avoids the visual clutter of traditional skuomorphism, resulting in a serene, gallery-like environment. The goal is to evoke the feeling of a private tasting room: quiet, spacious, and impeccably curated.

## Colors

The palette is anchored by **Silk White**, an off-white base that allows the soft-UI shadow effects to remain visible yet ethereal. **Navy** serves as the primary accent, used for high-level hierarchy and primary actions to ground the lighter elements with a sense of authority. **Silver** provides a secondary accent, specifically for hair-line borders and metadata labels, adding a metallic, polished finish.

The color system relies heavily on tonal variation rather than hue. Gradients should be extremely subtle, moving between the Silk White and a slightly more saturated variant to simulate light hitting a soft surface. Text utilizes the Navy at varying opacities to maintain legibility without breaking the "soft" visual ethos.

## Typography

Typography follows a classic editorial structure. **EB Garamond** is used for all major headings and display text, bringing a historical, scholarly weight to the wine expertise presented. Its serif structure is sophisticated and signals a high-end collector experience.

**Manrope** is the workhorse for body text, interface controls, and labels. It was chosen for its modern, balanced proportions that provide a clean counterpoint to the decorative serif. All labels use Manrope with increased letter-spacing and uppercase styling to ensure clarity within the soft-UI containers. Line heights are generous to preserve the "breathable" quality of the design system.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to ensure a consistent, premium feel across desktop and tablet devices. The layout is structured on a 12-column grid with wide 32px gutters, emphasizing horizontal space. 

Vertical spacing is intentionally dramatic. A section gap of 120px is standard to allow the eye to rest and to highlight individual "collections" or "advice sessions." Components are spaced using a base-8 unit, but internal padding within neumorphic cards is increased to 40px or 48px to prevent the content from feeling cramped against the soft edges.

## Elevation & Depth

Elevation in this design system is achieved through **Neumorphic-lite layering**. Instead of traditional high-contrast dropshadows, elements use two specific shadow values:
1.  **Light Shadow:** A white (#FFFFFF) shadow offset to the top-left (-8px, -8px) with a 20px blur.
2.  **Dark Shadow:** A muted blue-grey (#D1D9E6) shadow offset to the bottom-right (8px, 8px) with a 20px blur.

This creates the illusion that the UI components are extruded from the Silk White background. Surfaces should never appear "stacked" or "floating" high above the background; they should appear as if they are part of a continuous, molded material. Silver accents are used as 1px "ghost" borders on interactive elements to provide a crisp definition that neumorphism sometimes lacks.

## Shapes

The shape language is consistently soft. A **roundedness level of 2** (0.5rem base) is applied to standard inputs and small buttons, while larger containers and cards utilize the **rounded-xl** (1.5rem) setting. This curvature mimics the organic lines of glassware and decanters, reinforcing the "human" aspect of the brand. Sharp corners are strictly avoided to maintain the gentle, sophisticated tactile feel of the interface.

## Components

### Buttons & Interaction
Primary buttons are Navy with white Manrope text, featuring a subtle inner-glow to suggest a convex surface. Secondary buttons are Silk White, using the dual-shadow neumorphic technique to appear "pressed" when active.

### Cards
Cards are the primary vessel for wine labels and sommelier profiles. They feature a 1.5rem corner radius and the signature dual-shadow elevation. Imagery within cards should have a subtle 1px Silver border to separate high-resolution photography from the soft UI surface.

### Input Fields
Inputs use an "inset" shadow effect (concave) rather than an extruded one. This creates a clear visual affordance that the field is a container for data entry. The focus state is signaled by a transition to a thin Navy border.

### Chips & Tags
Used for wine regions or tasting notes (e.g., "Full-bodied," "Bordeaux"). These are flat Silver surfaces with Navy text, using a pill shape to distinguish them from the more structural rectangular cards.

### Premium Features
- **The Cellar Drawer:** A slide-out panel using backdrop-blur (glassmorphism) over the neumorphic background for managing a live cart or favorites.
- **Consultation Timeline:** A vertical silver hair-line connecting soft-UI nodes, representing the journey of a wine's aging or a consultation history.