---
name: Kinetic-Bag Design System
colors:
  surface: '#fcf9f6'
  surface-dim: '#dcdad7'
  surface-bright: '#fcf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f0'
  surface-container: '#f0edea'
  surface-container-high: '#eae8e5'
  surface-container-highest: '#e5e2df'
  on-surface: '#1c1c1a'
  on-surface-variant: '#554240'
  inverse-surface: '#31302f'
  inverse-on-surface: '#f3f0ed'
  outline: '#887270'
  outline-variant: '#dbc1be'
  surface-tint: '#99443e'
  primary: '#2c0001'
  on-primary: '#ffffff'
  primary-container: '#4e0b0b'
  on-primary-container: '#d37068'
  inverse-primary: '#ffb3ac'
  secondary: '#725a39'
  on-secondary: '#ffffff'
  secondary-container: '#fbdbb0'
  on-secondary-container: '#765f3d'
  tertiary: '#0f1112'
  on-tertiary: '#ffffff'
  tertiary-container: '#242626'
  on-tertiary-container: '#8c8d8d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb3ac'
  on-primary-fixed: '#400204'
  on-primary-fixed-variant: '#7b2d29'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f6'
  on-background: '#1c1c1a'
  surface-variant: '#e5e2df'
typography:
  display-xl:
    fontFamily: playfairDisplay
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: playfairDisplay
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  headline-md:
    fontFamily: playfairDisplay
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: metropolis
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system embodies "Architectural-Chic," a fusion of high-fashion luxury and structural precision. The brand personality is exclusive, intelligent, and tactile. It targets a discerning audience that values the intersection of heritage craftsmanship and modern technology.

The aesthetic leverages **Neomorphism (Soft-UI)** not as a skeuomorphic relic, but as a digital translation of embossed leather and architectural molding. The UI should feel like a physical object—extruding from and receding into the canvas with soft, directional light. Visuals are driven by high-resolution detail photography of hardware, stitching, and leather grains, framed by generous whitespace and rigid structural lines.

## Colors

The palette is anchored in heritage and structural clarity:
- **Deep Burgundy (#4E0B0B):** Used sparingly for high-impact brand moments, primary actions, and sophisticated accents.
- **Tan Leather (#D2B48C):** Represents the tactile nature of the product. Used for secondary interactive elements and decorative architectural lines.
- **Crisp White (#FFFFFF):** The primary surface color, providing a clean, gallery-like backdrop.
- **Off-White/Bone (#F8F5F2):** The background canvas color, essential for creating the "Soft-UI" depth effect where white highlights can pop.

Maintain high contrast between the Deep Burgundy and the light surfaces to ensure an editorial, premium feel.

## Typography

Typography follows a strict hierarchy inspired by luxury editorial magazines. 

**Playfair Display** serves as the primary serif for all headlines. It should be used to convey elegance and history. For the most prestigious "Display" levels, use tighter letter-spacing.

**Metropolis** provides the geometric, architectural balance for body copy and UI labels. It is highly legible and reinforces the "smart" technology aspect of the brand. 

Use **Label-Caps** for category eyebrows, overlines, and small interactive buttons to maintain a structured, organized grid.

## Layout & Spacing

This design system utilizes a **fixed grid** model for desktop to maintain the "Architectural-Chic" structure, transitioning to a fluid model for mobile devices. 

Layouts are governed by a 12-column grid. Emphasize "negative space" as a luxury feature—do not crowd the canvas. Use large section gaps (120px+) to separate product stories. Vertical rhythm is strictly adhered to in 8px increments. 

Elements should often be aligned to a central axis or offset intentionally to mimic architectural blueprints.

## Elevation & Depth

Depth is the defining characteristic of this system. Rather than traditional floating shadows (Material design), we use **Neomorphic Tonal Layers**:

1.  **The Canvas:** The base layer is `#F8F5F2`.
2.  **Extruded Elements:** Created using two shadows: a "Light" shadow (`#FFFFFF`) at -5px -5px and a "Dark" shadow (`#D1CDC7`) at 5px 5px. This creates a soft, embossed look that feels like leather being pressed from behind.
3.  **Recessed Elements:** For input fields or active button states, reverse the shadows to create an "inset" effect, simulating a physical cavity in the material.
4.  **Glass Blurs:** Used exclusively for top navigation bars and product overlays to suggest a modern, high-tech layer over the traditional materials.

## Shapes

The shape language reflects the "Architectural" aspect of the brand. We use **Rounded (Level 2)** settings for primary UI elements to mirror the softened edges of luxury handbags. 

- **Standard Buttons/Cards:** 0.5rem (8px) corner radius.
- **Large Product Containers:** 1rem (16px) corner radius.
- **Iconography:** Icons should feature consistent 1.5px stroke weights with slightly rounded terminals to match the font geometry of Metropolis.

Sharp corners (0px) are reserved only for full-bleed photography containers to anchor the page.

## Components

### Buttons
- **Primary:** Deep Burgundy background, white text. No Neumorphism; high contrast only.
- **Secondary:** Neumorphic "Extruded" style. Same color as the background, using the dual-shadow technique. Text in Deep Burgundy.
- **Tertiary:** Text-only in Tan Leather, uppercase with 0.15em tracking.

### Cards
Cards should not have borders. They are defined by their soft-UI elevation. Product cards use the "Extruded" look with the product image placed inside a slightly "Recessed" inner container to create a "framed" architectural feel.

### Input Fields
Inputs must use the "Recessed" (inner shadow) style to look like they are carved into the interface. Use a 1px Tan Leather focus ring for accessibility.

### Progress Indicators (Smart Features)
Use thin, architectural lines in Tan Leather to show battery life or sync status, blending the smart-handbag tech seamlessly into the chic aesthetic.

### Chips & Tags
Small, pill-shaped elements with a subtle 1px border in Tan Leather. Text in Metropolis Bold, 10px, uppercase.