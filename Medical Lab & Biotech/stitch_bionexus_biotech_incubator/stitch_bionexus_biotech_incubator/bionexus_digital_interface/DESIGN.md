---
name: BioNexus Digital Interface
colors:
  surface: '#07122a'
  surface-dim: '#07122a'
  surface-bright: '#2f3952'
  surface-container-lowest: '#030d25'
  surface-container-low: '#101b33'
  surface-container: '#151f37'
  surface-container-high: '#1f2942'
  surface-container-highest: '#2a344e'
  on-surface: '#d9e2ff'
  on-surface-variant: '#bbc9cf'
  inverse-surface: '#d9e2ff'
  inverse-on-surface: '#263049'
  outline: '#859398'
  outline-variant: '#3c494e'
  surface-tint: '#3cd7ff'
  primary: '#a8e8ff'
  on-primary: '#003642'
  primary-container: '#00d4ff'
  on-primary-container: '#00586b'
  inverse-primary: '#00677e'
  secondary: '#b9c7e4'
  on-secondary: '#233148'
  secondary-container: '#3c4962'
  on-secondary-container: '#abb9d6'
  tertiary: '#e1dedd'
  on-tertiary: '#313030'
  tertiary-container: '#c5c2c2'
  on-tertiary-container: '#515050'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b4ebff'
  primary-fixed-dim: '#3cd7ff'
  on-primary-fixed: '#001f27'
  on-primary-fixed-variant: '#004e5f'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#07122a'
  on-background: '#d9e2ff'
  surface-variant: '#2a344e'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
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

The design system is engineered to evoke a sense of "Scientific Precision meets Venture Capital." It positions the platform as a high-stakes, future-forward incubator where biological breakthroughs are accelerated by cutting-edge technology. 

The aesthetic is a refined blend of **Minimalism** and **Glassmorphism**. By utilizing deep, dark backgrounds with luminous accents, the UI mimics a high-end laboratory terminal or a premium executive dashboard. Surfaces are treated with translucent, frosted glass effects to create a sense of depth and lightness within a dark environment, ensuring the interface feels breathable despite its technical density. The emotional response should be one of absolute trust, technological superiority, and quiet sophistication.

## Colors

The palette is anchored in a trio of deep tones to provide a stable, professional foundation. 

*   **Matte Black (#121212)** and **Deep Navy (#0A192F)** function as the core structural colors, used for backgrounds and primary containers to create a high-contrast environment for data. 
*   **Neon Blue (#00D4FF)** is the primary "Signal" color, reserved for critical actions, active states, and highlighting data points. 
*   **Accent Neutrals** consist of cool greys and slate tones to handle secondary text and subtle borders without competing for attention.

The default mode is strictly Dark. Transparency is used strategically to create the glass effect, utilizing the Deep Navy color with varying alpha channels (60-80%) over blurred background elements.

## Typography

This design system utilizes a dual-font strategy to balance technical innovation with readability.

**Space Grotesk** is used for all headlines and labels. Its geometric, slightly technical character reinforces the biotech and aerospace-adjacent aesthetic. Headlines should utilize tighter letter spacing to maintain a "high-tech" density.

**Inter** is the workhorse for all body copy and data tables. It provides maximum legibility for complex scientific descriptions and financial figures. Small labels and "data headers" should use Space Grotesk with increased letter spacing and uppercase styling to denote a "readout" or "terminal" feel.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop (1440px max-width) and a fluid model for smaller viewports. 

A 12-column system is used to organize complex data dashboards. Spacing is strictly based on an 8px baseline rhythm. Information density should be moderate; large margins (48px+) are used to separate major sections, while tight spacing (12-24px) is used within components to maintain a cohesive "data-cluster" look. Alignment should be rigorous, favoring left-aligned text for readability in scientific documentation.

## Elevation & Depth

Elevation is achieved through **Glassmorphism** and tonal layering rather than traditional drop shadows.

1.  **Base Layer:** Solid Matte Black (#121212) or Deep Navy (#020C1B).
2.  **Surface Layer:** Semi-transparent Navy (#0A192F at 70% opacity) with a `backdrop-filter: blur(12px)`.
3.  **Borders:** Subtle, 1px solid or gradient strokes using Neon Blue (#00D4FF) at very low opacity (10-20%) to define edges without creating heavy visual weight.
4.  **Luminous Glow:** For high-priority elements, a soft, inner-glow or a very diffused outer-glow in Neon Blue can be used to simulate a self-illuminated digital screen.

## Shapes

The shape language is primarily **Soft (Level 1)**. 

Rectilinear forms with subtle rounding (4px to 8px) are used to maintain a professional, architectural feel. This avoids the "playfulness" of highly rounded corners while remaining more modern and approachable than sharp, 0px corners. Larger components like cards or modal containers should use the `rounded-lg` (8px) setting, while buttons and input fields use the base `rounded` (4px).

## Components

*   **Buttons:** Primary buttons are solid Neon Blue with Matte Black text. Secondary buttons are "Ghost" style with a 1px Neon Blue border and subtle glass background.
*   **Chips:** Used for "Stage" (e.g., Seed, Series A) or "Bio-Tech Sector" tags. Small, uppercase Space Grotesk text inside a low-opacity Neon Blue capsule.
*   **Cards:** Glassmorphic backgrounds with 1px borders. Header areas within cards should have a subtle horizontal separator.
*   **Inputs:** Dark, recessed backgrounds with a bright 1px bottom-border highlight upon focus.
*   **Data Visualizations:** Charts should exclusively use Neon Blue, White, and secondary cool-tones (Teals). Avoid warm colors unless indicating a "Critical Error" state.
*   **Status Indicators:** Small, pulsing "Glow" dots to represent live data feeds or active incubator status.
*   **Lists:** Monospaced-style alignment for numerical data, using Inter with tabular-lining enabled to ensure alignment of scientific figures.