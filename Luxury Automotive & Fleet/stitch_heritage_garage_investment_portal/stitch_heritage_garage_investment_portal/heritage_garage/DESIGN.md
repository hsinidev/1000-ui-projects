---
name: Heritage Garage
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#404942'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
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
  tertiary: '#232415'
  on-tertiary: '#ffffff'
  tertiary-container: '#383a29'
  on-tertiary-container: '#a3a48d'
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
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 3rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 2rem
    fontWeight: '500'
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1'
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
  gutter: 32px
  margin-edge: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style
The brand personality is grounded in the prestige of automotive history and the meticulous nature of high-value investments. This design system evokes an emotional response of security, legacy, and tactile luxury—akin to opening a leather-bound logbook or stepping into a private showroom.

The design style is a blend of **Tactile Minimalism** and **Editorial Elegance**. It avoids the sterility of modern corporate tech, opting instead for a physical presence through subtle textures and precise line work. Every interface element should feel like a deliberate craft, emphasizing the "archival" nature of the service through spacious layouts and high-end photography that mimics film-stock quality.

## Colors
The palette is rooted in the "British Racing Green" tradition, paired with the warmth of mid-century leather interiors. 

- **Racing Green (#004225):** Used for primary actions, deep backgrounds, and brand signifiers. It represents stability and prestige.
- **Tan Leather (#A67B5B):** Used for secondary accents, interactive highlights, and decorative borders. It adds a human, tactile warmth.
- **Parchment (#F5F5DC):** The primary canvas color. It replaces pure white to reduce ocular strain and reinforce the archival, vintage paper aesthetic.
- **Neutral (#1A1A1A):** A "Carbon Black" used for body text and high-contrast structural elements.

## Typography
This design system utilizes a traditional typographic hierarchy to establish authority. **Noto Serif** provides the timeless, literary feel required for headlines, suggesting a history of expertise. 

**Work Sans** is selected for body copy and data-heavy interfaces due to its exceptional legibility and professional, grounded character. It balances the "old world" serif with "new world" precision. Use `label-caps` for all metadata, small navigation items, and overlines to evoke the feel of stamped engineering plates.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy with generous margins to mimic the layout of high-end lifestyle magazines. 

A 12-column grid is used for desktop, but the layout should prioritize "The Golden Gap"—ample whitespace (stack-lg) between sections to allow photography to breathe. Elements are often centered or offset in an asymmetrical "editorial" style. Content should never feel crowded; the spacing rhythm is intentional and slow, guiding the user through the restoration narrative or investment data without urgency.

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layering** and **Subtle Textures** rather than heavy shadows.

- **Surface Tiers:** Use slight variations of the Parchment color and Tan Leather to stack elements. 
- **Shadows:** When necessary, use extremely diffused, low-opacity "Ambient Shadows" (0% - 5% opacity) with a slight Tan tint to make cards feel like they are resting on paper.
- **Dividers:** Use thin (1px) solid lines in Tan Leather or a 10% opacity Racing Green to separate content.
- **Texture:** Apply a very fine noise or grain overlay to the Parchment background to simulate vintage paper stock.

## Shapes
The shape language is **Soft (0.25rem)**. This provides just enough curvature to feel sophisticated and finished without becoming "bubbly" or overly modern. 

- **Buttons & Inputs:** Use the base `rounded` (4px) setting.
- **Imagery:** Large archival photos should remain sharp (0px) to look like traditional printed photographs, or use a very slight corner radius (2px) to mimic a physical photo print.
- **Dividers:** Use hairline strokes for a "draftsman" or "blueprinted" feel.

## Components
- **Buttons:** Primary buttons use Racing Green with Parchment text. Secondary buttons are outlined in Tan Leather with Tan text. Avoid gradients. Use a "Pressed" state that slightly shifts the color to a deeper shade of the background.
- **Cards:** Cards should have a 1px Tan Leather border and no shadow. The header of the card should use the `label-caps` typography style.
- **Input Fields:** Use a traditional "underlined" style or a fully bordered box with the Parchment background. Labels should always be visible (never floating).
- **Chips/Badges:** Use Racing Green backgrounds with Parchment text for status indicators (e.g., "In Restoration," "Sold").
- **Lists:** Use elegant, serif-driven list items with Tan Leather bullet points or icons.
- **Specialty Component - The Specification Table:** A clean, 2-column data grid with horizontal dividers only, used for car specs (Chassis #, Engine, Mileage), utilizing `Work Sans` for precision.