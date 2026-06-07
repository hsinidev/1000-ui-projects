---
name: Aegis Precision
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a29'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#c6c4df'
  on-secondary: '#2f2e43'
  secondary-container: '#47475d'
  on-secondary-container: '#b8b6d0'
  tertiary: '#ffffff'
  on-tertiary: '#303030'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#646464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#e2e0fc'
  secondary-fixed-dim: '#c6c4df'
  on-secondary-fixed: '#1a1a2e'
  on-secondary-fixed-variant: '#45455b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
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
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  telemetry:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
  density-tight: 8px
  density-comfortable: 24px
---

## Brand & Style

The design system is engineered to project an aura of absolute security, vigilance, and luxury. It targets high-net-worth individuals who demand both aesthetic sophistication and uncompromising functional authority. The brand personality is "The Silent Sentinel"—unobtrusive until required, then clinical and decisive.

The visual style is a fusion of **Minimalism** and **Glassmorphism**. It utilizes a dark, high-contrast environment to simulate a command-center atmosphere. The interface relies on density and precision, using hairline strokes and metallic finishes to evoke the feeling of high-end surveillance hardware. Every element is designed to feel "bolted down" and impenetrable, utilizing a mathematical rhythm that suggests technological superiority.

## Colors

The palette is anchored in high-contrast neutrals to maintain focus on surveillance feeds. **Platinum Silver** serves as the primary interactive and structural color, providing a metallic, premium sheen. **Deep Indigo** is used for background layering to provide depth and a "night-vision" context, while **Black** provides the absolute foundation of the UI.

Alerting uses a high-chroma Red and Amber. These are the only vibrant colors allowed, ensuring that "Human Detected" events or system breaches immediately command the user's optical periphery. Gradients should be used sparingly, restricted to subtle "brushed metal" linear transitions on primary buttons and headers.

## Typography

This design system utilizes **Inter** for its clinical precision and exceptional legibility at small sizes—critical for telemetry data and timestamps. The typographic hierarchy is designed to be authoritative and sharp.

Headers utilize tighter letter-spacing and heavier weights to feel "heavy" and established. A specialized "Label-Caps" style is used for categorization and system status to mimic military-grade labeling. All body text must maintain a high contrast ratio against the dark backgrounds to ensure clarity in low-light residential environments.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for primary dashboards to ensure that monitoring zones remain in consistent, predictable locations. A 12-column system is used for desktop views, with a focus on high-density information clusters.

Spacing is governed by a 4px baseline grid. Elements are tightly packed to create a "technical" look, but separated by clear, 1px Platinum Silver borders. This density suggests a wealth of data and professional-grade capability. Internal margins within containers are kept strict to maintain the impenetrable, structural feel of the system.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Metallic Tonal Layers** rather than traditional shadows. 

1.  **Base Layer:** Solid Black (#000000).
2.  **Surface Layer:** Deep Indigo (#1A1A2E) at 60% opacity with a 20px backdrop blur.
3.  **Interactive Layer:** Platinum Silver hairline borders (1px) with a subtle inner glow to simulate light catching the edge of a metal plate.
4.  **Overlay Layer:** Absolute Platinum Silver text or high-contrast status badges.

Avoid soft, diffused shadows. Instead, use "Hard Elevation"—distinct changes in border luminosity or background opacity to signal that an element is positioned above another.

## Shapes

The shape language is primarily **Sharp**. A very subtle 0.25rem (4px) radius is applied to main containers to provide a "machined" look, preventing the UI from feeling dated or overly aggressive while maintaining a defensive posture. 

Buttons and input fields should strictly adhere to this minimal rounding. Circular shapes are reserved exclusively for camera lenses, status pips, and biometric indicators to provide a functional contrast against the rectangular architectural grid.

## Components

### Buttons
Primary buttons feature a vertical linear gradient (Platinum Silver to a slightly darker steel grey) with black text. They should feel like physical, machined toggles. Secondary buttons are "Ghost" style with a 1px Silver border.

### Chips & Badges
"Human Detected" badges must use a solid Red background with White text and a subtle outer pulse animation. System status chips (e.g., "Online") use Deep Indigo with a 1px Silver border and a small, glowing green pip.

### Lists & Telemetry
Lists of events use alternating background opacities (Deep Indigo at 20% and 40%) to maintain scanability without needing dividers. All timestamps use the "Telemetry" typography style.

### Input Fields
Inputs are recessed (inset shadow) with a Black background and a Platinum Silver border that glows slightly (2px spread) when focused.

### Cards & Panels
Panels use the Glassmorphism specification: Deep Indigo tint, backdrop blur, and a 1px Silver top-border to catch "overhead light."

### Specialized Components
- **The Sight-Line:** A crosshair element used in live feeds to indicate the center of the camera's focus.
- **The Threat Level Meter:** A vertical segmented bar indicating environmental security status, transitioning from Silver to Amber to Red.