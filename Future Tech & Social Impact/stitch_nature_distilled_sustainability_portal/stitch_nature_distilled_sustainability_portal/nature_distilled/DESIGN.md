---
name: Nature Distilled
colors:
  surface: '#f5fafe'
  surface-dim: '#d5dbde'
  surface-bright: '#f5fafe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4f8'
  surface-container: '#e9eff2'
  surface-container-high: '#e3e9ec'
  surface-container-highest: '#dee3e7'
  on-surface: '#171c1f'
  on-surface-variant: '#434843'
  inverse-surface: '#2b3134'
  inverse-on-surface: '#ecf1f5'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#8d4e2d'
  on-secondary: '#ffffff'
  secondary-container: '#fdaa83'
  on-secondary-container: '#783d1e'
  tertiary: '#494031'
  on-tertiary: '#ffffff'
  tertiary-container: '#615747'
  on-tertiary-container: '#dccdb9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#ffb693'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#703718'
  tertiary-fixed: '#f0e0cc'
  tertiary-fixed-dim: '#d3c4b1'
  on-tertiary-fixed: '#221a0e'
  on-tertiary-fixed-variant: '#4f4537'
  background: '#f5fafe'
  on-background: '#171c1f'
  surface-variant: '#dee3e7'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built on the principle of "Organic Professionalism." It bridges the gap between environmental activism and institutional finance, creating a high-trust atmosphere for sustainability initiatives. The brand personality is grounded, wise, and transparent.

The aesthetic leans into a **Tactile Minimalism**. It rejects the sterile, sharp-edged nature of traditional corporate tech in favor of "biomorphic" structures that feel hand-molded yet precisely engineered. We utilize subtle clay-like textures (noise and grain overlays) to give digital surfaces a sense of physical permanence and weight. The movement is fluid and intentional, mirroring natural cycles rather than mechanical transitions.

## Colors

The palette is a curated distillation of natural elements, muted to maintain a professional "SaaS" level of legibility and trust.

*   **Primary (Sage Green):** A deep, desaturated green used for primary actions and navigational anchors. It symbolizes growth and stability.
*   **Secondary (Clay Terracotta):** Used sparingly for highlights, data visualizations, and calls-to-action that require warmth.
*   **Tertiary (Warm Sand):** Used for large surface areas and subtle backgrounds to keep the interface feeling open and breathable.
*   **Neutral (Slate Grey):** A cool-toned grey reserved for high-contrast typography and utilitarian UI elements.

All surfaces should feature a micro-texture overlay (2% opacity monochromatic grain) to simulate the tactile feel of pressed clay or recycled paper.

## Typography

The typography system balances the modern geometric structure of **Manrope** for headings with the grounded, highly-legible nature of **Work Sans** for functional text.

Headlines should be set with tight tracking to appear authoritative. Body copy uses a generous line height to ensure readability in data-heavy sustainability reports. For labels and captions, uppercase styling with slight letter spacing is encouraged to provide a clear hierarchy against rich background textures.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy centered around a 12-column structure for desktop, transitioning to 4 columns for mobile. The rhythm is dictated by "Natural Breathing Room"—whitespace is used not just as a separator, but as a luxury element that signifies high-value content.

Margins are unusually wide to prevent the UI from feeling "cramped" or "industrial." Spacing between sections should follow a Fibonacci-inspired progression to feel more organic.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and physical shadow metaphors rather than pure light-source simulation.

1.  **The Base:** The lowest level is the "Warm Sand" background with a heavy clay texture.
2.  **Raised Surfaces:** Containers use "Surface" colors (soft off-whites) with very soft, diffused shadows. Shadows are tinted with the Primary Sage color (`rgba(74, 93, 78, 0.08)`) to maintain a cohesive environment.
3.  **Inset Elements:** Input fields and secondary buttons use inner shadows to appear "pressed" into the clay-like surface.
4.  **Glass Elements:** Occasional backdrop blurs (10px) are used for sticky navigations to maintain context of the earthy textures beneath.

## Shapes

The defining characteristic of this design system is its **Biomorphic Geometry**. Avoid perfect circles or identical corner radii.

Every container and button should utilize "squircle" mathematics or irregular radii. For example, a card might have a top-left radius of 24px, a top-right of 32px, a bottom-right of 20px, and a bottom-left of 28px. This creates a "hand-formed" appearance that feels organic and unique. Interactive elements should subtly "pulse" or shift their corner radii on hover, simulating a living, breathing interface.

## Components

### Buttons
Primary buttons are solid Sage Green with high-contrast white text. They must feature irregular, organic rounding. On hover, the shape should subtly shift its "blob" intensity.

### Cards & Containers
Cards use a subtle inner stroke (1px) in a slightly darker Clay tone. They serve as the primary vessel for sustainability data. The "biomorphic" rounding is most pronounced here to break the rigidity of the 12-column grid.

### Chips & Tags
Small, pill-like shapes but with "melted" edges. Used for categorizing impact areas (e.g., "Carbon Neutral," "Water Restoration"). Use Sage or Terracotta backgrounds with 15% opacity for a soft, integrated look.

### Input Fields
Fields appear as soft indentations in the UI. Use a slightly darker "Sand" color for the fill and a subtle inner shadow. Focus states are indicated by a 2px Sage Green organic border.

### Progress Indicators
Sustainability metrics should be visualized using thick, organic strokes that resemble natural growth rings or flowing water rather than sharp, mechanical bars.