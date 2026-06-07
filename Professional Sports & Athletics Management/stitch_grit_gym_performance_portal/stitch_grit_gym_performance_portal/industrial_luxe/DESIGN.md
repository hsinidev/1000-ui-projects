---
name: Industrial Luxe
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
  on-surface-variant: '#d1c5b4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9a8f80'
  outline-variant: '#4e4639'
  surface-tint: '#e9c176'
  primary: '#e9c176'
  on-primary: '#412d00'
  primary-container: '#c5a059'
  on-primary-container: '#4e3700'
  inverse-primary: '#775a19'
  secondary: '#c7c6c6'
  on-secondary: '#2f3031'
  secondary-container: '#464747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#a7a5a5'
  on-tertiary-container: '#3b3b3b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdea5'
  primary-fixed-dim: '#e9c176'
  on-primary-fixed: '#261900'
  on-primary-fixed-variant: '#5d4201'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 80px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
  data-viz:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
spacing:
  base: 8px
  container-max: 1440px
  gutter: 32px
  margin-mobile: 24px
  margin-desktop: 64px
  section-gap: 128px
---

## Brand & Style

The design system embodies "Industrial Luxe," a fusion of raw, structural power and sophisticated refinement. It targets an elite tier of high-performance athletes who value exclusivity, discipline, and precision. The UI must evoke a sense of architectural strength and "grit" through textures while maintaining a premium, frictionless user experience.

The visual style is **High-Contrast / Bold**, utilizing sharp edges and expansive whitespace to create a gallery-like atmosphere. It borrows elements of **Glassmorphism** for functional overlays to simulate high-end materials like frosted glass and polished metal, ensuring the interface feels like an extension of a luxury physical space.

## Colors

The palette is rooted in a monochromatic industrial base with metallic highlights. 

*   **Deep Black (#0A0A0A):** The primary canvas, providing a dramatic, void-like backdrop that emphasizes high-performance imagery.
*   **Brushed Brass (#C5A059):** Used sparingly for critical CTAs, active states, and accents to signify prestige and value.
*   **Exposed Concrete (#8E8E8E):** A textured neutral used for secondary text and borders, bridging the gap between black and white.
*   **Structural Slate (#1A1A1A):** Used for container backgrounds and surfaces to create depth without losing the dark aesthetic.

## Typography

This design system utilizes **Space Grotesk** for all headlines and labels to reinforce a technical, architectural character. Headings should be set with tight letter-spacing to feel compact and powerful. 

**Inter** is utilized for body copy to ensure maximum legibility against dark backgrounds. For specialized data readouts (heart rate, power output, duration), use Space Grotesk to maintain the high-performance, instrument-cluster aesthetic.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to maintain a curated, editorial feel. A 12-column grid is used with generous 32px gutters.

The spacing rhythm is intentional and expansive. Heavy use of "Macro-whitespace" (128px+ section gaps) is required to separate different training modules or club features, mirroring the spaciousness of an ultra-luxury facility. Content should often be offset or asymmetrical to create visual tension and interest.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and **Glassmorphism** rather than traditional shadows.

1.  **Level 0 (Floor):** Deep Black (#0A0A0A) base.
2.  **Level 1 (Plinth):** Structural Slate (#1A1A1A) cards with 1px solid Concrete borders.
3.  **Level 2 (Float):** Glassmorphic overlays with a 20px backdrop-blur and 10% white tint, used for navigation bars and modal dialogues.
4.  **Accents:** Thin, 1px Brushed Brass "shimmer" borders on active elements to simulate metallic inlay.

## Shapes

The design system adheres to a **Sharp (0px)** corner radius across all components. This zero-radius approach reinforces the industrial, architectural narrative and conveys a sense of uncompromising precision. Any "softness" should come from the imagery and lighting, not the UI geometry.

## Components

### Buttons
Primary buttons are rectangular with a Brushed Brass background and Black text in all-caps Space Grotesk. Secondary buttons are "Ghost" style with a 1px brass border and no fill. Hover states should feature a subtle metallic gradient shift.

### Cards
Cards use the Structural Slate background. A distinctive feature is the "Brass Header" — a 2px horizontal line of Brushed Brass at the top of the card or a small brass corner-accent. 

### Glassmorphism Overlays
Used for "Quick Action" menus and filter bars. These elements must have a high-contrast 1px border (#FFFFFF @ 20%) to remain visible against dark backgrounds.

### Data Visualizations
Charts should utilize thin, high-precision lines. Use Brushed Brass for the primary data series and a desaturated Concrete Gray for grid lines. Avoid fills or gradients unless they are low-opacity brass glows.

### Inputs
Fields are bottom-border only (1px Concrete Gray), transforming to Brushed Brass on focus. Labels sit above the line in the "label-caps" typographic style.