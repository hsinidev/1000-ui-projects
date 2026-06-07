---
name: Technical-Luxe
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#b8c8da'
  on-secondary: '#223240'
  secondary-container: '#394857'
  on-secondary-container: '#a7b7c8'
  tertiary: '#d0cdcd'
  on-tertiary: '#303030'
  tertiary-container: '#b4b2b2'
  on-tertiary-container: '#454544'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  spec-value:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max: 1440px
  fine-line: 1px
---

## Brand & Style

This design system is built for the horological connoisseur, blending the heritage of high-end watchmaking with the cold precision of modern engineering. The personality is authoritative, archival, and immersive—evoking the feeling of stepping into a private atelier where every detail is scrutinized under a loupe.

The visual style is a fusion of **Minimalism** and **Architectural Tactility**. It relies on structured layouts that mirror technical blueprints, using high-contrast typography to signal luxury and monospaced accents to signal mechanical expertise. Every interaction should feel intentional, mimicking the weighted click of a crown or the smooth rotation of a ceramic bezel.

## Colors

The palette is anchored in **Deep Charcoal**, creating a void-like depth that allows the mechanical components to take center stage. **Champagne Gold** is used sparingly as a high-value accent for critical interactive elements and branding, representing the precious metals found in movement calibres. 

**Slate** provides the technical framework, used for schematic lines, secondary text, and inactive states. To create the "Architectural" feel, use subtle metallic gradients (linear, 45 degrees) that transition from a slightly lifted charcoal to the base neutral, simulating machined steel or titanium surfaces.

## Typography

The typographic scale uses a dramatic contrast between serif and monospaced fonts to reinforce the "Technical-Luxe" narrative. 

- **Playfair Display** handles all major headings. It should be treated with generous whitespace to emphasize its editorial elegance.
- **Inter** is the workhorse for long-form descriptions, providing clean legibility against dark backgrounds.
- **JetBrains Mono** is reserved for technical specifications (e.g., jewel counts, vibrations per hour, power reserve). This font should often be paired with fine-line dividers to evoke the look of a calibration sheet.

## Layout & Spacing

This design system utilizes a **Fixed 12-Column Grid** for desktop views to maintain a sense of architectural permanence. Margins are intentionally wide (64px+) to create a "gallery" feel, pushing the content into a focused central stage.

Spacing follows a strict 8px rhythmic scale. However, structural elements are often separated by 1px "schematic lines" in Slate or low-opacity Gold. These lines should extend to the edges of the container, creating a blueprint-like framework that organizes the technical data.

## Elevation & Depth

Depth is achieved through a combination of **Tonal Layers** and **Deep Shadows**, rather than simple color shifts.

1.  **The Base:** Deep Charcoal (#121212).
2.  **The Floor:** Inset panels use a slightly darker shade with inner shadows to create the appearance of a cavity within a watch case.
3.  **The Component:** Floating cards use a subtle linear gradient (Charcoal to slightly lighter Slate) and a 1px border. 
4.  **The Shadow:** Shadows are sharp but highly diffused (e.g., `0 20px 40px rgba(0,0,0,0.8)`), suggesting that elements are hovering exactly 2-3mm above the surface, like hands over a dial.

Use backdrop blurs (20px+) on overlays to maintain the "Glassmorphism" of a sapphire crystal exhibition back.

## Shapes

The shape language is precise and controlled. A "Soft" roundedness (0.25rem) is applied to primary components to mimic the subtle chamfering on a watch lug or bridge. 

- **Hard Edges:** Used for structural dividers and "technical" containers to maintain a sense of rigid engineering.
- **Soft Radii:** Used for buttons, cards, and input fields to ensure they feel tactile and approachable.
- **Perfect Circles:** Reserved exclusively for circular movement components (e.g., balance wheels, gears) or icon backdrops to create visual focal points.

## Components

### Buttons
Primary buttons should feature a metallic Champagne Gold gradient with center-aligned technical data labels. On hover, the gradient should "shimmer"—achieved by shifting the gradient position—simulating light hitting polished metal.

### Chips & Tags
Use JetBrains Mono at 10px. Surround with a 1px Slate border. Chips should look like serialized parts tags found in a factory, perhaps including a small "part number" prefix.

### Lists & Specs
Information should be presented in a key-value format. Use a dotted or solid fine-line leader between the label (Inter) and the value (JetBrains Mono) to guide the eye, similar to a technical manual.

### Input Fields
Inputs are "inset" into the UI. Use a dark background with a 1px bottom-border that glows Champagne Gold when focused. Labels should always be visible in the `data-label` style.

### Cards
Cards act as "Exhibition Cases." They should have a subtle 1px border and a very slight metallic sheen. Content inside cards should be layered, with high-resolution imagery of watch movements appearing to sit beneath a "crystal" layer (backdrop-blur).

### Additional Components
- **The Calibre Gauge:** A custom progress bar or radial dial that mimics a power reserve indicator.
- **The Schematic Divider:** A horizontal line that ends in a small diamond or technical "crosshair" symbol.