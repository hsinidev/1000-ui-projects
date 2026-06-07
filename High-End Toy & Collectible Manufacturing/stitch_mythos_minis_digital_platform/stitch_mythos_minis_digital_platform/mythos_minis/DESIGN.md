---
name: Mythos-Minis
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c3c8c1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8d928c'
  outline-variant: '#434843'
  surface-tint: '#b4cdb8'
  primary: '#b4cdb8'
  on-primary: '#203527'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#4d6453'
  secondary: '#ccc6b3'
  on-secondary: '#333123'
  secondary-container: '#4a4738'
  on-secondary-container: '#bab5a3'
  tertiary: '#ffb596'
  on-tertiary: '#581e00'
  tertiary-container: '#501a00'
  on-tertiary-container: '#d47b53'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#e8e2cf'
  secondary-fixed-dim: '#ccc6b3'
  on-secondary-fixed: '#1e1c10'
  on-secondary-fixed-variant: '#4a4738'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#76320f'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1-display:
    fontFamily: Newsreader
    fontSize: 4rem
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2-heading:
    fontFamily: Newsreader
    fontSize: 2.5rem
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0em
  h3-subheading:
    fontFamily: Newsreader
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Manrope
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Manrope
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-edge: 40px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built to evoke the atmosphere of an ancient, high-fantasy archive. The brand personality is scholarly yet dangerous, appealing to hobbyists who view miniatures not just as toys, but as high-art artifacts. The emotional response is one of discovery and reverence, as if the user is leafing through a forbidden tome or uncovering relics in a forgotten temple.

The visual style is **Tactile / Skeuomorphic**. It moves away from the flat trends of modern SaaS, embracing the physicality of the hobby. Every interface element should feel heavy and permanent. Key characteristics include:
- **Atmospheric Depth:** A mix of dark, light-absorbing surfaces and illuminated parchment.
- **Material Honesty:** Digital surfaces mimic stone, vellum, and oxidized metal.
- **Macro Focus:** Using high-detail photography of miniatures as the primary visual anchor, often breaking the bounds of traditional containers to emphasize the "object" nature of the product.

## Colors

The palette is rooted in natural, earthy pigments that suggest a dark forest setting.

- **Deep Forest Green (#1B3022):** Used for primary backgrounds and high-level containers. It represents the "void" of the forest and provides a moody foundation.
- **Parchment (#F0EAD6):** Used for primary content areas where legibility is paramount. It acts as the "light" in the darkness, mimicking aged vellum.
- **Burnt Sienna (#A0522D):** Used as the primary action color. It evokes dried clay, rusted iron, or wax seals, providing a warm contrast to the green.
- **Neutral / Shadow:** Deep obsidian blacks are used for true shadows and to ground the UI elements.

Apply color with a "layering" logic: the furthest background is Deep Forest Green, while interactive or informational "scrolls" are Parchment.

## Typography

This design system utilizes a high-contrast typographic pairing to balance flavor with functionality.

- **Headlines (Newsreader):** A sophisticated serif that brings a literary, authoritative feel. Use it for titles, product names, and section headers. High-contrast strokes should be emphasized at larger scales.
- **Body & Labels (Manrope):** A modern, geometric sans-serif that ensures clarity when reading technical miniature specs or assembly instructions. 
- **Styling Note:** For H1 and H2 levels, use "Oldstyle" figures if available to reinforce the antique aesthetic. Labels should frequently use increased letter spacing and uppercase styling to mimic the markings on a map or a technical diagram.

## Layout & Spacing

The layout follows a **Fixed Grid** approach for primary content to maintain the feeling of a structured book or ledger. 

- **Grid:** A 12-column system with generous gutters (24px) to allow the "stone" and "forest" backgrounds to breathe between content pieces.
- **Rhythm:** Spacing follows an 8px base unit. Use larger vertical stacks (64px+) between sections to suggest chapters or distinct artifact groupings.
- **Composition:** Asymmetric layouts are encouraged for gallery sections to mimic a collector's table, while checkout and technical data should remain strictly aligned to the grid for trust and clarity.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layers** and **Physical Metaphors** rather than standard drop shadows.

- **Surface Tiers:** The "Base" is the Deep Forest Green. Elements placed "on top" (like cards or menus) use a subtle stone texture overlay. 
- **Inner Shadows:** Use subtle inner shadows on input fields and containers to make them appear carved into the surface.
- **Weathered Borders:** Instead of clean 1px lines, use "stamped" or "rough-edge" borders. Borders on Parchment surfaces should appear slightly bled or ink-stained.
- **Tactile Shadows:** When shadows are used (e.g., for floating action buttons or miniature previews), they should be high-offset and soft, suggesting a single directional light source like a candle or torch.

## Shapes

The shape language is primarily **Sharp (0)**. 

To maintain the "carved" and "hand-cut" feel, avoid perfectly rounded corners. Rectangular forms should feel like blocks of stone or cut sheets of vellum. 

- **Exceptions:** Use "clipped" or "notched" corners (45-degree cuts) for buttons and status tags to suggest medieval heraldry or stonework. 
- **Detailing:** Interactive elements can feature thin, double-line borders (a thick outer line and a hair-line inner stroke) to mimic bookbinding details.

## Components

- **Buttons:** Primary buttons use a solid Burnt Sienna background with notched corners. Hover states should involve a subtle "glow" effect, as if the element is being heated. Text is always uppercase Manrope with high tracking.
- **Cards:** Product cards use the Parchment background for the content area, with a Deep Forest Green "header" for the macro photography. Borders are weathered and dark.
- **Inputs:** Text fields appear as recessed slots carved into the UI. Use a dark background (#0D0D0D) with a thin Burnt Sienna border when focused.
- **Chips/Tags:** Used for "In-Stock" or "Limited Edition" markers. These should look like wax seals or stamped leather patches.
- **Progress Indicators:** Use a "melting candle" or a "filling ink-well" metaphor for loading states and progress bars.
- **Modals:** Modals should take the form of an unrolling scroll or a heavy stone tablet appearing over a dimmed, blurred background.