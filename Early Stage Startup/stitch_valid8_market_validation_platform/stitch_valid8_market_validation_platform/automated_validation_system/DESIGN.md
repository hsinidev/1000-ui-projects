---
name: Automated Validation System
colors:
  surface: '#0c1322'
  surface-dim: '#0c1322'
  surface-bright: '#323949'
  surface-container-lowest: '#070e1d'
  surface-container-low: '#141b2b'
  surface-container: '#191f2f'
  surface-container-high: '#232a3a'
  surface-container-highest: '#2e3545'
  on-surface: '#dce2f7'
  on-surface-variant: '#ccc3d8'
  inverse-surface: '#dce2f7'
  inverse-on-surface: '#293040'
  outline: '#958da1'
  outline-variant: '#4a4455'
  surface-tint: '#d2bbff'
  primary: '#d2bbff'
  on-primary: '#3f008e'
  primary-container: '#7c3aed'
  on-primary-container: '#ede0ff'
  inverse-primary: '#732ee4'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#656768'
  on-tertiary-container: '#e5e6e7'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#eaddff'
  primary-fixed-dim: '#d2bbff'
  on-primary-fixed: '#25005a'
  on-primary-fixed-variant: '#5a00c6'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#0c1322'
  on-background: '#dce2f7'
  surface-variant: '#2e3545'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin: 32px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is built for the high-velocity world of market validation. It embodies a **Modern-Startup** aesthetic that is unapologetically tech-forward and high-energy. The visual language is designed to instill confidence in founders and product teams through precision, speed, and clarity.

The style leverages a **High-Contrast / Bold** foundation combined with **Glassmorphism** to create depth within a **Bento-Box** layout structure. This approach organizes complex data sets into digestible, modular units, reflecting the systematic nature of A/B testing and market research. The interface feels reactive, premium, and authoritative.

## Colors

The palette is anchored by **Matte Black (#111827)**, providing a deep, sophisticated canvas that allows high-energy accents to pop. **Vibrant Purple (#7C3AED)** serves as the primary brand driver, used for key actions and brand presence. **Mint (#10B981)** is utilized specifically for success states, positive validation metrics, and "Go" signals.

This design system uses a dark-mode-first approach to reduce eye strain during deep data analysis. High-contrast white and off-white are used for text and iconography to ensure maximum legibility against the dark backgrounds.

## Typography

This design system employs a dual-font strategy. **Space Grotesk** is used for headlines and display text; its geometric and technical character reinforces the platform's innovative and futuristic positioning. **Inter** is used for all body copy, data points, and UI labels due to its exceptional legibility and systematic, neutral feel.

Headlines should utilize tight letter-spacing to maintain a "high-energy" and compact look. Labels and captions should use all-caps for a structural, institutional feel when displaying metadata or secondary information.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with a heavy emphasis on **Bento-Box** modules. Content is grouped into distinct, logical containers with consistent padding to create a sense of organized complexity. 

A 12-column grid is used for desktop layouts, while the spacing rhythm is strictly based on an 8px scale. Components within bento boxes should use generous internal padding (24px or 32px) to ensure that even data-heavy screens feel breathable and premium.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Tonal Layers** rather than traditional shadows. 

1. **Surface Base:** Matte Black (#111827).
2. **Surface Container:** A slightly lighter charcoal (#1F2937) with a subtle 1px border.
3. **Glass Overlay:** For modals and floating elements, a semi-transparent surface (10% opacity white) with a 20px backdrop blur and a thin, vibrant purple or white inner stroke.

Shadows, if used, are extremely subtle and "ambient"—using high blur and low opacity (5-10%) to suggest a slight lift without breaking the clean, flat-tech aesthetic.

## Shapes

The shape language is **Rounded**, striking a balance between the friendliness of a startup and the precision of a technical tool. Standard UI components like buttons and input fields utilize a 0.5rem (8px) radius. Larger bento-box containers use `rounded-xl` (1.5rem / 24px) to clearly define major sections of the interface. This contrast in corner radii helps users distinguish between interactive elements and structural containers.

## Components

### Buttons
Buttons are high-contrast and high-energy. The **Primary Action** is a solid Vibrant Purple with white text. **Success Actions** use Mint. Secondary buttons should use a ghost style (transparent background with a 1px border) or a subtle dark grey background.

### Bento Cards
These are the core of the design system. Every bento card must have a subtle border (#374151) and a consistent internal padding of 24px. They may optionally include a "Glass" header for title bars within the module.

### Inputs & Fields
Input fields are dark-filled with a subtle border. On focus, the border transitions to Vibrant Purple with a subtle outer glow (0px 0px 8px).

### Data Visualization
Charts and graphs should use Mint for "Validated/Positive" results and Purple for "Testing/Active" variables. Background grids in charts must be low-contrast (Matte Black + 5% white).

### Chips & Badges
Small, high-contrast pills used for status indicators. Use "Mint" with 10% opacity background and 100% opacity text for "Validated" states.