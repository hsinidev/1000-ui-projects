---
name: Aura-Couture
colors:
  surface: '#fdf9f4'
  surface-dim: '#ddd9d5'
  surface-bright: '#fdf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3ee'
  surface-container: '#f1ede8'
  surface-container-high: '#ebe8e3'
  surface-container-highest: '#e6e2dd'
  on-surface: '#1c1c19'
  on-surface-variant: '#4d4635'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f4f0eb'
  outline: '#7f7663'
  outline-variant: '#d0c5af'
  surface-tint: '#735c00'
  primary: '#735c00'
  on-primary: '#ffffff'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#e9c349'
  secondary: '#5d5e63'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfe4'
  on-secondary-container: '#626267'
  tertiary: '#5f5e5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#b4b2b2'
  on-tertiary-container: '#454544'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#fdf9f4'
  on-background: '#1c1c19'
  surface-variant: '#e6e2dd'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: notoSerif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-md:
    fontFamily: notoSerif
    fontSize: 22px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.03em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 24px
  gutter: 16px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
---

## Brand & Style

The design system is anchored in the concept of "Digital Atelier"—a digital space that feels as personal and refined as a physical high-end tailoring house. It serves an audience that values craftsmanship, exclusivity, and precision. The emotional response is one of calm assurance and effortless luxury.

The style is a fusion of **Minimalism** and **Tactile** design. It utilizes heavy whitespace to allow high-resolution imagery of fabrics and garments to breathe, while employing subtle physical metaphors—such as textures that mimic fine stationery or the soft "give" of premium textiles—to create a sensory experience. The interface is intentionally quiet, allowing the service and the product to remain the focal point.

## Colors

The palette is rooted in the "Silk Cream" neutral, which replaces standard whites to provide a warmer, more expensive foundation. "Gold" is used sparingly as a signature accent for primary calls-to-action and brand flourishes, signifying value and quality. "Soft Grey" provides a sophisticated mid-tone for secondary text and decorative borders. 

A deep charcoal (#1A1A1A) is introduced for high-contrast typography to ensure readability without the harshness of pure black. Backgrounds should primarily utilize the Silk Cream, with occasional Soft Grey sections to create subtle tonal shifts between content blocks.

## Typography

Typography in this design system relies on the interplay between the timeless elegance of **notoSerif** and the functional clarity of **inter**. Headlines should be treated with editorial care, utilizing tighter letter-spacing and generous line-heights to evoke the feel of a luxury fashion lookbook.

Labels and interactive elements use Inter with increased letter-spacing and uppercase styling to provide a modern, service-driven aesthetic. Priority is given to legibility on mobile devices, ensuring that even at smaller scales, the information remains clear and sophisticated.

## Layout & Spacing

The layout philosophy follows a **fixed-width adaptive** approach for mobile, centered within the viewport. To maintain an air of exclusivity, this design system mandates generous margins (24px) that prevent content from feeling crowded. 

The rhythm is dictated by an 8px base unit. Vertical spacing is intentionally "loose"—using the `stack-xl` (64px) unit between major sections to emphasize the luxury of space. Grids for product listings should use a 2-column format on mobile to allow for large, high-detail imagery, emphasizing the tactile nature of the garments.

## Elevation & Depth

Hierarchy is established through **tonal layers** and **ambient shadows** rather than heavy stylistic effects. 
- **Surface Elevation:** Primary content sits on the Silk Cream background. Elevated elements (like floating cards or action sheets) use a slightly lighter tint of Silk Cream or pure White with a very soft, diffused shadow (15% opacity of the Secondary color, 20px blur, 4px offset).
- **Depth Metaphor:** Navigation bars and sticky headers should use a high-blur backdrop filter (glassmorphism) with 95% opacity to maintain a sense of depth while scrolling.
- **Interactions:** Hover or active states use a subtle inner-shadow to simulate a "pressed fabric" effect, reinforcing the tailoring theme.

## Shapes

The shape language is **Soft**, striking a balance between the precision of a needle and the softness of the fabric. Primary containers and buttons utilize a 0.25rem (4px) radius. This minimal rounding maintains a high-fashion, structured silhouette while appearing more approachable than sharp 90-degree corners. 

Image containers for fabric swatches and model photography should follow this same rounding logic to ensure a cohesive, curated aesthetic across the mobile experience.

## Components

- **Buttons:** Primary buttons are solid Gold with Charcoal text. Secondary buttons are outlined in Soft Grey with a thin 1px stroke. All buttons use the Label-LG typography.
- **Inputs:** Text fields use a "minimalist underline" or a very light Silk Cream fill with a Soft Grey bottom-border only, mimicking bespoke measurement forms.
- **Cards:** Product and service cards use a 1px Soft Grey border with no shadow in their default state. On interaction, they transition to a soft ambient shadow.
- **Icons:** Use thin-line vector icons (1pt stroke weight). Gold is used only for "active" icon states or specific decorative elements like a "certified tailor" badge.
- **Progress Indicators:** For the tailoring process (Step 1, 2, 3), use a thin horizontal line with Gold highlights, avoiding heavy circular pips for a more streamlined look.
- **Fabric Swatches:** A specialized component—circular or soft-square thumbnails that include a subtle "zoom" interaction to emphasize texture.