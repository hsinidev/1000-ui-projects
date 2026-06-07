---
name: Industrial Integrity
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
  on-surface-variant: '#4f4540'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#81756f'
  outline-variant: '#d2c4bd'
  surface-tint: '#6f5a4f'
  primary: '#35251c'
  on-primary: '#ffffff'
  primary-container: '#4d3b31'
  on-primary-container: '#bea598'
  inverse-primary: '#dcc1b3'
  secondary: '#705d00'
  on-secondary: '#ffffff'
  secondary-container: '#fcd408'
  on-secondary-container: '#6f5c00'
  tertiary: '#1c2a3d'
  on-tertiary: '#ffffff'
  tertiary-container: '#324054'
  on-tertiary-container: '#9dacc3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f9ddcf'
  primary-fixed-dim: '#dcc1b3'
  on-primary-fixed: '#271810'
  on-primary-fixed-variant: '#554339'
  secondary-fixed: '#ffe170'
  secondary-fixed-dim: '#e9c400'
  on-secondary-fixed: '#221b00'
  on-secondary-fixed-variant: '#544600'
  tertiary-fixed: '#d5e3fd'
  tertiary-fixed-dim: '#b9c7e0'
  on-tertiary-fixed: '#0d1c2f'
  on-tertiary-fixed-variant: '#3a485c'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  technical-sm:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  touch-target: 48px
---

## Brand & Style

This design system is built upon the principles of **Industrial Brutalism**, optimized for the high-stakes world of logistics and land brokerage. The brand personality is unshakeable, precise, and authoritative. It evokes the physical scale of massive warehouses and the raw utility of construction sites.

The visual narrative shifts away from ephemeral digital trends toward a "built to last" aesthetic. It utilizes heavy strokes, structural grid alignment, and subtle environmental textures—specifically concrete grain and brushed steel—to ground the digital experience in the physical reality of the assets being traded. The target audience expects data density and technical accuracy without the friction of decorative fluff. Every element feels heavy, intentional, and permanent.

## Colors

The palette is derived from industrial landscapes. 
- **Earthy Brown (#4D3B31)**: The primary anchor. Used for heavy headers, structural backgrounds, and primary branding to represent the earth and stability.
- **Safety Yellow (#FAD201)**: Reserved strictly for high-contrast actions (CTAs), warnings, and critical highlights. It mimics site-safety markings to draw immediate attention.
- **Slate Gray (#334155)**: Used for secondary technical information, borders, and UI scaffolding. 
- **Concrete Neutral (#F2F2F2)**: The base canvas, providing a neutral, low-strain background that allows technical data to stand out.

Backgrounds should occasionally utilize a subtle "grain" texture overlay (2-3% opacity) to mimic the tactile feel of physical site plans.

## Typography

This design system utilizes a high-contrast typographic pairing to distinguish between "Authority" and "Data."

**Headings** use **Newsreader**. While traditionally a literary face, when used at heavy weights it functions as a sophisticated slab-serif, providing the visual weight and stability of a cornerstone. It is used for property names, section headers, and value propositions.

**Technical Data & Body** use **Work Sans**. This font was chosen for its architectural precision and exceptional readability in data-heavy environments. The generous x-height ensures that complex measurements (square footage, acreage, zoning codes) remain legible on mobile devices. Technical labels should use the `label-caps` style to mimic industrial signage.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to mirror the rigid planning of industrial zones. Content is housed within defined containers that use a strict 4px baseline rhythm.

- **Mobile-First Data**: For data sheets, utilize a vertical stack with "Touch Zones" of no less than 48px in height. 
- **Structural Gutters**: A 16px gutter is standard, providing clear separation between data points.
- **Alignment**: Everything must align to the grid. Avoid "floating" elements; if an element exists, it should be anchored by a border or a structural line.

## Elevation & Depth

In keeping with the "Grounded" aesthetic, this design system eschews soft, ambient shadows in favor of **Bold Borders** and **Tonal Layering**.

- **Depth through Borders**: Layers are separated by 1px or 2px solid strokes in Slate Gray or Earthy Brown. This creates a blueprint-like clarity.
- **Inset Depth**: Use subtle inner shadows on input fields to make them feel "stamped" into the UI, like an engraved serial plate.
- **Surface Tiering**: Backgrounds use a light concrete gray, while active "cards" or "sheets" use a pure white surface to pop against the textured background.
- **No Blurs**: Do not use backdrop blurs or glassmorphism, as they feel too "digital" and fragile for an industrial context.

## Shapes

The shape language is strictly **Sharp (0px)**. 

To convey "Terra" and "Scale," the UI utilizes right angles and hard edges. This mimics the geometry of shipping containers, property boundaries, and steel beams. Rounding is only permitted in the form of "chamfered" corners (45-degree cuts) if used for decorative industrial accents, but the standard for buttons, cards, and inputs is a 90-degree corner. This reinforces the sense of precision and unyielding strength.

## Components

**Buttons**
Primary buttons are solid Safety Yellow with black text. They feature a 2px bottom "offset shadow" (solid black) to give them a tactile, physical presence. Hover states should simply darken the yellow.

**Input Fields**
Inputs feature a heavy bottom border (2px) in Earthy Brown. Labels are always visible and use the `label-caps` typography style. On focus, the border thickness increases to 3px.

**Data Chips**
Used for zoning or status (e.g., "Heavy Industrial," "Zoned"). These are rectangular, using a Slate Gray stroke with a very light gray fill. Text is high-contrast.

**Property Cards**
Cards are defined by a 1px Slate Gray border. The header of the card should use a subtle concrete texture background to differentiate the "title" area from the "data" area.

**Data Sheets (Mobile)**
For technical specs, use zebra-striping with a very pale brown tint on alternate rows to maintain tracking across the screen. Every row has a minimum height of 48px to ensure touch-friendly interaction for brokers in the field.

**Industrial Icons**
Icons must be monoline and geometric. Avoid rounded caps on icon strokes; use square caps to match the "Sharp" shape language.