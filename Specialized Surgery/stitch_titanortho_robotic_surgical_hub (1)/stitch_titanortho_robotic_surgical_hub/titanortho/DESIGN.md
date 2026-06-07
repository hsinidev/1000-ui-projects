---
name: TitanOrtho
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#434653'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#2559bd'
  primary: '#00327d'
  on-primary: '#ffffff'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#b1c5ff'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdf'
  on-secondary-container: '#626263'
  tertiary: '#353737'
  on-tertiary: '#ffffff'
  tertiary-container: '#4b4d4e'
  on-tertiary-container: '#bdbebe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
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
    letterSpacing: 0em
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
  max_width: 1440px
---

## Brand & Style

The design system is engineered to evoke a sense of surgical precision, robotic accuracy, and institutional trust. It targets a sophisticated audience of surgeons, medical stakeholders, and patients seeking high-tech orthopedic solutions. 

The aesthetic is **Industrial-Tech**, blending the cold, sterile reliability of a surgical suite with the advanced engineering of robotics. This is achieved through a high-contrast, structural approach that prioritizes clarity and functional hierarchy. Visuals should leverage subtle metallic textures and high-definition medical imagery to reinforce the "Titanium" narrative. The interface should feel like a high-end diagnostic instrument—uncompromising, expert, and focused.

## Colors

This design system utilizes a high-contrast palette to distinguish between structural elements and interactive points. 

- **Cobalt Blue (#0047AB):** The primary driver for action and critical technical highlights. It represents precision and modern medicine.
- **Titanium Grey (#707070):** Used for secondary information, borders, and structural divisions. It provides the "industrial" weight to the interface.
- **Stark White (#FFFFFF):** The primary surface color to maintain a clinical, sterile environment.
- **Support Accents:** Use subtle linear gradients moving from `#707070` to `#A0A0A0` to simulate brushed metal for headers or specialized cards.

## Typography

The typography strategy pairs **Space Grotesk** for headlines with **Inter** for functional text. 

- **Space Grotesk** provides a technical, slightly futuristic edge with its geometric apertures, perfect for high-level headings and data callouts.
- **Inter** is utilized for body copy and UI labels to ensure maximum legibility and a systematic, utilitarian feel essential for medical documentation.
- **Contrast:** High-level headers should use tighter letter-spacing, while technical labels and tags should use increased tracking and uppercase styling to mimic industrial equipment labeling.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to maintain rigorous alignment and order. 

- **Grid Model:** A 12-column grid system on desktop with a fixed 24px gutter. 
- **Rhythm:** An 8px base unit (derived from the 4px base) dictates all padding and margins to ensure technical consistency.
- **Layout Philosophy:** Content should be grouped in distinct, high-contrast modules. Use heavy top-borders on sections to ground the layout, creating a sense of "engineered" segments rather than a continuous fluid flow.

## Elevation & Depth

In this design system, depth is conveyed through **Low-contrast outlines** and **Tonal layering** rather than traditional soft shadows. This maintains the "hard-surface" industrial aesthetic.

- **Borders:** Use 1px or 2px solid strokes in Titanium Grey (#707070) or its lighter variants to define containers.
- **Layering:** Backgrounds are slightly off-white (#F5F7F9), while active modules are Stark White (#FFFFFF). 
- **Shadows:** When necessary for temporary overlays (modals), use "Technical Shadows"—short, sharp offsets with low blur and 20% opacity to suggest a physical object sitting closely on a laboratory surface.
- **Metallic Gradients:** Apply a subtle 45-degree linear gradient to primary action cards to give them a machined, three-dimensional quality.

## Shapes

The shape language is strictly **Sharp**. 

Rounded corners are avoided to reinforce the industrial, high-precision nature of surgical instruments. All buttons, input fields, cards, and containers feature 90-degree angles. This geometric rigidity communicates strength, accuracy, and a no-nonsense professional environment. Decorative elements should utilize 45-degree "chamfered" corners for specialized callouts to mimic the CNC-machined components found in orthopedic robotics.

## Components

- **Buttons:** Primary buttons are Cobalt Blue with white uppercase text. They should have a 1px inner border of a lighter blue to simulate a beveled edge. Hover states shift the background to a metallic grey gradient.
- **Input Fields:** Stark White background with a 1px Titanium Grey border. Use Inter Bold for labels, placed strictly above the field. Focus states use a 2px Cobalt Blue bottom-border.
- **Chips / Status Tags:** Rectangular boxes with high-contrast fills. "Active" or "Precision Met" statuses use Cobalt Blue; "Standard" uses Titanium Grey.
- **Cards:** White surfaces with 1px Grey borders. Headers within cards should be separated by a technical horizontal rule.
- **Data Visualizations:** Use Cobalt Blue for primary data points. Ensure all charts use sharp-angled lines and technical cross-hair markers.
- **Imagery:** Photography should be high-contrast, featuring cool-toned lighting, shallow depth of field focusing on metallic surgical instruments, or clean-room environments. Use "Blueprint" style overlays for robotic schematics.