---
name: Velocità Luxe
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
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#bcc3ff'
  on-tertiary: '#001a97'
  tertiary-container: '#000432'
  on-tertiary-container: '#5369ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#dfe0ff'
  tertiary-fixed-dim: '#bcc3ff'
  on-tertiary-fixed: '#000d60'
  on-tertiary-fixed-variant: '#0029d3'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
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
    letterSpacing: 0.15em
  ui-action:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style
The brand personality is defined by an uncompromising commitment to excellence, catering to a discerning clientele that values time, exclusivity, and precision. This design system evokes the feeling of a private concierge service—effortless, quiet, yet powerful.

The design style utilizes a hybrid of **Minimalism** and **Glassmorphism**. By leaning into heavy whitespace and a restricted palette, the system allows high-contrast imagery of exotic automobiles to serve as the primary visual driver. Glassmorphism is applied selectively to create depth and a sense of "tech-forward" luxury, simulating the polished surfaces of high-end automotive cockpits.

## Colors
This design system employs a "Dark Mode" default to emphasize the "Deep Onyx Black" (#0A0A0A) base, which provides a premium, cinematic backdrop. 

- **Primary:** Deep Onyx Black serves as the foundation for all surfaces.
- **Secondary:** Metallic Silver is used for iconography, thin borders, and secondary text, providing a cold, machined aesthetic.
- **Tertiary (Accent):** Electric Blue is reserved strictly for interactive elements, primary calls to action, and status indicators. It should be used sparingly to maintain high visual impact.
- **Surface Tints:** Use #1A1A1A for elevated containers to maintain a subtle distinction from the background without breaking the dark immersion.

## Typography
The typographic hierarchy creates a tension between traditional luxury and modern performance. 

**Noto Serif** is used for headlines to convey a sense of heritage, authority, and "editorial" quality. Large display sizes should use a lighter weight to appear more elegant. 

**Manrope** provides a crisp, balanced counterpoint for all functional UI elements, body copy, and data points. Use `label-caps` for section headers and small metadata to echo the typography found on precision instruments and luxury watches.

## Layout & Spacing
The layout philosophy centers on a **fixed grid** with exceptionally generous whitespace. This "breathing room" is a hallmark of luxury, signaling that the interface is not crowded or rushed.

A 12-column grid is used for desktop layouts, with large external margins (80px+) to center the content as a focal point. Vertical spacing between major sections should be expansive (120px+) to allow the high-contrast photography to occupy its own visual plane. Use a 8px base unit for all component-level padding and alignment.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and layering rather than traditional shadows. 

1.  **Backdrop Blurs:** Use a 20px-30px Gaussian blur on semi-transparent Onyx Black layers (40-60% opacity). This creates a "frosted" look that allows car imagery to bleed through softly.
2.  **Thin Borders:** Instead of shadows, use 1px "Metallic Silver" borders at 20% opacity to define the edges of cards and containers.
3.  **Z-Axis:** Reserve the highest elevation for the "Concierge" chat or booking flow overlays, which should feature a more pronounced glass effect and a very subtle, diffused Electric Blue glow (#0033FF at 10% opacity) to signify focus.

## Shapes
The shape language is "Soft" (Level 1) to maintain a precise, architectural feel. While fully sharp corners can feel too aggressive, overly rounded corners feel too "tech-startup." 

A consistent 0.25rem (4px) base radius provides just enough refinement to the corners of buttons and input fields, echoing the tight tolerances of high-performance automotive bodywork. Large image containers may use up to 0.75rem (rounded-xl) to slightly soften the high-contrast photography.

## Components
- **Buttons:** Primary buttons use a solid Electric Blue fill with white or silver text. Secondary buttons are "Ghost" style with 1px Silver borders. All buttons feature a subtle transition to a slightly wider letter-spacing on hover.
- **Cards:** Utilize the Glassmorphism style. Background is a blur of the car imagery behind it, with a 1px Silver stroke. Content within cards is heavily inset with generous padding.
- **Inputs:** Minimalist bottom-border only or very thin 4-sided borders. Labels use the `label-caps` style positioned above the field.
- **Chips:** Used for car features (e.g., "V12", "Convertible"). These should be dark grey with silver text and no fill, just a thin border.
- **Concierge Widget:** A persistent, high-blur glass element. It should feel like a premium hardware button, using a subtle gradient of Metallic Silver.
- **Progress Indicators:** Linear, thin Electric Blue lines. Avoid thick or circular loaders; use "shimmer" effects on silver gradients to indicate loading states.