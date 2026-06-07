---
name: Raw Material
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
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#b9c7e0'
  on-secondary: '#233144'
  secondary-container: '#3c4a5e'
  on-secondary-container: '#abb9d2'
  tertiary: '#b9c8de'
  on-tertiary: '#233143'
  tertiary-container: '#8b9aaf'
  on-tertiary-container: '#233243'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 8px
  gutter: 24px
  margin: 48px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built on the philosophy of structural integrity and functional honesty. It captures the "Raw Material" of residential construction—concrete, steel, and high-visibility safety—and refines them into a professional digital environment. The aesthetic sits at the intersection of **Industrial Brutalism** and **Modern Corporate** design.

The brand personality is authoritative, weathered, and unshakeable. It avoids the "polished corporate" clichés in favor of a tactile, ground-level perspective. The UI should evoke the feeling of a blueprint or a well-organized job site: every element has a purpose, every boundary is clearly defined, and the overall impression is one of immense reliability and physical presence. To achieve this, we utilize heavy strokes, subtle film grain textures to mimic concrete dust, and a strict adherence to a grid that feels architectural.

## Colors

The color palette is derived directly from the job site. The foundation is a "Dark Mode" environment using **Charcoal (#1A1A1A)** and **Slate (#334155)** to represent structural steel and deep shadows. These are complemented by a range of **Concrete Grays** that provide tonal layering without losing the gritty essence of the brand.

The primary accent is **High-Visibility Orange (#FF6B00)**. This color is used sparingly but with high impact to denote action, safety, and critical information. It should pop aggressively against the desaturated backgrounds, much like a safety vest on a construction site. Functional colors (Success/Error) should be desaturated to maintain the professional, understated tone of the system.

## Typography

Typography in this design system is engineered for clarity and impact. We use **Space Grotesk** for headlines and technical labels; its geometric, slightly idiosyncratic letterforms suggest a technical or architectural precision. Large-scale headings should be set with tight tracking to feel heavy and imposing.

For body text, **Work Sans** provides a grounded and versatile reading experience. It maintains a professional, neutral tone that balances the aggressive nature of the headlines. Labels and metadata should frequently use the `label-caps` style to mimic the stenciled lettering found on crates and heavy machinery.

## Layout & Spacing

The layout follows a **Fixed Grid** model, treated like a structural blueprint. A 12-column system is used for desktop, with rigid 24px gutters that are never collapsed. This creates a sense of "frames" and "bays" within the UI.

Spacing is governed by a strict 8px linear scale. We favor generous vertical "stacks" to give the content room to breathe, ensuring the density of the "raw" materials doesn't become overwhelming. High-impact imagery should span the full width of the grid container or exactly half (6 columns) to maintain architectural symmetry.

## Elevation & Depth

This design system rejects soft, ambient shadows in favor of **Structural Layering** and **Bold Borders**. 

1.  **Hard Borders:** Instead of shadows, use 2px solid borders (#334155) to define containers.
2.  **Tonal Stacking:** Depth is achieved by placing lighter gray surfaces on top of darker ones (e.g., a Slate card on a Charcoal background).
3.  **Grain & Texture:** A subtle 3-5% opacity noise overlay should be applied to the primary background to simulate the texture of concrete or cast stone.
4.  **Cut-outs:** Use "inset" borders for input fields to make them feel carved into the surface rather than floating above it.

## Shapes

The shape language is strictly **Sharp (0px)**. Construction materials like I-beams, concrete blocks, and plywood sheets are defined by hard edges and right angles. By eliminating border radii, the UI gains a sense of permanence and strength. Every button, card, and input field must feature crisp 90-degree corners to reinforce the industrial aesthetic.

## Components

### Buttons
Primary buttons are solid High-Vis Orange with black text. They feature no gradients or shadows, only a hard 2px black or dark-slate border. On hover, the button should invert colors or shift to a slightly lighter orange.

### Cards & Containers
Cards are defined by a 2px Slate border and a subtle grain texture. Headlines inside cards should be followed by a thin horizontal rule (1px) to separate the "header" from the "content," mimicking technical drawings.

### Input Fields
Inputs use a dark background (#121212) with a 2px Slate border. Labels sit above the input in the `label-caps` typography style. Focus states must use the High-Vis Orange for the border color.

### Progress Indicators
Modeled after measuring tapes or structural gauges. Use thick, blocky bars with no rounding. Use the primary orange to indicate "work in progress" or "completion."

### Additional Components
- **The "Spec" Sheet:** A stylized list component for technical details, using monospaced labels and dotted leaders to connect keys to values.
- **Status Badges:** Solid-color rectangular blocks (no rounding) with heavy-weight text.