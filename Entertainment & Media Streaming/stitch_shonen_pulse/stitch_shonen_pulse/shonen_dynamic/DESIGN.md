---
name: Shonen Dynamic
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e7bdb2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#ad887e'
  outline-variant: '#5d4038'
  surface-tint: '#ffb5a0'
  primary: '#ffb5a0'
  on-primary: '#601400'
  primary-container: '#ff5625'
  on-primary-container: '#541100'
  inverse-primary: '#b12d00'
  secondary: '#8bd5ff'
  on-secondary: '#003549'
  secondary-container: '#00bdfd'
  on-secondary-container: '#004964'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#909191'
  on-tertiary-container: '#282a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a0'
  on-primary-fixed: '#3b0900'
  on-primary-fixed-variant: '#872000'
  secondary-fixed: '#c3e8ff'
  secondary-fixed-dim: '#7ad0ff'
  on-secondary-fixed: '#001e2c'
  on-secondary-fixed-variant: '#004c69'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-hero:
    fontFamily: Epilogue
    fontSize: 72px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Spline Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Spline Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  xxl: 80px
---

## Brand & Style

This design system captures the kinetic energy and high-stakes drama of Shonen action manga and anime. The brand personality is explosive, heroic, and unapologetically bold, targeting an audience that thrives on intensity and visual spectacle. 

The design style is a fusion of **Neo-Brutalism** and **High-Contrast Bold**. It utilizes heavy outlines, aggressive angles, and halftone textures to mimic the print quality of manga, while layering in "electric" digital effects like neon glows and chromatic aberration on hover states. The emotional response is one of hype and momentum—every interaction should feel like a "power-up."

## Colors

The palette is optimized for a cinematic, dark-mode-first viewing experience. The foundation is built on **Deep Charcoal (#121212)** for primary surfaces and **Slate (#1A1A1A)** for secondary containers, providing a high-contrast stage for the accent colors.

**Shonen Orange (#FF4500)** is the primary action color, used for critical CTAs and "heat" moments. **Spirit Blue (#00BFFF)** serves as the secondary accent for energy-based UI elements, progress bars, and metadata highlights. White is used sparingly for maximum legibility against the dark void. All interactive accents should utilize a subtle outer glow to simulate an "aura" effect.

## Typography

The typography system relies on extreme weight and posture to convey movement. Headlines use **Epilogue** at its heaviest weight, forced into a slanted/italic style to mimic the speed lines found in manga panels. 

**Spline Sans** provides a clean, modern contrast for long-form content and descriptions, ensuring readability is not sacrificed for style. For technical data, tags, and navigation labels, **Space Grotesk** adds a slightly futuristic, geometric edge that complements the angular UI components.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop, transitioning to a fluid layout for mobile. A 12-column grid with generous 24px gutters allows for asymmetrical "manga-panel" style layouts. 

Spacing should feel intentional and rhythmic, using a 4px base unit. To break the monotony of standard streaming grids, elements are encouraged to slightly overlap or use "break-out" positioning, where character art or specific cards extend beyond their containers to create depth and visual excitement.

## Elevation & Depth

Depth is achieved through **Bold Borders** and **Tonal Layering** rather than traditional soft shadows. 

1.  **Surfaces:** Use #1A1A1A for cards and #222222 for elevated states.
2.  **Borders:** All primary containers must feature a 2px or 3px solid border in Shonen Orange or Spirit Blue. 
3.  **Halftones:** Apply a subtle SVG halftone dot pattern (10% opacity) to background surfaces to provide tactile "ink-on-paper" texture.
4.  **Electric Glows:** Instead of drop shadows, use `box-shadow` with 0px blur and a hard offset for a "sticker" look, or a vibrant neon glow (`0px 0px 15px`) for active/hovered elements to simulate energy.

## Shapes

The shape language is strictly **Sharp (0px)**. To evoke the aggressive nature of Shonen battle scenes, UI elements avoid rounded corners entirely. 

Use clipped corners (dog-eared) at 45-degree angles for buttons and tags to reinforce the "angular" and "sharp" aesthetic. This geometric rigidity ensures that the platform feels high-energy and dangerous, standing out against the typical soft-rounded edges of modern streaming services.

## Components

### Buttons
Primary buttons are solid Shonen Orange with heavy 3px black internal borders. On hover, they shift to Spirit Blue with a "glitch" transition effect and a vibrant outer glow. Text is always uppercase and slanted.

### Cards (Manga Panels)
Anime title cards should resemble manga panels, featuring high-contrast borders. When hovered, the card should scale slightly and the border color should "flash" or pulse with an electric blue aura.

### Chips & Tags
Use Spirit Blue backgrounds with black text for genre tags. Shapes should be octagonal or feature sharp, clipped corners rather than pills.

### Inputs & Forms
Input fields use a Deep Charcoal background with a 2px Slate border. Upon focus, the border "ignites" into Shonen Orange.

### Transitions
Motion should be snappy and "step-based" (60ms - 100ms) rather than slow and fluid. Use "impact" animations—where elements bounce slightly upon appearing—to mimic the force of a physical landing.