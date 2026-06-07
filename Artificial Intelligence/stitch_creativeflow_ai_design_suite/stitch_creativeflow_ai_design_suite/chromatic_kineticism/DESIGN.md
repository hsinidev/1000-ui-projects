---
name: Chromatic Kineticism
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#ffb690'
  on-tertiary: '#552100'
  tertiary-container: '#ec6a06'
  on-tertiary-container: '#4a1c00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#ffdbca'
  tertiary-fixed-dim: '#ffb690'
  on-tertiary-fixed: '#341100'
  on-tertiary-fixed-variant: '#783200'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display:
    fontFamily: Epilogue
    fontSize: 72px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  h1:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
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
  gutter: 24px
  margin: 40px
---

## Brand & Style

This design system is built to mirror the velocity of the creative process. It balances the raw intensity of a high-energy artistic environment with the sophisticated precision required by professional AI tools. The visual language utilizes a "Deep Space" aesthetic—where vibrant, neon-inflected gradients collide with absolute blacks and stark whites to create a sense of infinite digital canvas.

The core style is a fusion of **Glassmorphism** and **High-Contrast Boldness**. It rejects the mundanity of traditional SaaS interfaces in favor of a layered, cinematic experience. Users should feel empowered, as if they are operating a high-performance engine for their imagination. The interface does not just facilitate work; it inspires it through kinetic visuals and a tactile sense of depth.

## Colors

The palette is anchored in a true-black environment to allow vibrant accent colors to "glow" with maximum luminosity. 

- **Primary (Electric Purple):** Represents the AI intelligence and the "magic" of the tool.
- **Secondary (Cyber Cyan):** Used for precision tools, active states, and technical feedback.
- **Tertiary (Solar Orange):** Acts as a high-energy disruptor for calls to action and creative highlights.
- **Neutrals:** A range of "Onyx" grays provide structure without breaking the dark-mode immersion.

Gradients should be used purposefully to indicate flow and direction, often serving as the "fuel" behind interactive elements.

## Typography

This design system employs a high-contrast typographic pairing to distinguish between "Creation" and "Utility."

**Epilogue** is the voice of the brand. It is used for all major headings and display text. Its geometric yet expressive nature feels modern and editorial. Use tight letter spacing for display sizes to increase the visual impact and "power" of the headlines.

**Manrope** is the workhorse for the interface. It provides a clean, balanced, and highly legible experience for settings, labels, and long-form body text. Its neutral but contemporary character ensures that the AI's complex technical data remains easy to digest.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with an emphasis on "Negative Space as Canvas." While the grid provides the structure, this design system encourages "Breaking the Box"—elements like floating glass panels and overlapping imagery should intentionally sit across grid lines to create an artistic, layered feel.

A standard 12-column grid is used for core dashboard layouts, but padding and margins are generous (80px+) in hero sections to evoke a premium, gallery-like experience. Use the 8px base unit for all component-level spacing to maintain rhythmic consistency amidst the visual energy.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. It is achieved through three distinct layers:

1.  **The Void (Level 0):** The absolute black background. This is the foundation.
2.  **The Frosted Layer (Level 1):** Semi-transparent surfaces using **Glassmorphism**. Apply a 20px background blur and a 1px semi-transparent white border (opacity 10%) to define the edges of cards.
3.  **The Kinetic Layer (Level 2):** Elements that "float" above the frosted layers. These use **Ambient Shadows**—soft, widely diffused shadows (30px-50px blur) tinted with a subtle purple or cyan glow instead of pure black to simulate light emission from the interface.

Overlapping cards is a signature move: an image or a secondary tool window should often offset its parent container by 24-48px to create a physical sense of "stacking" in a 3D space.

## Shapes

The shape language balances organic creativity with digital precision. Level 2 (Rounded) is the default, providing a 0.5rem (8px) base radius. This softens the aggressive high-contrast color palette, making the interface feel approachable and modern.

Large container cards and "Glass" panels should utilize `rounded-xl` (1.5rem / 24px) to emphasize the frosted-glass aesthetic. Small utility elements like checkboxes or mini-tags may drop down to `rounded-sm` (4px) to retain a sense of crispness.

## Components

- **Buttons:** Primary buttons use the `gradient_vibrant` background with white text. Hover states should trigger a "glow" effect via a box-shadow that matches the gradient colors. Secondary buttons use the "Glass" style with a 1px border.
- **Glass Cards:** The signature component. They must feature a `backdrop-filter: blur(16px)`, a dark semi-transparent background, and a subtle top-down internal highlight to simulate thickness.
- **Input Fields:** Deep charcoal backgrounds (#171717) with 1px borders that transition to a Cyan or Purple gradient on focus.
- **Chips & Tags:** Use high-saturation backgrounds (Purple/Cyan/Orange) with low opacity (15%) and a solid border of the same color for a "neon sign" effect.
- **AI Prompt Bar:** A specialized floating component. It should be a pill-shaped glass container that spans the bottom-center of the viewport, featuring a subtle animated gradient border to indicate "Thinking" or "Active" states.
- **Lists:** Items should be separated by high-contrast thin lines (#262626) with generous vertical padding to maintain the "Gallery" aesthetic.