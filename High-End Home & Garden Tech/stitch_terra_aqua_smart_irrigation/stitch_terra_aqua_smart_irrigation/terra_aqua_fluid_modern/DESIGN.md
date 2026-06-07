---
name: Terra-Aqua Fluid-Modern
colors:
  surface: '#f9f9ff'
  surface-dim: '#d7dae4'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3fe'
  surface-container: '#ebedf8'
  surface-container-high: '#e6e8f3'
  surface-container-highest: '#e0e2ed'
  on-surface: '#181c23'
  on-surface-variant: '#414754'
  inverse-surface: '#2d3039'
  inverse-on-surface: '#eef0fb'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005cbc'
  primary: '#005ab7'
  on-primary: '#ffffff'
  primary-container: '#0072e5'
  on-primary-container: '#fefcff'
  inverse-primary: '#abc7ff'
  secondary: '#446464'
  on-secondary: '#ffffff'
  secondary-container: '#c6e9e9'
  on-secondary-container: '#4a6a6a'
  tertiary: '#9d3f00'
  on-tertiary: '#ffffff'
  tertiary-container: '#c45100'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#004590'
  secondary-fixed: '#c6e9e9'
  secondary-fixed-dim: '#abcdcd'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#2c4c4c'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb693'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7a2f00'
  background: '#f9f9ff'
  on-background: '#181c23'
  surface-variant: '#e0e2ed'
typography:
  h1:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 1.5rem
  margin: 2rem
---

## Brand & Style

The design system is anchored in the concept of "Intelligent Hydration." It balances the precision of high-end agricultural technology with the organic, life-giving essence of water. The brand personality is sophisticated, reliable, and effortless, targeting luxury homeowners and professional estate managers who value both aesthetic beauty and environmental stewardship.

The aesthetic fuses **Minimalism** with **Glassmorphism**. High-fidelity interfaces utilize generous whitespace to evoke a sense of calm and clarity. Fluidity is expressed through soft, organic shapes and subtle motion, while technical grounding is provided by structured Slate accents. The goal is a UI that feels as refreshing and transparent as water itself.

## Colors

The palette is designed to reflect the interplay between water and earth. 

*   **Deep Azure** acts as the primary driver, used for key actions and brand-critical information.
*   **Slate** provides the professional depth required for a high-end tool, used primarily for text, borders, and grounding elements.
*   **Vibrant Teal** is reserved for active states, signifying "flow" and system health.
*   **Soft Aqua** is used for decorative "liquid" elements, secondary data visualizations, and background washes.
*   **Backgrounds** remain predominantly white, using Slate-tinted grays (`#F5F7F8`) to define distinct content zones without breaking the minimalist flow.

## Typography

This design system utilizes a dual-font strategy. **Montserrat** provides a geometric, modern confidence for headings, suggesting the precision of the hardware. **Inter** is used for all functional body text and UI labels to ensure maximum legibility and a clean, systematic feel across data-heavy dashboards.

Hierarchy is established through significant scale shifts and the use of Slate for primary text, ensuring that even dense irrigation schedules remain scannable.

## Layout & Spacing

The design system employs a **Fluid Grid** model with a 12-column structure for desktop and a 4-column structure for mobile. A rhythmic 8px base unit ensures consistency.

To maintain the luxury aesthetic, generous internal padding within cards and large margins between sections are mandatory. Elements should never feel "cramped"; rather, they should appear to float within the layout, echoing the spaciousness of a well-manicured landscape.

## Elevation & Depth

Depth is conveyed through a combination of **Glassmorphism** and **Ambient Shadows**. 

1.  **Glass Layers:** Top-level cards use a backdrop blur (20px to 30px) with a semi-transparent white fill (opacity 70-80%). They feature a 1px soft border in Slate-tinted white to catch the light.
2.  **Ambient Shadows:** Objects use highly diffused, low-opacity shadows. Instead of pure black, shadows are tinted with Deep Azure or Slate to maintain color harmony and prevent a "muddy" appearance.
3.  **Tonal Stacking:** Background surfaces use subtle gray tints to separate the navigation from the main canvas, creating a tiered hierarchy of information.

## Shapes

The shape language is defined by **Rounded** geometry. Base components use a 0.5rem radius, while larger containers like cards use 1rem to 1.5rem for a softer, more approachable presence.

A specific "Fluid" variation is used for data visualizations and decorative accents, utilizing non-uniform border radii (e.g., `60% 40% 30% 70% / 60% 30% 70% 40%`) to create organic, water-droplet shapes that feel dynamic rather than static.

## Components

### Liquid Progress Bars
Used for soil moisture levels and water usage tracking. These feature a horizontal fill with a subtle wave-motion animation at the leading edge. Gradients transition from Soft Aqua to Deep Azure to represent volume.

### Instant Toggle
Switches for zone control are oversized for tactile ease. The "Off" state is Slate with a recessed shadow; the "On" state transforms into a Vibrant Teal glow with a slight outer bloom effect, signifying active irrigation.

### Weather-Specific Status Cards
High-fidelity glassmorphic cards that change their background subtle gradient based on local conditions (e.g., a warm golden hue for sunny, a soft cool blue for rain). Icons are thin-line, 1.5pt stroke weight, using Azure for highlights.

### Buttons & Inputs
*   **Primary Action:** Solid Deep Azure with white text, using a subtle pulse effect on hover.
*   **Ghost Buttons:** Thin Slate borders with high letter-spacing labels.
*   **Input Fields:** Clean, bottom-border-only design or light-gray fills with 0.5rem rounding, prioritizing a minimal footprint.