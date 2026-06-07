---
name: Nautical Modernity
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0edec'
  surface-container-high: '#ebe7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#3f4945'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#707975'
  outline-variant: '#bfc9c4'
  surface-tint: '#29695b'
  primary: '#00342b'
  on-primary: '#ffffff'
  primary-container: '#004d40'
  on-primary-container: '#7ebdac'
  inverse-primary: '#94d3c1'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#2c2e2e'
  on-tertiary: '#ffffff'
  tertiary-container: '#424444'
  on-tertiary-container: '#b0b1b1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#afefdd'
  primary-fixed-dim: '#94d3c1'
  on-primary-fixed: '#00201a'
  on-primary-fixed-variant: '#065043'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  margin-mobile: 24px
  margin-desktop: 80px
  gutter: 16px
  section-gap: 120px
---

## Brand & Style

This design system is built upon the principles of **Minimalism** and **High-Contrast Editorial** design. It evokes the prestige of the open sea and the architectural precision of custom yacht builds. The brand personality is authoritative yet serene, targeting an elite demographic that values discretion and uncompromising quality.

The visual language emphasizes "quiet luxury"—avoiding unnecessary ornamentation in favor of structural integrity, expansive whitespace (wide margins), and a sophisticated interplay between deep oceanic tones and metallic accents. The user experience is designed to feel like a private concierge service: effortless, spacious, and meticulously organized.

## Colors

The palette is anchored by **Deep Teal**, representing the depth of the ocean and providing a stable, professional foundation. **Silver** is used as a secondary accent for thin borders, dividers, and interactive states, mimicking the polished chrome and stainless steel found on a yacht’s deck.

**Crisp White** serves as the primary canvas, ensuring a high-contrast environment that allows high-resolution photography of vessels to take center stage. Text is set in a near-black neutral to maintain legibility while avoiding the harshness of pure black against white surfaces. Use color sparingly to guide the eye toward "Call to Action" elements or critical status indicators.

## Typography

The typography strategy pairs the timeless elegance of **Noto Serif** with the functional precision of **Manrope**. 

- **Headlines** utilize Noto Serif to convey heritage and exclusivity. They should be given significant vertical breathing room.
- **Body text** utilizes Manrope for its high readability on mobile screens and its balanced, professional character.
- **Labels and metadata** use Manrope in uppercase with increased letter spacing to create an "instrument panel" aesthetic, reminiscent of nautical navigation tools.

## Layout & Spacing

This design system adopts a **mobile-first, fixed-margin** approach. Layouts are governed by a strict 8px rhythmic grid, but the defining characteristic is the "Wide Margin" philosophy. 

On mobile devices, a generous 24px side margin prevents the UI from feeling cramped. On desktop, this expands to 80px or more to create an editorial, gallery-like feel. Section gaps are intentionally large to facilitate a slow, deliberate scrolling pace, allowing the user to digest high-end imagery without visual fatigue. Components should prioritize vertical stacking on mobile, transitioning to a refined 12-column grid on larger viewports.

## Elevation & Depth

To maintain a sophisticated and modern nautical aesthetic, this design system avoids heavy drop shadows. Depth is instead communicated through **Low-Contrast Outlines** and **Tonal Layering**.

- **Level 0 (Floor):** Pure Crisp White.
- **Level 1 (Cards/Containers):** Defined by a 1px Silver (#C0C0C0) border. No shadow.
- **Level 2 (Modals/Overlays):** A subtle, ultra-diffused shadow (10% opacity Deep Teal) may be used to indicate a temporary state, combined with a backdrop blur to simulate frosted glass or sea mist.
- **Dividers:** Hairline Silver strokes (0.5pt where possible) are used to separate content sections cleanly.

## Shapes

The shape language of the design system is **Sharp (0)**. 

Sharp corners communicate architectural precision, luxury, and a "bespoke" quality. This rigidity mimics the clean lines of a modern yacht hull and interior cabinetry. Buttons, input fields, and image containers must maintain 90-degree angles. Any deviation from this (such as circular avatars) should be used only for functional differentiation and kept to a minimum to maintain the brand’s disciplined aesthetic.

## Components

### Buttons
Primary buttons use a solid Deep Teal fill with Crisp White text. Secondary buttons are defined by a 1px Silver border and Deep Teal text. All buttons are rectangular with zero corner radius. Hover states should involve a subtle shift to a slightly lighter teal or a silver tint.

### Inputs & Forms
Input fields are characterized by a single bottom border (1px Silver) rather than a full box, creating a cleaner, more "signed-document" feel. Labels sit above the line in Manrope uppercase.

### Cards
Cards do not use shadows. They are defined by high-quality, full-bleed imagery at the top, followed by a Silver hairline divider and a generous padding area for Noto Serif titles. 

### Thin-Line Icons
Icons must be 1px stroke weight, vector-based, and monochromatic (Deep Teal or Silver). They should be geometric and avoid playful or rounded terminals.

### Featured Vessel List
A specialized component for yachts, featuring a large image, a prominent "Spec Table" using the Label-Caps typography, and a "Request Charter" CTA that remains anchored or highly visible.