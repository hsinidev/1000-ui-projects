---
name: Heritage Preservation Interface
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#544341'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#877270'
  outline-variant: '#dac1bf'
  surface-tint: '#954742'
  primary: '#2a0002'
  on-primary: '#ffffff'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#ffb3ad'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
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
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  display-lg:
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
    lineHeight: '1.3'
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
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  margin-mobile: 24px
  gutter: 16px
  section-gap: 48px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style

The brand personality is authoritative, reverent, and academic yet accessible. It functions as a digital museum, prioritizing the weight of history over modern trends. The target audience includes cultural researchers, global historians, and curious digital explorers seeking deep immersion into human legacy.

The design system employs a **Tactile / Skeuomorphic** approach blended with **Minimalism**. It utilizes the physical metaphors of a curated archive—parchment textures, deckle edges, and ink-press effects—while maintaining the clean structural integrity required for mobile-first navigation. The emotional response is one of "discovered treasure": the UI should feel like a rare manuscript being unfolded on a high-definition screen.

## Colors

The palette is rooted in classical materials. **Parchment (#F4EBD0)** serves as the primary canvas, providing a warm, non-glare background that mimics aged paper. **Deep Burgundy (#4A0E0E)** is used for primary actions and structural headers, signifying the "seal" of authenticity. **Gold (#D4AF37)** is reserved for accents, highlights, and decorative borders, representing the precious nature of the preserved content.

Text is rendered in a deep charcoal (#2D2926) rather than pure black to maintain a softer, ink-on-paper contrast. Functional states (success/error) should be muted to match this historical tone—use ochre for warnings and deep forest green for success.

## Typography

This design system utilizes **Newsreader** for all storytelling and editorial components. Its variable optical sizes allow for high legibility at large display scales and classic "bookish" feel at smaller headline scales. Italics should be used frequently for quotes and botanical/cultural nomenclature.

**Inter** provides the functional backbone. It is used for UI labels, metadata, and dense body copy where clarity is paramount on mobile devices. The juxtaposition of the traditional serif with the utilitarian sans-serif creates a "curated archive" aesthetic—where the content is historical, but the preservation method is modern.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for vertical scrolling and long-form storytelling. On mobile, a 4-column grid is used with generous 24px side margins to create a "framed" effect, reminiscent of a printed page. 

The spacing rhythm is based on an 8px scale, but utilizes "breathable" white space (or parchment space) to prevent the UI from feeling cluttered. Content blocks are separated by significant vertical gaps (48px+) to allow the archival photography to command full attention before the user transitions to the next narrative segment.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and texture rather than heavy drop shadows. 
- **Surface:** The base Parchment layer.
- **Elevation 1:** Use subtle inner-glows and very faint, large-radius shadows (opacity < 5%) to suggest paper being laid upon paper.
- **Dividers:** Instead of standard grey lines, use thin Gold (#D4AF37) rules or "double-line" borders to separate sections.
- **Imagery:** Archival photos should have a slight "inset" shadow to appear as if they are physically mounted to the page. 

Avoid modern blurs or neon glows; the depth should feel like the physical thickness of heavy-weight paper or cardstock.

## Shapes

The shape language is strictly **Sharp (0px)**. 

To evoke the feel of historical documents and maps, UI elements such as buttons, input fields, and cards utilize 90-degree corners. Rounded corners are perceived as too modern and "friendly" for this serious subject matter. Softness is instead introduced through texture—using masking to create "deckle" or torn-paper edges on the top and bottom of full-width containers to break the rigid digital grid.

## Components

**Buttons:** Solid Deep Burgundy with Gold text for primary actions. Use a "ghost" style with a 1px Gold border for secondary actions. Always use uppercase labels with increased tracking.

**Cards:** Cards are styled as "Archive Folders." They feature a subtle parchment texture, a thin gold border, and no shadow. The header of the card uses Newsreader in a smaller, bold weight.

**Input Fields:** Bottom-border only, mimicking a signature line on a document. Labels should float above the line in a small Inter caps font.

**Refined Borders:** Use decorative "corner brackets" in Gold to frame high-end archival photography.

**Scroll Progress:** A vertical "ink line" that grows as the user moves through the story, reinforcing the storytelling focus.

**Chips/Tags:** Styled as "Museum Labels"—small, rectangular blocks with a thin border and monospaced-style Inter text to represent cataloging numbers.