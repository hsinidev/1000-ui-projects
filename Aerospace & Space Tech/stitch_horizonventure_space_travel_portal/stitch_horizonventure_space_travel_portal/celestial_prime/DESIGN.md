---
name: Celestial Prime
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353435'
  on-surface: '#e5e2e2'
  on-surface-variant: '#c7c5cc'
  inverse-surface: '#e5e2e2'
  inverse-on-surface: '#313031'
  outline: '#919096'
  outline-variant: '#46464c'
  surface-tint: '#c5c5d4'
  primary: '#c5c5d4'
  on-primary: '#2e303b'
  primary-container: '#0b0d17'
  on-primary-container: '#797a87'
  inverse-primary: '#5c5e6a'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#0b0e0f'
  on-tertiary-container: '#797b7c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e1f0'
  primary-fixed-dim: '#c5c5d4'
  on-primary-fixed: '#191b26'
  on-primary-fixed-variant: '#444652'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#131314'
  on-background: '#e5e2e2'
  surface-variant: '#353435'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.1em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.2em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 32px
  margin: 80px
  container-max: 1440px
  stack-xl: 120px
---

## Brand & Style

The design system embodies the intersection of elite aerospace engineering and high-end hospitality. It targets ultra-high-net-worth individuals seeking an aspirational and cinematic journey into the cosmos. The UI must evoke a sense of calm authority, immense scale, and meticulous exclusivity.

The visual style is a fusion of **Minimalism** and **Glassmorphism**. It utilizes expansive "Lean-Back" editorial layouts that prioritize high-quality imagery over dense information. The aesthetic is clean and futuristic, avoiding cluttered "tech" tropes in favor of an opulent, streamlined experience reminiscent of a private orbital lounge.

## Colors

The palette is anchored by **Deep Space Blue**, serving as a boundless, immersive background. **Pearl White** provides high-contrast clarity for typography and essential UI cues, while **Metallic Gold** is reserved for moments of high-end prestige, such as calls to action, premium tier indicators, and subtle glowing accents.

The interface operates exclusively in a dark-mode environment to simulate the sensation of looking out of a spacecraft viewport into the void. Use gold sparingly as a "light-source" element to guide the user's eye through the narrative.

## Typography

This design system utilizes **Space Grotesk** for headings to provide a technical, geometric edge that feels inherently futuristic. For body copy, **Manrope** is selected for its refined, balanced, and highly legible characteristics, ensuring comfort during longer editorial reads.

All headlines should utilize generous letter spacing to evoke a sense of vastness. "Label-caps" should be used for navigational elements and small data points to maintain a clean, organized hierarchy.

## Layout & Spacing

The layout follows a **Fixed Grid** model centered on a 12-column system. To achieve the "Lean-Back" editorial feel, the design system employs aggressive vertical margins (stack-xl) and wide outer margins. Content should never feel crowded; the whitespace is as much a luxury feature as the imagery itself.

Components and sections should rely on a consistent 8px rhythm, with larger increments used to separate distinct narrative beats. Use asymmetrical placement for hero elements to create a more cinematic, less "templated" appearance.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and selective illumination rather than traditional shadows. 

1.  **Base Layer:** The Deep Space Blue background.
2.  **Mid Layer:** Semi-transparent glass panels (back-drop blur 12px-20px) with 1px Pearl White borders at 10% opacity.
3.  **Top Layer:** Interactive elements featuring a subtle gold outer glow (5-15px spread, low opacity) to simulate light reflecting off metallic surfaces.

Avoid solid fills for containers; instead, use gradients of transparency to suggest volume and the presence of glass.

## Shapes

The shape language is "Soft" (0.25rem - 0.75rem), balancing the precision of aerospace engineering with the comfort of luxury furniture. Hard 90-degree angles are used only for the primary grid lines, while UI containers and buttons use subtle radii to feel approachable and high-end. 

Interactive elements like "Explore" buttons may utilize a mix of soft corners and extended horizontal widths to emphasize the cinematic horizon.

## Components

**Buttons:** Primary buttons are ghost-style with a Pearl White 1px border, transitioning to a solid Metallic Gold fill on hover. Text is always Uppercase Space Grotesk.

**Cards:** Use extreme backdrop blurs. Cards should not have shadows but rather a thin, glowing top-edge highlight to suggest a light source from above.

**Input Fields:** Minimalist lines rather than boxes. The active state is indicated by a Metallic Gold underline and a very subtle vertical glow.

**Chips:** Small, pill-shaped outlines used for flight status or cabin class. Use Pearl White for standard and Metallic Gold for "First Class" or "Priority" indicators.

**Progress Indicators:** Thin, sleek lines (2px height). For spaceflight trajectories, use a glowing Metallic Gold path against a faint Pearl White dashed line.

**Additional Components:** 
*   **The Viewport:** A full-screen media container for high-resolution planetary photography.
*   **Concierge HUD:** A floating glass panel for personal itinerary details.