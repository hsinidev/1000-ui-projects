---
name: Luminous Beauty
colors:
  surface: '#fff8f4'
  surface-dim: '#e1d8d2'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2eb'
  surface-container: '#f5ece5'
  surface-container-high: '#f0e7df'
  surface-container-highest: '#eae1da'
  on-surface: '#1f1b17'
  on-surface-variant: '#4d4635'
  inverse-surface: '#34302b'
  inverse-on-surface: '#f8efe8'
  outline: '#7f7663'
  outline-variant: '#d0c5af'
  surface-tint: '#735c00'
  primary: '#735c00'
  on-primary: '#ffffff'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#e9c349'
  secondary: '#6b5a5f'
  on-secondary: '#ffffff'
  secondary-container: '#f4dde3'
  on-secondary-container: '#716065'
  tertiary: '#5e5e5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#b4b3af'
  on-tertiary-container: '#454543'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#f4dde3'
  secondary-fixed-dim: '#d7c1c7'
  on-secondary-fixed: '#24181c'
  on-secondary-fixed-variant: '#524348'
  tertiary-fixed: '#e4e2de'
  tertiary-fixed-dim: '#c8c6c3'
  on-tertiary-fixed: '#1b1c1a'
  on-tertiary-fixed-variant: '#474744'
  background: '#fff8f4'
  on-background: '#1f1b17'
  surface-variant: '#eae1da'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
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
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

The design system is centered on the concept of "Effortless Radiance." It targets a discerning, luxury-oriented audience seeking high-end skincare and cosmetics. The aesthetic response should be one of serenity, purity, and clinical prestige. 

The style utilizes a sophisticated **Minimalism** blended with **Glassmorphism**. By using heavy whitespace and high-contrast typography, the design system creates a gallery-like experience where products are treated as art. Visual interest is maintained through pearlescent surface treatments—using extremely subtle, multi-stop radial gradients—that mimic the reflective properties of healthy skin and premium packaging.

## Colors

The palette is anchored in a collection of "Warm Whites" and "Soft Blushes" to create a glowing atmosphere.
- **Primary (Champagne Gold):** Used sparingly for high-value actions, logos, and premium accents. It should feel metallic but soft, never brassy.
- **Secondary (Soft Blush):** Employed for subtle backgrounds, secondary buttons, and decorative elements to add warmth and a human touch.
- **Tertiary (Warm White):** The foundational surface color, providing a more inviting and premium feel than a clinical pure white.
- **Neutral (Deep Taupe):** Used for typography and iconography to maintain readability without the harshness of pure black.
- **Pearlescent Gradients:** A signature treatment for hero sections and card surfaces, utilizing very low-opacity washes of pink and gold to create "luminosity."

## Typography

This design system uses a high-contrast typographic pairing to balance heritage and modern utility.
- **Noto Serif:** Reserved for headlines and editorial callouts. It evokes a sense of timeless elegance and editorial authority. Use "display-lg" for hero moments with tight line heights and slight negative letter spacing.
- **Manrope:** A modern, balanced sans-serif used for all functional UI components, body copy, and labels. Its clean geometry ensures maximum legibility for product descriptions and ingredients. 
- **Hierarchy:** Use "label-caps" for product categories and small eyebrow text to introduce sections, creating a structured, organized feel.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with an emphasis on "negative space as a luxury." 
- **Grid:** A 12-column grid system is used for desktop, but elements frequently span centered columns (e.g., 6 or 8 columns) to increase the surrounding whitespace.
- **Rhythm:** An 8px base unit drives all spacing. 
- **Vertical Spacing:** Generous "section-gaps" (up to 120px) are used to separate brand stories from product listings, preventing the UI from feeling cluttered or "discount-driven."
- **Margins:** Oversized desktop margins (64px) frame the content, making the browser window feel like a high-end magazine spread.

## Elevation & Depth

To maintain the "Luminous" theme, the design system rejects heavy, dark shadows in favor of **Ambient Shadows** and **Tonal Layers**.
- **Shadows:** When necessary, use extremely diffused, low-opacity shadows tinted with the primary Champagne Gold or a soft Blush hue. This prevents the "dirty" look of gray shadows on warm surfaces.
- **Glassmorphism:** Use backdrop blurs (20px-40px) on navigation bars and floating modals. Overlay these with a subtle white border (0.5px at 20% opacity) to create a "etched glass" effect.
- **Layering:** Hierarchy is primarily established through color shifts—from a Warm White background to a Pearlescent surface—rather than physical height.

## Shapes

The design system adopts a **Soft** shape language. 
- **Corner Radii:** A consistent 0.25rem (4px) radius is applied to buttons, input fields, and small UI elements to maintain a precise, professional look that isn't overly organic or "bubbly."
- **Product Imagery:** Large-scale product photography may use slightly larger radii (rounded-lg) to soften the visuals against the structured grid.
- **Dividers:** Use extremely thin (0.5pt), low-contrast lines to separate sections without breaking the visual flow.

## Components

- **Buttons:** Primary buttons use a solid Champagne Gold background with white text or a sophisticated "Outline" style with 1px gold borders. Hover states should include a subtle pearlescent shimmer.
- **Inputs:** Clean, bottom-border-only fields or very light-tinted blush backgrounds. Focus states should be indicated by a weight increase in the bottom border or a soft gold glow.
- **Cards:** Product cards utilize a "No Border" style, relying on high-quality photography and generous internal padding. On hover, a subtle pearlescent background or soft ambient shadow may appear.
- **Chips/Filters:** Use the "Pill-shaped" variant with a Soft Blush background and Taupe text for a delicate, accessible filtering experience.
- **Specialty Components:** 
    - **Ingredient Modals:** Utilizing glassmorphism to overlay detailed scientific info without losing the context of the product page.
    - **Luminosity Slider:** A custom UI element for color-matching foundations, featuring a smooth gradient track.
    - **Floating Cart:** A translucent, blurred panel that slides from the right, maintaining the sense of depth and luxury.