---
name: Predictive Financial Intelligence
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#191919'
  on-tertiary-container: '#838181'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-margin: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for high-stakes decision-making, evoking an atmosphere of institutional authority and cutting-edge predictive power. It prioritizes a "Financial-Sleek" aesthetic—a synthesis of **Minimalism** and **Glassmorphism**—that delivers a premium, high-density information environment without succumbing to visual clutter.

The visual narrative is one of absolute precision. By utilizing high-contrast elements against a deep, nocturnal foundation, the system directs focus toward critical "action signals" and predictive data. The emotional response is one of calm confidence, mirroring the experience of a high-end trading terminal or a private wealth management suite. Subtraction is used as a tool; every border, gradient, and layer serves to categorize intelligence or emphasize a trend.

## Colors

The color palette is anchored in a triple-black architecture to ensure maximum depth and contrast. The primary **Deep Navy (#0A192F)** functions as the structural surface color, while **Matte Black (#121212)** defines the background "void," creating a sense of infinite space. **Silver (#C0C0C0)** is utilized for primary typography and iconography, providing a metallic, premium sheen that remains legible at small scales.

For financial indicators, the system employs high-chroma neon variations of Green and Red. These are not merely decorative; they are "signal colors" that must pierce through the dark interface. Subtle gradients are used to transition between navy and black to create "wells" of information, while glassmorphism effects use a semi-transparent silver stroke to define edges without adding heavy visual weight.

## Typography

This design system utilizes a dual-font strategy to balance technical rigor with utilitarian readability. **Space Grotesk** is the primary headline and data font. Its geometric, slightly futuristic construction provides the "technical" feel required for financial intelligence and ensures that numerical data—specifically tickers and percentages—feels distinct and architecturally sound.

**Inter** is the workhorse for body copy and administrative UI. It was selected for its exceptional legibility at small sizes and its neutral, corporate character. When displaying numerical values in tables or charts, the `data-mono` style should be applied to ensure tabular alignment and immediate scannability. All labels should lean toward slightly tighter tracking and uppercase styling to mimic professional trading instrumentation.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to ensure data density and structural integrity across professional-grade monitors. A 12-column system is used for dashboard views, allowing for flexible arrangement of modular "intelligence widgets." 

Spacing is governed by a 4px baseline grid. This granular control allows for high information density while maintaining legibility through strict vertical and horizontal alignment. Elements should be "stacked" with minimal padding (8px–16px) to maximize the amount of visible data on a single screen, relying on color value shifts and thin borders rather than large gaps of whitespace to create separation.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and **Tonal Layering** rather than traditional drop shadows. Surfaces appear as translucent planes of Deep Navy floating over the Matte Black background.

1.  **Level 0 (Background):** Solid Matte Black (#050B14).
2.  **Level 1 (Panels):** Deep Navy with 80% opacity and a 16px backdrop blur.
3.  **Level 2 (Active Elements):** Same as Level 1 but with a 1px "Silver" inner stroke (10% opacity) to catch the "light."
4.  **Level 3 (Modals/Popovers):** Higher opacity (95%) with a more pronounced silver border (20% opacity) and a very subtle, large-radius ambient glow using the primary navy color to simulate light emission.

This approach creates a "screen-behind-the-screen" effect, characteristic of premium digital cockpits.

## Shapes

The shape language is "Soft" (0.25rem base radius). Sharp enough to feel industrial and precise, yet slightly rounded to avoid the aggressive harshness of pure brutalism. 

*   **Standard Components:** (Buttons, Inputs, Cards) use a 4px radius.
*   **Large Containers:** (Dashboards, Main Feed) use an 8px radius.
*   **Data Indicators:** Small indicators like "Buy/Sell" badges or status dots may use a fully rounded (pill) shape to distinguish them as interactive or status-driven tokens.

Consistent corner radii across all data-dense widgets ensure that the grid feels unified and systematic.

## Components

### Buttons & Action Signals
Primary actions use a high-contrast Silver-to-White linear gradient with black text, creating a "pressed metal" look. Secondary actions are ghost buttons with 1px silver borders. "Action Signals" (Buy/Sell) must be vibrant; a "Buy" signal uses a neon cyan-green glow, while "Sell" uses a sharp, high-contrast red.

### Technical Indicators & Charts
Charts must utilize high-contrast line weights (2px minimum) against the Matte Black background. Grid lines within charts should be ultra-low contrast (Deep Navy at 50% opacity). Use subtle area gradients beneath line charts to provide volume without obscuring the background grid.

### Input Fields & Search
Inputs are recessed (darker than the panel they sit on) with a Silver placeholder at 40% opacity. Upon focus, the border should glow with a subtle primary navy pulse.

### Intelligence Cards
Cards serve as the primary container for predictive data. They feature a glassmorphic blur and a thin top-border highlight. The header of every card should use the `label-sm` typography style in Silver to clearly categorize the data type.

### Predictive Badges
Small, high-contrast chips that display "Probability" or "Confidence" scores. These should use the `data-mono` font and be color-coded based on the strength of the prediction.