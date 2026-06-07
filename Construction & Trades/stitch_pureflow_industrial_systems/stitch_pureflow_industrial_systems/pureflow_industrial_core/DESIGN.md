---
name: PureFlow Industrial Core
colors:
  surface: '#071424'
  surface-dim: '#071424'
  surface-bright: '#2e3a4b'
  surface-container-lowest: '#030f1e'
  surface-container-low: '#101c2c'
  surface-container: '#142031'
  surface-container-high: '#1f2b3c'
  surface-container-highest: '#2a3547'
  on-surface: '#d7e3fa'
  on-surface-variant: '#c4c5d9'
  inverse-surface: '#d7e3fa'
  inverse-on-surface: '#253142'
  outline: '#8e90a2'
  outline-variant: '#434656'
  surface-tint: '#b8c3ff'
  primary: '#b8c3ff'
  on-primary: '#002388'
  primary-container: '#2e5bff'
  on-primary-container: '#efefff'
  inverse-primary: '#124af0'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#6e6d6d'
  on-tertiary-container: '#f3f0ef'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c3ff'
  on-primary-fixed: '#001356'
  on-primary-fixed-variant: '#0035be'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#071424'
  on-background: '#d7e3fa'
  surface-variant: '#2a3547'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0em
spacing:
  base: 8px
  gutter: 24px
  margin: 40px
  column_count: '12'
  blueprint_grid: 32px
---

## Brand & Style
The brand personality is engineered, precise, and authoritative. It targets engineers, plant managers, and procurement specialists who value reliability over flourish. The UI evokes the feeling of a high-end physical control console—tactile, heavy-duty, and structurally sound.

This design system utilizes a **Technical-Modern** aesthetic. It blends the structural integrity of Brutalism (heavy borders, visible grids) with the precision of Modern Corporate design. Backgrounds are treated as drafting surfaces, featuring subtle blueprint-style grids and schematic line-work that anchor the content. The emotional response is one of total "operational confidence."

## Colors
The palette is dominated by **Matte Black** (#1A1A1A) and deep charcoal tones to create a high-contrast industrial canvas. **Cobalt Blue** serves as the primary action color, representing liquid flow and digital intelligence. **Silver** and light greys are used for structural outlines and technical data points, mimicking brushed aluminum and steel. 

Backgrounds should use a "Deep Matte" finish, while interactive elements leverage the vibrant Cobalt to pull the eye. Status indicators use industrial standard greens and ambers for clear operational feedback.

## Typography
The typography system prioritizes legibility under "field conditions." **Space Grotesk** is used for headings and labels to provide a geometric, technical edge that feels like stamped metal or architectural lettering. **Inter** is the workhorse for body copy and data, chosen for its exceptional clarity and neutral, systematic tone. 

Use "label-caps" for all technical specifications and metadata headers to reinforce the industrial-manual aesthetic. Data readouts should always maintain a consistent vertical rhythm to ensure scanability across complex tables.

## Layout & Spacing
This design system employs a **Fixed Grid** model within a 1440px container, utilizing a 12-column structure. The rhythm is strictly 8px-based (the "Mechanical Pitch"). 

A distinctive visual element is the **Blueprint Overlay**: a secondary 32px grid of faint blue lines (1px width, 5% opacity) that sits behind all content. Elements should align strictly to these grid intersections. Margins are generous at 40px to give the "robust" components room to breathe, preventing the technical data from feeling cluttered.

## Elevation & Depth
Depth is communicated through **Structural Layering** rather than soft shadows. We use a "machined" approach:
- **Level 0 (Base):** Matte Black background with blueprint schematic lines.
- **Level 1 (Panels):** Slightly lighter charcoal (#242424) with 1px Silver borders. No shadow.
- **Level 2 (Active Elements):** Cobalt Blue surfaces or Silver-framed pop-overs.
- **Level 3 (Alerts):** High-contrast borders (2px) in accent colors.

Instead of ambient shadows, use **inner bevels** (1px highlights on top/left edges) to simulate physical depth and "pressed" or "extruded" metal surfaces.

## Shapes
The shape language is strictly **Sharp (0px)**. Roundness is perceived as "soft" and "consumer-grade," which contradicts the industrial narrative. Every card, button, and input field must have 90-degree corners.

To add visual interest without using radii, utilize **chamfered corners** (45-degree angled cuts) on large container headers or primary action buttons. This mimics heavy machinery casing and reinforces the "mechanical" nature of the product.

## Components

### Buttons & Controls
Buttons are rectangular blocks. The **Primary Button** is solid Cobalt Blue with white caps-lock text. On hover, it gains a 2px Silver "inset" border. **Secondary Buttons** are transparent with a 1px Silver border.

### Problem-Solution Grid
A specialized 2-column component. The left side (Problem) features a dark grey background with a schematic "X" pattern overlay. The right side (Solution) features a Cobalt Blue left-accent border and high-contrast typography. Both halves are joined by a central "Connector Line" reminiscent of a technical drawing.

### Inputs & Fields
Input fields are "inset" into the UI. They feature a 1px solid Matte Black border on a #111111 background, creating a recessed look. Labels always sit above the field in "label-caps" style.

### Data Chips
Small, rectangular tags with no rounded corners. They use high-contrast backgrounds (Cobalt for "Active", Dark Grey for "Static") and always include a 1px border.

### Industrial Cards
Cards must have a visible header bar separated from the body by a 1px Silver line. The header should include a "Component ID" in the top-left (e.g., PF-DR-001) to simulate industrial part numbering.