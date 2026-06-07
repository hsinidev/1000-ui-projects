---
name: Heritage Horology
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#544341'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#877270'
  outline-variant: '#dac1bf'
  surface-tint: '#954742'
  primary: '#2a0002'
  on-primary: '#ffffff'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#ffb3ad'
  secondary: '#7b580d'
  on-secondary: '#ffffff'
  secondary-container: '#fdcd79'
  on-secondary-container: '#785509'
  tertiary: '#131003'
  on-tertiary: '#ffffff'
  tertiary-container: '#292514'
  on-tertiary-container: '#938c75'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffdea8'
  secondary-fixed-dim: '#eebf6d'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5e4200'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
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
    fontFamily: Playfair Display
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max: 1440px
---

## Brand & Style

This design system embodies the meticulous craftsmanship of high-end horology. It is rooted in a **Tactile/Skeuomorphic** philosophy, where digital surfaces mimic physical materials like cold enamel, brushed steel, and hand-stitched leather. The goal is to evoke the sensation of holding a bespoke timepiece—heavy, precise, and timeless.

The aesthetic balance leans toward **Minimalism** in layout to allow rich, textured material cards and high-performance video assets to take center stage. Every interaction should feel intentional and dampened, mirroring the mechanical resistance of a watch crown or a sapphire glass bezel. The target audience values heritage over trends and expects a digital experience that feels as curated as a private atelier.

## Colors

The palette is a triptych of traditional luxury materials. 
- **Deep Burgundy (#4A0E0E)** serves as the primary "Enamel" color, used for high-contrast backgrounds and deep structural elements. 
- **Tan Leather (#B68D40)** acts as the "Patina" accent, applied to interactive states, call-to-actions, and fine-line borders.
- **Parchment (#F4EBD0)** provides the foundational "Dial" surface, offering a warm, non-clinical background that reduces eye strain and enhances the richness of the dark wood and metal tones.
- **Polished Steel (#E5E5E5)** and **Obsidian (#1A1A1A)** are used for technical details, shadows, and crisp typography.

## Typography

Typography in this design system prioritizes legibility and editorial elegance. **Playfair Display** is the signature typeface for all headlines and labels, utilizing its high-contrast strokes to reflect the engraving on a watch face. Headlines should favor tighter letter-spacing to feel more "locked" and intentional.

**Manrope** provides a functional, modern counterpoint for body text and technical specifications. Its geometric but warm structure ensures that detailed watch descriptions remain readable across all devices. Small labels and category markers should use Playfair Display in uppercase with generous letter-spacing to mimic the branding found on a watch dial.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model to maintain an editorial, "lookbook" feel. Content is centered within a maximum container width, surrounded by generous margins that act as a frame for the high-end visuals. 

The spacing rhythm follows an 8px base unit, but emphasizes large "breathing spaces" (64px+) between major sections to denote prestige. Use a 12-column grid for desktop views, with components frequently spanning the center 8 columns to create a sense of focused, intimate luxury. Gutters are kept wide (24px) to ensure that intricate textures on cards do not visually bleed into one another.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and **Ambient Shadows** that simulate physical height. 
- **The Base:** All content sits on the Parchment surface.
- **The Material Layer:** Cards and containers use a subtle "inner glow" (top-left light source) to mimic beveled sapphire glass or polished metal edges.
- **The Shadow:** Shadows are not neutral grey; they use a 15% opacity of the Deep Burgundy to feel "warm" and integrated. Shadows should be diffused and soft (large blur, 0 offset) to suggest a close proximity to the surface.
- **Guilloché Overlay:** Interactive containers may feature a low-opacity SVG pattern overlay that mimics engine-turned metal engraving, adding a layer of micro-depth visible only upon close inspection.

## Shapes

The shape language is **Soft (0.25rem)**, reflecting the precision-machined edges of a watch case. While large cards and video containers use a subtle radius to feel approachable, inner elements like input fields and button containers utilize sharp corners to maintain a "technical instrument" aesthetic. The juxtaposition of soft outer containers and sharp inner components communicates the blend of organic leather and rigid mechanical parts.

## Components

### Navigation
Sophisticated and minimal. The header should be transparent, transitioning to a solid Parchment or Burgundy blur only upon scroll. Use a centered logo with navigation links hidden behind a "Collection" trigger or spaced widely across the top.

### Material Cards
Cards are the primary storytelling vehicle. They must feature a "Guilloché" texture background (subtle geometric engraving) and a 1px "Polished Metal" border (#B68D40 at 30% opacity).

### Elegant Sliders
Range sliders and carousels must avoid standard "pill" handles. Use a stylized "Watch Hand" or a simple vertical needle indicator in Tan Leather. The track should be a thin, recessed line.

### Video Containers
High-performance video assets (close-ups of movements) should be housed in "Bezel" containers—heavy frames with a slight inner shadow to create a sense of looking through a crystal.

### Buttons
Primary buttons use the Deep Burgundy background with Parchment text. Interaction should be subtle; a slight shift in the "inner bevel" rather than a dramatic color change, simulating a physical push-piece.

### Lists & Inputs
Inputs should be "Minimalist Underlined" rather than boxed, utilizing a 1px Tan Leather bottom border. List items should be separated by high-precision "hairline" dividers in light gold or parchment-smoke.