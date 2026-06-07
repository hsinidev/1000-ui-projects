---
name: Mission Critical Utilitarian
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
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#ffb599'
  on-secondary: '#5a1c00'
  secondary-container: '#fe5f00'
  on-secondary-container: '#521900'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#101213'
  on-tertiary-container: '#7c7d7e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb599'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#7f2b00'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  telemetry-lg:
    fontFamily: monospace
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  telemetry-sm:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-reg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  base: 4px
  gutter: 16px
  margin: 24px
  panel-padding: 12px
---

## Brand & Style

This design system is engineered for high-stakes, zero-latency environments where information density and split-second recognition are paramount. The brand personality is clinical, authoritative, and strictly utilitarian, drawing heavily from industrial control systems and aerospace telemetry dashboards.

The visual style is a fusion of **Industrial Brutalism** and **High-Contrast Minimalism**. It eschews decorative flourishes in favor of raw structural integrity. Every pixel must serve a functional purpose. The aesthetic prioritizes "at-a-glance" comprehension, using heavy strokes and a rigid hierarchy to ensure that critical data points are never lost in the UI. It evokes a sense of being in a high-tech command center: cold, precise, and unwavering.

## Colors

The palette is restricted to a triad of functional zones:
- **Graphite (Primary):** The foundation. Used for backgrounds to minimize eye strain in low-light command environments and to provide a void-like canvas for data.
- **Safety Orange (Secondary):** Reserved exclusively for alerts, active states, and critical mission timings. It is the "Action Color"—if it is orange, it requires attention.
- **White (Tertiary/Neutral):** Used for primary data readouts and high-readability labels.

Secondary neutrals like mid-tone greys are used sparingly for borders and inactive telemetry to maintain a clear visual hierarchy between "active" and "background" data.

## Typography

Typography is divided by function rather than just scale.
- **Space Grotesk** is used for high-urgency alerts and section headers. Its geometric, technical nature signals "System Status."
- **Monospaced Fonts** (System Mono) are used for all telemetry, coordinates, and live data streams. This ensures character alignment in rapidly changing numeric values, preventing "jumping" layouts during high-frequency updates.
- **Inter** handles standard body text and instructional labels, providing a neutral, highly legible balance to the more aggressive technical fonts.

All labels should be displayed in uppercase to reinforce the industrial, documented aesthetic.

## Layout & Spacing

This design system utilizes a **Rigid Grid** model based on a 4px baseline. The layout is data-dense, minimizing whitespace to ensure maximum information is visible within a single viewport without scrolling.

- **12-Column Grid:** For primary dashboard organization.
- **Micro-Grids:** Individual telemetry panels use internal sub-grids to align data labels and values.
- **Gutter Strategy:** Tight 16px gutters reinforce the "instrument cluster" feel, making the UI feel like a singular, unified machine rather than a collection of separate cards.

## Elevation & Depth

Depth is conveyed through **Bold Borders** and **Tonal Layering** rather than shadows. In a mission-critical UI, shadows add visual noise; this system relies on:
- **Stroke-based Separation:** Panels are defined by 1px or 2px solid borders (White or Mid-Grey at low opacity).
- **Z-Axis layering:** Active alerts use a "Safety Orange" glow effect (inner-shadow) to simulate a physical backlit button or warning lamp.
- **Occlusion:** Overlays are rare; when they occur, they use a solid Graphite background with a high-contrast Safety Orange border to "interrupt" the workflow completely.

## Shapes

The shape language is **Sharp (0px)**. Rounded corners are perceived as "soft" or "consumer-friendly," which contradicts the industrial, high-precision nature of rocket operations. 

All buttons, panels, inputs, and status bars must have 90-degree angles. This allows elements to be packed tightly together and maintain a perfect grid-lock appearance. Beveled corners (45-degree cuts) may be used on primary action buttons to evoke a "tactical" hardware feel, but standard radius rounding is strictly prohibited.

## Components

### Buttons & Inputs
Buttons are rectangular blocks. **Primary Actions** (e.g., LIFT OFF, ABORT) use a solid Safety Orange background with black text. **Secondary Actions** are outlined in White with no fill. **Inputs** are simple Graphite boxes with a 1px White bottom border, utilizing monospaced text for all numerical entry.

### Status Bars
High-contrast indicators that fill horizontally. Backgrounds are deep charcoal; "Fill" is Safety Orange for active/critical progress or White for standard progress. No gradients are permitted.

### Telemetry Cards
Utilitarian containers with a top-aligned label in uppercase `label-caps`. Data is presented in `telemetry-lg`. If a value exceeds a threshold, the border of the entire card should pulse in Safety Orange.

### Countdown Timers
The most prominent component. Uses `headline-xl` in Safety Orange. The timer must be centered within a thick-bordered container to serve as the visual anchor of the interface.

### Toggles & Switches
Designed to mimic physical toggle switches. Use high-contrast states (Solid White for "ON", Dark Graphite for "OFF") to ensure the state is legible from a distance.