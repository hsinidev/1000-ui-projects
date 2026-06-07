---
name: The Verdant Standard
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
  on-surface-variant: '#3e4a3f'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#6e7a6e'
  outline-variant: '#bdcabc'
  surface-tint: '#006d36'
  primary: '#006d36'
  on-primary: '#ffffff'
  primary-container: '#50c878'
  on-primary-container: '#005025'
  inverse-primary: '#66dd8b'
  secondary: '#4b53bc'
  on-secondary: '#ffffff'
  secondary-container: '#8991fe'
  on-secondary-container: '#1b218f'
  tertiary: '#5c5f60'
  on-tertiary: '#ffffff'
  tertiary-container: '#b0b2b3'
  on-tertiary-container: '#424546'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#83fba5'
  primary-fixed-dim: '#66dd8b'
  on-primary-fixed: '#00210c'
  on-primary-fixed-variant: '#005227'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.02em
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for the elite tier of estate and grounds management. It balances the vitality of landscape architecture with the cold precision of high-end logistics. The aesthetic is "Clinical Luxury"—a fusion of scientific meticulousness and country-club prestige.

The style leverages **Minimalism** to ensure that complex data remains legible and authoritative. By emphasizing high-resolution architectural photography and expansive whitespace, the UI evokes a sense of calm control. Every element is intentional, reflecting a brand personality that is professional, reliable, and utterly uncompromising in its standards.

## Colors

The palette is anchored by the high-contrast relationship between **Emerald Green** and **Navy**. Emerald represents the health and precision of the managed grounds, while Navy provides a foundation of institutional authority and trust.

**Crisp White** is the primary canvas, used to maintain a sterile, clinical environment that allows data and imagery to stand out. Accent colors are used sparingly to denote status; the primary Emerald is reserved for success states and primary actions, while Navy is utilized for navigation and structural headers.

## Typography

This design system utilizes **Inter** to achieve a modern, systematic, and utilitarian feel. The typeface’s tall x-height and neutral character provide the "clinical" clarity required for high-stakes management software.

Typography follows a strict hierarchical structure. Headlines use a slightly tighter letter-spacing to appear more "designed" and authoritative. Labels and metadata utilize uppercase styling with increased tracking to mimic the precise labeling found in architectural blueprints and scientific journals.

## Layout & Spacing

The layout employs a **fixed grid system** to maintain a sense of rigid order and predictability. A 12-column grid is centered within the viewport, utilizing generous 64px margins to frame the content like a piece of fine art.

Spacing is governed by an 8px baseline rhythm. This ensures that every element—from the height of a button to the padding within a card—is mathematically aligned. High-density data views must maintain significant "breathing room" between sections to prevent visual fatigue and reinforce the elite, unhurried nature of the brand.

## Elevation & Depth

Depth is conveyed through **low-contrast outlines** and structural alignment rather than shadows. In keeping with the "clinical" and "sharp" directive, the UI avoids diffused light sources.

Hierarchy is created through a "Paper-on-Paper" approach:
- **Level 0 (Background):** Crisp White (#FFFFFF).
- **Level 1 (Containers):** Tertiary Grey (#F8F9FA) with a 1px solid border (#E0E0E0).
- **Active State:** A hairline stroke of Navy or Emerald to denote focus.

This flat, layered approach ensures that the interface feels grounded and engineered, emphasizing structural integrity over decorative effects.

## Shapes

The shape language is strictly **Sharp (0px radius)**. Every button, input field, card, and modal is defined by perfect 90-degree angles. 

Sharp edges communicate a high level of precision and technological sophistication. This lack of "softness" reinforces the meticulous and reliable nature of the brand, distinguishing it from consumer-grade software and aligning it with professional instrumentation and high-end architectural documentation.

## Components

### Buttons
Primary buttons are solid Navy or Emerald with centered, uppercase labels in white. They are perfectly rectangular with no rounding. Secondary buttons utilize a 1px Navy stroke with no fill.

### Input Fields
Inputs feature a 1px light grey bottom border only, or a full rectangular border with 0px radius. Labels sit above the field in a small, uppercase bold weight for a "form-like" clinical feel.

### Chips & Tags
Status indicators are rectangular blocks. Success states use a light Emerald tint with deep Emerald text. Administrative or neutral tags use Navy. They never have rounded ends; they are always sharp-cornered blocks.

### Icons
Iconography must be executed in 1px or 1.5px stroke weights. Icons should be geometric and avoid filled-in shapes. They function as precise markers rather than illustrative elements.

### Cards & Imagery
Cards are defined by thin 1px borders and no shadows. High-resolution imagery within cards should be "full-bleed" to the top and sides, maintaining the sharp-edged aesthetic. Imagery should favor natural light and architectural perspectives of manicured landscapes.