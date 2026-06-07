---
name: MetaEstate Immersive
colors:
  surface: '#190b31'
  surface-dim: '#190b31'
  surface-bright: '#403259'
  surface-container-lowest: '#14052c'
  surface-container-low: '#22143a'
  surface-container: '#26183e'
  surface-container-high: '#302349'
  surface-container-highest: '#3c2e55'
  on-surface: '#ebdcff'
  on-surface-variant: '#e4bebb'
  inverse-surface: '#ebdcff'
  inverse-on-surface: '#372950'
  outline: '#ab8986'
  outline-variant: '#5b403e'
  surface-tint: '#ffb3ae'
  primary: '#ffb3ae'
  on-primary: '#68000d'
  primary-container: '#ff5354'
  on-primary-container: '#5c000a'
  inverse-primary: '#ba1826'
  secondary: '#d6baff'
  on-secondary: '#3d1f6a'
  secondary-container: '#593c87'
  on-secondary-container: '#cdadff'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#909191'
  on-tertiary-container: '#282a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ae'
  on-primary-fixed: '#410005'
  on-primary-fixed-variant: '#930016'
  secondary-fixed: '#ecdcff'
  secondary-fixed-dim: '#d6baff'
  on-secondary-fixed: '#270254'
  on-secondary-fixed-variant: '#543782'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#190b31'
  on-background: '#ebdcff'
  surface-variant: '#3c2e55'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

The design system is engineered to evoke the feeling of high-stakes digital frontierism. It positions the user as a sophisticated pioneer in the metaverse real estate market. The brand personality is aspirational, high-tech, and authoritative, bridging the gap between traditional luxury brokerage and cutting-edge virtual architecture.

The aesthetic follows a **Glassmorphic** and **Futuristic** movement. It utilizes deep spatial layers, translucent surfaces, and vibrant neon accents to simulate a 3D environment within a 2D screen. The interface should feel like a high-end "Head-Up Display" (HUD) for an investor navigating a digital universe. Every interaction should reinforce a sense of depth and tactile light.

## Colors

The color palette of the design system is rooted in a high-contrast, dark-mode-first approach. 

- **Deep Purple (#2D0B5A)** serves as the primary canvas color, representing the infinite depth of digital space. 
- **Sunset Orange (#FF4E50)** is the active "energy" color, used for primary calls-to-action, high-value status indicators, and focal points. 
- **Crisp White (#FFFFFF)** provides high-legibility anchors for critical data and body text. 
- A secondary **Neutral (#12042A)** is used for deep background layers to create a sense of infinite void behind the glass components.

Gradients are encouraged, specifically transitioning from Sunset Orange to a slightly more vibrant pinkish-red to simulate 3D light sources.

## Typography

Typography in this design system is designed to look technical and precise. **Space Grotesk** is used for all headlines and UI labels to provide a geometric, cutting-edge feel. A wider-than-average tracking (letter-spacing) is applied to all headlines to enhance the "tech" aesthetic and improve legibility against dark, complex backgrounds.

**Inter** is utilized for body copy and dense data sets. Its neutral, systematic nature balances the expressive qualities of Space Grotesk, ensuring that investment data remains the priority. For secondary metadata and "HUD" elements, use the `label-caps` style to mimic the readouts of a high-tech scanner.

## Layout & Spacing

The design system employs a **Fluid Grid** model built on an 8px base rhythm. Content is housed within a 12-column layout with generous 24px gutters to allow the "3D space" to breathe. 

Layouts should prioritize large, immersive hero areas for property visualization, while data panels are docked to the edges of the screen, reinforcing the "Command Center" aesthetic. Vertical rhythm is expansive; avoid crowding elements to maintain the "aspirational" feel of luxury property. Use the `xl` spacing for section breaks to emphasize the vastness of the digital estates being showcased.

## Elevation & Depth

Depth is the core differentiator of the design system. Unlike traditional material depth, we use **Glassmorphism** and **Light Emission**:

1.  **Surface Layers:** All containers use a semi-transparent background (e.g., White at 5-10% opacity) with a `backdrop-filter: blur(20px)`.
2.  **Neon Glows:** High-priority elements use "Drop Shadows" as outer glows. Instead of black shadows, use Sunset Orange with a 15-30% opacity and large blur radius (20px+).
3.  **Inner Light:** Use 1px semi-transparent white borders on the top and left edges of cards to simulate a light source hitting the edge of a glass pane.
4.  **Z-Axis:** Interactive elements should scale up slightly (+2%) on hover, appearing to float closer to the user.

## Shapes

The design system utilizes **Rounded** geometry. A base radius of 0.5rem (8px) provides a modern, sophisticated feel that is more approachable than sharp tech-brutalism but more professional than soft, pill-shaped consumer apps.

Large containers like property cards and immersive panels should use `rounded-xl` (1.5rem) to emphasize their role as "windows" into another world. Small interactive elements like checkboxes or utility tags should maintain the base `rounded` (0.5rem) to keep the UI feeling tight and engineered.

## Components

**Buttons:** 
Primary buttons feature a Sunset Orange gradient fill with white text. They must have a subtle outer glow of the same color. Secondary buttons use a "Ghost" style with a 1px orange border and a heavy backdrop blur.

**Cards (Property Tiles):** 
Cards are the primary vehicle for 3D content. They must use the glassmorphic style: blurred backgrounds and a thin, light-catching border. Text within cards should be layered, with labels in `label-caps` and prices in `headline-md`.

**Input Fields:** 
Inputs are ultra-minimal. A bottom border only, which glows Sunset Orange upon focus. Backgrounds for inputs should be a darker shade of Deep Purple to create an "inset" 3D effect.

**Chips & Badges:** 
Used for property status (e.g., "For Sale," "Sold"). These should be high-contrast with a slight neon pulse animation for "Live" events or auctions.

**3D Map Controller:** 
A unique component for this design system—a floating radial or directional controller used for navigating virtual land parcels. It should use heavy glassmorphism and clear, wide-tracked labels.

**Progress Indicators:** 
For investment tiers or "land scarcity" meters, use sleek, non-rounded progress bars with a gradient fill from Sunset Orange to a bright highlight.