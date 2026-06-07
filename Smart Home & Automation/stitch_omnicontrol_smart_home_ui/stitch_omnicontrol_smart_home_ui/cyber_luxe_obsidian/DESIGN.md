---
name: Cyber-Luxe Obsidian
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#303031'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#ffffff'
  on-secondary: '#003737'
  secondary-container: '#00fbfb'
  on-secondary-container: '#007070'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#121212'
  on-tertiary-container: '#7e7d7d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#00fbfb'
  secondary-fixed-dim: '#00dddd'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
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
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  gutter: 24px
  margin-safe: 32px
---

## Brand & Style

The design system is engineered for high-end technical interfaces where precision meets luxury. It targets an audience that values exclusivity, high-performance technology, and immersive digital environments. The emotional response is one of "calculated power"—a calm, dark environment punctuated by sharp, energetic signals.

The aesthetic is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes a "Deep Tech" philosophy: expansive matte surfaces provide the foundation, while translucent, frosted layers create a sense of physical depth and sophisticated materiality. Interaction is treated as a tactile event, using light and subtle movement to simulate physical responses.

## Colors

The palette is strictly nocturnal, anchored by **Matte Black (#121212)** to minimize eye fatigue and maximize contrast for accent elements. **Neon Cyan (#00FFFF)** acts as the singular source of "energy" in the UI, used for critical indicators, active states, and interactive hotspots. 

Secondary surfaces utilize a slightly lighter **Obsidian (#1A1A1A)** to define hierarchy without breaking the dark immersion. Transparency is a core color property; "Glass" surfaces are defined by low-opacity white overlays and cyan-tinted edge highlights to simulate refractive properties.

## Typography

This design system employs a dual-typeface strategy to balance technical edge with premium readability. **Space Grotesk** is used for headlines and functional labels, providing a geometric, futuristic silhouette that feels engineered. 

**Manrope** is used for all body copy and long-form data, offering a more organic and balanced sans-serif structure that ensures clarity against dark backgrounds. Tight letter-spacing is reserved for large headings to create a high-fashion, editorial look, while functional labels use wide tracking for maximum legibility at small sizes.

## Layout & Spacing

The layout follows a **Fixed Grid** model to maintain the structural integrity required of a premium tool. Content is centered within a maximum-width container to prevent visual "drift" on ultra-wide monitors. 

Spacing is based on a 4px geometric progression, emphasizing generous internal margins within cards to allow the glass effects to "breathe." Large-scale elements should span a 12-column system, while utility panels are anchored to the screen edges with consistent 32px safe-area margins.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and light-based hierarchy rather than traditional shadows. Surfaces are stacked using three primary methods:

1.  **Backdrop Blurs:** Floating cards use a 20px to 40px Gaussian blur on the background layer, creating a frosted appearance that maintains context while providing focus.
2.  **Inner Glows:** Instead of drop shadows, elevated elements use a 1px inner stroke (0.1 opacity white) and a faint Neon Cyan outer "aura" to simulate light emitting from the component.
3.  **Tonal Stacking:** The further "back" an element is in the Z-axis, the darker and more opaque the matte black becomes.

## Shapes

The design system utilizes **Rounded (0.5rem)** corners as its base, providing a sophisticated balance between technical sharpness and organic comfort. 

Large containers and glass cards use `rounded-xl` (1.5rem) to emphasize their "object-like" quality within the UI. Small interactive components like tags and toggles use the base `rounded` (0.5rem) to maintain a crisp, precise feel.

## Components

### Buttons & Controls
Buttons are "haptic-ready," utilizing a subtle scaling effect on press. Primary buttons are solid Neon Cyan with black text, while ghost buttons feature a frosted glass fill and a 1px cyan border. 

### Cards
Cards are the primary container. They must feature a semi-transparent background and a "light-leak" border—a gradient stroke that transitions from Cyan to transparent, simulating a light source hitting the edge of the glass.

### Sleek Sliders
Sliders use a thin 2px track. The handle is a high-gloss Cyan orb that leaves a faint glowing "trail" behind it.

### Glowing Indicators
Status indicators (on/off, active/inactive) are rendered as small, pulsating neon dots. They use an outer glow (box-shadow) with a 10px spread to simulate a physical light emission.

### Input Fields
Inputs are minimal, defined only by a bottom border in a low-opacity white. When focused, the border becomes a solid Cyan line with a soft glow reflecting onto the text above it.