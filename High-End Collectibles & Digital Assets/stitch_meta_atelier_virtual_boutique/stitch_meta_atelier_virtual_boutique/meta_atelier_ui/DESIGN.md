---
name: Meta-Atelier UI
colors:
  surface: '#19101c'
  surface-dim: '#19101c'
  surface-bright: '#403643'
  surface-container-lowest: '#130b16'
  surface-container-low: '#211824'
  surface-container: '#261c28'
  surface-container-high: '#302733'
  surface-container-highest: '#3c313e'
  on-surface: '#eeddee'
  on-surface-variant: '#d4c0d7'
  inverse-surface: '#eeddee'
  inverse-on-surface: '#372d3a'
  outline: '#9d8ba0'
  outline-variant: '#514255'
  surface-tint: '#ecb2ff'
  primary: '#ecb2ff'
  on-primary: '#520071'
  primary-container: '#bd00ff'
  on-primary-container: '#ffffff'
  inverse-primary: '#9900cf'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#777575'
  on-tertiary-container: '#fcffff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f8d8ff'
  primary-fixed-dim: '#ecb2ff'
  on-primary-fixed: '#320047'
  on-primary-fixed-variant: '#74009f'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#19101c'
  on-background: '#eeddee'
  surface-variant: '#3c313e'
typography:
  display-xl:
    fontFamily: syne
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: syne
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: syne
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  editorial-caps:
    fontFamily: outfit
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.4em
  body-md:
    fontFamily: outfit
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: outfit
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
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
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
---

## Brand & Style

This design system embodies the intersection of high-concept haute couture and the boundless potential of the digital metaverse. It is crafted for an audience that views fashion as a digital asset—ethereal, fluid, and avant-garde. The aesthetic is centered on **Glassmorphism** and **Ethereal Minimalism**, creating a sense of physical products rendered in digital light.

The emotional response should be one of "exclusive discovery." By utilizing translucent layers and iridescent light, the interface feels less like a traditional app and more like a curated gallery in a virtual space. The visual language favors breathing room, high-contrast clarity, and light-based feedback over traditional heavy shadows.

## Colors

The palette is anchored by a **Deep Charcoal** (#121212) foundation to provide a "void" where iridescent elements can shine. **Stark White** is used for primary text and structural borders to maintain a crisp, editorial feel.

The **Primary Iridescent Gradient** is the signature of this design system, transitioning through vivid pinks, deep purples, and electric blues. Use this gradient sparingly for interactive states, focal points, and branding moments. **Glowing Accent States** utilize a high-vibrancy Cyan to signify "active" or "hover" status, simulating a light source emitting from behind the frosted glass surfaces.

## Typography

The typography strategy employs a "High-Contrast Pairing." **Syne** is utilized for headlines, offering an avant-garde, wide-set geometry that feels uniquely digital. For body and utility text, **Outfit** provides a clean, geometric sans-serif balance that ensures legibility within glassmorphic containers.

Editorial spacing is a core requirement. Large titles should use tight tracking to feel cohesive and "designed," while utility labels and subheaders should use expanded letter-spacing (notably the `editorial-caps` style) to evoke the feeling of luxury print magazines.

## Layout & Spacing

This design system uses a **Fixed Grid** model on desktop to mimic the structured layout of fashion editorials, transitioning to a fluid model on mobile devices. 

- **Desktop (1440px+):** 12-column grid with wide 80px side margins to create a sense of exclusivity and focus.
- **Tablet:** 8-column grid with 40px margins.
- **Mobile:** 4-column grid with 20px margins.

Spacing follows an 8px rhythmic scale. Use larger-than-standard vertical padding (e.g., 120px - 160px) between sections to maintain the "avant-garde" minimalist aesthetic, allowing high-fidelity 3D assets to breathe within the layout.

## Elevation & Depth

Depth is conveyed through **Light Refraction** rather than traditional shadows. 

1.  **Backdrop Blurs:** All elevated surfaces must use `backdrop-filter: blur(20px)` with a semi-transparent white tint (5-10% opacity).
2.  **Inner Glows:** Instead of drop shadows, use thin 1px inner borders (top and left) with 30% white opacity to simulate a light source hitting the edge of a glass pane.
3.  **Iridescent Bloom:** Interactive elements should emit a soft "bloom" (a blurred colored shadow) in the primary iridescent hues when focused or hovered, making the UI feel like it is powered by internal light.

## Shapes

The shape language is **Precision-Softened**. Sharp corners are avoided to prevent a "brutalist" feel, but large radii are avoided to keep the look sophisticated and architectural. 

- **Cards & Containers:** Use `rounded-lg` (0.5rem) to suggest a machined, premium glass edge.
- **Buttons & Small Interactive Elements:** Use `rounded-sm` (0.25rem) for a sharp, high-fashion look.
- **Media Containers:** Large image/video frames remain sharp (0px) to treat the creative content like a full-bleed gallery piece.

## Components

### Buttons
Buttons are either "Glass Ghost" (frosted background with white text) or "Iridescent Solid" (gradient background). On hover, buttons should exhibit a subtle expansion (scale 1.02) and an increased backdrop blur. Text within buttons always uses the `editorial-caps` style.

### Cards
Frosted glass cards are the primary container. They must feature a 1px border using a semi-transparent white-to-transparent gradient to define the edges against the deep background.

### Lists
Lists are separated by ultra-thin (0.5px) stark white lines with 10% opacity. Interaction on a list item triggers a soft iridescent glow that follows the cursor (light-tracking effect).

### Inputs
Input fields are minimal—only a bottom border (0.5px white). Upon focus, the border transitions to the iridescent gradient and a subtle glow appears beneath the text.

### Progress & Interactive States
Use the primary iridescent gradient for all progress bars and sliders. The "thumb" of a slider should be a solid white circle that emits a cyan glow (`accent_color_hex`) when active.