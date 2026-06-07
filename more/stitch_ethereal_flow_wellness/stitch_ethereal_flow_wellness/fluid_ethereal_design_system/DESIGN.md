---
name: Fluid & Ethereal Design System
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#46464c'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#77767d'
  outline-variant: '#c7c5cc'
  surface-tint: '#5c5d6e'
  primary: '#5c5d6e'
  on-primary: '#ffffff'
  primary-container: '#e6e6fa'
  on-primary-container: '#656677'
  inverse-primary: '#c5c5d8'
  secondary: '#74593f'
  on-secondary: '#ffffff'
  secondary-container: '#fed9b8'
  on-secondary-container: '#795d43'
  tertiary: '#5c5f60'
  on-tertiary: '#ffffff'
  tertiary-container: '#e7e8e9'
  on-tertiary-container: '#666869'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e1f5'
  primary-fixed-dim: '#c5c5d8'
  on-primary-fixed: '#191b29'
  on-primary-fixed-variant: '#444655'
  secondary-fixed: '#ffdcbe'
  secondary-fixed-dim: '#e3c0a0'
  on-secondary-fixed: '#2a1704'
  on-secondary-fixed-variant: '#5a422a'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  headline-display:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
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
    lineHeight: '1.6'
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  safe-margin: 40px
  gutter: 24px
  fluid-gap-lg: 80px
  fluid-gap-md: 48px
---

## Brand & Style
This design system is anchored in the concept of "Digital Sanctuary." It targets a wellness-conscious audience seeking refuge from the cluttered, high-frequency interfaces of modern life. The brand personality is serene, nurturing, and sophisticated, evoking the feeling of a quiet morning or a tranquil spa.

The visual style is a hybrid of **Glassmorphism** and **Minimalism**, prioritizing breathability and soft transitions. By utilizing organic, anti-grid shapes and luminous gradients, the UI creates an immersive atmosphere that feels more like a living environment than a static tool. Every interaction is designed to feel effortless and fluid, reinforcing a sense of premium quality and emotional well-being.

## Colors
The palette is centered on a "Luminous Dawn" spectrum. The primary Lavender (#E6E6FA) and secondary Peach (#FFDAB9) are never used in isolation; they are applied as soft, radial, or linear gradients to create depth and movement. 

The color mode is strictly light to maintain an airy and optimistic feel. Surface colors utilize high-transparency whites to allow background gradients to bleed through, creating a sense of ethereal layering. Neutral tones are kept soft—avoiding pure blacks in favor of deep, warm grays to maintain the premium, gentle aesthetic.

## Typography
The typography strategy relies on a sophisticated contrast between two distinct families. **Noto Serif** is used for all headings to provide a sense of timeless elegance and literary authority. It should be typeset with generous leading and occasionally slightly negative letter-spacing for a high-end editorial look.

**Manrope** serves as the functional counterpart for body copy and UI labels. Chosen for its geometric clarity and balanced proportions, it ensures legibility within translucent glass containers. To maintain the "airy" feel, text blocks should be kept concise with wide margins and ample line-height to prevent the interface from feeling crowded.

## Layout & Spacing
The layout philosophy moves away from rigid, box-based structures toward a **Fluid & Overlapping** model. While an underlying grid exists for alignment, elements should frequently break the grid with "anti-grid" placements—organic shapes that drift behind or between content blocks to create a sense of interconnectedness.

Spacing is generous and used as a tool for storytelling. Large vertical gaps (fluid-gap-lg) are used to separate major thematic sections, allowing the background gradients to breathe. Components should use wide internal padding to emphasize the pebble-like, soft nature of the containers.

## Elevation & Depth
Depth in this design system is achieved through **Glassmorphism** and **Ambient Light**. Instead of traditional drop shadows, elevation is conveyed through:

1.  **Backdrop Blurs:** Surface containers use a blur radius of 20px to 40px, creating a frosted glass effect that tints the background colors.
2.  **Luminous Outlines:** A 1px semi-transparent white border on the top and left edges of components simulates a "rim light" hitting a physical glass object.
3.  **Colored Shadows:** High-elevation elements use extremely diffused (60px+ blur), low-opacity shadows that are tinted with the primary Lavender or Peach colors rather than neutral grays. This keeps the shadows feeling "luminous" rather than heavy.

## Shapes
The shape language is strictly organic. Sharp corners are forbidden. This design system uses "Pebble-like" geometry, where corner radii are aggressively high to mimic water-worn stones. 

Beyond standard components, the system utilizes "Blob" shapes—non-geometric, vector paths—as background accents. These blobs should have soft, blurred edges and appear to "float" or "drift" behind the main content layers, breaking up the linear flow of the page.

## Components
Consistent styling across components is vital to maintaining the ethereal atmosphere:

*   **Buttons:** Primary buttons are pill-shaped with a soft gradient fill. Secondary buttons use the "Glass" effect with a luminous border. All hover states should involve a subtle expansion in size and an increase in backdrop blur intensity.
*   **Cards:** Containers for content must be translucent. They should not have visible background colors but rather a `backdrop-filter: blur()` and a thin, semi-transparent white stroke. 
*   **Chips & Tags:** Small, pill-shaped elements with high transparency and Noto Serif labels for a premium touch.
*   **Input Fields:** Ghost-style inputs with a soft underline or a very subtle glass container. The focus state should be a soft glow rather than a hard border.
*   **Progress Indicators:** Use fluid, wave-like animations rather than standard bars or circles to represent completion or loading states.
*   **Floating Navigation:** A bottom-anchored, glassmorphic navigation bar with high roundedness, appearing to hover over the page content.