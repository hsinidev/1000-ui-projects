---
name: AlumniSphere
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#434843'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#161817'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a2c2b'
  on-tertiary-container: '#929392'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e3e1'
  tertiary-fixed-dim: '#c6c7c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#454746'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  h1:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: notoSerif
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: notoSerif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  button:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

This design system is built upon a foundation of **Heritage Minimalism**. It targets a high-end, professional demographic of graduates who value prestige, legacy, and exclusive networking. The visual narrative balances the weight of institutional history with the fluid connectivity of a modern digital network.

The aesthetic evokes a "digital private club" atmosphere. It utilizes expansive whitespace—referencing high-end editorial print—to allow content to breathe and to signify luxury. The emotional response should be one of quiet confidence, belonging, and institutional pride. The interface avoids trendy gimmicks in favor of timeless structural clarity and subtle, high-value accents.

## Colors

The color palette is anchored by **Forest Green**, representing growth, stability, and academic tradition. This serves as the primary brand color for high-importance elements and typography. 

**Gold** is used sparingly as a "prestige accent." It should be reserved for CTAs, active states, and decorative borders that signify achievement or premium status. **Off-White** serves as the primary canvas, providing a warmer, more sophisticated alternative to pure white, reducing eye strain and enhancing the "ivory tower" academic feel.

- **Primary:** Forest Green for headers, primary buttons, and deep backgrounds.
- **Secondary:** Gold for interactive highlights and iconography.
- **Neutral:** A range of greys derived from the forest green hue to ensure harmonic cohesion.

## Typography

This design system employs a classic typographic pairing to bridge the gap between tradition and technology. 

**Noto Serif** is the voice of the institution. It is used for all major headings to convey authority and elegance. Large headings should use a tighter letter spacing to maintain a cohesive visual block.

**Inter** provides the functional backbone. Its neutral, highly legible character is used for all body copy, UI controls, and data-heavy displays. For navigation and small labels, an uppercase "Label-Caps" style is used with increased letter spacing to provide an airy, modern feel that complements the serif headers.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid Grid**. Content is housed within a 12-column grid with a maximum width of 1200px on desktop to ensure optimal line lengths for reading. 

Spacing is intentionally generous. We utilize "macro-white-space" (the `xl` unit) between major sections to emphasize the premium nature of the brand. Alignment should be predominantly left-aligned for text to maintain a structured, clean-cut professional look, while decorative gold dividers can be used to separate thematic content blocks. On mobile, margins should be a minimum of 20px to ensure the interface doesn't feel cramped.

## Elevation & Depth

This design system avoids heavy shadows and skeuomorphism in favor of **Tonal Layering and Fine Outlines**. 

Depth is achieved through the use of subtle color shifts in the background (e.g., placing a white card on an off-white background). When elevation is necessary for interactivity (like a hovering card), use an extremely soft, diffused shadow: `0px 10px 30px rgba(27, 48, 34, 0.05)`. 

Gold accents are used to create "visual depth" through thin 1px borders rather than 3D effects. This maintains a flat, sophisticated profile while clearly defining interactive areas.

## Shapes

The shape language is **Soft and Architectural**. We use a subtle corner radius (`0.25rem`) for standard components like input fields and buttons. This provides a modern touch without appearing overly "bubbly" or casual.

Larger containers like cards or image modules may use a larger radius (`0.5rem`) to feel more approachable. Profile avatars and specific "Connect" icons should be circular to represent the "Sphere" and the concept of a closed, unified community.

## Components

### Buttons
- **Primary:** Forest Green background with white Inter medium text. No border.
- **Secondary:** Transparent background with a 1px Gold border and Gold text.
- **Ghost:** Forest Green text with no background, used for low-priority actions.

### Cards
- **Directory Cards:** White background, 1px Off-White border, subtle shadow on hover.
- **Event Cards:** Top-heavy with high-quality photography, using a Gold accent bar at the bottom.

### Inputs
- Underlined style or subtle 1px Forest Green (low opacity) border. 
- Focus state: Border becomes 1px Gold with a very faint gold outer glow.

### Lists
- Clean, high-contrast rows. Use the "Label-Caps" style for category headers.
- Use 24px vertical padding between list items to maintain the premium whitespace.

### Chips/Tags
- Small, uppercase Inter font. Forest Green text on a very light Forest Green tint (5% opacity) background. Use the "Soft" radius.

### Exclusive Elements
- **Alumni Badge:** A circular gold-bordered element used for verified alumni status.
- **Legacy Divider:** A 1px wide horizontal gold line used to separate major page sections.