---
name: Industrial-Luxe Audio
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c7c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#e6c8b7'
  on-tertiary: '#3f2c20'
  tertiary-container: '#c9ad9c'
  on-tertiary-container: '#554133'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#fbddca'
  tertiary-fixed-dim: '#dec1af'
  on-tertiary-fixed: '#28180d'
  on-tertiary-fixed-variant: '#574335'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
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
  spec-label:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  spec-value:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1440px
---

## Brand & Style

This design system embodies the meticulous engineering and sensory richness of high-end analog audio. The brand personality is "The Modern Connoisseur"—reverent of heritage materials like timber and brass, yet defined by precision manufacturing. 

The aesthetic is **Industrial-Luxe**, characterized by a dark, atmospheric palette that allows metallic and wood textures to emerge from the shadows. The UI utilizes **Neumorphism (Soft-UI)** specifically to create a tactile, skeuomorphic bridge between digital controls and physical hi-fi hardware. The goal is to evoke the physical sensation of turning a weighted brass knob or toggling a precision steel switch. Every interaction should feel heavy, dampened, and intentional.

## Colors

The palette is anchored in a moody, near-black environment to emphasize depth and luxury.

- **Primary (Polished Brass):** Used sparingly for interactive highlights, active states, and focal points. It represents the "crown jewels" of the hardware.
- **Secondary (Brushed Steel):** Used for structural elements, secondary iconography, and labels. It provides a cold, technical contrast to the warmth of the other colors.
- **Tertiary (Deep Walnut):** Provides organic warmth. This color is used for container backgrounds and large surfaces to soften the industrial edge.
- **Background & Neutrals:** The base is a deep matte charcoal (#121212) to ensure that neomorphic shadows (both light and dark) have enough range to appear three-dimensional.

## Typography

The typographic strategy contrasts the emotional and the technical.

- **Headlines:** Use **Playfair Display**. This serif adds a layer of editorial elegance and timelessness. It should be typeset with tight tracking in display sizes to feel like a high-end magazine.
- **Body:** **Inter** provides high legibility for descriptions, ensuring the UI remains functional and modern.
- **Technical Specs:** **JetBrains Mono** is utilized for all "hard" data (RPM, weight, frequency response). The monospaced nature mimics the stamped serial numbers and engraved plates found on industrial equipment.

## Layout & Spacing

This design system employs a **Fixed Grid** on desktop to maintain the composed, high-end feel of a luxury catalog. 

- **Grid:** A 12-column grid with generous 24px gutters. Content should be centered with wide margins to create a sense of exclusivity and focus.
- **Rhythm:** An 8px linear scale governs all internal padding. 
- **Reflow:** On mobile, the grid collapses to 4 columns. Neomorphic elements should increase in size to ensure "touchability," as the soft shadows require more visual real estate to be effective.

## Elevation & Depth

Depth is the core of this design system. We move away from traditional flat layers in favor of **Extruded Surface Geometry**.

- **Neumorphism:** Elements do not "float" above the background; they emerge from it. Use two shadows: a "highlight" shadow (top-left) using a semi-transparent #D3D3D3 and a "drop" shadow (bottom-right) using a deep #000000.
- **Convex vs. Concave:** Interactive buttons should appear convex (pushed out). When pressed or active, they transition to concave (sunken), mimicking the physical displacement of a button.
- **Materiality:** Use subtle grain overlays on Walnut containers and a brushed-metal CSS gradient (linear-gradient at 45 degrees) on Steel surfaces to enhance the tactile illusion.

## Shapes

The shape language reflects precision machining. While the overall feel is industrial, "sharp" edges are avoided to maintain the "Luxe" and "Soft-UI" aesthetic.

- **Standard Radius:** 0.5rem (8px) for cards and primary buttons to suggest a "milled" finish.
- **Knobs & Dials:** These must always be perfectly circular (full pill-shape) to reflect the circular nature of turntables and tonearm components.
- **Inlays:** Decorative dividers and spec-plates should use 0px roundedness to mimic metal nameplates attached to wood chassis.

## Components

- **Knobs (Rotary Sliders):** The hero component. A circular neomorphic disk with a Polished Brass indicator dot. As the user slides, the brass dot rotates and glows.
- **Buttons:** Large, tactile squares with rounded corners. The active state uses an inner shadow (concave) with a Polished Brass text color.
- **Cards:** Deep Walnut surfaces with a very subtle 1px brushed steel border at 10% opacity. 
- **Toggles:** Styled as heavy industrial flip-switches. The "on" state triggers a brass-colored glow at the base of the switch.
- **Inputs:** Sunken (concave) fields with JetBrains Mono text. The cursor should be a solid Polished Brass block.
- **VU Meters:** Digital representations of analog needles. Use a Steel background for the meter scale and a thin Brass needle for the readout.