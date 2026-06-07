---
name: Aero-City Sky-Sleek
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#b9c8de'
  on-secondary: '#233143'
  secondary-container: '#39485a'
  on-secondary-container: '#a7b6cc'
  tertiary: '#7bd0ff'
  on-tertiary: '#00354a'
  tertiary-container: '#001c29'
  on-tertiary-container: '#008cbd'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
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
  data-mono:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-edge: 40px
  safe-zone: 64px
---

## Brand & Style

The design system is engineered for the elite tier of sky-level real estate and helipad logistics. The brand personality is authoritative, sophisticated, and technologically advanced, aiming to evoke a sense of precision and "high-altitude" exclusivity. 

The aesthetic is defined as **Sky-Sleek**, a synthesis of **Glassmorphism** and **Futuristic HUD (Heads-Up Display)** interfaces. It prioritizes clarity and technical density without sacrificing high-end luxury. The emotional response is one of controlled power and seamless navigation through a complex, vertical urban environment. Every element should feel like a piece of high-precision aerospace instrumentation reimagined for architectural luxury.

## Colors

The design system utilizes a deep, atmospheric palette to simulate the feeling of high-altitude flight and twilight horizons.

- **Primary (Deep Navy Blue):** Used for the core background environment, providing a stable, vast foundation.
- **Secondary (Brushed Steel):** Applied to structural elements, thin borders, and inactive states to ground the interface in industrial hardware.
- **Tertiary (Aero Glow):** A vibrant cyan-blue used sparingly for glowing accents, active data points, and interactive feedback.
- **Neutral (Cloud White):** Reserved for high-priority typography and icons to ensure maximum legibility against the dark background.

The interface operates exclusively in a **Dark Mode** to maintain the HUD aesthetic and reduce glare for users who may be operating in low-light cockpit or lounge environments.

## Typography

Typography in this design system balances human-centric readability with machine-precision data visualization.

- **Headlines & Body:** **Inter** provides a clean, geometric sans-serif foundation that feels modern and unobtrusive. Use tighter tracking for large display text to enhance the "sleek" aesthetic.
- **Technical Overlays & Data:** **Space Mono** is used for all coordinate data, logistics values, and labels. This differentiates "information" from "instruction" and reinforces the HUD theme.
- **Hierarchy:** Maintain a clear distinction between editorial content (Inter) and telemetry (Space Mono). Use uppercase transformations for labels to mimic aeronautical control panels.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with a "peripheral focus." Essential telemetry and navigation elements are anchored to the screen edges (HUD style), while core content resides in a central glass container.

- **12-Column Grid:** Use a standard 12-column grid for page content, but allow technical overlays to break the grid and float at the viewport edges.
- **Safe Zones:** Implement wide 40px - 64px outer margins to simulate the "frame" of a cockpit window or a high-end display.
- **Rhythm:** Use a 4px baseline grid to maintain alignment for dense data tables. Internal padding within glass cards should be generous (24px or 32px) to prevent the "technical" feel from becoming "cluttered."

## Elevation & Depth

Depth is achieved through **Glassmorphism** and light-based layering rather than traditional shadows.

- **Surface Layers:** Surfaces are semi-transparent (#0A192F at 60-80% opacity) with a `backdrop-filter: blur(12px)`. This allows the "sky" (background imagery) to bleed through subtly.
- **Thin Borders:** Every container must have a 1px solid border. Use a gradient border (Brushed Steel to Transparent) to simulate light hitting the edge of a glass panel.
- **Glow Accents:** Instead of drop shadows, use `box-shadow` with the Tertiary color and high blur (e.g., `0 0 15px rgba(56, 189, 248, 0.3)`) to indicate active or "powered-on" states.
- **Stacking:** Higher elevation levels should have slightly higher opacity and a brighter border-color value.

## Shapes

The shape language is dominated by **sharp, technical precision**. 

- **Corner Radius:** Standard components utilize a `0.25rem` (4px) radius. This provides a "subtle rounding" that feels modern but maintains the aggressive, structural look of aerospace components.
- **Angled Accents:** Where possible, use clipped corners (45-degree chamfers) on decorative elements or buttons to reinforce the aeronautical theme.
- **Micro-interactions:** On hover, shapes should not expand or bounce; instead, they should "activate" through line-weight changes or internal glow shifts.

## Components

- **Translucent Cards:** The primary container. Must include a 1px steel border, backdrop blur, and a top-left "data-tag" using Space Mono.
- **Buttons:** 
  - *Primary:* Solid Brushed Steel with Cloud White text. High-contrast hover state featuring a Tertiary glow.
  - *Ghost:* 1px Cloud White border, transparent background, text in Mono.
- **Inputs:** Underlined or fully boxed with 1px steel borders. On focus, the border color transitions to the Tertiary glow.
- **Micro-Interactions:** Transitions should be instantaneous (150ms or less) to mimic high-speed computer processing. Use "scanline" animations or subtle flickering for loading states.
- **Technical Overlays:** Floating labels that display GPS coordinates, wind speed, or altitude relative to the real estate being viewed. These should appear in the corners of the viewport with a lower opacity (60%).
- **Status Indicators:** Small circular pips that pulse with a soft glow to indicate helipad availability or real-time connectivity.