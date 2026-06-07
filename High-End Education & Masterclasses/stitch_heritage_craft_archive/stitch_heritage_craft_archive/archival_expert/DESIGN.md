---
name: Archival-Expert
colors:
  surface: '#fff8f6'
  surface-dim: '#e6d7d3'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ed'
  surface-container: '#fbeae6'
  surface-container-high: '#f5e5e1'
  surface-container-highest: '#efdfdb'
  on-surface: '#221a17'
  on-surface-variant: '#54433e'
  inverse-surface: '#372e2c'
  inverse-on-surface: '#feede9'
  outline: '#87736d'
  outline-variant: '#dac1ba'
  surface-tint: '#944930'
  primary: '#91462e'
  on-primary: '#ffffff'
  primary-container: '#af5e44'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb59e'
  secondary: '#665e4b'
  on-secondary: '#ffffff'
  secondary-container: '#ebdec6'
  on-secondary-container: '#6a624f'
  tertiary: '#5c5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#757474'
  on-tertiary-container: '#fffcfb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#ffb59e'
  on-primary-fixed: '#3a0b00'
  on-primary-fixed-variant: '#76321c'
  secondary-fixed: '#ede1c9'
  secondary-fixed-dim: '#d1c5ae'
  on-secondary-fixed: '#211b0c'
  on-secondary-fixed-variant: '#4d4634'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#fff8f6'
  on-background: '#221a17'
  surface-variant: '#efdfdb'
typography:
  display-xl:
    fontFamily: Libre Caslon Text
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
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
  label-sm:
    fontFamily: Work Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 80px
---

## Brand & Style
This design system is anchored in the concept of the "Modern Atelier." It balances the weight of heritage with the clarity of high-end digital education. The brand personality is that of a master artisan: patient, precise, and deeply knowledgeable. 

The visual style is **Tactile-Minimalism**. It leverages physical metaphors—specifically paper textures, leather-like grain, and the precision of a watchmaker’s loupe—to evoke a sense of permanence and quality. The UI should never feel "plastic" or disposable; every element should feel curated and archived. The "Detail-Loupe" motif is used to signify moments of deep focus and expert insight, where the UI zooms in on high-resolution craftsmanship.

## Colors
The palette is rooted in natural, raw materials. 
- **Terra-Cotta (#C26D52):** Used for primary actions, progress indicators, and key highlights. It represents the warmth of the workshop and the human hand.
- **Sand (#E8DCC4):** The secondary surface color, used to create a "parchment" or "canvas" backdrop for content blocks.
- **Deep Charcoal (#2C2C2C):** Reserved for high-contrast typography and structural elements, providing the "ink" that anchors the design.
- **Neutral Base (#F9F6F0):** A warm off-white used as the global background to prevent the clinical feel of pure white, enhancing the archival aesthetic.

## Typography
This design system utilizes a classic serif/sans-serif pairing to distinguish between "Tradition" and "Utility."
- **Headings:** **Libre Caslon Text** is the voice of authority. Its historical roots in publishing make it ideal for conveying expertise. Large display sizes should use tighter letter-spacing to feel more like a premium editorial.
- **Body & Interface:** **Work Sans** provides a grounded, neutral counter-balance. Its high legibility at small sizes ensures that complex technical instructions in the craft courses remain accessible.
- **Labels:** Use uppercase Work Sans with increased tracking for a clean, "cataloged" look, reminiscent of museum archives or technical blueprints.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy to mirror the structured pages of a physical archive or a rare book. 
- Use a 12-column grid for desktop with generous 64px margins to allow the content to "breathe" and maintain a premium feel.
- Vertical rhythm is strictly based on 8px increments. 
- Content density should be kept low; white space (or "sand space") is a critical luxury asset in this system, signaling that the user's time and focus are respected.

## Elevation & Depth
Depth is created through **Tonal Layering** and soft, artisanal shadows rather than aggressive light sources.
- **Level 1 (Base):** The parchment background (#F9F6F0).
- **Level 2 (Inlay):** Elements like input fields or secondary modules use a slightly darker Sand (#E8DCC4) or a subtle 1px "Deep Charcoal" stroke at 10% opacity.
- **Level 3 (Raised):** Cards and primary modules use a very soft, diffused shadow (Blur: 20px, Y: 4px, Color: Deep Charcoal at 5% opacity) to suggest they are laying on top of the paper surface.
- **Detail-Loupe State:** When an element is focused or inspected, it should use a circular mask and a slightly higher elevation (Level 4) to "magnify" it above the rest of the UI.

## Shapes
The shape language is **Soft-Organic**. While the grid is structured, the elements themselves avoid harsh 90-degree angles to feel more natural and hand-finished. 
- Standard components use a 4px (Soft) radius.
- Larger cards use an 8px radius.
- The "Detail-Loupe" motif is the only perfectly circular element, creating a distinct visual contrast against the otherwise rectangular, book-like layout.
- Icons should use a medium stroke weight (1.5pt to 2pt) with slightly rounded terminals to match the typography.

## Components
- **Buttons:** Primary buttons are solid Terra-Cotta with white or Sand text. Use a subtle inner-shadow (1px, top-down) to give a "pressed" or "embossed" tactile feel.
- **Cards:** Content containers use the Sand background with a very fine 1px Charcoal border at low opacity. They should never be pure white.
- **Detail-Loupe Inspection:** A specialized component for viewing high-res imagery (e.g., watch movements). This is a circular floating frame that magnifies the content beneath it on hover or drag.
- **Inputs:** Form fields should look like ledger entries—clean underlines or subtle Sand boxes with labels in the "Label-sm" style positioned above the line.
- **Progress Markers:** For educational courses, use a "stitched" line aesthetic—dashed lines that become solid Terra-Cotta as modules are completed, referencing bespoke tailoring.
- **Chips/Tags:** Use a "Wax Seal" or "Stamp" metaphor—low-contrast background colors with centered, high-tracking text.