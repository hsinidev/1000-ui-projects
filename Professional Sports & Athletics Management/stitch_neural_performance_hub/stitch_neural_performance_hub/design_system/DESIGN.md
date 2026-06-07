---
colors:
  surface: '#0b1032'
  surface-dim: '#0b1032'
  surface-bright: '#32375a'
  surface-container-lowest: '#060a2d'
  surface-container-low: '#13183a'
  surface-container: '#181d3f'
  surface-container-high: '#22274a'
  surface-container-highest: '#2d3255'
  on-surface: '#dfe0ff'
  on-surface-variant: '#c7c5ce'
  inverse-surface: '#dfe0ff'
  inverse-on-surface: '#292e51'
  outline: '#919098'
  outline-variant: '#46464d'
  surface-tint: '#c1c4e8'
  primary: '#c1c4e8'
  on-primary: '#2b2e4b'
  primary-container: '#0a0e29'
  on-primary-container: '#777a9b'
  inverse-primary: '#595c7b'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#0f1111'
  on-tertiary-container: '#7b7d7d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe0ff'
  primary-fixed-dim: '#c1c4e8'
  on-primary-fixed: '#151935'
  on-primary-fixed-variant: '#414562'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0b1032'
  on-background: '#dfe0ff'
  surface-variant: '#2d3255'
typography:
  h1-display:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2-headline:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  h3-subhead:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  margin-mobile: 20px
  gutter-mobile: 12px
---

## Brand & Style

This design system is built for the "Neuro-Athlete"—individuals seeking to merge biological potential with technological precision. The brand personality is clinical yet high-octane, evoking the feeling of a high-performance cockpit for the mind. 

The aesthetic follows a **Cyber-Biological** direction. It utilizes the depth of "Deep Indigo" to represent the vast, untapped subconscious, punctuated by "Metallic Gold" synaptic pathways that signify peak cognitive firing. Visuals should feel energetic and high-speed, utilizing motion blurs and sharp directional lines to imply rapid information processing. The UI relies on glassmorphism to create layers of data that feel like they are floating within a neural field, maintaining focus through high-contrast typography and intentional "neural-path" glows.

## Colors

The palette is strictly high-contrast to facilitate cognitive focus and minimize visual fatigue during intense training. 

*   **Deep Indigo (#0A0E29):** The primary void. Used for the background and core UI structure.
*   **Metallic Gold (#D4AF37):** The "Neural Pulse." Used sparingly for achievements, active synaptic paths, and critical CTA states.
*   **Crisp White (#FFFFFF):** The data layer. Used for all primary text and high-visibility UI markers.
*   **Surface Indigo (#161B3D):** A slightly elevated secondary base for card backgrounds and container layering.

Use "Neural Glows" (Gold with 40% opacity and 20px blur) to highlight active progress or focused interactive elements.

## Typography

This design system employs a dual-font strategy to balance technical edge with readable data. 

**Space Grotesk** is used for all headlines and labels. Its geometric, slightly eccentric terminals give the UI a "cutting-edge" and "scientific" feel. Large display headers should use tight letter spacing to feel aggressive and fast.

**Inter** is utilized for body copy and dense data readouts. It provides the necessary "utilitarian" clarity to ensure users can absorb training instructions and performance metrics instantly without cognitive load. 

All labels must be rendered in Space Grotesk with increased letter spacing and uppercase styling to mimic telemetry readouts found in high-performance equipment.

## Layout & Spacing

The design system uses a **Fluid Grid** optimized for mobile devices. The base unit is 4px, driving an 8pt rhythm for all spatial relationships. 

The mobile layout is built on a 4-column grid with 20px outer margins. Elements should feel "locked-in" and structural. Use ample vertical white space (using the `lg` and `xl` tokens) between training modules to allow the user to focus on one cognitive task at a time. Containers and interactive cards should use the `sm` (16px) or `md` (24px) padding to maintain a sense of density and data-richness without feeling cluttered.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and **Tonal Layering**, rather than traditional drop shadows.

1.  **Base Layer:** Deep Indigo (#0A0E29).
2.  **Surface Layer:** Surface Indigo (#161B3D) with a subtle 1px border of 10% White to define edges.
3.  **Interactive Layer (Glass):** Semi-transparent white (5-8% opacity) with a 20px backdrop blur. This creates a frosted-lens effect that suggests a digital overlay on top of biological data.
4.  **Neural Elevation:** Elements that require immediate attention (like an active timer or peak state) should feature a Gold (#D4AF37) outer glow with a high spread and low opacity, simulating light emitting from a neural connection.

## Shapes

The shape language of this design system is **Sharp**. 

To reinforce the "precision" and "cutting-edge" aspect of neuro-athletic training, all primary containers, buttons, and input fields use 0px border radii. Octagonal "clipped-corner" motifs can be used for secondary buttons or decorative elements to further the "cyber" aesthetic. 

Small UI elements like progress bars should be perfectly rectangular, using hard edges to emphasize accuracy and the definitive nature of performance data.

## Components

**Buttons:** 
Primary buttons are solid Metallic Gold with black text, utilizing sharp corners and a subtle "pulse" glow on hover/active states. Secondary buttons are "Ghost" style—white 1px borders with sharp corners and no fill.

**Cards:** 
Constructed using the glassmorphism style. Cards feature a 1px border on the top and left sides only, creating a "specular highlight" effect that makes the UI feel like machined glass.

**Neural-Paths (Progress Indicators):** 
Linear progress bars should be ultra-thin (2px). The track is Deep Indigo (blending into the background), and the progress fill is Metallic Gold with a leading glow effect that leaves a faint trail, suggesting movement and speed.

**Inputs:** 
Input fields are underlined with a 1px White line. When focused, the line transitions to Gold and emits a subtle glow, signaling an "active synapse."

**Performance Chips:** 
Small, sharp-edged rectangles used for tagging metrics (e.g., "REACTION TIME"). Background is Surface Indigo, text is White in all-caps Space Grotesk.