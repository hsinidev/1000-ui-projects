---
name: Atelier-Live
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#56423e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#89726d'
  outline-variant: '#ddc0bb'
  surface-tint: '#a03f30'
  primary: '#9d3d2e'
  on-primary: '#ffffff'
  primary-container: '#bd5444'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb4a7'
  secondary: '#645d53'
  on-secondary: '#ffffff'
  secondary-container: '#e8ded1'
  on-secondary-container: '#686257'
  tertiary: '#55642b'
  on-tertiary: '#ffffff'
  tertiary-container: '#6e7d41'
  on-tertiary-container: '#040600'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a7'
  on-primary-fixed: '#400200'
  on-primary-fixed-variant: '#80281b'
  secondary-fixed: '#ebe1d4'
  secondary-fixed-dim: '#cfc5b9'
  on-secondary-fixed: '#1f1b13'
  on-secondary-fixed-variant: '#4c463c'
  tertiary-fixed: '#d9eaa3'
  tertiary-fixed-dim: '#bdce89'
  on-tertiary-fixed: '#161f00'
  on-tertiary-fixed-variant: '#3e4c16'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  h1:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: EB Garamond
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
  h3:
    fontFamily: EB Garamond
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system is built to bridge the gap between the tactile world of a physical art studio and the precision of a digital learning environment. The brand personality is deeply human, cultivated, and inspiring, positioning itself as a premium mentor rather than a corporate utility. 

The aesthetic direction is a blend of **Minimalism** and **Tactile** design. It prioritizes expansive whitespace to let artwork breathe, while incorporating "human-made" elements—organic, non-perfect shapes and subtle paper-like textures—to evoke the feeling of high-quality art supplies and archival paper. The goal is to create an atmosphere that feels as intentional and curated as a gallery, yet as warm and accessible as a personal sketchbook.

## Colors

The palette is rooted in natural, earthy pigments. **Terra-Cotta** serves as the primary action color, used sparingly to draw attention to key interactions and educational milestones. The **Off-White** background is not a flat hex code but should be perceived as a "canvas," providing a warm, non-clinical foundation.

**Charcoal** is used for typography to ensure high legibility without the harshness of pure black, maintaining a soft, charcoal-sketch aesthetic. A muted Sage (Tertiary) is introduced for success states and secondary accents to keep the palette feeling organic. All surfaces should utilize a very low-opacity grain overlay to simulate the texture of heavy-weight paper.

## Typography

The typographic scale creates a sophisticated editorial rhythm. **EB Garamond** is the primary choice for headings, lending an air of history, authority, and literary grace to the educational content. It should be typeset with slightly tighter tracking in larger sizes to emphasize its elegant letterforms.

**Manrope** provides a clean, contemporary counterpoint for body text and functional UI elements. It ensures that instructional content is easy to digest across all device sizes. For "handwritten" accents (annotations, underlines, and arrows), use custom SVG paths or a specialized script font sparingly to highlight key insights or suggest a teacher's personal touch on the page.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to maintain the integrity of art compositions, transitioning to a flexible fluid model for mobile. The layout is inspired by art monographs, featuring generous margins (`xl`) and off-center alignments to create a sense of movement.

Spacing should be used to group related concepts—narrower gaps between descriptions and images, and wide "breathing room" between different sections of a lesson. Horizontal rules, when used, should have a slight "hand-drawn" wobble rather than being perfectly straight 1px lines.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layers** and subtle physical metaphors rather than dramatic shadows. Surfaces do not "float" high above the background; instead, they feel like sheets of paper or canvas laid upon one another.

- **Level 0 (Canvas):** The Off-White base with a subtle tooth/texture.
- **Level 1 (Paper):** Secondary surfaces used for cards or sidebars, slightly lighter than the background or with a very thin, low-contrast Charcoal border (10% opacity).
- **Level 2 (Active):** Elements that require immediate focus use a soft, diffused "ambient shadow" that is tinted with the Terra-Cotta hue to feel warm and integrated, rather than gray and sterile.

## Shapes

The shape language avoids clinical sharp corners. A **Rounded** setting (0.5rem base) is applied to most components to make the interface feel approachable and "soft." 

To reinforce the artistic theme, secondary decorative elements (like image frames or button hovers) should occasionally use **Organic Shapes**—subtle "squiggles" or slightly asymmetrical radii—to mimic the hand-drawn nature of an artist's workspace.

## Components

### Buttons
Primary buttons are solid Terra-Cotta with Off-White text, featuring a subtle inner-glow to feel slightly tactile. Secondary buttons use a "Charcoal" outline with a hand-drawn stroke quality.

### Cards
Cards are the primary container for art pieces and course modules. They should feature the Level 1 "Paper" surface with a 1px border in a slightly darker cream. The "soft" rounded corners (1rem for large cards) are essential.

### Input Fields
Inputs should feel like writing on a form. Use a simple bottom-border focus state in Terra-Cotta, with labels set in the `label-caps` Manrope style for clarity.

### Handwritten Accents
Small SVG-based annotations (circles around key terms, arrows pointing to details in a painting) should appear as if a mentor has sketched directly onto the interface.

### Textured Backgrounds
Large surfaces, such as the main dashboard or lesson headers, must include a subtle noise or paper-grain texture to eliminate the "digital" flat look and provide a premium, tactile quality.