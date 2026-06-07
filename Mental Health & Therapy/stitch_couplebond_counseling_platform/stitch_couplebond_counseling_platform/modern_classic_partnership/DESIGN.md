---
name: Modern Classic Partnership
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#584141'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#8c7071'
  outline-variant: '#e0bfbf'
  surface-tint: '#af2b3e'
  primary: '#570013'
  on-primary: '#ffffff'
  primary-container: '#800020'
  on-primary-container: '#ff828a'
  inverse-primary: '#ffb3b5'
  secondary: '#5e5e5d'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdd'
  on-secondary-container: '#626361'
  tertiary: '#262727'
  on-tertiary: '#ffffff'
  tertiary-container: '#3c3d3d'
  on-tertiary-container: '#a8a8a7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdada'
  primary-fixed-dim: '#ffb3b5'
  on-primary-fixed: '#40000b'
  on-primary-fixed-variant: '#8e0f28'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e3e2e1'
  tertiary-fixed-dim: '#c7c6c5'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464746'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
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
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  split-gap: 0px
---

## Brand & Style

The brand personality is rooted in the intersection of emotional depth and clinical stability. It evokes a sense of maturity, empathy, and structured healing. The target audience consists of couples seeking a sophisticated, safe space to navigate complex relational dynamics.

This design system employs a **Minimalist** style with **High-Contrast** focal points. It leverages expansive whitespace to provide mental breathing room, while using bold color blocks to signify the union of two distinct perspectives. The visual language avoids trendy "app-like" fluff in favor of a timeless, editorial aesthetic that feels more like a premium publication than a utility tool.

## Colors

The palette is anchored by Deep Burgundy, used intentionally to represent the heart of the relationship—passion, commitment, and the gravity of the work being done. This is balanced by Warm Grey, which serves as the "neutral ground," providing a calming, stable backdrop that prevents the interface from feeling over-stimulating.

- **Primary (Burgundy):** Reserved for high-priority actions, headings, and the "individual" side of the split-screen layout.
- **Secondary (Warm Grey):** Used for large surface areas, secondary containers, and the "partner" side of the split-screen.
- **Tertiary (Cream/Off-white):** Used for global backgrounds to soften the contrast between the grey and pure white.
- **Neutral (Charcoal):** Applied to body text and icons to ensure WCAG-compliant legibility.

## Typography

This design system uses a high-contrast typographic pairing to reinforce its "Modern Classic" roots. 

**Noto Serif** is utilized for all headings. Its timeless proportions and elegant serifs communicate authority and tradition. For headlines, use tighter tracking to create a sophisticated, editorial feel.

**Inter** is the functional workhorse for all body copy, inputs, and UI labels. It provides a clean, neutral counterpoint to the serif headings, ensuring that long-form counseling content or chat interfaces remain highly readable and accessible. All labels should use Inter in semi-bold with increased letter spacing for a refined, organized appearance.

## Layout & Spacing

The layout is governed by a **Split-Screen** philosophy. On desktop, the screen is divided into two primary vertical columns (50/50). This represents the two individuals in the relationship. Information relevant to one partner or one "side" of an argument occupies one half, while the other half remains neutral or reflects the partner's data.

**Grid & Rhythm:**
- **Desktop:** 12-column grid, but often treated as two 6-column blocks.
- **Mobile Stacking:** On mobile devices, the left column stacks on top of the right column. 
- **The "Seam":** Use the Deep Burgundy and Warm Grey to color-block these halves. The "seam" where they meet should be sharp and clean, symbolizing clarity and directness.
- **Padding:** Use generous `xl` padding for page headers to maintain the minimalist, airy feel.

## Elevation & Depth

This design system avoids heavy shadows to maintain its classic, flat-pressed aesthetic. Instead, depth is communicated through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Tiers:** Use subtle shifts between the Tertiary cream background and the Secondary warm grey to denote hierarchy.
- **Borders:** Instead of shadows, use 1px solid borders in a slightly darker shade of the background color (e.g., a 10% darken of the Warm Grey) to define card boundaries.
- **Focus States:** When an element requires focus, use a sharp 2px Burgundy border rather than a glow or shadow. This maintains the "Classic" crispness.

## Shapes

To balance the "Modern" and "Classic" aspects, this design system uses **Soft** roundedness. Sharp corners (0px) feel too aggressive for a therapy app, while highly rounded corners (Pill-shaped) feel too casual.

- **Primary Elements:** Buttons and input fields use a consistent `0.25rem` radius. 
- **Containers:** Large cards or split-screen containers use `0.5rem` to feel substantial yet approachable. 
- **Iconography:** Use medium-weight, geometric line icons with slightly rounded caps to match the typography's weight.

## Components

### Buttons
The primary Call-to-Action (CTA) for consultation booking is the centerpiece of the mobile experience.
- **Primary CTA:** Deep Burgundy background with White text. Centered, full-width on mobile. High contrast is mandatory.
- **Secondary CTA:** Warm Grey background with Burgundy text or a transparent background with a 1px Burgundy border.

### The Split-Card
A unique component for this design system. A card that is visually bisected. The left 20% might be Burgundy (representing "My Progress") and the right 80% is Warm Grey (representing "Shared Tasks"). 

### Inputs & Forms
Forms should be minimalist. Use "Floating Labels" in Inter. The bottom border of an input field should be a 1px solid line that thickens to 2px Burgundy upon focus. Avoid boxed input fields to keep the interface feeling open.

### Navigation
A centered bottom-bar on mobile using a "Warm Grey" frosted blur (Glassmorphism Lite) to ensure it sits elegantly over the split-screen content without obscuring the color blocks.

### Consultation Booking
The booking flow should be a centered modal that overrides the split-screen, signifying that the "two halves" are now entering a singular, unified space for healing.