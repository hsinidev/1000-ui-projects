---
name: Vitis-Vault
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#554241'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#887270'
  outline-variant: '#dbc0be'
  surface-tint: '#9b4240'
  primary: '#290002'
  on-primary: '#ffffff'
  primary-container: '#4e070c'
  on-primary-container: '#d46d6a'
  inverse-primary: '#ffb3af'
  secondary: '#5f5f56'
  on-secondary: '#ffffff'
  secondary-container: '#e2e0d5'
  on-secondary-container: '#64635a'
  tertiary: '#170e00'
  on-tertiary: '#ffffff'
  tertiary-container: '#322200'
  on-tertiary-container: '#a98742'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410005'
  on-primary-fixed-variant: '#7d2b2b'
  secondary-fixed: '#e5e2d8'
  secondary-fixed-dim: '#c9c7bc'
  on-secondary-fixed: '#1c1c15'
  on-secondary-fixed-variant: '#48473f'
  tertiary-fixed: '#ffdea5'
  tertiary-fixed-dim: '#e9c176'
  on-tertiary-fixed: '#261900'
  on-tertiary-fixed-variant: '#5d4201'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin: 40px
---

## Brand & Style

The brand personality is that of a private sommelier—expert, discreet, and deeply rooted in heritage. It targets high-net-worth collectors who view their wine cellar as both a passion project and a serious investment. The emotional response should be one of quiet confidence, security, and prestige.

This design system employs a **Tactile & Refined** style. It rejects the sterility of flat modernism in favor of a digital experience that feels like a physical heirloom. By layering subtle paper-grain textures with crisp, high-contrast typography, the UI bridges the gap between a leather-bound cellar book and a high-performance data platform. The aesthetic is anchored in "Old World" luxury, prioritizing legibility and a sense of permanence.

## Colors

The palette is derived from the lifecycle of a premier vintage. **Deep Burgundy** serves as the primary brand color, used for core navigational elements and primary actions to evoke the richness of a full-bodied red. **Parchment** provides the primary background surface, offering a warmer, more sophisticated alternative to pure white that reduces eye strain during long inventory sessions.

**Metallic Gold** is used sparingly as an accent to denote premium status, scarcity, or high-value investment alerts. The neutral palette is a collection of "Ink" tones—near-blacks and deep charcoals—to ensure that functional data and fine-print vintage details maintain absolute readability against the parchment backdrop.

## Typography

This design system utilizes a high-contrast typographic pairing to balance editorial beauty with functional utility. **Playfair Display** is the authoritative voice of the system, used for headings and bottle titles to convey elegance and history.

For functional data—such as bottle counts, vintage years, and market valuations—**Manrope** is used. Its geometric clarity ensures that dense tables and cellar maps remain legible at small sizes. All uppercase labels should utilize increased letter-spacing to maintain a sophisticated, airy feel. Tabular numerals must be used for all financial and inventory figures to ensure vertical alignment in data-rich environments.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, mirroring the structured nature of a physical wine rack. A 12-column grid system is used for the primary dashboard, with generous 40px outer margins to give the content "room to breathe," reinforcing the premium positioning.

Spacing is strictly governed by an 8px rhythmic scale. Components and sections should favor larger gaps (24px and up) to avoid a cluttered "tech-first" appearance. Information is grouped into logical "bins" or containers, ensuring that the user's eye is guided through the data in a linear, stress-free manner.

## Elevation & Depth

Hierarchy in this design system is achieved through **Tonal Layering** rather than aggressive shadows. Surfaces are stacked to mimic the layering of physical items on a desk. 

- **Level 0 (Base):** The Parchment background, textured with a subtle matte noise.
- **Level 1 (Cards/Containers):** Flat surfaces with a slightly lighter parchment tint and a 1px border in a muted gold or faint burgundy.
- **Level 2 (Modals/Popovers):** These elements feature a very soft, diffused burgundy-tinted shadow (5% opacity) and a crisp 1px Gold border to signify their active, elevated state.

Backdrop blurs should be avoided; instead, use solid overlays of Deep Burgundy at 40% opacity to bring focus to foreground elements.

## Shapes

The shape language is conservative and architectural. A **Soft** roundedness (4px) is applied to most UI elements—such as buttons, input fields, and cards—to prevent the interface from feeling sharp or aggressive, while maintaining a sense of traditional structure.

Iconography should be monolinear and elegant, with sharp corners where appropriate to match the serif typeface. Primary call-to-action buttons may use a slightly larger corner radius to signify interactability, but should never become fully pill-shaped, as that would detract from the "refined" aesthetic.

## Components

### Buttons
Primary buttons are Deep Burgundy with Gold text, using uppercase Manrope for the label. Secondary buttons use a Parchment fill with a thin Burgundy border. The "hover" state for all buttons is a subtle shift in color depth, never a dramatic change in size or shape.

### Input Fields
Inputs should resemble high-quality stationery. Use a solid Parchment background with a bottom-only border in Burgundy for a minimalist, "signed line" feel, or a full 1px border for complex forms. Labels always sit above the field in uppercase Manrope.

### Cards & Cellar Slots
Individual bottle records are housed in cards with a subtle 1px border. When a bottle is "selected," the border transitions to Metallic Gold. Use high-quality photography or stylized silhouettes of bottle shapes to represent different wine types (e.g., Bordeaux vs. Burgundy bottle shapes).

### Data Tables
Tables are the heart of the system. They feature Deep Burgundy headers with Parchment text. Rows should use alternating subtle tints or simple dividers to maintain horizontal tracking. Use "Gold" accents specifically for financial gain indicators or "Rare" status tags.

### Navigation
The side or top navigation uses a "Leather" texture overlay—a very dark, desaturated version of Burgundy—with Gold or Parchment icons to provide a tactile sense of a physical binder or ledger.