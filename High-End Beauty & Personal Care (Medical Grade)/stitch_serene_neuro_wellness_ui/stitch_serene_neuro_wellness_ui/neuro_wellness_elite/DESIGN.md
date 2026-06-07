---
name: Neuro-Wellness Elite
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#909097'
  outline-variant: '#45464c'
  surface-tint: '#c0c6db'
  primary: '#c0c6db'
  on-primary: '#2a3041'
  primary-container: '#050b1a'
  on-primary-container: '#737a8d'
  inverse-primary: '#585e70'
  secondary: '#cbbeff'
  on-secondary: '#322664'
  secondary-container: '#493d7c'
  on-secondary-container: '#b9acf3'
  tertiary: '#c3c0ff'
  on-tertiary: '#1d00a5'
  tertiary-container: '#05003b'
  on-tertiary-container: '#6a64ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dce2f8'
  primary-fixed-dim: '#c0c6db'
  on-primary-fixed: '#151b2b'
  on-primary-fixed-variant: '#404658'
  secondary-fixed: '#e6deff'
  secondary-fixed-dim: '#cbbeff'
  on-secondary-fixed: '#1d0e4e'
  on-secondary-fixed-variant: '#493d7c'
  tertiary-fixed: '#e2dfff'
  tertiary-fixed-dim: '#c3c0ff'
  on-tertiary-fixed: '#0f0069'
  on-tertiary-fixed-variant: '#3323cc'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin: 64px
  section-gap: 128px
---

## Brand & Style

This design system embodies a "Cognitive Sanctuary" aesthetic—a fusion of cutting-edge neuroscience and serene mindfulness. The brand personality is authoritative yet empathetic, positioning itself as a high-performance tool for mental clarity. 

The visual style is **Glassmorphism**, utilized to create a sense of lightness and transparency in data processing. It avoids the heavy, opaque interfaces of traditional medical software in favor of airy, multi-layered environments. The emotional response is one of "focused calm," where the user feels they are interacting with an intelligent, sophisticated partner in their wellness journey.

## Colors

The palette is anchored by **Midnight Blue**, serving as a deep, expansive canvas that reduces eye strain and evokes the stillness of deep thought. **Lavender** acts as the primary focal point, used for interactive elements and highlights to provide a soft, non-aggressive contrast.

To achieve the glassmorphism effect, the system utilizes translucent whites (White at 5-15% opacity) for surface layers. Gradients should be subtle and radial, mimicking the natural fall of light on organic surfaces.

## Typography

This design system utilizes a dual-font strategy to balance technical precision with human accessibility. **Space Grotesk** is reserved for headlines and data labels, providing a geometric, futuristic rhythm. **Manrope** is used for body text and descriptive content, ensuring readability and a soft, professional tone.

Generous letter spacing (tracking) is applied across all levels to enhance the "premium" feel and prevent the UI from feeling cluttered during data-heavy interactions.

## Layout & Spacing

The layout follows a **Fixed Grid** model with extreme breathing room. Large outer margins (64px+) ensure that content feels centered and focused, reflecting a state of "uncluttered mind."

The spacing rhythm is built on an 8px base unit, but emphasizes large "Section Gaps" to separate distinct cognitive tasks. Components should be spaced widely enough to allow the background gradients and blurs to remain visible, maintaining the sense of depth.

## Elevation & Depth

Depth is established through **Glassmorphism and Backdrop Blurs** rather than traditional drop shadows. 

1.  **Base Layer:** Midnight Blue background with soft, moving radial gradients in Lavender.
2.  **Surface Layer:** 10% white opacity with a 24px-40px Backdrop Blur and a subtle 1px white border (10% opacity) to define edges.
3.  **Active Layer:** Lavender glows (Bloom effect) positioned behind active elements to indicate focus or "brain activity."

Shadows, when used, are extremely diffused and tinted with the Primary Midnight Blue to avoid "dirty" grey artifacts.

## Shapes

The shape language uses **Rounded** corners to communicate safety and approachability. A standard 1rem (16px) radius is used for primary cards, while interactive elements like buttons use slightly more pronounced curves to feel "touchable" and organic. Sharp 90-degree angles are avoided entirely to maintain the serene visual narrative.

## Components

### Buttons
Primary buttons use a solid Lavender fill with dark text. Secondary buttons utilize the glass effect: a translucent white background with a thin Lavender stroke and Lavender text. Hover states should include a soft "outer glow" bloom.

### Cards
Cards are the primary container for data. They must feature a `backdrop-filter: blur(20px)` and a 1px inner border. Content inside cards should have a minimum of 32px padding to maintain the airy aesthetic.

### Data Visualization
Charts and graphs should use glowing, neon-inspired lines in Lavender and Cyan. Area charts should use soft gradients that fade into the background, rather than hard solid fills.

### Input Fields
Inputs are "ghost" style: no background fill, only a subtle bottom border or a very faint translucent frame. On focus, the border transitions to Lavender with a soft shadow.

### Bio-Feedback Indicators
Unique to this system, include pulse indicators or "breathing" animations for real-time neuro-data, using soft scaling animations and opacity shifts.