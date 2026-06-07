---
name: Industrial Security Architecture
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c6c5d4'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#908f9d'
  outline-variant: '#454652'
  surface-tint: '#bcc2ff'
  primary: '#bcc2ff'
  on-primary: '#152383'
  primary-container: '#283593'
  on-primary-container: '#9aa5ff'
  inverse-primary: '#4955b3'
  secondary: '#bdc2ff'
  on-secondary: '#1b247f'
  secondary-container: '#343d96'
  on-secondary-container: '#a8afff'
  tertiary: '#c7c6c4'
  on-tertiary: '#303130'
  tertiary-container: '#3f403f'
  on-tertiary-container: '#acabaa'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe0ff'
  primary-fixed-dim: '#bcc2ff'
  on-primary-fixed: '#000c62'
  on-primary-fixed-variant: '#303c9a'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bdc2ff'
  on-secondary-fixed: '#000767'
  on-secondary-fixed-variant: '#343d96'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c4'
  on-tertiary-fixed: '#1b1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-spec:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  border-thick: 2px
  border-heavy: 3px
---

## Brand & Style

The design system is engineered to project an image of absolute structural integrity, high-performance reliability, and industrial-grade security. It targets technical professionals and enterprise stakeholders who require the digital equivalent of a reinforced steel vault. 

The visual language draws heavily from **Industrial Brutalism** and **High-Tech Corporate** styles. It rejects soft, organic forms in favor of rigid geometry, high-contrast clarity, and physical metaphors of reinforced hardware. Every element is designed to feel "bolted down" and immovable, evoking a sense of calm authority and impenetrable protection.

## Colors

The palette is anchored by a foundational **Deep Black**, providing a high-contrast canvas that mimics professional server environments. **Security Blue** and **Deep Indigo** serve as the primary brand drivers, used to highlight critical paths and active states with clinical precision.

**Platinum Silver** is utilized for primary text and structural borders, providing the "brushed metal" aesthetic required for industrial hardware metaphors. Status colors are saturated and intense, ensuring high visibility against the dark backdrop for immediate technical feedback.

## Typography

This design system utilizes **Inter** for all UI elements and headings to maintain a neutral, systematic appearance. Weight is used to establish hierarchy, with heavy bolds for headers and regular weights for dense technical information.

For technical specifications, checksums, and data readouts, a **Monospace** stack is mandatory. This ensures character alignment in data tables and reinforces the "high-performance storage" narrative. All labels and secondary metadata should be rendered in uppercase with increased letter spacing to mimic industrial stamped metal plates.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to provide a sense of structure and predictability. Content is organized within a 12-column grid with 24px gutters. The spacing rhythm is strictly derived from an 8px base unit, ensuring mathematical consistency across all viewports.

Margins are generous at the edges of the screen to focus the user's attention on the "central vault" of content, while internal component padding is tight and efficient to maximize information density.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Hardened Outlines** rather than soft shadows. Higher elevation levels are indicated by lighter shades of grey/indigo and thicker borders.

To achieve the "brushed metal" effect, containers should use subtle linear gradients (e.g., a 135-degree tilt from `rgba(229, 228, 226, 0.05)` to `rgba(0, 0, 0, 0)`). Borders are the primary indicators of separation; use 2px or 3px solid lines in Platinum Silver for all primary cards and containers. Micro-interactions should feel mechanical: when a user interacts with a button, it shouldn't "softly glow," but rather "click" into a high-contrast inverted state.

## Shapes

The shape language is strictly **Sharp**. A `0px` border-radius is the default for all cards, buttons, and input fields. This lack of rounding reinforces the "Hardened" UI concept, suggesting that the components are cut from solid material.

In rare instances where "very subtle rounding" is required for specific hardware-mimicking components, a maximum radius of `2px` may be applied, but this must be used sparingly to avoid softening the overall industrial aesthetic.

## Components

### Buttons & Controls
Buttons are "mechanical" blocks. Default state: 2px Platinum Silver border, transparent background. Active/Pressed state: Background fills with Security Blue, text shifts to White. Interactions must be instant (0ms - 50ms) to feel like physical switches.

### Hardened UI Cards
Cards are the primary container. They must feature a 2px border and a subtle top-to-bottom brushed metal gradient. Header areas within cards should be separated by a 2px horizontal rule.

### Inputs & Technical Specs
Input fields use the Deep Black background with a 2px Silver border that turns Security Blue on focus. Use the Monospace font for all user input to emphasize data integrity.

### Status Indicators
Status chips should look like LED indicators: small, high-saturation squares or rectangles with a "lit" appearance (0.5 inner glow) but no outer blur.

### Data Grids
Tables are high-density with 1px indigo dividers. Technical specs (bitrate, capacity, encryption level) must always use the Monospace typography level for perfect vertical alignment of numbers.