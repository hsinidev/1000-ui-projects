---
name: Lux-Hive
colors:
  surface: '#181309'
  surface-dim: '#181309'
  surface-bright: '#3f382d'
  surface-container-lowest: '#130d05'
  surface-container-low: '#211b11'
  surface-container: '#251f14'
  surface-container-high: '#30291e'
  surface-container-highest: '#3b3428'
  on-surface: '#ede1d0'
  on-surface-variant: '#d5c4ab'
  inverse-surface: '#ede1d0'
  inverse-on-surface: '#362f24'
  outline: '#9e8f78'
  outline-variant: '#514532'
  surface-tint: '#ffba20'
  primary: '#ffdca1'
  on-primary: '#412d00'
  primary-container: '#ffb800'
  on-primary-container: '#6b4c00'
  inverse-primary: '#7c5800'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#abebff'
  on-tertiary: '#003641'
  tertiary-container: '#00d7fe'
  on-tertiary-container: '#005a6b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdea8'
  primary-fixed-dim: '#ffba20'
  on-primary-fixed: '#271900'
  on-primary-fixed-variant: '#5e4200'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#b0ecff'
  tertiary-fixed-dim: '#17d8ff'
  on-tertiary-fixed: '#001f27'
  on-tertiary-fixed-variant: '#004e5d'
  background: '#181309'
  on-background: '#ede1d0'
  surface-variant: '#3b3428'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
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
  data-ui:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system embodies the intersection of ancestral heritage and cutting-edge apiculture technology. Designed for the discerning estate owner, the visual direction—**Golden & Refined**—evokes the prestige of a private library combined with the precision of a scientific laboratory. 

The aesthetic is **Minimalist-Tactile**. It utilizes a dark, sophisticated backdrop to allow the biological data of the hives to glow with importance. By blending high-contrast digital elements with organic, parchment-like textures, the interface feels less like a utility and more like a curated legacy asset. The emotional response should be one of quiet confidence, environmental stewardship, and absolute control over a delicate natural process.

## Colors

The palette is rooted in the "Golden Hour" of a thriving estate. 

- **Deep Charcoal (#1A1A1A)** serves as the primary canvas, providing a velvet-like depth that reduces eye strain and establishes a premium "Dark Mode" foundation.
- **Rich Parchment (#F5F2E8)** is used for content surfaces and cards. It provides a tactile, organic contrast to the digital surroundings, mimicking high-quality heavy-stock paper.
- **Amber Glow (#FFB800)** is the pulse of the system. It is reserved for active states, critical data highlights, and interactive "glow" effects that simulate sunlight passing through honey.
- **Honey Gold (#D4AF37)** functions as the success state, offering a more muted, metallic alternative to standard greens to maintain the high-end aesthetic.

## Typography

The typography strategy employs a "High-Contrast Pairing" to signal both tradition and technology.

**Playfair Display** is used for all major headings. Its high-contrast serifs and elegant terminals provide a sense of editorial prestige and historical weight. It should be used with generous leading to maintain a sense of "breathable" luxury.

**Inter** is the workhorse for all functional UI elements, data readouts, and body text. Chosen for its exceptional legibility on small screens and technical neutrality, it ensures that hive vitals (temperature, humidity, weight) are parsed with zero ambiguity. Use the "Label-Caps" style for all technical categories and metadata tags to create a sharp, architectural hierarchy.

## Layout & Spacing

This design system utilizes a **Fixed-Width Centered Grid** for desktop (12 columns) and a **Fluid Grid** for mobile devices. The rhythm is governed by an 8px base unit, ensuring mathematical harmony across all components.

Layouts should favor asymmetry and generous negative space to avoid a "cluttered" dashboard feel. Content areas are structured using "Parchment Containers" that often utilize a hexagonal clipping mask or subtle hexagonal corner treatments. Margins are intentionally wide (32px+) to frame the content like a piece of fine art, reinforcing the "estate" nature of the product.

## Elevation & Depth

Hierarchy is established through a combination of **Tonal Layering** and **Organic Shadows**.

1.  **Level 0 (Floor):** Deep Charcoal (#1A1A1A) background. This is the infinite base layer.
2.  **Level 1 (Sub-surface):** Subtle hexagonal grid patterns rendered in 5% opacity Amber Glow, appearing as if etched into the charcoal.
3.  **Level 2 (Cards):** Rich Parchment (#F5F2E8) surfaces. These use a "Soft Diffusion" shadow—a multi-layered shadow with a wide blur (30px+) and very low opacity (10%) to make them appear as if they are resting lightly on the dark base.
4.  **Level 3 (Interactive):** Elements that are hovered or active emit an "Inner Glow" using the Primary Amber color, simulating the warmth of a hive's internal heat.

## Shapes

The shape language is primarily **Geometric & Architectural**. While the general roundedness is "Soft" (4px - 8px), the defining characteristic is the **Hexagonal Motif**. 

Use subtle 120-degree angles for corner treatments of parchment cards rather than standard radii where possible. Buttons should remain strictly rectangular or use very slight rounding to maintain a formal, bespoke feel. Icons are housed in thin-stroke gold hexagonal frames to unify the biological subject matter with the digital interface.

## Components

### Buttons & Interaction
Buttons are high-contrast elements. The primary action button is a solid Deep Charcoal block with Amber Glow text and a 1px Amber border. On hover, the button develops a subtle outer glow. Secondary buttons use "Ghost" styling with thin Gold (#D4AF37) strokes.

### Parchment Cards
Cards serve as the primary container for hive data. They should include a very subtle, low-opacity grain texture to simulate organic paper. Borders are either non-existent (relying on the soft shadow) or a very thin 0.5px Charcoal line at 10% opacity.

### Data Visualization
Charts should use the Amber Glow (#FFB800) for primary data lines. The area under the curve should use a soft Amber gradient that fades into the Parchment background. Avoid standard "web-safe" colors; use Honey Gold for success and a deep, muted Ochre for warnings.

### Iconography
Icons must be "Monoline Gold." Use a consistent 1.5pt stroke weight with open terminals. Icons should be simplified representations of beekeeping tools, bees, and environmental factors (sun, wind, rain), all rendered in the Honey Gold (#D4AF37) palette.

### Specialized Components
- **Hive Vital Gauges:** Semi-circular or hexagonal meters that use the Amber Glow for the progress fill.
- **Honey Level Indicator:** A vertical cylinder component that uses a liquid-motion animation to represent current hive weight/honey yield.
- **Estate Map:** A custom-styled Mapbox or SVG layer using the Charcoal/Gold palette, stripped of all standard public labels to focus on hive locations.