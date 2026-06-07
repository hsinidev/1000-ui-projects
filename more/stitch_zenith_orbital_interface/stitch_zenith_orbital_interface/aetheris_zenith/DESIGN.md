---
name: Aetheris Zenith
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#46362e'
  surface-container-lowest: '#170b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362720'
  surface-container-highest: '#41312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#bfc6db'
  on-secondary: '#293041'
  secondary-container: '#41495a'
  on-secondary-container: '#b1b8cd'
  tertiary: '#9ccaff'
  on-tertiary: '#003257'
  tertiary-container: '#059eff'
  on-tertiary-container: '#003357'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#dbe2f8'
  secondary-fixed-dim: '#bfc6db'
  on-secondary-fixed: '#141c2b'
  on-secondary-fixed-variant: '#3f4758'
  tertiary-fixed: '#d0e4ff'
  tertiary-fixed-dim: '#9ccaff'
  on-tertiary-fixed: '#001d35'
  on-tertiary-fixed-variant: '#00497b'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#41312a'
typography:
  h1-display:
    fontFamily: Noto Serif
    fontSize: 84px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2-editorial:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  h3-technical:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  body-large:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-main:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.2em
spacing:
  unit: 4px
  gutter: 24px
  margin: 64px
  grid_overlay_opacity: '0.05'
---

## Brand & Style

The design system is engineered to evoke the awe of orbital travel and the exclusivity of ultra-luxury concierge services. It targets high-net-worth explorers who demand precision-grade technology paired with high-fashion aesthetics.

The visual style is **Glassmorphic-Aerospace**. It leverages the translucency of modern UI to simulate looking through reinforced cockpit glass into the void. This is supported by high-contrast typography and neon accents that mimic flight instrumentation. The interface feels weightless yet structurally sound, utilizing a "Technical Luxury" personality that balances the coldness of space with the warmth of high-end hospitality.

## Colors

The palette is anchored in the "Infinite Void"—a deep, near-pure black used for base layers to maximize OLED contrast. The secondary "Midnight Navy" provides depth and structural relief, preventing the UI from feeling flat.

"Solar Orange" is the singular high-energy accent, reserved exclusively for primary actions and critical telemetry data. Neutral tones are strictly cool-shifted grays and translucent whites to maintain the "aerospace instrumentation" feel. All gradients should follow a top-down light falloff, simulating light reflecting off a planet’s curvature.

## Typography

The typography strategy employs a "Formal vs. Functional" tension. Headlines utilize **Noto Serif** to provide an editorial, prestigious feel that speaks to the luxury of the experience. 

For all technical data, interactive elements, and body copy, **Space Grotesk** is used for its geometric, wide-stanced architecture which mimics digital flight displays. Data-heavy views should utilize wide tracking (letter spacing) and uppercase styling to ensure legibility against dark, blurred backgrounds.

## Layout & Spacing

This design system uses a **Fixed 12-Column Grid** with a tight 4px baseline rhythm. To reinforce the technical aesthetic, a subtle 1px grid overlay may be visible at 5% opacity in the background of data-rich panels.

Margins are generous (64px+) to create a sense of "vacuum" and luxury, ensuring the UI never feels cluttered. Spacing between related data modules should be kept tight and boxed within crisp borders to resemble a modular flight console.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional drop shadows.
- **Base Level:** Deep space black (#050505).
- **Surface Level:** Midnight navy panels with a 20px backdrop blur and 40% opacity.
- **Raised Level:** Elements like active cards use a 1px "Solar Orange" inner stroke and a subtle glow (box-shadow: 0 0 15px rgba(255, 107, 0, 0.2)).
- **Overlay Level:** Modals use a heavy 40px backdrop blur to isolate the user from the background telemetry.

Borders are strictly 1px wide, using a "shimmer" effect (linear-gradient borders) to simulate light catching the edge of metallic instrumentation.

## Shapes

The design system utilizes **Sharp (0px)** corners for all structural containers, buttons, and input fields. This mimics the machined precision of aerospace hardware. 

Internal elements, such as icons or decorative HUD rings, may utilize perfect circles to represent celestial bodies, but the primary UI framework remains strictly rectangular and architectural.

## Components

### Primary Buttons (Solar Orange)
Buttons feature a solid #FF6B00 background with an "inner-glow" effect (white inner shadow, 10% opacity, top-aligned) to simulate a physical backlit switch. Text is always uppercase Space Grotesk in #050505.

### Glass Panels
Standard containers utilize a "Cold-Fusion" glass effect: 1px border (#FFFFFF 10% opacity), 20px blur, and a background of `rgba(10, 18, 33, 0.6)`.

### HUD Data-Viz
Telemetry charts must avoid soft curves. Use stepped lines or faceted bar charts. Accent colors for data include "Neon Cyan" and "Solar Orange" to distinguish between nominal and critical status.

### Instrumentation Inputs
Input fields are underlined only or fully boxed with 1px borders. When focused, the border glows in Solar Orange, and a small "Active Telemetry" blinking dot (2px) appears in the top-right corner of the field.

### Status Chips
Pill-shaped (the only exception to the sharp-edge rule) with a 1px stroke and no fill. The text color dictates the state (Orange for Alert, White for Nominal).