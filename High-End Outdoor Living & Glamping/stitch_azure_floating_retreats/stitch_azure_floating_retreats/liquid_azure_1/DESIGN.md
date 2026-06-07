---
name: Liquid Azure
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#414754'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005cbc'
  primary: '#005ab7'
  on-primary: '#ffffff'
  primary-container: '#0072e5'
  on-primary-container: '#fefcff'
  inverse-primary: '#abc7ff'
  secondary: '#156874'
  on-secondary: '#ffffff'
  secondary-container: '#a4ebf9'
  on-secondary-container: '#1c6c78'
  tertiary: '#535e61'
  on-tertiary: '#ffffff'
  tertiary-container: '#6c767a'
  on-tertiary-container: '#f9fdff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#004590'
  secondary-fixed: '#a7eefc'
  secondary-fixed-dim: '#8bd2df'
  on-secondary-fixed: '#001f24'
  on-secondary-fixed-variant: '#004e59'
  tertiary-fixed: '#d9e4e8'
  tertiary-fixed-dim: '#bdc8cc'
  on-tertiary-fixed: '#131d20'
  on-tertiary-fixed-variant: '#3e484c'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding-mobile: 24px
  container-padding-desktop: 64px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
This design system embodies the serenity of high-end over-water living. The brand personality is "Effortless Luxury"—a mix of sophisticated architectural minimalism and the organic, refreshing movement of water. The target audience seeks exclusivity, tranquility, and a deep connection to nature without sacrificing modern comfort.

The UI style is centered on **Glassmorphism**, utilizing layered translucency to mimic the clarity of water and the mist of the ocean. It prioritizes "Liquid" transitions—animations that feel viscous and smooth rather than mechanical. High-resolution drone photography serves as the foundation of the visual experience, with UI elements floating lightly above the scenery.

## Colors
The palette is derived from the varying depths of the ocean and the brightness of a coastal midday sun. 

- **Azure Blue (Primary):** Used for primary actions, active states, and highlighting key navigational elements.
- **Deep Ocean Teal (Secondary):** Provides contrast and grounding for text and structural components, representing the mystery and depth of the sea.
- **Pristine White (Neutral/Background):** The canvas for the glassmorphic effects, ensuring the UI remains airy and breathable.
- **Surface Tints:** Use ultra-light azure tints for subtle backgrounds to prevent a sterile, "pure-gray" institutional feel.

## Typography
The typographic hierarchy balances the geometric, modern authority of **Montserrat** with the functional clarity of **Inter**. 

Headlines utilize lighter weights (300-400) at larger scales to evoke a sense of high-fashion and editorial elegance. Body text is prioritized for legibility against dynamic photographic backgrounds, utilizing a slightly generous line height to maintain the "airy" design philosophy. Labels and captions should be set in uppercase with increased letter spacing to provide a sophisticated, metadata-like feel.

## Layout & Spacing
This design system employs a **fluid layout model** optimized for mobile-first consumption. 

Margins are intentionally wide to create a "gallery" effect for the photography. On mobile devices, a single-column layout is standard, with 24px side margins. On larger screens, the design expands into a 12-column grid with generous 64px margins. Use "white space" as a functional element to separate concepts rather than heavy dividers or borders. Vertical spacing should follow an 8px rhythmic scale to maintain consistency across the fluid transitions.

## Elevation & Depth
Depth is not communicated through traditional drop shadows, but through **Backdrop Blurs** and **Specular Highlights**.

- **Surface Layers:** Use semi-transparent white (60-80% opacity) with a `backdrop-filter: blur(20px)`.
- **Borders:** Every glass layer should have a 1px solid border at 20% white opacity to define the edge of the "glass."
- **Shadows:** Use extremely diffused, low-opacity shadows (e.g., `rgba(0, 127, 255, 0.05)`) to give the impression of elements floating above water.
- **Liquid Depth:** Active elements may expand slightly or "ripple" when interacted with, creating a tactile, fluid response.

## Shapes
Shapes are defined by organic, soft curvature. While the base `roundedness` is set to 2 (0.5rem), interactive components like buttons and search bars should lean toward `rounded-xl` (1.5rem) or full pill shapes to mimic smooth river stones or water droplets. 

Avoid sharp 90-degree angles entirely, as they conflict with the "Fluid" and "Refreshing" brand values. Large containers and image masks should use the most generous corner radii to maintain a premium, friendly aesthetic.

## Components
- **Buttons:** Primary buttons use a solid Azure Blue with a subtle inner glow. Secondary buttons are "Glass" (translucent white with blur and a 1px border).
- **Cards:** Floating glass layers over imagery. Content should be bottom-aligned within the card to maximize image visibility.
- **Input Fields:** Minimalist translucent wells with a 1px bottom border that expands into a full Azure outline upon focus.
- **Progress Indicators:** Use "Liquid" loaders—smoothly oscillating waves or expanding circles rather than standard spinning wheels.
- **Floating Action Bar:** A bottom-docked navigation bar using the highest level of glass blur, making it appear as though the menu is floating on the surface of the content.
- **Chips:** Small, pill-shaped tags used for "Available" or "Luxury Tier" indicators, using subtle ocean-teal backgrounds.