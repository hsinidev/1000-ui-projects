---
name: Digital Gallery
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
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdf'
  on-secondary-container: '#626263'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1b1b1b'
  on-tertiary-container: '#848484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Epilogue
    fontSize: 80px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  h2:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h3:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-sm:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.02em
  mono-label:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  grid-line-weight: 1px
  margin-page: 64px
  gutter: 0px
  cell-padding: 24px
---

## Brand & Style

The design system is an exercise in restraint, designed to serve as a neutral, high-fidelity stage for architectural expression. It targets discerning professionals and clients in the architecture and design industries, evoking a sense of structural integrity, precision, and spatial clarity.

The visual language is rooted in **Minimalism** and **Modernism**, drawing inspiration from technical drawings and physical galleries. It utilizes a visible grid system as a decorative yet functional element, mirroring the structural skeletons of buildings. The emotional response is one of calm, intellectual rigor, and premium quality, ensuring that the interface never competes with the architectural photography it hosts.

## Colors

The palette is strictly monochrome, emphasizing value over hue to reflect the "Blueprint-to-Build" narrative. 

- **Primary & Secondary:** Pure Black (#000000) is reserved for structural lines, borders, and primary typography. Deep Greys are used for secondary information and metadata.
- **Backgrounds:** Pure White (#FFFFFF) provides maximum "breathing room," while the subtle Grey (#F5F5F5) defines the "void" spaces between structural grid cells.
- **Accents:** Light Grey (#E0E0E0) is used exclusively for the visible grid lines and inactive UI states, mimicking the faint markings of a drafting table.

## Typography

The typography strategy pairs a high-contrast, geometric sans-serif for headings with a technical, engineering-inspired sans-serif for body and labels.

- **Headings:** Use **Epilogue**. Its tight kerning and bold weights create a striking, editorial feel that mimics architectural signage.
- **Body & Labels:** Use **Space Grotesk**. Its geometric construction and wide apertures provide high legibility and a subtle "technical" aesthetic reminiscent of blueprint annotations.
- **Usage:** All labels should be set in uppercase with increased letter spacing to emphasize the precision of the design system.

## Layout & Spacing

The layout is governed by a **Strict Fixed Grid**. Unlike traditional layouts where the grid is invisible, this design system uses a 1px solid line (#E0E0E0) to define every column and row.

- **The Grid:** A 12-column grid system where elements are "contained" within visible cells. Gutters are 0px, as the 1px grid line serves as the separator.
- **Horizontal Scrolling:** Portfolio galleries utilize full-height horizontal containers that snap to the grid lines, allowing users to "walk" through a project linearly.
- **Information Density:** Significant padding (24px to 64px) is maintained within grid cells to ensure the interface feels expansive and gallery-like.

## Elevation & Depth

This design system rejects shadows and depth effects in favor of **Structural Flattening**. Hierarchy is achieved through the thickness of lines and the arrangement of containers rather than elevation.

- **Tonal Layers:** The background is always the lowest layer. "Floating" elements do not exist; every UI component must be anchored to a grid intersection or contained within a grid cell.
- **Interactions:** Depth is simulated via "Blueprint" overlays—semi-transparent white fills (90% opacity) that appear over imagery to reveal technical data or descriptions.
- **Borders:** Only 1px solid lines are used. No blurs, no gradients, and no soft edges.

## Shapes

The shape language is strictly **Sharp (0px)**. Every element—from buttons and input fields to large-scale image containers—must maintain 90-degree angles. This reflects the rigidity of architectural forms and the precision of drafting tools. Circular elements are prohibited unless they represent specific technical icons (e.g., a compass or north-point indicator).

## Components

- **Buttons:** Rectangular with a 1px black border. On hover, the button fills with solid black and the text flips to white. There are no rounded corners.
- **Blueprint-to-Build Toggle:** A specialized switch using a "drafting" aesthetic. The "Blueprint" state displays a faint grey wireframe icon, while the "Build" state displays a solid black icon. The transition should be a sharp, instant flick with no easing.
- **Horizontal Containers:** Used for project galleries. They must span the full viewport height minus the header/footer grid cells, scrolling on the X-axis with a visible scroll progress bar at the bottom.
- **Inputs & Forms:** Simple lines that sit flush against the grid. Labels are placed above the line in the `mono-label` style.
- **Project Cards:** Image-heavy containers where the project title and year are positioned in a dedicated grid cell directly below or beside the image, separated by a 1px line.
- **Status Indicators:** Small, solid black squares (no circles) used to denote active projects or selected states.