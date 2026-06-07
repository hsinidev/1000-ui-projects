---
name: Stage-Glow Aesthetic
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#d5c0d7'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#9d8ba0'
  outline-variant: '#514254'
  surface-tint: '#ecb1ff'
  primary: '#ecb1ff'
  on-primary: '#520070'
  primary-container: '#bf00ff'
  on-primary-container: '#ffffff'
  inverse-primary: '#9900ce'
  secondary: '#d9b9ff'
  on-secondary: '#460085'
  secondary-container: '#8c0eff'
  on-secondary-container: '#efdeff'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#777676'
  on-tertiary-container: '#ffffff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f9d8ff'
  primary-fixed-dim: '#ecb1ff'
  on-primary-fixed: '#320046'
  on-primary-fixed-variant: '#75009e'
  secondary-fixed: '#eedbff'
  secondary-fixed-dim: '#d9b9ff'
  on-secondary-fixed: '#2a0054'
  on-secondary-fixed-variant: '#6400ba'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style

The design system is engineered to capture the raw energy and premium exclusivity of a front-row concert experience. It centers on an immersive "Stage-Glow" aesthetic, where the interface recedes into the darkness of a venue, allowing content and performance to take center stage. 

The style is a sophisticated blend of **Glassmorphism** and **High-Contrast Minimalism**. By utilizing deep, obsidian blacks as the canvas and vibrant neon purples as the "light," the UI mimics the atmosphere of a darkened arena illuminated by strobe lights. The emotional goal is to evoke a sense of hype, luxury, and digital craftsmanship, ensuring the user feels physically closer to the music through tactile, translucent layers and radiant glow effects.

## Colors

The palette is strictly nocturnal. The primary neon purple (#BF00FF) serves as the "spotlight," used for critical actions and active states. The secondary electric violet (#8B00FF) is reserved for gradients and depth-building. 

The neutral foundation relies on absolute black (#000000) for the base background to maximize the contrast of the OLED display, while a slightly lifted black (#050505) defines the primary containers. Accents should never feel flat; they must appear as light sources, often accompanied by soft, diffused glows to simulate the bloom of stage lighting against a dark environment.

## Typography

This design system utilizes **Epilogue** for all headlines to provide a bold, editorial edge that feels contemporary and expressive. High weight variance and tight letter-spacing on display sizes create the high-energy impact required for artist names and track titles.

For functional text and body copy, **Be Vietnam Pro** is used for its friendly yet modern geometric construction. It ensures high legibility during fast-paced interactions. Labels are frequently set in uppercase with increased letter-spacing to distinguish metadata from content.

## Layout & Spacing

The layout follows a **fluid grid** philosophy that prioritizes content immersion. A 12-column grid is standard for desktop, while mobile views leverage a flexible single-column layout with generous 24px side margins to ensure the "Glass" containers have room to breathe.

Spacing is based on a 4px baseline. Large vertical gaps (xl) are used between major sections to emphasize the premium, airy feel of the brand. Negative space is not just "empty"—it is part of the obsidian stage.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional shadows. Surfaces do not "cast" shadows as much as they "refract" light.

1.  **Base:** Pure #000000.
2.  **Layer 1 (The Glass):** Semi-transparent surfaces (white at 5-10% opacity) with a 20px backdrop-blur. This creates a frosted effect where background content is softly visible.
3.  **Borders:** Elements are defined by 1px "inner-glow" borders—subtle, low-opacity white or purple lines that simulate light hitting the edge of a glass pane.
4.  **Active Depth:** Interactive elements use an outer neon glow (#BF00FF at 30% opacity) to signify they are "on" or "live."

## Shapes

The design system employs a **Rounded** shape language to balance the aggressive high-contrast colors with a sense of approachable luxury. Standard UI components use a 0.5rem (8px) radius, while larger cards and containers utilize 1rem (16px) or 1.5rem (24px) for a more organic, modern feel. Buttons and specific badges may use a full pill-shape to draw focus as interactive "capsules."

## Components

-   **Buttons:** Primary buttons are pill-shaped with the `accent_gradient`. They feature a subtle outer glow on hover. Secondary buttons use the "Glass" effect with a 1px violet border.
-   **Cards:** Album and artist cards use the frosted glass treatment. The background blur is essential to maintain legibility when cards overlap vibrant artist photography.
-   **Lists:** List items are separated by thin, low-opacity (10%) white dividers. Active tracks or items are highlighted with a vertical neon purple "status bar" on the left edge.
-   **Inputs:** Text fields are dark and recessed with a subtle bottom border. Upon focus, the border transitions to a neon purple glow.
-   **Glow Accents:** Floating "Light Orbs"—large, extremely blurred blobs of purple—should be placed behind key components to simulate volumetric stage lighting.
-   **Now Playing Bar:** A persistent, high-blur glass bar at the bottom of the viewport, featuring a neon progress bar that appears to "pulse" with the music.