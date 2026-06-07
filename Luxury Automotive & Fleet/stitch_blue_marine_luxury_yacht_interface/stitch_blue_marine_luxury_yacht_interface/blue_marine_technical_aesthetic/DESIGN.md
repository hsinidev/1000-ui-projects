---
name: Blue-Marine Technical Aesthetic
colors:
  surface: '#021525'
  surface-dim: '#021525'
  surface-bright: '#293b4d'
  surface-container-lowest: '#000f1e'
  surface-container-low: '#091d2e'
  surface-container: '#0e2132'
  surface-container-high: '#192b3d'
  surface-container-highest: '#243648'
  on-surface: '#d1e4fb'
  on-surface-variant: '#bfc8c8'
  inverse-surface: '#d1e4fb'
  inverse-on-surface: '#203243'
  outline: '#899392'
  outline-variant: '#3f4848'
  surface-tint: '#94d1d1'
  primary: '#94d1d1'
  on-primary: '#003737'
  primary-container: '#004d4d'
  on-primary-container: '#80bdbc'
  inverse-primary: '#296767'
  secondary: '#a7c8ff'
  on-secondary: '#003061'
  secondary-container: '#1f477b'
  on-secondary-container: '#93b6f1'
  tertiary: '#ffb595'
  on-tertiary: '#571e00'
  tertiary-container: '#782d00'
  on-tertiary-container: '#ff9767'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b0eeed'
  primary-fixed-dim: '#94d1d1'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#044f4f'
  secondary-fixed: '#d5e3ff'
  secondary-fixed-dim: '#a7c8ff'
  on-secondary-fixed: '#001b3c'
  on-secondary-fixed-variant: '#1f477b'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb595'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7c2e00'
  background: '#021525'
  on-background: '#d1e4fb'
  surface-variant: '#243648'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
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
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  waterline-thick: 2px
  waterline-thin: 1px
  section-padding: 120px
---

## Brand & Style

This design system embodies the intersection of elite naval engineering and high-luxury lifestyle. The personality is disciplined, authoritative, and sophisticated. It targets ultra-high-net-worth individuals and maritime professionals who value technical precision as much as aesthetic beauty.

The visual style is a fusion of **Industrial Minimalism** and **High-Contrast Boldness**. It utilizes sharp geometric forms and a dark-leaning atmosphere to evoke the depths of the ocean and the resilience of marine-grade materials. Every interface element should feel like a piece of custom-machined hardware—intentional, durable, and refined. High-resolution drone imagery and metallic textures are used to ground the digital experience in the physical reality of superyacht manufacturing.

## Colors

The palette is anchored in deep, oceanic tones to establish a premium nautical foundation. The use of **Deep Teal** and **Ocean Blue** provides a sophisticated alternative to standard blacks, creating depth that mimics the sea. 

**Safety Orange** is reserved strictly for technical callouts, critical data points, and primary actions, ensuring high visibility against the dark gunmetal surfaces. **Metallic Silver** is applied through subtle gradients and hair-line borders to simulate brushed aluminum and stainless steel components. The default state for this design system is dark mode, which enhances the luminosity of high-resolution photography and technical diagrams.

## Typography

This design system utilizes **Space Grotesk** for all headings and technical labels to lean into a modern, industrial grotesque aesthetic. Its geometric construction mirrors the precision of yacht blueprints. For body copy, **Inter** provides maximum legibility across technical specifications and narrative content.

A strict hierarchy is maintained through the use of uppercase labels with increased letter spacing, mimicking the markings found on maritime equipment and hull identifiers. Display type should be set with tight tracking to emphasize the "wide" and "bold" industrial feel of the brand.

## Layout & Spacing

The layout follows a **Fixed-Max Fluid Grid** model, built on a 12-column system. Content is structured to feel expansive and "at sea," utilizing significant vertical whitespace between sections. 

The "Waterline" concept is the primary structural device. These are horizontal dividers that span the width of the container or viewport, used to separate content blocks or align data. Large-scale drone photography should break the grid occasionally or bleed edge-to-edge to create a cinematic experience. Interactive scroll effects should prioritize a "heavy" feel, where elements move with a slight inertial lag, suggesting the displacement of a large vessel.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Material Contrast** rather than traditional shadows. 

1. **Surface Tiers:** Backgrounds are the darkest tone, with UI "plates" or "modules" sitting one shade lighter.
2. **Glassmorphism:** Navigation bars and technical overlays use a frosted glass effect (backdrop-blur: 20px) with a semi-transparent Deep Teal tint, simulating the look of high-end bridge instruments.
3. **Ghost Outlines:** Elements are defined by 1px "Metallic Silver" borders with low opacity (10-20%) to create a technical, wireframe-inspired aesthetic.
4. **Waterline Shadows:** When depth is required, use a single-direction downward shadow tinted with Ocean Blue to ground elements without creating "mushy" blurs.

## Shapes

In keeping with the industrial-nautical theme, the shape language is **Sharp (0px radius)**. 

Every button, card, and input field must feature hard 90-degree corners to reflect the precision-cut nature of marine fabrication. This angularity creates a sense of strength and high-tech sophistication. Softening is only permitted in iconography or circular technical gauges, where the geometry serves a functional, read-out purpose.

## Components

### Buttons
Primary buttons are sharp-edged boxes with a Safety Orange fill and black/dark-teal text for maximum visibility. Secondary buttons use a Silver metallic border with a hover state that triggers a subtle "sheen" gradient animation.

### Technical Callouts (Chips)
Used for vessel specifications (e.g., "Length: 12m"). These use a Slate background with the "Technical-Data" typography style and a 1px left-hand accent border in Safety Orange.

### Waterline Dividers
Horizontal rules that often include a technical label or coordinate (e.g., "00.1-Vessel Specs") positioned at the intersection of the line and the grid margin.

### Cards
Cards are defined by their borders rather than their backgrounds. Use "Gunmetal" backgrounds only when necessary to separate from the main canvas. Content inside cards should be aligned to a sub-grid to maintain the technical look.

### Interactive Iconography
Icons should be thin-line (1px or 1.5px stroke), geometric, and strictly non-rounded. They should look like stylized architectural or engineering symbols.

### Input Fields
Inputs are minimal, featuring only a bottom border (Waterline) that becomes thicker and changes to Silver or Safety Orange on focus. Labels sit above the line in the "label-caps" style.