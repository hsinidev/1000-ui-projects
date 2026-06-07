---
name: Executive Precision
colors:
  surface: '#f9f9fc'
  surface-dim: '#d9dadd'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#edeef1'
  surface-container-high: '#e8e8eb'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#43474e'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#476083'
  primary: '#000613'
  on-primary: '#ffffff'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#afc8f0'
  secondary: '#5d5e63'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfe4'
  on-secondary-container: '#626267'
  tertiary: '#040606'
  on-tertiary: '#ffffff'
  tertiary-container: '#1d1f1f'
  on-tertiary-container: '#858687'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  display:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '600'
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
    fontFamily: metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-point:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built for the intersection of high-end tailoring and wearable technology. The brand personality is authoritative, precise, and sophisticated, catering to an executive audience that values both utility and aesthetic discipline. 

The visual style is **Architectural Minimalism**. It utilizes a strict structural grid to evoke a sense of engineered luxury. By combining high-contrast elements with expansive whitespace, the interface mirrors the clarity of a premium watch face and the sharp lines of a bespoke suit. The aesthetic avoids unnecessary ornamentation, favoring "less but better" to ensure that smart features feel like an extension of the garment rather than a digital intrusion.

## Colors

The palette is rooted in a traditional executive spectrum. **Navy Blue (#001F3F)** serves as the primary anchor, used for core branding, primary actions, and deep structural elements to convey trust and permanence. **Brushed Steel (#8E8E93)** provides a technical counterpoint, used for borders, inactive states, and iconography to mimic the hardware of a smartwatch. 

**White (#FFFFFF)** is the primary canvas, ensuring a high-contrast environment that promotes legibility and a "gallery" feel. For subtle depth, a secondary neutral off-white is used for background surfacing to prevent eye strain without sacrificing the pristine aesthetic.

## Typography

The typography strategy relies on a rigid hierarchy to guide the user through complex NFC and biometric data. **Metropolis** is selected for headlines and labels due to its geometric, architectural proportions that align with the "sleek" brand requirement. Large display sizes use tighter letter spacing to feel impactful and modern.

**Inter** is utilized for body text and technical data points, ensuring maximum legibility at smaller scales. A specialized "Label-Caps" style is used for technical metadata and category headers, employing increased letter spacing to create an airy, premium feel reminiscent of luxury watch branding.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop and tablet views to maintain a sense of controlled, intentional composition. The layout is built on a 12-column grid with generous gutters to allow the content to breathe.

The spacing rhythm follows an 8px base unit. Vertical rhythm is strictly enforced to maintain the "architectural" feel, with large gaps between major sections to emphasize the premium nature of the content. Alignment should always be crisp; elements should feel "locked" into the grid, avoiding centered layouts in favor of strong left-aligned or justified structures that imply technical precision.

## Elevation & Depth

To maintain a minimal and high-contrast profile, this design system rejects heavy shadows and traditional skeuomorphism. Instead, depth is achieved through **Low-contrast Outlines** and **Tonal Layering**.

- **Surface Tiers:** Primary content sits on pure white. Secondary management panels use a very light grey tint to create a subtle recessed effect.
- **Borders as Depth:** Elements are defined by 1px "Brushed Steel" strokes rather than dropshadows. This mimics the physical edges of metal hardware.
- **NFC Visuals:** When an NFC element is "active," it uses a slight inner-glow or a bold Navy Blue stroke to indicate state, rather than lifting off the page. The goal is a flat, engineered aesthetic that feels integrated into the fabric of the UI.

## Shapes

The shape language is disciplined and geometric. A **Soft (0.25rem)** roundedness is applied to standard UI elements like buttons and input fields. This subtle rounding prevents the interface from feeling "sharp" or hostile, while remaining much more professional than a fully rounded "pill" style.

For larger card layouts or NFC management modules, a slightly more pronounced radius may be used (up to 0.5rem) to differentiate them as interactive containers. Line-work remains strictly 1px or 2px in weight—never variable—to maintain the architectural integrity of the system.

## Components

### Buttons
Primary buttons are solid Navy Blue with White typography, featuring a 1px steel-colored hover stroke. Secondary buttons are "Ghost" style—transparent backgrounds with a 1px Brushed Steel border and Navy text. All buttons use the `label-caps` typographic style for a high-end feel.

### NFC Management Cards
Cards are the core of the experience. They feature a 1px Brushed Steel border, no shadow, and a high-contrast Navy Blue header. Inside, precise line-work separates "Status," "Signal Strength," and "Link Configuration" data points.

### Input Fields & Controls
Inputs are minimal, defined by a bottom-only border in Brushed Steel that turns Navy Blue on focus. Labels sit strictly above the line in the `label-caps` style.

### Precise Line-work (Dividers)
Dividers are not just separators but design features. Use 1px Brushed Steel lines to create "cells" of information, similar to a technical blueprint or a sophisticated dashboard.

### Status Indicators
Small, high-contrast dots are used for status (e.g., Connected/Disconnected). They should never use glowing effects, only solid, flat colors to maintain the "executive" tone.