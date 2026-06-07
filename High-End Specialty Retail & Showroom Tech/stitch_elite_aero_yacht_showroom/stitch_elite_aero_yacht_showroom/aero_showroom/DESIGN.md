---
name: Aero-Showroom
colors:
  surface: '#131319'
  surface-dim: '#131319'
  surface-bright: '#393840'
  surface-container-lowest: '#0d0e14'
  surface-container-low: '#1b1b22'
  surface-container: '#1f1f26'
  surface-container-high: '#292930'
  surface-container-highest: '#34343b'
  on-surface: '#e4e1eb'
  on-surface-variant: '#c6c5d5'
  inverse-surface: '#e4e1eb'
  inverse-on-surface: '#303037'
  outline: '#908f9e'
  outline-variant: '#464653'
  surface-tint: '#bfc2ff'
  primary: '#bfc2ff'
  on-primary: '#181d8c'
  primary-container: '#000080'
  on-primary-container: '#777eea'
  inverse-primary: '#4b53bc'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#202222'
  on-tertiary-container: '#888989'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bfc2ff'
  on-primary-fixed: '#00006e'
  on-primary-fixed-variant: '#3239a3'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131319'
  on-background: '#e4e1eb'
  surface-variant: '#34343b'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.05em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-point:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.1em
  label-caps:
    fontFamily: Space Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.2em
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1440px
---

## Brand & Style

This design system embodies the "Sky-Sleek" aesthetic, catering to ultra-high-net-worth individuals in the private aviation and superyacht sectors. The brand personality is elite, technical, and precise, mirroring the engineering excellence of the vessels it showcases. 

The visual style is a hybrid of **Glassmorphism** and **High-Tech HUD (Heads-Up Display)** interfaces. It prioritizes clarity and high-performance data visualization. Every interface element should feel like a tactical instrument—sharp, intentional, and expensive. The emotional response is one of total control and quiet luxury, using transparency and light to create a sense of weightlessness and infinite horizon.

## Colors

The palette is anchored in **Deep Navy Blue**, representing the depths of the ocean and the edge of the atmosphere. **Metallic Gold** is used sparingly as a precision accent for borders, critical call-outs, and "active" states, signifying exclusivity.

*   **Primary (Navy):** Used for deep backgrounds and structural layering.
*   **Secondary (Gold):** Used for interactive "hotspots," thin borders, and premium data markers.
*   **Tertiary (Cloud White):** Primary color for text and icons to ensure high legibility against dark backgrounds.
*   **Accent Glow:** A technical cyan/blue glow used for data points and "Heads-Up" status indicators.
*   **Surface:** Semi-transparent variants of Navy (e.g., `rgba(0, 0, 128, 0.4)`) create the frosted glass effect.

## Typography

Typography functions as a telemetry readout. **Hanken Grotesk** provides a sharp, authoritative voice for headlines. **Inter** handles high-density information with neutral efficiency. **Space Mono** is reserved for technical data, specs, and labels, reinforcing the HUD aesthetic.

All labels and technical readouts should utilize uppercase styling with increased letter spacing to mimic cockpit instrumentation. Use the `data-point` style for any numerical values (e.g., knots, range, hull length).

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to maintain a cinematic, composed feel, while transitioning to a fluid model on mobile. A 12-column grid is used with generous gutters (24px) to allow components room to "breathe" against the deep navy background.

Alignment should be strictly mathematical. Elements are often grouped into tactical "clusters" or "modules" rather than long scrolling lists. Use wide margins (64px+) on desktop to create a sense of premium space, focusing the eye on the high-resolution assets in the center.

## Elevation & Depth

This design system rejects traditional shadows in favor of **Luminous Depth**. Hierarchy is established through:

1.  **Backdrop Blurs:** High-index blurs (20px-40px) on semi-transparent navy surfaces create a sense of vertical stacking.
2.  **Internal Glows:** Instead of drop shadows, use subtle inner glows (1px-2px) in Gold or White to define the "lip" of a component.
3.  **Additive Lighting:** "Glow points" behind key aircraft or yacht images to make them appear as though they are floating in an illuminated hangar or bay.
4.  **Z-axis Layers:** The base UI is the "glass," the data is the "projection," and the media content is the "viewfinder."

## Shapes

To maintain the high-performance, precision engineering feel, the shape language is **Sharp (0px)**. All containers, buttons, and input fields utilize hard 90-degree angles. This geometric severity suggests structural integrity and professional equipment.

Tactical elements like "corner brackets" or "crosshair" icons may be used to frame content, emphasizing the "targeting" or "selection" of high-value assets.

## Components

*   **Frosted Glass Cards:** Background: `rgba(0, 0, 128, 0.4)`, Backdrop-filter: `blur(20px)`, Border: `0.5px solid rgba(212, 175, 55, 0.3)`.
*   **Tactical Buttons:** Sharp corners. Primary state: Solid Navy with Gold 1px border. Hover state: Gold text with a subtle external Gold outer glow (0px 0px 8px).
*   **Data Points:** Small circular icons (4px) with a `box-shadow` glow in the color of the data category (e.g., green for "Available," gold for "Reserved").
*   **HUD Inputs:** Underlined text fields (no full box) with a gold 1px bottom border that expands on focus. Labels appear in `label-caps` style above the field.
*   **Vessel Spec Lists:** Use `Space Mono` for values and `Inter` for titles. Values should be right-aligned for easy vertical scanning.
*   **Crosshair Nav:** A custom cursor or hover effect that uses hair-thin gold lines extending to the edges of the screen/container, mimicking a rangefinder.