---
name: Technical Luxury Hydration
colors:
  surface: '#101419'
  surface-dim: '#101419'
  surface-bright: '#35393f'
  surface-container-lowest: '#0a0f13'
  surface-container-low: '#181c21'
  surface-container: '#1c2025'
  surface-container-high: '#262a30'
  surface-container-highest: '#31353b'
  on-surface: '#dfe2ea'
  on-surface-variant: '#bec8ce'
  inverse-surface: '#dfe2ea'
  inverse-on-surface: '#2d3136'
  outline: '#899298'
  outline-variant: '#3f484d'
  surface-tint: '#7fd1f7'
  primary: '#d1eeff'
  on-primary: '#003547'
  primary-container: '#86d8ff'
  on-primary-container: '#005e7c'
  inverse-primary: '#006685'
  secondary: '#c1c7cf'
  on-secondary: '#2b3137'
  secondary-container: '#41474e'
  on-secondary-container: '#afb6bd'
  tertiary: '#e9e9ec'
  on-tertiary: '#2f3133'
  tertiary-container: '#cdcdd0'
  on-tertiary-container: '#555759'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#bfe8ff'
  primary-fixed-dim: '#7fd1f7'
  on-primary-fixed: '#001f2a'
  on-primary-fixed-variant: '#004d65'
  secondary-fixed: '#dde3eb'
  secondary-fixed-dim: '#c1c7cf'
  on-secondary-fixed: '#161c22'
  on-secondary-fixed-variant: '#41474e'
  tertiary-fixed: '#e2e2e5'
  tertiary-fixed-dim: '#c6c6c9'
  on-tertiary-fixed: '#1a1c1e'
  on-tertiary-fixed-variant: '#454749'
  background: '#101419'
  on-background: '#dfe2ea'
  surface-variant: '#31353b'
typography:
  display-xl:
    fontFamily: spaceGrotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: spaceGrotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: spaceGrotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-padding: 80px
---

## Brand & Style

The brand personality of this design system is rooted in elite performance and mechanical precision. It targets high-performance athletes and professionals who demand gear that is both indestructible and aesthetically refined. The UI must evoke a sense of "technical luxury"—the feeling of handling a precision-milled instrument that is cold to the touch and perfectly weighted.

The design style combines **Minimalism** with **High-Contrast Technical** elements. It utilizes heavy whitespace to allow high-fidelity product photography to breathe, punctuated by dense, data-rich overlays. Visual cues are drawn from industrial engineering: hairline strokes, monochromatic scales, and "liquid" motion curves that mimic the fluid dynamics of water. The emotional response is one of absolute reliability, chilled freshness, and advanced thermal control.

## Colors

The palette is anchored in a high-contrast dark mode to emphasize the "Matte Grey" and "Silver" textures of the hardware. **Ice Blue** serves as the primary action and state color, representing peak thermal cooling. **Silver** is used for structural lines and hairline borders to simulate brushed aluminum.

**Matte Grey** and **Deep Charcoal** form the foundation of the interface, providing a non-reflective, premium surface that reduces visual noise. Functional accents use a temperature-sensitive logic: "Ice Blue" for cooling states and a muted "Titanium White" for metadata. High-performance data visualizations should utilize gradients between Silver and Ice Blue to represent fluid movement.

## Typography

This design system utilizes **Space Grotesk** for all headlines and technical labels to reinforce the "precision-engineered" aesthetic. Its geometric quirks provide a futuristic, laboratory-grade feel. **Inter** is employed for body copy to ensure maximum legibility and a neutral, functional tone.

Key typographic treatments include the use of `label-caps` for all metadata and technical specifications, paired with `data-mono` for live thermal readouts. Large display type should be used sparingly but aggressively to create a sense of scale, mirroring the monolithic presence of the physical product.

## Layout & Spacing

The layout follows a **Fixed Grid** system for desktop (12 columns) and a fluid model for mobile. Every element is aligned to a strict 4px baseline grid to ensure mathematical precision. Gutters are kept wide to prevent the "technical" data from feeling cluttered, maintaining the "luxury" aspect of the brand.

Content blocks should be separated by significant vertical padding (`section-padding`) to create a gallery-like experience. Information density is managed through modular "pods"—self-contained data units that snap to the grid. Use hard alignment for text and imagery to mimic the rigid construction of insulated flasks.

## Elevation & Depth

Elevation in this design system is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. Surfaces are stacked using varying shades of Matte Grey and Charcoal. Depth is reinforced with "Silver" hairline borders (0.5pt to 1pt) that catch the "light" like the edge of a metal lid.

To represent the "Ice" element, **Glassmorphism** is used for overlaying data panels. These panels feature a high-intensity backdrop blur (20px+) and a subtle inner glow, suggesting condensation or a frost-covered surface. Shadows, when used, are "Ambient Shadows"—extremely diffused, low-opacity, and tinted with a hint of Ice Blue to simulate a cool glow.

## Shapes

The shape language reflects industrial machining. A **Soft (0.25rem)** roundedness is the standard, providing enough ergonomic comfort to feel premium without losing the sharp, technical edge. This mimics the precise radius of a CNC-milled component.

Circular elements (perfect 1:1 aspect ratio) are reserved exclusively for "liquid" indicators and thermal gauges, creating a visual distinction between the "container" (rectangular/rigid) and the "content" (circular/fluid). Avoid organic or overly rounded "pill" shapes for buttons; prefer the precision of the standard radius.

## Components

**Buttons:** Buttons are high-contrast blocks. Primary buttons use an Ice Blue fill with black text; secondary buttons use a Silver "ghost" style with a 1px border. Hover states should trigger a "liquid fill" animation where the color rises from the bottom of the button.

**Thermal Charts:** Data visualizations must be "precision-engineered." Use hairline paths with Ice Blue gradients. Data points should be represented by micro-crosshairs rather than dots.

**Inputs & Fields:** Fields are underlined with a Silver 1px stroke that turns Ice Blue on focus. Labels are always `label-caps` positioned above the field.

**Cards:** Cards utilize the Tonal Layering approach. They have no visible shadow but are defined by a 1px Matte Grey border that is slightly lighter than the background. 

**Fluid Elements:** Incorporate a "Liquid Progress Bar" for hydration tracking, where the fill level has a subtle wave-motion animation at the leading edge.

**Textures:** Incorporate "Material Cards" that feature high-resolution textures of powder-coated steel or brushed silver as background elements for product feature highlights.