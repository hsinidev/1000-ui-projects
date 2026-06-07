---
name: Optical Minimalism
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#414754'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc0'
  primary: '#0059bb'
  on-primary: '#ffffff'
  primary-container: '#0070ea'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc7ff'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#646464'
  tertiary: '#9e3d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#c64f00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb695'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 32px
  gutter: 20px
---

## Brand & Style

This design system centers on the concept of "Digital Optics"—mimicking the clarity and precision of high-end microscopy through a user interface. The brand personality is clinical, ultra-precise, and transparent. It is designed for pathologists and laboratory technicians who require a zero-distraction environment to focus on high-resolution imaging.

The design style blends **Minimalism** with a refined **Glassmorphism**. It utilizes the "lens" as a primary metaphor: interface elements should feel like precision-ground glass overlays sitting atop raw data. By combining generous whitespace with high-tech, translucent layers, the system achieves a sterile yet sophisticated laboratory feel that prioritizes data integrity over decorative flair.

## Colors

The palette is strictly limited to ensure optical clarity. **Pure White (#FFFFFF)** serves as the primary canvas, representing the sterile laboratory environment. **Crystal Blue (#007BFF)** is used sparingly for interactive states, highlighting critical specimen data, and as a translucent tint for glass layers. **Black (#000000)** provides the necessary contrast for text and hairline borders, ensuring maximum legibility.

Secondary neutrals focus on cool greys and "Air" whites to distinguish between surface levels without introducing warmth. Transparency is a functional color here; "Crystal Blue" should often be applied at 10-15% opacity for background blurs to maintain the optical glass effect.

## Typography

The design system utilizes **Inter** for its neutral, systematic, and utilitarian qualities. In a clinical pathology context, legibility is paramount; Inter’s tall x-height and open counters ensure that microscopic data values and labels remain readable at small sizes.

Headlines should be set with tight tracking to feel "engineered," while labels utilize slightly increased letter spacing and uppercase styling to denote technical metadata. Typography is almost exclusively Black or High-Contrast Grey, reserving Blue only for interactive links or critical status indicators.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** within flexible containers. The workspace is divided into "Viewports" (for the microscopy scan) and "Panels" (for data and tools). A 12-column system is used for dashboard views, while the primary pathology viewer uses a "HUD" (Heads-Up Display) layout where menus float as glass overlays.

Generous whitespace is mandatory to prevent cognitive overload. Spacing follows a 4px baseline grid, with internal component padding usually defaulting to 16px (md) or 24px (lg) to maintain an airy, high-end feel. Use margin-heavy layouts to separate specimen imagery from UI controls.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and subtle **Ambient Shadows**. Instead of heavy dropshadows, this design system uses high-refraction backdrop blurs (20px to 40px) to simulate light passing through glass lenses.

1.  **Base Layer:** Pure White, flat.
2.  **Surface Layer:** Subtle 1px "Crystal Blue" border at 10% opacity.
3.  **Overlay Layer (Glass):** White background at 70% opacity with a 30px backdrop blur and a crisp 1px Black border at 5% opacity.
4.  **Interactive Layer:** Low-offset, highly diffused shadows (e.g., 0px 10px 30px rgba(0,0,0,0.05)) to suggest a slight lift from the surface.

Crisp borders are essential—every elevated element must have a defined, hairline edge to maintain the "precision instrument" aesthetic.

## Shapes

The shape language is **Soft** but disciplined. A default border radius of 0.25rem (4px) is used for most technical elements like input fields and specimen thumbnails, providing a clean, architectural look. 

Larger containers and overlay cards may use `rounded-lg` (0.5rem) to soften the clinical feel slightly without becoming "playful." Pill shapes are reserved strictly for status tags (e.g., "In Review," "Diagnostic") to distinguish them from functional buttons.

## Components

-   **Buttons:** Primary buttons are Solid Black with White text for maximum authority. Secondary buttons use a "Glass" style: White 80% opacity, 1px grey border, and Black text. No heavy gradients.
-   **Input Fields:** Ghost-style inputs with a 1px Black border at 15% opacity. On focus, the border turns Crystal Blue with a subtle blue outer glow (3px).
-   **Overlay Menus:** These are the centerpiece of the system. Use high-blur glass (80% opacity white) with hairline borders. Content inside should be strictly aligned to a internal 8px grid.
-   **Specimen Cards:** Minimalist frames with zero shadows. Information is categorized using "label-sm" typography. The card itself should feel like a glass slide.
-   **Checkboxes & Radios:** Sharp, high-contrast squares and circles. When active, they fill with Crystal Blue and use a white checkmark/dot.
-   **Microscopy HUD:** Floating toolbars that appear on hover. They utilize a darker "Smoked Glass" variant (Black at 60% opacity with blur) for high-contrast visibility over light tissue samples.