---
name: Heritage-Restore Design System
colors:
  surface: '#fef8f2'
  surface-dim: '#dfd9d3'
  surface-bright: '#fef8f2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f3ec'
  surface-container: '#f3ede6'
  surface-container-high: '#ede7e1'
  surface-container-highest: '#e7e2db'
  on-surface: '#1d1b18'
  on-surface-variant: '#524342'
  inverse-surface: '#32302c'
  inverse-on-surface: '#f6f0e9'
  outline: '#857372'
  outline-variant: '#d7c2c0'
  surface-tint: '#8a4d4b'
  primary: '#2f0608'
  on-primary: '#ffffff'
  primary-container: '#4a1a1a'
  on-primary-container: '#c57e7b'
  inverse-primary: '#ffb3b0'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#161610'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a2a24'
  on-tertiary-container: '#939188'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b0'
  on-primary-fixed: '#380c0d'
  on-primary-fixed-variant: '#6e3635'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e5e2d9'
  tertiary-fixed-dim: '#c9c6bd'
  on-tertiary-fixed: '#1c1c16'
  on-tertiary-fixed-variant: '#484740'
  background: '#fef8f2'
  on-background: '#1d1b18'
  surface-variant: '#e7e2db'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Source Sans Three
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Source Sans Three
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Source Sans Three
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

The design system is rooted in the concepts of **stewardship, craftsmanship, and timelessness**. It is designed to evoke the feeling of a private library or a master craftsman’s atelier. The target audience consists of high-net-worth individuals and institutional conservators who value historical integrity over fleeting trends.

The aesthetic follows a **Tactile & Refined** approach. It leverages physical metaphors—such as heavy paper stock, gold leaf filigree, and polished wood—translated into a digital interface. The goal is to establish immediate trust through a visual language that feels established and authoritative, yet mobile-responsive and effortless to navigate.

## Colors

The palette is a sophisticated trio that mimics the materials of historical restoration:

*   **Deep Mahogany (#4A1A1A):** Used for structural elements, borders, and primary brand moments. It represents the "wood" and "foundation" of the firm.
*   **Parchment (#F5F2E8):** The primary canvas for all interfaces. It reduces eye strain and provides a warm, archival background that feels more prestigious than pure white.
*   **Gold Accents (#D4AF37):** Reserved for interactive highlights, call-to-action buttons, and decorative dividers. It should be used sparingly to maintain its "precious" quality.
*   **Ink (#2C2A26):** A near-black with warm undertones used for body text to ensure high legibility against the parchment background.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage with modern utility.

**Playfair Display** is used for all headlines and display text. Its high-contrast strokes and elegant terminals evoke 18th-century copperplate engraving. It should be set with slightly tighter letter-spacing for large displays.

**Source Sans Three** serves as the workhorse for body copy and UI labels. It was chosen for its exceptional legibility and neutral character, which allows the serif headlines to remain the focal point. Use the Bold weight sparingly for emphasis within paragraphs.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to maintain a "book-like" centered composition, transitioning to a flexible fluid grid for mobile devices. 

A strict 8px spacing rhythm ensures consistency. Generous whitespace (macro-spacing) is encouraged to allow the parchment textures and mahogany borders to "breathe," reinforcing the feeling of luxury. Sections should be separated by significant vertical padding (stack-lg) to prevent the interface from feeling cluttered or "discount."

## Elevation & Depth

Elevation in this design system is achieved through **Material Layering** rather than aggressive shadows. 

1.  **Base Layer:** The Parchment (#F5F2E8) background, ideally featuring a subtle, non-repeating paper grain texture.
2.  **Raised Layer:** Parchment-colored cards that use a 1px Mahogany border or a very soft, warm-tinted ambient shadow (4% opacity #4A1A1A) to suggest they are sitting on top of the base.
3.  **Accent Depth:** Gold elements should utilize a subtle linear gradient (from #D4AF37 to #B8962E) to simulate a metallic foil effect, providing a sense of physical "stamping" into the surface.

## Shapes

The design system employs **Sharp (0px)** corners for all structural elements. This choice reflects the precision of architectural blueprints and the crisp edges of hand-cut stone or wood. 

Small UI elements like checkboxes or input fields may use a negligible 1px radius only if required for browser rendering clarity, but the overarching visual directive is "sharp and deliberate."

## Components

### Buttons
Primary buttons are solid Mahogany (#4A1A1A) with Gold (#D4AF37) text, set in uppercase Source Sans Three. Secondary buttons utilize a Mahogany 1px border with a "Gold Foil" hover state where the border thickness increases slightly.

### Cards
Cards are the primary container for property listings and historical records. They feature a parchment background and a mandatory 1px Mahogany border. For "featured" properties, add a 2px Gold top-border.

### Dividers
Use "Foil Dividers"—a 1px horizontal line in Gold (#D4AF37). For section breaks, a decorative flourish (like a centered diamond or small crest icon) may be placed in the middle of the divider.

### Input Fields
Fields should be styled as "Underlined" rather than boxed, mimicking a ledger. Use Mahogany for the underline and Parchment for the fill. The active state changes the underline to Gold.

### Navigation
The navigation bar should be fixed and minimalist, using high-contrast Playfair Display for the brand mark and Source Sans Three for menu items. Mobile menus should use a full-screen Parchment overlay with Mahogany text.