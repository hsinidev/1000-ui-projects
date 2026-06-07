---
name: Lumina Grid
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#89ceff'
  on-secondary: '#00344d'
  secondary-container: '#00a2e6'
  on-secondary-container: '#00344e'
  tertiary: '#defcff'
  on-tertiary: '#00363a'
  tertiary-container: '#00f1ff'
  on-tertiary-container: '#006a70'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#c9e6ff'
  secondary-fixed-dim: '#89ceff'
  on-secondary-fixed: '#001e2f'
  on-secondary-fixed-variant: '#004c6e'
  tertiary-fixed: '#79f5ff'
  tertiary-fixed-dim: '#00dbe8'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
spacing:
  base: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for the renewable energy sector, targeting engineers, environmentalists, and tech-forward homeowners. The aesthetic is "Energy-Efficient Brutalism"—a high-contrast, low-glow style that prioritizes data legibility and power preservation on OLED displays. 

The brand personality is technical, urgent, and precise. It avoids unnecessary decoration, opting instead for a "Command Center" feel. By utilizing deep slates and sharp accents, the UI evokes the feeling of advanced monitoring software used in modern smart-grids and solar arrays.

## Colors

The palette is optimized for dark-room environments and energy efficiency. 
- **Core Canvas**: The primary background (#0F172A) provides a deep, non-distracting foundation.
- **Surface Hierarchy**: Secondary surfaces (#1E293B) and tertiary containers (#334155) create clear visual grouping without the need for heavy drop shadows.
- **The Sun-Yellow (#FFD700)**: Reserved strictly for primary calls to action, active toggles, and critical system statuses.
- **The Sky-Blue (#0EA5E9)**: Used for technical data points, progress bars, and informational links, providing a cool contrast to the warm primary yellow.
- **Success/Warning**: Use Sky-Blue for "nominal" operations and Sun-Yellow for "active/high-output" alerts.

## Typography

The design system utilizes **Space Grotesk** across all levels to maintain a technical, futuristic edge. 
- **Headlines**: Large, bold, and tightly tracked to mimic architectural signage.
- **Body Text**: Rendered in pure white or light grey (#E2E8F0) to ensure high contrast against the midnight background.
- **Labels**: Utilize the uppercase "label-caps" style for all technical metadata and small UI descriptors to improve scannability in dense data views.
- **Readability**: Always use a minimum of 1.5 line height for body copy to prevent the "vibrating text" effect often found in high-contrast dark modes.

## Layout & Spacing

This design system uses a **Fixed Grid** model for desktop (1280px max-width) and a **Fluid Grid** for mobile devices. 
- **The Grid**: A 12-column layout with 24px gutters. Elements should align strictly to the vertical rhythm.
- **Rhythm**: All spacing is based on a 4px base unit. 
- **Density**: Given the technical nature of the product, use "md" spacing for dashboard views to maximize information density, while using "lg" and "xl" for landing pages to allow the high-contrast typography to breathe.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** rather than traditional shadows to maintain the energy-efficient aesthetic.
- **Level 0 (Canvas)**: #0F172A. Used for the main background.
- **Level 1 (Surface)**: #1E293B. Used for secondary sections and large cards.
- **Level 2 (Container)**: #334155. Used for interactive elements within surfaces or highlighted content.
- **Accents**: Use 1px solid borders in Sky-Blue (#0EA5E9) at 20% opacity to define boundaries on Level 2 containers. Shadows are used sparingly, only as a 4px "hard shadow" with 0 blur in Sun-Yellow for focused interactive states.

## Shapes

To reinforce the industrial and technical narrative, this design system uses **Sharp (0px)** corners for all primary UI elements. 
- **Exceptions**: Use circular shapes only for status indicators (LED style) or user avatars. 
- **Borders**: All containers should have a 1px border. For standard containers, use a slightly lighter slate; for active elements, use the Sky-Blue or Sun-Yellow.

## Components

- **Buttons**: Primary buttons are solid Sun-Yellow with black text (#000000). Secondary buttons use a Sky-Blue 1px border with Sky-Blue text. All buttons have 0px radius.
- **Input Fields**: Background matches the #1E293B surface with a #334155 border. On focus, the border turns Sky-Blue.
- **Chips**: Small, rectangular boxes with Sky-Blue borders and "label-caps" typography, used for system tags (e.g., "SOLAR", "GRID", "BATTERY").
- **Data Visualizations**: Use Sky-Blue for the primary data line and Sun-Yellow for peak values or warning thresholds. Grid lines within charts should be #334155 at 50% opacity.
- **Status Indicators**: A small square icon. Pulse the Sun-Yellow for "Active" and keep Sky-Blue static for "Standby."
- **Cards**: Sharp-edged containers with a background of #1E293B and a top-border of 2px in Sky-Blue to denote technical data blocks.