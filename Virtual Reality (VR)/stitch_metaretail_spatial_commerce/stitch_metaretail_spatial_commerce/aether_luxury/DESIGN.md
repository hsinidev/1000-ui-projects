---
name: Aether Luxury
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#524345'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#857374'
  outline-variant: '#d7c1c3'
  surface-tint: '#8c4b55'
  primary: '#8a4853'
  on-primary: '#ffffff'
  primary-container: '#a6606b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
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
  margin-edge: 48px
  section-gap: 120px
---

## Brand & Style

This design system is engineered for the intersection of haute couture and augmented reality. The personality is "Quiet Luxury Tech"—an atmosphere that prioritizes breathing room, material honesty, and spatial depth. It targets a discerning clientele that expects the tactility of a physical boutique within a digital medium.

The visual style merges **Minimalism** with **Glassmorphism**. By utilizing semi-transparent surfaces and blurred backdrops, the UI feels like a layer of light floating over the real world (or high-resolution product photography). The "Rose Gold" is treated not just as a color, but as a light source, creating soft-glow effects that guide the eye toward primary actions and high-value items.

## Colors

The palette is anchored by **Deep Charcoal** (#121212) for grounding elements and **White** (#FFFFFF) for expansive, airy backgrounds. **Rose Gold** (#B76E79) serves as the primary brand signifier, used for interactive states, key call-to-actions, and subtle atmospheric glows.

- **Primary:** Rose Gold. Used for selection states, primary buttons, and price highlights.
- **Secondary:** Deep Charcoal. Used for heavy typography, navigation bars, and high-contrast iconography.
- **Surface:** White and Off-White. Used to maintain a clean, editorial feel.
- **Glow:** A semi-transparent Rose Gold is used for `box-shadow` and `filter: drop-shadow` to simulate light emission in AR environments.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage and innovation.

- **Headlines:** `Noto Serif` provides a literary, authoritative, and premium feel. It should be used for product names, editorial titles, and collection headers. Keep weights light (300) to maintain elegance.
- **Body & UI:** `Manrope` provides a refined, balanced sans-serif foundation. It is chosen for its geometric clarity and excellent readability in technical contexts (AR overlays, spec sheets).
- **Labels:** Small caps with generous letter spacing are used for category tags and secondary metadata to evoke luxury fashion labeling.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach for web experiences and a **Safe-Zone Margin** approach for AR views. 

- **The Grid:** A 12-column grid with wide 24px gutters ensures that content never feels crowded. 
- **Rhythm:** We use a generous vertical rhythm. Section gaps are intentionally large (120px+) to allow the eye to rest and to emphasize the "Spatial" nature of the product.
- **AR Margins:** For head-mounted or mobile AR views, maintain a 48px safety margin from all edges to avoid peripheral distortion.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Soft-Glow** layering rather than traditional drop shadows.

- **Base Layer:** Solid White or photographic environment.
- **Mid Layer (Cards/Modals):** A frosted glass effect (`backdrop-filter: blur(20px)`) with a 1px solid white border at 20% opacity.
- **Top Layer (Interactive):** Elements that are hovered or active emit a soft Rose Gold glow (`box-shadow: 0 0 30px rgba(183, 110, 121, 0.2)`).
- **Z-Axis:** In AR mode, higher-elevation items should physically scale slightly toward the user to indicate focus.

## Shapes

The shape language is **Soft**. We avoid sharp, aggressive corners to maintain a "couture" feel, but we also avoid pill-shapes which can feel too casual or "bubbly."

- **Standard Radius:** 4px (0.25rem) for input fields and small UI elements.
- **Large Radius:** 8px (0.5rem) for product cards and primary modals.
- **Buttons:** Rectangular with a 4px soft radius to maintain a formal, structured appearance.

## Components

- **Buttons:** Primary buttons use a Deep Charcoal background with Rose Gold text and a subtle 1px Rose Gold border. Secondary buttons are transparent glass with a 1px white border.
- **Cards:** Product cards must be borderless with a subtle white-to-transparent gradient background. On hover, the image should slightly scale, and the Rose Gold glow should appear behind the price label.
- **Inputs:** Underlined or minimally framed fields. Use `Manrope` 14px for placeholder text. The focus state should change the underline to Rose Gold with a faint glow.
- **AR Reticle:** A thin, circular Rose Gold element that pulse-animates when hovering over a physical object.
- **Chips:** Used for sizing or color selection. They should be transparent with a white border, filling with Deep Charcoal when selected.
- **Spatial Breadcrumbs:** Minimalist text links separated by thin vertical lines (|) to help users navigate complex AR product configurations.