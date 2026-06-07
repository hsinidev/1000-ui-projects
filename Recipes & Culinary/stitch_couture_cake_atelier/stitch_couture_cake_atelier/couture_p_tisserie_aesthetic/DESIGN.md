---
name: Couture Pâtisserie Aesthetic
colors:
  surface: '#faf9f9'
  surface-dim: '#dadada'
  surface-bright: '#faf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#524345'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f0'
  outline: '#857374'
  outline-variant: '#d7c1c3'
  surface-tint: '#8c4b55'
  primary: '#8a4853'
  on-primary: '#ffffff'
  primary-container: '#a6606b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb2bc'
  secondary: '#5e604d'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1c9'
  on-secondary-container: '#636451'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd9dd'
  primary-fixed-dim: '#ffb2bc'
  on-primary-fixed: '#3a0915'
  on-primary-fixed-variant: '#70343e'
  secondary-fixed: '#e4e4cc'
  secondary-fixed-dim: '#c8c8b0'
  on-secondary-fixed: '#1b1d0e'
  on-secondary-fixed-variant: '#474836'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#faf9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  xxl: 128px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

The design system is anchored in the concept of "Pastry as Art." It targets an ultra-high-net-worth clientele seeking bespoke, artisanal excellence. The brand personality is poised, quiet, and exclusive, evoking the emotional response of entering a high-end atelier or a private gallery.

The visual style is a meticulous blend of **Minimalism** and **Modern Editorial** design. It prioritizes the "breathability" of the interface, using generous negative space to ensure that high-fidelity imagery of the cakes remains the undisputed focal point. Every interaction is designed to feel deliberate and effortless, utilizing thin lines and a restrained palette to convey sophistication without clutter.

## Colors

This design system utilizes a warm, organic palette that mimics the raw materials of high-end baking—cream, flour, and metallic accents. 

- **Primary (Rose Gold):** Reserved exclusively for calls to action, active states, and critical brand accents. It should be used sparingly to maintain its impact.
- **Secondary (Cream):** The foundation of the design system. This serves as the primary background color, providing a softer, more luxurious alternative to pure white.
- **Neutral (Soft Grey):** Used for secondary text, hairline borders, and decorative dividers. It ensures legibility while maintaining a low-contrast, ethereal feel.
- **Tertiary (White):** Used for high-level surface containers or to create subtle "paper-on-cream" layering effects.

## Typography

The typography strategy for this design system relies on the contrast between traditional elegance and modern clarity. 

**Headlines** utilize a refined serif to establish an authoritative, "high-couture" voice. Generous letter spacing is mandatory for all display and headline levels to evoke a sense of luxury and airiness. 

**Body copy** is set in a modern, balanced sans-serif. This ensures that while the brand feels classic, the user experience remains efficient and accessible. **Labels** and small metadata should be set in uppercase with increased tracking to mimic the engraving found on luxury packaging.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to maintain a curated, editorial composition, transitioning to a fluid margin-based system for mobile. 

The spacing rhythm is intentionally "loose." Margin and padding values should lean toward the larger end of the scale (XL and XXL) to create the "airy" feel requested. Alignment should be primarily centered for hero sections and brand-heavy pages, while functional pages (like a checkout or booking form) follow a structured 12-column grid. Vertical rhythm is established through large blocks of whitespace between sections to allow the user's eyes to rest.

## Elevation & Depth

Hierarchy is conveyed through **Tonal Layers** and **Ambient Shadows**. Because the background is a rich Cream, depth is created by placing White containers slightly "above" the surface using highly diffused, low-opacity shadows.

Shadows should never be harsh or black. Use a subtle Rose Gold or Soft Grey tint in the shadow color (e.g., 5% opacity) with a large blur radius (30px+) to simulate natural, soft studio lighting. Thin, 1px Soft Grey borders are preferred over shadows for defining structural elements like input fields and image frames.

## Shapes

The shape language of this design system is "Soft Minimalist." While the layout is structured and grid-based, UI elements possess a subtle 0.25rem (4px) corner radius to prevent the interface from feeling sharp or clinical. 

High-fidelity imagery should remain sharp-cornered or use a very slight roundness (Soft) to maintain the look of a professional photography portfolio. Decorative elements, such as thin line dividers, should be 1px thick and extend to the edges of the grid or terminate in a soft fade.

## Components

### Buttons
Buttons are the primary vehicle for the Rose Gold accent.
- **Primary:** Solid Rose Gold fill with white text. No shadow, or a very faint ambient shadow on hover.
- **Secondary:** 1px Rose Gold or Soft Grey border ("Ghost Button") with increased letter spacing on the label.

### Input Fields
To maintain minimalism, input fields should avoid full enclosures. Use a "Bottom-Border Only" style in Soft Grey, which turns Rose Gold upon focus. Labels should be small, uppercase, and float above the line.

### Cards
Cards for cake collections should be borderless with a White background and a very soft ambient shadow. Imagery should occupy at least 70% of the card area. 

### Chips & Tags
Used for cake flavors or categories (e.g., "Gluten-Free," "Wedding"). These should be styled as pill-shaped outlines with 1px Soft Grey borders and small-caps typography.

### Additional Elements
- **Image Carousels:** Use thin line indicators instead of bulky arrows.
- **Dividers:** Horizontal rules should be 1px, Soft Grey, and used only to separate major content thematic shifts.