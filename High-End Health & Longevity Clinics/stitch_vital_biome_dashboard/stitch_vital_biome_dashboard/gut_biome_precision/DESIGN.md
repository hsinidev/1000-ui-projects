---
name: Gut-Biome Precision
colors:
  surface: '#f7fbef'
  surface-dim: '#d7dcd0'
  surface-bright: '#f7fbef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f5e9'
  surface-container: '#ebefe4'
  surface-container-high: '#e5eade'
  surface-container-highest: '#e0e4d9'
  on-surface: '#181d16'
  on-surface-variant: '#434843'
  inverse-surface: '#2d322a'
  inverse-on-surface: '#eef2e7'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#5f5e5b'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2dd'
  on-secondary-container: '#656461'
  tertiary: '#404242'
  on-tertiary: '#ffffff'
  tertiary-container: '#575959'
  on-tertiary-container: '#cfd0d0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#e5e2dd'
  secondary-fixed-dim: '#c9c6c2'
  on-secondary-fixed: '#1c1c19'
  on-secondary-fixed-variant: '#474743'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f7fbef'
  on-background: '#181d16'
  surface-variant: '#e0e4d9'
typography:
  h1:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-display:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  card-gap: 24px
  section-margin: 64px
---

## Brand & Style

This design system establishes a visual language at the intersection of biological nature and laboratory precision. The brand personality is deeply rooted in "The Scientific Sanctuary"—an environment that feels as sterile and accurate as a high-end clinic, yet as soothing and tactile as an organic garden. It targets health-conscious individuals and medical professionals who require data-driven insights without the anxiety-inducing aesthetics of traditional medical software.

The UI style utilizes a sophisticated **Soft-UI Neumorphism** approach. Rather than the harsh, high-contrast shadows of early neumorphism, this system employs subtle, multi-layered "Sand-on-Sand" extrusions. Elements appear to emerge from the background like smooth river stones or organic cellular structures. This creates a tactile, approachable interface that encourages exploration and softens the complexity of microbiome data.

## Colors

The palette is intentionally restrained to evoke a sense of calm and biological purity. 

*   **Moss Green (#4A5D4E):** Used primarily for actionable items, technical highlights, and representing "optimal health" in data visualizations.
*   **Sand (#F5F2ED):** The foundational canvas. All neumorphic "extrusions" occur on this base color, using it for both the background and the surface of the components.
*   **White (#FFFFFF):** Utilized for specular highlights on the "raised" edges of components and as a clean backdrop for specific high-density data tables.

The "Soft-UI" effect is achieved by using two distinct shadow tones: a dark shadow derived from a desaturated Moss Green to simulate depth, and a pure White highlight to simulate a light source from the top-left.

## Typography

The typography strategy in this design system balances authority with technological precision.

**Headings** utilize **EB Garamond**. This elegant serif brings a "literary" and "established" feel to the product, suggesting a foundation of deep research and clinical heritage. It should be used for all editorial content, page titles, and primary card headers.

**Technical Data and Interface Labels** utilize **Geist**. As a highly legible, mono-spaced influenced sans-serif, Geist provides the "Technical" half of the "Organic & Technical" aesthetic. It is used for microbiome metrics, percentage values, and UI controls to ensure clarity and a modern, scientific feel. All numerical data should be set in Geist to maintain a rigorous, grid-aligned appearance.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid** model. While the primary content containers conform to a 12-column grid for technical data alignment, the internal spacing relies on generous "breathable" margins to prevent a cluttered medical feel.

A rhythmic 8px scale governs all spatial relationships. Because neumorphic elements require "breathing room" for their shadows to be visible without overlapping, the system mandates a minimum of 24px (3 units) between interactive cards. This prevents the "muddy" look often associated with poorly implemented Soft-UI. Containers should use "Safe Areas" that prioritize whitespace, directing the eye toward the technical visualizations at the center of the screen.

## Elevation & Depth

Depth in this design system is communicative, not just decorative. We move away from traditional Z-axis stacking and toward "Surface Displacement."

1.  **Level 0 (The Sandbed):** The base background layer (#F5F2ED).
2.  **Level 1 (The Soft Raised):** Neumorphic cards and containers. These use a light shadow (-6px, -6px, 12px, White) and a dark shadow (6px, 6px, 12px, rgba(74, 93, 78, 0.08)).
3.  **Level 2 (The Pressed):** Used for active states of buttons or selected input fields. The shadows are reversed and set to `inset`, creating the illusion that the element has been physically pressed into the Sand surface.

Backdrop blurs are used sparingly, reserved only for "Micro-Modals" that float above the data, maintaining the organic, glass-like transparency of a microscope slide.

## Shapes

The shape language avoids perfect geometric symmetry in favor of **Biomorphic Curvature**. While the primary system uses a base `roundedness: 2` (0.5rem - 1.5rem) for standard UI elements, the "signature" components like progress rings and data nodes should utilize uneven, organic radii.

Buttons and card headers should feel like polished pebbles—smooth and inviting to the touch. In technical visualizations, the use of "blob" shapes for data clusters represents the fluid nature of the microbiome, contrasting against the rigid, straight-line precision of the Geist-based labels.

## Components

*   **Neumorphic Cards:** The primary vessel for information. They must have the same background color as the page (#F5F2ED) to achieve the Soft-UI effect. They should never have a stroke; the boundary is defined entirely by the light/dark shadow pair.
*   **Organic Progress Rings:** Instead of a perfect circular stroke, these use a variable-width "liquid" path. The Moss Green fill should animate with a slight "pulse" to indicate biological vitality.
*   **Technical Data Visualizations:** Use Moss Green for positive/healthy metrics and a muted coral or gold (secondary accents) for imbalances. Grid lines should be faint (#FFFFFF at 40% opacity) to remain clinical but unobtrusive.
*   **Pressed Buttons:** Primary actions use the Moss Green as a flat fill with a subtle white inner glow. Secondary actions use the "Sand" color with the neumorphic "Pressed" state upon interaction.
*   **Input Fields:** Designed as "wells" (inset shadows) rather than boxes. This mimics the appearance of a tray or slide holder in a lab setting.
*   **Microbiome Nodes:** Interactive data points that use a soft "Glassmorphism" blur to represent bacterial colonies, appearing as translucent, organic spheres.