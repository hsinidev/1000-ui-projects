---
name: Star-Path
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#313031'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#ffb95a'
  on-secondary: '#462a00'
  secondary-container: '#c68315'
  on-secondary-container: '#3d2400'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#0d0f0f'
  on-tertiary-container: '#7a7c7c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#ffddb6'
  secondary-fixed-dim: '#ffb95a'
  on-secondary-fixed: '#2a1800'
  on-secondary-fixed-variant: '#643f00'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: 0.02em
  telemetry-data:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 24px
    letterSpacing: 0.05em
  body-standard:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  display-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
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
  panel-gap: 16px
---

## Brand & Style
This design system is engineered for the high-stakes environment of deep-space navigation, where clarity, speed of data acquisition, and atmospheric immersion are paramount. The personality is authoritative, technical, and cinematic—evoking the feeling of a sophisticated spacecraft bridge. 

The aesthetic leverages **Advanced Glassmorphism** to create a sense of depth and multi-layered information architecture. The UI should feel like a holographic projection floating against the vastness of space. The target audience includes interstellar pilots and navigators who require high-contrast telemetry that remains legible during long-duration missions in low-light cockpit environments. The emotional response is one of calm control amidst the unknown.

## Colors
The palette is optimized for extreme contrast and ocular comfort in dark environments. 

- **Primary (Deep Navy Blue):** Used for the foundational canvas and deep-layer surfaces. It represents the vacuum of space.
- **Secondary (Amber Glow):** Reserved for critical highlights, active navigational paths, and cautionary alerts. It provides a warm, high-visibility contrast against the cold navy.
- **Tertiary (Stark White):** Utilized exclusively for data readouts, coordinates, and primary labels to ensure maximum legibility.
- **Accents:** Neon Cyan is used for "Safe/Stable" telemetry, while a high-intensity Red is reserved for "Critical/Proximity" warnings.

All surfaces use varying opacities of the primary color to maintain the glass effect without sacrificing text contrast.

## Typography
The typography system uses a dual-font approach to balance futuristic branding with technical precision. 

**Space Grotesk** is used for headlines, navigation markers, and UI labels. Its geometric construction provides a modern, cutting-edge feel. **JetBrains Mono** is utilized for all telemetry, coordinates, and technical readouts; the monospaced nature ensures that fluctuating numerical data does not cause layout jitter, maintaining a stable visual field for the pilot. 

All technical data should be rendered with slightly increased letter spacing to prevent character blurring at high brightness levels.

## Layout & Spacing
The design system employs a **fixed-grid** architecture to mimic physical hardware consoles. The layout is organized into "Mission Sectors" (Panels).

- **Desktop (1440px+):** 12-column grid with wide 40px margins to keep critical data away from peripheral edges.
- **Tablet/Cockpit Display:** 8-column grid focusing on touch-accessible hit targets.
- **Mobile:** 4-column fluid grid for remote monitoring.

Spacing follows a 4px base unit. Elements are grouped in translucent "Container Pods" with a 16px gap between adjacent modules. Critical telemetry is always centered or placed in the top-right quadrant for immediate eye-scan availability.

## Elevation & Depth
Depth is communicated through **Glassmorphism** and light-based hierarchy rather than traditional shadows.

1.  **Level 0 (The Void):** Deep Navy (#0A0E1A) solid background.
2.  **Level 1 (Navigation Panels):** Background Blur (20px) with 10% opacity white fill and a 0.5px "Stark White" border at 20% opacity.
3.  **Level 2 (Active Modals/Alerts):** Background Blur (40px) with 15% opacity primary color and a 1px "Amber Glow" outer glow (4px spread).

Shadows are replaced by **Ambient Glows**. When an element is focused, it emits a subtle Amber or Cyan aura, simulating the light cast from a holographic display onto a glass surface.

## Shapes
This design system utilizes a "Soft" (0.25rem) corner radius for most panels to maintain a technical, engineered appearance while avoiding the aggression of sharp points. 

However, functional buttons and interactive "holographic" nodes use a "Pill-shaped" radius to clearly distinguish them from static informational displays. Ornamental elements, such as corner brackets on gauges, remain sharp (0px) to emphasize the precision instruments feel.

## Components
- **Holographic Buttons:** Transparent backgrounds with a 1px Amber border. On hover, the background fills with a 10% Amber tint and the border glow intensity increases.
- **Translucent Cards:** Used for grouping telemetry. They feature a "frosted" blur and thin, top-aligned accent lines in Amber.
- **Neon-Accented Gauges:** Circular or linear indicators using "Stark White" for scale markers and "Amber Glow" or "Cyan" for the current value needle/fill.
- **Telemetry Readouts:** JetBrains Mono text blocks, often paired with a small pulsing "Live" dot indicator to show real-time data streaming.
- **Proximity Alerts:** Full-frame translucent red overlays with a rhythmic "breath" animation for critical system failures.
- **Navigation Chips:** Small, high-contrast labels used for tagging astronomical objects, utilizing the `label-caps` typography style.