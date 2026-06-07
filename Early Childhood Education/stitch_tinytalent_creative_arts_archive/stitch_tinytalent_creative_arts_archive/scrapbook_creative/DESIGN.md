---
name: Scrapbook Creative
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
  on-surface-variant: '#3e4948'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#6e7978'
  outline-variant: '#bdc9c8'
  surface-tint: '#006a68'
  primary: '#006a68'
  on-primary: '#ffffff'
  primary-container: '#48a9a6'
  on-primary-container: '#003938'
  inverse-primary: '#78d6d2'
  secondary: '#785a00'
  on-secondary: '#ffffff'
  secondary-container: '#fdc73c'
  on-secondary-container: '#705400'
  tertiary: '#a63839'
  on-tertiary: '#ffffff'
  tertiary-container: '#f47370'
  on-tertiary-container: '#690912'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#94f2ef'
  primary-fixed-dim: '#78d6d2'
  on-primary-fixed: '#00201f'
  on-primary-fixed-variant: '#00504e'
  secondary-fixed: '#ffdf9a'
  secondary-fixed-dim: '#f4bf34'
  on-secondary-fixed: '#251a00'
  on-secondary-fixed-variant: '#5a4300'
  tertiary-fixed: '#ffdad7'
  tertiary-fixed-dim: '#ffb3af'
  on-tertiary-fixed: '#410005'
  on-tertiary-fixed-variant: '#862124'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-xl:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
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
  margin: 32px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The design system is built to evoke the tactile, unrefined joy of a child's physical art portfolio. It rejects the sterile precision of modern tech in favor of a **Tactile & Brutalist-Lite** hybrid aesthetic. The emotional response should be one of "curated chaos"—warm, encouraging, and deeply personal. 

The interface mimics a digital refrigerator door. It uses paper textures, visible "tape" or "pin" elements, and intentional "messiness" to lower the barrier to creativity. By celebrating imperfections like asymmetrical alignments and hand-drawn strokes, the design system makes kids feel that their work—no matter how messy—belongs in a professional-grade gallery.

## Colors
The palette is grounded in an off-white paper base to reduce eye strain and provide a "canvas" feel.
- **Background:** A warm, fibrous off-white (#F9F7F2).
- **Ink:** Charcoal (#333333) is used for all text and hand-drawn borders to mimic marker or pen.
- **Accents:** Teal (Primary), Mustard (Secondary), Coral (Tertiary), and Purple (Quaternary) are used as "splatters." These colors should never be used for structural backgrounds, only for decorative accents, button states, and category tags. 

Apply colors with a "watercolor" logic: use varying opacities (80-90%) to allow underlying paper textures to bleed through.

## Typography
The typography strategy pairs the distinctive, slightly quirky geometry of **Epilogue** for headings with the high readability of **Lexend** for body copy. 

**Epilogue** serves as the "hand-drawn" surrogate; its bold weights feel expressive and editorial. **Lexend** is chosen for its educational roots, ensuring that even young readers can navigate the portfolio easily. Headings should occasionally use a slight rotation (1-2 degrees) to reinforce the scrapbook aesthetic.

## Layout & Spacing
This design system utilizes an **Asymmetrical Grid**. While a 12-column underlying structure exists for placement, elements should rarely snap perfectly to it. 

- **The "Wobble" Rule:** Major layout containers (cards, images) should have a random CSS transform rotation between -1.5deg and +1.5deg.
- **Overlays:** Elements are encouraged to overlap. A "sticker" or "caption" should partially obscure the corner of a photo or video frame.
- **Negative Space:** Use generous, uneven margins to mimic a physical desk where items have been tossed down.

## Elevation & Depth
Depth is created through **physical metaphors** rather than digital shadows. 
- **Layering:** Items higher in the hierarchy overlap items below them. 
- **Adhesives:** Use small rectangular overlays with a low-opacity "washi tape" texture to "hold" elements to the background. 
- **Drop Shadows:** Avoid soft, ambient shadows. Instead, use a "Hard Shadow" (4px offset, 0 blur, Charcoal at 20% opacity) to give the impression of thick cardstock paper lifted slightly off the surface.
- **Textures:** Apply a subtle grain overlay across the entire UI to kill digital flatness.

## Shapes
Shapes in the design system should feel "cut by hand." 
- **Borders:** All primary containers must use a `2px` charcoal border with a `border-image` that simulates a shaky, hand-drawn line.
- **Corners:** Use "Soft" (0.25rem) roundedness as a base, but apply `clip-path` or irregular border-radii (e.g., `255px 15px 225px 15px/15px 225px 15px 255px`) to create organic, non-perfect rectangles.
- **Splatters:** Decorative background elements should use organic, blob-like SVG shapes rather than circles or squares.

## Components
- **Buttons:** Styled as "Duct Tape" or "Labels." They feature a solid fill of one of the accent colors, a hard 2px charcoal border, and a slight hover lift (translation Y-2px).
- **Cards:** Use a white background with a subtle paper texture. Each card should have a unique "pin" or "tape" graphic at the top center.
- **Input Fields:** Styled as underlined handwriting prompts. The border-bottom should be a hand-drawn charcoal line.
- **Chips/Tags:** Look like small scraps of torn paper. The edges should be jagged (using a mask-image or SVG path).
- **Progress Indicators:** Use a "Crayon Stroke" style—wide, textured lines that fill up as the user progresses.
- **Interactive Splatters:** When a user "likes" or "claps" for a piece of art, a watercolor splatter in a random accent color should bloom behind the icon.