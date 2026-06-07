---
name: GT Luxe Intelligence
colors:
  surface: '#0b1420'
  surface-dim: '#0b1420'
  surface-bright: '#323a47'
  surface-container-lowest: '#060e1b'
  surface-container-low: '#141c28'
  surface-container: '#18202d'
  surface-container-high: '#222a37'
  surface-container-highest: '#2d3543'
  on-surface: '#dbe3f4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dbe3f4'
  inverse-on-surface: '#29313e'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c5c7c8'
  on-secondary: '#2e3132'
  secondary-container: '#494c4d'
  on-secondary-container: '#babcbd'
  tertiary: '#f7f6ff'
  on-tertiary: '#2c303d'
  tertiary-container: '#d7daec'
  on-tertiary-container: '#5b5f6e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e1e3e4'
  secondary-fixed-dim: '#c5c7c8'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#454748'
  tertiary-fixed: '#dfe2f3'
  tertiary-fixed-dim: '#c3c6d7'
  on-tertiary-fixed: '#171b28'
  on-tertiary-fixed-variant: '#434654'
  background: '#0b1420'
  on-background: '#dbe3f4'
  surface-variant: '#2d3543'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  display-md:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  headline-sm:
    fontFamily: Montserrat
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.03em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.2em
  data-viz:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.0'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  element-gap: 16px
---

## Brand & Style

The design system embodies the intersection of high-performance grand touring and avant-garde digital engineering. It targets a demographic that values technical precision as much as sensory luxury. The aesthetic is "Minimalist-Luxe," defined by a reductionist approach to information density paired with a rich, atmospheric depth.

The UI utilizes **Glassmorphism** to simulate the high-tech cockpit of an electric GT. This involves multi-layered frosted surfaces, ethereal background blurs, and luminous accents that mimic the phosphorescence of instrument clusters. The emotional response is one of calm, authoritative control—cool to the touch, yet responsive and alive with fluid energy.

## Colors

The palette is anchored in a monochromatic dark spectrum to preserve night-vision and reduce ocular strain during high-speed travel. 

- **Deep Navy (#0A0E1A):** The infinite foundation. Used for the primary background to create an "endless" sense of space.
- **Silk White (#F8F9FA):** High-contrast typography and iconography. It feels more refined and less aggressive than pure white.
- **Glass-Cyan (#00F2FF):** The technical pulse. Used sparingly for critical telemetry, active states, and biometric highlights.
- **Gradients:** Utilize fluid transitions from Deep Navy to a slightly lighter #161C2D to define surface curvature without hard edges.

## Typography

This design system uses a dual-font strategy to balance editorial luxury with technical accuracy. 

**Montserrat** is the primary display face, set with wide tracking to evoke a sense of premium engineering and spaciousness. **Inter** provides high-legibility for functional body text. For data-heavy readouts and biometric labels, **JetBrains Mono** is introduced to provide a "developer-spec" aesthetic that aligns with the vehicle's advanced computing power. All labels should lean toward uppercase with generous letter-spacing to emphasize the minimalist-luxe theme.

## Layout & Spacing

The layout follows a **Fixed Grid** system for the primary dashboard and a **Fluid Grid** for secondary infotainment modules. 

- **Desktop/Cockpit:** A 12-column grid with 24px gutters. Elements are often centered or anchored to the edges to maximize the "panoramic" feel of a vehicle display.
- **Mobile/Remote App:** A 4-column fluid grid with 16px margins.
- **Rhythm:** Spacing is strictly based on an 8px base unit. To maintain the minimalist aesthetic, use larger "breathing rooms" (40px+) between major functional blocks to prevent visual clutter.

## Elevation & Depth

Depth is not communicated through shadows, but through **light transmission and blur density**.

1.  **Base Layer:** The Deep Navy solid background.
2.  **Mid Layer (Content Cards):** Translucent surfaces with a 20px-40px Backdrop Blur and a 1px inner border of Silk White at 10% opacity.
3.  **Top Layer (Interactions):** Elements like active buttons use a "Neon-Glass" effect—increased transparency but with a 2px outer glow in Glass-Cyan.
4.  **Z-Axis:** Higher elevation is represented by increased blur intensity and higher surface opacity, creating a "stacked glass" effect.

## Shapes

The shape language is "Sophisticated Geometric." We use **Rounded (Level 2)** settings to mirror the aerodynamic curves of the GT’s exterior. 

- **Standard Elements:** 8px (0.5rem) corner radius.
- **Large Container/Cards:** 16px (1rem) corner radius.
- **Interactive Triggers:** Full pill-shapes are reserved exclusively for "Go" or "Start" actions to distinguish them from informational cards.
- **Visual Accents:** Use 45-degree chamfered corners on decorative lines to hint at technical precision.

## Components

- **Neon-Glass Buttons:** Ghost-style buttons with a Glass-Cyan border. On hover/active, the border glows and a subtle cyan gradient fills the background at 15% opacity.
- **Translucent Cards:** Surfaces using `backdrop-filter: blur(20px)` and a background of `rgba(255, 255, 255, 0.03)`. No drop shadows; depth is provided by the blur of the layer beneath.
- **Biometric Visualizations:** Circular progress rings and heart-rate waves using thin (1px) Glass-Cyan lines. Use "Pulse" animations for active data streams.
- **Input Fields:** Bottom-border only, Silk White at 30% opacity. Upon focus, the border transitions to Glass-Cyan with a subtle glow.
- **Status Chips:** Small, pill-shaped indicators with a 4px blur and monochromatic icons.
- **Telemetry Lists:** High-contrast data points with JetBrains Mono values and Montserrat labels, separated by faint 1px horizontal rules.