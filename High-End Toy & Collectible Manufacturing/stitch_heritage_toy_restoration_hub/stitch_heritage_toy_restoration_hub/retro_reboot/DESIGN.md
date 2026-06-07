---
name: Retro-Reboot
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3e4949'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#6e7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#006a6a'
  primary: '#006565'
  on-primary: '#ffffff'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#76d6d5'
  secondary: '#775a00'
  on-secondary: '#ffffff'
  secondary-container: '#fec72c'
  on-secondary-container: '#6f5400'
  tertiary: '#5a5a59'
  on-tertiary: '#ffffff'
  tertiary-container: '#737272'
  on-tertiary-container: '#fbf8f8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#ffdf98'
  secondary-fixed-dim: '#f5bf22'
  on-secondary-fixed: '#251a00'
  on-secondary-fixed-variant: '#5a4300'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 16px
  margin-mobile: 20px
---

## Brand & Style
The brand personality of this design system is a sophisticated blend of archival reverence and vibrant energy. It targets collectors and enthusiasts who value the precision of modern restoration applied to the soul of vintage objects. The emotional response is one of "premium nostalgia"—evoking the excitement of a new toy arrival while maintaining the gravitas of high-end craftsmanship.

The design style utilizes **Brutalism** as its foundation, characterized by bold, unapologetic geometry and thick structural borders. This is softened by **Tactile** elements like subtle grain textures that mimic toy plastics and printed cardstock. High-resolution photography of toy textures (chipped paint vs. polished chrome) provides the "High-End" contrast against the flat, graphic UI.

## Colors
The palette is rooted in a "Nostalgic-Vibrant" spectrum. **Retro Teal** serves as the primary brand anchor, providing a cool, professional depth. **Mustard Yellow** acts as the high-energy accent for calls to action and interactive states, reminiscent of 80s warning labels and racing stripes. 

**Off-White** is the essential canvas, used for backgrounds to prevent the high-contrast elements from feeling sterile. **Charcoal** is reserved for text and structural "Thick Borders" (2px to 4px), ensuring maximum readability and a graphic, comic-book-like definition.

## Typography
Typography in this design system emphasizes structural integrity. **Space Grotesk** is used for all headings and labels; its geometric quirks reflect the "Retro-Tech" aesthetic of the 1980s. Headings should be set with tight line-heights to feel like solid blocks of information.

**Inter** provides a clean, utilitarian balance for body copy. It is highly legible against grained backgrounds and ensures that technical restoration details are easy to digest. Use the `label-caps` style for small metadata or toy specifications to maintain the "archival" look.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy within a mobile-first framework. On mobile, a 4-column grid is used with generous 20px side margins to "frame" the content like a boxed toy. Desktop layouts expand to a 12-column grid, keeping content contained within a max-width to maintain the premium, editorial feel.

Spacing is governed by an 8px base unit. Consistent use of `md` (24px) for internal padding within cards and `lg` (48px) for vertical section breathing room creates a rhythmic, organized structure that counters the "loud" colors and thick borders.

## Elevation & Depth
Depth is conveyed through **Bold Borders** and **Hard Offsets** rather than ambient shadows. This design system avoids blurs. Instead, it uses:
- **Layered Fills:** A secondary color "shadow" block placed 4px to 8px behind a primary card (the "Hard Shadow" look).
- **Thick Outlines:** All interactive or distinct containers must have a minimum 2px Charcoal border.
- **Grain Overlays:** A subtle noise texture (opacity 3-5%) is applied to the top layer of all large color blocks to give them a physical, material quality that mimics vintage plastic or matte-finished metal.

## Shapes
Geometry is uncompromising. This design system uses **Sharp Corners** (0px radius) for every UI element, from buttons and cards to input fields. This choice reinforces the "mechanical" and "heritage" nature of toy manufacturing. To create visual variety, use diagonal "clipped corners" (45-degree cuts) on specific accent elements like price tags or status chips, suggesting a vintage punch-card or label aesthetic.

## Components
- **Cards:** White or Teal backgrounds with 3px Charcoal borders. Content is padded heavily (24px). Header sections of cards may use a Mustard Yellow background for immediate hierarchy.
- **Buttons:** Rectangular with no rounding. Primary buttons use Mustard Yellow with a Charcoal border and a 4px bottom-right Charcoal "hard shadow" offset.
- **Restoration Slider:** A high-contrast vertical handle (Teal) with a Mustard Yellow center icon. The "Before" side is slightly desaturated, while the "After" side features high-resolution photography with the subtle grain overlay.
- **Input Fields:** Simplified boxes with 2px borders. Labels use the `label-caps` typography style and sit outside the field.
- **Chips:** Small, sharp-cornered rectangles with Teal borders and Space Grotesk text, used for toy categories or condition grades.
- **Progress Bars:** Thick, blocky bars that fill with Mustard Yellow, moving in discrete segments rather than a smooth fluid motion to mimic 8-bit loading sequences.