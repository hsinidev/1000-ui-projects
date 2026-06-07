---
name: Nomad-Luxe
colors:
  surface: '#131411'
  surface-dim: '#131411'
  surface-bright: '#3a3936'
  surface-container-lowest: '#0e0e0c'
  surface-container-low: '#1c1c19'
  surface-container: '#20201d'
  surface-container-high: '#2a2a27'
  surface-container-highest: '#353532'
  on-surface: '#e5e2dd'
  on-surface-variant: '#dcc1b9'
  inverse-surface: '#e5e2dd'
  inverse-on-surface: '#31302d'
  outline: '#a48b84'
  outline-variant: '#56423c'
  surface-tint: '#ffb59e'
  primary: '#ffb59e'
  on-primary: '#5e1700'
  primary-container: '#dd7250'
  on-primary-container: '#521300'
  inverse-primary: '#9d4223'
  secondary: '#bcc7dd'
  on-secondary: '#263142'
  secondary-container: '#3c475a'
  on-secondary-container: '#aab6cc'
  tertiary: '#bdc7dc'
  on-tertiary: '#273141'
  tertiary-container: '#8791a5'
  on-tertiary-container: '#202a3a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#ffb59e'
  on-primary-fixed: '#3a0b00'
  on-primary-fixed-variant: '#7e2b0e'
  secondary-fixed: '#d8e3fa'
  secondary-fixed-dim: '#bcc7dd'
  on-secondary-fixed: '#111c2c'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#d9e3f9'
  tertiary-fixed-dim: '#bdc7dc'
  on-tertiary-fixed: '#121c2c'
  on-tertiary-fixed-variant: '#3d4759'
  background: '#131411'
  on-background: '#e5e2dd'
  surface-variant: '#353532'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 60px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 8px
  container-max: 1440px
  gutter: 24px
  margin-edge: 64px
  section-gap: 120px
---

## Brand & Style

This design system is engineered to evoke the intersection of unyielding durability and uncompromising luxury. It serves a clientele that demands elite performance in the world’s harshest environments without sacrificing sophisticated comfort. The visual language is rooted in a **Tactile Industrial** aesthetic—balancing the raw, utilitarian essence of expedition gear with the polished refinement of a high-end atelier.

The UI utilizes a "Machined Precision" philosophy: every element should feel like it was milled from a solid block of material. We lean into heavy textures—specifically brushed metal and canvas grain—to provide a sense of physical presence. This is contrasted by generous whitespace and high-fashion editorial layouts, ensuring the product feels as at home in a desert crossing as it does in a private hangar.

## Colors

The palette is informed by the transition from the garage to the horizon. 

*   **Primary (Terracotta):** Used as a functional highlight and a nod to the earth. It should be reserved for primary calls to action and critical status indicators.
*   **Secondary & Tertiary (Slate & Industrial Grey):** These form the structural foundation of the interface, mimicking weathered steel and volcanic rock.
*   **Contrast (Sand):** This off-white serves as the primary canvas for text and high-contrast backgrounds, providing a premium, readable surface that softens the industrial core.

The default mode is **Dark**, emphasizing the "Industrial Grey" and "Slate" to create a cockpit-like atmosphere that feels focused and high-end.

## Typography

The typographic hierarchy is designed to command authority. 

For headlines, we utilize **Noto Serif** at its heaviest weights to mimic the impact of a slab-serif. This choice provides a literary, elite feel that bridges the gap between ruggedness and high-culture. 

The body text uses **Work Sans**, selected for its grounded, neutral, and highly legible characteristics. To lean into the "industrial" aesthetic, **Space Grotesk** is used for labels, technical data, and micro-copy. All labels should be set in all-caps with generous letter spacing to replicate the look of stamped serial numbers on vehicle components.

## Layout & Spacing

The design system employs a **Fixed Grid** model to maintain the rigorous structure of a technical blueprint. A 12-column grid is used with wide gutters (24px) and substantial outer margins (64px) to ensure content feels curated and premium.

Spacing follows an 8px rhythmic scale, but vertical section gaps are intentionally exaggerated (120px+) to evoke the vastness of the landscapes these vehicles traverse. Elements should often span 4, 6, or 8 columns to create asymmetric, editorial layouts that avoid the "boxy" feel of standard SaaS products.

## Elevation & Depth

Depth in this design system is conveyed through **Tonal Layers** and **Physical Metaphor** rather than traditional soft shadows.

1.  **Layering:** Surfaces are stacked using color—Terracotta elements sit atop Industrial Grey, which sits atop a textured Sand or Slate base. 
2.  **Hard Edges:** Avoid diffused shadows. Instead, use thin (1px), high-contrast inner borders in a lighter tint of the surface color to simulate a "beveled" or "machined" edge.
3.  **Texture Overlays:** Use low-opacity (.03 - .05) SVG patterns of brushed aluminum or canvas on containers to create a tactile sense of material weight.

## Shapes

The shape language is strictly **Sharp (0px)**. 

To reinforce the durable and elite brand personality, UI elements avoid rounded corners entirely. This "Hard-Edge" philosophy mimics the precision-cut steel and rugged chassis of an expedition vehicle. Occasional 45-degree clipped corners (chamfers) may be used on buttons or "status tags" to further the industrial, military-grade aesthetic.

## Components

### Buttons
Primary buttons are solid Terracotta with Sharp corners. They utilize a heavy inset border on hover to simulate a physical "press." Text is always the "label-caps" style for a technical look.

### Input Fields
Inputs are defined by a heavy bottom border (2px) in Slate rather than a full box. When active, the border shifts to Terracotta. Labels sit above the field in the Space Grotesk caps style.

### Cards & Containers
Cards do not use shadows. They are defined by a solid 1px Industrial Grey border or a slight tonal shift from the background. Large-scale cards may feature a "canvas" texture overlay to provide visual depth.

### Data Viz & Gauges
Given the vehicle focus, the design system includes custom "Telematic" components—circular or linear progress bars that resemble analog dials found in high-end vehicle cockpits, utilizing thin lines and Space Grotesk numerals.

### Imagery
Images should be high-contrast, featuring deep shadows and warm highlights. Use a slight grain filter to match the "Tactile" style of the UI.