---
name: Aura-Seating
colors:
  surface: '#f6f9ff'
  surface-dim: '#d4dbe2'
  surface-bright: '#f6f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef4fc'
  surface-container: '#e8eef6'
  surface-container-high: '#e3e9f1'
  surface-container-highest: '#dde3eb'
  on-surface: '#161c22'
  on-surface-variant: '#44474a'
  inverse-surface: '#2b3137'
  inverse-on-surface: '#ebf1f9'
  outline: '#75777b'
  outline-variant: '#c5c6cb'
  surface-tint: '#595f66'
  primary: '#1a2025'
  on-primary: '#ffffff'
  primary-container: '#2f353b'
  on-primary-container: '#989da5'
  inverse-primary: '#c1c7cf'
  secondary: '#5c5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dee0e0'
  on-secondary-container: '#606363'
  tertiary: '#002518'
  on-tertiary: '#ffffff'
  tertiary-container: '#003d2a'
  on-tertiary-container: '#00b382'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde3eb'
  primary-fixed-dim: '#c1c7cf'
  on-primary-fixed: '#161c22'
  on-primary-fixed-variant: '#41474e'
  secondary-fixed: '#e1e3e3'
  secondary-fixed-dim: '#c4c7c7'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#444748'
  tertiary-fixed: '#6cfbc4'
  tertiary-fixed-dim: '#4adea9'
  on-tertiary-fixed: '#002115'
  on-tertiary-fixed-variant: '#005139'
  background: '#f6f9ff'
  on-background: '#161c22'
  surface-variant: '#dde3eb'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: 0.04em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  data-metric:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '300'
    lineHeight: '1.0'
    letterSpacing: -0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding-mobile: 24px
  container-padding-desktop: 64px
  gutter: 24px
  section-gap: 80px
---

## Brand & Style

The design system is rooted in the intersection of high-precision biomechanics and serene wellness. It targets an audience that values both technical excellence and aesthetic tranquility. The visual narrative balances the clinical accuracy of an orthopedic tool with the premium, airy feel of a high-end spa or design studio.

The style is a sophisticated blend of **Minimalism** and **Glassmorphism**, characterized by:
- **Bio-mechanical Precision:** Technical data is presented with surgical clarity using high-fidelity 3D visualizations.
- **Organic Serenity:** The rigid nature of hardware is softened by "liquid" organic shapes and fluid transitions.
- **Ethereal Depth:** Layers appear to float in a luminous, atmospheric space, utilizing semi-transparent "silk" surfaces and soft, ambient glows.

## Colors

The color strategy for this design system utilizes a restricted, high-end palette to maintain a calm, focused environment.

- **Slate Grey (#2F353B):** Used for primary typography, structural icons, and deep semantic meaning. It provides the grounding force against the lighter elements.
- **Silk White (#F9FBFB):** The primary background color. It is slightly cool-toned to evoke a sterile yet premium "laboratory" feel.
- **Mint (#4ADEA9):** The energetic "pulse" of the system. Reserved for active states, health indicators, calibration success, and primary calls to action.
- **Atmospheric Accents:** Subtle gradients moving from Silk White to ultra-pale Mint are used for glassmorphic backgrounds to create a sense of oxygen and air.

## Typography

This design system utilizes **Geist** for its technical precision and "developer-grade" clarity, which reinforces the calibration aspect of the product. 

- **Tracking:** Generous letter-spacing (0.01em to 0.1em) is applied to all levels except large metrics to create an expensive, airy feel.
- **Hierarchy:** High contrast between light weights (300) for large displays and medium weights (500-600) for functional labels.
- **Data Display:** Numerical values (pressure points, angles) should use the `data-metric` style with tighter tracking to feel like an integrated part of a 3D visualization.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with significant negative space to prevent cognitive overload during technical calibration.

- **Grid:** A 12-column grid for desktop and a 4-column grid for mobile. 
- **Rhythm:** An 8px linear scale is used. However, section-level spacing is intentionally "over-sized" (80px+) to maintain the serene aesthetic.
- **Adaptation:** On mobile, 3D visualizations occupy the top 40% of the viewport, with calibration controls sliding up from the bottom in glassmorphic sheets. On desktop, the visualization is centered or offset to the left, with data rich side-panels on the right.

## Elevation & Depth

Depth in this design system is conveyed through transparency and "Atmospheric Diffusion" rather than traditional shadows.

- **Glassmorphism:** Primary cards and overlays use a 15% opacity Silk White fill with a heavy (40px+) backdrop blur. A 1px translucent border (Mint at 20% opacity) defines the edges.
- **Ambient Shadows:** Where shadows are required for separation, they are ultra-diffused, using a large blur radius (30px-50px) with low-intensity Slate Grey at 5% opacity.
- **Organic Layers:** Use "liquid" blobs in the background with varying levels of blur (60px-100px) and Mint hues to create a sense of depth and movement behind the UI.

## Shapes

The shape language reflects the "Bio-mechanical" theme by mixing geometric containers with organic inner elements.

- **Containers:** Standard UI cards and buttons use `rounded-lg` (16px) or `rounded-xl` (24px) for a soft, approachable feel.
- **Liquid Elements:** Visualization backgrounds and accent shapes use high-degree Bézier curves that mimic biological forms or fluid droplets.
- **Active Indicators:** Interaction states (like selected calibration zones) use perfectly circular or "squircle" masks.

## Components

- **Calibration Buttons:** Primary actions use a solid Mint fill with Slate Grey text. Secondary actions use glassmorphic "ghost" styles with a 1px Slate Grey border at 10% opacity.
- **Metric Chips:** Small, pill-shaped indicators for real-time data. Use a semi-transparent Slate Grey background with white Geist Mono text for a technical look.
- **3D Visualization:** The central chair model should be rendered in a monochromatic Slate Grey matte finish, with "Active Hotspots" pulsing in Mint.
- **Glass Sliders:** Adjustment sliders for lumbar or height should feature a thick, translucent track and a large, tactile Mint thumb.
- **Pressure Maps:** Use a gradient scale from Silk White (low pressure) to Mint (optimal) to Slate Grey (high pressure/danger), avoiding traditional red/yellow/green scales to maintain the specific palette.
- **Liquid Transitions:** Page transitions and modal appearances should use a fluid "expanding droplet" animation rather than a standard fade or slide.