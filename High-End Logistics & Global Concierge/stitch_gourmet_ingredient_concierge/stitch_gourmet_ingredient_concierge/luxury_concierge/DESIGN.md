---
name: Luxury Concierge
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#dcc0bd'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a38b88'
  outline-variant: '#554240'
  surface-tint: '#ffb4aa'
  primary: '#ffb4aa'
  on-primary: '#5f1410'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#9d4139'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#212121'
  on-tertiary-container: '#8a8888'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  margin-mobile: 24px
  margin-desktop: 64px
  gutter: 16px
  section-gap: 80px
---

## Brand & Style
The design system embodies an "Artistic-Moody" aesthetic, specifically tailored for an ultra-high-end culinary audience. The brand personality is exclusive, knowledgeable, and uncompromising. It avoids common corporate tropes in favor of an editorial, gallery-like experience. 

The visual style leverages high-contrast compositions where deep, immersive shadows meet sharp, golden highlights. We utilize a blend of **Minimalism** and **Glassmorphism**, ensuring that the rare ingredients—the truffles and the marbled wagyu—remain the focal point through full-screen, high-fidelity photography. Every interaction must feel intentional, using slow, cinematic transitions to reinforce the feeling of a bespoke concierge service.

## Colors
The palette is rooted in a "Noir-Culinaria" philosophy. The primary color is a **Deep Burgundy**, evocative of aged wine and rare meats, used sparingly for depth and emotional resonance. The secondary **Amber** acts as a metallic gold accent, reserved for calls to action, premium indicators, and refined borders.

The background is a tiered **Rich Black**, providing a canvas that allows high-contrast food photography to "pop" off the screen. Gradients are subtle and linear, typically transitioning from transparent to a solid black to ensure text legibility over full-bleed imagery.

## Typography
The typographic strategy relies on the tension between the classic and the contemporary. **Playfair Display** provides the editorial authority required for a luxury service, used for large-scale headlines and price points. 

For functional UI and long-form descriptions, **Hanken Grotesk** offers a clean, sharp, and modern contrast. We use a "Label-Caps" style for navigation and metadata to instill a sense of precision and meticulousness. Line heights are generous to maintain an airy, unhurried feel even within a dark, moody environment.

## Layout & Spacing
This design system employs a **Fixed Grid** model with a heavy mobile-first emphasis. On mobile devices, we utilize a 4-column grid with generous 24px side margins to ensure the content feels framed like a piece of art. 

The spacing rhythm is based on a 4px baseline, but we intentionally utilize large "empty" blocks (Section Gaps) to prevent the interface from feeling cluttered. Content is often center-aligned or dramatically offset to create a dynamic, rhythmic flow as the user scrolls.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Glassmorphism** rather than traditional drop shadows. We avoid heavy blurs in favor of "Surface-Container" tiers:
- **Base:** The deep #050505 black background.
- **Mid:** Semi-transparent #1A1A1A overlays with a 12px backdrop blur for floating cards or navigation bars.
- **High:** Subtle 1px inner-borders in Amber (#D4AF37) at 20% opacity to define edges.

Shadows, when used, are "Ambient Shadows"—extremely diffused, long, and tinted with the Primary Burgundy color to maintain the moody atmosphere.

## Shapes
The shape language is disciplined and "Soft." We use a 0.25rem (4px) base radius to take the edge off sharp corners without losing the sophisticated, architectural feel of the brand. 

Interactive elements like buttons and input fields maintain this consistent, subtle roundness. Photography containers may occasionally use a "Sharp" (0px) radius when they are full-bleed to emphasize the expansive nature of the imagery.

## Components
- **Buttons:** Primary buttons feature a solid Amber background with black Hanken Grotesk text. Secondary buttons are "Ghost" style with a 1px Amber border and high-letter-spacing caps.
- **Minimalist Cards:** Cards have no background fill by default; they use a 1px subtle border or a slight tonal shift. The focus is entirely on the typography and the product image.
- **Input Fields:** Bottom-border only (border-bottom: 1px solid #D4AF37) to mimic high-end stationery. Labels float above the line in Label-Caps style.
- **Chips:** Used for ingredient origins (e.g., "Piedmont," "Kobe"). These are small, dark grey backgrounds with low-opacity Amber text.
- **Transitions:** Every component transition should use a `cubic-bezier(0.4, 0, 0.2, 1)` timing function to create a "weighted" feel.
- **Status Indicators:** For "In Stock" or "Sourced," use a small, glowing Amber dot rather than standard green/red icons to maintain the aesthetic.