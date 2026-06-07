---
name: NEON BRUTAL
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#e3bfb3'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#aa897f'
  outline-variant: '#5b4138'
  surface-tint: '#ffb59c'
  primary: '#ffb59c'
  on-primary: '#5c1900'
  primary-container: '#ff5f1f'
  on-primary-container: '#561700'
  inverse-primary: '#ab3600'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#939494'
  on-tertiary-container: '#2b2d2d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59c'
  on-primary-fixed: '#390c00'
  on-primary-fixed-variant: '#832700'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-2xl:
    fontFamily: Epilogue
    fontSize: 120px
    fontWeight: '900'
    lineHeight: 100%
    letterSpacing: -0.05em
  headline-xl:
    fontFamily: Epilogue
    fontSize: 72px
    fontWeight: '900'
    lineHeight: 110%
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 110%
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 150%
    letterSpacing: 0em
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 150%
    letterSpacing: 0em
  mono-label:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 120%
    letterSpacing: 0.05em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 100%
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 0px
  margin: 32px
  container-padding: 24px
  border-width-thin: 1px
  border-width-heavy: 4px
---

## Brand & Style
This design system captures the raw, high-velocity energy of underground sneaker culture. It is rooted in **Brutalism** and **High-Contrast** aesthetics, prioritizing impact over subtlety. The interface is designed to feel like a digital wheat-paste poster—unapologetic, industrial, and urgent. 

The target audience is the "hypebeast" and high-end collector who values technical precision and bold self-expression. The UI should evoke a sense of "The Drop"—the adrenaline-fueled moment of a limited release. Visual elements are oversized, borders are heavy, and the overall composition feels engineered rather than decorated.

## Colors
The palette is built on maximum ocular tension. **Neon Orange** serves as the primary action color, used for CTA buttons, urgent notifications, and critical data points. The background is a solid **Deep Black**, providing a void-like canvas that makes typography and product photography pop. 

**Stark White** is reserved for primary information and large-scale display type, while **Muted Gray** is used for structural elements, secondary technical data, and "Market Value" chart backgrounds to create a layered, industrial depth without breaking the high-contrast ethos.

## Typography
The typography strategy utilizes **Epilogue** for its aggressive, geometric weight in headings. All headlines must be uppercase with negative letter spacing to create a dense, "blocky" feel. 

For body copy and technical metadata, **Space Grotesk** provides a utilitarian, futuristic aesthetic that mirrors technical spec sheets. Large-scale typography should often be used as a background element or clipped by the edges of the viewport to reinforce the raw, unpolished brutalist layout.

## Layout & Spacing
This design system employs a **Fixed Grid** model with a hard-edge execution. Gutters are eliminated (0px) in many sections to allow components to butt against each other, separated only by heavy 4px borders. 

The layout should feel "boxed in." Use a 12-column grid for desktop, but allow elements like product cards and technical charts to span the full width of their containers. Padding within elements is generous to ensure readability amidst the aggressive visual style, but external margins between major sections should be tight to maintain a high-energy, crowded feel.

## Elevation & Depth
Depth is achieved through **Bold Borders** and high-contrast stacking rather than shadows. No ambient shadows or blurs are permitted. 

To indicate elevation or "active" states, use "Hard Shadows"—solid offsets of the primary color or white at 4px or 8px distances with 100% opacity. Tonal layers are strictly black (#000000) or muted gray (#333333). When an element is hovered, it should physically shift (translate) rather than glow, mimicking a tactile, mechanical movement.

## Shapes
The shape language is strictly **Sharp (0px)**. There are no rounded corners in this design system. Every button, card, input field, and image container must have 90-degree angles. This reinforces the industrial, brutalist aesthetic and ensures the heavy borders align perfectly to create a seamless, monolithic grid.

## Components
- **Buttons:** Oversized, rectangular, with 4px black or white borders. The "Primary Action" button is Neon Orange with black text. Use "Hard Shadow" offsets on hover.
- **Cards:** Product cards use a 1px white border. The product name should be in a heavy display font, often overlapping the product image for a collaged, "street" look.
- **Drop Timers:** Styled like industrial digital clocks. Use large-scale monospace numbers and a Neon Orange color for the countdown.
- **Market Value Charts:** Line graphs should be sharp (no curves) and use the primary Neon Orange for the data line against a Muted Gray grid background.
- **Input Fields:** Thick 2px white borders on black backgrounds. Labels should be positioned "on the line" or inside the top-left corner in a small technical-data font.
- **Chips/Tags:** Small rectangular boxes with 1px borders, using uppercase technical-data typography. Labels like "SOLD OUT" should be Neon Orange with black text.
- **Scrollbars:** Custom-styled as thick, Neon Orange bars with no track styling, making them a visible part of the industrial UI.