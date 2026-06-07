---
name: Sky-Sleek Luxury
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#464653'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0ef'
  outline: '#767684'
  outline-variant: '#c6c5d5'
  surface-tint: '#4b53bc'
  primary: '#00003c'
  on-primary: '#ffffff'
  primary-container: '#000080'
  on-primary-container: '#777eea'
  inverse-primary: '#bfc2ff'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#090b0c'
  on-tertiary: '#ffffff'
  tertiary-container: '#202222'
  on-tertiary-container: '#888989'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bfc2ff'
  on-primary-fixed: '#00006e'
  on-primary-fixed-variant: '#3239a3'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e5e2e1'
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
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style

The design system is engineered for the discerning long-haul traveler, evoking the serene atmosphere of a private first-class cabin. The brand personality is poised, quiet, and profoundly competent, prioritizing ease of movement and sensory indulgence. 

The aesthetic style is a refined **Minimalism** blended with **Tactile** elements. It utilizes expansive whitespace to denote luxury—suggesting that space itself is the ultimate commodity. Borders are largely eschewed in favor of subtle tonal shifts and material-inspired textures (silk, brushed metal, and fine-grain leather) to create a interface that feels physically premium.

## Colors

The palette is anchored by **Silk White**, which serves as the primary canvas to maintain a light, airy feel. **Navy Blue** provides an authoritative, "captain-class" foundation for primary actions and deep navigation elements. **Gold** is used exclusively as an accent—reserved for moments of high value, luxury markers, and premium call-to-actions.

- **Primary (Navy Blue):** Represents stability, trust, and the deep horizon.
- **Secondary (Gold):** Evokes craftsmanship, sunlight at altitude, and exclusivity.
- **Neutral (Silk White):** The core background color, providing a soft, non-reflective surface that reduces eye strain.

## Typography

This design system employs a classic typographic pairing to balance heritage with modernity. **Noto Serif** provides an editorial, high-fashion feel for headers, suggesting a history of craftsmanship. **Plus Jakarta Sans** is used for body copy and UI labels; its soft, geometric curves ensure readability and a welcoming, contemporary touch.

Hierarchy is established through generous leading and purposeful use of "Label Caps" for secondary metadata, ensuring the interface feels organized without the need for heavy structural lines.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop, centered to create a focused, boutique-like shopping experience. We utilize a 12-column grid with exceptionally wide gutters (32px) and massive page margins (64px+) to prevent the UI from feeling "crowded." 

The rhythm is dictated by a vertical spacing scale that prioritizes breathing room between sections (120px+). Components are grouped logically using "safe areas" rather than visible containers, allowing imagery to bleed into the whitespace.

## Elevation & Depth

To maintain the "Sky-Sleek" aesthetic, the design system avoids traditional heavy shadows. Instead, it utilizes **Tonal Layers** and **Ambient Shadows**. 

Depth is communicated through:
1.  **Soft Illumination:** Elements that need to appear "raised" use an ultra-diffused shadow (#000080 at 4% opacity) with a large blur radius (30px-50px), mimicking the way soft cabin lighting hits a surface.
2.  **Material Transitions:** Overlays use a subtle backdrop blur (10px) to simulate frosted glass or translucent silk, maintaining a connection to the content beneath.
3.  **Gold Outlines:** Occasionally, a 1px Gold stroke is used on white surfaces to indicate an active state or a "premium" layer, replacing the need for elevation.

## Shapes

The shape language is sophisticated and restrained. A **Soft (1)** roundedness is applied to UI elements (4px - 12px radii). This creates a subtle "hand-finished" quality that is smoother than sharp industrial edges but more serious than bubbly, highly-rounded consumer apps. Larger components like material-story cards may use a slightly increased radius (rounded-lg) to emphasize their tactile, object-like nature.

## Components

### Buttons
Primary buttons are Navy Blue with white text, featuring a 2px Gold bottom-border "accent" that appears on hover. Secondary buttons are Silk White with a delicate 1px Gold border. All buttons use the "Label-Caps" typography for a refined, formal look.

### Material Story Cards
These are the centerpiece of the system. They feature high-resolution imagery with no visible borders. The text is overlaid on the image using a gradient-fade or a "silk" translucent panel at the bottom. These cards focus on the "feel" of the leather or fabric.

### Input Fields
Inputs are minimalist, consisting only of a bottom stroke (1px) in a light grey that transitions to Gold when focused. Labels float above the line in the "Label-Caps" style.

### Refined Chips
Used for material types (e.g., "Full-Grain Leather," "Cashmere Mix"). These are Navy Blue text on a very faint Navy tint background, with no border and a subtle 4px corner radius.

### Imagery Focus
Images should be high-contrast with soft lighting. Product photography should always include a "material close-up" shot to emphasize the luxury textures defined in the brand narrative.