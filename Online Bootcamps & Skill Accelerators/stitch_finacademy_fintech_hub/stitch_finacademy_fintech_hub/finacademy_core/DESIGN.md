---
name: FinAcademy Core
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c5c6d2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e909c'
  outline-variant: '#444650'
  surface-tint: '#b3c5ff'
  primary: '#b3c5ff'
  on-primary: '#0d2c6e'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#435b9f'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#4cd6ff'
  on-tertiary: '#003543'
  tertiary-container: '#002d39'
  on-tertiary-container: '#009cc0'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#b7eaff'
  tertiary-fixed-dim: '#4cd6ff'
  on-tertiary-fixed: '#001f28'
  on-tertiary-fixed-variant: '#004e60'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
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
  code-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
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
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

The design system is engineered to evoke a sense of institutional authority and cutting-edge technological prowess. It targets high-aspiring professionals transitioning into fintech and blockchain, requiring a UI that feels as secure as a banking terminal but as innovative as a decentralized protocol.

The aesthetic direction is **Glassmorphism**, applied with surgical precision. Rather than a whimsical or "candy" look, this design system uses frosted layers to create architectural depth against a deep, matte void. The style relies on high-contrast accents and mathematical precision to maintain a professional, high-end atmosphere suitable for complex financial data.

## Colors

This design system utilizes a deep-dark color mode to emphasize the "Matte Black" background, providing a canvas where information glows with clarity.

- **Primary (Royal Blue):** Used for primary actions, progress indicators, and brand identification. It represents stability and institutional trust.
- **Secondary (Silver):** Applied to borders, secondary icons, and structural dividers. It provides a premium, metallic edge to the interface.
- **Tertiary (Electric Blue/Cyan):** A high-visibility accent specifically reserved for blockchain status indicators and data visualization highlights.
- **Neutral (Matte Black):** The foundation of the UI, creating a high-contrast environment that reduces eye strain during long coding or trading sessions.

## Typography

Typography focuses on systematic legibility. **Inter** serves as the primary typeface for its exceptional readability in data-heavy environments. To lean into the blockchain aesthetic, **Space Grotesk** is introduced for labels, data points, and code snippets, adding a technical, futuristic edge.

Headers should be tightly kerned and bold to command attention, while body text maintains generous line height for educational content. Numerical data should always utilize tabular figures where possible to ensure columns of figures align perfectly in financial tables.

## Layout & Spacing

The design system employs a **12-column fixed grid** for desktop environments to maintain a sense of structured, high-end editorial layout. On smaller screens, the layout transitions to a fluid model with increased side margins to ensure the "Glass" modules have room to breathe against the matte background.

Spacing is strictly based on an 8px linear scale. Large components and "modules" are separated by 48px or 64px to prevent visual clutter, reflecting the "minimalist" aspect of sophisticated fintech interfaces.

## Elevation & Depth

In this design system, depth is achieved through **Glassmorphism** and layering rather than traditional drop shadows.

- **The Void:** The base layer is #0B0B0B (Matte Black).
- **Glass Layers:** All containers use a `backdrop-filter: blur(20px)` with a very subtle semi-transparent white or silver fill (`rgba(255, 255, 255, 0.03)`).
- **The Silver Edge:** Every glass module must have a 1px solid border using the Silver token at low opacity. This defines the object's boundaries in the dark space.
- **Inner Glow:** Active elements may feature a subtle inner shadow or "rim light" to simulate a physical glass edge catching a light source from above.

## Shapes

The shape language is "Soft-Technical." Sharp corners feel too aggressive, while fully rounded corners feel too consumer-grade. A subtle **0.25rem (4px)** base radius is used for small elements (inputs, buttons), while large glass modules use **0.75rem (12px)**.

This controlled roundedness maintains a professional, "engineered" look while ensuring the interface feels modern and premium.

## Components

- **Glass Cards:** The signature component. Features a 1px silver border, 20px backdrop-blur, and 32px internal padding.
- **Action Buttons:** Primary buttons are solid Royal Blue with white text. Secondary buttons use a "ghost" style with a silver border and silver text.
- **Data Visualizations:** Charts use high-contrast strokes. Primary trends are Royal Blue, while secondary metrics use Silver. Grid lines in charts should be barely visible (3% opacity silver).
- **Input Fields:** Darker than the background (#000000) with a 1px silver border that glows Royal Blue on focus.
- **Status Chips:** Small, pill-shaped markers for "Live," "Pending," or "Confirmed" (blockchain states). These use a high-saturation version of the tertiary color with a subtle outer glow.
- **Terminal Snippets:** Dark blocks for blockchain code execution, featuring monospaced text and syntax highlighting that adheres to the primary blue and silver palette.