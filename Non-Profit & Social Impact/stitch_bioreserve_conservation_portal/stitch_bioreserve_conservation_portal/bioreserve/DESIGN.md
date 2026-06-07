---
name: BioReserve
colors:
  surface: '#131410'
  surface-dim: '#131410'
  surface-bright: '#3a3935'
  surface-container-lowest: '#0e0e0b'
  surface-container-low: '#1c1c18'
  surface-container: '#20201c'
  surface-container-high: '#2a2a26'
  surface-container-highest: '#353530'
  on-surface: '#e5e2db'
  on-surface-variant: '#c3c8c1'
  inverse-surface: '#e5e2db'
  inverse-on-surface: '#31312c'
  outline: '#8d928c'
  outline-variant: '#434843'
  surface-tint: '#b4cdb8'
  primary: '#b4cdb8'
  on-primary: '#203527'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#4d6453'
  secondary: '#d6c692'
  on-secondary: '#3a3009'
  secondary-container: '#544820'
  on-secondary-container: '#c8b885'
  tertiary: '#b9c9d3'
  on-tertiary: '#23323a'
  tertiary-container: '#1f2e36'
  on-tertiary-container: '#86969f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#f3e2ac'
  secondary-fixed-dim: '#d6c692'
  on-secondary-fixed: '#231b00'
  on-secondary-fixed-variant: '#51461e'
  tertiary-fixed: '#d5e5ef'
  tertiary-fixed-dim: '#b9c9d3'
  on-tertiary-fixed: '#0e1d25'
  on-tertiary-fixed-variant: '#3a4951'
  background: '#131410'
  on-background: '#e5e2db'
  surface-variant: '#353530'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
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
    lineHeight: '1'
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
  container-margin: 20px
  gutter: 16px
  section-gap: 48px
---

## Brand & Style
This design system is built on the philosophy of **Tactile Minimalism**. It captures the urgent, stoic reality of wildlife conservation by blending raw environmental textures with a high-performance digital interface. The target audience includes conservationists, donors, and field researchers who require a tool that feels as grounded as the earth they protect.

The aesthetic avoids "techy" artifice, favoring an immersive experience that uses full-bleed photography to bring the user into the habitat. Visual interest is driven by a paper-like grain and organic shapes that mimic the irregularities of nature, moving away from the clinical perfection of standard SaaS interfaces.

## Colors
The palette is rooted in the "Deep Jungle Green," which serves as the primary canvas for the dark-mode interface. "Sand" is reserved for high-priority calls to action and critical data points, providing a high-contrast warmth against the cool forest tones. "Slate" functions as the secondary surface color, used to distinguish UI containers from the background.

To maintain the "Raw" aesthetic, avoid pure blacks. The dark-mode experience relies on the deep green for depth, while the neutral "Off-White/Sand" accents ensure readability. Use low-opacity versions of Slate for overlays to maintain the visibility of background imagery.

## Typography
The typography pairing establishes an "archival yet modern" tone. **Newsreader** provides the literary, authoritative weight needed for environmental storytelling and species profiles. Its serif structure feels grounded and traditional.

**Work Sans** is used for all functional interface elements and long-form data. It provides the necessary clarity and neutral balance to the expressive headings. Use the `label-caps` style for category tags and small UI metadata to ensure distinct hierarchy without overwhelming the page with serif text.

## Layout & Spacing
This design system utilizes a **Fluid Grid** optimized for mobile-first immersion. On mobile devices, a 4-column structure with 20px outer margins is standard. For desktop, the grid expands to 12 columns with a maximum content width of 1280px.

A key layout feature is the "Immersive Breakout": specific image or video modules should ignore grid margins to span the full width of the viewport, creating a cinematic rhythm. Vertical spacing is generous to reflect the openness of natural landscapes, using a base 8px increment.

## Elevation & Depth
Depth is communicated through **Tonal Layering** and texture rather than traditional shadows. Surfaces do not "float"; they are stacked. 

1. **Base Layer:** Deep Jungle Green (#1B3022) with a subtle grain texture overlay.
2. **Surface Layer:** Slate (#2F3E46) at 80-90% opacity, allowing hints of the background imagery to bleed through.
3. **Interactive Layer:** Sand (#C2B280) for elements that require immediate attention.

Avoid drop shadows. If depth is required for readability over complex images, use a soft gradient scrim or a 1px Slate border to define the edge.

## Shapes
The shape language is **Organic**. While the base `roundedness` is set to 2 (0.5rem), this design system encourages "squircle" variations and non-uniform corner radii (e.g., 24px, 4px, 24px, 4px) for featured image masks. This mimics the irregular shapes found in leaves, stones, and maps. Buttons should remain consistently rounded (level 2) to ensure they are recognizable as interactive elements.

## Components
- **Buttons:** Primary buttons use the Sand (#C2B280) background with Deep Jungle Green text. Secondary buttons are "Ghost" style with a 1.5px Slate border.
- **Cards:** Use "Themed Containers" with a subtle paper texture. Headlines within cards should be Newsreader, while metadata uses Work Sans.
- **Lists:** Use horizontal dividers with a low-opacity Slate stroke (15% opacity). List items should have generous vertical padding (16px+).
- **Input Fields:** Bottom-border only or fully enclosed with a Slate background. Focus states are indicated by a Sand underline.
- **Species Chips:** Small, organic-shaped badges with a low-contrast Slate background and Sand text, used for conservation status (e.g., "Endangered").
- **Immersive Progress Bars:** Thick, textured bars showing population recovery or habitat coverage, using Sand as the "fill" color against a Slate background.
- **Media Controls:** Minimalist, high-contrast icons placed directly on full-bleed imagery, utilizing a subtle backdrop blur for legibility.