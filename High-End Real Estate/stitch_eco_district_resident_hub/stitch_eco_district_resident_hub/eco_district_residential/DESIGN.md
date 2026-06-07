---
name: Eco-District Residential
colors:
  surface: '#f9faf2'
  surface-dim: '#d9dbd3'
  surface-bright: '#f9faf2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4ec'
  surface-container: '#edefe7'
  surface-container-high: '#e8e9e1'
  surface-container-highest: '#e2e3db'
  on-surface: '#1a1c18'
  on-surface-variant: '#414844'
  inverse-surface: '#2f312c'
  inverse-on-surface: '#f0f1e9'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#7d562d'
  on-secondary: '#ffffff'
  secondary-container: '#ffca98'
  on-secondary-container: '#7a532a'
  tertiary: '#1e2b00'
  on-tertiary: '#ffffff'
  tertiary-container: '#304200'
  on-tertiary-container: '#91b243'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffdcbd'
  secondary-fixed-dim: '#f0bd8b'
  on-secondary-fixed: '#2c1600'
  on-secondary-fixed-variant: '#623f18'
  tertiary-fixed: '#ccf078'
  tertiary-fixed-dim: '#b0d360'
  on-tertiary-fixed: '#151f00'
  on-tertiary-fixed-variant: '#394d00'
  background: '#f9faf2'
  on-background: '#1a1c18'
  surface-variant: '#e2e3db'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 84px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
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
  margin: 64px
  section-gap: 120px
---

## Brand & Style

The brand identity centers on "Quiet Sustainability"—a high-end, net-zero residential experience that feels restorative rather than industrial. The design system prioritizes a **Tactile Minimalism** approach, blending the precision of modern architecture with the warmth of organic materials. 

The emotional response should be one of "Grounded Optimism." The UI avoids clinical whites and harsh blacks in favor of natural pigments and soft light. It communicates exclusivity through generous whitespace and meticulous typography, while maintaining an approachable, eco-conscious ethos through texture and organic curves.

## Colors

The palette is derived from the natural forest floor and sustainable building materials. 

*   **Primary (Forest Green):** Used for primary actions, deep backgrounds, and high-contrast typography. It represents density and growth.
*   **Secondary (Oak Wood):** A warm, wood-inspired tone used for accents and secondary interactive elements to provide a tactile contrast to the greens.
*   **Tertiary (Sapling):** A brighter green used sparingly for success states, badges, and highlighting environmental metrics.
*   **Neutral (Off-White/Parchment):** The primary canvas color. It reduces eye strain and feels more organic than pure white.
*   **Surface (Sage Mist):** A very desaturated green-grey (#E9EDDE) used for input fields and subtle section backgrounds.

## Typography

This design system utilizes **Plus Jakarta Sans** across all levels to maintain a modern, friendly, and geometric appearance. The soft curves of the letterforms mirror the organic UI shapes. 

Large display titles should be set in Forest Green with tight tracking to evoke a premium, editorial feel. Body text utilizes a slightly increased line-height to ensure readability and a "breathing" layout. Label styles should be used for metadata and small captions, often paired with the Oak Wood secondary color.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop, centered within a 1280px container. A 12-column structure is used with generous 32px gutters to prevent content density from feeling overwhelming.

Vertical rhythm is driven by wide "Section Gaps" (120px) to give each narrative piece of the development space to shine. Spacing between related elements should follow an 8px base unit (e.g., 8, 16, 24, 40, 64). Leaf-patterned dividers are used to separate major thematic sections, acting as a visual "breath" in the user journey.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Ambient Shadows**. Instead of harsh drop shadows, this design system uses soft, multi-layered shadows tinted with the primary Forest Green (at very low opacity) to create a natural, "floating" effect.

Wood textures are applied to specific background layers or "hero cards" to ground the digital experience in the physical world. For interactive depth, a "pressed" state should use a slight inner shadow, mimicking the compression of natural materials.

## Shapes

The shape language is strictly organic. Sharp corners are avoided. Standard UI elements (buttons, inputs) use a 0.5rem (8px) base radius. Larger containers, such as property cards or featured image blocks, use the `rounded-xl` (1.5rem / 24px) setting to emphasize a soft, non-industrial aesthetic.

Leaf patterns and botanical illustrations should be used as masks for images or as subtle background watermarks, reinforcing the net-zero narrative.

## Components

*   **Buttons:** Primary buttons are Forest Green with white text; secondary buttons use a Ghost style with a Forest Green border. All buttons have a high-tap area and 8px corners.
*   **Cards:** Property and feature cards use an Off-White background with a subtle Oak Wood bottom border (2px). They should feature a soft ambient shadow on hover.
*   **Leaf Dividers:** Horizontal rules are replaced with a stylized, repeating leaf-vein SVG pattern in a faint Sage Mist color.
*   **Input Fields:** Soft-filled backgrounds (#E9EDDE) with no initial border; they transition to a Forest Green border on focus.
*   **Progress Indicators:** Used for sustainability metrics (e.g., solar yield, water savings). These should use "organic" bar shapes with rounded caps in Tertiary Sapling green.
*   **Wood Accents:** Occasional use of high-resolution, light oak grain textures as a background for "Call to Action" sections or navigation headers to add tactile luxury.