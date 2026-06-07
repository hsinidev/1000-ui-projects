---
name: Nuage-Luxe
colors:
  surface: '#fcf8f8'
  surface-dim: '#ddd9d9'
  surface-bright: '#fcf8f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f3'
  surface-container: '#f1eded'
  surface-container-high: '#ebe7e7'
  surface-container-highest: '#e5e2e2'
  on-surface: '#1c1b1c'
  on-surface-variant: '#45474b'
  inverse-surface: '#313030'
  inverse-on-surface: '#f4f0f0'
  outline: '#76777b'
  outline-variant: '#c6c6cb'
  surface-tint: '#5d5e64'
  primary: '#1a1c21'
  on-primary: '#ffffff'
  primary-container: '#2f3136'
  on-primary-container: '#98999f'
  inverse-primary: '#c5c6cc'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#211b14'
  on-tertiary: '#ffffff'
  tertiary-container: '#373028'
  on-tertiary-container: '#a2978d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e8'
  primary-fixed-dim: '#c5c6cc'
  on-primary-fixed: '#191c20'
  on-primary-fixed-variant: '#45474c'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ede0d4'
  tertiary-fixed-dim: '#d0c4b9'
  on-tertiary-fixed: '#211b13'
  on-tertiary-fixed-variant: '#4d453d'
  background: '#fcf8f8'
  on-background: '#1c1b1c'
  surface-variant: '#e5e2e2'
typography:
  headline-display:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Bodoni Moda
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
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
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-point:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 24px
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding-desktop: 64px
  container-padding-mobile: 24px
  gutter: 24px
  element-gap: 16px
---

## Brand & Style

The design system is engineered for the intersection of high-fashion and aerospace technology. It targets an ultra-high-net-worth audience, evoking the sensation of a private jet interior—hushed, exclusive, and intuitively responsive. The brand personality is poised and serene, favoring understated luxury over loud branding.

The UI style is defined as **Refined Neumorphism**. Unlike the heavy, "plastic" aesthetics of early Neumorphism, this design system uses microscopic elevation changes to create a tactile, soft-touch surface. It prioritizes high-contrast typography and a minimalist layout to ensure that biometric data and environmental controls feel like physical extensions of the seating architecture. The emotional goal is to provide the user with a sense of total mastery and biological calm.

## Colors

The color palette is anchored by **Crisp White**, used as a matte base to simulate high-grade synthetic leather and aerospace composites. 

- **Primary Text & Depth:** A **Deep Grey** (almost obsidian) provides the necessary contrast for legibility and defines the deep shadows of the Neumorphic recesses.
- **Accents:** **Rose Gold** is used sparingly for active states, critical biometric indicators, and focal points in the seating adjustment dials.
- **Surface Logic:** Depth is achieved not through color shifts, but through light physics. Surfaces use a "Soft-UI" approach where elements are the same color as the background, distinguished only by a light highlight on the top-left and a soft shadow on the bottom-right.

## Typography

The typography strategy leverages high-contrast serif and sans-serif pairings to reinforce the "High-Fashion" narrative.

- **Headlines:** Uses **Bodoni Moda** to provide an editorial, luxury feel. The high stroke contrast of the serif echoes fashion mastheads.
- **Body:** Uses **Hanken Grotesk** for its contemporary, clean, and highly legible profile. It remains unobtrusive while feeling premium.
- **Data & Labels:** Uses **Geist** for biometric readouts and technical labels. Its monospaced-influenced precision suggests technological advancement and biometric accuracy. All labels should be set in uppercase with tracking increased to 10% for a breathable, airy feel.

## Layout & Spacing

The design system utilizes a **Fluid-Fixed Hybrid** grid. While the overall container stretches to accommodate wide-format cockpit or armrest displays, the content modules are centered with generous "safe-zone" margins.

- **Spacing Rhythm:** Based on an 8px linear scale. 
- **Layout Philosophy:** Extreme whitespace is utilized to prevent "control claustrophobia." Each biometric card or seating toggle is given a wide berth (minimum 32px) to ensure the user feels calm and unhurried.
- **Responsiveness:** On mobile/handheld controllers, the layout collapses into a single-column scroll with increased touch targets (min 48px height) to accommodate the tactile nature of the Neumorphic components.

## Elevation & Depth

Depth in this design system is architectural rather than graphical. There are no "floating" elements; everything is either extruded from or recessed into the primary surface.

- **Extruded (Buttons/Cards):** Used for interactive elements. These feature a top-left highlight (#FFFFFF at 80% opacity) and a bottom-right shadow (#D1D9E6 at 50% opacity). The blur radius is typically double the distance of the offset to ensure "softness."
- **Recessed (Inputs/Toggles):** Used for biometric data fields and track-based sliders. The shadows are inverted, creating an "inset" look that suggests the screen has been physically molded.
- **Glassmorphism Overlay:** Occasionally used for high-level system notifications, utilizing a 20px backdrop blur and a thin 1px Rose Gold border to separate the alert from the tactile background.

## Shapes

The shape language mimics the ergonomic curves of luxury seating.

- **Primary Radius:** Standard components use a 16px (1rem) radius to feel soft to the touch.
- **Biometric Circles:** Circular dials and heart-rate monitors are perfect circles to represent the organic nature of human biology.
- **Interactions:** When a Neumorphic button is pressed, it transitions from "Extruded" to "Recessed" via a CSS inset shadow, providing a physical "click" sensation in the UI.

## Components

### Neumorphic Adjustment Toggles
These appear as soft-molded switches. The active state is indicated by a subtle Rose Gold glow emanating from the "recessed" track, suggesting energy flow.

### Circular Biometric Dials
Used for temperature, recline angle, and lumbar support. The dial features a "brushed metal" texture effect using a subtle conical gradient in Deep Grey, with a Rose Gold needle or indicator light.

### Biometric Data Cards
Sleek, extruded surfaces with minimal borders. They display heart rate, oxygen levels, and "calmness scores." These cards use **Geist** for numeric data to maintain a technical, clinical edge within the luxury environment.

### Buttons
Buttons do not have distinct background colors; they are the same color as the surface. Their presence is communicated solely through Neumorphic elevation. Text within buttons is either Deep Grey (default) or Rose Gold (primary action).

### Input Fields
Designed as "wells" sunk into the UI surface. They use a light inner shadow to create depth, with a thin Rose Gold cursor.