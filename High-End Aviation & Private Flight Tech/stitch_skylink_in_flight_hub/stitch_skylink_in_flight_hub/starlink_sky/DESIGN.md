---
name: Starlink-Sky
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#333b3b'
  surface-container-lowest: '#080f10'
  surface-container-low: '#151d1e'
  surface-container: '#192122'
  surface-container-high: '#232b2c'
  surface-container-highest: '#2e3637'
  on-surface: '#dce4e5'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dce4e5'
  inverse-on-surface: '#2a3233'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#c3c6d3'
  on-secondary: '#2c303a'
  secondary-container: '#454954'
  on-secondary-container: '#b5b8c5'
  tertiary: '#f4f5ff'
  on-tertiary: '#2b303b'
  tertiary-container: '#d5d9e7'
  on-tertiary-container: '#5a5f6b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#dfe2ef'
  secondary-fixed-dim: '#c3c6d3'
  on-secondary-fixed: '#181b25'
  on-secondary-fixed-variant: '#434751'
  tertiary-fixed: '#dee2f1'
  tertiary-fixed-dim: '#c2c6d4'
  on-tertiary-fixed: '#171c26'
  on-tertiary-fixed-variant: '#424752'
  background: '#0d1515'
  on-background: '#dce4e5'
  surface-variant: '#2e3637'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 1.5rem
  margin-desktop: 2.5rem
  margin-mobile: 1rem
  bento-gap: 1rem
---

## Brand & Style
The design system is engineered to evoke a sense of orbital precision, speed, and high-performance reliability. It targets tech-savvy travelers and executive users who demand seamless, secure connectivity in challenging environments. The brand personality is authoritative yet ethereal, blending technical sophistication with a futuristic, "cockpit-inspired" aesthetic.

The visual direction utilizes **Glassmorphism** as its foundational layer—representing the thin veil between the passenger and the stratosphere. This is paired with a **Bento-Box** layout structure to organize complex technical data into digestible, high-contrast modules. The emotional response should be one of calm control, high-speed capability, and absolute digital security.

## Colors
The palette is rooted in the deep spectrum of the upper atmosphere. The primary background is **Midnight Blue (#0A0E17)**, providing a high-contrast foundation for technical readouts. **Electric Cyan (#00F0FF)** serves as the primary action color, used for interactive elements, "One-Tap" buttons, and active status glows.

Deep obsidian shades are used to create structural depth within bento containers. Data visualizations should leverage the Electric Cyan for primary metrics, with subtle gradients transitioning into deep purples or dark blues to represent signal strength or bandwidth flow.

## Typography
This design system employs a tiered typography strategy to balance futuristic character with extreme legibility. 
- **Space Grotesk** is used for headlines and prominent display metrics, providing a technical, geometric edge. 
- **Inter** handles the bulk of the body copy, ensuring high readability during flight turbulence or in low-light cabin conditions.
- **Geist** is utilized for labels and "Privacy-Tunnel" status readouts, where its mono-spaced heritage aids in the rapid scanning of fluctuating technical data.

## Layout & Spacing
The layout follows a **Bento-Box** philosophy, utilizing a 12-column fluid grid for desktop and a single-column stack for mobile. Content is encapsulated in modular cards that span varying column counts (e.g., 4, 6, or 12). 

A strict 4px spacing scale ensures mathematical harmony. Margins are generous to maintain a "premium" feel, while the gaps between bento modules remain tight (16px) to emphasize the interconnected nature of the connectivity suite. On mobile, cards reflow vertically while maintaining their internal padding to preserve data density.

## Elevation & Depth
Elevation is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces are defined by:
1.  **Backdrop Blur:** 12px to 20px blur on container backgrounds.
2.  **Translucent Fills:** Midnight Blue at 40-60% opacity.
3.  **Subtle Borders:** 1px solid borders using a "Cyan-to-Transparent" linear gradient at 20% opacity.
4.  **Outer Glows:** Interactive elements (buttons, active status indicators) emit a soft Electric Cyan outer glow (0px 0px 15px) to simulate illuminated cockpit controls.

## Shapes
The shape language is "Soft-Tech." While the grid is rigid and geometric, individual containers utilize a **Rounded (0.5rem)** base radius to feel sophisticated and modern. 

- **Cards:** 1rem (`rounded-lg`) for external bento modules.
- **Buttons:** Fully pill-shaped (`rounded-xl`) to contrast against the rectangular grid.
- **Status Indicators:** Small circular pips with blurred glow halos.

## Components
- **One-Tap Action Buttons:** High-contrast Electric Cyan fills with black text. These should feature a slight "pulse" animation when in a ready state.
- **Bento Cards:** Semi-transparent frosted glass containers. Headers within these cards should use `label-caps` in a muted cyan.
- **Privacy-Tunnel Indicator:** A specialized component featuring a monolinear icon of a shielded node. When active, a cyan "flow" animation moves through the border of the card.
- **Data Visualizations:** Line charts and gauges should use "Neon-Stroke" styles—thin 2px lines with a concentrated glow at the leading data point.
- **Monolinear Icons:** All icons must be stroke-based (1.5px weight) with a subtle `drop-shadow` filter that matches the icon color to create a "glowing wire" effect.
- **Status Pips:** Use a "breathing" opacity animation (0.4 to 1.0) to indicate live connection telemetry.