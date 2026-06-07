---
name: Rugged Technical
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
  on-surface-variant: '#e4bfb1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#ab8a7d'
  outline-variant: '#5b4137'
  surface-tint: '#ffb599'
  primary: '#ffb599'
  on-primary: '#5a1c00'
  primary-container: '#ff5f00'
  on-primary-container: '#531a00'
  inverse-primary: '#a63b00'
  secondary: '#dec1ac'
  on-secondary: '#3f2d1e'
  secondary-container: '#574333'
  on-secondary-container: '#ccb09c'
  tertiary: '#c1c8c7'
  on-tertiary: '#2b3232'
  tertiary-container: '#8e9595'
  on-tertiary-container: '#272e2e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#ffb599'
  on-primary-fixed: '#370e00'
  on-primary-fixed-variant: '#7f2b00'
  secondary-fixed: '#fbddc7'
  secondary-fixed-dim: '#dec1ac'
  on-secondary-fixed: '#28180b'
  on-secondary-fixed-variant: '#574333'
  tertiary-fixed: '#dde4e3'
  tertiary-fixed-dim: '#c1c8c7'
  on-tertiary-fixed: '#161d1d'
  on-tertiary-fixed-variant: '#414848'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
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
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  code-tech:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
spacing:
  base: 4px
  unit-1: 4px
  unit-2: 8px
  unit-4: 16px
  unit-6: 24px
  unit-8: 32px
  unit-12: 48px
  unit-16: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built for the high-stakes environment of mountain expeditions. The brand personality is authoritative, resilient, and utilitarian, prioritizing functional clarity over decorative flair. It evokes a sense of "field equipment" rather than a lifestyle app.

The design style is a hybrid of **Brutalism** and **High-Contrast Modernism**. It utilizes a strict underlying grid to imply structural integrity. Visual elements should feel machined and durable, using heavy strokes and technical markers (like coordinate crosshairs or corner brackets) to reinforce the expeditionary narrative. The emotional response is one of safety, preparedness, and precision.

## Colors

The palette is rooted in the "Safety-Vest Orange" primary color (#FF5F00), used exclusively for critical actions and navigational cues. This high-visibility hue ensures legibility against complex topographical backgrounds. 

The background architecture uses "Neutral" (#1A1A1A) and "Slate Gray" (#2C3333) to provide a low-glare, dark-mode foundation suitable for outdoor use. "Earthy Brown" (#4A3728) is used for secondary containers and subtle textural shifts. Accent borders and grid lines should use a 20% opacity white to maintain a technical "blueprint" feel without distracting from the content.

## Typography

Typography is a tool for data delivery. For headings and technical labels, **Space Grotesk** provides a geometric, slightly futuristic aesthetic reminiscent of radar readouts and instrumentation. Headings should often be paired with numeric prefixes (e.g., 01, 02) to reinforce a sequential, tactical logic.

**Inter** is the workhorse for body copy, selected for its exceptional legibility at small sizes and high contrast ratios. Use `label-caps` for all metadata and system statuses to differentiate them from narrative text. All uppercase text should have increased letter spacing to ensure readability under harsh lighting conditions.

## Layout & Spacing

This design system employs a **Fixed Grid** model within a maximum container width of 1440px. The layout is based on a strict 12-column grid. 

A unique "visible grid" philosophy is applied: vertical and horizontal lines (1px width) may be used to separate major sections, mimicking a topographic map or technical manual. Spacing is strictly mathematical, built on a 4px baseline. Large margins (32px+) are preferred to keep the UI from feeling claustrophobic, ensuring that each data point or interactive element has a clear "clearance zone" for gloved-hand interaction or high-vibration environments.

## Elevation & Depth

This design system rejects traditional shadows and ambient depth. Instead, it uses **Bold Borders** and **Tonal Layering** to define hierarchy.

- **Level 0 (Base):** The deepest neutral background (#1A1A1A).
- **Level 1 (Panels):** Slate Gray (#2C3333) with a 1px solid border (#FFFFFF, 10% opacity).
- **Level 2 (Active/Floating):** Earthy Brown (#4A3728) with high-visibility orange accents.

Depth is communicated through "stacking" indicators rather than light sources. For example, a modal does not cast a shadow; it sits on a semi-opaque black overlay and is framed by a distinct 2px safety-orange border.

## Shapes

The shape language is strictly **Sharp (0px)**. Every element—buttons, cards, input fields—must have 90-degree corners to reflect a "machined" and "rugged" look. 

To add visual interest without using rounds, use "clipped corners" (45-degree chamfers) on primary action buttons or decorative frame elements. This reinforces the tactical, military-grade aesthetic. Icons should follow this logic, using straight lines and sharp angles where possible.

## Components

### Buttons
Primary buttons use a solid Safety-Vest Orange fill with black text, strictly uppercase. Secondary buttons use a transparent background with a 2px Slate Gray border. On hover, buttons should invert colors or display a "scanning" glitch effect to signal responsiveness.

### Cards
Cards are treated as "Modules." They feature 1px Slate Gray borders and a header section separated by a horizontal line. Technical metadata (e.g., coordinates, altitude, or timestamp) should be tucked into the corner of the card in `label-caps` typography.

### Input Fields
Inputs are rectangular blocks with a dark background. The focus state is indicated by a 2px Safety-Vest Orange bottom border. Use monospaced-style characters for numeric inputs to ensure digit alignment.

### Functional Iconography
Icons must be "Line-Weight 2px" and strictly functional. Use symbols derived from navigation, surveying, and weather instrumentation. Avoid soft, illustrative styles.

### Additional Components
- **The Progress Bar:** Designed as a "Battery Meter" or "Signal Strength" indicator to track expedition milestones.
- **The Coordinate Grid:** A decorative background element that pulses subtly, providing a sense of real-time tracking and technical sophistication.