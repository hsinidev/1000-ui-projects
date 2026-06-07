---
name: Kinetic Art Design System
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#45474b'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#75777c'
  outline-variant: '#c5c6cc'
  surface-tint: '#585f6b'
  primary: '#555c68'
  on-primary: '#ffffff'
  primary-container: '#6e7582'
  on-primary-container: '#fdfcff'
  inverse-primary: '#c0c7d5'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#5a5c5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#737576'
  on-tertiary-container: '#fcfcfe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce3f1'
  primary-fixed-dim: '#c0c7d5'
  on-primary-fixed: '#151c26'
  on-primary-fixed-variant: '#404753'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#e2e2e4'
  tertiary-fixed-dim: '#c6c6c8'
  on-tertiary-fixed: '#1a1c1d'
  on-tertiary-fixed-variant: '#454749'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  body-base:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  technical-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
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
  margin-mobile: 16px
  margin-desktop: 64px
  max-width: 1280px
---

## Brand & Style

This design system is anchored in the intersection of traditional craftsmanship and modern engineering. It targets a discerning audience that appreciates the silent complexity of a well-oiled machine and the warmth of natural materials. The emotional response is one of **serene fascination**—a quiet, meditative experience that mirrors the rhythmic motion of a mechanical automaton.

The aesthetic blends **Minimalism** with **Tactile/Skeuomorphic** accents. While the layout remains airy and clean, individual UI elements are treated as physical objects. Interaction is defined by mechanical precision; buttons should feel like machined metal and containers like inlaid wood. The style avoids excessive digital "glow," opting instead for realistic shadows and material-based depth to evoke the tactile quality of a luxury desktop accessory.

## Colors

The palette is derived from raw, high-quality materials.
- **Brushed Steel (Primary):** A mid-tone cool gray used for structural elements, iconography, and technical borders. It represents the "machine" within.
- **Warm Wood (Secondary):** A rich walnut brown used sparingly for high-impact accents, call-to-action backgrounds, or as a signature "organic" touch to offset the cool metal.
- **Crisp White (Surface):** The primary background color, providing a clinical, museum-like environment for the products to reside in.
- **Ink Black (Neutral):** Used for primary typography to ensure maximum legibility against white and gray surfaces.

Color application must prioritize high contrast between technical data and lifestyle imagery. Transitions between states should use color shifts that mimic the way light hits a rotating metal surface.

## Typography

This design system employs a dual-font strategy to balance luxury with technicality.

**Noto Serif** is reserved for storytelling, product names, and editorial headlines. It should be typeset with generous leading to convey a sense of prestige and unhurried elegance.

**Space Grotesk** is used for all functional and technical information. Its geometric, slightly futuristic construction echoes the precision of mechanical blueprints. Technical specs, pricing, and navigational labels should be set in this face, often in all-caps for labels to emphasize the "stamped metal" aesthetic. 

Maintain a strict hierarchy: use the serif to speak to the soul of the user, and the sans-serif to speak to their intellect.

## Layout & Spacing

The layout follows a **Fixed Grid** model to maintain a curated, gallery-like feel. Content is centered on a 12-column grid with a maximum width of 1280px, ensuring that on ultra-wide monitors, the interface remains a focused "object" in the center of the screen.

Whitespace is used as a luxury commodity. The spacing rhythm is based on an 8px base unit. Margins between disparate sections should be aggressive (often 120px+) to allow the products to "breathe" and to emphasize the silence and serenity of the brand. Horizontal alignment should be rigid and precise, mimicking the alignment of gears and plates in a physical movement.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Ambient Shadows**. Instead of high-elevation floating shadows, this design system uses "inset" and "low-drop" shadows to suggest that elements are either carved into wood or resting firmly on a steel surface.

- **Surface Levels:** The background is always the lowest level (Level 0). Cards and containers are Level 1, using a 1px steel-colored border or a subtle 4px blur shadow.
- **Shadow Character:** Shadows are tight, crisp, and slightly tinted with the secondary wood color to feel natural. Avoid large, diffuse blurs; think of the shadow cast by a metal ruler on a desk under a desk lamp.
- **Micro-interactions:** When an element is pressed, it should visually "sink" (using an inner shadow) to provide tactile feedback consistent with a physical mechanical button.

## Shapes

The shape language is driven by **Machined Precision**. 

The base roundedness is set to `1` (0.25rem). This is intended to simulate "eased edges"—metal or wood that has been sanded or milled just enough to be comfortable to the touch, without losing its geometric integrity. 

- **Primary containers:** Sharp or slightly softened (4px) corners.
- **Buttons:** Rectangular with the same 4px radius, unless it's a "toggle" component which may be fully circular to represent a dial or a screw head.
- **Dividers:** Hairline strokes (0.5px to 1px) in Brushed Steel, suggesting the joints between mechanical parts.

## Components

### Buttons
Primary buttons use the **Warm Wood** background with white **Space Grotesk** text. Hover states should feature a subtle "sheen" transition, mimicking light reflecting off a finished surface. Secondary buttons are "ghost" style with a **Brushed Steel** 1px border.

### Cards
Product cards should appear as trays. Use a background of #F5F5F7 with a 1px border. On hover, the card should gain a subtle outer shadow, and the image within (the kinetic toy) should subtly animate or change angle, suggesting movement.

### Input Fields & Controls
Form fields are minimal, defined only by a bottom border in steel. Toggles and switches are designed as mechanical levers or sliders. The "knob" of a slider should have a metallic texture or a subtle radial gradient to suggest volume.

### Lists
Technical specs are displayed in a clean list format with a monospaced feel. Use **Label-Caps** for headers (e.g., MATERIAL, DIMENSIONS, CALIBER) followed by the value in **Body-Base**.

### Mechanical Indicators
Special components such as "Movement Progress" or "Power Reserve" bars should look like physical gauges, using linear gradients that mimic metallic cylinders rather than flat digital progress bars.