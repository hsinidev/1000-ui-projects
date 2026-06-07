---
name: Precision-Sleek
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#cac6c3'
  on-tertiary: '#32302f'
  tertiary-container: '#0b0a09'
  on-tertiary-container: '#7c7977'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e6e1df'
  tertiary-fixed-dim: '#cac6c3'
  on-tertiary-fixed: '#1d1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-weight:
    fontFamily: JetBrains Mono
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.1em
  display-weight-mobile:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 48px
---

## Brand & Style

The design system is engineered for the high-end traveler who values technical excellence and minimalist luxury. The brand personality is authoritative, precise, and sophisticated, evoking the feeling of a premium aerospace instrument or a professional-grade horological interface.

The visual style is **Tactile-Minimalism** mixed with **Glassmorphism**. It utilizes dark mode by default to create a sense of depth and focus. The interface should feel like an extension of the luggage hardware—cold, metallic, and incredibly responsive. Elements use subtle gradients to mimic brushed aluminum and high-tech glass, while thin, crisp borders maintain structural integrity. The emotional response is one of total control and absolute reliability.

## Colors

The palette is anchored in **Deep Space Black**, providing a limitless backdrop that emphasizes the physical components of the interface. **Silver** serves as the primary structural color, used for borders, icons, and metallic finishes to ground the digital experience in hardware.

**Mint** is reserved exclusively for "Data-Positive" states: successful weight checks, active Bluetooth connections, and battery health. It acts as a beacon of precision against the monochromatic base. Surfaces utilize a layered approach where background depth is achieved through varying shades of near-black and subtle radial gradients that suggest curved glass.

## Typography

Typography is used as a functional readout. **Geist** provides a clean, technical sans-serif aesthetic for navigation and content, offering high legibility with a professional tone. 

For all numeric and telemetry data—specifically the integrated scale readouts—**JetBrains Mono** is employed. Its monospaced nature ensures that weight fluctuations do not cause visual "jitter" on the screen, maintaining the feeling of a stable digital instrument. Large display sizes for weights should use negative letter-spacing to feel compact and "heavy," mirroring the physical weight of the luggage.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy within a fluid container, emphasizing horizontal hierarchy. On desktop, a 12-column grid with generous 40px gutters ensures data doesn't feel cramped. On mobile, a 4-column grid is used with a focus on vertical telemetry stacks.

Spacing is disciplined and utilizes a 4px baseline. High-density data zones (like weight history) use `sm` spacing, while primary hardware controls use `lg` to `xl` spacing to prevent accidental triggers and to impart a sense of "premium breathing room." Alignment should always be crisp, with content strictly adhering to grid lines to reinforce the precision narrative.

## Elevation & Depth

Elevation is not conveyed through traditional shadows, but through **Tonal Layering** and **Backdrop Blurs**.

1.  **Level 0 (Base):** Deep Space Black (#0A0A0A).
2.  **Level 1 (Panels):** Near-black (#141414) with a 1px Silver (#C0C0C0) border at 10% opacity.
3.  **Level 2 (Active Components):** Subtle linear gradients (top-to-bottom) from #1A1A1A to #0A0A0A, mimicking the sheen of a metallic surface.
4.  **Level 3 (Modals/Overlays):** 40% opacity Silver blur (20px) to simulate frosted glass resting above the luggage hardware.

Borders are the primary separators. A 0.5pt stroke is used for all internal dividers to maintain the "etched" hardware look.

## Shapes

The shape language is strictly **Sharp (0)**. To reflect the high-end industrial design of the luggage, the design system avoids rounded corners. Every button, input field, and card uses 90-degree angles to convey structural strength and precision.

The only exceptions are for purely circular icons (e.g., status indicators) or "Balance-Check" progress rings, which serve as a visual contrast to the rigid, rectangular layout of the data modules.

## Components

### Buttons
Primary buttons are "Inverted" (White/Silver background, Black text) to feel like physical illuminated switches. Secondary buttons use a transparent background with a 1px Silver border. All buttons use a "press" state that changes the border color to Mint.

### Telemetry Cards
These house the scale data. They feature a 1px Silver border and a subtle top-to-bottom brushed metal gradient. The Mint accent is used for the "Weight Stabilized" state.

### Input Fields
Inputs are minimal, featuring only a bottom border in Silver. When focused, the border glows slightly with a Mint outer glow (2px blur).

### Balance-Check Gauge
A custom component mimicking a physical spirit level. It uses the monospaced font for degree readouts and turns Mint when the luggage is perfectly balanced for an accurate weight reading.

### Progress Indicators
Thin, 2px horizontal lines. Empty states are #262626; active states are Mint with a slight neon-glow effect (4px blur).