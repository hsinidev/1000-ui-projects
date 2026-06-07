---
name: Urban Industrial
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e0c0b5'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a78a81'
  outline-variant: '#58423a'
  surface-tint: '#ffb59c'
  primary: '#ffb59c'
  on-primary: '#5c1a00'
  primary-container: '#b7410e'
  on-primary-container: '#ffe2d9'
  inverse-primary: '#a93702'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#494949'
  on-secondary-container: '#b9b8b8'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#676868'
  on-tertiary-container: '#e8e8e8'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59c'
  on-primary-fixed: '#380c00'
  on-primary-fixed-variant: '#822800'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Epilogue
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  gutter: 24px
  margin: 48px
  divider-weight: 2px
  container-max: 1440px
---

## Brand & Style

This design system embodies a **Rugged-Luxe** aesthetic, balancing the raw, unrefined character of industrial spaces with the sophisticated polish of modern high-end furniture. The brand personality is architectural, masculine, and deliberate. It targets an audience that appreciates the "lofts of Soho" or "converted warehouses of Berlin"—users who value structural integrity and material authenticity.

The UI style is a hybrid of **Brutalism** and **Minimalism**. It utilizes heavy structural lines and a monochromatic foundation to mimic steel beams and concrete slabs, while maintaining a premium feel through expansive whitespace and high-contrast photography. The emotional response should be one of "stable luxury": a sense that the interface is as permanent and well-built as a cast-iron pillar.

## Colors

The palette is anchored in the materials of the urban landscape. 

- **Matte Black (#1A1A1A):** Serves as the primary canvas, providing a deep, architectural background.
- **Rust (#B7410E):** Used sparingly as a high-impact accent for calls to action, price points, and active states.
- **Exposed Concrete Grey (#4A4A4A, #D3D3D3):** Used for structural elements, secondary text, and borders to create depth without relying on traditional shadows.

The design system defaults to a **dark mode** experience to emphasize the "industrial night" atmosphere, using high-contrast white text against the dark neutrals for maximum legibility.

## Typography

This design system uses a strategic pairing of **Epilogue** and **Work Sans**. 

**Epilogue** is utilized for headlines to simulate the weight and presence of heavy slab-serif and geometric wood-block type. It is always set with tight tracking and heavy weights to feel "stamped" onto the page.

**Work Sans** provides a functional, utilitarian contrast for body copy and UI labels. It is highly legible and grounded, evoking the feel of technical blueprints or shipping manifests. All labels and secondary metadata should be set in Uppercase with wide letter spacing to reinforce the industrial labeling aesthetic.

## Layout & Spacing

The layout follows a **fixed grid** philosophy with a 12-column structure. It prioritizes "spacious grit"—using generous margins (48px+) to allow high-contrast photography to breathe, while using **bold, 2px dividers** in `#4A4A4A` to compartmentalize information.

The spacing rhythm is strictly based on an 8px scale. Layouts should feel vertical and modular, like stacked shipping containers. Avoid fluid, organic transitions; instead, use hard lines and clear geometric boundaries to separate content sections.

## Elevation & Depth

This design system rejects soft shadows and traditional depth. Instead, it uses **Tonal Layers** and **Bold Borders**. 

- **Surface Levels:** The base background is `#1A1A1A`. Raised elements (like cards) use `#2A2A2A`.
- **Structural Lines:** Depth is communicated through 1px or 2px solid borders in `#4A4A4A`. 
- **Active States:** Elements do not "glow"; they shift in color (e.g., from Grey to Rust) or gain a thick, solid stroke.
- **Textures:** Distressed overlays (subtle grain or concrete grit) are applied to large background surfaces to provide tactile "tooth" to the digital interface.

## Shapes

The shape language is strictly **Sharp (0px)**. 

To maintain the industrial integrity of the system, all buttons, input fields, images, and containers must have 90-degree corners. This evokes the hardness of steel beams and cut stone. Circular elements are permitted only for functional icons or specific status indicators, but all structural UI components must remain rectangular.

## Components

- **Buttons:** Primary buttons are solid `#B7410E` (Rust) with white, bold caps-locked text. Secondary buttons are outlined in 2px `#D3D3D3` with no fill.
- **Cards:** Cards use a `#2A2A2A` background with a 1px border. Product cards should feature high-contrast photography that bleeds to the edges of the top and sides, with a heavy divider separating the image from the text content.
- **Input Fields:** Bottom-border only, 2px thick, in `#4A4A4A`. Upon focus, the border transitions to `#B7410E`.
- **Chips/Tags:** Rectangular boxes with a solid `#4A4A4A` fill and white Work Sans labels.
- **Dividers:** Prominent 2px horizontal or vertical rules in `#4A4A4A` used to define the grid and separate content blocks.
- **Photography:** Imagery should be desaturated or high-contrast, highlighting textures like rusted metal, porous concrete, and grainy wood.