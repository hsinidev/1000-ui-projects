---
name: Lumina Medical
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#43474f'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#747780'
  outline-variant: '#c4c6d0'
  surface-tint: '#3f5f92'
  primary: '#001736'
  on-primary: '#ffffff'
  primary-container: '#002b5c'
  on-primary-container: '#7594cb'
  inverse-primary: '#aac7ff'
  secondary: '#595f66'
  on-secondary: '#ffffff'
  secondary-container: '#dde3eb'
  on-secondary-container: '#5f656c'
  tertiary: '#001639'
  on-tertiary: '#ffffff'
  tertiary-container: '#002a60'
  on-tertiary-container: '#5091ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aac7ff'
  on-primary-fixed: '#001b3e'
  on-primary-fixed-variant: '#264779'
  secondary-fixed: '#dde3eb'
  secondary-fixed-dim: '#c1c7cf'
  on-secondary-fixed: '#161c22'
  on-secondary-fixed-variant: '#41474e'
  tertiary-fixed: '#d8e2ff'
  tertiary-fixed-dim: '#adc7ff'
  on-tertiary-fixed: '#001a41'
  on-tertiary-fixed-variant: '#004493'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-mobile: 24px
  touch-target-min: 56px
---

## Brand & Style

This design system is built on the pillars of **Precision, Clarity, and Empathy**. It serves a premium patient base seeking life-changing ophthalmic procedures. The aesthetic moves beyond traditional healthcare "coldness" into a **Corporate/Modern** style with **Minimalist** influences, evoking the feeling of a high-end tech laboratory that is both welcoming and scientifically superior.

The visual narrative focuses on the "restoration of sight." This is achieved through expansive whitespace (representing clarity), high-contrast elements (ensuring accessibility), and a "glass-like" purity in the UI layers. Every interaction must feel intentional and effortless, reducing cognitive load for patients who may be experiencing visual impairment.

## Colors

The palette is centered around **Optical Blue**, a deep, authoritative navy that anchors the brand in medical expertise and trust. **Crystal White** serves as the primary canvas, providing a sterile, high-end backdrop that maximizes readability.

**Silver** is utilized as a sophisticated accent for borders, dividers, and inactive states, mimicking the precision instruments used in surgery. A secondary, more vibrant blue is reserved for critical action triggers to ensure they are unmistakable for users with blurred vision. All color combinations must strictly adhere to WCAG 2.1 AA standards for contrast.

## Typography

This design system prioritizes legibility above all. **Manrope** is used for headlines to provide a modern, technical, yet balanced feel. Its geometric construction ensures that characters are distinct even when blurred.

**Inter** is the workhorse for all functional text and body copy. It is selected for its exceptional x-height and neutral personality. To accommodate patients with cataracts or post-LASIK sensitivity, the base body size is set higher than standard (18px/20px) with generous line heights to prevent "crowding" of text.

## Layout & Spacing

The design system utilizes a **Fixed Grid** on desktop (12 columns) and a **Fluid Grid** on mobile (4 columns). The spacing rhythm is strictly based on an 8px scale.

A "Whitespace-First" philosophy is applied: margins between sections are significantly larger than traditional medical sites (minimum 80px - 120px) to provide a sense of calm and focus. Interactive elements must maintain a minimum distance of 16px from one another to prevent accidental taps, catering to users with reduced motor precision or visual clarity.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Ambient Shadows**. 

- **Level 0 (Base):** Crystal White background.
- **Level 1 (Cards):** Pure White surface with a very soft, highly diffused 15% opacity Optical Blue shadow (Blur: 20px, Y: 4px).
- **Level 2 (Modals/Popovers):** Slightly more pronounced shadow with a 1px Silver border to define the edge clearly.

Depth is used sparingly to avoid visual clutter. Surfaces should feel like "sheets of light," using subtle 1px inner highlights in Silver to create a polished, high-tech glass effect.

## Shapes

The shape language is consistently **Rounded**. This softens the "clinical" nature of the product, making the technology feel accessible and human-centric. 

A standard radius of 8px (0.5rem) is used for most interface elements, while larger containers like pricing cards or hero image masks use 16px (1rem). Buttons and input fields should never have sharp corners, as rounded shapes are easier for the eye to track and process.

## Components

### Buttons & Inputs
- **Primary Action:** Solid Optical Blue background with white text. Minimum height of 56px to ensure a large touch target. 
- **Input Fields:** Silver 2px borders that transition to Optical Blue on focus. Labels must always be visible (no floating labels that disappear).

### Selection Controls
- **Checkboxes/Radios:** Oversized (24px) with high-contrast checkmarks. The "hit area" should extend to the entire label row.
- **Segmented Controls:** Used for switching between procedure types, using a subtle "sliding" micro-animation.

### Cards & Lists
- **Service Cards:** Use a Level 1 shadow. Include a "Crystal" icon style—line icons in Optical Blue with a soft blue circular background.
- **Medical Data Lists:** Clear horizontal separators in Silver with 24px of vertical padding between items.

### Specialist Components
- **Vision Toggle:** A micro-animation component that allows users to increase font size or contrast globally.
- **Progress Steppers:** For surgical journeys, using a thick 4px line to clearly indicate the path from consultation to recovery.