---
name: Tactile & Chic Bespoke
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#524345'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#857374'
  outline-variant: '#d7c1c3'
  surface-tint: '#8c4b55'
  primary: '#8a4853'
  on-primary: '#ffffff'
  primary-container: '#a6606b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#5c5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#757474'
  on-tertiary-container: '#fffcfb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Playfair Display
    fontSize: 42px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-margin: 20px
  gutter: 16px
  section-padding: 64px
---

## Brand & Style
The brand personality is rooted in sensory luxury and craftsmanship. It targets a discerning clientele who appreciates the intersection of traditional horology and modern bespoke fashion. The UI must evoke the physical sensation of high-grade exotic leather—alluding to grain, supple texture, and durability.

The chosen design style is **Soft-UI (Neumorphism)**. Unlike traditional flat design, this system uses subtle protrusions and indentations to mimic a surface that has been molded or embossed. The interface should feel like a single sheet of fine material where elements are pressed into or pushed out from the background, creating a cohesive, "squishy" yet structured tactile experience.

## Colors
The palette is a sophisticated trio designed to let high-contrast photography shine.
- **Rose Gold (#B76E79):** Used sparingly for call-to-actions, active states, and premium accents.
- **Pure White (#FFFFFF):** The source of light for Neumorphic highlights and the primary surface color.
- **Deep Grey (#2F2F2F):** Reserved for high-contrast typography and structural shadows.
- **Neutral Soft Grey (#F5F5F5):** The base background color required to make Soft-UI shadows and highlights visible.

The design relies on a light-mode default to maintain the "chic" and airy feel of a high-end boutique.

## Typography
The typography strategy creates a tension between heritage and modern precision.
- **Headings:** Use *Playfair Display*. Its high-contrast strokes reflect the luxury of fashion editorials and the precision of watchmaking.
- **Body & Interface:** Use *Manrope*. This sans-serif is balanced and highly legible on mobile devices, providing a functional contrast to the decorative serif headings.
- **Labels:** Small caps with increased letter spacing are used for category tags and metadata to maintain an organized, premium aesthetic.

## Layout & Spacing
This design system utilizes a **Mobile-First Fluid Grid**. Given the bespoke nature of the product, the layout prioritizes large, edge-to-edge imagery and generous negative space to prevent the UI from feeling "crowded."

- **Grid:** A 4-column grid for mobile, expanding to 12-columns for desktop.
- **Rhythm:** An 8px base unit drives all padding and margins. 
- **Margins:** 20px safe areas on mobile ensure that the soft shadows of cards do not get clipped by the screen edge.

## Elevation & Depth
Depth is the primary communicator of hierarchy in this system. Instead of traditional Z-index stacking, we use **Dual-Shadow Neumorphism**:
- **Extruded (Raised):** Elements like buttons or cards use a light shadow (Pure White) on the top-left and a soft dark shadow (Deep Grey at 10% opacity) on the bottom-right.
- **Inverted (Pressed):** Elements like input fields or active button states use inner shadows to appear recessed into the surface, mimicking leather being embossed.
- **Shadow Softness:** All shadows must have a high blur-to-distance ratio (e.g., 10px distance, 20px blur) to ensure the "Soft-UI" effect remains subtle and chic rather than muddy.

## Shapes
The shape language is "Rounded" (0.5rem base), reflecting the natural curves of a watch face and the flexibility of leather straps. 
- **Standard Radius:** 8px for buttons and small components.
- **Large Radius:** 16px for product cards and containers.
- **Pill Shapes:** Used exclusively for tags and "Add to Cart" actions to differentiate them from static UI elements.
- **Avoid Sharp Corners:** Sharp edges are avoided as they contradict the tactile, "soft" brand promise.

## Components
- **Buttons:** Primary buttons use the Rose Gold palette with a subtle "extruded" effect. On tap, they transition to a "pressed" state.
- **Cards:** Product cards are soft-edged containers with no borders. Elevation alone defines their boundary. High-contrast leather photography should occupy 70% of the card area.
- **Selection Chips:** Used for leather type (Alligator, Ostrich, Calf). These should look like physical buttons that stay "pressed" when selected.
- **Input Fields:** Search and customization forms use the "inverted/pressed" style to look like they are carved into the background.
- **Visual Progress Tracker:** A bespoke component for the "Hand-Stitching" process, using a dotted line that mimics actual leather thread paths.
- **Image Carousels:** Full-bleed on mobile with soft-shadowed pagination dots to emphasize the tactile quality of the photography.