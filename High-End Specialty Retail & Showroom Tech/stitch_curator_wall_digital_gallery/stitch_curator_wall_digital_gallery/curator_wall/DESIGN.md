---
name: Curator-Wall
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#353434'
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
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c9c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#050505'
  on-tertiary-container: '#797777'
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
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 32px
  margin-desktop: 80px
  margin-tablet: 40px
  margin-mobile: 20px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of a silent, high-end gallery located in a futuristic metropolis. It prioritizes the artwork above all else, using a "Void" philosophy where the interface recedes into the background until needed.

The aesthetic combines **Minimalism** with **Glassmorphism**. The primary goal is to create a sense of digital "prestige" through the use of expansive whitespace (breathability), razor-sharp edges, and atmospheric depth. The mood is cinematic, intellectual, and exclusive, catering to serious collectors and digital artists who value curation over clutter. High-contrast interactions and thin metallic accents ground the ethereal glass elements, providing a structural framework that feels both architectural and ethereal.

## Colors

The palette is anchored by **Deep Space Black**, which serves as the infinite canvas. This total-darkness approach eliminates visual noise and allows the colors within the artwork to vibrate. 

**Metallic Silver** is used strictly for structural integrity—thin borders, iconography, and secondary labels—mimicking the physical hardware of a gallery. 

Interactive highlights utilize a dual-accent strategy:
- **Electric Blue** is used for primary actions, navigation states, and "Live" indicators, suggesting high-tech precision.
- **Neon Purple** is reserved for rare collectibles, special exhibitions, and premium loyalty features.

Transparency is a functional color state in this design system, using low-opacity whites to create the "glass" surfaces that sit atop the black void.

## Typography

The typography strategy relies on a dramatic contrast between the "Heritage" of the serif and the "Utility" of the sans-serif.

**Playfair Display** is the voice of the gallery. It is used for exhibition titles, artist names, and high-level editorial headers. At large scales, it evokes the classic sophistication of printed art catalogs.

**Inter** provides the functional layer. It is used for descriptions, metadata (medium, dimensions, year), and navigation. To maintain the premium feel, labels and metadata should often utilize wide letter-spacing and uppercase styling, resembling the small brass plaques found next to physical paintings. 

Font hierarchy should be aggressive; small text should be very small but legible, and large text should be dominant, creating a rhythmic cadence throughout the scroll.

## Layout & Spacing

This design system employs a **Fixed Grid** model for content alignment but allows for "Artistic Bleed" where imagery may break the grid to touch the edges of the viewport.

The desktop layout uses a 12-column grid with generous 32px gutters. Breathability is achieved through significant vertical margins (80px+), ensuring that no two artworks feel crowded. 

**Reflow Rules:**
- **Desktop:** Asymmetric layouts are encouraged (e.g., artwork on columns 1-7, text on columns 9-11).
- **Tablet:** 8-column grid. Imagery moves to a more structured, stacked appearance.
- **Mobile:** 4-column grid. Margins compress to 20px, and large display type scales down to ensure legibility while maintaining the high-contrast serif presence.

## Elevation & Depth

Depth is not communicated through traditional shadows, but through **light refraction and translucency**.

1.  **The Floor (Base):** #050505. Pure black, zero light.
2.  **The Glass (Floating Surfaces):** Using `backdrop-filter: blur(20px)` and a 0.5px silver border. These surfaces appear to float at varying "heights" based on their blur intensity.
3.  **The Glow (Interactive):** When an element is active, it emits a subtle outer glow using the Electric Blue or Neon Purple colors (blur: 15px, opacity: 0.2).

Borders must remain extremely thin (hairline) to maintain a technical, futuristic precision. Thick borders are prohibited.

## Shapes

The design system utilizes **Sharp (0px)** corners for all primary containers, image frames, and structural layout blocks. This reinforces the "architectural" feel of a high-end gallery and mimics the sharp edges of a physical picture frame.

Minor interactive elements—such as utility chips or notification badges—may use a slight softening (2px) to differentiate them from the "Art," but for the core experience, 90-degree angles are the standard. This rigidity emphasizes the precision of the digital medium.

## Components

**Buttons**
Primary buttons are ghost-style with a thin silver border. On hover, they transition to a solid fill of Electric Blue with black text, or trigger a "Glass-Glow" effect. 

**Cards (Art Frames)**
Art cards have no background color by default. They consist of the high-res image and a hairline silver bottom border. Upon hovering, a glassmorphic overlay appears with the artist's metadata.

**Inputs**
Fields are represented by a single silver bottom-border (0.5px). The label sits above in Inter (Uppercase, 10px). On focus, the border transitions to Electric Blue.

**Navigation**
The top navigation bar is a persistent glassmorphic strip with a blur effect that reveals hints of the art passing beneath it.

**Status Chips**
Used for "Sold," "Reserved," or "Auction Live." These are sharp-edged boxes with a 1px border. "Auction Live" should pulse subtly with the Neon Purple accent.

**Imagery**
All imagery should be presented with `object-fit: cover`. Where possible, include a subtle grain overlay on images to enhance the "moody" texture of the gallery.