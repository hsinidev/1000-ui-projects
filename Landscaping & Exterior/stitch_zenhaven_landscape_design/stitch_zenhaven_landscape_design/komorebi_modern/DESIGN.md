---
name: Komorebi Modern
colors:
  surface: '#fcf9f4'
  surface-dim: '#dcdad5'
  surface-bright: '#fcf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ee'
  surface-container: '#f0ede9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e5e2dd'
  on-surface: '#1c1c19'
  on-surface-variant: '#45483c'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f3f0eb'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#5f5f58'
  on-secondary: '#ffffff'
  secondary-container: '#e2e0d7'
  on-secondary-container: '#64635c'
  tertiary: '#4b3e24'
  on-tertiary: '#ffffff'
  tertiary-container: '#63553a'
  on-tertiary-container: '#decaa8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#e5e2da'
  secondary-fixed-dim: '#c9c6be'
  on-secondary-fixed: '#1c1c17'
  on-secondary-fixed-variant: '#474741'
  tertiary-fixed: '#f5e0bd'
  tertiary-fixed-dim: '#d8c4a2'
  on-tertiary-fixed: '#241a05'
  on-tertiary-fixed-variant: '#52452b'
  background: '#fcf9f4'
  on-background: '#1c1c19'
  surface-variant: '#e5e2dd'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  gutter: 24px
  margin-edge: 64px
  section-gap: 128px
  asymmetric-offset: 48px
---

## Brand & Style

The design system is rooted in the Japanese concept of *Ma*—the pure space between objects. It evokes a sense of tranquility, intentionality, and organic precision, tailored for a high-end landscape design clientele who values serenity over stimulation.

The aesthetic blends **Minimalism** with **Tactile** elements. It avoids the coldness of clinical minimalism by introducing natural textures, such as paper-grain backgrounds and subtle wood-grain overlays. The visual rhythm is governed by asymmetrical balance, where large areas of "Sand" whitespace are anchored by "Moss Green" focal points, mimicking the composition of a Zen garden. Transitions are slow and deliberate, moving with a "fade-and-slide" motion that feels like a calm breeze rather than a digital snap.

## Colors

The palette is derived from the natural world, emphasizing earthy, grounded tones.

- **Primary (Moss Green):** Used for primary actions, navigation highlights, and representing growth. It should be used sparingly to maintain its impact.
- **Secondary (Sand):** The foundation of the design system. This warm off-white serves as the primary background color, reducing eye strain and providing a soft, paper-like canvas.
- **Tertiary (Pale Wood):** Used for structural elements, dividers, and subtle containers. It provides a tactile warmth that complements the green.
- **Neutral (Ink):** A soft, warm black used for typography to ensure high legibility without the harshness of pure black.

Avoid pure whites or vibrant gradients. All colors should feel matte and organic.

## Typography

This design system employs a sophisticated typographic hierarchy that balances the literary elegance of a serif with the functional clarity of a sans-serif.

**Noto Serif** is reserved for headlines. It should be set with tight leading and slightly negative letter-spacing for large displays to create a sense of refined authority.

**Manrope** is used for all functional text. Its geometric yet friendly character ensures readability in long-form descriptions of landscape projects. For navigational elements and small labels, use "label-caps" to create a distinct architectural feel, reminiscent of traditional Japanese floor plans.

## Layout & Spacing

The layout is built on a **12-column fixed grid**, but it is executed with intentional asymmetry. Content should rarely be perfectly centered. Instead, utilize "Ma" by leaving entire columns empty to draw the eye toward the imagery.

- **Asymmetrical Balance:** If a text block occupies 5 columns on the left, the corresponding image might occupy 6 columns on the right, shifted down by the `asymmetric-offset`.
- **Rhythm:** Use large `section-gap` values to separate different phases of the narrative, allowing the user to "breathe" between sections.
- **Verticality:** Use thin, vertical lines (1px width, Pale Wood color) to occasionally divide sections, mimicking the structure of Shōji screens.

## Elevation & Depth

This design system rejects traditional drop shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**. Depth is communicated through the stacking of colors rather than artificial light sources.

- **The Ground Plane:** The Sand background is the lowest level.
- **Elevated Surfaces:** Elements like cards use a subtle "Pale Wood" border (0.5px or 1px) or a slightly darker "Sand" tint to indicate interactivity.
- **Depth through Texture:** Use CSS masks or subtle noise overlays on containers to create a tactile, paper-like feel. 
- **Focus:** When a modal or menu appears, instead of a heavy black overlay, use a "Sand" tinted backdrop-blur to maintain the airy, serene atmosphere.

## Shapes

The shape language is strictly **Sharp (0px)**. 

To honor the precision of traditional Japanese carpentry and architecture, all buttons, image containers, and input fields must have crisp, 90-degree angles. This severity is softened not by rounding corners, but by the organic nature of the photography and the warmth of the color palette. Any "softness" should come from the content (plants, flowing water, stones in photos), while the UI acts as a structured frame.

## Components

- **Buttons:** Rectangular with a 1px Moss Green border. The hover state fills the button with Moss Green and changes text to Sand. The transition should be a slow 400ms fade.
- **Cards:** No shadows. Use a 1px Pale Wood border. Images within cards should have a slight zoom-in effect on hover to simulate moving closer to nature.
- **Inputs:** A single bottom border in Pale Wood. The label should use the "label-caps" style, positioned above the line. On focus, the bottom border darkens to Moss Green.
- **Chips/Tags:** Small, rectangular boxes with a Moss Green background and Sand text. Use these for categorizing garden types (e.g., "Zen," "Tsukiyama").
- **Navigation:** A minimal top-bar with wide letter-spacing. Use a simple dot indicator (Moss Green) below the active page link.
- **Transitions:** Page transitions should utilize a "curtain" effect where a Sand-colored panel wipes across the screen, creating a moment of total minimalism before the next content appears.