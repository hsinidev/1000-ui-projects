---
name: Zen-Industrial Minimalist
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#4f453b'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#81756a'
  outline-variant: '#d3c4b7'
  surface-tint: '#7b5730'
  primary: '#7b5730'
  on-primary: '#ffffff'
  primary-container: '#b58b5f'
  on-primary-container: '#412603'
  inverse-primary: '#edbe8e'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#605e5a'
  on-tertiary: '#ffffff'
  tertiary-container: '#95938e'
  on-tertiary-container: '#2d2c28'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdcbc'
  primary-fixed-dim: '#edbe8e'
  on-primary-fixed: '#2c1700'
  on-primary-fixed-variant: '#60401b'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e5e2dc'
  tertiary-fixed-dim: '#c9c6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#484743'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  h1:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: notoSerif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: notoSerif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  ma-xs: 16px
  ma-sm: 32px
  ma-md: 64px
  ma-lg: 128px
  gutter: 24px
  margin: 48px
---

## Brand & Style
The design system is a meditation on the intersection of Japanese craftsmanship and Scandinavian functionalism. It bridges the gap between the raw, structural honesty of industrial design and the soft, organic tranquility of Zen philosophy. The visual language centers on the concept of *Ma*—the intentional use of negative space—to create a sense of breath and focus.

The design style is **Minimalist-Tactile**. While the layouts remain strictly architectural and grid-bound, the interface utilizes high-fidelity textures to evoke a physical presence. The user experience is designed to feel grounded, deliberate, and quiet, moving away from digital noise toward a more artisanal, curated digital environment.

## Colors
The palette is rooted in natural materials. **Washi** (off-white) serves as the primary canvas, providing a warmer, more organic background than pure white. **Matte Black** and **Ink** provide structural weight and high-contrast legibility for typography.

**Oak** and **Cedar** are used as functional accents to highlight primary actions and interactive states, mimicking the warmth of wood in a concrete space. **Stone Grey** acts as a secondary structural color for borders, dividers, and inactive states, maintaining a neutral, industrial baseline.

## Typography
The typographic hierarchy relies on the tension between a refined serif and a systematic sans-serif. **Noto Serif** is reserved for headlines and editorial moments, conveying a sense of heritage and precision. It should be typeset with generous leading and occasional asymmetrical alignment.

**Manrope** provides a clean, functional counterpoint for body copy and interface labels. Its geometric yet approachable structure ensures legibility across industrial-themed UI components. For metadata and small labels, use the "Label Caps" style with increased letter spacing to evoke the feeling of architectural blueprints.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy inspired by *Tatami* mat proportions. A 12-column grid is used for desktop, but elements should rarely be centered. Instead, embrace asymmetrical balance by shifting content blocks to the left or right, leaving wide margins (Ma) to create focal points.

The spacing rhythm is strictly based on an 8px module. Use larger spacing increments (`ma-md` and `ma-lg`) between major sections to prevent visual clutter and maintain the "Zen" aesthetic.

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layers** and **Tactile Textures** rather than traditional drop shadows. 

1.  **Base Layer:** The Washi paper background.
2.  **Surface Layer:** Subtle Stone Grey or very light Wood Grain textures for container backgrounds.
3.  **Dividers:** Use 1px solid lines in Stone or Matte Black to define boundaries. 
4.  **Interaction:** Instead of "lifting" an object with a shadow, change its texture (e.g., a button transitions from a flat Stone texture to a rich Oak grain on hover).

If depth is absolutely required for overlays, use a single, sharp 2px "cut-out" border or a very soft, diffused ambient occlusion tint (#1A1A1A at 5% opacity).

## Shapes
The shape language is **Sharp (0px)**. To reflect industrial precision and traditional Japanese joinery, all buttons, cards, and input fields use 90-degree corners. This uncompromising geometry reinforces the grid and creates a sense of architectural permanence. 

In rare instances where an organic element is needed (such as a profile image), use a perfect circle to provide a singular point of contrast against the rigid rectangular environment.

## Components

### Buttons
Buttons are rectangular with 0px radius. The **Primary Button** features a Matte Black background with Washi-toned text. The **Secondary Button** uses an Oak wood-grain texture overlay. Interaction states should involve a subtle shift in grain intensity or a color transition to Cedar.

### Input Fields
Inputs are defined by a bottom-border only (1px Stone Grey), mimicking a clean slate. When focused, the border transitions to Matte Black. Labels always sit above the field in "Label Caps" style.

### Cards & Containers
Cards do not use shadows. They are defined by either a 1px Stone border or a subtle fill change (e.g., a Stone-colored background against a Washi page). Use asymmetrical padding inside cards—for example, more padding on the bottom than the top—to maintain the Japandi aesthetic.

### Material Palette Selectors
A unique component for this system: small, square tactile chips representing different materials (Oak, Stone, Fabric). These are used for filtering or customization, featuring high-resolution photographic textures cropped into the sharp-edged square.

### Progress Indicators
Linear and minimalist. Avoid circular loaders. Use a thin, 2px horizontal bar that fills with the Oak accent color.