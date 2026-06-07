---
name: Industrial Brutalism
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#333535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#c7c6c6'
  on-secondary: '#303031'
  secondary-container: '#464747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#f6f6f6'
  on-tertiary: '#303030'
  tertiary-container: '#dadada'
  on-tertiary-container: '#5f5f5f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
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
  label-bold:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
  border-thick: 4px
  border-thin: 1px
---

## Brand & Style

This design system is built on the principles of **Raw Brutalism**, mirroring the structural integrity and unyielding nature of concrete construction. It rejects superficial softness in favor of transparency, strength, and heavy-duty performance. 

The visual language communicates authority and physical presence through high-contrast intersections of yellow, grey, and black. It is designed to evoke a sense of reliability and "work-site" professionalism, ensuring that information feels as solid and permanent as a foundation. The target audience—architects, site managers, and commercial developers—will experience a UI that prioritizes clarity, structural hierarchy, and industrial utility over decorative trends.

## Colors

The palette is derived directly from the construction environment. **Construction Yellow (#FFD700)** is the primary action color, used sparingly but aggressively to draw attention to critical interactions and safety-critical data. **Concrete Grey (#808080)** serves as the primary structural background, providing a neutral, industrial canvas.

**Deep Black (#000000)** is utilized for high-contrast borders and heavy typography, creating a "blueprint" feel. The design system defaults to a dark/industrial mode where the background transitions between deep greys and blacks to minimize eye strain in high-glare outdoor environments while maintaining a gritty, professional aesthetic.

## Typography

Typography in this design system is treated as a structural element. Headlines utilize **Noto Serif** at maximum weight to simulate the impact of a slab-serif, providing a heavy, authoritative presence that anchors the page. 

For body copy and functional data, **Public Sans** provides a neutral, institutional clarity. It is a utilitarian typeface that ensures legibility across technical specifications and project manifests. All labels and secondary metadata should be rendered in uppercase with increased letter spacing to mimic industrial stamping and signage.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** system that emphasizes rigid containment. The structure uses a 12-column grid with 24px gutters, where every element is bounded by visible, thick black borders. 

Spacing follows a strict 4px baseline rhythm. Padding within containers should be generous to contrast with the "heavy" weight of the borders, preventing the UI from feeling cramped. Content modules are stacked vertically like pre-cast concrete slabs, using 40px margins to separate major sections.

## Elevation & Depth

This design system avoids soft shadows and organic depth. Instead, it uses **Bold Borders** and high-contrast stacking to communicate hierarchy. 

Depth is achieved through "Hard Shadows"—solid black offsets (e.g., 4px x 4px) with 100% opacity—that give components a physical, extruded appearance. Backgrounds should incorporate subtle concrete textures and hatch-mark patterns (45-degree industrial stripes) to differentiate between the base layer and interactive surfaces. Diamond plate textures are reserved for header backgrounds or heavy-duty card states.

## Shapes

The shape language is strictly **Sharp (0px)**. In the world of concrete and foundation work, there are no rounded corners—only clean breaks and structural angles. 

All buttons, input fields, cards, and containers must have 90-degree corners. This reinforces the raw, unrefined brutalist aesthetic and ensures that the UI feels engineered rather than "designed." Decorative elements such as "notched" corners or diagonal cuts (reminiscent of industrial chamfers) are permitted for high-level branding elements.

## Components

### Buttons
Primary buttons are high-visibility **Construction Yellow** with **Deep Black** text. They feature a 4px solid black border and a solid black hard-offset shadow that disappears on "active" states to simulate a physical press. Secondary buttons use a transparent background with a thick black border.

### Input Fields
Inputs are rendered as stark white or light grey rectangular blocks with 2px black borders. Labels must always be positioned above the field in uppercase bold **Public Sans**. Focus states switch the border to yellow with a subtle hatch-mark pattern inside the field.

### Cards & Containers
Cards represent individual concrete slabs. They must have a 4px solid black border. Use a subtle concrete grain texture for the card background to add grit. Header areas of cards should be separated by a 2px horizontal rule.

### Lists & Specifications
Data lists should mimic industrial shipping manifests. Use alternating row colors (Concrete Grey and a slightly lighter tint) and separate them with 1px black lines.

### Additional Components
- **Progress Bars:** Represented as "filling" a concrete form, using a yellow hatch-mark pattern for the fill.
- **Status Chips:** High-contrast tags with solid black backgrounds and yellow text for "Warning" or "Active" states.
- **Section Dividers:** 8px thick black lines or 45-degree "Caution" striped bars.