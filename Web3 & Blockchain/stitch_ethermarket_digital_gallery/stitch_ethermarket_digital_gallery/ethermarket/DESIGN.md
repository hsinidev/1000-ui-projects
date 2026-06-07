---
name: EtherMarket
colors:
  surface: '#1e0a29'
  surface-dim: '#1e0a29'
  surface-bright: '#473151'
  surface-container-lowest: '#190523'
  surface-container-low: '#271332'
  surface-container: '#2c1736'
  surface-container-high: '#372241'
  surface-container-highest: '#422c4c'
  on-surface: '#f6d9ff'
  on-surface-variant: '#cec3d0'
  inverse-surface: '#f6d9ff'
  inverse-on-surface: '#3e2848'
  outline: '#978e9a'
  outline-variant: '#4b444f'
  surface-tint: '#e0b6ff'
  primary: '#e0b6ff'
  on-primary: '#441c65'
  primary-container: '#2e004f'
  on-primary-container: '#9d72c0'
  inverse-primary: '#754c97'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#cdcd00'
  on-tertiary: '#323200'
  tertiary-container: '#b1b100'
  on-tertiary-container: '#424200'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f2daff'
  primary-fixed-dim: '#e0b6ff'
  on-primary-fixed: '#2e004e'
  on-primary-fixed-variant: '#5c347d'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#eaea13'
  tertiary-fixed-dim: '#cdcd00'
  on-tertiary-fixed: '#1d1d00'
  on-tertiary-fixed-variant: '#494900'
  background: '#1e0a29'
  on-background: '#f6d9ff'
  surface-variant: '#422c4c'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  container-max: 1440px
  gutter: 32px
  margin-page: 64px
  section-gap: 128px
---

## Brand & Style
This design system is built for an elite digital environment, treating NFTs and digital assets not just as tokens, but as curated artifacts in a high-end virtual gallery. The personality is sophisticated, calm, and exclusive. 

The aesthetic leverages **Glassmorphism** as its primary structural driver, creating a sense of layered depth and futuristic lightness against a deep, infinite background. It balances the timeless elegance of gallery curation with the cutting-edge nature of blockchain technology. The user should feel like they are stepping into a private, high-contrast exhibition space where the interface recedes to let the digital assets take center stage.

## Colors
The palette is centered on a "Midnight Universe" foundation. The primary **Midnight Purple** functions as the base canvas, providing a depth that feels more premium and intentional than pure black. 

**Silver** is used as the primary accent for interactive elements, borders, and high-level metadata, evoking a precious-metal finish. **Translucent White** (at varying opacities) provides the frosted glass effect necessary for visual hierarchy. Use silver for primary calls to action and critical UI markers to ensure they "pop" against the deep violet backdrop.

## Typography
This design system utilizes a high-contrast typographic pairing to reinforce the "High-Gallery" feel. **Noto Serif** is reserved for headlines, titles, and price points, providing an editorial, authoritative tone. 

**Inter** handles all functional UI, body copy, and technical data. It is chosen for its clarity and neutral, futuristic profile. Labels and secondary metadata should use Inter with increased letter spacing and uppercase styling to mimic the architectural signage found in physical galleries.

## Layout & Spacing
The layout philosophy is "spacious minimalism." It uses a **12-column fluid grid** but prioritizes generous negative space to prevent the UI from feeling cluttered. 

Large "section-gaps" are used to separate different content zones, such as the featured hero asset from the marketplace grid. Elements should never feel cramped; margin and padding values are intentionally oversized to convey luxury and breathing room. Align content to a central container for standard pages, but allow for full-bleed glass overlays in "immersive" gallery views.

## Elevation & Depth
Depth is conveyed through **Glassmorphism and Tonal Layering**. Instead of traditional shadows, this design system uses:

1.  **Backdrop Blurs:** High-value blurs (20px to 40px) on semi-transparent surfaces to create a frosted glass effect.
2.  **Inner Glows:** Subtle, 1px Silver or White inner borders at low opacity (10-15%) to define the edges of glass panels.
3.  **Layered Opacity:** Foreground elements sit on surfaces with higher opacity (e.g., 20% white) while background elements sit on lower opacity (e.g., 5% white).
4.  **Tinted Overlays:** Modals and drawers should use a semi-transparent Midnight Purple tint rather than a generic black overlay to maintain color harmony.

## Shapes
To maintain an elite and architectural aesthetic, the design system uses **Soft (0.25rem to 0.75rem)** roundedness. 

Sharp edges feel too aggressive, while pill shapes feel too casual. The chosen "Soft" roundedness provides a sophisticated balance—modern and approachable, yet structured. Use the base 0.25rem for small components like checkboxes or tags, and 0.75rem for large asset cards and primary glass panels.

## Components
-   **Buttons:** Primary buttons feature a solid Silver fill with Midnight Purple text. Secondary buttons are "Ghost" style: a 1px Silver border with a backdrop blur and no fill.
-   **Cards:** Asset cards are the centerpiece. They use a frosted glass background with a subtle silver stroke. The asset image should be flush to the top, with metadata appearing in the lower glass section.
-   **Chips/Tags:** Small, high-transparency glass capsules with uppercase Inter text. Used for "Rare," "Limited Edition," or category labels.
-   **Inputs:** Minimalist bottom-border-only fields or fully transparent glass containers with a 1px Silver border on focus.
-   **Navigation:** A fixed, top-aligned glass bar with a high backdrop-blur value (40px) to ensure legibility as users scroll through vibrant NFT content.
-   **Price Display:** Always rendered in Noto Serif with a silver color or a subtle metallic gradient to emphasize the value of the assets.