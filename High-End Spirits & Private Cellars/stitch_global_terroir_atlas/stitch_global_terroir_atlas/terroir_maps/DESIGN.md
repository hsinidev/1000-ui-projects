---
name: Terroir-Maps
colors:
  surface: '#fdfae7'
  surface-dim: '#dddbc8'
  surface-bright: '#fdfae7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f4e1'
  surface-container: '#f1eedb'
  surface-container-high: '#ece9d6'
  surface-container-highest: '#e6e3d0'
  on-surface: '#1c1c11'
  on-surface-variant: '#46483c'
  inverse-surface: '#313124'
  inverse-on-surface: '#f4f1de'
  outline: '#77786b'
  outline-variant: '#c7c8b9'
  surface-tint: '#586330'
  primary: '#485422'
  on-primary: '#ffffff'
  primary-container: '#606c38'
  on-primary-container: '#dfedac'
  inverse-primary: '#bfcd8f'
  secondary: '#75593a'
  on-secondary: '#ffffff'
  secondary-container: '#fdd6ae'
  on-secondary-container: '#785b3c'
  tertiary: '#425159'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a6972'
  on-tertiary-container: '#d8e9f3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe9a9'
  primary-fixed-dim: '#bfcd8f'
  on-primary-fixed: '#171e00'
  on-primary-fixed-variant: '#404b1b'
  secondary-fixed: '#ffddbb'
  secondary-fixed-dim: '#e5c099'
  on-secondary-fixed: '#2b1701'
  on-secondary-fixed-variant: '#5c4224'
  tertiary-fixed: '#d5e5ef'
  tertiary-fixed-dim: '#b9c9d3'
  on-tertiary-fixed: '#0e1d25'
  on-tertiary-fixed-variant: '#3a4951'
  background: '#fdfae7'
  on-background: '#1c1c11'
  surface-variant: '#e6e3d0'
typography:
  h1:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
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

The design system is anchored in the intersection of viticultural heritage and modern geographic data. It targets an audience that values both the artisanal tradition of winemaking and the precision of environmental science. The brand personality is scholarly yet approachable—a "digital field guide" that feels like a premium physical atlas.

The visual style is a blend of **Minimalism** and **Tactile/Organic** elements. It prioritizes clarity for complex mapping data while using subtle textures and soft geometry to avoid a sterile, purely technical feel. The interface should feel like high-quality recycled paper: substantial, intentional, and grounded in the earth.

## Colors

The palette is derived from the natural lifecycle of a vineyard. The primary **Olive Green** serves as the brand’s anchor, used for key actions and navigational markers. The secondary **Sand** acts as a warm, humanizing neutral for surfaces, providing a softer alternative to pure white. 

**Slate** is reserved for high-contrast typography and technical data visualizations, ensuring accessibility against the warmer background tones. For the "data-driven but natural" feel, use the **background_paper** hex for primary containers and **neutral_color_hex** for secondary page sections to create subtle contrast without harsh lines.

## Typography

The typographic hierarchy balances editorial elegance with functional precision. **Libre Caslon Text** is used for headings to evoke the history and prestige of global vineyards. It should be typeset with generous leading to maintain a classic, readable feel.

**Hanken Grotesk** handles all functional UI, data points, and body copy. It provides a sharp, contemporary contrast to the serif headings. For map labels and coordinate data, use the `data-mono` style with increased letter spacing to ensure legibility over complex vector backgrounds.

## Layout & Spacing

The design system utilizes a **fixed-grid** philosophy for content-heavy pages (educational articles, vineyard profiles) to ensure optimal line lengths for reading. For the discovery platform and mapping views, the system shifts to a **fluid grid** with safe-area margins.

A consistent 8px rhythm governs all spacing. Vertical rhythm is particularly important in this design system to mimic the structured columns of a traditional encyclopedia or a field journal. Use `lg` and `xl` spacing for section breaks to allow the UI to "breathe" like a physical book.

## Elevation & Depth

Depth is conveyed through **tonal layers** and **subtle textures** rather than traditional drop shadows. Instead of floating elements, UI components should feel like they are layered sheets of paper or tactile cards resting on a surface.

- **Surface Tiers:** Use varying shades of Sand and Paper to define hierarchy. A "raised" card is simply a lighter shade of Sand against a darker Sand background.
- **Micro-shadows:** When necessary for interactivity (e.g., a hovered button), use a very soft, low-opacity Slate tint (#2F3E46 at 8%) with a large blur radius to maintain the organic feel.
- **Textures:** Apply a faint, non-tiling grain overlay (reminiscent of parchment or fine silt) to primary background layers at 3-5% opacity.

## Shapes

The shape language is **Rounded**, avoiding the harshness of sharp corners to reflect the organic nature of vines and hillsides. 

- Standard components (buttons, input fields) use a 0.5rem radius.
- Larger containers (cards, map overlays) use a 1rem radius (`rounded-lg`).
- Feature imagery and profile avatars should use a "squircle" or soft-circle shape to maintain the organic aesthetic.
- Vector lines on maps should be slightly smoothed, avoiding jagged 90-degree turns.

## Components

### Buttons & Inputs
Buttons feature solid Olive Green fills with Slate or White text. Secondary actions use Slate outlines with a Sand hover state. Input fields should have a 1px Slate border at 20% opacity, which darkens to 100% on focus, mimicking a pencil stroke on paper.

### Chips & Tags
Used for soil types (e.g., "Calcareous," "Volcanic") and grape varieties. These should use the `label-sm` typography and a light Slate-tinted background with rounded-pill shapes.

### Information Cards
Cards are the primary vehicle for vineyard data. They should feature a thin, low-contrast Slate border and a subtle internal texture. Header sections within cards use the Serif typeface, while the "stats" section uses the Sans-Serif at a smaller scale.

### Vector Maps
Map markers are custom-designed as minimalist vector nodes. Use varied line weights in Slate to represent topographic contours, creating a "hand-drawn but accurate" appearance.

### Progress & Data Viz
Use Olive Green for positive growth data and Sand/Slate for neutral data. Avoid "alert" reds unless absolutely necessary; instead, use a deep terracotta for warnings to keep the palette earthy.