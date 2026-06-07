---
name: Bio-Interior
colors:
  surface: '#f8faf8'
  surface-dim: '#d8dad9'
  surface-bright: '#f8faf8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f2'
  surface-container: '#eceeec'
  surface-container-high: '#e6e9e7'
  surface-container-highest: '#e1e3e1'
  on-surface: '#191c1b'
  on-surface-variant: '#414844'
  inverse-surface: '#2e3130'
  inverse-on-surface: '#eff1ef'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#8c4f09'
  on-secondary: '#ffffff'
  secondary-container: '#fdad62'
  on-secondary-container: '#754000'
  tertiary: '#242627'
  on-tertiary: '#ffffff'
  tertiary-container: '#3a3c3c'
  on-tertiary-container: '#a5a6a6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffdcc1'
  secondary-fixed-dim: '#ffb878'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6c3a00'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f8faf8'
  on-background: '#191c1b'
  surface-variant: '#e1e3e1'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  margin-mobile: 20px
  gutter: 16px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is anchored in the "Lush & Sustainable" narrative, targeting high-end residential and commercial clients who seek to integrate nature into modern architecture. The UI evokes a sense of tranquility, premium craftsmanship, and ecological vitality.

The visual style is **Tactile & Organic**, blending the soft, pillowy depth of neomorphism with realistic, earthy textures. It avoids rigid geometric perfection in favor of fluid, biological forms. The "Breathe" keyframe animation is a core identifier, applying a subtle, rhythmic pulse to headers to simulate the respiration of a living organism, reinforcing the brand's connection to air quality and life.

## Colors

The palette is derived from deep silvan environments and raw earth.
- **Forest Green (#1B4332):** The primary anchor, used for headers, key backgrounds, and primary actions to represent dense foliage.
- **Terra-Cotta (#D68C45):** The secondary accent, used for high-contrast call-to-actions and interactive highlights, referencing clay pots and organic soil.
- **White (#FFFFFF) & Off-White (#F9FBF9):** Used for canvases to provide "air" and high-end clarity.
- **Surface Accents:** Use a 5% opacity Forest Green overlay on white surfaces to create a "leaf-tinted" neutral background.

## Typography

The typography system creates a sophisticated contrast between heritage and modern utility.
- **Headlines:** Utilize the "Breathe" animation (scale 1.0 to 1.02) on primary page titles. Serif characters provide a literary, high-end feel.
- **Body:** Plus Jakarta Sans provides a clean, breathable counterpoint to the dense serif headings, ensuring legibility on mobile devices.
- **Hierarchy:** Use wide letter-spacing for uppercase labels (Terra-Cotta) to denote categories or "Sustainable Certifications."

## Layout & Spacing

This design system utilizes a **Mobile-First Fluid Grid**. 
- **Rhythm:** An 8px base unit drives all vertical rhythm.
- **Margins:** Generous 20px side margins ensure content does not feel cramped, mimicking the open space of a garden.
- **Negative Space:** Intentional "dead zones" are used between sections to allow the user's eyes to rest, emphasizing the premium nature of the products.
- **Dividers:** Traditional lines are replaced with leaf-patterned SVG masks or organic "vining" paths that bleed off the edge of the screen.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Subtle Textures**.
- **Shadows:** Use large-radius, low-opacity shadows tinted with Forest Green (`rgba(27, 67, 50, 0.08)`) to suggest elements are floating above a mossy surface.
- **Depth:** Higher elevation elements (like "Plant Care" cards) should utilize a grain texture overlay at 3% opacity to mimic the tactile feel of recycled paper or stone.
- **Backdrop:** Use a soft blur (10px) on navigation bars to allow the lush greens of the background photography to peek through.

## Shapes

The shape language is strictly **Asymmetrical & Organic**.
- **Corner Radii:** Standard containers use a 16px (rounded-lg) radius.
- **Teardrop Elements:** Primary buttons and featured image frames should use mismatched radii (e.g., `40px 40px 8px 40px`) to create a "teardrop" or "seedling" silhouette.
- **Iconography:** Use thick-stroke (2pt) icons with rounded terminals. Avoid sharp angles; every point should have a slight radius.

## Components

- **Teardrop Buttons:** The primary action button uses a Terra-Cotta fill with a custom teardrop shape. On hover/active, it should "pulse" slightly.
- **Living Cards:** Cards containing plant data should feature an image that breaks the top boundary, creating a 3D effect.
- **Organic Chips:** Category tags use a Forest Green border with a 50% opacity green tint fill, shaped like small river pebbles.
- **Input Fields:** Bottom-aligned labels only, with a soft-bottom border that looks like a subtle horizon line. No harsh box-enclosures.
- **The "Breathe" Header:** A specialized component for top-level navigation that rhythmically scales and desaturates slightly, creating a "living" UI header.
- **Growth Progress Bar:** For maintenance tracking, progress bars use a vine-growing animation rather than a standard fill-load.