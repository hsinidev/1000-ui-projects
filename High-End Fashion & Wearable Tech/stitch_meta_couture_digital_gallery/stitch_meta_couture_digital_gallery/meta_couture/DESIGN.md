---
name: Meta-Couture
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
  primary-container: '#050505'
  on-primary-container: '#797777'
  inverse-primary: '#5f5e5e'
  secondary: '#d3fbff'
  on-secondary: '#00363a'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#ffabf3'
  on-tertiary: '#5b005b'
  tertiary-container: '#100010'
  on-tertiary-container: '#d300d3'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#ffd7f5'
  tertiary-fixed-dim: '#ffabf3'
  on-tertiary-fixed: '#380038'
  on-tertiary-fixed-variant: '#810081'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Bodoni Moda
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  technical-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.2em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-padding: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
This design system embodies the intersection of digital haute couture and futuristic architecture. It is built for a target audience of digital collectors and metaverse residents who value exclusivity and avant-garde aesthetics. The visual language is defined by a "Digital Noir" atmosphere—deep, immersive blacks punctuated by ethereal, iridescent light. 

The style utilizes **Glassmorphism** and **High-Contrast** editorial layouts. Every interface element should feel like a holographic projection within a luxury physical space. The emotional response is one of awe, sophistication, and technical precision, ensuring that the 3D digital garments remain the undisputed focal point of the experience.

## Colors
The palette is rooted in **Obsidian Black**, providing a limitless void that allows the digital fabrics to glow. The primary interaction colors are iridescent—Cyan, Violet, and Magenta—used sparingly for high-value touchpoints and status indicators. 

The "Iridescent" gradient is the signature of the design system, mimicking the light-refraction properties of futuristic materials. Backgrounds should utilize the deep neutral for depth, while the primary black is reserved for the base canvas. Text is strictly white or high-contrast silver to maintain legibility against the dark void.

## Typography
The typographic strategy balances heritage luxury with technical specs. **Bodoni Moda** is used for all high-level headings, providing an editorial, "Vogue-esque" high-contrast serif look. 

For all technical data, metadata (like polygon counts or blockchain hashes), and UI labels, **JetBrains Mono** is utilized. This monospaced font reinforces the "digital-only" nature of the brand. Headings should be set with tight tracking, while monospaced labels should be generously spaced to enhance the futuristic, data-driven aesthetic.

## Layout & Spacing
This design system follows a **Mobile-First, Fluid Grid** philosophy. On mobile, a 4-column grid is used with 24px outer margins to provide a sense of luxury through whitespace. 

The layout is optimized for a 3D asset showcase. The "Hero" area is usually a full-height viewport for the garment, with UI elements floating as frosted glass overlays. Spacing follows an 8px rhythmic scale, but larger "editorial" gaps (48px+) are encouraged between sections to maintain the high-end boutique feel.

## Elevation & Depth
Depth is not communicated through traditional shadows, but through **Backdrop Blurs** and **Luminous Borders**. 

1.  **Base Layer:** Solid Obsidian Black (#050505).
2.  **Surface Layer:** Frosted Glass (20% opacity white) with a 20px backdrop blur.
3.  **Accent Layer:** Components at this level feature a 1px "Glowing Border" using the iridescent gradient.
4.  **Active Level:** Elements gain an outer neon glow (bloom effect) using a diffused box-shadow of the primary cyan or magenta at low opacity.

This stacking creates a sense of translucent layers floating in a dark, 3D space.

## Shapes
The shape language is "Architectural Minimalist." Elements use a **Soft (0.25rem)** corner radius to feel modern but structured. 

Avoid high-radius "pill" shapes for standard buttons or cards, as they appear too casual for an avant-garde luxury brand. Rectilinear forms with subtle rounding suggest precision and digital craftsmanship. The exception is the "Glow-Intensity" slider thumb, which should remain a sharp vertical line or a small diamond.

## Components
-   **Glassmorphism Cards:** Use as containers for product descriptions. They must have a 1px stroke (glass_stroke) and a 20px-32px backdrop blur.
-   **Luminous Buttons:** Primary buttons are ghost-style with an iridescent border. On hover or tap, the button fills with a semi-transparent cyan glow.
-   **Glow-Intensity Sliders:** Sleek, minimalist horizontal tracks with a neon-filled progress line. The slider thumb is a 2px wide vertical "needle" that glows when touched.
-   **3D Asset Showcase:** A dedicated component that fills 70% of the viewport. UI controls for rotation and zoom are placed in the bottom corners as floating, borderless icons.
-   **Technical Data Chips:** Monospaced text inside small, high-opacity black boxes with a sharp 1px border. Used for "Rarity," "Material," and "Mint Number."
-   **Navigation:** A bottom-fixed floating bar, utilizing heavy glassmorphism and haptic-feedback-driven icons.