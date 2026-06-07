---
name: Architectural Excellence
colors:
  surface: '#fcf8f9'
  surface-dim: '#dcd9da'
  surface-bright: '#fcf8f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f4'
  surface-container: '#f0edee'
  surface-container-high: '#eae7e8'
  surface-container-highest: '#e5e2e3'
  on-surface: '#1b1b1c'
  on-surface-variant: '#4f4441'
  inverse-surface: '#303031'
  inverse-on-surface: '#f3f0f1'
  outline: '#817471'
  outline-variant: '#d3c3bf'
  surface-tint: '#6f5a53'
  primary: '#2f1f1a'
  on-primary: '#ffffff'
  primary-container: '#46342e'
  on-primary-container: '#b59c94'
  inverse-primary: '#dcc1b8'
  secondary: '#735a35'
  on-secondary: '#ffffff'
  secondary-container: '#fddaac'
  on-secondary-container: '#785e39'
  tertiary: '#212323'
  on-tertiary: '#ffffff'
  tertiary-container: '#363839'
  on-tertiary-container: '#a0a1a2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f9dcd3'
  primary-fixed-dim: '#dcc1b8'
  on-primary-fixed: '#271813'
  on-primary-fixed-variant: '#56423c'
  secondary-fixed: '#ffddb0'
  secondary-fixed-dim: '#e2c194'
  on-secondary-fixed: '#291800'
  on-secondary-fixed-variant: '#594320'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf8f9'
  on-background: '#1b1b1c'
  surface-variant: '#e5e2e3'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The brand personality for this design system is authoritative, meticulous, and enduring. It targets commercial architects, developers, and general contractors who value precision and premium materials. The UI must evoke the same confidence as a perfectly leveled marble floor or a seamless walnut inlay.

The chosen style is **Minimalism with Tactile Accents**. While the layout remains clean and functional to satisfy commercial utility, the design incorporates physical metaphors through material-inspired colors and subtle depth. This "Architectural Modernism" approach ensures that the interface feels as structured and intentional as a blueprint, yet as luxurious as a finished high-end lobby.

## Colors

The palette is derived from high-end construction materials to create an immediate visual link to the craft of flooring.

- **Walnut (Primary):** A deep, rich brown used for primary navigation, headings, and heavy structural elements. It provides the "grounding" for the interface.
- **Brass (Secondary):** Used sparingly for call-to-actions, highlights, and active states. It adds a metallic "spark" that signifies premium quality.
- **Marble White (Surface):** A clean, slightly cool white used for backgrounds and containers. It ensures the UI feels airy and "polished."
- **Onyx (Neutral):** A near-black for high-readability body text and iconography.

Maintain a high ratio of Marble White to Walnut to ensure the "Clean" aesthetic is not overwhelmed by the "Rich" tones.

## Typography

This design system utilizes a traditional serif/sans-serif pairing to balance heritage with modern efficiency. 

**Noto Serif** is used for headlines to convey a sense of established authority and "old-world" craftsmanship. It should be used for all major section headers and hero statements.

**Work Sans** is used for all functional text, including body copy and UI labels. Its neutral, architectural proportions ensure legibility in technical contexts, such as floor specifications or contract details. Use the `label-caps` style for small sub-headers and metadata to mimic the look of architectural notations.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to mirror the precision of commercial flooring installation. A 12-column grid provides the framework for all desktop views, emphasizing vertical alignment and rigid structure.

The spacing rhythm is based on an 8px scale. Wide margins (`xl`) and significant whitespace around imagery are encouraged to maintain the "Polished" aesthetic. Content should be grouped into clear, logical modules that align to the grid, avoiding organic or overlapping placements.

## Elevation & Depth

Visual hierarchy is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. 

1.  **Surfaces:** The base layer is Marble White. Secondary containers or "inlaid" sections use a very light grey or the Tertiary color to create subtle separation.
2.  **Borders:** Use thin (1px) borders in Brass or light Walnut to define card edges. This mimics the transition strips used between different flooring types.
3.  **Shadows:** When necessary for interactivity (e.g., a raised card), use a single, highly diffused ambient shadow: `0px 10px 30px rgba(70, 52, 46, 0.08)`. The shadow color is tinted with Walnut to keep the depth feeling warm and natural.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding suggests a "finished edge" — much like the bullnose on a tile or the sanded edge of a plank. 

Avoid fully circular buttons or pill shapes; the geometry should remain grounded in squares and rectangles to reflect the modular nature of flooring materials. Larger containers like image carousels or cards may use `rounded-lg` (0.5rem) to feel more inviting, but the primary UI elements should remain crisp.

## Components

- **Buttons:** Primary buttons are solid Walnut with White text. Secondary buttons are Marble White with a Brass border and Brass text. Buttons should have a slight "weight" to them, feeling substantial when hovered.
- **Input Fields:** Fields use a Marble White background with a 1px Walnut border that turns Brass on focus. Labels should always use the `label-caps` typography style.
- **Cards:** Cards should feature a 1px border. For premium content, a 4px Walnut "accent strip" can be placed at the top or left edge of the card.
- **Chips/Tags:** Used for flooring material categories (e.g., "Hardwood", "Epoxy"). Use a Brass background with a very low opacity (10%) and Walnut text for a sophisticated, tonal look.
- **Progress Indicators:** Use a thin Brass line. For multi-step commercial quotes, use a "Stepper" component that mimics the linear flow of a construction timeline.
- **Lists:** Use Brass icons or custom bullet points that resemble floor plan symbols to reinforce the industry connection.