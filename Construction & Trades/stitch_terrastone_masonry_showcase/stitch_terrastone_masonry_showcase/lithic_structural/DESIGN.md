---
name: Lithic Structural
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#56423e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#89726d'
  outline-variant: '#ddc0ba'
  surface-tint: '#9f402d'
  primary: '#9f402d'
  on-primary: '#ffffff'
  primary-container: '#e2725b'
  on-primary-container: '#5a0d02'
  inverse-primary: '#ffb4a5'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5e604d'
  on-tertiary: '#ffffff'
  tertiary-container: '#93947e'
  on-tertiary-container: '#2b2d1c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad3'
  primary-fixed-dim: '#ffb4a5'
  on-primary-fixed: '#3e0500'
  on-primary-fixed-variant: '#802918'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  technical-data:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 32px
  margin: 48px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

The design system is built upon the principles of geological permanence and engineering precision. It targets architects, developers, and high-end contractors who value the intersection of ancestral masonry and modern facade technology. The UI should evoke a sense of weight, stability, and "quiet strength"—avoiding flighty animations or neon accents in favor of a tactile, grounded experience.

The visual style is a hybrid of **Tactile/Skeuomorphism** and **Minimalism**. It utilizes physical metaphors of stone, mortar, and clay to create a sense of craftsmanship. Every digital element should feel as though it was hewn from physical material, emphasizing durability and the structural integrity inherent in masonry.

## Colors

The color palette is derived from raw, architectural materials. **Sandstone Beige** serves as the primary canvas, acting as a warm, expansive background that mimics light-washed facade panels. **Slate** provides the structural contrast, used for secondary elements, technical diagrams, and heavy accents. **Terracotta** is the primary "action" color, representing the warmth of kiln-fired ceramics and human craftsmanship.

Neutral tones are deep and earthy rather than pure black or grey, ensuring that even the highest-contrast elements feel part of a natural landscape. Use Terracotta sparingly for calls-to-action to ensure they stand out against the more muted Slate and Beige foundations.

## Typography

This design system utilizes a high-contrast typographic pairing to reflect the balance between art and engineering. **Newsreader** is used for all headlines; its traditional, authoritative serifs reflect the history of architecture and the permanence of stone. 

For body text and functional UI, **Work Sans** provides a grounded, straightforward reading experience. It is highly legible and neutral, ensuring that technical specifications and engineering data are easy to digest. Use the "label-caps" style for categorization and technical metadata to mimic the look of etched or stamped structural markings.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model, specifically a 12-column system that prioritizes generous gutters. This reflects the "joints" in masonry, where the space between elements is as important as the elements themselves. 

Vertical rhythm is strictly maintained in 8px increments to ensure a sense of mathematical order and structural reliability. Content should be grouped into monolithic blocks, separated by significant whitespace (stack-lg) to allow the "weight" of each section to be felt by the user.

## Elevation & Depth

Hierarchy in this design system is conveyed through **Tonal Layers** and **Subtle Textures** rather than traditional floating shadows. Surfaces do not "hover"; they are stacked or carved. 

- **Level 0 (Foundation):** Sandstone Beige background with a subtle, low-opacity grain texture.
- **Level 1 (Stacked):** Surfaces slightly lighter than the foundation with a crisp 1px "rugged" border (a slightly irregular stroke to mimic hand-cut stone).
- **Level 2 (Inlay):** Recessed elements (like input fields) use an inner shadow to appear carved into the surface.
- **Overlays:** Modals use a heavy Slate semi-transparent backdrop to focus the eye, suggesting a solid, darkened room.

## Shapes

The shape language is primarily **Soft (0.25rem)**, reflecting stone that has been weathered or professionally finished but retains its structural corners. Sharp 90-degree angles are used for large structural containers, while smaller interactive components (buttons, chips) use the soft roundedness to improve touch ergonomics and visual comfort. 

Borders should never be perfectly smooth; where possible, a subtle "chiseled" effect is applied via a high-frequency, low-amplitude stroke-dash array or a custom SVG filter to reinforce the masonry aesthetic.

## Components

### Buttons
Buttons are designed to feel like physical blocks. Primary buttons use a solid Terracotta fill with a subtle "chiseled" bottom border (2px darker shade). On press, they should appear to sink into the page using an inset shadow, rather than lifting.

### Cards & Containers
Cards feature the "Foundation" texture and a rugged Slate border. They should be used to house project case studies or technical details, appearing like stone slabs.

### Inputs & Selects
Input fields are "Inlay" components. They appear carved into the Sandstone background with a subtle inner shadow. The focus state replaces the Slate border with a thicker Terracotta border to signal activity.

### Chips & Tags
Chips use a Slate background with Sandstone text, resembling small metal identification tags often used in structural engineering.

### Additional Components: "The Spec Sheet"
A custom component for this design system is the "Spec Sheet"—a high-density data table with heavy vertical lines and mono-spaced numeric features, used for displaying facade performance metrics and material properties.