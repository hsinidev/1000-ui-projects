---
name: Epicurean Club
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
  on-surface-variant: '#dbc0be'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a38b89'
  outline-variant: '#554241'
  surface-tint: '#ffb3ae'
  primary: '#ffb3ae'
  on-primary: '#5f1415'
  primary-container: '#540b0e'
  on-primary-container: '#da716c'
  inverse-primary: '#9c413e'
  secondary: '#ffb77b'
  on-secondary: '#4d2700'
  secondary-container: '#7a4100'
  on-secondary-container: '#ffb270'
  tertiary: '#ddc0ba'
  on-tertiary: '#3e2c28'
  tertiary-container: '#352420'
  on-tertiary-container: '#a38a84'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ae'
  on-primary-fixed: '#410004'
  on-primary-fixed-variant: '#7d2a29'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ffb77b'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6d3a00'
  tertiary-fixed: '#fadcd5'
  tertiary-fixed-dim: '#ddc0ba'
  on-tertiary-fixed: '#271814'
  on-tertiary-fixed-variant: '#56423d'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
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
  label-lg:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
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
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style

This design system is engineered to evoke the sensory experience of a private wine cellar and an exclusive chef’s table. The brand personality is rooted in discretion, heritage, and the pursuit of artisanal excellence. It caters to a discerning clientele that values rarity over trendiness.

The style is a synthesis of **Tactile Sophistication** and **Modern Minimalism**. We leverage the depth of high-contrast photography—specifically macro shots of textured grape skins, crystalline wine surfaces, and polished wood grains—to anchor the UI. By utilizing dark, atmospheric layers and metallic accents, we create a digital environment that feels physical and permanent. The emotional response should be one of quiet confidence, exclusivity, and immersive luxury.

## Colors

The palette is anchored in a deeply atmospheric **Dark Mode** default. 

*   **Deep Burgundy (#540B0E):** Used as the primary brand signal for meaningful actions and high-level brand moments.
*   **Polished Copper (#B87333):** Used for interactive elements, highlights, and fine details. This should be treated as a precious metal—used sparingly to denote value.
*   **Dark Walnut Wood (#2B1B17):** Served as a structural background color, providing a softer, warmer alternative to pure black.
*   **Ink Black (#0F0F0F):** The foundational base layer for the entire interface.
*   **Parchment (#F5F5DC):** The primary text color, chosen to avoid the harshness of pure white while maintaining high legibility against dark backgrounds.

## Typography

Typography in this design system balances the editorial weight of a traditional serif with the precision of a modern sans-serif.

**Noto Serif** is utilized for headlines and display text to convey heritage and authority. It should be typeset with generous leading and occasional negative letter-spacing for large displays.

**Manrope** provides a functional, balanced counterpoint for body copy and metadata. Its clean, geometric nature ensures that even in a dark, atmospheric environment, information is easily digestible. High-level labels and navigation items should use Manrope in Uppercase with expanded letter-spacing to mimic the look of luxury engravings.

## Layout & Spacing

This design system employs a **Fixed Grid** model to maintain a cinematic, curated feel. The central content container is capped at 1440px to ensure that macro photography and typography maintain their compositional integrity on wide displays.

The spacing rhythm is intentional and generous. We prioritize vertical "breathing room" (stack-lg) to separate distinct sections of the narrative. All layout decisions should be guided by a golden-ratio-inspired hierarchy, ensuring that the eye is never overwhelmed. Use wide margins (64px) to frame the content like a piece of fine art.

## Elevation & Depth

Depth is achieved through **Tonal Layering** rather than traditional drop shadows. Surfaces are stacked from darkest to lightest:

1.  **Level 0 (Base):** Ink Black (#0F0F0F).
2.  **Level 1 (Card/Container):** Dark Walnut (#2B1B17) with a subtle 1px border of Copper at 10% opacity.
3.  **Level 2 (Active/Floating):** Deep Burgundy with a soft, copper-tinted ambient glow to simulate light hitting a glass of wine.

For interactive elements, we utilize a subtle "inner glow" technique to mimic the bevel of a polished surface. Glassmorphism is used exclusively for navigation overlays, using a heavy backdrop blur (20px) to maintain the atmospheric mood while showing hints of the macro-imagery beneath.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding removes the clinical edge of sharp corners while remaining far more sophisticated than fully rounded or pill-shaped designs. It mimics the subtle softening found on hand-cut wood or stone. 

Secondary elements like images or full-screen sections should maintain sharp corners to emphasize the grid-like, architectural nature of the design system.

## Components

**Buttons:**
Primary buttons are styled in Polished Copper with Noto Serif text. They should have a subtle linear gradient to mimic light reflection. Secondary buttons are ghost-style with a Copper border and high letter-spacing.

**Cards:**
Cards must feature a background-image focus. Text should be overlaid on a Dark Walnut scrim at the bottom or housed in a semi-transparent glassmorphic panel. Macro-photography is the primary occupant of any card component.

**Input Fields:**
Fields are defined by a single bottom-border in Copper (1px). Focus states should intensify the border-color and introduce a very faint Burgundy background tint.

**Lists & Itineraries:**
Used for vineyard tours, these should feature Noto Serif numerals and Manrope body text, separated by thin, low-opacity Copper horizontal rules.

**Navigation:**
The top navigation should be minimal and fixed, using a backdrop-blur. The active state is indicated by a small, polished copper dot beneath the label rather than an underline.

**Signature Component: The "Sommelier Badge":**
A specialized chip component used to denote rare vintages or exclusive tours. It uses the Deep Burgundy background with a 1px Polished Copper border and gold-toned Parchment text.