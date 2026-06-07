---
name: VisionHub
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
  on-surface-variant: '#bbc8d0'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#869399'
  outline-variant: '#3c494e'
  surface-tint: '#5ed4ff'
  primary: '#9de2ff'
  on-primary: '#003545'
  primary-container: '#00ccff'
  on-primary-container: '#005369'
  inverse-primary: '#006782'
  secondary: '#bfc8ce'
  on-secondary: '#293236'
  secondary-container: '#3f484d'
  on-secondary-container: '#adb6bc'
  tertiary: '#00effb'
  on-tertiary: '#00363a'
  tertiary-container: '#00d0db'
  on-tertiary-container: '#005459'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#bbe9ff'
  primary-fixed-dim: '#5ed4ff'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d63'
  secondary-fixed: '#dbe4ea'
  secondary-fixed-dim: '#bfc8ce'
  on-secondary-fixed: '#141d21'
  on-secondary-fixed-variant: '#3f484d'
  tertiary-fixed: '#74f5ff'
  tertiary-fixed-dim: '#00dbe7'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The design system is engineered for high-stakes industrial safety training within virtual reality environments. The brand personality is authoritative yet weightless, aiming to reduce cognitive load while maintaining a high-tech, professional atmosphere. It prioritizes clarity and immersion, ensuring that users feel they are interacting with a sophisticated heads-up display (HUD) rather than a traditional flat interface.

The visual style is **Glassmorphism**. By utilizing semi-transparent surfaces, background blurs, and subtle light refraction, the UI mimics a digital overlay that exists within a physical space. This approach maintains a sense of "spatial presence," allowing the industrial environment to remain visible behind the interface, thereby increasing safety and situational awareness during training.

## Colors
The palette is derived from the concepts of air, light, and digital precision. The default mode is **dark**, as it better represents an immersive VR environment and allows glowing elements to pop without causing eye strain.

- **Sky Blue (Primary):** Used for primary actions, progress indicators, and active states. It represents the "safe" path.
- **Cloud White (Secondary):** Used for primary text and high-contrast iconography. It provides maximum legibility against dark, blurred backgrounds.
- **Glass-Cyan (Tertiary):** A vibrant, electric accent used for data visualizations, scanning effects, and critical alerts.
- **Deep Space (Neutral):** A deep, slightly desaturated navy used for the base environment and solid backing layers when glass effects are toggled off.

## Typography
The typography system uses **Inter** for its exceptional readability and systematic feel, essential for technical instructions. To add a tech-forward, futuristic edge, **Space Grotesk** is introduced for labels, status indicators, and telemetry data.

All typography should maintain high contrast. On glass surfaces, a subtle text-shadow may be used to ensure legibility when the background environment is complex or brightly lit.

## Layout & Spacing
This design system utilizes a **fluid grid** model optimized for a field-of-view (FOV) of 120 degrees. Elements are spaced using an 8px base unit to ensure alignment and rhythmic consistency.

The layout philosophy emphasizes "peripheral clarity"—placing critical safety data in the center-focus area and auxiliary information at the edges of the HUD. Components are spaced generously to prevent accidental interactions in a 3D spatial environment where precision can be affected by physical movement.

## Elevation & Depth
In this design system, depth is conveyed through **Glassmorphism** and z-axis layering rather than traditional drop shadows.

1.  **Backdrop Blur:** Surfaces should utilize a 16px to 32px Gaussian blur to separate UI content from the industrial background.
2.  **Translucency:** Backgrounds are 40-60% opaque using the neutral or primary colors.
3.  **Inner Glow/Highlight:** Surfaces feature a 1px solid border at 20% opacity (Cloud White) on the top and left edges to simulate a light source reflecting off the "glass" edge.
4.  **Z-Axis Stacking:** Active panels "float" closer to the user (increased scale and decreased transparency), while inactive panels recede into the distance.

## Shapes
The shape language is **Rounded**. This softens the technical aesthetic, making the interface feel more approachable and modern. 

- **Containers:** Use `rounded-lg` (16px) for main training panels and information cards.
- **Interactive Elements:** Buttons and input fields use `rounded` (8px) to provide a distinct, clickable appearance.
- **Status Indicators:** Fully circular (pill-shaped) for binary states (e.g., ON/OFF or SAFE/DANGER).

## Components
Components are designed to look lightweight, as if they are projected light rather than physical objects.

- **Buttons:** Primary buttons use a solid Sky Blue fill with white text. Secondary buttons use a Glass-Cyan outline with a 10% fill. All buttons should have a hover state that increases the "glow" (outer shadow) effect.
- **Cards:** High-transparency glass layers with a 1px border. Title areas are separated by a thin, 10% opacity white line.
- **Input Fields:** Bottom-border only or very light ghost-outlines to keep the interface feeling "thin."
- **Chips/Status Badges:** Compact, pill-shaped elements with semi-transparent backgrounds and high-saturation text.
- **Telemetry Lists:** For industrial data, use monospaced numerals (from Space Grotesk) aligned to a strict vertical grid for rapid scanning.
- **Safety Gauges:** Custom circular progress indicators using the Tertiary Glass-Cyan color, featuring a pulse animation when reaching critical thresholds.
- **Spatial Waypoints:** Floating markers that exist in 3D space, mirroring the glass style of the HUD for visual continuity.