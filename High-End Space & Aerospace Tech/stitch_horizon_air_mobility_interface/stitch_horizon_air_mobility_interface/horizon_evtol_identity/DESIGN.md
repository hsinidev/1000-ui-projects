---
name: Horizon EVTOL Identity
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
  on-surface-variant: '#41484d'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#71787e'
  outline-variant: '#c1c7ce'
  surface-tint: '#2e6385'
  primary: '#2e6385'
  on-primary: '#ffffff'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#9accf3'
  secondary: '#595f66'
  on-secondary: '#ffffff'
  secondary-container: '#dde3eb'
  on-secondary-container: '#5f656c'
  tertiary: '#005bc1'
  on-tertiary: '#ffffff'
  tertiary-container: '#bfd2ff'
  on-tertiary-container: '#0056b8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#dde3eb'
  secondary-fixed-dim: '#c1c7cf'
  on-secondary-fixed: '#161c22'
  on-secondary-fixed-variant: '#41474e'
  tertiary-fixed: '#d8e2ff'
  tertiary-fixed-dim: '#adc6ff'
  on-tertiary-fixed: '#001a41'
  on-tertiary-fixed-variant: '#004493'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
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
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The brand personality is defined by "Weightless Precision." This design system communicates the effortless efficiency of electric flight through a Sustainable-Sleek aesthetic. It targets affluent urban commuters and eco-conscious travelers who value time and environmental stewardship. 

The visual language blends **Minimalism** with **Glassmorphism** to evoke the sensation of looking through a cockpit canopy or drifting through a clear sky. The emotional response should be one of calm, safety, and futuristic optimism. Every element must feel "aero-dynamic"—using clean lines and generous whitespace to ensure the interface never feels cluttered or grounded.

## Colors

The palette is anchored in **Ice Blue** and **Clean White**, creating a high-key, airy environment. 
- **Ice Blue (#A5D8FF):** Used for primary actions and highlights, representing the sky and clean energy.
- **Silver / Secondary (#E2E8F0):** Used for structural elements, dividers, and secondary surfaces to provide a metallic, high-tech finish.
- **Clean White (#FFFFFF):** The foundation of the glassmorphic layers and primary background space.
- **Electric Accent (#007AFF):** Reserved for high-priority status indicators or interactive states to ensure legibility against the light palette.

Gradients should be subtle, moving from Ice Blue to a transparent White to simulate atmospheric depth.

## Typography

This design system utilizes **Geist** for its technical precision and minimal footprint. The typeface’s monospaced-influence in its kerning (especially in numbers) reinforces the "aviation instrument" feel.

- **Headlines:** Should be set with slight negative letter-spacing to feel tight and engineered.
- **Labels:** Use uppercase with increased tracking for metadata and navigational labels to mimic flight HUDs (Heads-Up Displays).
- **Body:** Maintain a generous line height (1.6) to support the "airy" brand pillar, ensuring maximum readability during transit.

## Layout & Spacing

The design system employs a **fluid grid** with an emphasis on "Safe Zones." A 12-column grid is used for desktop, while mobile relies on a flexible single-column stack with 32px side margins to prevent content from feeling cramped.

The spacing rhythm is strictly based on an **8px linear scale**. To maintain the "Sleek" aesthetic, use larger-than-standard vertical padding (e.g., `xl` or 80px) between major sections to allow the glassmorphic components to "breathe" and appear as if they are floating in the sky.

## Elevation & Depth

Depth is achieved through **Backdrop Blurs** and **Specular Highlights** rather than traditional heavy shadows.

- **Surface Layers:** Use semi-transparent white (opacity 40-70%) with a `backdrop-filter: blur(20px)`.
- **Borders:** Components must feature a 1px "Inner Glow" border using a white-to-transparent linear gradient at 15% opacity. This simulates the edge of a glass pane.
- **Shadows:** Use a single, highly diffused "Ambient Light" shadow: `0px 20px 40px rgba(165, 216, 255, 0.1)`. The shadow color is tinted with Ice Blue to maintain the cool, atmospheric feel.
- **Z-Index:** Content "elevates" as the user interacts, increasing the backdrop blur intensity rather than shifting the shadow size significantly.

## Shapes

The shape language is "Aerodynamic Geometry." Sharp corners are avoided to maintain a friendly, sustainable feel, while excessive roundness (pill shapes) is reserved only for interactive triggers.

- **Containers:** Use `rounded-lg` (1rem/16px) to create a soft but structured frame.
- **Inputs & Smaller Elements:** Use `rounded` (0.5rem/8px).
- **Buttons & Chips:** Use `rounded-xl` (1.5rem/24px) to distinguish them from layout containers.

All lines must be "Clean"—avoiding heavy strokes. Use 1px widths for all decorative or structural borders.

## Components

- **Buttons:** Primary buttons use a subtle gradient (Ice Blue to Silver) with a high-gloss finish. Hover states should increase the backdrop blur of the elements behind them.
- **Cards:** These are the hero of the design system. They must be glassmorphic with a 1px white stroke and 20px blur. Content inside should have ample padding (24px+).
- **Input Fields:** Minimalist containers with a bottom-border only or a very light frosted-glass background. Focus states should trigger a soft Ice Blue outer glow.
- **Flight Trackers (Specialty):** Use thin, glowing lines for paths and "dot" indicators for vehicle locations. Lines should use a "comet" gradient effect (opaque head, transparent tail).
- **Status Chips:** Use low-saturation background tints (e.g., a faint green for "Ready") with high-contrast text.
- **Progress Indicators:** Use thin, 2px "Electric" blue lines for loading and battery status to emphasize the high-tech nature of the service.