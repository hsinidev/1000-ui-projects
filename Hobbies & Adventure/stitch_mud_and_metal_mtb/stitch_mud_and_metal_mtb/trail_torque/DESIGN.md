---
name: Trail & Torque
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#becab7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#899483'
  outline-variant: '#3f4a3b'
  surface-tint: '#77dd6a'
  primary: '#77dd6a'
  on-primary: '#003a03'
  primary-container: '#3fa539'
  on-primary-container: '#003202'
  inverse-primary: '#006e0c'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#e5bfa3'
  on-tertiary: '#432b17'
  tertiary-container: '#ac8a70'
  on-tertiary-container: '#3b2511'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#92fa83'
  primary-fixed-dim: '#77dd6a'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#005307'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#e5bfa3'
  on-tertiary-fixed: '#2b1705'
  on-tertiary-fixed-variant: '#5b412c'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1280px
---

## Brand & Style

This design system is built on a "Mud-and-Metal" philosophy, blending the raw, visceral energy of mountain biking with the precision of high-end mechanical engineering. The brand personality is rugged, resilient, and unapologetically functional. It targets thrill-seekers and technical enthusiasts who value the gear as much as the trail.

The visual style is a hybrid of **Tactile Industrialism** and **High-Contrast Brutalism**. It utilizes physical metaphors—brushed aluminum, weathered steel, and organic grit—to ground the digital experience in the physical world. The UI should feel like a piece of well-maintained equipment: heavy, durable, and ready for extreme conditions. High-contrast transitions and raw textures replace traditional clean gradients to evoke a sense of adrenaline and outdoor authenticity.

## Colors

The palette is anchored in a deep, nocturnal environment to make the metallic and organic accents pop.

*   **Primary (Forest Green - #228B22):** Used for primary actions, success states, and indicating "the trail." It should feel vibrant but rooted.
*   **Secondary (Metallic Silver - #C0C0C0):** Represents the "Metal." Used for headers, icons, and structural borders. It should often be paired with a brushed texture overlay.
*   **Tertiary (Mud Brown - #634832):** An accent color used for secondary highlights, hover states, and "worn" elements.
*   **Neutral (Charcoal & Ink):** The background is a layered charcoal (#1A1A1A), providing a high-contrast foundation that mimics asphalt and dark earth.

Apply "mud splatter" masks (using #634832 at 20-40% opacity) sparingly in the background corners to break the digital perfection of the layout.

## Typography

This design system utilizes a high-tension typographic pairing. 

**Headings** use a bold, technical grotesque that feels machined and precise. Large display headers should be set with tight tracking to mimic the weight of heavy machinery. **Body text** utilizes a highly legible, athletic sans-serif to ensure readability during high-activity scenarios or low-light outdoor viewing. 

All navigational elements and small labels should be set in uppercase with increased letter spacing to maintain a functional, "instructional manual" aesthetic.

## Layout & Spacing

The layout follows a **12-column fixed grid** with generous gutters to allow the rugged textures room to breathe. The spacing rhythm is strictly mathematical, based on an 8px base unit, reinforcing the industrial theme.

Content blocks should feel modular and "bolted" together. Use asymmetric compositions for hero sections to simulate the unpredictability of a mountain trail, while keeping functional booking and technical data within a rigid, structured grid.

## Elevation & Depth

Depth in this design system is achieved through **Material Layering** rather than traditional shadows. 

1.  **Base Layer:** Charcoal gray (#1A1A1A) with a faint noise texture.
2.  **Surface Layer:** Secondary containers use a slightly lighter gray (#2A2A2A) with 1px solid metallic borders.
3.  **Active Layer:** Elements meant to be interacted with use a "Brushed Metal" effect—a linear gradient of Metallic Silver (#C0C0C0 to #8E8E8E) at a 45-degree angle.

Avoid soft, ambient shadows. Instead, use "Hard Drops"—offset 2px or 4px solid black shadows—to give components a physical, stamped-out appearance.

## Shapes

The shape language is strictly **Sharp (0)**. 

To evoke the feel of industrial components and trail gear, all buttons, cards, and input fields must have 0px border radii. This reinforces the "Metal" aspect of the aesthetic, suggesting precision-cut steel. For decorative elements, use 45-degree clipped corners (chamfers) rather than curves to denote a rugged, technical build.

## Components

*   **Buttons:** Primary buttons are solid Forest Green with black, bold uppercase text. They feature a 1px inner border in a lighter green to simulate a beveled edge. Hover states shift the background to Mud Brown.
*   **Cards:** Use a "Metal Plate" style. Dark charcoal background, 1px Silver border, and visible "screw" icons (small circles) in the four corners for decorative high-fidelity.
*   **Inputs:** Fields should have a thick 2px bottom border in Metallic Silver. When focused, the border glows in Forest Green.
*   **Chips/Tags:** Small, rectangular boxes with high-contrast backgrounds. Use Mud Brown for "Difficulty" levels and Forest Green for "Status."
*   **Progress Bars:** Designed to look like mechanical gauges or tire treads. Use a segmented bar instead of a continuous fill.
*   **Specialty Component - "Trail Status":** A custom indicator using an icon of a mountain with a textured "splatter" overlay that changes density based on trail conditions (dry to muddy).