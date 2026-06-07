---
name: Soma-Twin
colors:
  surface: '#0d112a'
  surface-dim: '#0d112a'
  surface-bright: '#343752'
  surface-container-lowest: '#080c25'
  surface-container-low: '#161a33'
  surface-container: '#1a1e37'
  surface-container-high: '#242842'
  surface-container-highest: '#2f334e'
  on-surface: '#dee0ff'
  on-surface-variant: '#bbc9cf'
  inverse-surface: '#dee0ff'
  inverse-on-surface: '#2b2f49'
  outline: '#859399'
  outline-variant: '#3c494e'
  surface-tint: '#4cd6ff'
  primary: '#a4e6ff'
  on-primary: '#003543'
  primary-container: '#00d1ff'
  on-primary-container: '#00566a'
  inverse-primary: '#00677f'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#d5dde4'
  on-tertiary: '#293137'
  tertiary-container: '#b9c1c8'
  on-tertiary-container: '#474f55'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b7eaff'
  primary-fixed-dim: '#4cd6ff'
  on-primary-fixed: '#001f28'
  on-primary-fixed-variant: '#004e60'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#dbe4ea'
  tertiary-fixed-dim: '#bfc8ce'
  on-tertiary-fixed: '#151d22'
  on-tertiary-fixed-variant: '#40484d'
  background: '#0d112a'
  on-background: '#dee0ff'
  surface-variant: '#2f334e'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono-lg:
    fontFamily: Space Mono
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  data-mono-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 20px
  margin: 32px
---

## Brand & Style
The design system is engineered to evoke a sense of absolute clinical authority and hyper-advanced medical precision. It targets a high-net-worth demographic seeking life-extension technologies, requiring an interface that feels more like a diagnostic terminal than a consumer app. 

The aesthetic merges **Minimalism** with **Glassmorphism**. It utilizes a "Dark Lab" philosophy: deep, immersive backgrounds that simulate a light-controlled clinical environment, punctuated by self-illuminating data points. Every element must feel intentional, sterile, and high-stakes, suggesting that the software is a direct interface with the user's biological data.

## Colors
The palette is anchored in **Deep Indigo (#0A0E27)**, providing a void-like depth that allows technical elements to recede or advance through luminance rather than hue. **Silver (#C0C0C0)** serves as the primary structural color, used for borders and secondary text to mimic brushed metal or technical instrument casings.

**Frost White (#F0F8FF)** is reserved for high-level headings and primary navigation, ensuring maximum legibility against the dark void. The **Medical-grade blue glow (#00D1FF)** is the functional heartbeat of the design system; it is used exclusively for active data streams, critical findings, and interactive states. A high-contrast red is permitted only for "Biological Risk" or system-critical alerts.

## Typography
This design system utilizes a dual-font strategy to balance human readability with technical authenticity. 

**Inter** provides the structural foundation. Headings use tighter letter spacing and heavier weights to command authority. Body text is set with generous line heights for clinical clarity.

**Space Mono** is used strictly for telemetry, timestamps, and biological data values. This distinction ensures that the user can immediately differentiate between "instructional content" and "raw data." All mono-spaced labels should be set in uppercase to reinforce the sterile, machine-output aesthetic.

## Layout & Spacing
The layout follows a **Fixed 12-Column Grid** for desktop views, emphasizing structural rigidity. Gutters are kept narrow (20px) to maximize the "instrument panel" density. 

A strict 4px/8px baseline rhythm is enforced. Spacing should be used to create clear groupings of data; related clinical metrics should be tightly packed with `xs` or `sm` spacing, while distinct diagnostic modules are separated by `lg` or `xl` gaps. Padding within components should be symmetrical to maintain the "sterile" balance required by the brand.

## Elevation & Depth
Depth is not conveyed through traditional shadows, but through **Tonal Layering** and **Glassmorphism**. 

1.  **Background:** The base layer is the solid Deep Indigo.
2.  **Modules:** Diagnostic cards use a subtle backdrop blur (12px - 20px) and a semi-transparent Indigo fill (opacity 40-60%).
3.  **Borders:** Precision is defined by 1px solid Silver (#C0C0C0) borders.
4.  **Illumination:** High-priority elements use "Medical Glow"—a 0px blur, 1px spread outer glow in #00D1FF at low opacity, or a sharp inner glow to suggest an illuminated glass panel. 

The goal is to make the UI feel like a series of glass overlays on a light-sensitive medical monitor.

## Shapes
To maintain a technical and "medical instrument" feel, the design system utilizes **Soft (0.25rem)** roundedness for standard UI elements. 

Complete sharpness (0px) is reserved for data charts and vertical separators to maintain a "cutting-edge" feel. The 0.25rem radius on cards and buttons is just enough to prevent the UI from feeling aggressive while remaining significantly sharper than standard consumer interfaces. Pills and circular buttons are prohibited; all interactive zones must be rectangular or subtly rounded.

## Components
### Buttons
Primary buttons use a ghost-style Silver border with Frost White text. The "Active" state triggers the #00D1FF blue glow and a subtle increase in border thickness.

### Input Fields
Inputs are bottom-border only or fully enclosed in a 1px Silver frame. Backgrounds must be 10% Frost White to create a "recessed" glass look. The cursor and focus state must use the Medical Blue glow.

### Critical Findings Alerts
These are high-contrast modules. Unlike standard glass cards, these use a solid Silver background with Deep Indigo text to force immediate visual attention, or a pulsing #00D1FF border for live critical data updates.

### Data Chips
Small, rectangular tags using Space Mono. They should look like physical labels found on lab samples. No background fill; only 1px Silver borders.

### Diagnostic Cards
The core container. Features a subtle glass blur, a header area separated by a 1px Silver line, and "corner-bracket" accents to reinforce the high-precision framing.