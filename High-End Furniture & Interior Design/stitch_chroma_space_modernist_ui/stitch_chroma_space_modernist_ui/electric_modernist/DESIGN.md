---
name: Electric Modernist
colors:
  surface: '#fff9ef'
  surface-dim: '#e1d9c7'
  surface-bright: '#fff9ef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf3e0'
  surface-container: '#f6edda'
  surface-container-high: '#f0e7d5'
  surface-container-highest: '#eae2cf'
  on-surface: '#1f1b10'
  on-surface-variant: '#4d4732'
  inverse-surface: '#343024'
  inverse-on-surface: '#f9f0dd'
  outline: '#7e775f'
  outline-variant: '#d0c6ab'
  surface-tint: '#705d00'
  primary: '#705d00'
  on-primary: '#ffffff'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#e9c400'
  secondary: '#2559bd'
  on-secondary: '#ffffff'
  secondary-container: '#6c98ff'
  on-secondary-container: '#002f76'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#d9dada'
  on-tertiary-container: '#5e5f60'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#dae2ff'
  secondary-fixed-dim: '#b1c5ff'
  on-secondary-fixed: '#001946'
  on-secondary-fixed-variant: '#00419e'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fff9ef'
  on-background: '#1f1b10'
  surface-variant: '#eae2cf'
typography:
  headline-xl:
    fontFamily: Epilogue
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Work Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Epilogue
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  border-width: 4px
  hard-shadow: 8px
---

## Brand & Style
The design system embodies a high-energy, unapologetic aesthetic rooted in the fusion of Neo-Brutalism and Pop-Art. It is designed for a design-conscious audience that values confidence, geometric precision, and artistic expression. The UI is intentionally loud, replacing subtle gradients and soft shadows with raw structural elements and high-contrast color blocking.

The emotional response should be one of immediate impact and clarity—reminiscent of a physical design magazine. It avoids the "safety" of corporate minimalism in favor of a bold, tactile environment that feels both structured and rebellious.

## Colors
The palette is restricted to a high-saturation triad to maintain visual intensity. 

- **Primary Yellow (#FFD700):** Used for key calls to action, highlights, and primary "hero" Bento containers.
- **Cobalt Blue (#0047AB):** Used for interactive secondary elements, links, and contrasting background sections.
- **Stark White (#FFFFFF):** The primary canvas color, ensuring that the heavy black accents and vibrant primary colors remain legible.
- **Heavy Black (#000000):** Used for all structural borders, typography, and "hard" shadows to anchor the design.

Color usage should be aggressive; avoid using neutral grays. If a surface is not white, it should be a full-strength primary or secondary color.

## Typography
Typography is a structural pillar of this design system. Headings utilize **Epilogue** for its geometric, editorial feel. These should be set with tight letter-spacing and heavy weights to create "blocks" of text that integrate with the Bento-grid layout.

**Work Sans** is used for body copy to provide a clean, legible counterpoint to the aggressive headers. Maintain generous line-heights for body text to ensure readability against high-contrast backgrounds. All labels and functional micro-copy should be set in Epilogue Bold and converted to uppercase to reinforce the architectural tone.

## Layout & Spacing
The layout follows a strict **Bento-box grid** philosophy. Every element must be contained within a defined rectangular cell.

- **Grid Model:** A 12-column fluid grid for desktop and a 4-column grid for mobile. 
- **Gutter Logic:** Gutters should match the `border-width` (4px) or multiples of the `base` unit (4px) to create a seamless "window-pane" effect where borders appear to touch.
- **Rhythm:** Use the 8px stepping system for internal padding. Containers should use `lg` (40px) or `xl` (64px) outer margins to frame the high-energy content with sufficient breathing room.

## Elevation & Depth
This design system rejects ambient shadows and blur-based depth. Hierarchy is established through **Bold Borders** and **Hard Shadows**.

- **Structural Borders:** Every container, button, and input must have a minimum 4px solid black border.
- **Hard Shadows:** To indicate interactivity or "lift," use a 2D offset shadow (8px x 8px) in solid black. There is no blur radius.
- **Layering:** Elements appear to sit on different planes based on their background color and shadow offset, rather than Z-axis gradients. 
- **Active State:** When pressed, elements should shift their shadow to 0px and translate 4px or 8px to simulate a physical "click" onto the page.

## Shapes
Shapes are strictly geometric and rectangular. This design system uses **zero border-radius** across all components, including buttons, input fields, and containers. 

The "stark corner" approach reinforces the modernist architectural influence. Circles may only be used for specific icon backgrounds or profile avatars, but they must still be framed by a square container or a thick black stroke.

## Components
- **Buttons:** Massive, rectangle-shaped, with 4px black borders. Primary buttons use the Primary Yellow background with black text. On hover, apply the hard 8px shadow.
- **Chips:** Small rectangular blocks with white or yellow backgrounds and 2px black borders. Use Epilogue Bold for text.
- **Cards (Bento Cells):** High-saturation image backgrounds or solid color fills. Content within cards is bottom-aligned to mimic magazine layouts.
- **Input Fields:** Stark white background, 4px black border, and no rounded corners. The focus state changes the background color to Primary Yellow.
- **Checkboxes/Radios:** Square-only. No circles. The "checked" state is a solid black fill or a heavy "X" mark.
- **Swipeable Strips:** For mobile, use full-bleed horizontal carousels where the image is framed by a 4px black border on the top and bottom.
- **Imagery:** High-saturation, high-contrast photography. Images should be treated as structural elements, often filling the entire Bento cell.