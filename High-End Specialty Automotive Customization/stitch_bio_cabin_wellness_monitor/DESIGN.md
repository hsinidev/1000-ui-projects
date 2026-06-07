---
name: Bio-Cabin Design System
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#434843'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#5c5d6e'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1f5'
  on-secondary-container: '#626374'
  tertiary: '#2f4633'
  on-tertiary: '#ffffff'
  tertiary-container: '#465e49'
  on-tertiary-container: '#bbd6bb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#e1e1f5'
  secondary-fixed-dim: '#c5c5d8'
  on-secondary-fixed: '#191b29'
  on-secondary-fixed-variant: '#444655'
  tertiary-fixed: '#ceeace'
  tertiary-fixed-dim: '#b2ceb3'
  on-tertiary-fixed: '#09200f'
  on-tertiary-fixed-variant: '#354c38'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  vital-display:
    fontFamily: Atkinson Hyperlegible Next
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  label-sm:
    fontFamily: Atkinson Hyperlegible Next
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  stack-gap: 16px
  inline-gap: 12px
  safe-area-bottom: 34px
---

## Brand & Style

This design system is anchored in the concept of "Biological Serenity." It reimagines the high-tech vehicle cabin as a living, breathing ecosystem rather than a cold machine. The target audience includes health-conscious commuters and long-distance travelers who view their vehicle as a sanctuary for mental and physical recovery.

The visual style is a hybrid of **Soft-Minimalism** and **Glassmorphism**. By utilizing translucent layers and organic, non-linear movements, the interface avoids clinical rigidity. The emotional response is one of calm, empathy, and safety—ensuring the driver feels monitored and cared for, never surveilled.

## Colors

The palette is derived from natural landscapes to lower cortisol levels.
- **Moss Green (#4A5D4E):** The grounding primary color, used for primary actions and structural hierarchy.
- **Lavender (#E6E6FA):** A soothing secondary tone used for focus states, "breathing" UI indicators, and supplementary health metrics.
- **Soft White (#F8F9FA):** The expansive background color that provides a "clean air" feel.
- **Tertiary Moss (#A8C3A9):** A desaturated green used for subtle gradients and secondary biological data.

Gradients should be extremely soft, typically moving from `Soft White` to a 5% opacity `Lavender` or `Moss Green` to simulate natural light filtering through leaves.

## Typography

Typography prioritizes clarity and compassion. **Plus Jakarta Sans** provides a modern, friendly geometric skeleton for general interface text. For critical health data and driver vitals, **Atkinson Hyperlegible Next** is utilized to ensure maximum readability and accessibility under various lighting conditions.

- **Headlines:** Use tight letter-spacing and bold weights to ground the interface.
- **Vital Metrics:** Numbers should be prominent, using the specialized legibility of Atkinson Hyperlegible to prevent misinterpretation of heart rate or oxygen levels.
- **Compassionate Copy:** All system messaging should use `body-lg` to remain legible and approachable.

## Layout & Spacing

The layout follows a **fluid, context-aware grid** designed for single-hand mobile use. Because this is for an in-car environment, tap targets are oversized (minimum 48x48dp).

- **Margins:** 24px horizontal margins provide "breathing room" against the edge of the device.
- **Vertical Rhythm:** Elements are stacked using an 8px base unit, with 16px or 24px gaps between major sections to maintain a sense of serenity and lack of clutter.
- **Vitals Grid:** Health summaries should use a 2-column card layout to maximize vertical space for real-time monitoring graphs.

## Elevation & Depth

This design system uses **Tonal Layers** and **Glassmorphism** to convey hierarchy. 
- **The Base:** The `Soft White` background acts as the primary floor.
- **Surface Level 1:** Cards use a high-transparency `Lavender` or `White` fill with a `24px` backdrop blur.
- **Surface Level 2:** Active modals or alerts use a soft shadow—`0px 10px 30px rgba(74, 93, 78, 0.08)`—to appear as if they are floating gently above the surface.
- **Outlines:** Instead of harsh borders, use 1px "ghost" strokes at 10% opacity of the primary `Moss Green` to define boundaries without interrupting the visual flow.

## Shapes

Shapes are "Biological," meaning they avoid sharp 90-degree angles. 
- **Standard Containers:** Use `rounded-lg` (16px) for cards and main UI modules.
- **Interactive Elements:** Buttons and input fields use `rounded-xl` (24px) or full pill-shapes to feel soft to the touch.
- **Organic Variance:** Progress bars and health rings should utilize "squircle" geometries rather than perfect circles to feel more human and less mathematical.

## Components

### Buttons
Primary buttons are solid `Moss Green` with `Soft White` text. Secondary buttons use a `Lavender` glass effect with a subtle 1px border. All buttons should have a subtle "pulse" animation when in a focused/monitoring state.

### Vitals Cards
These are the core of the design system. They feature a primary metric (Atkinson Hyperlegible), a small sparkline showing the last 30 seconds of data, and a "breathing" status icon—a soft-glowing circle that expands and contracts.

### Breathing Guide
A full-width component with a large, fluid gradient blob that expands and contracts to guide the driver through calming breathwork. The motion is non-linear (Ease-in-out) to mimic natural lung expansion.

### Chips & Tags
Used for health statuses (e.g., "Optimal," "Resting"). These are pill-shaped with low-contrast background fills and high-contrast text.

### Input Fields
Fields are translucent with a soft bottom-border indicator. On focus, the border transitions from `Moss Green` to a `Lavender` glow, signifying the system is "listening" or "ready."

### Health Summaries
Lists of historical health data use "alternating leaf" layouts where icons are placed on the left or right to create a more natural, staggered flow rather than a rigid vertical line.