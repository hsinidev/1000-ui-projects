---
name: Atmos-Flow
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434654'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737685'
  outline-variant: '#c3c6d6'
  surface-tint: '#0c56d0'
  primary: '#003d9b'
  on-primary: '#ffffff'
  primary-container: '#0052cc'
  on-primary-container: '#c4d2ff'
  inverse-primary: '#b2c5ff'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#004a54'
  on-tertiary: '#ffffff'
  tertiary-container: '#006470'
  on-tertiary-container: '#33e6ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#9cf0ff'
  tertiary-fixed-dim: '#00daf3'
  on-tertiary-fixed: '#001f24'
  on-tertiary-fixed-variant: '#004f58'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
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
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-padding: 32px
  gutter: 24px
---

## Brand & Style

This design system is built upon the principles of clinical precision and atmospheric tranquility. It mirrors the experience of breathing pure, conditioned air: light, unobtrusive, and refreshing. The aesthetic draws heavily from high-end medical laboratory equipment and futuristic aerospace interiors, prioritizing clarity and trust.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes expansive whitespace to create a sense of "breathability" within the interface, while translucent layers suggest the invisible yet tangible nature of air. Every interaction is designed to feel deliberate and calm, avoiding unnecessary friction to evoke a sense of professional reliability and luxury.

## Colors

The color palette is rooted in sterile purity and technical depth. **Pure White** serves as the primary canvas, ensuring the interface feels surgical and clean. **Medical Blue** is used strategically for primary actions and critical status indicators, providing a grounded, authoritative contrast.

**Glass-Cyan** is the signature accent of the design system, used primarily for background washes, decorative blurs, and secondary interactive elements to reinforce the "airy" metaphor. A spectrum of cool-toned grays (Slates) is used for typography and borders to maintain a sophisticated, tech-forward appearance without the harshness of pure black.

## Typography

The typography strategy balances editorial elegance with technical rigor. **Space Grotesk** is utilized for headlines and primary data points, offering a geometric, futuristic character that aligns with high-performance engineering. 

**Inter** is the workhorse for body copy and UI labels, chosen for its exceptional legibility and neutral, systematic tone. For climate metrics and air quality readouts, the system utilizes a high-weight, tracked-out styling of Inter to mimic the precision of digital medical displays. Generous line-heights are maintained across all levels to prevent visual crowding.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop environments and a fluid, margin-heavy model for mobile. The layout is built on an 8px base unit to ensure mathematical harmony between components.

The layout philosophy emphasizes "Atmospheric Padding." Elements are never cramped; instead, they are given significant breathing room to reflect the premium nature of the product. Information density is kept low on primary dashboards, with deep-dive technical data reserved for secondary "Technical Specs" drawers or modals.

## Elevation & Depth

Hierarchy in this design system is conveyed through **Glassmorphism** and soft, ambient shadows. Instead of traditional opaque stacking, the system uses "layered translucency."

- **Base Layer:** Pure #FFFFFF.
- **Surface Layer:** Semi-transparent Glass-Cyan (#E0F7FA at 40-60% opacity) with a 12px to 20px backdrop blur.
- **Shadows:** Use extremely diffused, low-opacity shadows tinted with Medical Blue (e.g., `rgba(0, 82, 204, 0.08)`) to avoid a "dirty" look and maintain the clinical aesthetic.
- **Borders:** Low-contrast, 1px solid borders in a slightly darker cyan or white are used to define edges on translucent surfaces, mimicking the bezel of high-end glass equipment.

## Shapes

The shape language is "Softly Technical." A **Rounded (Level 2)** approach is standard, utilizing 0.5rem (8px) for base components and up to 1.5rem (24px) for large containers and cards.

This level of roundedness avoids the aggression of sharp corners while maintaining a more professional and structured feel than fully pill-shaped "organic" UI. It suggests precision manufacturing—like the curved metal and glass of a premium air purification unit.

## Components

### Buttons
Primary buttons use a solid Medical Blue fill with white text, featuring a subtle inner glow to appear slightly convex and "robust." Secondary buttons utilize the glass effect: a semi-transparent cyan background with a crisp 1px border.

### Cards
Cards are the primary organizational unit. They must feature a backdrop blur and a thin, light-colored border. Shadows should only be applied to the "active" or "top-level" card in a stack to indicate focus.

### Inputs & Controls
Input fields use a subtle inset shadow to appear recessed into the surface, suggesting a physical console. Sliders for temperature or fan speed should be thick and tactile, with the active track highlighted in Medical Blue.

### Status Indicators
Air quality indicators use glowing "pulses" rather than static dots. The glow uses a heavy blur of the status color (Green for Pure, Blue for Cooling, Amber for Warning) to simulate light refracting through vapor.

### Technical Data Points
Data such as "PM2.5 Levels" or "Filter Life %" should be displayed in Space Grotesk, accompanied by a small, uppercase Inter label. These units should be grouped in a "Technical Cluster" with a slightly darker neutral background to separate data from navigation.