---
name: Event-Aegis
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cec3d3'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#978d9d'
  outline-variant: '#4c4451'
  surface-tint: '#ddb7ff'
  primary: '#ddb7ff'
  on-primary: '#4a0080'
  primary-container: '#4b0082'
  on-primary-container: '#ba7ef4'
  inverse-primary: '#7b41b3'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#313131'
  on-tertiary-container: '#9b9998'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f0dbff'
  primary-fixed-dim: '#ddb7ff'
  on-primary-fixed: '#2c0050'
  on-primary-fixed-variant: '#622599'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-base:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  panel-padding: 24px
---

## Brand & Style

The design system is engineered for high-stakes environments where precision and authority are paramount. It evokes a "Command-Center" atmosphere, positioning the user as an elite operator overseeing complex logistics. The aesthetic is a sophisticated fusion of **Glassmorphism** and **Tactile/Military-grade** elements.

The UI utilizes heavy, translucent layers to imply depth and technical complexity, while tactile buttons provide a sense of physical consequence and reliability. This design system prioritizes high-density information displays, ensuring that critical data is immediately accessible within a dark, immersive environment. The emotional response is one of total control, security, and prestige.

## Colors

The palette is anchored by **Deep Charcoal (#121212)**, providing a low-light, high-contrast canvas that reduces eye strain in dark environments. 

**Royal Purple (#4B0082)** serves as the primary brand color, used for high-impact headers and active states to signify power and exclusivity. **Metallic Gold (#D4AF37)** is reserved for critical status indicators, borders, and high-priority alerts, creating a visual hierarchy of "Urgency and Value." Neutral surfaces are layered using slightly lighter shades of charcoal (#1E1E1E) to maintain depth without sacrificing the atmospheric aesthetic.

## Typography

This design system utilizes **Montserrat** across all levels to maintain an authoritative, geometric, and technical feel. 

Headlines use heavy weights and slight tracking increases for a cinematic, bold appearance. Labels and data-heavy strings are set in uppercase with generous letter-spacing to mimic military HUDs and technical manuals. All text should maintain high contrast against the dark background, primarily using off-white or light grey to avoid harsh "vibration" while ensuring legibility.

## Layout & Spacing

The layout philosophy follows a **fixed 12-column grid** designed for widescreen command-center displays. It prioritizes information density, utilizing a tight 4px base unit to allow for complex data visualizations and multi-panel layouts.

Content is organized into "Modules" or "Pods." Sidebars are persistent for navigation, while the main staging area uses a modular masonry-style layout to accommodate varying levels of data importance. Margins are generous on the outer edges (32px) to frame the content, but internal gutters are kept tight (16px) to maintain a cohesive, high-density dashboard feel.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and subtle **Glowing Borders**. Surfaces do not use traditional shadows; instead, they use backdrop blurs (20px+) and semi-transparent fills (RGBA 18, 18, 18, 0.7) to create a sense of stacked glass panels.

- **Level 1 (Base):** Solid #121212 background.
- **Level 2 (Panels):** Translucent charcoal with a 1px border of #4B0082 at 30% opacity.
- **Level 3 (Pop-overs/Alerts):** Translucent charcoal with a 1px glowing border of #D4AF37, utilizing a 4px outer bloom (box-shadow) of the same color.
- **Active State:** Any "selected" element should emit a subtle Purple (#4B0082) inner glow to indicate focus.

## Shapes

The design system employs a **Soft (1)** roundedness approach. Buttons, cards, and input fields utilize a 4px (0.25rem) corner radius. This slight rounding prevents the UI from feeling overly aggressive or "retro-computer" sharp, while maintaining a precise, engineered aesthetic. 

Status chips and small indicator lights may use "Pill-shaped" (rounded-full) geometry to stand out as distinct interactive or status-only elements against the rectangular module structure.

## Components

### Buttons
Buttons are designed with a **Tactile, Military-Grade** feel. They feature a subtle vertical gradient (dark to light), a 1px inset top-border for a "beveled" look, and high-contrast Montserrat labels in all-caps. Active buttons emit a subtle Purple glow.

### Cards & Modules
Modules act as "Glass Panels." They must include a 1px semi-transparent border and a backdrop blur. Headers within cards should have a distinct Purple (#4B0082) background strip or underline to denote section authority.

### Input Fields
Inputs are recessed (inner shadow) with a Deep Charcoal background. On focus, the border transitions to a 1px Metallic Gold glow. All placeholders are set in uppercase "Data-Mono" style typography.

### Status Indicators
Indicators use the Metallic Gold for "Critical/Alert" and Purple for "Operational/Active." These should be accompanied by subtle pulse animations if the status requires immediate operator attention.

### High-Density Lists
List items use thin, 1px horizontal dividers in low-opacity grey. Data columns are strictly aligned to a sub-grid to ensure rapid scanning of logistics timestamps and security clearances.