---
name: Hydro-Tech Design System
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434656'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004dea'
  primary: '#0041c8'
  on-primary: '#ffffff'
  primary-container: '#0055ff'
  on-primary-container: '#e3e6ff'
  inverse-primary: '#b6c4ff'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#00576c'
  on-tertiary: '#ffffff'
  tertiary-container: '#00718b'
  on-tertiary-container: '#c4eeff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#001551'
  on-primary-fixed-variant: '#0039b3'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#b7eaff'
  tertiary-fixed-dim: '#4cd6ff'
  on-tertiary-fixed: '#001f28'
  on-tertiary-fixed-variant: '#004e60'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system centers on the intersection of clinical precision and the organic fluidity of water. It evokes the feeling of a high-end, futuristic laboratory—clean, sterile, yet approachable and life-giving. The target audience includes health-conscious consumers and technical professionals who value purity and scientific validation. 

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes expansive white space to denote cleanliness, while employing translucent, frosted layers to simulate the refractive properties of water and glass. The UI should feel lightweight, as if the elements are suspended in a clear liquid medium, ensuring every interaction feels high-tech and surgically precise.

## Colors

The palette is anchored by **Medical Blue**, used for critical data and primary actions to instill confidence and authority. **Glass-Cyan** serves as the primary accent for translucent backgrounds and decorative "liquid" elements, creating a sense of hydration and freshness. 

**Pure White** is the foundational canvas, ensuring the "clinical" aesthetic is maintained. Gradients should be subtle, transitioning from Medical Blue to a lighter cyan to mimic the movement of light through water. Use high-contrast ratios for text to ensure medical-grade legibility against semi-transparent backgrounds.

## Typography

This design system utilizes **Space Grotesk** for headlines to provide a technical, geometric edge that reflects scientific innovation. Its slightly unconventional letterforms suggest a "cutting-edge" personality. 

For body copy and functional labels, **Manrope** provides a balanced and highly readable counterpoint. It maintains the modern aesthetic while ensuring that complex technical data—such as mineral levels and filtration status—is easily digestible. Labels should often use uppercase styling with increased letter spacing to mimic laboratory equipment markings.

## Layout & Spacing

The layout follows a **fluid grid** model with generous margins to create a "breathable" atmosphere. Avoid crowding elements; the spatial rhythm should prioritize clarity and ease of focus. 

A 12-column system is recommended for desktop, while mobile layouts should rely on 4 columns with substantial vertical padding. Use "Safe Zones" around data visualizations to ensure they remain the focal point. Spacing should be used to group related technical metrics, while larger gaps (48px+) should be used to separate distinct functional modules.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and tonal layering rather than traditional heavy shadows. Surfaces should use a backdrop blur (12px to 20px) and a semi-transparent white fill (opacity 40-70%) to create a frosted glass effect.

To define hierarchy:
- **Level 1 (Base):** Pure white background.
- **Level 2 (Containers):** Glass-Cyan or White with 60% opacity and a subtle 1px inner border in Medical Blue (10% opacity).
- **Level 3 (Pop-overs/Modals):** High-blur glass surfaces with a very soft, diffused ambient shadow (Color: Medical Blue, Opacity: 5%, Blur: 30px) to suggest floatation.

## Shapes

The shape language uses **Rounded (0.5rem)** corners as a baseline to maintain a fluid, water-like quality. However, to preserve the "clinical" feel, certain technical elements like data charts or input fields should utilize smaller radii to appear more "tooled" and precise.

Interactive elements like primary buttons should lean toward the larger end of the scale (1rem) to feel approachable, while status indicators and mineral icons should be perfect circles to represent molecular structures.

## Components

### Buttons & Controls
Primary buttons should feature a subtle "liquid" gradient (Medical Blue to Tertiary Blue) with a slight inner glow. Secondary buttons are "Ghost" style with a 1px Medical Blue border. All interactive states should include a soft transition that mimics the surface tension of water.

### Input Fields
Fields must feel "medical-grade." Use a Pure White background with a crisp 1px border. On focus, the border should glow with a soft Cyan pulse. Typography inside inputs must be monospaced or highly geometric to emphasize data accuracy.

### Cards & Modules
Use glassmorphism for all container elements. Cards should have a "frost" effect that blurs the content behind them. Use thin, light-blue hairlines to separate sections within a card rather than heavy dividers.

### Data Visualizations
Progress bars for filtration or mineral levels should use "liquid" fills—gradients that appear to have a slight wave or shimmer. Use circular gauges with thin strokes to represent laboratory dials.

### Status Indicators
Use pulsing glows for "Active" states. A "Purifying" state might feature a slow, vertical blue gradient animation, while an "Alert" state should use a sharp, high-contrast clinical red that breaks the blue/cyan harmony to demand immediate attention.