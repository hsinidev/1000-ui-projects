---
name: Hydro-Clinical Luxury
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#8f9097'
  outline-variant: '#44474c'
  surface-tint: '#bcc7dd'
  primary: '#bcc7dd'
  on-primary: '#263142'
  primary-container: '#051020'
  on-primary-container: '#727d91'
  inverse-primary: '#545f72'
  secondary: '#bdf4ff'
  on-secondary: '#00363d'
  secondary-container: '#00e3fd'
  on-secondary-container: '#00616d'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#0e1011'
  on-tertiary-container: '#7b7c7c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e3fa'
  primary-fixed-dim: '#bcc7dd'
  on-primary-fixed: '#111c2c'
  on-primary-fixed-variant: '#3c475a'
  secondary-fixed: '#9cf0ff'
  secondary-fixed-dim: '#00daf3'
  on-secondary-fixed: '#001f24'
  on-secondary-fixed-variant: '#004f58'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  display-lg:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  title-sm:
    fontFamily: Sora
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-rg:
    fontFamily: Sora
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.03em
  label-caps:
    fontFamily: Sora
    fontSize: 12px
    fontWeight: '600'
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 20px
  margin: 32px
---

## Brand & Style

This design system embodies the intersection of high-end wellness and scientific precision. The brand personality is serene, intelligent, and revitalizing—evoking the sensation of pure water moving through a controlled, high-tech environment.

The aesthetic follows a **Fluid-Modern** approach, blending **Glassmorphism** with a **Clinical-Chic** edge. It prioritizes depth through translucency and motion through organic, liquid-inspired curves. The target audience expects a premium, frictionless experience that feels both medically reliable and aesthetically indulgent. The emotional response should be one of "clarity through hydration"—cooling, calming, and deeply sophisticated.

## Colors

The palette is anchored by **Deep Azure**, used primarily for backgrounds to create a vast, immersive depth. **Glass-Cyan** serves as the high-energy accent, representing mineralization, flow, and active technology. **Crisp White** is reserved for high-priority information and iconography to ensure clinical legibility.

This design system utilizes a "Deep-Sea Dark" mode by default. Gradients should not be static; they must feel fluid, using multi-stop transitions between deep blues and cyan to simulate caustic light patterns found in water. Use translucency (10-30% opacity) for container surfaces to maintain the glassmorphic theme.

## Typography

**Sora** is the sole typeface for this design system, chosen for its geometric clarity and rounded terminals that echo the fluid nature of the brand. To achieve a premium "luxury" feel, generous letter spacing (tracking) is applied to all body and label styles, creating an airy, breathable reading experience.

Headlines should use tighter tracking and heavier weights to command authority, while labels use wide tracking and uppercase transformations to denote a clinical, organized hierarchy. Line heights are intentionally tall to avoid visual clutter and maintain a sense of calm.

## Layout & Spacing

The layout philosophy utilizes a **Fluid Grid** with expansive margins, ensuring the UI never feels cramped or "utilitarian." A baseline 8px rhythm governs all spacing, but the system prioritizes "Safe Zones"—large pockets of negative space that allow the background gradients and glass elements to breathe.

Padding within cards and containers should be generous (min 24px) to emphasize the premium nature of the content. Alignment should be structured but allow for "liquid" offsets, where decorative elements might break the grid slightly to simulate organic flow.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and light-based layering rather than traditional shadows. 

1.  **Backdrop Blurs:** Surfaces should use a high-density background blur (20px to 40px) to simulate thick glass.
2.  **Inner Glows:** Instead of drop shadows, use subtle 1px inner borders (top and left) in a semi-transparent White or Cyan to catch "light."
3.  **Luminescent Depth:** Active elements or "high-elevation" items use a Cyan outer glow (drop shadow with 0 offset and high spread) to appear as if they are internally illuminated.
4.  **Tonal Stacking:** Layers are separated by varying the opacity of the glass surfaces (e.g., Background: 100%, Card Level 1: 15%, Overlays: 25%).

## Shapes

The shape language is characterized by **Soft Liquid Curves**. While the primary roundedness is set to Level 2 (0.5rem base), containers and large cards should utilize "Super-ellipses" (squircular corners) where possible to feel more organic. 

Interactive elements like buttons and chips should transition toward Level 3 (Pill-shaped) to represent the smooth, eroded surface of a river stone. Icons should feature rounded caps and junctions to maintain the fluid aesthetic. Avoid sharp 90-degree angles entirely.

## Components

### Transparent Cards
The signature component of this design system. Cards must feature a 1px "silk" border (white at 10% opacity) and a heavy backdrop blur. Content inside should be strictly aligned with generous padding.

### Glowing Status Indicators
Status indicators are not just dots; they are soft, pulsing radial gradients. A "Ready" state uses a Cyan glow, while "Processing" utilizes a slow, rotating liquid gradient.

### Sleek Sliders
Trackers for mineralization or pressure levels use a "hollow" track with a glowing, pill-shaped thumb. The track fills with a Glass-Cyan gradient as the user interacts, simulating a tube filling with water.

### Input Fields
Inputs are bottom-bordered only or encased in ultra-subtle glass containers. The focus state triggers a soft Cyan "aura" around the entire field.

### Fluid Buttons
Primary actions are pill-shaped with a vibrant Glass-Cyan fill. On hover, the button should exhibit a "liquid ripple" effect or a slight expansion of its inner glow. Secondary actions use the ghost-glass style with white text.