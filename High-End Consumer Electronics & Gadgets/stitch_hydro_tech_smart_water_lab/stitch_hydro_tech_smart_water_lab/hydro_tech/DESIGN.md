---
name: Hydro-Tech
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
  secondary: '#006973'
  on-secondary: '#ffffff'
  secondary-container: '#6debfd'
  on-secondary-container: '#006974'
  tertiary: '#324749'
  on-tertiary: '#ffffff'
  tertiary-container: '#495e61'
  on-tertiary-container: '#c0d7da'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#93f1ff'
  secondary-fixed-dim: '#56d7e9'
  on-secondary-fixed: '#001f23'
  on-secondary-fixed-variant: '#004f57'
  tertiary-fixed: '#d0e7ea'
  tertiary-fixed-dim: '#b4cbce'
  on-tertiary-fixed: '#091f21'
  on-tertiary-fixed-variant: '#364a4d'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-lg:
    fontFamily: manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: manrope
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
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
  data-display:
    fontFamily: jetbrainsMono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 16px
  container-max: 1280px
---

## Brand & Style

This design system embodies a clinical, high-end medical-grade aesthetic centered on the concept of "Absolute Purity." The UI must evoke feelings of sterile precision, reliability, and technological advancement. The target audience includes laboratory technicians, medical professionals, and high-end home purification enthusiasts who demand data transparency and professional-grade performance.

The visual direction is a refined **Glassmorphism**, utilizing multi-layered transparency to mimic the properties of water and laboratory glassware. The interface should feel breathable and light, utilizing high-transparency surfaces, soft ambient shadows, and fluid motion to communicate the flow and filtration of water. Elements should appear as if they are suspended in a clear liquid medium, maintaining a sterile, professional atmosphere.

## Colors

The palette is rooted in medical sterility and hydraulic clarity.
- **Pure White (#FFFFFF):** Used for primary backgrounds to establish a clinical, "lab-room" environment.
- **Medical Blue (#0052CC):** Reserved for primary actions, critical status indicators, and brand-level trust elements.
- **Glass-Cyan (#E0F7FA & #4DD0E1):** These are the functional "fluid" colors. Use the lighter tint for large glass surfaces and the darker tint for active data visualizations and secondary accents.
- **Surface Accents:** Use subtle blue-tinted greys for borders to maintain a cool temperature across the UI.

## Typography

This design system utilizes a tiered typographic approach to balance clinical readability with technical data density.
- **Headlines (Manrope):** Chosen for its modern, balanced, and professional geometric structure. It provides a "high-end medical equipment" feel.
- **Body (Inter):** The workhorse for all instructional and descriptive text, providing maximum legibility and a systematic, neutral tone.
- **Technical/Data (JetBrains Mono):** Used specifically for purification metrics (pH levels, TDS, flow rates) and timestamps. The monospaced nature emphasizes technical precision and "real-time" monitoring.

## Layout & Spacing

The layout follows a **Fluid Grid** model with high internal padding to simulate the "expansion" of water. 
- **Desktop:** A 12-column grid with generous 24px gutters. Content should be centered in a 1280px container to maintain a focused, premium feel.
- **Mobile:** A 4-column grid with 16px margins. 
- **Spacing Philosophy:** Use an 8px base unit (with 4px increments for tight technical data). Prioritize "white space" as a functional element to prevent the UI from feeling cluttered or unsterile. All "Glass" containers should feature internal padding of at least 24px to ensure content doesn't feel "compressed" against the frosted edges.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** rather than traditional opaque stacking.
- **Level 1 (Base):** Pure White background.
- **Level 2 (Panels):** Glass surfaces using `rgba(255, 255, 255, 0.6)` with a 12px-20px `backdrop-filter: blur()`.
- **Level 3 (Modals/Popovers):** Higher opacity white `rgba(255, 255, 255, 0.9)` with a more pronounced, extra-diffused soft shadow (Color: `#0052CC`, Opacity: 4%, Blur: 40px).

Borders on glass elements should be 1px solid with a very low opacity (`rgba(0, 82, 204, 0.1)`) to create a "light-catching" edge effect similar to the rim of a glass beaker.

## Shapes

The shape language is "Organic-Technical." While the system is clinical, it avoids sharp, aggressive corners to mimic the surface tension of water droplets. 
- **Standard Elements:** Use a 0.5rem (8px) radius.
- **Large Containers/Cards:** Use a 1.5rem (24px) radius to emphasize the "fluid" nature of the glass panels.
- **Data Accents:** Small circular elements (fully rounded) are used for status indicators, mimicking bubbles or particles in a filtration stream.

## Components

- **Buttons:** Primary buttons use a solid Medical Blue. Secondary buttons should be "Ghost-Glass" style: a transparent background with a 1px Cyan border that fills with a light Cyan tint on hover.
- **Data Cards:** These are the centerpiece. Use high-transparency glass backgrounds with JetBrains Mono for the primary metric and a "Fluid Wave" sparkline visualization in Glass-Cyan at the bottom of the card.
- **Input Fields:** Minimalist under-line or very subtle light-grey troughs. When focused, the border glows with a soft Cyan outer shadow.
- **Progress Bars:** Designed as "Vessels." A container with a light Cyan background where the fill level is a saturated Medical Blue, using a subtle wave-motion animation at the leading edge.
- **Chips/Status:** Use soft, pill-shaped badges with low-opacity background tints (e.g., a "Pure" status uses a light Cyan tint with dark Blue text).
- **Toggle Switches:** Designed to look like clinical hardware switches, using smooth sliding transitions and blue glow states for "Active."