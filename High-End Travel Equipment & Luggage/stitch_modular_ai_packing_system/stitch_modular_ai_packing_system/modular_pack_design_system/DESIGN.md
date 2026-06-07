---
name: Modular-Pack Design System
colors:
  surface: '#fbf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#fbf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f0'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e4e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#434842'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ed'
  outline: '#747872'
  outline-variant: '#c3c8c0'
  surface-tint: '#516352'
  primary: '#4e604f'
  on-primary: '#ffffff'
  primary-container: '#677967'
  on-primary-container: '#f7fff3'
  inverse-primary: '#b8ccb7'
  secondary: '#5e5f5c'
  on-secondary: '#ffffff'
  secondary-container: '#e0e0dc'
  on-secondary-container: '#626360'
  tertiary: '#4f5d71'
  on-tertiary: '#ffffff'
  tertiary-container: '#67758b'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e8d2'
  primary-fixed-dim: '#b8ccb7'
  on-primary-fixed: '#0f1f12'
  on-primary-fixed-variant: '#3a4b3b'
  secondary-fixed: '#e3e2df'
  secondary-fixed-dim: '#c7c7c3'
  on-secondary-fixed: '#1b1c1a'
  on-secondary-fixed-variant: '#464744'
  tertiary-fixed: '#d5e3fc'
  tertiary-fixed-dim: '#b9c7df'
  on-tertiary-fixed: '#0d1c2e'
  on-tertiary-fixed-variant: '#3a485b'
  background: '#fbf9f6'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2df'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-padding: 24px
  bento-gap: 16px
  section-margin: 48px
---

## Brand & Style

The design system is anchored in a philosophy of "Effortless Organization." It transforms the stressful task of packing into a curated, modular experience. The aesthetic leans heavily into **Modern Minimalism** with a **Bento-box layout** structure, organizing information into discrete, logical containers that reflect the physical act of packing cubes into a suitcase.

The UI should evoke a sense of professional preparation and calm. By using high-quality whitespace and a restrained palette, the design system ensures that the AI's guidance feels like a premium concierge service rather than a cluttered utility tool.

## Colors

The palette is designed for low cognitive load. **Sage Green** serves as the primary brand anchor, used for key actions and successful "packed" states. The **Off-White** background provides a warm, paper-like canvas that feels more sophisticated than pure white. 

**Slate** is used for text to maintain high legibility without the harshness of pure black. Status colors for weight alerts (Amber/Red) are applied with lower saturation to maintain the system's minimalist integrity while still providing clear visual cues for limits and errors.

## Typography

The design system utilizes **Manrope** for its modern, geometric construction and exceptional legibility across all sizes. It provides a technical yet friendly tone suitable for AI-guided assistance. 

For technical data—such as luggage weight, item counts, and dimensions—**JetBrains Mono** is introduced as a secondary label font. This monospaced addition reinforces the "precision" aspect of the system, making numerical data easy to scan and compare within the bento grid cells.

## Layout & Spacing

The layout follows a strict **Bento-box grid**. Elements are grouped into cards of varying sizes (1x1, 2x1, 2x2) that reflow based on the screen width.

- **Desktop:** 12-column grid with fixed 16px gaps between bento cells.
- **Tablet:** 6-column grid with 16px gaps.
- **Mobile:** Single column stack with 12px gaps.

Whitespace is used aggressively to separate categories (e.g., Electronics vs. Clothing). All modules within the bento grid should use internal padding of 24px to ensure content feels airy and premium.

## Elevation & Depth

Depth is achieved through **Soft Ambient Shadows** rather than traditional borders. Cards sit on the Off-White background with a subtle, large-radius shadow (0px 4px 20px rgba(71, 85, 105, 0.05)).

When an item is selected or a bento cell is "active," the shadow intensifies slightly, and the background shifts from Off-White to a pure White surface. This creates a "lift" effect that signals focus. Avoid heavy borders; use subtle 1px Slate-variant dividers only when necessary for internal list items.

## Shapes

The design system employs a **Large Radius** strategy. All primary bento containers use a `1.5rem` (24px) corner radius to create an approachable, soft-touch feel similar to high-end travel gear. 

Internal components like buttons and progress bars use a `0.5rem` (8px) radius. Success indicators and "Packed" checkboxes use a full pill-shape (circular) to distinguish them from the structural containers of the layout.

## Components

### Bento Cards
The core container. Must have a white background, 24px corner radius, and the standard soft shadow. Cards should contain a single functional group (e.g., "Weather Outlook" or "Packing Progress").

### Primary Buttons
Filled with Sage Green with Off-White text. They utilize a 0.5rem radius and 16px vertical padding. The hover state involves a slight darken of the Sage Green.

### Weight Alerts
Small, discrete chips within bento cells. If a suitcase is near weight limits, use a subtle Amber background with Slate text. If over limit, use a pale Red background with dark Red text. Avoid aggressive icons; use "Weight Critical" text in JetBrains Mono.

### Packing Chips
Used for item categories. These are "Ghost" style with a 1px Sage Green border when active, or a light Slate-variant border when empty.

### Success States
When a module is "100% Packed," the card's header or background should transition to a very faint tint of Sage Green (5% opacity) to provide a satisfying visual "done" state without breaking the minimalist aesthetic.