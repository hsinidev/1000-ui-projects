---
name: Atmos-Office
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#414755'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc1'
  primary: '#0058bc'
  on-primary: '#ffffff'
  primary-container: '#0070eb'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#9e3d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#c64f00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb595'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  stat-value:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '300'
    lineHeight: '1'
    letterSpacing: -0.03em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 32px
  gutter: 24px
  element-gap: 16px
---

## Brand & Style
The design system is defined by a "Clinical & Airy" aesthetic, prioritizing a sense of environmental purity and high-tech reliability. It targets professional office settings where air quality is a measurable component of productivity. 

The style merges **Minimalism** with **Glassmorphism**. The visual language must feel "breathable"—using generous whitespace to prevent cognitive load and a "sterile but refreshing" palette to evoke a sanitized, safe atmosphere. Surfaces are translucent, suggesting the invisibility of clean air, while interactive elements use high-precision medical blue to signal technological competence.

## Colors
This design system utilizes a high-brightness palette to maintain a clinical feel. 

- **Pure White (#FFFFFF):** Used for base surfaces and primary containers to ensure a sterile, clean background.
- **Medical Blue (#007AFF):** Reserved for primary actions, critical status data, and active "on" states. It represents trust and precision.
- **Glass-Cyan (#E0F7FA at 60%):** The signature overlay color. It should be applied with a heavy backdrop blur (20px+) to create the airy, glassmorphic effect for modals, dropdowns, and floating controllers.
- **Background:** A very faint off-white (#F8FAFC) is used for the application canvas to allow pure white cards to "pop" with soft depth.

## Typography
The system uses **Inter** exclusively to achieve a systematic and utilitarian feel. 

Typography should be treated with generous leading (line height) to reinforce the "airy" theme. Large display sizes for air quality indices (AQI) use a lighter font weight (300) to feel sophisticated and modern, while functional labels use a heavier weight (600) with increased letter spacing for immediate legibility in a medical/technical context.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop/tablet control panels, centered on the screen to evoke a sense of balance. 

A 12-column grid is used with wide 24px gutters. Spacing is strictly based on an 8px scale. To maintain the "breathable" personality, the design system mandates "Negative Space Zones"—large areas of at least 64px surrounding primary data visualizations to ensure the UI never feels cluttered or "stuffy."

## Elevation & Depth
Depth is created through **Glassmorphism** and **Ambient Shadows** rather than traditional stacking.

- **Surface Layers:** Primary containers use Pure White with a very soft, highly diffused shadow (0px 10px 40px rgba(0, 122, 255, 0.05)). The blue tint in the shadow reinforces the brand color.
- **Overlays:** Glass-Cyan surfaces use a `backdrop-filter: blur(24px)` and a subtle 1px inner border in white (opacity 40%) to simulate a glass edge.
- **Interactive Depth:** When pressed, buttons should not move "down" but rather increase in shadow spread to feel as if they are glowing or floating higher.

## Shapes
The shape language is organic and approachable. This design system uses a minimum corner radius of **24px** (pill-shaped) for all main containers and buttons. Smaller components like checkboxes use a 12px radius. The extreme roundedness is intended to contrast with the "clinical" sharpness of the typography, making the technology feel friendly and safe for a desktop environment.

## Components
- **Liquid-Style Progress Bars:** Track containers are filled with a semi-transparent Medical Blue. The progress indicator itself should have a subtle "wave" animation or a rounded, organic leading edge, simulating a fluid level.
- **Buttons:** Primary buttons are solid Medical Blue with white text. Secondary buttons are Glass-Cyan with Medical Blue text and no border.
- **Status Indicators:** Clear, circular "halos" that pulse slowly. Green for "Pure," Blue for "Filtering," and Amber for "Service Needed."
- **Cards:** Pure White background with 24px+ corner radius. Information is grouped with thin, light-gray dividers (1px, #E2E8F0) or simple whitespace.
- **Input Fields:** Large, pill-shaped fields with a subtle Glass-Cyan background on focus. Text is always centered for a balanced, minimalist appearance.
- **Air Quality Rings:** A custom component—a thin, circular gauge that uses a gradient of Medical Blue to Glass-Cyan to visualize air flow intensity.