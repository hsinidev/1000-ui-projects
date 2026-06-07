---
name: Muse-Masterclass
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
  display-xl:
    fontFamily: Playfair Display
    fontSize: 84px
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style
This design system embodies an elite, avant-garde aesthetic tailored for high-level creative direction. The visual narrative is "Dark Editorial"—mixing the prestigious weight of traditional fashion journalism with futuristic, digital-first accents. 

The style utilizes a sophisticated blend of **Glassmorphism** and **Minimalism**. It relies on high-contrast compositions where deep, infinite blacks meet sharp metallic lines. Atmosphere is generated through subtle grainy film textures and ethereal background blurs, creating a sense of depth and curated mystery. The user experience should feel like stepping into a private, high-end gallery or a bespoke digital atelier.

## Colors
The palette is anchored by **Deep Space Black**, which serves as the canvas for all interactions. **Metallic Silver** is used for structural elements, borders, and secondary text to provide a cold, architectural precision.

Vibrant accents—**Electric Purple** and **Acid Green**—are used sparingly to highlight high-value actions, active states, or critical calls to action. These colors should appear as if they are glowing light sources within a dark room. Surfaces use a semi-transparent glass effect to maintain the atmospheric quality of the design.

## Typography
The typographic hierarchy creates an immediate sense of prestige. **Playfair Display** is reserved for large headings and display moments, evoking the feel of a luxury masthead. Use tight letter-spacing for large headlines to increase the "editorial" impact.

**Inter** provides a functional, neutral counterpoint for body copy and UI labels. Its crisp, geometric clarity ensures readability against dark backgrounds. Use the "Label-Caps" style for navigation and small headers to maintain a disciplined, professional grid.

## Layout & Spacing
The layout follows a **Fixed Grid** model for desktop, centered within the viewport to create a focused, gallery-like experience. Large horizontal margins (64px+) are encouraged to allow the content to "breathe" and reinforce the premium positioning.

Spacing follows an 8px base unit but prioritizes large vertical "breathing room" (stack-lg) between major sections to emphasize the artistic nature of the masterclass. Information density should be kept low to medium.

## Elevation & Depth
Depth in this design system is achieved through **Glassmorphism** and light-based layering rather than traditional drop shadows. 

1.  **Base Layer:** Solid Deep Space Black with a 2% noise/grain overlay.
2.  **Middground Layer:** Surfaces with a 3% white opacity and a heavy backdrop-blur (30px-40px). These are used for cards and modals.
3.  **Accents:** Elements "float" using 1px stroke borders in Metallic Silver at 40% opacity. 
4.  **Atmospheric Glow:** Subtle radial gradients of Electric Purple or Acid Green (5-10% opacity) may be placed deep in the background to provide a sense of "colored mist" behind glass layers.

## Shapes
To maintain an avant-garde and professional tone, the shape language is strictly **Sharp (0px)**. All containers, buttons, and input fields must use 90-degree corners. This evokes architectural precision and high-end fashion branding. 

The only exception to the sharp rule is the use of circular "dots" for specific status indicators or decorative elements, emphasizing the contrast between the rigid grid and the "Muse" energy.

## Components
-   **Buttons:** Primary buttons use a solid Metallic Silver background with black text. Secondary buttons are "Ghost" style: transparent background, 1px silver border, and white text. Hover states should trigger a subtle glow or a color shift to Acid Green.
-   **Cards:** Use the glassmorphism technique (low-opacity white fill + heavy blur) with a 1px silver border. Content inside should be heavily inset.
-   **Inputs:** Minimalist bottom-border only, or a full 1px silver border. Placeholder text should be in a muted silver. On focus, the border shifts to Electric Purple.
-   **Chips/Tags:** Small, all-caps text using the "Label-Caps" typography, enclosed in a thin silver frame.
-   **Navigation:** Top-tier navigation should be sparse. Use high-contrast hover states where text transitions from Muted Silver to Bright White.
-   **Signature Element:** "The Silver Thread"—a 1px vertical or horizontal silver line used to separate sections or guide the eye through the editorial layout.