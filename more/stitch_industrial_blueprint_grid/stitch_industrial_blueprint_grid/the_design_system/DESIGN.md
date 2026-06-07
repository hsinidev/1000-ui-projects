---
name: The Design System
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
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#b1c5ff'
  on-tertiary: '#002c70'
  tertiary-container: '#000822'
  on-tertiary-container: '#4775da'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#dae2ff'
  tertiary-fixed-dim: '#b1c5ff'
  on-tertiary-fixed: '#001946'
  on-tertiary-fixed-variant: '#00419e'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 96px
    fontWeight: '700'
    lineHeight: 100%
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 110%
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 120%
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 160%
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 160%
  technical-data:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 140%
    letterSpacing: 0.05em
spacing:
  grid-unit: 8px
  gutter: 1px
  margin-edge: 64px
  column-count: '12'
---

## Brand & Style
The design system is engineered to evoke the precision of a master architect’s blueprint and the monumental scale of high-end commercial real estate. It targets high-stakes developers and architectural firms who value technical rigor and structural clarity. 

The aesthetic is a synthesis of **Minimalism** and **Modern Brutalism**, where the underlying structure is not hidden but celebrated. The UI functions as a digital scaffolding, utilizing "Grid-Visible" layouts to communicate transparency and engineering excellence. Every element is placed with mathematical intent, creating a user experience that feels authoritative, expansive, and high-performance.

## Colors
The palette is rooted in a high-contrast dark mode to simulate a professional CAD environment. 

- **Deep Black (#0A0A0A):** The primary canvas color, providing a sense of infinite depth and prestige.
- **Stark White (#FFFFFF):** Used for primary typography and structural lines, ensuring maximum legibility and a sharp, clinical feel.
- **Blueprint Blue (#0047AB):** Reserved for technical overlays, interactive states, and data visualization. It mimics the light emitted from high-end architectural software.
- **Neutral (#1A1A1A):** Used for subtle surface differentiation and container backgrounds.

## Typography
The typography strategy contrasts heavy, industrial headlines with clinical, monospaced data.

- **Headlines:** Space Grotesk is utilized for its geometric, engineered appearance. Bold weights and tight letter-spacing are required for high-level headings to create a sense of architectural weight.
- **Body:** Inter provides a systematic, neutral counterpoint for long-form reading, ensuring clarity against complex technical backgrounds.
- **Data & Labels:** All technical specifications, coordinates, and metadata must use a monospaced font stack. This reinforces the "engineered" narrative and ensures that numerical values align perfectly in tables and overlays.

## Layout & Spacing
The design system employs a **Rigid Visible Grid**. The layout is not merely suggested; it is defined by 1px stark white or subtle blue lines that remain visible to the user, creating a "blueprint" effect.

- **The 12-Column Grid:** All content must snap to a 12-column structure. 
- **1px Technical Lines:** Use 1px borders to define the perimeter of the content area, individual columns, and section breaks.
- **Grand Scale:** Generous outer margins (64px+) are used to convey a sense of luxury and space, preventing the technical details from feeling cluttered.
- **Rhythm:** All vertical spacing must be a multiple of the 8px grid unit to maintain mathematical consistency.

## Elevation & Depth
Depth in the design system is achieved through **structural layering** rather than shadows. 

- **Flat Hierarchy:** Avoid ambient shadows or blurs. Elevation is conveyed by 1px borders and color shifts.
- **Tonal Layers:** Active or "elevated" panels use #1A1A1A against the #0A0A0A background.
- **Blueprint Overlays:** When an element requires focus (like a modal or data detail), it should appear as a "Blueprint Blue" framed box with a semi-transparent fill, suggesting a digital projection over the base architecture.
- **Interaction Borders:** Hovering over a grid cell should trigger a 1px Blueprint Blue border highlight and the appearance of monospaced coordinates at the corners.

## Shapes
The shape language is strictly **Sharp (0px)**. To reflect the hard materials of commercial architecture—steel, glass, and concrete—there are no rounded corners in the design system.

Every button, input field, card, and modal must feature 90-degree angles. This reinforces the precision and structural integrity of the brand. Visual interest is generated through line weight and the intersection of horizontal and vertical strokes rather than organic curves.

## Components
Consistent component behavior is vital for maintaining the technical aesthetic.

- **Buttons:** Rectangular with 1px borders. Primary buttons use a solid Blueprint Blue fill with white monospaced text. Secondary buttons are ghost-style with a white border that turns blue on hover.
- **Input Fields:** Bottom-border only or full 1px box. Labels are always monospaced and positioned above the field or "docked" in the top-left corner of the border.
- **Technical Chips:** Used for property tags (e.g., "COMMERCIAL," "LEED GOLD"). These should look like small CAD labels with a 1px border and monospaced uppercase text.
- **Cards:** Defined by their grid lines. A card is simply a cell in the layout grid. On hover, the internal area may shift slightly in color, and technical metadata (dimensions, ID numbers) should fade in.
- **Data Overlays:** Tooltips and popovers should include crosshair icons or "target" graphics at their anchor points to emphasize the precision of the data being displayed.
- **Progress Indicators:** Use thin, horizontal bars that fill with a blueprint-style hatch pattern or solid Blueprint Blue.