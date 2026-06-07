---
name: Premium Tech Retailer
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#cac6c3'
  on-tertiary: '#32302f'
  tertiary-container: '#131211'
  on-tertiary-container: '#807d7b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e6e1df'
  tertiary-fixed-dim: '#cac6c3'
  on-tertiary-fixed: '#1c1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
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
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is engineered to evoke the feeling of high-performance instrumentation and elite craftsmanship. The brand personality is clinical, authoritative, and unapologetically futuristic. It targets a discerning audience that values technical specification as much as aesthetic beauty.

The visual style combines **Minimalism** with **Glassmorphism** to create a multi-layered interface that feels like a head-up display (HUD). By utilizing a "Dark Mode" foundation, the interface recedes to allow high-contrast product photography to take center stage. The aesthetic relies on mathematical precision, rigid geometric alignments, and the tension between deep blacks and vibrant neon accents to simulate a high-tech laboratory or aerospace interface.

## Colors

This design system operates on a strictly nocturnal palette. **Pure Black (#000000)** is used for the base canvas to provide infinite depth and maximize the contrast of hardware photography. **Deep Charcoal (#121212)** serves as the primary surface color for structural elements like sidebars and cards, creating a subtle distinction from the background.

**Neon Blue (#00F3FF)** is the sole high-energy accent. It is reserved for critical interactive paths, active states, and data visualizations. It should be used sparingly to maintain its impact as a "signal" color. Neutral grays provide functional legibility for secondary text and borders without competing with the primary content.

## Typography

The typography strategy utilizes a dual-font approach to balance editorial impact with technical clarity. **Space Grotesk** is employed for headlines and technical data points, providing a geometric, futuristic skeleton that aligns with the "high-tech" directive. 

**Inter** is used for all body copy and UI labels to ensure maximum readability and a neutral, systematic feel. Uppercase treatments are applied to labels and small identifiers to mimic the instructional markings found on professional electronic equipment. Line heights are kept tight for headlines to maintain a compact, architectural feel, while body copy is given more breathing room for legibility.

## Layout & Spacing

This design system uses a **Fixed Grid** model for desktop and a fluid system for mobile. The layout is built on a 12-column grid with a 1px vertical and horizontal "ruler" aesthetic—often using thin borders rather than empty whitespace to define zones. 

The spacing rhythm is strictly derived from a 4px base unit. This ensures that every element, from the width of a button to the padding of a card, feels mathematically calculated. Gutters are intentionally narrow (16px) to reinforce the dense, high-information density of a technical dashboard.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and tonal layering rather than traditional drop shadows. Overlays and modal windows utilize a `backdrop-filter: blur(20px)` with a semi-transparent Deep Charcoal fill (opacity 70-80%). 

To define edges without adding visual bulk, the design system employs "Rim Lighting"—a 1px inner border using a low-opacity white or Neon Blue to simulate a light catch on a physical edge. This creates a sense of depth that feels like stacked glass panels. Shadows, when used for extreme focus, should be sharp and high-offset, mimicking a single harsh light source rather than soft ambient light.

## Shapes

The shape language is defined by **Sharp (0)** corners. This reinforces the "Rigid Geometric" requirement, suggesting precision engineering and structural integrity. All buttons, input fields, and product containers must feature 90-degree angles. 

The only exception to the rectangular rule is the use of 45-degree "clipped corners" for decorative technical accents or specific status tags, further leaning into the military-industrial or aerospace aesthetic.

## Components

### Buttons
Primary buttons feature a solid Neon Blue fill with black text. Secondary buttons use a 1px Neon Blue border with transparent backgrounds. All buttons have a sharp-cornered hover state that may include a subtle outer glow (neon bloom effect).

### Input Fields
Inputs are defined by a 1px Deep Charcoal bottom border that turns Neon Blue on focus. Labels are always positioned above the input in `label-caps` typography. Error states replace the Neon Blue with a high-contrast Red, maintaining the same 1px stroke.

### Cards
Cards use a Deep Charcoal background against the Pure Black canvas. They feature 1px borders (#333333). When focused or hovered, the border transitions to Neon Blue. Product cards emphasize the image, with technical specs displayed in `data-mono` typography.

### Chips & Tags
Chips are rectangular with a 1px border. Status indicators (e.g., "In Stock") use a small solid square of Neon Blue next to the text, rather than a rounded dot.

### Product Grid
A dense, multi-column grid where items are separated by 1px "hairline" dividers. This creates a blueprint-like appearance for the storefront.