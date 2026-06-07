---
name: Grit-Agility Kinetic System
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
  on-surface-variant: '#eabcb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#b08780'
  outline-variant: '#5f3e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690000'
  primary-container: '#ee0000'
  on-primary-container: '#ffffff'
  inverse-primary: '#c00100'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#777676'
  on-tertiary-container: '#ffffff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Anybody
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Anybody
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Anybody
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Archivo Narrow
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.5'
  body-md:
    fontFamily: Archivo Narrow
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  stat-lg:
    fontFamily: Anybody
    fontSize: 56px
    fontWeight: '900'
    lineHeight: '1.0'
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  edge-margin: 20px
  stack-gap: 12px
---

## Brand & Style

This design system is engineered for the high-octane world of professional canine sports. The brand personality is aggressive, disciplined, and relentlessly fast. It targets elite trainers and competitive handlers who value precision and performance over soft aesthetics. 

The visual language utilizes a **High-Contrast / Bold** style combined with elements of **Brutalism**. It rejects soft curves and subtle transitions in favor of "shear" effects and hard lines. The UI should evoke the sensation of a stopwatch ticking or a dog mid-sprint: focused, energetic, and industrial. All layout decisions prioritize rapid information scanning and "thumb-ready" interactions for on-the-field use.

## Colors

The palette is strictly limited to three core pillars to maintain maximum visual impact. **Carbon Black (#1A1A1A)** serves as the foundation, providing a deep, non-distracting canvas that reduces glare during outdoor use. **Racing Red (#EE0000)** is the primary action color, used exclusively for critical interactive elements, performance indicators, and brand accents. **White (#FFFFFF)** is reserved for high-priority typography and data points to ensure AAA accessibility against the dark ground. A mid-tone **Carbon Grey (#333333)** may be used for subtle borders or secondary container surfaces to define hierarchy without losing the dark-mode intensity.

## Typography

The typography system is built for motion. **Anybody** is used for all headlines; its variable widths and aggressive italic slant provide the "kinetic" feel required for a sports-centric UI. **Archivo Narrow** handles body copy, chosen for its high information density and legibility on mobile screens during active training sessions. For technical data, timestamps, and dog measurements, **JetBrains Mono** provides a precise, "telemetry" aesthetic. All headlines should be set in Italics to maintain the forward-leaning momentum of the brand.

## Layout & Spacing

This design system employs a **Fluid Grid** optimized for handheld devices. The spacing rhythm is based on a strict 4px baseline, but utilizes "energetic whitespace"—larger-than-standard vertical gaps (XL spacing) between major sections to prevent the high-contrast elements from feeling cluttered. 

Layouts should favor vertical stacks. Containers and cards should utilize a "clipped corner" or "slanted edge" motif rather than traditional boxes. Margins are generous at 20px to ensure touch targets remain clear of screen edges during physical activity.

## Elevation & Depth

This system avoids soft shadows and traditional depth metaphors. Hierarchy is achieved through **Tonal Layers** and **Hard Strokes**. 

1.  **Base:** Carbon Black (#1A1A1A).
2.  **Surface:** Carbon Grey (#333333) used for cards and sections.
3.  **Accent:** Racing Red (#EE0000) for interactive states.

Depth is communicated via "offset borders"—a 1px or 2px solid white or red border that is slightly offset from the container, creating a mechanical, layered look. No blurs are permitted; all edges must remain sharp to maintain the performance-oriented feel.

## Shapes

The shape language is **Sharp (0)**. There are zero rounded corners in this design system. All buttons, cards, inputs, and avatars are expressed as hard-edged rectangles or polygons. 

To emphasize speed, use a **6-degree shear** on primary call-to-action buttons and specific container headers, creating a "parallelogram" effect that points toward the right (the direction of progress).

## Components

-   **Buttons:** Rectangular with 0px radius. Primary buttons are Racing Red with White bold italic text. Hover/Active states should invert colors or shift to a solid white border.
-   **Cards:** Solid Carbon Grey backgrounds with a 1px Racing Red top-border or a sheared corner cut-out.
-   **Input Fields:** High-contrast White outlines against Carbon Black. Use JetBrains Mono for input text to emphasize data precision.
-   **Chips/Tags:** Small, sharp rectangles. For "Status: Active" or "Live" metrics, use a solid Racing Red block with white text.
-   **Progress Bars:** Lean, 4px height bars. The "fill" should be a repeating diagonal stripe (hazard pattern) in Red and Black to indicate active motion.
-   **Lists:** Divided by sharp 1px lines in Carbon Grey. High-contrast "Chevron" icons should be replaced by simple right-pointing arrows (`->`) or slanted "V" shapes.
-   **Data Visualizations:** Use only straight lines and sharp angles for graphs. No curved splines for performance charts.