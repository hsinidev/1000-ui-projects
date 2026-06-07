---
name: Architectural Luxe
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444748'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5e5e5e'
  primary: '#5b5c5c'
  on-primary: '#ffffff'
  primary-container: '#747475'
  on-primary-container: '#fefcfc'
  inverse-primary: '#c7c6c6'
  secondary: '#8e4e00'
  on-secondary: '#ffffff'
  secondary-container: '#ffa857'
  on-secondary-container: '#723e00'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3e2e2'
  primary-fixed-dim: '#c7c6c6'
  on-primary-fixed: '#1b1c1c'
  on-primary-fixed-variant: '#464747'
  secondary-fixed: '#ffdcc1'
  secondary-fixed-dim: '#ffb779'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6c3a00'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-xl:
    fontFamily: metropolis
    fontSize: 72px
    fontWeight: '300'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: metropolis
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: 0.05em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: 0.1em
  body-lg:
    fontFamily: ebGaramond
    fontSize: 20px
    fontWeight: '400'
    lineHeight: 30px
  body-md:
    fontFamily: ebGaramond
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: metropolis
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.2em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style
The design system embodies "Architectural Luxe," a visual language rooted in structural integrity and material honesty. It is designed for "Sculpt-Space," catering to a sophisticated audience of interior designers and art collectors. The brand personality is silent but commanding—prioritizing the 3D-printed form over excessive interface ornamentation.

The style is a fusion of **Minimalism** and **Tactile Modernism**. It leverages high-contrast transitions between raw, industrial surfaces and refined metallic accents. The user experience should feel like walking through a brutalist gallery: spacious, quiet, and meticulously curated. Interactive elements mimic the friction and weight of physical objects, emphasizing the precision of 3D craftsmanship.

## Colors
The palette is architectural and grounded. **Exposed Concrete Grey (#8C8C8C)** serves as the structural foundation, used for structural dividers and secondary backgrounds to provide a neutral, industrial stage. **Pure White (#FFFFFF)** is used for primary canvas areas to ensure high-fidelity 3D assets pop with clarity. 

**Metallic Bronze (#CD7F32)** is the precision element, reserved for high-value interactions, call-to-actions, and highlights that represent the "luxury" of the 3D printing filament. A deep carbon neutral (#1A1A1A) is used for text to maintain a high-contrast ratio against white and grey surfaces.

## Typography
The typographic strategy balances geometric precision with classical elegance. **Metropolis** is utilized for headlines and navigational elements; its structured, architectural forms mirror the 3D printing process. Headlines should use generous letter-spacing to evoke a sense of high-end editorial design.

**EB Garamond** is the primary serif for body copy, introducing a humanistic and intellectual warmth that softens the industrial grey tones. This contrast between the "technical" sans-serif and the "literary" serif reinforces the boutique nature of the brand. Use "Label-SM" for technical specifications of sculptures to give them a blueprint-like feel.

## Layout & Spacing
The design system employs a **Fixed Grid** model within a 1440px container, utilizing a 12-column structure. Spacing is intentionally aggressive and "wasteful" to signal luxury; large horizontal margins and vertical gaps prevent the interface from feeling cluttered.

Information is grouped into "Structural Blocks" defined by the 8px base unit. Sections should be separated by significant whitespace (128px+) to allow the 3D assets to be viewed in isolation, much like pieces in a physical gallery.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and **Material Contrast** rather than traditional drop shadows. Surfaces are stacked using color: a White surface might sit atop a Concrete Grey background to indicate a higher z-index.

Where depth is necessary for interaction (e.g., hovering over a sculpture card), use a subtle, sharp 1px border in Metallic Bronze or a slight "lift" effect using a very low-opacity ambient shadow (Alpha 0.05). Soft textures—simulating the micro-porosity of concrete or the brushed grain of metal—should be applied as subtle SVG overlays on backgrounds to provide a tactile sense of "place."

## Shapes
In alignment with the architectural narrative, the design system utilizes **Sharp (0px)** corners for all primary containers, buttons, and structural elements. The rigidity of the interface serves as a foil to the organic, flowing "sculpted" lines of the 3D assets themselves. 

Only the 3D assets should feature curves. UI components must remain strictly rectilinear to maintain a sense of precision engineering and blueprints.

## Components
- **Buttons:** Primary buttons are Solid Bronze (#CD7F32) with White caps-lock Metropolis text. Secondary buttons are "Ghost" style with a 1px Concrete Grey border. No rounding.
- **Interactive 3D Cards:** Cards featuring sculpture previews should have a Pure White background and a 1px Grey hairline border. On hover, the border transitions to Bronze.
- **Input Fields:** Minimalist underlines only (1px Concrete Grey), transitioning to Bronze on focus. Labels sit above the line in uppercase Metropolis.
- **Progress Indicators:** For 3D asset loading, use a thin, architectural line that fills with Bronze, avoiding standard circular spinners.
- **Navigation:** Top-tier navigation uses wide letter-spacing. Active states are indicated by a 2px Bronze underline that spans the width of the text.
- **Image Treatment:** All sculpture photography should be silhouetted or set against neutral, tonal backgrounds that match the #F5F5F5 or #8C8C8C tokens.