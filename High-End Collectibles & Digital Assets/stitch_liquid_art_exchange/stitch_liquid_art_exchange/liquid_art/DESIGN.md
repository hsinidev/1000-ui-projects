---
name: Liquid-Art
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1c1b1d'
  surface-container: '#201f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e5e1e4'
  on-surface-variant: '#c4c5da'
  inverse-surface: '#e5e1e4'
  inverse-on-surface: '#313032'
  outline: '#8e8fa3'
  outline-variant: '#434657'
  surface-tint: '#b9c3ff'
  primary: '#b9c3ff'
  on-primary: '#00228a'
  primary-container: '#0047ff'
  on-primary-container: '#d4d9ff'
  inverse-primary: '#0046fa'
  secondary: '#d3fbff'
  on-secondary: '#00363a'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#5f6061'
  on-tertiary-container: '#dbdbdb'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b9c3ff'
  on-primary-fixed: '#001257'
  on-primary-fixed-variant: '#0033c0'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131315'
  on-background: '#e5e1e4'
  surface-variant: '#353437'
typography:
  headline-lg:
    fontFamily: Sora
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  bento-gap: 12px
---

## Brand & Style

The design system is engineered for the high-velocity environment of digital art speculation. The brand personality is aggressive, precise, and premium, catering to sophisticated collectors and algorithmic traders. The UI evokes the feeling of a high-end trading floor fused with a contemporary digital gallery.

To achieve a "Vibrant & Fast" aesthetic, the design system utilizes a **Glassmorphic-Industrial** hybrid style. It combines the structural rigidity of bento-box layouts with the ethereal depth of frosted surfaces. High-speed data is prioritized through high-contrast accents and kinetic motion cues. Surfaces are polished, utilizing subtle background blurs to maintain focus on fluctuating market data while preserving a sense of depth and layering.

## Colors

The design system operates on a deep-space **dark mode** foundation to make the "Vibrant" palette elements truly pop. 

- **Primary Blue (#0047FF):** Used for core actions, primary brand elements, and indicating active market "buy" states.
- **Neon Cyan (#00F0FF):** Reserved for highlights, interactive triggers, and high-velocity data points like price surges.
- **Pure White (#FFFFFF):** Utilized for maximum legibility of primary data and iconography against dark backgrounds.
- **Neutral (#0A0A0C):** A near-black obsidian used for the base background, providing the necessary contrast for glass effects.
- **Functional Accents:** Success and error states use hyper-saturated greens and pink-reds to maintain the high-energy aesthetic without clashing with the primary blue.

## Typography

This design system employs a tri-font strategy to balance character, legibility, and technical precision.

1. **Sora** is used for headlines. Its geometric and futuristic construction reflects the generative art focus of the platform.
2. **Hanken Grotesk** serves as the primary body face. It is sharp and contemporary, ensuring high readability even when data density is high.
3. **JetBrains Mono** is utilized for labels and numerical data. The monospaced nature ensures that fluctuating price tickers do not cause visual "jumping," maintaining a stable environment for rapid scanning.

All numerical data should use tabular figures to ensure alignment across dense bento-box grids.

## Layout & Spacing

The design system utilizes a **Bento-box layout model** built on a 12-column fluid grid. This model organizes diverse data sets—charts, tickers, and art previews—into distinct, rectangular modules of varying sizes.

- **Desktop:** A rigid 12-column grid. Modules should snap to 3, 4, 6, or 12 column spans.
- **Tablet:** 8-column grid with increased gutters to maintain breathability between complex modules.
- **Mobile:** Single column stack. Visual hierarchy is determined by the vertical order of bento tiles.

Spacing is based on a 4px baseline grid. Internal module padding is tighter (12px-16px) to maximize data density, while external "bento-gap" spacing remains consistent at 12px to create clear separation between distinct functional areas.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Tonal layering and Glassmorphism** rather than traditional drop shadows.

1. **Base Level:** The background (#0A0A0C).
2. **Bento Surface:** Semi-transparent layers with a 20px-40px background blur and a 1px inner stroke of White at 10% opacity. This creates a "glass plate" effect.
3. **Active Surface:** When a tile is hovered or active, the inner stroke brightness increases, and a subtle #0047FF outer glow (15% opacity, 30px blur) is applied to suggest "energy" and focus.
4. **Overlays:** Modals and tooltips use a higher opacity glass effect with a 60% darker background dimming to ensure focus remains on the utility.

## Shapes

The shape language is "Rounded-Industrial." We avoid organic or fully pill-shaped elements to maintain the feeling of a professional tool, while avoiding 0px corners to keep the "high-end" feel.

- **Bento Modules:** Use `rounded-lg` (1rem) to create a soft but defined frame for data.
- **Buttons & Inputs:** Use the base `rounded` (0.5rem) for a crisp, actionable appearance.
- **Tags & Status Chips:** Use `rounded-xl` (1.5rem) to differentiate them from functional inputs.
- **Art Previews:** Within a module, art should maintain the same corner radius as the parent container minus the internal padding to create a nested, balanced look.

## Components

### Sleek Cards & Bento Tiles
Every card is a bento-style container. Top sections should feature a "Header-Action" layout where the title is left-aligned and a secondary action (e.g., "Expand" or "Filter") is right-aligned using a ghost button.

### Interactive Heatmaps
Used for market activity. Use a gradient scale from Primary Blue (low activity) to Neon Cyan (high activity). Cells should have a 2px gap and use the system `rounded` value.

### Vibrant Tickers
Tickers should be edge-to-edge components. Negative values use the Error accent, positive values use the Success accent. Use **JetBrains Mono** for all ticker digits to prevent horizontal shifting during live updates.

### Buttons
- **Primary:** Solid #0047FF with White text. High-energy hover state using a #00F0FF outer glow.
- **Secondary:** Transparent background with a #00F0FF 1.5px border.
- **Actionable Icons:** Small 32x32px glass tiles with centered White icons.

### Inputs
Search and filter bars should utilize a dark-translucent background with a 1px border. On focus, the border transitions to Neon Cyan with a subtle "pulse" animation.

### Progress Indicators
Linear bars use a dual-tone gradient of Primary Blue to Neon Cyan, moving with a "shimmer" effect to indicate real-time data streaming.