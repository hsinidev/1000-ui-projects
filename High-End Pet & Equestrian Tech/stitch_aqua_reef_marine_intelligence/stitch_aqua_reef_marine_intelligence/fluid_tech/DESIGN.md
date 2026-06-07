---
name: Fluid-Tech
colors:
  surface: '#08151c'
  surface-dim: '#08151c'
  surface-bright: '#2e3b42'
  surface-container-lowest: '#031016'
  surface-container-low: '#101d24'
  surface-container: '#142128'
  surface-container-high: '#1f2c33'
  surface-container-highest: '#29373e'
  on-surface: '#d6e5ee'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#d6e5ee'
  inverse-on-surface: '#253239'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#b1c9e2'
  on-secondary: '#1a3246'
  secondary-container: '#31495e'
  on-secondary-container: '#9fb8d1'
  tertiary: '#f8f8f8'
  on-tertiary: '#303030'
  tertiary-container: '#dbdbdb'
  on-tertiary-container: '#606060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#cde5ff'
  secondary-fixed-dim: '#b1c9e2'
  on-secondary-fixed: '#021d30'
  on-secondary-fixed-variant: '#31495e'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#08151c'
  on-background: '#d6e5ee'
  surface-variant: '#29373e'
typography:
  display-xl:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  element-gap-sm: 8px
  element-gap-md: 16px
  element-gap-lg: 32px
---

## Brand & Style
This design system embodies "Submersive Intelligence"—a bridge between the raw, organic depths of the ocean and the crystalline precision of advanced marine science. The brand personality is authoritative and ultra-premium, targeting high-end aquarium enthusiasts and professional marine researchers. 

The visual style is a specialized execution of **Glassmorphism**, treated with "Liquid Tech" metaphors. UI elements should appear as though they are high-tech HUD overlays suspended in deep water. High-contrast neon accents provide "bioluminescent" functional cues against a dark, abyssal backdrop, ensuring the interface feels both immersive and highly legible under varied lighting conditions.

## Colors
The palette is rooted in the "Abyssal Spectrum." **Deep Sea Blue (#001B2E)** serves as the primary container and surface color, providing a sense of volume and depth. **Pure Black (#000000)** is used for the deepest background layers to create infinite contrast. 

**Neon Cyan (#00F2FF)** is the "Bioluminescent" accent, reserved strictly for interactive states, critical data points, and primary call-to-actions. This color should often be accompanied by a subtle outer glow to simulate light scattering in water. Neutral tones are cool-skewed grays to maintain the "chilled" professional atmosphere of the platform.

## Typography
The typographic hierarchy prioritizes rapid data assimilation. **Montserrat** is utilized for headlines to convey a geometric, architectural premium feel. It should be used sparingly for impact. 

**Inter** handles all functional body copy and complex data visualizations. For telemetry and sensor readings, use the "data-mono" style—a semi-bold Inter variant with increased letter spacing—to mimic technical readouts. High contrast is mandatory; primary text should remain near-white (#F0F9FF) to pop against the deep-sea backgrounds.

## Layout & Spacing
The layout uses a **Fluid Grid** system to reflect the expansive nature of the ocean. A 12-column structure is standard for desktop, but spacing is generous to prevent "claustrophobia." 

Content should be grouped into logical "pods" or "modules." Use a 24px gutter to maintain clear separation between glass cards. Vertical rhythm is strictly enforced in 8px increments to ensure the technical precision expected of an intelligence platform. Large margins (32px+) are encouraged for top-level dashboard views to create a premium, uncrowded feel.

## Elevation & Depth
Depth in this design system is achieved through **Backdrop Blurs** and **Refractive Layers** rather than traditional drop shadows. 

1.  **Base Layer:** Pure Black background.
2.  **Mid Layer:** Deep Sea Blue semi-transparent surfaces (60-80% opacity) with a 20px backdrop blur.
3.  **Floating Layer:** Glassmorphic cards with a 1px solid stroke in `glass_stroke` color. 
4.  **Interactive Layer:** Elements that gain "energy." These use a 0px 0px 12px `primary_color` outer glow to indicate they are active or selected.

Avoid heavy black shadows; instead, use inner shadows (dark blue) to create "wells" for input fields and recessed data displays.

## Shapes
The shape language is "Organic-Tech." Surfaces use **Rounded (0.5rem/8px)** corners to soften the high-tech aesthetic, mimicking the way water rounds hard edges over time. 

- **Primary Cards:** 1rem (16px) corner radius for a friendly but structured containment.
- **Buttons and Chips:** Fully pill-shaped (3rem) to represent smooth pebbles or liquid droplets.
- **Icons:** Use a 2px stroke weight with slightly rounded terminals. 

Avoid sharp 0px corners entirely, as they feel too industrial and "dry" for the aquatic narrative.

## Components
- **Buttons:** Primary buttons are solid Neon Cyan with black text. Secondary buttons are ghost-style with a cyan border and a subtle cyan outer glow on hover.
- **Glass Cards:** The signature component. These must have `backdrop-filter: blur(20px)` and a thin, translucent top-down gradient stroke to simulate light hitting the edge of a glass tank.
- **Data Visualizations:** Charts should use "Liquid" line styles (smoothed Bezier curves) rather than jagged points. Use Neon Cyan for the primary data line and a gradient fill that fades into the Deep Sea Blue background.
- **Inputs:** Dark, recessed fields with a "Deep Sea" background. On focus, the border glows Neon Cyan.
- **Status Indicators:** Use bioluminescent pulses (subtle opacity animations) for "Live" or "Active" sensor readings.
- **Marine Gauges:** Circular progress indicators that resemble submersible depth gauges or oxygen tanks, using thin strokes and high-contrast labels.