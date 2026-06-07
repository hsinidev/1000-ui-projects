---
name: Modern-Organic System
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#424845'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#727875'
  outline-variant: '#c2c8c4'
  surface-tint: '#4e635a'
  primary: '#4e635a'
  on-primary: '#ffffff'
  primary-container: '#8da399'
  on-primary-container: '#263932'
  inverse-primary: '#b5ccc1'
  secondary: '#5f5e5a'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2dc'
  on-secondary-container: '#656460'
  tertiary: '#675d4f'
  on-tertiary: '#ffffff'
  tertiary-container: '#a99c8c'
  on-tertiary-container: '#3d3427'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#e5e2dc'
  secondary-fixed-dim: '#c9c6c1'
  on-secondary-fixed: '#1c1c18'
  on-secondary-fixed-variant: '#474743'
  tertiary-fixed: '#f0e0ce'
  tertiary-fixed-dim: '#d3c4b3'
  on-tertiary-fixed: '#221a0f'
  on-tertiary-fixed-variant: '#4f4538'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
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
  base: 8px
  container-max: 1280px
  gutter: 32px
  margin-edge: 48px
  section-gap: 120px
---

## Brand & Style

This design system is anchored in a "Modern-Organic" philosophy, blending the structured precision of high-end editorial design with the soft, tactile essence of nature. It is designed for an audience that values ethical living without sacrificing sophistication. The brand personality is serene, intentional, and culinary-forward.

The visual style is **Minimalist** with a focus on generous whitespace and "breathability." It avoids unnecessary decoration, allowing high-quality food photography to serve as the primary visual driver. The interface should evoke the feeling of a premium physical cookbook—crisp, authoritative, and timeless.

## Colors

The palette is rooted in a natural, desaturated spectrum. **Sage Green (#8DA399)** acts as the primary brand signifier, used for primary actions and key brand moments. **Bright White (#FFFFFF)** provides a clean, sterile canvas that emphasizes freshness. 

**Deep Charcoal (#2D2D2D)** provides high-contrast legibility for typography, ensuring an authoritative voice. Soft earthy accents—**Oat (#F2EFE9)** and **Stone (#C2B4A3)**—are utilized for subtle background shifts and secondary UI elements to prevent the design from feeling clinical.

## Typography

The typographic hierarchy relies on the tension between a traditional serif and a functional sans-serif. **Noto Serif** is used for headlines and editorial titles, providing a high-contrast, premium feel that mimics boutique lifestyle magazines. 

**Inter** handles all functional UI, body text, and instructional content. It is chosen for its exceptional legibility at small scales. For metadata like cook times or nutritional facts, use the "label-caps" style to create clear visual anchors within the recipes.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to maintain a disciplined, editorial structure. The layout is centered on a 12-column grid with wide 32px gutters to prevent visual clutter. 

Spacing is intentionally oversized to convey luxury. Vertical rhythm follows an 8px base unit, but section transitions should use the "section-gap" token to ensure a spacious, unhurried browsing experience. Content should be grouped logically with clear, expansive margins between disparate elements.

## Elevation & Depth

Depth in this design system is achieved through **low-contrast outlines** and **ambient shadows**. Elements do not "hover" far from the surface; instead, they feel seated within the page. 

- **Crisp Borders:** Use 1px solid borders in a lightened version of the Sage or Stone colors to define cards and containers.
- **Ambient Shadows:** Shadows must be extremely diffused (blur > 20px) and low-opacity (5-8%), using the Deep Charcoal color as the shadow base to maintain a clean, high-end look without the heaviness of standard black shadows.
- **Tonal Layering:** Use the secondary Oat color (#F2EFE9) for large background sections to create a subtle sense of depth against the primary white background.

## Shapes

The shape language is "Soft-Crisp." While the overall layout is architectural and structured, a subtle **0.25rem (4px) corner radius** is applied to buttons, input fields, and card containers. This prevents the interface from feeling sharp or aggressive, aligning it with the "organic" brand pillar. Large image containers for food photography should maintain this subtle rounding to feel like printed photographs.

## Components

### Buttons
Primary buttons use the Sage Green background with White text, using wide horizontal padding (24px+) to emphasize a premium feel. Secondary buttons use a crisp 1px Sage border with no fill.

### Cards
Recipe cards are defined by a 1px Stone border and a soft ambient shadow on hover. Content within cards must adhere to the 32px gutter for internal padding, ensuring ingredients and titles never feel cramped.

### Input Fields
Forms should be minimalist. Use a simple 1px Deep Charcoal bottom border for the "Normal" state, transitioning to a full Sage Green stroke on "Focus." Labels should always use the "label-caps" typography style.

### Chips & Tags
Used for dietary labels (e.g., "Gluten-Free," "Nut-Free"). These should have a subtle Oat background with Charcoal text and no border, keeping them secondary to the main recipe titles.

### Ingredient Lists
Lists should utilize generous line height (1.8) and subtle dividers. Use a custom checkbox design that is a simple Sage circle with a charcoal checkmark to maintain the organic aesthetic.