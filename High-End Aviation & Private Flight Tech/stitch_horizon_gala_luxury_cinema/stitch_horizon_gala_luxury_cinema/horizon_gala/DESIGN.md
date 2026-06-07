---
name: Horizon-Gala
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#dac1bf'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#a28c8a'
  outline-variant: '#544341'
  surface-tint: '#ffb3ad'
  primary: '#ffb3ad'
  on-primary: '#5a1a19'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#954742'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#bbcbbd'
  on-tertiary: '#26342a'
  tertiary-container: '#1a271e'
  on-tertiary-container: '#808f83'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#d7e7d8'
  tertiary-fixed-dim: '#bbcbbd'
  on-tertiary-fixed: '#111e16'
  on-tertiary-fixed-variant: '#3c4a40'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Bodoni Moda
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
  headline-lg-mobile:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  title-lg:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: 0.01em
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
  label-lg:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.08em
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 64px
  margin-tablet: 40px
  margin-mobile: 20px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for a premier, front-row cinema experience at 30,000 feet. It targets a discerning audience that expects the tactile luxury of a private screening room combined with the seamless functionality of modern technology. The emotional response is one of exclusive sanctuary—calm, prestigious, and deeply immersive.

The aesthetic blends **Glassmorphism** with **Minimalist Luxury**. We utilize ultra-soft background blurs and translucent layers to maintain a sense of physical depth without clutter. High-contrast elements ensure legibility on 8K displays, while the interaction model relies on "Golden Path" highlights—using gold accents to guide the user through the interface like a spotlight in a darkened theater.

## Colors

The palette is rooted in the "Cinema Dark" philosophy. The default mode is strictly dark to preserve the cabin's light environment and maximize the vibrancy of 4K/8K media content.

- **Deep Burgundy (#4A0E0E):** Used sparingly for primary brand moments and deep-depth backgrounds. It evokes the feeling of velvet theater curtains.
- **Antique Gold (#D4AF37):** Reserved exclusively for interactive states, progress indicators, and premium call-outs. It acts as the "light" within the dark.
- **Smoke (#738276 / #2C2C2C):** Used for secondary text and structural borders. The lighter smoke (#738276) provides a sophisticated mist-like quality for inactive icons.
- **Surface Foundations:** Backgrounds use a near-black (#0A0A0A). Surfaces utilize a custom semi-transparent smoke (#2C2C2C at 60% opacity) to achieve the glassmorphic effect.

## Typography

This design system employs a high-contrast typographic pairing to reflect its cinematic heritage. 

**Bodoni Moda** is used for all headlines and display text, providing a fashion-forward, editorial look that feels like a film title card. **Manrope** handles the bulk of the UI's functional text, offering a neutral, balanced, and highly legible sans-serif for content descriptions. **Hanken Grotesk** is used for utility labels and navigation items, where its sharp, contemporary character aids in quick recognition. 

Letter spacing is intentionally increased on labels to enhance the premium, "spaced-out" aesthetic of luxury branding.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid** grid. On large 4K/8K displays, content is centered within a 1440px container to prevent eye strain, while the smoke-gradient backgrounds bleed to the edges of the screen.

A strict 8px spacing scale governs all internal margins. We utilize generous whitespace (64px margins on desktop) to ensure the interface feels "airy" and expensive. 

**Breakpoints:**
- **Mobile (<600px):** 4-column grid, 20px margins. Headlines scale down to mobile variants.
- **Tablet (600px - 1024px):** 8-column grid, 40px margins.
- **Desktop (>1024px):** 12-column grid, 64px margins. Content is capped at 1440px for optimal cinema viewing ergonomics.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and **Soft Smoke-like Gradients**. Rather than traditional drop shadows, we use:

1.  **Backdrop Blurs:** Every floating panel (cards, menus) uses a 20px - 40px background blur with a subtle 1px border in Smoke (#738276 at 20% opacity).
2.  **Tonal Stacking:** Surfaces closer to the user are lighter and more transparent, while the background remains a deep, opaque Burgundy-Black.
3.  **Gradients:** Radial gradients are used in the corners of the screen to draw the eye toward the center, mimicking the vignetting of a high-end cinema projector.
4.  **Active Depth:** When a component is focused or active, it receives a soft, inner Antique Gold glow rather than a shadow, making it appear "backlit."

## Shapes

The design system uses **Soft (0.25rem)** roundedness for standard interface elements like buttons and input fields. This subtle rounding provides a modern touch while maintaining the sharp, architectural precision associated with luxury brands. 

For larger elements like movie posters or featured content cards, we use `rounded-lg` (0.5rem) to soften the immersion. Circular treatments are reserved exclusively for profile avatars and play/pause controls to distinguish them from structural UI.

## Components

### Buttons & Controls
- **Primary Action:** Solid Deep Burgundy with Antique Gold text. On hover, the button gains a subtle outer glow of Gold.
- **Ghost Buttons:** 1px Smoke border with Manrope Semi-Bold text. 
- **Cinema Play Button:** A large, circular Gold button with a Smoke-Black play icon, featuring a pulsating ambient gold ring.

### Cards
- **Media Cards:** No visible borders. Content relies on high-quality 8K imagery. Information overlays appear on hover using a glassmorphic bottom-aligned sheet.
- **System Cards:** Translucent smoke backgrounds with a 1px top-light border to catch the "ceiling light" of the interface.

### Input Fields
- Underlined style rather than boxed, using a 1px Smoke line. The line turns Antique Gold and thickens to 2px when focused. Labels use Hanken Grotesk in uppercase.

### Navigation
- **The Spotlight Rail:** A vertical navigation bar on the left with a subtle smoke gradient. The active icon is highlighted with an Antique Gold dot and a slight increase in opacity.

### Interactive States
- All interactive elements must transition using a soft ease-in-out (300ms). The use of Antique Gold should be strictly limited to the currently focused element to maintain the "Cinema environment" focus.