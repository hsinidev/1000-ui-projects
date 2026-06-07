---
name: Executive Tech
colors:
  surface: '#0e141a'
  surface-dim: '#0e141a'
  surface-bright: '#333a40'
  surface-container-lowest: '#080f14'
  surface-container-low: '#161c22'
  surface-container: '#1a2026'
  surface-container-high: '#242b31'
  surface-container-highest: '#2f353c'
  on-surface: '#dde3eb'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#dde3eb'
  inverse-on-surface: '#2b3137'
  outline: '#909097'
  outline-variant: '#45464c'
  surface-tint: '#c0c6db'
  primary: '#c0c6db'
  on-primary: '#2a3041'
  primary-container: '#050b1a'
  on-primary-container: '#737a8d'
  inverse-primary: '#585e70'
  secondary: '#e9c176'
  on-secondary: '#412d00'
  secondary-container: '#604403'
  on-secondary-container: '#dab36a'
  tertiary: '#c3c6cf'
  on-tertiary: '#2d3137'
  tertiary-container: '#080c12'
  on-tertiary-container: '#777a82'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dce2f8'
  primary-fixed-dim: '#c0c6db'
  on-primary-fixed: '#151b2b'
  on-primary-fixed-variant: '#404658'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e0e2eb'
  tertiary-fixed-dim: '#c3c6cf'
  on-tertiary-fixed: '#181c22'
  on-tertiary-fixed-variant: '#43474e'
  background: '#0e141a'
  on-background: '#dde3eb'
  surface-variant: '#2f353c'
typography:
  display-lg:
    fontFamily: Epilogue
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  data-focus:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.02em
  body-regular:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
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
  container-padding: 24px
  gutter: 16px
  section-gap: 40px
  stack-sm: 4px
  stack-md: 12px
---

## Brand & Style

The brand personality of this design system is authoritative, elite, and meticulously engineered. It targets high-achieving individuals who demand the same level of performance from their health data as they do from their professional lives. The UI evokes the feeling of a bespoke luxury timepiece—combining the weight of tradition with the friction-less speed of modern intelligence.

The visual style is a refined execution of **Glassmorphism**, integrated into a high-performance framework. It avoids the playfulness often associated with glass effects, opting instead for "Industrial Transparency"—where layers appear as polished sapphire crystal or smoked glass. Every element should feel precision-machined, utilizing subtle metallic accents and a strict adherence to layout hierarchy to convey a sense of premium "Executive Tech."

## Colors

The palette is rooted in a deep, nocturnal foundation to emphasize luxury and reduce eye strain during high-performance tracking.

*   **Primary Background (Deep Navy):** A sophisticated, near-black navy that provides more depth and "intelligence" than a standard neutral black.
*   **Accent (Champagne Gold):** Used sparingly for critical data points, call-to-actions, and active states. It should feel like a metallic leaf—bright but not garish.
*   **Depth (Matte Black):** Reserved for the lowest layer of the UI and interactive surfaces that require maximum contrast against the gold accents.
*   **Data Highlights:** Use high-clarity whites and extremely muted versions of the gold to indicate secondary information without breaking the premium aesthetic.

## Typography

This design system utilizes a dual-font strategy to balance editorial authority with technical precision.

**Epilogue** is used for headlines and primary brand touchpoints. Its geometric yet expressive nature provides the "High-Contrast" look required for an executive presence. Use heavy weights (600+) for section headers to command attention.

**Manrope** serves as the functional workhorse. It is used for all body text and, crucially, for all health data points. Its modern, balanced proportions ensure that complex metrics remain legible at a glance. For data visualization, utilize the tabular lining figures of Manrope to ensure numbers align perfectly in lists and dashboards.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid** model optimized for mobile devices. While the outer container uses a fixed 24px safety margin to maintain a "frame" like a watch face, the internal components utilize a fluid grid.

The rhythm is dictated by an 8px base unit. 
*   **Vertical Rhythm:** Group related metrics with 4px or 12px gaps; separate distinct functional modules with 40px gaps to allow the background Navy to provide "breathing room."
*   **Precision Alignment:** All data points must be vertically center-aligned within their glass containers to reinforce the feeling of engineered balance.

## Elevation & Depth

Depth is the defining characteristic of this design system, achieved through meticulous layering rather than traditional drop shadows.

1.  **The Void (Base):** The Matte Black background represents the deepest level.
2.  **The Canvas (Primary):** The Deep Navy surface sits above the void.
3.  **Glass Containers:** These are the primary data carriers. Use a `backdrop-filter: blur(20px)` with a background color of `rgba(255, 255, 255, 0.04)`. 
4.  **The Golden Edge:** Every glass card must feature a 1px solid border. Use a linear gradient for this border: `Champagne Gold` at 30% opacity at the top-left, fading to 5% opacity at the bottom-right. This simulates a "light catch" on a chamfered metal edge.
5.  **Interactive Glow:** High-priority elements use a very soft, Champagne Gold ambient glow (spread 20px, opacity 10%) to indicate they are "active" or "live."

## Shapes

The shape language reflects "Softened Precision." Elements are not hyper-round (which feels too consumer-grade) nor perfectly sharp (which feels too aggressive).

*   **Cards and Containers:** Use a 16px (1rem) radius. This creates a silhouette that mimics the rounded corners of a premium smartwatch or high-end smartphone display.
*   **Small Elements (Chips/Inputs):** Use an 8px radius to maintain a tighter, more technical appearance.
*   **Icons:** Use a 1.5pt stroke weight with slightly rounded caps to match the typography's weight.

## Components

*   **Primary Buttons:** Solid Champagne Gold with Matte Black text. No gradients. The impact should be immediate and high-contrast.
*   **Glass Cards:** Semi-transparent containers for all health metrics (Heart Rate, HRV, Sleep). They should always feature the 1px subtle gold border and internal 24px padding.
*   **Metric Gauges:** Use thin, circular strokes for progress. The "track" should be Matte Black, and the "progress" should be a Champagne Gold gradient.
*   **List Items:** Separated by 1px dividers in Deep Navy (lighter than the background) to create a subtle recessed look.
*   **Segmented Controls:** These should appear as if "milled" out of the background—Matte Black recessed tracks with a Glassmorphic sliding indicator.
*   **Data Inputs:** Underlined or subtly boxed with 0.05 opacity white, turning Champagne Gold upon focus.
*   **Status Indicators:** Use small, high-intensity "LED" style dots. Instead of green for success, use a pale Gold or bright White to maintain the brand's sophisticated palette.