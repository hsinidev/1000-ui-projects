---
name: Dopamine Metaverse
colors:
  surface: '#131318'
  surface-dim: '#131318'
  surface-bright: '#39383e'
  surface-container-lowest: '#0e0e13'
  surface-container-low: '#1b1b20'
  surface-container: '#1f1f25'
  surface-container-high: '#2a292f'
  surface-container-highest: '#35343a'
  on-surface: '#e4e1e9'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e4e1e9'
  inverse-on-surface: '#303036'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#fface8'
  on-secondary: '#5e0053'
  secondary-container: '#ff24e4'
  on-secondary-container: '#520049'
  tertiary: '#fdf2ff'
  on-tertiary: '#4b007e'
  tertiary-container: '#ebcfff'
  on-tertiary-container: '#8d00e5'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#ffd7f0'
  secondary-fixed-dim: '#fface8'
  on-secondary-fixed: '#3a0033'
  on-secondary-fixed-variant: '#840076'
  tertiary-fixed: '#f1daff'
  tertiary-fixed-dim: '#dfb7ff'
  on-tertiary-fixed: '#2d004f'
  on-tertiary-fixed-variant: '#6b00b0'
  background: '#131318'
  on-background: '#e4e1e9'
  surface-variant: '#35343a'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 80px
    fontWeight: '700'
    lineHeight: 88px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-margin: 64px
  gutter: 24px
  section-gap: 120px
  element-gap: 16px
---

## Brand & Style
This design system centers on a high-energy, "dopamine-hit" aesthetic tailored for the high-stakes world of digital real estate. The brand personality is audacious, immersive, and unapologetically futuristic. It targets tech-savvy investors and digital collectors who view the metaverse not just as a tool, but as a lifestyle. 

The visual style is a hybrid of **Glassmorphism** and **High-Contrast Bold** movements. It utilizes translucent layers to suggest infinite depth while anchoring the user with vibrant, neon-lit focal points. The emotional response is one of excitement and premium exclusivity, achieved through the tension between dark, expansive voids and hyper-saturated interface elements.

## Colors
The palette is built on a "Dark Mode" foundation to allow high-saturation "Dopamine" accents to resonate. The primary Electric Blue serves as the main interactive signal, while Neon Pink and Vibrant Purple are used for secondary actions and tier-based property categories. 

Neutrals are kept extremely dark, moving away from flat grays toward deep space blacks to enhance the glow of neon borders. Gradients should be used sparingly but with high impact, specifically utilizing "linear-burn" or "screen" blending modes to simulate light emissions.

## Typography
This design system employs **Space Grotesk** across all levels to maintain a technical, cutting-edge atmosphere. Its geometric construction mirrors the architectural nature of digital property. 

Headlines use tight letter-spacing and heavy weights to command attention, while body text remains legible with generous line heights. A specialized "Label-Caps" style is used for technical metadata, property coordinates, and secondary UI cues to evoke a "heads-up display" (HUD) feel.

## Layout & Spacing
The layout follows a **Fluid Grid** model with an emphasis on "Airy" composition. By utilizing large section gaps (120px+), the design system allows 3D elements to "breathe" and reduces visual clutter in a high-saturation environment.

Information is grouped into floating modules that do not necessarily touch the edges of the viewport, creating a sense of a UI suspended in space. Grid gutters are wide to prevent the neon glows of adjacent elements from bleeding into one another, preserving the distinctiveness of each property listing.

## Elevation & Depth
Depth is the primary communicator of hierarchy. This design system discards traditional flat shadows in favor of:

1.  **Glassmorphism:** All containers use a backdrop blur (minimum 20px) and a semi-transparent fill. This simulates physical layers of glass floating in a 3D environment.
2.  **Neon Glows:** Active or high-value elements use outer glows (drop shadows with 0 offset, high spread, and 50-70% opacity of the accent color) to appear "self-illuminated."
3.  **Z-Axis Layering:** Elements further back in the visual stack are desaturated and have higher blur values, while foreground elements are crisp and hyper-saturated.
4.  **Floating Borders:** Use 1px internal strokes with linear gradients (e.g., primary color to transparent) to define edges without closing the shapes off entirely.

## Shapes
The shape language is **Rounded**, striking a balance between organic softness and mathematical precision. 

Large container surfaces (cards, modals) use a 1rem (16px) radius to feel approachable. Interactive elements like buttons and chips utilize pill-shaped (full radius) geometry to distinguish them from informational containers. Borders are never solid; they should always be treated as "light paths" using subtle gradients that highlight the top-left corner as if hit by a distant light source.

## Components
- **Buttons:** Primary buttons are pill-shaped with a full neon gradient fill and a matching colored drop shadow (glow). Secondary buttons use a "ghost" style with a neon border and backdrop blur.
- **Property Cards:** These are the centerpiece. They must feature a high-blur glass background, a 1px gradient border, and a 3D-transformed image of the digital asset that slightly overflows the card boundary to induce depth.
- **Input Fields:** Minimalist glass fields. On focus, the bottom border "ignites" with a primary color glow, and the label floats upward using the "Label-Caps" typography.
- **Chips/Badges:** Small, high-saturation pills used for "New," "Hot," or "Sold" status. These use the tertiary purple to contrast against primary blue actions.
- **HUD Navigation:** A floating bottom bar or side rail that uses extreme glassmorphism (80% blur) and icons that glow when active.
- **Data Visualizers:** For property value history, use glowing line charts with area gradients that "pulse" slowly to indicate real-time data flow.