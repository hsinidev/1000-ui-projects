---
name: AuraVillas
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4b463d'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#7d766c'
  outline-variant: '#cec5ba'
  surface-tint: '#685d4a'
  primary: '#685d4a'
  on-primary: '#ffffff'
  primary-container: '#f7e7ce'
  on-primary-container: '#726753'
  inverse-primary: '#d3c5ad'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5e5f54'
  on-tertiary: '#ffffff'
  tertiary-container: '#eaeadb'
  on-tertiary-container: '#68695e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0e0c8'
  primary-fixed-dim: '#d3c5ad'
  on-primary-fixed: '#221b0b'
  on-primary-fixed-variant: '#4f4533'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e3e3d5'
  tertiary-fixed-dim: '#c7c7ba'
  on-tertiary-fixed: '#1b1c14'
  on-tertiary-fixed-variant: '#46483d'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  h1:
    fontFamily: notoSerif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  margin-page: 80px
  gutter: 24px
  section-gap: 160px
  stack-sm: 12px
  stack-md: 32px
---

## Brand & Style

This design system is built upon the concept of "Quiet Luxury." It targets a high-net-worth audience that values discretion, architectural precision, and heritage over loud branding. The emotional response is one of calm, exclusivity, and effortless sophistication.

The design style is **Editorial Minimalism**. It draws inspiration from premium lifestyle and architecture magazines like *Cereal* or *Kinfolk*. The interface acts as a silent gallery, stepping back to allow high-fidelity property photography to command the viewer's attention. Visual weight is carried through negative space and precise typographic rhythm rather than decorative elements or heavy shadows.

## Colors

The palette is anchored in **Ivory (#FFFFF0)**, which serves as the primary canvas for all interfaces, providing a warmer, more organic feel than pure white. **Slate (#708090)** is used for structural elements, thin borders, and secondary text, offering a cool contrast to the warmth of the background. 

**Champagne (#F7E7CE)** is reserved for high-value accents, active states, and call-to-action highlights, symbolizing the "gold standard" of the properties represented. Primary text is set in a deep, softened charcoal to maintain readability without the harshness of absolute black.

## Typography

The typography strategy focuses on the interplay between the timeless elegance of **notoSerif** and the functional clarity of **inter**. 

Headlines utilize Noto Serif with tight tracking to mimic the look of high-end editorial mastheads. Body text relies on Inter with a light weight (300) and generous line-height to ensure a breathable, "airy" reading experience. Navigational elements and small labels use Inter in uppercase with wide letter-spacing to create a sense of architectural structure and authority.

## Layout & Spacing

This design system employs a **fixed grid** model to ensure consistent alignments that feel intentional and curated. A 12-column grid is used for the desktop experience with significant external margins (80px+) to frame the content.

The spacing rhythm is intentionally oversized. Section gaps are expansive to prevent the "cluttered" feel of standard commercial sites. Elements should feel as though they have "room to breathe," prioritizing the user's focus on one piece of information or one image at a time. Gutters remain tight to maintain the relationship between related items, while vertical stacking is used to create a clear visual hierarchy.

## Elevation & Depth

To maintain the editorial aesthetic, this design system avoids traditional drop shadows and neomorphic effects. Depth is instead communicated through:

1.  **Low-Contrast Outlines:** Surfaces are defined by 1px or 0.5px "hairline" borders in Slate at low opacity.
2.  **Tonal Layering:** Using subtle shifts between Ivory and a slightly darker cream to distinguish between the background and foreground containers.
3.  **Scale and Overlap:** Occasional overlapping of images and text blocks creates a 2.5D effect reminiscent of a physical magazine layout.
4.  **Full-Bleed Media:** High-contrast photography provides its own depth, making the UI feel like an overlay on top of a physical environment.

## Shapes

The shape language is strictly **Sharp (0)**. All buttons, image containers, cards, and input fields utilize 90-degree corners. This decision reinforces the architectural nature of the product, reflecting the clean lines of luxury villas and modern estate design. Rounded corners are perceived as too "friendly" or "app-like" for this specific luxury context; sharp edges provide the necessary precision and formal tone.

## Components

### Buttons
Primary buttons are Slate-filled with Ivory text, maintaining a sharp, rectangular profile. Secondary buttons are "Ghost" style—1px Slate borders with no fill. All button interactions should be subtle, such as a gentle opacity shift or a Champagne-colored underline on hover.

### Cards
Property cards are borderless. The focus is a high-resolution image with typography placed either directly below or partially overlapping. Information density is kept extremely low—only price, location, and name.

### Input Fields
Forms are minimalist, consisting of a single 1px Slate bottom-border (underline style) rather than a full box. Labels use the `label-caps` typography style and sit above the line. Focus states are indicated by the line transitioning to Champagne.

### Navigation
The main navigation is spacious, using wide letter-spacing for links. A "sticky" header should be translucent (Ivory with backdrop blur) to maintain a light footprint as the user scrolls.

### Additional Components
- **Image Carousels:** Use hairline arrows and "fraction" pagination (e.g., 01 / 12) in Noto Serif.
- **Dividers:** Horizontal hairlines in Slate (20% opacity) used sparingly to separate major editorial sections.