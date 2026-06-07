---
name: Essence-Lab
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#dac1bf'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#a28c8a'
  outline-variant: '#544341'
  surface-tint: '#ffb3ad'
  primary: '#ffb3ad'
  on-primary: '#5a1a19'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#954742'
  secondary: '#ffe2ab'
  on-secondary: '#402d00'
  secondary-container: '#ffbf00'
  on-secondary-container: '#6d5000'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#242424'
  on-tertiary-container: '#8d8b8b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffdfa0'
  secondary-fixed-dim: '#fbbc00'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5c4300'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 16px
  margin: 24px
  container-max: 1200px
---

## Brand & Style
The design system is rooted in the "Scent of Mystery." It evokes the sensorial experience of high-end perfumery—atmospheric, intimate, and deeply personal. The brand target is the discerning connoisseur who values craftsmanship and the alchemy of scent.

The visual style follows a **Moody Minimalism** approach with elements of **Glassmorphism**. By layering semi-transparent surfaces over high-contrast, smoke-filled photography, the UI achieves a sense of depth and fluidity. The interface must feel "weightless" yet tactile, encouraging exploration through subtle motion and soft transitions that mimic the diffusion of fragrance in the air.

## Colors
The palette is centered on a high-luxury, nocturnal aesthetic. **Charcoal Black** serves as the infinite canvas, providing a deep, grounding base for all interfaces. **Deep Burgundy** is used for primary brand moments and emotional resonance, appearing in interactive states and key brand motifs. 

**Amber** acts as a luminous highlight, representing the liquid essence of the perfume. It is used sparingly for call-to-actions and indicators to ensure high contrast against the dark backgrounds. Surfaces utilize subtle gradients of Charcoal to Deep Burgundy to create a "smoky" depth rather than flat blocks of color.

## Typography
The typographic hierarchy relies on the tension between the classic and the contemporary. **Noto Serif** provides an authoritative, literary elegance for headlines, suggesting the heritage and boutique nature of the brand.

**Manrope** is used for body copy and functional labels to ensure absolute legibility on mobile devices. Large headlines should be set with tight letter spacing for a sophisticated editorial look, while uppercase labels in Manrope should have generous tracking (letter spacing) to denote a premium, curated feel.

## Layout & Spacing
The layout philosophy utilizes a **Fluid Grid** model with an emphasis on vertical rhythm and generous negative space to prevent visual clutter. On mobile, a 4-column system is used, expanding to 12 columns on desktop.

Spacing follows an 8px incremental scale. To reinforce the luxury feel, "safe zones" are larger than standard e-commerce sites, allowing photography to breathe. Content blocks are often offset or staggered to create a flow that feels organic and fluid rather than rigid and mechanical.

## Elevation & Depth
Depth in this design system is achieved through **Glassmorphism** and **Tonal Layers** rather than traditional drop shadows. 

1.  **Base Layer:** Solid Charcoal Black (#121212).
2.  **Mid Layer:** Semi-transparent Deep Burgundy surfaces with a `backdrop-filter: blur(20px)`.
3.  **Accent Layer:** Subtle Amber inner glows (0.5px) on active elements to simulate backlighting.

Where shadows are necessary, they are highly diffused and tinted with the primary Burgundy hue to maintain the atmospheric mood.

## Shapes
The shape language is architectural and precise. Elements use a **Soft (Level 1)** roundedness to maintain a sense of custom craftsmanship without appearing "bubbly" or overly playful. 

Buttons and inputs feature a subtle 4px corner radius. Circular elements are reserved exclusively for "scent profile" visualizations and fragrance notes, creating a visual metaphor for the roundness and balance of a well-composed perfume.

## Components
- **Buttons:** Primary buttons use a solid Deep Burgundy fill with Amber text. Secondary buttons are "ghost" style with a 1px Amber border and a subtle backdrop blur.
- **Cards:** Product cards are borderless with high-contrast photography. Information appears on a translucent burgundy overlay that slides up or fades in on interaction.
- **Inputs:** Minimalist bottom-border only fields. On focus, the border transitions from Charcoal to Amber with a soft outer glow.
- **Chips:** Used for scent notes (e.g., "Sandalwood," "Oud"). These are pill-shaped with a low-opacity Burgundy background and white text.
- **Progress Indicators:** Fluid, animated lines that mimic a "filling" liquid effect using Amber gradients.
- **Custom Scrollbar:** A thin, Amber-colored track that only appears during active scrolling to minimize visual distraction.