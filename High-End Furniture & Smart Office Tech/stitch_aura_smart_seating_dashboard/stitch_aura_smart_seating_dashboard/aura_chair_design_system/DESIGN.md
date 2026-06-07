---
name: Aura-Chair Design System
colors:
  surface: '#f9f9fb'
  surface-dim: '#d9dadc'
  surface-bright: '#f9f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f5'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e4'
  on-surface: '#1a1c1d'
  on-surface-variant: '#3e4944'
  inverse-surface: '#2f3132'
  inverse-on-surface: '#f0f0f2'
  outline: '#6e7a73'
  outline-variant: '#bdc9c2'
  surface-tint: '#006c51'
  primary: '#006c51'
  on-primary: '#ffffff'
  primary-container: '#98ffd8'
  on-primary-container: '#00785b'
  inverse-primary: '#73d9b4'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5d5e60'
  on-tertiary: '#ffffff'
  tertiary-container: '#ebebed'
  on-tertiary-container: '#686a6c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#8ff6cf'
  primary-fixed-dim: '#73d9b4'
  on-primary-fixed: '#002116'
  on-primary-fixed-variant: '#00513c'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e4'
  tertiary-fixed-dim: '#c6c6c8'
  on-tertiary-fixed: '#1a1c1d'
  on-tertiary-fixed-variant: '#454749'
  background: '#f9f9fb'
  on-background: '#1a1c1d'
  surface-variant: '#e2e2e4'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-padding: 24px
  stack-gap: 12px
---

## Brand & Style
This design system embodies a "Soft-Biomechanical" philosophy, merging the precision of high-end aerospace engineering with the fluid, restorative nature of human anatomy. The brand is positioned as a luxury wellness technology leader, evoking a sense of calm, intelligence, and physical weightlessness.

The visual language utilizes Neumorphism (Soft-UI) to simulate tactile, molded surfaces that feel like the physical controls of an ergonomic masterpiece. The interface should feel extruded from the background rather than floating above it, creating a unified, physical presence that is futuristic yet approachable.

## Colors
The palette is rooted in **Silk White (#F5F5F7)**, which serves as the primary canvas for neomorphic effects. **Slate Grey (#2F2F2F)** provides high-contrast grounding for text and critical structural elements, while **Mint (#98FFD8)** is reserved for active states, AI-driven insights, and "breathable" UI moments.

To achieve the soft-UI effect, the background must remain consistent. Shadows are derived from the Silk White base: a darker shade (#D1D1D6) for the bottom-right depth and pure white (#FFFFFF) for the top-left highlight.

## Typography
**Manrope** is the sole typeface, chosen for its geometric purity and modern, technical legibility. The typographic hierarchy relies on subtle weight shifts and generous leading to maintain an airy, premium feel. Headlines use tighter tracking and heavier weights to suggest strength and stability, while body text remains open and accessible for long-form ergonomic data and insights.

## Layout & Spacing
The layout follows a fluid model with wide margins to emphasize the "Soft-UI" depth. A 4px baseline grid ensures vertical rhythm, while component spacing uses an 8px modular scale. 

The mobile experience is anchored by a bottom navigation bar, allowing for easy thumb access. Large, tactile containers should be separated by at least 16px to prevent shadow overlap and maintain visual clarity. "Safe areas" are exaggerated to simulate the comfort and spaciousness of high-end seating.

## Elevation & Depth
Elevation is not achieved through traditional stacking, but through surface deformation. All elements are part of the same Silk White plane.

1.  **Convex (Raised):** Elements use a top-left light shadow (#FFFFFF) and a bottom-right dark shadow (#D1D1D6) to appear pushed out. Used for buttons and interactive cards.
2.  **Concave (Sunken):** Inset shadows create a "carved" look. Used for input fields, progress tracks, and active button states.
3.  **Glass Layers:** For overlays and navigation bars, a high-refraction background blur (20px-30px) is used with a semi-transparent Silk White tint (80% opacity) to create a premium, futuristic sense of translucency.

## Shapes
The shape language is strictly organic and "bio-mechanical." Avoid sharp corners entirely. This design system uses high-radius pill shapes and "squircular" containers to mimic the curves of the human body and ergonomic cushioning. Containers should feel molded, with transitions between sections appearing seamless rather than distinct blocks.

## Components
- **Neumorphic Toggles:** Base is a concave "track." The handle is a convex pill that glows softly with a Mint (#98FFD8) drop shadow when active.
- **Tactile Sliders:** The slider thumb is a large, rounded-rect with a subtle tactile ridge texture. The track appears as an engraved groove in the surface.
- **Glass Bottom Bar:** A floating, blurred glass container with a subtle 1px Silk White border. Icons use Mint for active states.
- **Information Cards:** Large-radius containers with a convex elevation. Content inside is grouped with subtle inset horizontal rules.
- **Input Fields:** Deeply recessed (concave) shapes with Manrope Medium text. Focus is indicated by a soft Mint glow emanating from the inner shadow.
- **Biometric Visualizers:** Smooth, animated wave-forms using Mint gradients to represent real-time ergonomic adjustments or posture data.