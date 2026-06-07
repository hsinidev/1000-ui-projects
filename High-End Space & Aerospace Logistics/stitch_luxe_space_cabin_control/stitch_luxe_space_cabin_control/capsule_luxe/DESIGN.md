---
name: Capsule-Luxe
colors:
  surface: '#121318'
  surface-dim: '#121318'
  surface-bright: '#38393e'
  surface-container-lowest: '#0d0e12'
  surface-container-low: '#1a1b20'
  surface-container: '#1e1f24'
  surface-container-high: '#292a2f'
  surface-container-highest: '#343439'
  on-surface: '#e3e2e8'
  on-surface-variant: '#c5c6d2'
  inverse-surface: '#e3e2e8'
  inverse-on-surface: '#2f3035'
  outline: '#8e909c'
  outline-variant: '#444650'
  surface-tint: '#b3c5ff'
  primary: '#b3c5ff'
  on-primary: '#0d2c6e'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#435b9f'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#272929'
  on-tertiary-container: '#8f9090'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#121318'
  on-background: '#e3e2e8'
  surface-variant: '#343439'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-label:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-value:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  margin-main: 24px
  gutter: 16px
  unit-base: 8px
  stack-sm: 12px
  stack-lg: 32px
---

## Brand & Style

This design system is tailored for the elite space traveler, blending the heritage of executive aviation with the futuristic demands of orbital tourism. The brand personality is authoritative yet welcoming, prioritizing quiet luxury over technological clutter.

The visual style employs **Soft-UI / Neumorphism** to create a tactile, physical connection between the traveler and the cabin environment. In a zero-gravity or low-light setting, the UI mimics the physical extrusion of premium materials—brushed metals and lacquered surfaces. High-contrast accents ensure legibility and a sense of "gold-standard" service, while the deep indigo depths of the palette mirror the vastness of space outside the viewport.

## Colors

The palette is anchored in **Royal Blue (#002366)**, serving as the primary atmospheric base. To optimize for low-light cabin environments, the system utilizes a "Deep Dark" mode where the background is a further desaturated version of the primary blue, allowing interactive elements to emerge through light and shadow.

**Champagne Gold (#D4AF37)** is used sparingly as a high-status accent for critical controls, active states, and brand signatures. **Clean White (#FFFFFF)** is reserved for high-priority data and primary labels to ensure maximum AA/AAA accessibility against the dark background.

## Typography

The typographic hierarchy utilizes a tri-font system to delineate function:
1. **Headings:** Noto Serif provides an editorial, prestigious feel, signaling comfort and luxury.
2. **Body:** Inter ensures frictionless legibility for descriptive text and instructions.
3. **Technical Data:** Space Grotesk is employed for environmental readings (Oxygen, G-Force, Orbital Velocity), providing a clean, futuristic precision that contrasts with the classical serif.

On mobile devices, display sizes are capped at 32px to maintain a sophisticated, non-aggressive presence. Large letter spacing is applied to uppercase labels to enhance readability in vibrating or low-gravity conditions.

## Layout & Spacing

This design system follows a **Fluid Grid** model optimized for handheld mobile use. The standard horizontal margin is 24px, providing a spacious, premium "frame" for the content. 

A strict 8px rhythmic scale governs vertical spacing. Elements are grouped into tactile "pods" with 16px gutters. Given the executive nature of the interface, whitespace (or "space-blue-space") is used as a luxury asset, preventing the UI from feeling cramped. Touch targets are rigorously maintained at a minimum of 48x48px to account for the potential of slight physical instability during flight.

## Elevation & Depth

Depth is the primary communicator of interactivity. This design system uses **Neumorphism** with a refined, executive constraint:
- **Concave/Pressed:** Used for inactive states or container backgrounds to suggest a molded interior.
- **Convex/Extruded:** Used for primary buttons and toggles. These features use two shadows: a "top-left" light highlight (White at 5-10% opacity) and a "bottom-right" deep shadow (Black at 40% opacity).
- **Gold Glow:** High-priority active elements (like the "Call Purser" or "Oxygen Control") may feature a faint, inner-glow using the Champagne Gold palette to suggest "live" energy.

## Shapes

The shape language reflects the organic, pressurized curves of a spacecraft cabin. A **Rounded (0.5rem)** base is used for all functional elements to avoid sharp "hostile" corners.

Large containers and modal sheets use **rounded-xl (1.5rem)** to create a soft, "cocoon-like" feel. Interactive chips and pill-selectors use a full radius (Pill-shaped) to distinguish themselves from structural cabin data cards.

## Components

### Buttons
Primary buttons are extruded Neumorphic forms. The text is rendered in Space Grotesk Bold. In their active state, the button appears "pressed" (inner-shadow) and the text shifts from White to Champagne Gold.

### Cards
Cabin data cards (e.g., Temperature, Lighting levels) use a subtle concave "inset" look. They serve as the background for data-rich overlays.

### Inputs / Sliders
Sliders are critical for cabin lighting and window opacity. The track is an inset "trough," while the thumb is a highly-polished Champagne Gold sphere that appears to sit on top of the glass.

### Chips
Status indicators (e.g., "Docked," "Atmosphere Stable") are small, high-contrast pills with a subtle outer glow to ensure they are the first thing a traveler sees when glancing at the device.

### Specialized: Viewport Toggle
A unique component for this system is the "Viewport Control," a large circular dial that mimics the cabin's porthole, allowing the traveler to digitally tint the actual windows of the craft. It uses a heavy Neumorphic bezel.