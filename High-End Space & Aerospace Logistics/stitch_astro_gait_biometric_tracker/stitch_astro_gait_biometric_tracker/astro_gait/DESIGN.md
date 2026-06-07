---
name: Astro-Gait
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#00a572'
  on-tertiary-container: '#00311f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
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
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
This design system centers on a **Kinetic-Biological** aesthetic tailored for the rigors of long-duration spaceflight. The interface serves as a high-precision medical instrument, blending the rigidity of aerospace engineering with the organic fluidity of human physiology.

The design style is a hybrid of **Glassmorphism** and **High-Contrast Instrumentation**. It utilizes translucent, layered surfaces to represent depth in microgravity environments, while employing sharp, glowing interactive elements to ensure immediate recognition of critical biometric data. The mood is clinical yet futuristic, prioritizing performance and clarity to mitigate cognitive load during extended missions.

## Colors
The palette is optimized for dark-mode orbital environments to reduce eye strain and preserve night vision.

- **Primary (Electric Violet):** Used exclusively for interactive states, active biological tracking, and critical kinetic paths. It possesses a "neon-gas" glow effect.
- **Secondary (Pure White):** Reserved for high-priority data readouts and primary labels to ensure maximum legibility against dark voids.
- **Background (Deep Slate):** A tiered series of desaturated dark blues and grays that provide spatial depth without total blackness.
- **Tertiary (Vital Green):** Used for nominal health statuses and "Go" flight configurations.
- **Accents:** Low-opacity violet washes are used for "spider" chart fills and translucent card backgrounds.

## Typography
The typography system balances technical precision with rapid scanability.

- **Headlines:** Use **Space Grotesk** for a geometric, futuristic feel that mimics aerospace hull markings.
- **Body:** Use **Inter** for sustained reading of medical logs and mission parameters, chosen for its exceptional legibility in low-light conditions.
- **Technical/Data:** **JetBrains Mono** is utilized for all numerical readouts, timestamps, and "Spider" chart axis labels, providing a monospaced "instrumentation" feel that ensures numbers align perfectly in shifting data tables.

## Layout & Spacing
The layout follows a **Fluid Grid** model with a heavy emphasis on "Safe Zones" to account for peripheral viewing during physical exertion or microgravity maneuvers.

- **Grid:** A 12-column system on desktop, collapsing to 4 columns on mobile/wrist-mounted displays.
- **Rhythm:** A 4px baseline grid ensures all components align with mathematical precision. 
- **Adaptation:** On mobile (handheld/EVA modules), margins are tightened and interactive targets are scaled up to accommodate gloved interaction or high-vibration environments. Large data visualizations reflow from side-by-side to vertical stacks.

## Elevation & Depth
Depth is communicated through **Glassmorphism** and light-emissive properties rather than traditional shadows.

- **Base Layer:** The deepest Slate color, representing the "void."
- **Glass Surfaces:** Semi-transparent layers (10-20% opacity) with a heavy **Backdrop Blur (20px - 40px)**. These represent floating data panes.
- **Emissive Glow:** Active elements use a `0px 0px 12px` outer glow in Electric Violet to simulate light-emitting diodes (LEDs) and holographic projections.
- **Z-Axis Hierarchy:** Higher-order alerts are more opaque and have a subtle primary-colored inner border to "pop" from the background.

## Shapes
The shape language combines technical geometry with **biological-inspired curves**. 

Containers utilize a standard 0.5rem radius, but primary data containers and biological "spider" charts feature asymmetric or "squircle" curves to feel more organic. Interactive strokes use a variable weight—thin on the sides and slightly thicker at the "joints" or corners—to mimic skeletal structures.

## Components
- **Buttons:** High-contrast, filled Electric Violet for primary actions. Ghost buttons with glowing borders for secondary navigation. All buttons feature a 1px "micro-trim" border.
- **Glassmorphism Cards:** Use a 1px Pure White border at 10% opacity. The background is a Deep Slate blur.
- **Spider Charts:** Centralized biometric visualizations. The "web" lines are 0.5px Pure White, and the data area is a semi-transparent Electric Violet fill with glowing vertices.
- **Input Fields:** Bottom-bordered only, mimicking cockpit readouts. Active state triggers a vertical Violet pulse on the left edge.
- **Biometric Lists:** High-density rows with monospaced data on the right and "Biological Curve" sparklines on the left.
- **Status Chips:** Small, pill-shaped indicators. "Oxygen," "Heart Rate," and "Gait Symmetry" utilize Tertiary Green or Primary Violet depending on threshold status.