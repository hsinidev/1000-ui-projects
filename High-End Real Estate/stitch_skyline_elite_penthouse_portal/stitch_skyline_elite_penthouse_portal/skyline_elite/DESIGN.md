---
name: Skyline Elite
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dcdddd'
  on-secondary-container: '#5f6161'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1b1a'
  on-tertiary-container: '#868382'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e6e2df'
  tertiary-fixed-dim: '#cac6c4'
  on-tertiary-fixed: '#1c1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  display-xl:
    fontFamily: notoSerif
    fontSize: 72px
    fontWeight: '400'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 32px
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 28px
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

The brand personality of this design system is defined by architectural precision, quiet confidence, and an uncompromising dedication to exclusivity. It targets ultra-high-net-worth individuals who value discretion, craftsmanship, and timeless elegance over fleeting trends. The UI is designed to evoke a sense of serenity and "digital quietude," allowing the architectural marvels of the penthouses to take center stage.

The design style is **Minimalist-Luxe**. It draws heavily from modern architectural minimalism—utilizing vast expanses of whitespace to create a "gallery-like" experience. High contrast is used strategically to guide the eye, while premium textures (simulated via subtle gradients and high-quality imagery) provide a tactile feel to the digital interface. This design system avoids unnecessary ornamentation, ensuring every line, font choice, and margin serves a structural purpose.

## Colors

This design system utilizes a high-contrast, monochromatic-led palette to establish a sophisticated atmosphere. 

- **Deep Charcoal (#1A1A1A):** Used for typography, structural borders, and primary CTA backgrounds. It provides the grounding weight required for a premium feel.
- **Marble White (#F5F5F5):** The primary canvas. This off-white shade reduces eye strain compared to pure white while maintaining a crisp, clean aesthetic.
- **Accents of Gold (#D4AF37):** Reserved exclusively for high-value interactions, status indicators, or subtle navigational highlights. It must be used sparingly to maintain its perceived value.
- **Muted Grays:** Used for secondary text and subtle dividers to ensure the hierarchy remains clear without cluttering the visual field.

## Typography

The typography in this design system creates a tension between traditional luxury and modern efficiency. 

**Noto Serif** is the authoritative voice of the system, used for large headlines and display text. Its elegant serifs provide a literary and sophisticated quality. For body copy and functional elements, **Manrope** is used for its geometric clarity and superior readability at smaller scales.

Key typographic rules:
- **Generous Leading:** Line heights are intentionally wide to promote a relaxed reading pace.
- **Letter Spacing:** Labels and small headers use increased letter spacing and all-caps styling to denote "specifications" or "metadata."
- **Optical Sizing:** Display styles use tighter letter spacing to maintain visual impact on large screens.

## Layout & Spacing

This design system follows a **Fixed Grid** philosophy for desktop layouts, centering content within a 1440px container to ensure a consistent, curated viewing experience on ultra-wide displays. 

The spacing rhythm is built on an 8px base unit, but emphasizes "The Big Gap"—intentionally large vertical margins between sections (128px+) to prevent the user from feeling rushed. Elements are organized on a 12-column grid with wide 32px gutters, allowing for asymmetrical compositions that mirror high-end editorial magazines. Imagery should frequently break the grid or span full-bleed to emphasize the scale of the properties.

## Elevation & Depth

To maintain a minimalist-luxe aesthetic, this design system avoids heavy shadows. Instead, it utilizes **Tonal Layers** and **Low-Contrast Outlines**.

- **Depth through Layering:** Higher-order elements (like modal windows or property details) use the Marble White background with an ultra-subtle, 1px Deep Charcoal border at 10% opacity.
- **Ambient Shadows:** When depth is required (e.g., on primary floating buttons), use an extremely diffused shadow: `0px 20px 40px rgba(0, 0, 0, 0.05)`. The goal is for the shadow to be felt rather than seen.
- **Glassmorphism:** Sub-navigation menus or image overlays use a light backdrop blur (20px) with a semi-transparent Deep Charcoal or Marble White fill to create a sense of physical transparency and material quality.

## Shapes

The shape language of this design system is **Sharp**. UI elements utilize 0px roundedness to reflect the clean lines and hard edges of modern penthouse architecture. 

Buttons, input fields, and image containers must maintain 90-degree angles. This severity reinforces the "Elite" brand positioning, distinguishing the portal from more "friendly" or "consumer-grade" platforms that use rounded corners. The only exception is for circular icon containers or decorative elements that require a perfect geometric contrast to the rectangular grid.

## Components

### Buttons
- **Primary:** Solid Deep Charcoal background with Marble White text. Sharp edges. No hover scale, only a subtle opacity shift or a Gold bottom-border transition.
- **Secondary/Ghost:** 1px Deep Charcoal border with transparent background.
- **CTA Label:** All-caps Manrope with 0.15em letter spacing.

### Input Fields
- **Style:** Underlined fields are preferred over boxed fields to maintain horizontal flow.
- **Focus State:** The bottom border transitions from Light Gray to Gold.

### Cards
- **Property Cards:** Large-scale imagery with text overlays. Titles in Noto Serif. Use a "reveal on hover" animation for specifications (sq ft, beds, baths) to keep the initial view uncluttered.

### Lists & Tables
- **Specification Lists:** Used for property details. High vertical padding (16px+) between rows. 1px hairline dividers in Light Gray.

### Additional Components
- **Image Gallery:** A full-screen, horizontal-scroll component with a minimal progress indicator at the bottom.
- **Inquiry Overlay:** A sleek, right-aligned drawer for lead capture, utilizing the backdrop blur effect to keep the property visible in the background.