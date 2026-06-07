---
name: Aqua-Reef Fluid-Tech
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#bac9cc'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#849396'
  outline-variant: '#3b494c'
  surface-tint: '#00daf3'
  primary: '#c3f5ff'
  on-primary: '#00363d'
  primary-container: '#00e5ff'
  on-primary-container: '#00626e'
  inverse-primary: '#006875'
  secondary: '#b5cad3'
  on-secondary: '#20333b'
  secondary-container: '#364a52'
  on-secondary-container: '#a4b8c2'
  tertiary: '#d1f2ff'
  on-tertiary: '#003642'
  tertiary-container: '#95dbf2'
  on-tertiary-container: '#076276'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#9cf0ff'
  primary-fixed-dim: '#00daf3'
  on-primary-fixed: '#001f24'
  on-primary-fixed-variant: '#004f58'
  secondary-fixed: '#d1e6f0'
  secondary-fixed-dim: '#b5cad3'
  on-secondary-fixed: '#0a1e25'
  on-secondary-fixed-variant: '#364a52'
  tertiary-fixed: '#b2ebff'
  tertiary-fixed-dim: '#8bd1e8'
  on-tertiary-fixed: '#001f27'
  on-tertiary-fixed-variant: '#004e5f'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 3rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 2rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-point:
    fontFamily: Space Grotesk
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

The design system is engineered to evoke the precision of marine science combined with the exclusivity of luxury property management. It centers on a **Fluid-Tech** aesthetic—a synthesis of organic liquid motion and rigid technical accuracy. The target audience consists of high-net-worth aquarium owners and professional aquarists who require sophisticated data visualization without sacrificing the serene, immersive beauty of a marine environment.

The visual style utilizes **Glassmorphism** to create depth, simulating the refractive quality of water and thick acrylic tanks. This is complemented by high-performance technical details, such as micro-glows and hairline strokes, ensuring the interface feels like a premium instrument panel. The emotional response is one of calm control, deep-sea exploration, and absolute reliability.

## Colors

The palette is anchored in a "Deep Sea" dark mode. The primary color, **Neon Cyan**, acts as the bioluminescent guide, used exclusively for interactive elements, critical data points, and active states. The **Deep Sea Blue** and **Pure Black** form the structural foundation, providing a high-contrast backdrop that allows cyan elements to "pop" with a perceived glow.

Gradients should be used to simulate fluid depth. Use linear gradients transitioning from `#005F73` to `#001219` for large surface areas. Interactive glows should utilize the primary cyan with a high diffusion rate and low opacity (15-25%) to prevent visual fatigue while maintaining a high-tech energy.

## Typography

This design system utilizes a dual-font strategy to balance technical futurism with readability. **Space Grotesk** is the primary choice for headlines and data labels; its geometric construction mirrors high-tech instrumentation. **Inter** is reserved for body copy and long-form information, ensuring maximum legibility across dense data sets.

Headings should often be paired with subtle text-shadows in the primary cyan color when used sparingly for "hero" moments. For data visualizations, the `data-point` style provides a crisp, legible weight that stands out against the dark backgrounds.

## Layout & Spacing

The layout philosophy follows a **fluid grid** model with a 12-column structure, allowing the interface to scale seamlessly from tablet-sized monitoring stations to large-scale gallery displays. A generous 24px gutter ensures that complex data widgets do not feel cluttered, maintaining the "luxury" of white space (or in this case, "deep space").

Components are aligned to an 8px rhythmic grid. Internal padding within glass cards should be consistent at 32px (4 units) to reinforce the premium feel. Sections should be separated by clear, wide margins to allow the liquid background gradients to breathe.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces are stacked using varying levels of translucency and background blurs.

1.  **Base Layer:** Pure Black (#000000) or a deep gradient.
2.  **Surface Layer (Cards/Panels):** Deep Sea Blue (#001219) at 40-60% opacity with a 20px-40px Backdrop Blur. A 1px border with a top-down linear gradient (Cyan to Transparent) creates a "glass edge" effect.
3.  **Interactive Layer (Hover/Active):** Addition of a soft Cyan outer glow (spread: 2px, blur: 15px, opacity: 0.3) to indicate focus.

Avoid heavy black shadows; instead, use "inner glows" on buttons to simulate light trapped within a glass surface.

## Shapes

The shape language is **Rounded**, favoring 0.5rem (8px) for standard components and 1.5rem (24px) for major container cards. This softness mimics the smoothed edges of high-end aquarium tanks and the organic flow of water. 

Circular elements are used strictly for status indicators (e.g., pH levels, temperature gauges) and user avatars to contrast against the predominantly rectangular grid. Decorative elements, such as graph lines, should use "spline" curves rather than sharp angles to maintain the fluid-tech narrative.

## Components

### Buttons
Primary buttons feature a full Neon Cyan fill with black text, utilizing a high-intensity glow on hover. Secondary buttons use the "glass edge" style: transparent background, 1px cyan border, and white or cyan text.

### Chips & Badges
Small, capsule-shaped elements used for status (e.g., "Salinity: Stable"). These should use a subtle background tint of the status color (Green for stable, Cyan for active, Red for alert) with a high-contrast border.

### Glass Cards
The core container for the design system. Must feature a `backdrop-filter: blur(20px)` and a subtle diagonal linear gradient to simulate light hitting glass. Headers within cards should be separated by a 1px divider with 10% opacity.

### Data Visualizations
Charts use thin, glowing lines in Neon Cyan. Fill areas beneath lines should use a vertical gradient from Cyan (20% opacity) to Transparent. Avoid solid grid lines; use a dotted pattern in a muted grey-blue for axis markers.

### Input Fields
Inputs are semi-transparent with a 1px bottom-border. Upon focus, the border transitions to a full Cyan glow, and the label (Space Grotesk) shifts to a smaller "label-caps" position above the field.

### Specialized Components
*   **Tank Scrubber:** A custom slider component for time-series data, featuring a "bubble" handle.
*   **Metric Orbs:** Circular gauges for life-support vitals, using circular progress bars with glowing ends.