---
name: Monolithic Elegance
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c5c6ca'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#8f9194'
  outline-variant: '#44474a'
  surface-tint: '#c6c6c9'
  primary: '#c6c6c9'
  on-primary: '#2f3133'
  primary-container: '#1a1c1e'
  on-primary-container: '#838486'
  inverse-primary: '#5d5e61'
  secondary: '#bcc7dd'
  on-secondary: '#263142'
  secondary-container: '#3c475a'
  on-secondary-container: '#aab6cc'
  tertiary: '#ffb77d'
  on-tertiary: '#4d2600'
  tertiary-container: '#2f1500'
  on-tertiary-container: '#c86c00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e5'
  primary-fixed-dim: '#c6c6c9'
  on-primary-fixed: '#1a1c1e'
  on-primary-fixed-variant: '#454749'
  secondary-fixed: '#d8e3fa'
  secondary-fixed-dim: '#bcc7dd'
  on-secondary-fixed: '#111c2c'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 4.5rem
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Work Sans
    fontSize: 1.25rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  gutter: 32px
  margin: 64px
  section-gap: 128px
  container-max: 1440px
---

## Brand & Style

This design system is built on the principles of **Structural Minimalism** and **Tactile Luxury**. The brand identity reflects the permanence of high-end hardscaping—stone, granite, and slate—translated into a digital interface. The goal is to evoke a sense of architectural stability, precision, and immense value.

The aesthetic utilizes a heavy, grounded layout where every element feels "set in stone." We move away from the airy weightlessness of typical SaaS design toward a more physical, industrial-chic presence. High-resolution granite texture overlays are applied sparingly to background surfaces to provide depth and a tactile connection to the physical medium of the work.

## Colors

The palette is rooted in the natural tones of quarry-extracted materials. 

*   **Granite Grey (#1A1C1E):** The primary foundation. Used for backgrounds to create a deep, sophisticated atmosphere that allows photography of stone projects to pop.
*   **Slate (#4A5568):** Used for secondary structural elements, borders, and subtle accents. It provides the "mortar" between the dark background and the content.
*   **Burnt Orange (#D97706):** Reserved exclusively for high-priority Call to Action (CTA) elements. It represents the warmth of a fire pit or the glow of sunset on stone, providing a sharp, high-end contrast.
*   **Text & Highlights:** Use high-contrast Slate-900 or off-white (#F8FAFC) for body copy to ensure maximum readability against dark backgrounds.

## Typography

Typography is used to reinforce the architectural theme. 

**Headings** utilize **Inter** with heavy weights and tight letter spacing to appear as solid blocks of text. This "monolithic" typesetting mirrors the weight of massive stone slabs.

**Body Text** utilizes **Work Sans**, chosen for its slightly wider apertures and grounded feel, ensuring long-form project descriptions or technical specifications are effortless to read against textured backgrounds. 

**Labels** are always set in uppercase Inter with increased letter spacing to serve as clear, structural signposts throughout the UI.

## Layout & Spacing

The design system employs a **Fixed Grid** model to maintain a sense of rigid, deliberate construction. 

*   **Grid:** A 12-column grid with generous 32px gutters to give every element room to breathe, preventing the "heavy" components from feeling cluttered.
*   **Rhythm:** Spacing follows an 8px base unit. Section gaps are intentionally large (128px+) to create an editorial, high-end gallery feel.
*   **Alignment:** Elements should favor flush, blocky alignments. Centered layouts should be reserved for high-impact hero statements.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and physical textures rather than traditional shadows. 

1.  **Base Layer:** Dark Granite Grey with a low-opacity granite texture overlay (set to 'Multiply' or 'Overlay' at 5-10%).
2.  **Raised Surfaces:** Slate (#4A5568) surfaces that appear to be carved out of the background.
3.  **Outlines:** Instead of shadows, use 1px or 2px solid borders in a slightly lighter slate tone to define the edges of "slabs" (cards/containers).
4.  **Recessed States:** Input fields and secondary buttons should use a darker-than-background hex to appear "etched" into the stone.

## Shapes

The shape language is strictly **Sharp (0)**. To mimic the precision of cut stone and architectural blueprints, there are no rounded corners in this design system. Every button, card, and input field must have 90-degree angles. This reinforces the "Elite" and "Hardscape" brand pillars by avoiding the "softness" of consumer tech.

## Components

### Buttons
Primary CTAs are solid Burnt Orange with black or deep grey text, using a heavy weight. They should have a "pressed" state that shifts the color to a deeper rust tone, rather than moving the element. Secondary buttons are outlined in Slate with no fill.

### Cards
Cards are treated as "Slabs." They feature a 1px Slate border and a subtle texture overlay. There is no hover elevation (shadow); instead, hover states should trigger a subtle increase in border brightness or a slight zoom of the background texture.

### Inputs
Fields are rectangular, heavy-bordered boxes. Labels sit above the field in "label-caps" typography. Focus states change the border color to Burnt Orange.

### Chips/Tags
Used for material types (e.g., "Basalt," "Travertine"). These should be styled as small, solid Slate blocks with high-contrast light text, resembling masonry samples.

### Image Containers
Since the product is visual, images should always fill their containers entirely. Apply a very subtle inner-stroke (1px semi-transparent white) to give the photo a "beveled" edge look inside the frame.

### Navigation
The navigation bar should feel like a heavy header stone, fixed at the top with a semi-opaque Slate background and a 2px bottom border that spans the full width of the viewport.