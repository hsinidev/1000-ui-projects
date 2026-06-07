---
name: Luxe Tactility
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c0c9c2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8a938d'
  outline-variant: '#414944'
  surface-tint: '#a0d1b8'
  primary: '#a0d1b8'
  on-primary: '#033826'
  primary-container: '#043927'
  on-primary-container: '#73a48c'
  inverse-primary: '#396752'
  secondary: '#ffb3b5'
  on-secondary: '#680018'
  secondary-container: '#8e0f28'
  on-secondary-container: '#ff989d'
  tertiary: '#e9c349'
  on-tertiary: '#3c2f00'
  tertiary-container: '#cba72f'
  on-tertiary-container: '#4e3d00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#bbeed3'
  primary-fixed-dim: '#a0d1b8'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#204f3c'
  secondary-fixed: '#ffdada'
  secondary-fixed-dim: '#ffb3b5'
  on-secondary-fixed: '#40000b'
  on-secondary-fixed-variant: '#8e0f28'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '600'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '500'
    lineHeight: 56px
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1440px
  gutter: 32px
---

## Brand & Style

This design system is built for an audience that values artisanal craftsmanship and sensory indulgence. The brand personality is sophisticated, intimate, and authoritative, positioning the product as a master of bespoke comfort. 

The visual style is a fusion of **Neomorphism** and **High-End Tactility**. Unlike traditional flat neumorphism, this design system uses soft-UI principles to mimic the physical depression and loft of upholstered fabric. The interface should feel "plush"—buttons should look like they are pressed into velvet, and cards should appear to rise gently from the surface like a cushioned seat. High-quality video storytelling and macro-photography of textures are central to the experience, creating an atmosphere of quiet luxury.

## Colors

The palette is anchored in deep, jewel-toned saturation to evoke the feeling of a private atelier at dusk. Emerald Green (#043927) serves as the primary surface color, providing a rich, immersive foundation. Deep Burgundy (#800020) is used sparingly for high-intent actions and accentuation, adding warmth and drama. Brass (#D4AF37) acts as the metallic highlight, used for trim, icons, and subtle borders to signify premium quality.

To achieve the "Velvet" effect, the primary color is never flat. It is used in conjunction with subtle radial gradients (moving from a slightly lighter emerald center to the darker #043927 edges) to simulate light catching the grain of the fabric.

## Typography

Typography in this design system balances traditional elegance with contemporary clarity. **Noto Serif** is used for all editorial and navigational headings. Its refined serifs and classic proportions lend an air of heritage and "slow-fashion" craftsmanship. 

**Manrope** is used for body copy and functional labels. Its geometric but slightly softened terminals complement the neumorphic UI elements without competing for attention. Headlines should use "display-lg" for hero sections to create a high-impact editorial feel, while small labels use "label-caps" with wide tracking to evoke luxury garment tagging.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to maintain a curated, boutique-like presentation. The layout is centered around a 12-column grid with generous 32px gutters, ensuring that content never feels crowded. 

Whitespace is treated as a luxury material. Significant vertical padding ("xl") is used between sections to allow the rich color palette and video content to breathe. Spacing follows an 8px rhythmic scale, ensuring that the soft-UI shadows have enough room to diffuse naturally without overlapping adjacent elements.

## Elevation & Depth

Depth is the defining characteristic of this design system. We use a **Tactile Neumorphic** approach to create three-dimensional hierarchy. 

Elements do not "float" with traditional drop shadows; instead, they are formed by the surface itself. 
- **Raised Elements:** Created using two shadows: a "light" shadow (a softer, lighter shade of Emerald) on the top-left and a "dark" shadow (deep black or near-black emerald) on the bottom-right.
- **Sunken Elements (In-set):** Used for input fields and fabric swatch containers. These use internal shadows to look like they have been pressed into the velvet.
- **Gradients:** Surfaces use 145-degree linear gradients that move from a highlight color to a shadow color to reinforce the 3D volume.

## Shapes

The shape language is purposefully **Rounded**. Sharp corners are avoided to maintain the "soft-touch" aesthetic. Standard UI containers use a 0.5rem radius, while large feature cards and hero images use a 1.5rem radius to suggest the plush corners of a premium sofa. 

Interactive elements like fabric swatches are circular or have high-radius pill shapes to invite touch and interaction. Brass-colored accents (dividers or borders) are kept extremely thin—1px—to look like delicate metallic inlays.

## Components

### Buttons
Primary buttons use the "Raised" neumorphic style with a subtle Brass (#D4AF37) border. On hover, the internal gradient shifts to simulate the fabric being compressed. Text within buttons is always Manrope Medium to ensure legibility against the textured background.

### Interactive Fabric Swatches
Swatches are presented in "Sunken" circular containers. When selected, the swatch "rises" using the raised neumorphic effect and gains a thin Brass ring. High-resolution video hover states should be used to show the fabric's movement and sheen.

### Multi-Step Forms
To simplify the bespoke ordering process, forms are broken into distinct tactile cards. A progress bar made of thin Brass lines indicates movement. Input fields use the "In-set" (sunken) shadow style, making the user feel like they are "carving" their preferences into the interface.

### Cards
Cards are the primary container for product storytelling. They feature a soft outer glow rather than a harsh shadow, making them appear as though they are softly resting on a velvet surface. They frequently include integrated video backgrounds with a low-opacity Emerald overlay to ensure text contrast.