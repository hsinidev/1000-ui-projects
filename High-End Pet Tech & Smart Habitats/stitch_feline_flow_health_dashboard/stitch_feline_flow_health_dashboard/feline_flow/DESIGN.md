---
name: Feline-Flow
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
  on-surface-variant: '#46464c'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#77767d'
  outline-variant: '#c7c5cc'
  surface-tint: '#5c5d6e'
  primary: '#5c5d6e'
  on-primary: '#ffffff'
  primary-container: '#e6e6fa'
  on-primary-container: '#656677'
  inverse-primary: '#c5c5d8'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e8e8'
  on-tertiary-container: '#666868'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e1f5'
  primary-fixed-dim: '#c5c5d8'
  on-primary-fixed: '#191b29'
  on-primary-fixed-variant: '#444655'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.015em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  section-gap: 64px
---

## Brand & Style

This design system embodies a "Clinical-Serenity" aesthetic, merging high-tech medical precision with the gentle nature of pet care. The brand personality is professional, sterile (in a clean, reassuring sense), and advanced. It targets discerning pet owners who prioritize health data and environmental control.

The style is a refined **Neomorphism-lite**, focusing on "Soft-UI" principles. Unlike heavy traditional Neumorphism, this approach uses extremely subtle tonal shifts and generous whitespace to ensure the interface feels airy and lightweight rather than "muddy." The visual language communicates a state of flow—uninterrupted, calm, and technologically superior.

## Colors

The palette is restricted to high-key, low-saturation tones to maintain a medical-grade look. 

- **Silk White (#F8F9FA):** The primary canvas color. It is used for large surfaces to maximize perceived whitespace and cleanliness.
- **Soft Lavender (#E6E6FA):** The signature brand accent. Used for interactive states, data visualizations, and primary actions. It provides a calming, non-aggressive alternative to traditional medical blues.
- **Metallic Silver (#C0C0C0):** Utilized for subtle borders, iconography, and secondary text, grounding the ethereal whites with a sense of hardware durability.
- **Pure White (#FFFFFF):** Reserved for "specular highlights" in the Neumorphic shadows to create the illusion of extruded surfaces.

## Typography

The design system utilizes **Inter** for its utilitarian clarity and modern geometric structure. To achieve the "high-tech" look, typography relies on generous tracking (letter-spacing) and light font weights for larger displays.

Text hierarchy is strictly enforced through scale rather than color contrast. Headings use a lighter weight to appear sophisticated, while labels use all-caps with significant tracking to mimic professional medical equipment labeling. Body text maintains a high line-height to ensure readability and support the overall theme of "maximum whitespace."

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid Grid** that emphasizes wide margins. Content is often centered in the viewport with significant "buffer zones" to prevent visual clutter.

A modular 8px scale is used for internal component spacing, but the design system mandates a "double-margin" philosophy for layout containers—where a standard margin might be 20px, this system uses 40px or 64px. This intentional "waste" of space is what creates the premium, serene atmosphere required for a medical-grade habitat interface.

## Elevation & Depth

Depth is achieved through **Neumorphic Extrusion**. Instead of traditional drop shadows that float an object, elements appear to be molded out of the background surface (Silk White).

- **Outer Extrusion:** Elements use two shadows. A light shadow (top-left) in `#FFFFFF` with a 12px-24px blur, and a dark shadow (bottom-right) in `#E0E3E8` (a slightly cooler version of the base) with the same blur.
- **Inner Recess:** For input fields or inactive states, an inner shadow is used to make the element appear sunken into the surface.
- **Tonal Layers:** Surfaces rarely use borders; elevation is defined purely by the interplay of light and shadow on the `#F8F9FA` base.

## Shapes

The shape language is hyper-rounded to evoke safety and organic flow. The base radius for all standard components (cards, buttons) starts at **24px**. Larger containers or full-screen modules should use **32px** or higher.

The use of "Pill" shapes for buttons and toggles is mandatory to maintain the soft-UI aesthetic. Sharp corners are entirely absent from the design system, ensuring every touchpoint feels approachable and "pet-friendly."

## Components

- **Buttons:** Pill-shaped with a soft Neumorphic lift. The primary state uses the Soft Lavender (#E6E6FA) as a subtle background tint, while the text remains Metallic Silver for professional contrast.
- **Cards:** Large, expansive containers with a 32px corner radius. Cards should not have visible borders; their boundaries are defined by the dual-shadow extrusion.
- **Status Indicators:** Small, glowing "pulsing" circles in Lavender to indicate active air flow or habitat vitals, mimicking medical monitor behavior.
- **Input Fields:** Recessed (sunken) shapes with a Silver inner shadow. The typography inside is centered and uses generous tracking.
- **Toggles/Sliders:** Tactile-style sliders where the "thumb" is a highly extruded Silk White circle, providing a physical, high-tech sensation upon interaction.
- **Health Charts:** Simplified line graphs using a Silver grid and a Lavender data line, emphasizing clean data over complex visualizations.