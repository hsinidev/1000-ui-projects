---
name: Executive Tech-Luxury
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#c6c6cb'
  on-secondary: '#2f3034'
  secondary-container: '#46464b'
  on-secondary-container: '#b5b4ba'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#1d1f1f'
  on-tertiary-container: '#858687'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display:
    fontFamily: Hanken Grotesk
    fontSize: 42px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 22px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
  data-mono:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  base: 8px
  container-padding: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 48px
---

## Brand & Style

The design system is engineered for a high-performance, executive audience that values the intersection of horology and technical apparel. It conveys a sense of "precision-machined luxury," emphasizing reliability, sophistication, and futuristic utility. 

The visual style is **Minimalist and Tech-Forward**, leaning heavily into architectural precision. It avoids soft, organic shapes in favor of sharp lines and structural integrity. Subtle metallic gradients are used to evoke the feel of brushed steel hardware, while the deep navy foundation provides a grounding, professional atmosphere. This design system communicates that the product is not just a garment, but a sophisticated piece of integrated technology.

## Colors

The palette of this design system is rooted in a high-contrast, "Executive Dark" mode.

- **Deep Navy Blue (#001F3F):** The primary structural color, used for large surfaces and backgrounds to provide a professional, authoritative depth.
- **Brushed Steel (#8E8E93):** Used for interactive elements, borders, and accents. This color should often be applied as a linear gradient (45-degree angle) to simulate light reflecting off a metallic surface.
- **Crisp White (#FFFFFF):** Reserved for primary typography and critical data points to ensure maximum legibility against the dark background.
- **Surface Neutrals:** Use #1A1A1A for container backgrounds to create subtle separation from the #001F3F base.

Avoid vibrant accent colors; use opacity and metallic texture to indicate hierarchy instead.

## Typography

This design system utilizes **Hanken Grotesk** for its sharp, architectural qualities and exceptional legibility on mobile screens. 

The typographic hierarchy is strictly grid-bound. Display and headline styles use tight letter spacing and heavier weights to evoke the "bold" presence of a premium watch face. Labels are predominantly uppercase with expanded letter spacing to act as technical annotations. All data visualizations or "smart" metrics should use the `data-mono` style to emphasize the technical nature of the apparel.

## Layout & Spacing

This design system employs a **Strict 8px Grid System** to maintain architectural alignment. On mobile, the layout uses a 4-column fluid grid with 24px outer margins and 16px gutters.

Elements are aligned with mathematical precision. Negative space is not "empty" but is used as a deliberate structural tool to separate technical data from lifestyle content. Vertical stacks should strictly follow the 8px base (8, 16, 24, 32, 48). All containers and cards should stretch to the full width of the grid columns to reinforce the horizontal and vertical axes.

## Elevation & Depth

Hierarchy in this design system is established through **Low-Contrast Outlines and Metallic Gradients** rather than traditional shadows.

- **Borders:** Use 1px "Hairline" borders in #8E8E93 (at 40-60% opacity) to define surfaces.
- **Tonal Layering:** Depth is achieved by placing #1A1A1A surfaces over the #001F3F background. 
- **The "Steel" Effect:** Interactive surfaces use a subtle linear gradient from #8E8E93 to #BFC0C4 to create a 2D-extruded appearance.
- **Glassmorphism:** Use very sparingly for top navigation bars or floating action overlays—apply a heavy backdrop blur (20px) with a subtle #FFFFFF 10% tint to simulate high-end watch crystals.

## Shapes

The shape language of this design system is **Sharp (0px)**. 

To reflect the precision of watchmaking and architectural drafting, all buttons, cards, and input fields feature 90-degree corners. The only exception to this rule is for purely circular elements that mimic watch faces or biometric sensors. This lack of roundedness reinforces the professional, high-end technical aesthetic and differentiates the brand from softer, consumer-grade wearables.

## Components

- **Buttons:** High-contrast blocks. Primary buttons feature the "Brushed Steel" gradient with #001F3F text. Secondary buttons are transparent with a 1px steel border and white text.
- **Cards:** Defined by a 1px border. Backgrounds are either transparent (outlined) or #1A1A1A. No shadows; separation is achieved via the border's interaction with the grid.
- **Input Fields:** Minimalist underlines or 1px sharp boxes. Labels use the `label-caps` style and are placed strictly above the input.
- **Chips/Status:** Rectangular and sharp. Use #FFFFFF text on #8E8E93 backgrounds.
- **Biometric Gauges:** Thin-line circular indicators that reflect the UI of a luxury smart watch. Lines should be exactly 1px or 2px thick.
- **The "Thread" Progress Bar:** A unique component for this design system, representing the watch-apparel sync. It should be a 2px horizontal line with a metallic steel "glow" for the active state.