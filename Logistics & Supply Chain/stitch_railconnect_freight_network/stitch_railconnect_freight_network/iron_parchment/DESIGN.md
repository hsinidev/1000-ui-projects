---
name: Iron & Parchment
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#5a403e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#8e706d'
  outline-variant: '#e2beba'
  surface-tint: '#b52424'
  primary: '#8f000d'
  on-primary: '#ffffff'
  primary-container: '#b22222'
  on-primary-container: '#ffc8c2'
  inverse-primary: '#ffb4ac'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e2'
  on-secondary-container: '#646464'
  tertiary: '#454634'
  on-tertiary: '#ffffff'
  tertiary-container: '#5c5e4b'
  on-tertiary-container: '#d7d7bf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb4ac'
  on-primary-fixed: '#410003'
  on-primary-fixed-variant: '#92030f'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: newsreader
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: newsreader
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: newsreader
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: workSans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: workSans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  utility-label:
    fontFamily: workSans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: workSans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
spacing:
  unit: 8px
  gutter: 1px
  margin-sm: 16px
  margin-md: 32px
  container-max: 1440px
  border-width-thick: 3px
  border-width-thin: 1px
---

## Brand & Style

This design system is built for the high-stakes world of intermodal logistics, evoking the mechanical reliability of heavy rail. The brand personality is authoritative, weathered, and unyielding. It targets logistics coordinators and yard operators who value precision over polish. 

The aesthetic leverages a **Industrial Brutalism** mixed with **Tactile** elements. It mimics physical infrastructure: structural steel, stamped metal plates, and printed manifests. The UI should feel like a piece of heavy equipment—functional, durable, and impossible to break. Every interaction should feel deliberate, emphasizing high-contrast readability and a "physical" presence through heavy strokes and rigid alignments.

## Colors

The palette is anchored in the utilitarian colors of the railway. 

- **Parchment (#F5F5DC)**: Used as the primary background surface, reminiscent of vintage waybills and technical paper.
- **Iron Grey (#4A4A4A)**: The structural color, used for heavy borders, icons, and primary text to provide a "machined" feel.
- **Rusty Red (#B22222)**: Reserved for critical actions, alerts, and branding accents. It signifies heat, urgency, and industrial power.
- **Status Tints**: Use high-saturation variants of forest green for "On Track" and amber for "Delayed," always framed by Iron Grey borders to maintain the rugged aesthetic.

## Typography

The typographic hierarchy creates a tension between traditional editorial authority and modern industrial efficiency.

- **Headlines**: Using **Newsreader** at its heaviest weights to simulate the slab-serif impact of 19th-century railway branding. Headlines should feel "stamped" onto the page.
- **Utility & Body**: **Work Sans** provides a clean, neutral counterpoint. Its high legibility ensures that complex technical data and schedules remain readable in low-light industrial environments.
- **Labels**: Small-caps or all-caps Work Sans should be used for table headers and input labels to mimic technical diagrams.

## Layout & Spacing

The 'Railway-Grid' layout is a **Fixed-Width Grid** inspired by ledger paper and train schematics. 

- **The Grid**: Layouts are strictly partitioned using visible **1px Iron Grey borders** rather than whitespace. This creates a "cell-based" UI where information is trapped in clear, durable compartments.
- **Rhythm**: All spacing follows an 8px base unit. 
- **The Ledger Effect**: Use horizontal banding in tables and lists, alternating between Parchment and a slightly darker "Dust" tint (#EBEBD0) to guide the eye across complex data rows.
- **Margins**: Heavy external margins (32px+) ensure the "document" feel is maintained within the screen.

## Elevation & Depth

In this design system, depth is communicated through **structural stacking** rather than shadows. 

- **Flat Layering**: We avoid ambient shadows entirely. Hierarchy is achieved through "inset" and "outset" logic.
- **The Stencil Look**: Primary buttons and active cards use a thick (3px) Iron Grey border to appear physically bolted to the background.
- **Sunken Elements**: Input fields and data cells use a 1px border with a slightly darker interior fill to appear recessed into the Parchment surface.
- **Overlay Panels**: When a modal or pop-over is required, it should have a thick 4px solid border with no blur, appearing like a physical plate placed over the interface.

## Shapes

The shape language is strictly **Sharp (0)**. 

Railways are built of steel and stone; there are no soft corners in the yard. Every button, input, card, and container must have a 0px corner radius. This reinforces the rugged, industrial nature of the system. Visual interest is generated through the intersection of vertical and horizontal lines (the grid) rather than organic curves.

## Components

- **Buttons**: Square corners, heavy 2px borders. Primary buttons use Rusty Red fill with Parchment text. Hover states should simply invert the colors (Parchment fill, Rusty Red text) to mimic a mechanical switch.
- **Data Tables**: The core of the system. Use visible borders for every cell. Headers should be Iron Grey with Parchment text in all-caps Work Sans.
- **Status Chips**: Rectangular blocks with solid fills. No transparency. Text must be high-contrast (e.g., White text on Rusty Red).
- **Inputs**: Rectangular boxes with a "recessed" feel. Labels should be placed directly on the border line or justified to the top-left in a smaller utility font.
- **Cards**: Use a "Manifest" style—a header section separated by a thick horizontal rule, with data points organized in a strict 2-column grid within the card body.
- **Progress Indicators**: Linear, blocky bars that fill in discrete segments, resembling train cars being added to a line.