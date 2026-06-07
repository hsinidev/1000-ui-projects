---
name: Chrono-Atelier
colors:
  surface: '#16130b'
  surface-dim: '#16130b'
  surface-bright: '#3d392f'
  surface-container-lowest: '#110e07'
  surface-container-low: '#1f1b13'
  surface-container: '#231f17'
  surface-container-high: '#2d2a21'
  surface-container-highest: '#38342b'
  on-surface: '#eae1d4'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#eae1d4'
  inverse-on-surface: '#343027'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c4c6cc'
  on-secondary: '#2d3135'
  secondary-container: '#46494e'
  on-secondary-container: '#b6b8be'
  tertiary: '#c9cfd6'
  on-tertiary: '#2b3137'
  tertiary-container: '#adb3bb'
  on-tertiary-container: '#40464c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e0e2e8'
  secondary-fixed-dim: '#c4c6cc'
  on-secondary-fixed: '#181c20'
  on-secondary-fixed-variant: '#44474b'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#16130b'
  on-background: '#eae1d4'
  surface-variant: '#38342b'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  display-sm:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  technical-data-lg:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  technical-data-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.1em
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
  ui-label:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

The design system embodies the intersection of heritage craftsmanship and engineering precision. It targets high-net-worth collectors and horology enthusiasts who value the "soul" of a mechanical movement as much as its accuracy. The aesthetic is a sophisticated blend of **Tactile Skeuomorphism** and **Technical Minimalist**, evoking the atmosphere of a Swiss watchmaker's workshop.

The UI should feel like a physical instrument—heavy, precise, and permanent. Key visual drivers include:
- **Blueprint Precision:** Utilizing fine 0.5px and 1px lines to define boundaries, reminiscent of technical drafts.
- **Metallic Materiality:** Surfaces should mimic the luster of brushed steel and the warmth of champagne gold through subtle linear gradients.
- **Micro-textures:** Implementation of extremely fine grain and "perlage" patterns in backgrounds to reduce digital flatness.
- **Instrumental Logic:** Interactions should feel mechanical, with "snapping" transitions and weighted movement.

## Colors

The palette is anchored in a deep, nocturnal Slate and an ultra-dark background to allow the metallic tones to "shimmer" with perceived luminosity.

- **Champagne Gold (#D4AF37):** Reserved for high-value highlights, primary calls to action, and critical brand moments. Use sparingly to maintain its luxury status.
- **Brushed Steel (#8E9196):** Used for secondary UI elements, iconography, and decorative line-work. It provides a technical, cool-toned contrast to the gold.
- **Slate (#2F353B):** The primary container and structural color. It provides the "canvas" for the metallic elements.
- **Functional Accents:** Status colors (success, error) should be desaturated and "jewel-toned" to avoid clashing with the primary gold leaf aesthetic.

## Typography

The typographic hierarchy distinguishes between narrative, utility, and data.

- **Headings:** Playfair Display provides an editorial, prestigious feel. Use for storytelling and section titles. Apply "optical sizing" where possible to maintain the elegance of the serifs.
- **Technical Data:** JetBrains Mono is utilized for all numerals—prices, reference numbers, calibers, and dimensions. This reinforces the "engineered" nature of the product.
- **UI & Navigation:** Inter provides high legibility at small sizes for menus, buttons, and settings. 

On mobile devices, scale `display-lg` down to `32px` to ensure visual balance. Always use uppercase for labels and small UI headers to mimic the engravings found on watch movements.

## Layout & Spacing

The layout philosophy follows a **Precision Grid** model based on a 4px base unit. 

- **Desktop:** A 12-column fixed-width layout centered in the viewport. Wide margins emphasize the exclusivity of the content.
- **Mobile:** A 4-column fluid layout with tighter margins.
- **Rhythm:** Use generous vertical spacing (80px–120px) between sections to allow the high-end photography to breathe.
- **Dividers:** Instead of standard borders, use "Technical Rules"—thin (0.5pt) lines in Brushed Steel with 40% opacity, often terminated with a small "+" or "crosshair" symbol at intersections to mimic drafting paper.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Tonal Layering** and **Material Stacking**:

1.  **Level 0 (Base):** Deep Slate/Black with a micro-noise texture.
2.  **Level 1 (Plates):** Surfaces mimicking "Steel Plates" (#1C1F22) with a 1px top-edge highlight in Brushed Steel to simulate light catching a beveled edge.
3.  **Level 2 (Active Elements):** Use "Inner Glows" rather than outer shadows to make elements appear recessed into the interface, like components in a watch case.
4.  **Glassmorphism:** Use only for overlays (e.g., watch specs over a photo). Apply a high-density blur (20px) with a Champagne Gold tint at 5% opacity to the background filter.

## Shapes

The shape language is strictly **Sharp (0px)** or **Technical-Chamfered**. 

- Elements should be rectangular to maintain a sense of structural integrity and engineering precision.
- **Chamfers:** For buttons or special containers, use a 45-degree clipped corner (4px) instead of a radius. This mimics the machining of high-grade metal components.
- **Frames:** Use "double-line" framing for primary image assets, where a 1px Gold line sits 4px outside a 1px Steel line.

## Components

- **Primary Buttons:** Solid Champagne Gold backgrounds with Slate text. No rounded corners. On hover, apply a subtle "brushed metal" texture overlay.
- **Secondary Buttons:** Ghost style with a 1px Brushed Steel border. The text is JetBrains Mono for a more technical appearance.
- **Technical Readouts:** Use "Data Chips"—small, Slate boxes with technical specs in JetBrains Mono, featuring a 1px top-border in Gold.
- **Input Fields:** Bottom-border only (1px Steel). The label should be floating and set in Inter Bold (10px, Uppercase).
- **Cards:** No shadows. Define card boundaries using the "Technical Rules" mentioned in the Spacing section.
- **Interactive Gauges:** Custom component using precise linework to display metrics (e.g., power reserve, water resistance) mimicking watch complications.