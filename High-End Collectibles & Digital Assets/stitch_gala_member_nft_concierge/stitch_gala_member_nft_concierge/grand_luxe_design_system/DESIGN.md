---
name: Grand-Luxe Design System
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#cfc2d5'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#988d9e'
  outline-variant: '#4d4353'
  surface-tint: '#dfb7ff'
  primary: '#dfb7ff'
  on-primary: '#4b007e'
  primary-container: '#6a0dad'
  on-primary-container: '#d4a1ff'
  inverse-primary: '#8333c6'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c3c6d7'
  on-tertiary: '#2c303d'
  tertiary-container: '#434755'
  on-tertiary-container: '#b2b5c6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f1daff'
  primary-fixed-dim: '#dfb7ff'
  on-primary-fixed: '#2d004f'
  on-primary-fixed-variant: '#690bac'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#dfe2f3'
  tertiary-fixed-dim: '#c3c6d7'
  on-tertiary-fixed: '#171b28'
  on-tertiary-fixed-variant: '#434654'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 42px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  interactive:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-margin-mobile: 20px
  container-margin-desktop: 64px
  gutter: 24px
  section-gap: 80px
---

## Brand & Style
This design system embodies an aesthetic of "Modern Sovereign"—a fusion of classical luxury and digital-first immersion. It is designed for high-end experiences where exclusivity and prestige are paramount. The personality is authoritative, mysterious, and unapologetically premium.

The style leverages **Glassmorphism** and **High-Contrast Bold** movements. Deep, layered backgrounds create a sense of infinite digital space, while vibrant purple and gold elements act as beacons of interaction. The user should feel as though they are interacting with a high-end physical concierge or a private club. Visual weight is used strategically to guide the eye toward "Premium" actions, using luminescence rather than just flat color to signify importance.

## Colors
The palette is rooted in deep shadow to allow accent colors to vibrate with intensity.

*   **Midnight Blue (#0A0E1A):** The foundation. Used for all primary backgrounds to create depth.
*   **Royal Purple (#6A0DAD):** The interactive engine. Used for primary buttons, active states, and progress indicators.
*   **Metallic Gold (#D4AF37):** The signature of quality. Used for borders, iconography, and "Premium" badges. 
*   **Surface Tones:** Use semi-transparent variants of Midnight Blue (e.g., `#161B2C`) for cards to create a "glass" effect against the base background.
*   **Active Glows:** Interactive elements utilize CSS `box-shadow` or `filter: drop-shadow` using the primary purple or gold at 40-60% opacity to simulate light emission.

## Typography
The typography strategy creates a tension between the traditional elegance of **Playfair Display** and the modern precision of **Inter**. 

*   **Headlines:** Always use Playfair Display. For top-tier headings, use `text-shadow` sparingly to create a "etched in gold" effect when the text color is set to Gold.
*   **UI & Body:** Inter provides the necessary legibility for functional data and controls. 
*   **Hierarchy:** Use the `label-caps` style for small meta-info or "Overline" text above headlines to establish a structured, editorial feel. 
*   **Color Application:** Headlines should default to Gold or White; body text should remain high-contrast (Off-white or Light Grey) for readability against the dark background.

## Layout & Spacing
This design system utilizes a **Fluid Grid** with generous breathing room to reinforce the feeling of "Luxury." 

*   **Mobile-First:** Start with a single-column layout with 20px side margins. Elements should be padded internally with at least 16px to ensure touch targets are comfortable.
*   **Desktop:** Transition to a 12-column grid. Max content width is 1280px.
*   **Rhythm:** Use an 8px base unit. Section spacing is intentionally large (80px+) to prevent the UI from feeling cluttered, which is a hallmark of premium design.
*   **Negative Space:** Avoid filling every corner of the screen. Allow the Midnight Blue background to dominate, serving as a canvas that makes the Purple and Gold elements "pop."

## Elevation & Depth
Depth is achieved through **Luminescence and Layering** rather than traditional grey shadows.

1.  **Level 0 (Base):** Midnight Blue (#0A0E1A).
2.  **Level 1 (Cards/Plates):** A slightly lighter navy (#161B2C) with a subtle 1px border of Gold at 20% opacity.
3.  **Level 2 (Modals/Popovers):** Surface color with a "Glass" effect (Backdrop-filter: blur(12px)) and a 1px solid Gold border.
4.  **Active Elevation:** When an element is focused or active, apply a Royal Purple outer glow (box-shadow: 0 0 15px rgba(106, 13, 173, 0.6)). This creates a "light-up" effect similar to high-end hardware.

## Shapes
The shape language is **Sophisticated and Rectilinear**. 

*   **Corners:** We use a "Soft" (4px) corner radius for most UI elements (buttons, inputs). This maintains a crisp, architectural feel while avoiding the harshness of 0px sharp corners.
*   **Large Surfaces:** Cards and containers use `rounded-lg` (8px) to feel substantial.
*   **Icons:** Use gold-tinted strokes with a consistent 2px weight. Icons should be housed in a square or circular container with a very subtle purple radial gradient background.

## Components
*   **Buttons:** Primary buttons are Royal Purple with white text. On hover, they emit a purple glow. Secondary buttons are transparent with a 1px Gold border and Gold text.
*   **Premium Badges:** Small, pill-shaped elements with a Gold background and Midnight Blue text. They must feature a subtle CSS animation (a "shimmer") to denote high value.
*   **Inputs:** Dark backgrounds (#05070D) with 1px borders. On focus, the border turns Gold and the text-cursor glows.
*   **Lists:** Separated by thin, 1px lines of Midnight Blue (lighter shade) or subtle Gold dividers.
*   **Icons:** Always tinted Gold (#D4AF37). Use a CSS `filter: drop-shadow(0 0 2px rgba(212, 175, 55, 0.5))` to give them a metallic luster.
*   **Progress Bars:** The track is the background color; the fill is a gradient from Royal Purple to a lighter Magenta-Purple, with a "glow" head.