---
name: High-Voltage Technical
colors:
  surface: '#111127'
  surface-dim: '#111127'
  surface-bright: '#37374f'
  surface-container-lowest: '#0c0c22'
  surface-container-low: '#191930'
  surface-container: '#1d1d34'
  surface-container-high: '#28283f'
  surface-container-highest: '#33324a'
  on-surface: '#e2dfff'
  on-surface-variant: '#cac7b4'
  inverse-surface: '#e2dfff'
  inverse-on-surface: '#2e2e46'
  outline: '#939180'
  outline-variant: '#484739'
  surface-tint: '#cbcb6a'
  primary: '#ffffff'
  on-primary: '#323200'
  primary-container: '#e8e883'
  on-primary-container: '#67680f'
  inverse-primary: '#616207'
  secondary: '#bfc2ff'
  on-secondary: '#181d8c'
  secondary-container: '#3239a3'
  on-secondary-container: '#a9afff'
  tertiary: '#ffffff'
  on-tertiary: '#2f3131'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#636565'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e8e883'
  primary-fixed-dim: '#cbcb6a'
  on-primary-fixed: '#1d1d00'
  on-primary-fixed-variant: '#494900'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#111127'
  on-background: '#e2dfff'
  surface-variant: '#33324a'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
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
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1280px
---

## Brand & Style

The design system is engineered to evoke the precision and raw energy of commercial electrical engineering. It targets a professional audience that values technical mastery, safety, and modern infrastructure. The aesthetic is "High-Voltage Technical"—a blend of high-contrast bold elements and neon accents set against a deep, structural void. 

This design system utilizes a dark-mode-first approach to simulate a high-tech control room or schematic interface. It leverages elements of **Brutalism** through sharp edges and heavy strokes, combined with **Vaporwave-inspired neon accents** to create "glowing" focal points. The emotional response is one of controlled power, expertise, and absolute reliability.

## Colors

The palette is built on a foundation of "Deep Navy" (#000080), serving as the primary background color to provide maximum depth. "Electric Yellow" (#FDFD96) acts as the high-visibility primary color, used for critical actions and glowing accents. 

To achieve the "high-voltage" effect, the primary yellow should be treated with an outer glow (bloom) when used on borders or icons. "Crisp White" is reserved for high-readability body text and technical data points. A deeper neutral (#0A0A20) is used for component backgrounds to create subtle layering against the navy base.

## Typography

The design system utilizes **Space Grotesk** for all headings and labels to lean into its geometric, technical characteristics. Its open counters and distinct glyphs mimic engineering blueprints and digital readouts. 

**Inter** is employed for body copy to ensure maximum legibility when displaying dense technical specifications or service descriptions. Headings should be set with tight letter spacing to feel aggressive and impactful, while labels should be frequently capitalized and tracked out to evoke a "serial number" or "warning label" aesthetic.

## Layout & Spacing

This design system follows a **fixed grid model** for desktop to maintain the rigidity of a technical document. A 12-column grid is used with generous 24px gutters. The layout rhythm is strictly based on an 8px base unit.

Components and sections should be separated by significant vertical gaps to allow "neon" elements space to breathe and glow without visual interference. Alignment should be sharp and mathematical, avoiding organic or offset placements in favor of a structured, modular hierarchy.

## Elevation & Depth

Depth in this design system is created through **neon-line accents** and **tonal layering** rather than traditional drop shadows. Surfaces do not "float" in a 3D space; instead, they appear as illuminated panels on a dark terminal.

1.  **Level 0 (Base):** Deep Navy background.
2.  **Level 1 (Panels):** Neutral Navy (#0A0A20) with a 1px solid border.
3.  **Level 2 (Active/Glow):** Panels with a 1px Electric Yellow border and a 4px-8px outer glow (box-shadow) of the same color to simulate illumination.

Backdrop blurs are used sparingly behind technical overlays to maintain focus on data.

## Shapes

The shape language of the design system is **strictly sharp (0px)**. All buttons, cards, and input fields must feature 90-degree angles to reinforce the professional, industrial nature of the electrical firm. 

Circular shapes are reserved exclusively for status indicators (e.g., "Live" or "Offline" lights) and specific technical icons. This geometric severity ensures the UI feels like a precision instrument rather than a consumer app.

## Components

### Buttons
Primary buttons are solid Electric Yellow with Deep Navy text, using bold caps. Secondary buttons are "Ghost" style with a 2px Electric Yellow border that glows on hover.

### Cards
Cards are constructed with the Neutral Navy background and sharp corners. They feature a "neon header" accent—a 2px horizontal yellow line at the top—or a full neon border for featured content.

### Inputs & Form Fields
Input fields use a 1px white border with low opacity (20%). Upon focus, the border turns Electric Yellow with a subtle glow, and the label transforms into the "technical-data" style above the field.

### Technical Icons
Icons must be monoline (1.5px stroke) and geometric. They should resemble circuit symbols or architectural notations. When active, icons inherit the Electric Yellow glow.

### Status Indicators
Small, circular "lamps" that use high-saturation red, green, or yellow to indicate system status, mimicking the physical LEDs found on electrical panels.