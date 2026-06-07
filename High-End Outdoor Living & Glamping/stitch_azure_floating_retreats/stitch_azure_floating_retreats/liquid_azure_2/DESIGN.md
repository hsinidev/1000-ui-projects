---
name: Liquid Azure
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#414754'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005cbc'
  primary: '#005ab7'
  on-primary: '#ffffff'
  primary-container: '#0072e5'
  on-primary-container: '#fefcff'
  inverse-primary: '#abc7ff'
  secondary: '#5b5f63'
  on-secondary: '#ffffff'
  secondary-container: '#dde0e5'
  on-secondary-container: '#606367'
  tertiary: '#4d5e69'
  on-tertiary: '#ffffff'
  tertiary-container: '#667782'
  on-tertiary-container: '#fbfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#004590'
  secondary-fixed: '#e0e2e7'
  secondary-fixed-dim: '#c4c6cb'
  on-secondary-fixed: '#181c20'
  on-secondary-fixed-variant: '#44474b'
  tertiary-fixed: '#d3e5f2'
  tertiary-fixed-dim: '#b7c9d5'
  on-tertiary-fixed: '#0c1d27'
  on-tertiary-fixed-variant: '#384953'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
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
  container-max: 1440px
  gutter: 32px
  margin-desktop: 80px
  section-gap: 120px
---

## Brand & Style

This design system embodies the serene intersection of water and light. Designed for a high-end glamping experience centered around aquatic environments, it prioritizes a minimalist luxury aesthetic that feels both expansive and intimate. The visual language mimics the properties of water: clarity, fluidity, and gentle refraction.

The personality is sophisticated and tranquil, aimed at an audience that values exclusivity and architectural beauty. By leveraging heavy whitespace and a light-filled interface, the system evokes a sense of "breathable" luxury, ensuring that high-resolution imagery of pristine landscapes remains the focal point while the interface acts as a refined, translucent lens.

## Colors

The palette is anchored by **Azure Blue (#007FFF)**, representing deep water and clear skies. This is used sparingly for high-impact accents, calls to action, and interactive states to maintain a sense of preciousness. 

**Pristine White** serves as the primary canvas, providing the "airy" feel essential to the brand. To create depth without adding visual weight, the system utilizes a spectrum of translucent blues and frosted whites. Gradients should be subtle, mimicking the way light filters through shallow water. 

Dark neutrals are reserved strictly for high-legibility typography and fine structural lines, ensuring the overall interface remains bright and ethereal.

## Typography

The typography uses **Montserrat** exclusively to achieve a modern, geometric, and clean look. Large display headings use a "Light" (300) weight with tight letter-spacing to create a sophisticated, editorial feel. 

Body text is set with generous line heights to enhance readability and contribute to the "airy" layout philosophy. Labels and utility text are occasionally transformed to uppercase with increased tracking (letter-spacing) to serve as elegant anchors for smaller UI elements. The hierarchy is strictly enforced through scale rather than weight, keeping the interface feeling light.

## Layout & Spacing

This design system utilizes a **fixed-width, centered grid** for desktop optimization, ensuring a consistent luxury experience across wide monitors. The 12-column grid is bounded by an 80px outer margin and 32px gutters, creating significant negative space.

Spacing follows an 8px incremental scale, but emphasizes "the breath." Sections are separated by large gaps (120px+) to prevent the user from feeling rushed. Elements within a group should feel connected through proximity, but the overall composition must prioritize a lack of clutter, mirroring the openness of a coastal horizon.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and soft, environmental shadows. Rather than using solid z-axis layers, surfaces use a 60%–80% opacity white fill with a high-saturation **backdrop-blur (20px - 40px)**. 

Shadows are "ambient"—extremely diffused, low-opacity, and slightly tinted with Azure Blue (#007FFF) to suggest a translucent object resting on a reflective surface. Borders are replaced by 1px semi-transparent "inner glows" to define edges without adding visual noise. The effect should be that of polished glass or frozen water floating over the content.

## Shapes

The shape language is "Softly Geometric." A consistent **0.5rem (8px)** corner radius is applied to standard elements like input fields and small cards, while larger glass containers may use **1rem (16px)** to emphasize their volume. 

The goal is to avoid the harshness of sharp 90-degree angles while steering clear of the overly casual look of pill-shapes. The rounded corners should feel like stones smoothed by water—intentional, soft, and premium.

## Components

### Buttons
Primary buttons use a solid Azure Blue fill with white text, featuring a subtle "liquid" hover transition where the background shifts slightly in saturation. Secondary buttons are "Ghost" style—clear backgrounds with a 1px Azure Blue or Pristine White border and semi-transparent fills on hover.

### Glass Cards
The signature component of this design system. These feature a 20px backdrop-blur, a 1px white stroke at 20% opacity, and a soft ambient shadow. They are used for hero content and modular booking forms.

### Input Fields
Inputs are minimalist: a single bottom border or a very subtle translucent container. Focus states are indicated by a gentle glow of Azure Blue and a slight increase in the backdrop-blur intensity.

### Interactive Elements
- **Chips:** Highly translucent with Montserrat Label-sm typography.
- **Lists:** Separated by thin, 10% opacity lines; hovering over an item triggers a soft Azure Blue tint.
- **Progress Indicators:** Use a fluid animation style, mimicking a filling reservoir rather than a static bar.

### Additional Components
- **The "Horizon" Carousel:** A full-width image slider with glassmorphic navigation overlays.
- **Floating Action Dock:** A blurred glass bar at the bottom of the viewport for primary navigation or booking summaries.