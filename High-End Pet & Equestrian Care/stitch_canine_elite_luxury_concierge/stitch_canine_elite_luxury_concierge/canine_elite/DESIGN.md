---
name: Canine-Elite
colors:
  surface: '#f7f9ff'
  surface-dim: '#d5dae2'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4fc'
  surface-container: '#e9eef6'
  surface-container-high: '#e3e9f0'
  surface-container-highest: '#dde3eb'
  on-surface: '#161c22'
  on-surface-variant: '#4b463d'
  inverse-surface: '#2b3137'
  inverse-on-surface: '#ecf1f9'
  outline: '#7d766c'
  outline-variant: '#cec5ba'
  surface-tint: '#685d4a'
  primary: '#685d4a'
  on-primary: '#ffffff'
  primary-container: '#f7e7ce'
  on-primary-container: '#726753'
  inverse-primary: '#d3c5ad'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5c5f60'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e9ea'
  on-tertiary-container: '#66696a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0e0c8'
  primary-fixed-dim: '#d3c5ad'
  on-primary-fixed: '#221b0b'
  on-primary-fixed-variant: '#4f4533'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f7f9ff'
  on-background: '#161c22'
  surface-variant: '#dde3eb'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
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
  margin-mobile: 24px
  gutter: 16px
  stack-sm: 12px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system targets an affluent demographic that views pet care as a bespoke lifestyle choice rather than a chore. The brand personality is poised, attentive, and whisper-quiet—avoiding the loud, colorful tropes of the pet industry in favor of a hospitality-first aesthetic.

The visual style is a refined hybrid of **Minimalism** and **Neumorphism**. It utilizes a "Soft-UI" approach to create a tactile, premium feel where interface elements appear to be molded from a single, continuous surface. By prioritizing generous whitespace and subtle depth, the UI evokes an emotional response of tranquility, cleanliness, and uncompromising quality.

## Colors

The palette is restricted to three core tones to maintain a high-fashion editorial feel. **Soft Champagne** serves as the primary accent, used sparingly for call-to-actions and premium highlights. **Slate** provides the structural grounding, used for text and iconography to ensure legibility without the harshness of true black. **Silk White** acts as the foundation, providing a clean, expansive canvas.

A "Deep Slate" (#2F353B) is reserved for high-contrast typography and critical interactive states. All background surfaces should utilize the Silk White base to allow the neumorphic shadows to bloom effectively.

## Typography

The typography strategy pairs a timeless serif with a technical, modern sans-serif. **Noto Serif** is used for headlines to convey heritage and authority. **Manrope** is utilized for all functional and body text, chosen for its balanced proportions and excellent readability on mobile displays.

To reinforce the luxury positioning, labels and small metadata should be set in uppercase Manrope with increased letter spacing. Headlines should maintain a tight tracking to feel cohesive and editorial.

## Layout & Spacing

This design system employs a **Fluid Grid** model optimized for mobile-first luxury. The standard margin is 24px, providing more "breathing room" than traditional apps to emphasize exclusivity. 

A strict 8px baseline grid governs all vertical rhythms. Spacing between major content sections (stack-lg) is intentionally wide to prevent the interface from feeling cluttered. Content blocks should be centered with ample padding within containers to maintain the "airy" luxury feel.

## Elevation & Depth

Hierarchy is achieved through **Soft-UI Neumorphism**. Instead of traditional drop shadows, elements use dual-source lighting:
1. **Highlight:** A white (#FFFFFF) shadow positioned at -4px, -4px with an 8px blur.
2. **Shadow:** A soft Slate-tinted shadow (#D1D9E6) at 4px, 4px with an 8px blur.

This creates the illusion that buttons and cards are physically extruded from the Silk White background. Deeply nested information uses "sunken" or "inset" shadows to signify input fields or containment. High-priority modal overlays utilize a subtle backdrop blur (10px) to maintain context while focusing the user's attention.

## Shapes

The shape language is sophisticated and organic. A consistent `16px` (rounded-lg) radius is the standard for cards and main UI containers, creating a "pebble-like" softness that feels safe and premium. 

Interactive elements like buttons and chips use a more pronounced `rounded-xl` or pill-shape to invite touch. Avoid sharp corners entirely, as they conflict with the "Soft-UI" narrative.

## Components

### Buttons
Primary buttons use the Soft Champagne fill with an extruded neumorphic effect. Labels are centered in Slate Bold, Uppercase. Secondary buttons are "Ghost" style with a fine 1px Slate border and no fill.

### Cards
Cards are the primary content vehicle. They must have the dual-shadow neumorphic treatment and a minimum internal padding of 24px. No borders should be used on cards; depth alone defines the boundary.

### Input Fields
Fields appear "recessed" into the UI using inset shadows. This provides a clear affordance for data entry without breaking the surface-continuity aesthetic.

### Progress & Health Indicators
For health tracking, use thin, elegant ring charts in Champagne and Slate. Avoid heavy blocks of color; prefer line-art iconography with a 1.5pt stroke weight.

### Concierge Float
A persistent, pill-shaped "Concierge" button should be anchored to the bottom-right, using a slightly more intense elevation to signify its 24/7 availability.