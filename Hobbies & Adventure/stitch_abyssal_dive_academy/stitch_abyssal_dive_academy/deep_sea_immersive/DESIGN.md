---
name: Deep-Sea Immersive
colors:
  surface: '#091517'
  surface-dim: '#091517'
  surface-bright: '#2f3b3d'
  surface-container-lowest: '#051012'
  surface-container-low: '#121d1f'
  surface-container: '#162123'
  surface-container-high: '#202c2e'
  surface-container-highest: '#2b3739'
  on-surface: '#d8e5e7'
  on-surface-variant: '#bac9cc'
  inverse-surface: '#d8e5e7'
  inverse-on-surface: '#273234'
  outline: '#849396'
  outline-variant: '#3b494c'
  surface-tint: '#00daf3'
  primary: '#c3f5ff'
  on-primary: '#00363d'
  primary-container: '#00e5ff'
  on-primary-container: '#00626e'
  inverse-primary: '#006875'
  secondary: '#a8c9f3'
  on-secondary: '#0a3254'
  secondary-container: '#294b6f'
  on-secondary-container: '#9abbe4'
  tertiary: '#e3edff'
  on-tertiary: '#1d3249'
  tertiary-container: '#bdd2f0'
  on-tertiary-container: '#465a73'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#9cf0ff'
  primary-fixed-dim: '#00daf3'
  on-primary-fixed: '#001f24'
  on-primary-fixed-variant: '#004f58'
  secondary-fixed: '#d1e4ff'
  secondary-fixed-dim: '#a8c9f3'
  on-secondary-fixed: '#001d36'
  on-secondary-fixed-variant: '#27496c'
  tertiary-fixed: '#d1e4ff'
  tertiary-fixed-dim: '#b3c8e5'
  on-tertiary-fixed: '#051d33'
  on-tertiary-fixed-variant: '#344860'
  background: '#091517'
  on-background: '#d8e5e7'
  surface-variant: '#2b3739'
typography:
  h1:
    fontFamily: Inter
    fontSize: 4rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1280px
---

## Brand & Style
This design system is engineered to evoke the profound depth and technical mastery of professional diving. The brand personality is rooted in expertise and adventure, utilizing a visual language that feels both authoritative and atmospheric. 

The aesthetic strategy merges **Glassmorphism** with **Minimalism**. By using semi-transparent layers and background blurs, the UI mimics the refractive quality of water. High-quality underwater photography serves as the primary environmental backdrop, while fluid, organic shapes break the rigidity of standard grid layouts to simulate oceanic currents. The experience should feel like a high-end diving computer: precise, illuminated, and deeply immersive.

## Colors
The palette is built on a "Deep-Sea" gradient logic, moving from the near-black depth of Midnight Blue to the electric clarity of vibrant Cyan.

- **Primary (Cyan):** Used for critical actions, interactive states, and "glowing" accents that guide the user through the dark environment.
- **Secondary (Deep Navy):** Acts as the primary surface color for large containers and navigation bars.
- **Tertiary (Midnight Blue):** The foundational background color, providing the "infinite depth" required for the immersive theme.
- **Neutral (Light Cyan/White):** Reserved for typography and iconography to ensure AAA accessibility against dark backgrounds.

Gradients should be applied diagonally (top-left to bottom-right) to suggest light penetrating from the surface down into the depths.

## Typography
The typography strategy balances technical precision with high readability. 

**Inter** is utilized for headlines and labels to provide a clean, modern, and professional structure. Large headlines should use tighter letter spacing and heavy weights to command attention. 

**Manrope** is selected for body text and instructional content. Its slightly wider apertures and balanced proportions ensure maximum legibility during long-form reading, even when rendered in light weights against dark, translucent backgrounds. 

For technical data—such as dive depths or durations—use the `label-caps` style to create a functional, instrumentation-like aesthetic.

## Layout & Spacing
The layout follows a **Fluid Grid** model with generous internal padding to create a sense of "breathable" space, mirroring the vastness of the ocean.

- **Grid:** A 12-column system is used for desktop, scaling down to 4 columns for mobile.
- **Rhythm:** Spacing is strictly based on an 8px linear scale. Use larger increments (64px, 80px) between major sections to emphasize the minimalist, premium feel.
- **Fluidity:** Incorporate asymmetrical placement of images and floating "glass" cards that overlap section boundaries, breaking the horizontal "striping" common in standard web design.

## Elevation & Depth
Depth is communicated through **Glassmorphism** rather than traditional drop shadows. Surfaces do not "cast shadows" as they would in a sunlit environment; instead, they "glow" or "refract."

- **Tiers:** Use background blur (16px to 32px) on surfaces to separate them from the background imagery.
- **Inner Borders:** Apply a 1px semi-transparent border (top and left sides only) using Light Cyan at 20% opacity to simulate a light source hitting the edge of a glass pane.
- **Glows:** Interactive elements utilize a `box-shadow` with a Cyan tint and high diffusion (e.g., `0 0 20px rgba(0, 229, 255, 0.3)`) to indicate active states, mimicking underwater bioluminescence or diving gear displays.

## Shapes
The shape language is "Soft-Organic." While the core containers use a 0.5rem (rounded) base, larger immersive cards and image masks should utilize fluid, non-uniform radii or subtle "blob" shapes to reinforce the water theme.

- **Buttons:** Fully rounded (pill-shaped) for primary actions to contrast against the more structured content cards.
- **Inputs:** Standard rounded (0.5rem) to maintain a professional, systematic feel.
- **Decorative Elements:** Use SVG paths with "liquid" animations for section dividers instead of straight lines.

## Components
Consistent component styling ensures the design system remains cohesive across all user touchpoints.

- **Buttons:** Primary buttons feature a solid Cyan fill with dark text. Secondary buttons use a "ghost" style with a Cyan border and a soft backdrop blur. On hover, they should exhibit a subtle outer glow.
- **Cards (The "Glass" Container):** These are the workhorse of the system. They feature a 10-15% opacity Deep Navy fill, a 20px backdrop blur, and a thin, light-cyan stroke.
- **Input Fields:** Dark, semi-transparent backgrounds with Cyan bottom-borders that animate to full-width on focus.
- **Chips/Badges:** Small, pill-shaped elements used for difficulty levels (e.g., "Beginner," "Master"). Use low-opacity Cyan fills with high-contrast text.
- **Progress Indicators:** Circular gauges or fluid bars that mimic the look of dive computers/manometers.
- **Interactive Tooltips:** Use the same glassmorphism style as cards but with higher transparency and sharp Cyan accents for directional pointers.