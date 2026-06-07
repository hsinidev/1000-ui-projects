---
name: Breathe-Ease
colors:
  surface: '#f7f9fc'
  surface-dim: '#d8dadd'
  surface-bright: '#f7f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f7'
  surface-container: '#eceef1'
  surface-container-high: '#e6e8eb'
  surface-container-highest: '#e0e3e6'
  on-surface: '#191c1e'
  on-surface-variant: '#3e4850'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f4'
  outline: '#6e7881'
  outline-variant: '#bdc8d1'
  surface-tint: '#00658d'
  primary: '#00658d'
  on-primary: '#ffffff'
  primary-container: '#00aeef'
  on-primary-container: '#003e58'
  inverse-primary: '#82cfff'
  secondary: '#4f6169'
  on-secondary: '#ffffff'
  secondary-container: '#d2e6ef'
  on-secondary-container: '#55676f'
  tertiary: '#8d4f00'
  on-tertiary: '#ffffff'
  tertiary-container: '#ea8c21'
  on-tertiary-container: '#572f00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c6e7ff'
  primary-fixed-dim: '#82cfff'
  on-primary-fixed: '#001e2d'
  on-primary-fixed-variant: '#004c6b'
  secondary-fixed: '#d2e6ef'
  secondary-fixed-dim: '#b6cad2'
  on-secondary-fixed: '#0b1e24'
  on-secondary-fixed-variant: '#374951'
  tertiary-fixed: '#ffdcc0'
  tertiary-fixed-dim: '#ffb876'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6b3b00'
  background: '#f7f9fc'
  on-background: '#191c1e'
  surface-variant: '#e0e3e6'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 48px
    letterSpacing: -0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-padding: 20px
  section-gap: 40px
---

## Brand & Style
The design system is centered on the concept of "Atmospheric Clarity." It targets patients and clinicians who require a high degree of precision without the anxiety often associated with medical software. The emotional response is one of calm, relief, and openness.

The style is a refined **Glassmorphism**, leveraging semi-transparent layers and background blurs to simulate the lightness of air. This approach eliminates visual "heaviness," replacing solid containment with "breathable" surfaces that maintain a clinical, professional edge through strict alignment and generous whitespace.

## Colors
The palette is intentionally limited to evoke a sterile yet soothing environment. 
- **Pure White (#FFFFFF)**: The foundation of the UI, used for the base canvas to maximize light and perceived airiness.
- **Sky Blue (#00AEEF)**: The primary action color, used for critical data points, active states, and the "Breathing-Rhythm" pulse motif.
- **Pale Azure (#E1F5FE)**: Used for large glass surfaces and "Liquid" fill states, providing a soft contrast against the white background.
- **Cloud Grey (#F5F7FA)**: Utilized for subtle structural dividers and secondary backgrounds to define hierarchy without creating hard stops.

## Typography
This design system utilizes **Inter** for its clinical precision and exceptional legibility at small sizes. The typographic hierarchy relies on weight and tracking rather than color to maintain the airy aesthetic. 

Headlines use semi-bold weights with slight negative letter-spacing to feel grounded. Data points (like lung capacity or O2 levels) utilize a light weight at large scales (`data-display`) to feel sophisticated and modern. All labels are strictly uppercase with increased letter-spacing to distinguish them from interactive body text.

## Layout & Spacing
The design system follows a **Mobile-First Fluid Grid**. Layouts are constructed with a 4-column system for mobile, prioritizing vertical flow and thumb-accessible hit targets. 

Generous whitespace is mandatory; sections should be separated by large gaps (`section-gap`) to allow the user's eyes to rest. Padding within glass cards should never drop below `lg` (24px) to ensure content never feels cramped. Alignment is strictly left-aligned for medical data to ensure rapid scanning.

## Elevation & Depth
Depth is created through **Backdrop Blurs** rather than traditional drop shadows. 
- **Surface Level 0:** The pure white base layer.
- **Surface Level 1 (Cards):** Background-blur (20px-30px), white fill at 70% opacity, and a 1px solid white border to simulate light hitting the edge of glass.
- **Floating Level 2 (Modals/Active):** Higher blur (40px) and a very soft, diffused Sky Blue shadow (10% opacity) to indicate priority.

The "Liquid" air-volume indicators use inner glows and subtle gradients rather than shadows to feel like contained fluid.

## Shapes
The shape language is consistently **Rounded**, avoiding sharp corners to maintain a friendly, organic feel. 
- Standard buttons and input fields use a `0.5rem` radius.
- Glass cards and liquid containers use a `1.5rem` radius (`rounded-xl`) to feel soft and approachable.
- The "Breathing-Rhythm" pulse motif uses continuous Bezier curves to avoid any jagged edges, reinforcing the "flow" of air.

## Components
- **Liquid Air Indicators**: Circular or pill-shaped containers with a dynamic Sky Blue fill that uses a "wave" animation at the meniscus level.
- **Glass Cards**: Semi-transparent containers with a subtle white border. Background content should be visible but heavily blurred to maintain legibility.
- **Action Buttons**: Solid Sky Blue for primary actions with white text. Ghost buttons (transparent with Sky Blue border) for secondary actions.
- **Pulse Motif**: A continuous, animated line graph representing the breathing rhythm, using a glowing 2px stroke of Sky Blue.
- **Input Fields**: Soft Grey (#F5F7FA) backgrounds that turn into "Glass" (semi-transparent) upon focus, with a Sky Blue bottom-border.
- **Lung Health Chips**: Small, pill-shaped indicators with Sky Blue backgrounds at 10% opacity and bold Sky Blue text for status updates.