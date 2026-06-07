---
name: Street-Luxe
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f8f5f5'
  on-tertiary: '#313030'
  tertiary-container: '#dcd9d8'
  on-tertiary-container: '#5f5e5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
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
    lineHeight: '1.5'
    letterSpacing: 0em
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  overlap-offset: -12px
---

## Brand & Style

This design system embodies the high-octane energy of sneaker culture, blending the raw, industrial grit of streetwear with the polished exclusivity of luxury fashion. The interface is designed to evoke a sense of speed, scarcity, and digital craftsmanship.

The visual direction utilizes a **High-Contrast / Bold** framework with elements of **Glassmorphism**. It relies on aggressive depth, where elements physically overlap to create a sense of "stacked" boxes—reminiscent of sneaker crates in a warehouse. The atmosphere is nocturnal, favoring deep blacks to make the "Electric Blue" accents appear as though they are self-illuminated light sources. The UI should feel like a high-end trading floor for the modern hypebeast: fast, data-driven, and visually arresting.

## Colors

The palette is anchored in a "Deep Black" foundation to maximize the luminosity of the "Electric Blue" primary color. 

- **Primary (Electric Blue):** Used for critical actions, interactive borders, and glowing accents. It represents the "energy" of the marketplace.
- **Base (Deep Black & Crisp White):** Black serves as the canvas, while White is reserved for high-contrast typography and primary "Luxe" surfaces.
- **Accents:** Neon blue glows are applied to active states and "hot" market items. High-contrast overlaps use a secondary gray (#1A1A1A) to separate stacked cards without losing the dark aesthetic.

## Typography

Typography is a dual-force system. **Space Grotesk** provides the "aggressive" energy required for headlines, featuring a technical, geometric construction that feels futuristic and sharp. Large-scale headings should use tight letter spacing to increase visual tension.

**Inter** is utilized for all functional data, market prices, and body copy. It ensures that complex market information (bid/ask prices, size charts, shipping data) remains perfectly legible at small sizes. Use the "Label-Mono" style for metadata like SKU numbers or timestamps to maintain the industrial, streetwear aesthetic.

## Layout & Spacing

The layout utilizes a **Fixed Grid** of 12 columns for desktop and a fluid single-column layout for mobile. 

The signature "Street-Luxe" look is achieved through **intentional overlapping**. Elements such as product images or "limited drop" badges should use the `overlap-offset` to break out of their parent containers. This creates a high-energy, collage-like feel. Padding should be generous within cards to maintain a premium feel, while the external spacing between cards remains tight (using the 8px base unit) to emphasize the fast-paced, dense nature of sneaker marketplaces.

## Elevation & Depth

Depth in this design system is not created with traditional soft shadows, but through **Tonal Layers** and **Neon Outlines**.

1.  **Level 0 (Surface):** The Deep Black background.
2.  **Level 1 (Card):** A dark charcoal (#0A0A0A) surface with a 1px solid border.
3.  **Level 2 (Interaction):** When hovered or active, cards gain an "Electric Blue" 1px border and a subtle outer glow (`box-shadow`) using the `accent_glow` variable.

Backdrop blurs (Glassmorphism) are reserved for sticky headers and modal overlays to maintain a sense of luxury and focus. The "overlapping" elements use sharp, high-contrast dividers instead of blurs to keep the "grit" of the streetwear influence.

## Shapes

The shape language is primarily **Soft (0.25rem)**. This provides a subtle nod to modern mobile hardware while maintaining the aggressive, sharp-edged feel of industrial design. 

Images should maintain a sharp `0` radius or a very small `rounded-sm` to keep the footwear photography looking crisp and unedited. Interactive elements like buttons and input fields use the standard `rounded-md` (0.5rem) to ensure they feel like touchable, modern components.

## Components

- **Buttons:** Primary buttons are solid "Electric Blue" with black text (Space Grotesk Bold). Secondary buttons are "Ghost" style: transparent background with a 2px "Electric Blue" border and white text.
- **Cards:** Cards are the core of the mobile experience. They feature a dark background, a 1px border, and "overlapping" price badges that sit on the top-right corner, breaking the container edge.
- **Market Labels:** Price changes (up/down) use "Electric Blue" for positive movement and a high-contrast white for neutral, avoiding traditional greens/reds to maintain the brand's specific color identity.
- **Input Fields:** Search bars and data inputs use a dark fill (#111111) and a bottom-only "Electric Blue" border that glows when focused.
- **Chips/Badges:** Use the "Label-Mono" typography. They are styled as small, rectangular "tags" with high-contrast borders, resembling price tags or shipping labels.
- **Price Ticker:** A continuous horizontal scroll component at the top of the viewport, featuring "Space Grotesk" labels for a high-speed trading floor effect.