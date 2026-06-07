---
name: Nautical-Industrial System
colors:
  surface: '#111414'
  surface-dim: '#111414'
  surface-bright: '#373a3a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#191c1c'
  surface-container: '#1d2020'
  surface-container-high: '#272a2a'
  surface-container-highest: '#323535'
  on-surface: '#e1e3e2'
  on-surface-variant: '#bfc8c8'
  inverse-surface: '#e1e3e2'
  inverse-on-surface: '#2e3131'
  outline: '#899292'
  outline-variant: '#3f4849'
  surface-tint: '#96d1d3'
  primary: '#96d1d3'
  on-primary: '#003738'
  primary-container: '#004b4d'
  on-primary-container: '#7fbabc'
  inverse-primary: '#2a6769'
  secondary: '#bec8cd'
  on-secondary: '#293236'
  secondary-container: '#414a4f'
  on-secondary-container: '#b0babf'
  tertiary: '#fbb894'
  on-tertiary: '#4e250c'
  tertiary-container: '#64371c'
  on-tertiary-container: '#e1a17e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b1edef'
  primary-fixed-dim: '#96d1d3'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#084f51'
  secondary-fixed: '#dbe4e9'
  secondary-fixed-dim: '#bec8cd'
  on-secondary-fixed: '#141d21'
  on-secondary-fixed-variant: '#3f484c'
  tertiary-fixed: '#ffdbca'
  tertiary-fixed-dim: '#fbb894'
  on-tertiary-fixed: '#331200'
  on-tertiary-fixed-variant: '#693b20'
  background: '#111414'
  on-background: '#e1e3e2'
  surface-variant: '#323535'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  technical-label:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  data-readout:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0.02em
spacing:
  unit: 4px
  container-padding: 32px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

This design system embodies the intersection of maritime heritage and cutting-edge amphibious engineering. The brand personality is authoritative, resilient, and technologically superior. It targets high-net-worth explorers and industrial naval contractors who demand precision and durability.

The visual style is a hybrid of **Corporate Modern** and **Glassmorphism**, leaning into a "Technical Premium" aesthetic. It utilizes semi-translucent surfaces to mimic water and high-tech HUDs, contrasted against rigid, industrial structures. The emotional response should be one of "Military-Grade Luxury"—the feeling of being inside a high-end submersible cockpit where every pixel represents a mission-critical metric.

## Colors

The palette is anchored in a **Dark Mode** environment to reduce glare and emphasize technical readouts. 

- **Primary (Deep Teal):** Used for depth and brand identity. It represents the ocean's depths and serves as the primary base for interactive elements.
- **Secondary (Gunmetal Grey):** Represents the industrial, metallic nature of the vehicles. Used for structural containers and "heavy" UI elements.
- **Accent (Crisp White):** Reserved for high-priority text and iconography to ensure maximum legibility against dark backgrounds.
- **Utility (Safety Orange):** Used exclusively for critical alerts, warnings, and emergency status indicators.
- **Utility (Bright Cyan):** Used for fluid-related data, tide levels, sonar pings, and "active" tech states.

## Typography

This design system uses **Hanken Grotesk** for primary communication to maintain a sophisticated, approachable tech feel. **Space Grotesk** is introduced for labels and data readouts to provide a geometric, futuristic contrast that mimics instrument clusters.

- **Headlines:** Should feel massive and structural.
- **Body:** Clean and highly legible with generous line height for operational clarity.
- **Technical Labels:** Always uppercase with increased letter spacing to evoke the feeling of engraved serial numbers or cockpit buttons.
- **Data Readouts:** Bold and prominent, ensuring telemetry data is the first thing a user sees.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for dashboard-style interfaces, ensuring that technical readouts do not shift unexpectedly. A 12-column grid is standard for desktop, while a 4-column grid is used for mobile handheld controllers.

The spacing rhythm is built on a 4px baseline, but emphasizes large, "safe" margins (64px on desktop) to evoke a premium, spacious feel despite the industrial density of the data. Components should be grouped into logical "modules" that mimic physical rack-mounted hardware.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Tonal Layering**. 

1.  **Background:** The deepest layer is a solid `#0B0E0F` (Background Dark).
2.  **Submerged Layers:** Semi-transparent Teal (`#004B4D` at 10-20% opacity) with a 20px backdrop blur creates the "liquid" feel.
3.  **Structural Components:** Gunmetal surfaces with subtle linear gradients (top-down) to simulate brushed metal.
4.  **Borders:** Every component uses a "Sharp Precise Border"—a 1px solid stroke in a lighter shade of the surface color (e.g., `#FFFFFF` at 15% opacity). This mimics machined edges.

Shadows are avoided in favor of "Inner Glows" and "Rim Lighting" to make components appear self-illuminated, like a backlit dashboard.

## Shapes

To reinforce the industrial and military-grade aesthetic, this design system utilizes **Sharp (0)** roundedness. Every corner is a precise 90-degree angle. This communicates rigidity, engineering precision, and structural integrity. 

Where "softness" is required for liquid-related visualizations (like sonar waves), it is achieved through circular masking rather than rounding the containers themselves.

## Components

### Buttons & Inputs
Buttons are rectangular with 1px precise borders. The "Primary" state uses a subtle Deep Teal to Cyan gradient. The "Industrial" state is Gunmetal with an inset inner shadow. Inputs should feature a "Scanning" animation on focus—a thin Cyan line moving across the border.

### Technical Readouts
Readouts are framed in thin, high-contrast borders with a small "Serial ID" label in the top-left corner in Space Grotesk. Values should flicker slightly upon updating to mimic real-time telemetry.

### Sonar Visualizations
Circular components that utilize Bright Cyan pulses. Backgrounds for these components must use the "Submerged" glass effect with a higher backdrop-blur (40px) to distinguish them from static data.

### Status Indicators
Robust, blocky indicators. A "Safe" state is Deep Teal, while "Active/Alert" is Safety Orange. Indicators should include a "Hazard" pattern (diagonal stripes) when in critical states.

### Cards & Containers
Containers are treated as "Modules." They feature "Structural Ribs"—thin vertical lines at the far left and right of the container—to visually reinforce the nautical-industrial frame.