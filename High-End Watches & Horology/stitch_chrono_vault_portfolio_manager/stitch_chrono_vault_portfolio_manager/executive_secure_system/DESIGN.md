---
name: Executive Secure System
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c5c7c8'
  on-tertiary: '#2e3132'
  tertiary-container: '#16191a'
  on-tertiary-container: '#808283'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display:
    fontFamily: metropolis
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  h1:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  h2:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.01em
  h3:
    fontFamily: metropolis
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  mono-data:
    fontFamily: jetbrainsMono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding-mobile: 20px
  container-padding-desktop: 40px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is built upon the pillars of **Precision, Authority, and Discretion**. It is engineered for a high-stakes executive environment where security is not just a feature, but an aesthetic. The visual language conveys a "digital vault" experience—weighty, impenetrable, yet technologically advanced.

We utilize a **refined Glassmorphism** style to imply depth and transparency without compromising the feeling of structural integrity. This is balanced with high-mechanical interactive details, such as hairline borders and micro-interactions that mimic the tactile feedback of high-end horology or aerospace instrumentation. The focus is mobile-first, ensuring that executive-level control is accessible and legible on the move.

## Colors

The palette is anchored in **Midnight Blue (#0A192F)**, providing a deep, stable foundation that evokes trust and security. This is a dark-mode first system. **Silver (#C0C0C0)** is used for structural elements, iconography, and secondary text, lending a metallic, industrial quality to the UI. **Silk White (#F8F9FA)** is reserved for primary typography and high-priority actions to ensure maximum legibility against the dark void.

A subtle cyan-tinted accent is permitted for success states and active indicators, but the primary focus remains monochromatic and tonal to maintain an executive composure.

## Typography

This design system employs **Metropolis** for headings to project a geometric, structured, and modern authority. Its clean lines are reminiscent of architectural drafting, fitting the "vault" theme. **Inter** is used for all body and functional text due to its exceptional legibility on mobile screens and neutral, systematic tone.

Data points, security codes, and timestamps should utilize **JetBrains Mono** to reinforce the technical and precise nature of the platform. Strict adherence to the `label-caps` style for section headers and metadata is required to maintain a professional, organized hierarchy.

## Layout & Spacing

The layout philosophy follows a **precise 4px baseline grid**. For mobile devices, a fluid 4-column grid is used with generous 20px side margins to ensure the interface doesn't feel cramped. On larger screens, the system transitions to a 12-column fixed-width grid to maintain the "executive dashboard" aesthetic.

Spacing is used to create "breathing room" between secure modules. Large vertical stacks (`stack-lg`) are used to separate distinct functional areas, while tighter spacing (`stack-sm`) is used within cards to associate data points closely.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism and Tonal Layering**. Unlike traditional systems that use heavy shadows, this system uses "Frosted Depth":

1.  **Base Layer:** Solid Midnight Blue (#0A192F).
2.  **Surface Layer:** Semi-transparent Silk White (4-8% opacity) with a 20px background blur (Backdrop Filter).
3.  **Borders:** Subtle 1px Silver outlines at 20% opacity are mandatory for all containers to define edges without adding visual weight.
4.  **Shadows:** Shadows are rarely used, but when necessary, they are highly diffused "Ambient Occlusions"—deep blue tints with 0 offset and large blur radii to simulate a soft glow rather than a physical drop.

## Shapes

The shape language is **Technical and Measured**. We avoid overly organic or round shapes, opting instead for a "Soft" corner radius (4px to 8px). This level of roundedness strikes a balance between modern software comfort and the rigid precision of machined metal parts. 

Interactive elements like buttons should maintain a 4px radius (`rounded-sm`), while larger containers and cards utilize 8px (`rounded-lg`). Fully circular "pill" shapes are reserved exclusively for status indicators and notification badges.

## Components

### Buttons
Primary buttons are solid Silver (#C0C0C0) with Midnight Blue text, featuring a subtle "brushed metal" gradient. Secondary buttons use the ghost style: a 1px Silver border with a blurred glass background. Hover/Active states should feel "mechanical"—a slight change in border luminosity and a 2px inward scale to simulate a physical press.

### Inputs
Fields are dark, recessed containers with a 1px bottom border that brightens when focused. Typography within inputs should be high-contrast Silk White. Validation icons should be sharp and minimalist.

### Glass Cards
The signature component. Every card must have `backdrop-filter: blur(20px)`, a semi-transparent background, and a 1px Silver border. Information density within cards should be high but organized, using `label-caps` for all sub-headings.

### Security Indicators
Specialized components such as "Lock Status" or "Biometric Prompt" should use high-mechanical animations—slow, deliberate rotations and iris-style expansions.

### Lists
Lists should be separated by hair-line dividers (1px Silver at 10% opacity) rather than cards to maintain a streamlined, executive flow. Every list item should have a 44px minimum hit target for mobile-first accessibility.