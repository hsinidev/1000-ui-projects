---
name: TechNexus
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#dcb8ff'
  on-secondary: '#480081'
  secondary-container: '#7701d0'
  on-secondary-container: '#dcb7ff'
  tertiary: '#d3ffed'
  on-tertiary: '#00382a'
  tertiary-container: '#00f5c3'
  on-tertiary-container: '#006b54'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#efdbff'
  secondary-fixed-dim: '#dcb8ff'
  on-secondary-fixed: '#2c0051'
  on-secondary-fixed-variant: '#6700b5'
  tertiary-fixed: '#26ffcc'
  tertiary-fixed-dim: '#00e0b2'
  on-tertiary-fixed: '#002118'
  on-tertiary-fixed-variant: '#00513f'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  code-technical:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 20px
  margin: 24px
---

## Brand & Style

The design system is engineered to feel like a high-performance command center for the modern home. It balances technical precision with a welcoming, "connected" energy. The brand personality is authoritative and reliable, yet approachable enough for daily household use.

The visual style is a fusion of **Glassmorphism** and **High-Tech Minimalism**. By utilizing a deep matte black foundation, the interface reduces visual noise and eye strain, allowing vibrant functional elements—like connectivity paths and status indicators—to emerge with clarity. The aesthetic prioritizes a "tactile digital" feel, where elements have weight and presence through subtle gradients and layered transparency, mimicking high-end hardware interfaces.

## Colors

The palette is anchored by a primary matte black (#121212) to provide a sophisticated, low-glare canvas. Connectivity and system health are represented through a "vibrant-on-dark" logic:

- **Primary (Electric Cyan):** Used for active states, primary actions, and successful connectivity.
- **Secondary (Deep Purple):** Used for secondary interactions and logic-based grouping.
- **Tertiary (Neon Teal):** Reserved for technical data points and environmental sensors.
- **Gradients:** Multi-color linear gradients represent the flow of data and energy between devices. 

All interactive elements must maintain a high contrast ratio against the matte background to ensure accessibility in various lighting conditions typical of a home environment.

## Typography

This design system utilizes a dual-font strategy to differentiate between technical data and instructional content. **Space Grotesk** is used for headlines and display units, providing a geometric, futuristic character that reinforces the high-tech vibe. **Inter** is used for all body copy and technical guides to ensure maximum legibility and a clean, utilitarian feel.

For technical readouts and device IDs, use the `label-caps` style to create a clear visual distinction from standard prose. High line-heights are maintained in body text to assist readability during troubleshooting or setup tasks.

## Layout & Spacing

The layout philosophy follows an **8px grid system** optimized for touch-heavy app interfaces. The system uses a fluid grid for mobile and tablet views, transitioning to a 12-column fixed-max-width grid for desktop dashboards. 

Padding within cards and containers is generous (`md` or 24px) to emphasize the tactile, airy feel of the components. Interaction targets (buttons/inputs) are oversized to accommodate quick taps in a smart home setting. Grouping of related sensors should use `sm` (12px) spacing, while major section breaks should use `lg` (40px) to maintain a clear hierarchy.

## Elevation & Depth

Depth is established through **Matte Glassmorphism**. Elements do not use traditional heavy drop shadows; instead, they utilize:

1.  **Backdrop Blurs:** Background surfaces use a 20px blur to create a sense of layered translucency over background gradients.
2.  **Inner Glows:** Interactive elements feature a subtle 1px inner border (white at 10% opacity) to simulate the edge of a physical glass panel.
3.  **Colored Glows:** Active or "On" states utilize a diffused ambient glow that inherits the color of the primary gradient (e.g., a cyan outer glow for an active smart light).
4.  **Tonal Stacking:** Higher elevation is communicated by increasing the opacity of the surface overlay rather than adding shadow distance.

## Shapes

The shape language is defined by "Soft Precision." The design system uses **Rounded (0.5rem base)** corners for all standard components. This level of roundedness softens the technical nature of the app, making it feel more consumer-friendly. 

Large container cards and glass panels should utilize `rounded-xl` (1.5rem) to emphasize the app-centric, modern aesthetic. Smaller elements like chips or status badges use the `rounded-lg` (1rem) setting to maintain a distinct "pill" silhouette when compared to primary action buttons.

## Components

### Buttons
Primary buttons are large and tactile, featuring a vibrant gradient background and a subtle 2px bottom shadow to imply a physical press. Secondary buttons use the "matte glass" style with a high-contrast border.

### Cards
Cards are the primary container for device controls. They must utilize the backdrop blur and a semi-transparent surface. Content inside cards should be vertically stacked, with the device status (e.g., "Connected") always positioned in the top right.

### Status Indicators
Status is communicated via a "Pulse" component—a small circular dot with an outer glowing ring. Green/Cyan indicates active, Purple indicates processing, and Red indicates a connection break.

### Input Fields
Inputs are dark-themed with a subtle 1px stroke. Upon focus, the stroke should transition to the primary gradient color with a soft outer glow.

### Connectivity Map
A custom component unique to this system is the "Connection Path," a stylized line or curve with a flowing gradient animation that visually links the hub to its peripheral devices.