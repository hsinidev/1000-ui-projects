---
name: OrthoAlign
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3a4a49'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6a7a7a'
  outline-variant: '#b9cac9'
  surface-tint: '#006a6a'
  primary: '#006a6a'
  on-primary: '#ffffff'
  primary-container: '#00ffff'
  on-primary-container: '#007272'
  inverse-primary: '#00dddd'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#e4e6e8'
  on-tertiary-container: '#646769'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#00fbfb'
  primary-fixed-dim: '#00dddd'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  container-max: 1280px
  gutter: 24px
  margin: 40px
  section-gap: 80px
---

## Brand & Style

This design system embodies the intersection of medical precision and futuristic luxury. The brand personality is transformative, positioning orthodontic care not just as a health service, but as a high-tech cosmetic evolution. 

The aesthetic style is **Glassmorphism** combined with **Minimalism**. The interface should feel like a high-end medical HUD (Heads-Up Display)—airy, luminous, and pristine. By utilizing translucent layers and frosted glass effects, the UI achieves a sense of depth and clinical cleanliness. The emotional response is one of absolute confidence, cutting-edge innovation, and "clean-room" perfection.

## Colors

The palette is anchored by **Glossy White**, serving as the clinical foundation. **Electric Cyan** is reserved exclusively for primary actions, progress indicators, and high-tech accents to symbolize energy and precision. 

- **Primary:** Electric Cyan (#00FFFF) — Used for critical CTAs and active states.
- **Secondary:** Slate (#334155) — Used for high-contrast typography and icon outlines to ensure legibility.
- **Base:** White (#FFFFFF) — The primary background and surface color.
- **Accent Glow:** A semi-transparent version of Electric Cyan (alpha 20%) used for subtle outer glows.
- **Glass Stroke:** A highly transparent white (#FFFFFF at 40% opacity) used for the edges of glassmorphic containers.

## Typography

This design system utilizes a dual-font strategy to balance futuristic character with clinical readability.

**Space Grotesk** is used for headings and labels. Its geometric, technical construction evokes a "Digital-First" feel. To enhance the premium aesthetic, wide tracking (letter-spacing) is applied to all headlines.

**Inter** is used for all body text and data-heavy interfaces. Its neutral, systematic nature ensures that complex orthodontic information remains highly legible and professional. Large blocks of text should maintain generous line heights to preserve the airy, minimalist feel.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model within a 1280px container, utilizing a 12-column system. The spacing rhythm is strictly based on 8px increments to reinforce the brand's core value of "precision."

Generous white space (margins and section gaps) is mandatory to prevent the UI from feeling "crowded" or "medicalized" in a traditional, cluttered sense. Elements should feel as though they are floating within a structured, clinical environment.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Subtle Glow Shadows**. 

1. **Surface Layers:** The primary background is Glossy White. Content containers use a backdrop-filter (blur: 12px) with a semi-transparent white fill (opacity 60-80%).
2. **Borders:** Every glass container must have a 1px solid border using the "Glass Stroke" (White at 40% opacity) to catch the "light" and define the edges.
3. **Shadows:** Avoid traditional black shadows. Use "Cyan Glows" for active states—a very soft, diffused outer glow (#00FFFF at 15% opacity, 20px blur) to make elements appear self-illuminated.
4. **Z-Axis:** Higher elevation elements receive more intense background blurs rather than darker shadows.

## Shapes

The shape language is **Rounded**, utilizing a 0.5rem base radius. This softens the "clinical" nature of the product, making the futuristic technology feel approachable and organic, like high-end dental aligners. 

Icons should be "High-Gloss"—utilizing 2px stroke weights with rounded terminals and subtle gradient fills or inner highlights to mimic the appearance of glass or polished resin.

## Components

- **Buttons:** Primary buttons are solid Electric Cyan with high-contrast Slate text. They feature a subtle top-down white gradient (5% opacity) to create a "glossy" finish. Hover states trigger the Cyan Glow effect.
- **Cards:** Use the Glassmorphism effect—frosted background, white border, and significant internal padding (24px+).
- **Inputs:** Clean, white backgrounds with a 1px Slate border at low opacity (20%). On focus, the border transitions to Electric Cyan with a soft glow.
- **Chips/Badges:** Pill-shaped with a faint Electric Cyan tint background and Space Grotesk labels in uppercase.
- **Progress Indicators:** Use glowing Cyan lines or circular "halo" loaders to represent treatment progress.
- **Treatment Visualizers:** Specialized components featuring 3D-render containers with high-transparency backgrounds, allowing the "glossy" dental models to be the focal point.