---
name: Helios Flux
colors:
  surface: '#0b1323'
  surface-dim: '#0b1323'
  surface-bright: '#31394a'
  surface-container-lowest: '#060e1d'
  surface-container-low: '#131c2b'
  surface-container: '#18202f'
  surface-container-high: '#222a3a'
  surface-container-highest: '#2d3546'
  on-surface: '#dbe2f8'
  on-surface-variant: '#c8c8ad'
  inverse-surface: '#dbe2f8'
  inverse-on-surface: '#283041'
  outline: '#929279'
  outline-variant: '#474833'
  surface-tint: '#c2d000'
  primary: '#ffffff'
  on-primary: '#2f3300'
  primary-container: '#deed2e'
  on-primary-container: '#626900'
  inverse-primary: '#5c6300'
  secondary: '#ffb86b'
  on-secondary: '#492900'
  secondary-container: '#ed9000'
  on-secondary-container: '#583300'
  tertiary: '#ffffff'
  on-tertiary: '#00363d'
  tertiary-container: '#9cf0ff'
  on-tertiary-container: '#006f7c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#deed2e'
  primary-fixed-dim: '#c2d000'
  on-primary-fixed: '#1b1d00'
  on-primary-fixed-variant: '#454b00'
  secondary-fixed: '#ffdcbc'
  secondary-fixed-dim: '#ffb86b'
  on-secondary-fixed: '#2c1700'
  on-secondary-fixed-variant: '#683d00'
  tertiary-fixed: '#9cf0ff'
  tertiary-fixed-dim: '#00daf3'
  on-tertiary-fixed: '#001f24'
  on-tertiary-fixed-variant: '#004f58'
  background: '#0b1323'
  on-background: '#dbe2f8'
  surface-variant: '#2d3546'
typography:
  display-lg:
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 1.5rem
  margin: 2rem
  container-max: 1440px
---

## Brand & Style

This design system centers on the concept of "Harnessing the Sun," blending high-performance utility with a futuristic, tech-forward aesthetic. The brand personality is energetic, optimistic, and highly precise, designed to appeal to homeowners who view their energy consumption as a data-driven lifestyle choice.

The visual style is a fusion of **Glassmorphism** and **Bento-box** modularity. We utilize translucent layers and vibrant backdrops to simulate the clarity of high-grade solar glass. The interface should feel like a premium command center—dark, immersive, and glowing with live data.

## Colors

The palette is optimized for a dark-mode-first experience to maximize the "glow" effect of data visualizations.

- **Primary (Electric Yellow):** Used for primary actions, current energy generation stats, and active states. It represents the raw power of the sun.
- **Secondary (Sun-glow Orange):** Reserved for storage levels (batteries), heat-maps, and warnings.
- **Tertiary (Cyber Cyan):** Used for grid-export data and secondary tech indicators.
- **Neutral (Midnight Navy):** Deep, saturated blues serve as the foundation, providing a more sophisticated contrast than pure black.
- **Accents:** High-vibrancy gradients transition from Electric Yellow to Sun-glow Orange to represent the daily solar cycle.

## Typography

This design system uses a dual-font strategy to balance technical precision with readability. 

**Space Grotesk** is used for headlines and large data readouts. Its geometric quirks and "tech" feel reinforce the solar innovation theme. **Inter** is used for all body copy, labels, and instructional text to ensure maximum clarity on dense dashboards. Numerical data should always use tabular lining to ensure numbers align perfectly in charts and tables.

## Layout & Spacing

The layout follows a **Fixed-Width Bento Box** model. Content is organized into modular "tiles" of varying sizes that snap to a 12-column grid. 

- **Grid:** 12-columns with 24px gutters.
- **Modular Rhythm:** Dashboard tiles should occupy 3, 4, 6, or 12 columns.
- **Padding:** Internal tile padding is a consistent 24px (3 units) to maintain a spacious, premium feel despite high data density.
- **Alignment:** All elements are center-aligned vertically within their bento containers to maintain balance.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Luminous Shadows** rather than traditional grey drop shadows.

- **Base Layer:** Deep Midnight Blue (#020817).
- **Surface Layer (Tiles):** Semi-transparent navy with a 12px backdrop-blur and a 1px border at 10% white opacity.
- **Glow Effects:** Active components (like the "System On" indicator) utilize an outer glow (box-shadow) using the Primary color with a 20px spread and 30% opacity.
- **Interactive States:** When hovered, tiles should increase in border-opacity and the backdrop-blur should intensify, creating a "lifting" effect.

## Shapes

The shape language is modern and approachable, utilizing consistent rounding to soften the technical nature of the data. 

- **Containers:** Bento tiles and main cards use `rounded-xl` (1.5rem) to create a soft, encapsulated look.
- **Interactive Elements:** Buttons and input fields use `rounded-lg` (1rem).
- **Data Visuals:** Progress bars and graph terminals use fully rounded (pill) caps.

## Components

### Buttons & Inputs
Buttons feature a subtle top-to-bottom gradient of the Primary color. The "Primary Action" button has a faint yellow drop-shadow to simulate light emission. Input fields are dark with semi-transparent fills and glow on focus.

### Bento Cards
The core unit of the design system. Every card must have a consistent corner radius and a 1px "glass" stroke. Cards should be categorized into "Static" (labels) and "Live" (real-time data streams).

### Data Visualization
Charts use "Neon-Line" styling—high-stroke-width lines with a blur layer underneath to create a glowing wire effect. 

### Status Chips
Small, high-contrast indicators. "Generating" uses the Electric Yellow glow; "Standby" uses a muted Grey-Blue; "Alert" uses the Sun-glow Orange.

### Solar Specifics
- **Energy Flow Component:** An animated path showing the flow of power from panels to battery to home using moving "light particles."
- **Sun Tracker:** A semi-circular gauge that visualizes the sun's position relative to peak efficiency.