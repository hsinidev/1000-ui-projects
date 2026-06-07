---
name: Studio Precision
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c7c6ca'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#909094'
  outline-variant: '#46474a'
  surface-tint: '#c8c6c7'
  primary: '#c8c6c7'
  on-primary: '#303031'
  primary-container: '#1a1a1b'
  on-primary-container: '#848283'
  inverse-primary: '#5f5e5f'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#ffb77b'
  on-tertiary: '#4d2700'
  tertiary-container: '#2c1400'
  on-tertiary-container: '#b87333'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e3'
  primary-fixed-dim: '#c8c6c7'
  on-primary-fixed: '#1b1b1c'
  on-primary-fixed-variant: '#474647'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#ffb77b'
  on-tertiary-fixed: '#2e1500'
  on-tertiary-fixed-variant: '#6d3a00'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353437'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
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
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max: 1440px
---

## Brand & Style
This design system is built for the uncompromising audiophile, evoking the atmosphere of a professional recording studio. The brand personality is technical, authoritative, and sophisticated, emphasizing engineering excellence over mass-market trends. 

The visual style blends **Minimalism** with **Tactile** elements. It utilizes a dark, low-distraction environment to let product photography and technical data shine. The "Studio Sleek" aesthetic is achieved through the juxtaposition of vast negative space and hyper-detailed material textures. The interface should feel like a piece of high-end hardware—precise, weighted, and responsive. Use high-resolution macro photography of leather grains, machined aluminum, and copper wiring as structural background elements or within hero sections to ground the digital experience in physical reality.

## Colors
The palette is rooted in the "Deep Charcoal" (#1A1A1B), which serves as the primary canvas for the entire interface. This creates a high-end, low-light environment that reduces eye strain and highlights product details. 

**Metallic Silver** (#C0C0C0) is used for primary text and structural borders, providing a crisp, machined look. **Brushed Copper** (#B87333) is reserved strictly for high-priority interactive elements, accents, and data visualizations (such as frequency response curves). 

To mimic physical materials:
- Use linear gradients from `#2E2E30` to `#1A1A1B` for soft-touch surfaces.
- Use subtle 45-degree gradients on Silver elements to simulate reflective anodized aluminum.
- Apply copper highlights as "glow" effects or thin 1px accents to indicate power or active connectivity.

## Typography
The typographic system prioritizes legibility and technical clarity. **Inter** is the primary typeface, selected for its neutral, modern appearance and excellent performance at various weights. For technical readouts, labels, and metadata (e.g., Ohms, Decibels, Frequency), **Space Grotesk** is introduced to provide a subtle "engineered" feel without sacrificing readability.

High contrast is essential: use pure Silver or White for primary information against the Charcoal background. Secondary information should drop to 60% opacity. Tracking (letter spacing) should be tightened slightly for large headlines to maintain a "compressed" professional look, while labels should be tracked out for an open, airy technical feel.

## Layout & Spacing
The layout follows a **Fixed Grid** model for editorial precision. A standard 12-column grid is used with a generous 64px outer margin to ensure the content feels premium and uncrowded. 

Spacing is governed by a strict 8px base unit. 
- Use 24px (3 units) for standard gutters between cards and content blocks.
- Use larger vertical rhythm blocks (80px, 120px) to separate distinct product sections.
- Alignment should be rigorous; interactive elements should align to the typography's cap height to maintain a sense of structural integrity.

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layering** and physical metaphors rather than traditional shadows. 

- **Surface Levels:** The base level is #1A1A1B. Raised surfaces (cards, panels) use #252526 with a subtle 1px "inner-light" stroke on the top edge to simulate a beveled edge catching light.
- **In-set Elements:** Inputs and recessed areas use a darker #121213 with an inner shadow to feel "milled" into the surface.
- **Gradients:** Use soft radial gradients to mimic the way light hits matte, soft-touch materials. 
- **Active States:** Instead of elevation height, use the Brushed Copper accent as a "lit" state, mimicking an LED indicator on a piece of studio gear.

## Shapes
The shape language is "Technical Soft." While the aesthetic is sharp and precise, we avoid aggressive points to mimic the ergonomic nature of high-end headphones. 

- **Primary Radius:** 0.25rem (4px) for most interactive components like buttons and input fields, providing a "precision-milled" look.
- **Secondary Radius:** 0.5rem (8px) for larger cards and containers.
- **Macro Imagery:** Photography should be masked in circles or large-radius rectangles to contrast with the rigid grid of the UI.
- **Icons:** Use 1.5px or 2px stroke weights with squared ends to maintain the technical, minimalist feel.

## Components
- **Buttons:** Primary buttons feature a subtle vertical gradient mimicking brushed metal. Use the Copper accent for primary CTAs with a white label. Secondary buttons are outlined in 1px Silver with 20% opacity.
- **Chips/Badges:** Small, rectangular with a 2px radius. Use for technical specs like "LDAC," "APTX," or "ANC."
- **Input Fields:** Recessed backgrounds with a 1px Silver bottom border that turns Copper upon focus.
- **Cards:** Use a "Glassmorphism" variant for overlays—low opacity charcoal backgrounds with a heavy background blur (20px+) to maintain focus on the hardware photography beneath.
- **Sliders (Volume/EQ):** The track should be Deep Charcoal with a Copper "fill" and a Silver circular handle that looks like a machined dial.
- **Visualizers:** Audio waveforms and frequency response graphs should be rendered in a thin Copper stroke with a faint Copper outer glow to simulate an oscilloscope display.