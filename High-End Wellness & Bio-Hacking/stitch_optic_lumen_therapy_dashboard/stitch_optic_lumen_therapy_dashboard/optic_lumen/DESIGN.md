---
name: Optic-Lumen
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
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#909191'
  on-tertiary-container: '#282a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 2.25rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 1.5rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: '1.5'
  technical-data:
    fontFamily: JetBrains Mono
    fontSize: 1rem
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  grid_columns: '12'
  gutter: 24px
---

## Brand & Style

This design system is engineered for professional medical environments, blending clinical precision with an immersive, atmospheric aesthetic. The interface prioritizes high-intensity focus, utilizing a dark-mode-centric approach to eliminate visual noise and emphasize the therapeutic light frequency.

The style is a hybrid of **High-Contrast Minimalism** and **Tactile Medical Instrumentation**. It avoids decorative flourishes in favor of functional data visualization and high-end hardware metaphors. The emotional response is one of reliability, technical mastery, and physiological efficacy. Use "Glow" effects not as ornament, but as a direct simulation of light intensity and treatment status, making the interface feel like an extension of the physical red-light hardware.

## Colors

The color strategy is strictly functional. 
- **Signal Red (#FF0000):** Reserved exclusively for active therapy states, critical alerts, and primary interactive highlights. It represents the 660nm-850nm light spectrum.
- **Charcoal (#121212):** The foundation of the interface, providing a void-like depth that minimizes screen glare in clinical settings.
- **Off-White (#F5F5F5):** Used for maximum legibility of data and technical labels, ensuring high-contrast readability against the dark background.
- **Surface Accents:** Mid-range grays (#2A2A2A) define secondary containers and inactive states to maintain a clear hierarchy of importance.

## Typography

The typographic system utilizes a tiered approach to reinforce the scientific narrative. 
- **Headlines:** Space Grotesk provides a modern, geometric technicality for primary navigation and mode selection.
- **Body:** Inter ensures high-speed legibility for instructional content and patient data.
- **Technical/Data:** JetBrains Mono is utilized for all fluctuating values (mW/cm², Joules, Timers) to mimic the look of high-precision digital readouts. 

Text-shadows using `rgba(255, 0, 0, 0.5)` should be applied to active numerical values to simulate a glowing LED hardware display.

## Layout & Spacing

This design system employs a **Fixed Grid** model within a standard 12-column framework. The layout is structured to prioritize a "Cockpit" feel, where the most vital controls (Time, Intensity, Spectrum) are centered or placed in high-visibility zones.

Spacing is generous around interactive touch targets (minimum 48px) to prevent errors during operation. Components use a modular 4px base unit to ensure alignment is mathematically precise, reflecting the internal rigor of medical engineering. Containers should use `lg` (40px) padding to maintain a feeling of luxury and specialized utility.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Photometric Glow**. 
- **Base Layer:** Charcoal (#121212).
- **Surface Layer:** Subtle 1px borders of `rgba(245, 245, 245, 0.1)` define cards, with a deep `0px 20px 40px rgba(0, 0, 0, 0.5)` shadow.
- **Active State:** Elements currently emitting or controlling light receive an outer glow (`box-shadow: 0 0 15px rgba(255, 0, 0, 0.4)`) and an inner glow to suggest the component is "powered on."
- **Interaction:** Hover and active states should feel "pressable" through slight scaling (0.98x) and an increase in glow intensity, simulating a high-quality physical membrane switch.

## Shapes

To maintain a professional, medical-grade appearance, the shape language uses a **Soft (0.25rem)** rounding. This provides enough approachability to feel modern, while the predominantly sharp corners maintain a "precision-tooled" aesthetic. 

Large control panels and containers may use `rounded-lg` (0.5rem) to differentiate them from smaller buttons. Circular shapes are reserved strictly for circular light-emitter icons or "Session Start" buttons to create a clear visual distinction for primary actions.

## Components

### Buttons & Controls
Primary buttons use a solid Signal Red background with Off-White text. In an "Active" or "On" state, buttons emit a `box-shadow` of 10px–20px in red. Secondary buttons utilize a ghost style with a subtle white border.

### Precision Sliders
Sliders for intensity (0–100%) should feature a "light trail" effect, where the track to the left of the thumb glows red, increasing in intensity as the value rises.

### Cards
Cards are the primary container for data groups. They feature a charcoal background slightly lighter than the page background (#1A1A1A), a hairline border, and deep shadows. Headers within cards use `label-caps` for a "spec-sheet" feel.

### Status Indicators
Small, circular "LED" indicators.
- **Off:** Dim gray.
- **Warming Up:** Pulsing Amber.
- **Active:** Glowing Signal Red.

### Treatment Timer
A large-scale display component using `display-xl` typography. The numbers should have a `text-shadow` that flickers slightly upon session completion to provide a haptic-visual alert.