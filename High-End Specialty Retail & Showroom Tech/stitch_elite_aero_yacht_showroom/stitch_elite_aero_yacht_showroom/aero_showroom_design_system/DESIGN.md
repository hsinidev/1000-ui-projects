---
name: Aero-Showroom Design System
colors:
  surface: '#100f2f'
  surface-dim: '#100f2f'
  surface-bright: '#363657'
  surface-container-lowest: '#0a0a2a'
  surface-container-low: '#181838'
  surface-container: '#1c1c3c'
  surface-container-high: '#272747'
  surface-container-highest: '#313153'
  on-surface: '#e2dfff'
  on-surface-variant: '#c6c5d5'
  inverse-surface: '#e2dfff'
  inverse-on-surface: '#2d2d4e'
  outline: '#908f9e'
  outline-variant: '#464653'
  surface-tint: '#bfc2ff'
  primary: '#bfc2ff'
  on-primary: '#181d8c'
  primary-container: '#000080'
  on-primary-container: '#777eea'
  inverse-primary: '#4b53bc'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#ae8d10'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#202222'
  on-tertiary-container: '#888989'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bfc2ff'
  on-primary-fixed: '#00006e'
  on-primary-fixed-variant: '#3239a3'
  secondary-fixed: '#ffe087'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#231a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#100f2f'
  on-background: '#e2dfff'
  surface-variant: '#313153'
typography:
  display-xl:
    fontFamily: Hanken Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  technical-label:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  mono-data:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
spacing:
  grid-margin: 48px
  gutter: 24px
  unit: 8px
  section-gap: 80px
  hud-padding: 16px
---

## Brand & Style
This design system captures the intersection of high-altitude aviation and deep-sea luxury. The brand personality is authoritative and hyper-technical, evoking the feeling of a pilot’s Head-Up Display (HUD) or a captain’s bridge. It targets high-net-worth individuals and logistics professionals who demand precision, exclusivity, and clarity.

The aesthetic combines **Glassmorphism** with **Technical Minimalism**. Deep navy backgrounds provide a foundation of stability, while semi-transparent frosted containers and glowing gold accents create a sense of ethereal luxury. Intricate line work and "radar" motifs bridge the gap between a consumer-facing high-end showroom and a data-dense Admin Command Center.

## Colors
The palette is rooted in a dark-mode-first architecture. 
- **Midnight Navy (#000080):** The primary canvas, used for deep backgrounds to minimize eye strain and maximize the "infinite sky/sea" feel.
- **Aero Gold (#E9C349):** The precision accent. Used for interactive elements, status indicators, and critical HUD data.
- **Cloud White (#FFFFFF):** High-contrast secondary used for primary legibility and iconography.
- **Glass/Stroke:** A technical palette of semi-transparent whites and navy variants used for borders and container backgrounds to create the frosted glass effect.

## Typography
**Hanken Grotesk** serves as the sole typeface to maintain a clinical, high-tech consistency across both the Showroom and Admin interfaces. 

Headlines utilize tighter tracking and heavier weights for a commanding presence. Labels and data-heavy Admin components leverage uppercase transformations and increased letter spacing to mimic flight instrument readouts. For mobile, `display-xl` scales down to 40px, while `headline-lg` adjusts to 28px to ensure technical legibility on smaller viewports.

## Layout & Spacing
The layout employs a **12-column fluid grid** for the consumer showroom to allow high-resolution imagery of aircraft and yachts to breathe. For the **Admin Command Center**, the system shifts to a **fixed-sidebar navigation** with a modular dashboard layout.

Spacing is based on an 8px technical rhythm. The "HUD" effect is achieved through wide outer margins (48px+) that frame the content, creating a sense of looking through a cockpit window. Elements should be grouped in modular "pods" with 16px internal padding.

## Elevation & Depth
Depth is expressed through **Glassmorphism** and **Light Emission** rather than traditional shadows.
- **Layer 0 (Base):** Deep Navy (#000080).
- **Layer 1 (Containers):** Semi-transparent white (5-8% opacity) with a 20px backdrop blur and 1px hairline border (Cloud White at 15% opacity).
- **Layer 2 (Interactive):** Active elements emit a "Gold Glow" (Outer Glow: 0px 0px 12px Aero Gold at 40% opacity).
- **Technical Overlays:** Fine 0.5px line-work crosshairs or grid patterns are used to separate data sections in the Admin Center, providing depth without adding visual bulk.

## Shapes
This design system utilizes a **Sharp (0px)** aesthetic to reinforce the technical, military-grade precision of aerospace engineering. 

While containers are strictly rectangular, call-to-action buttons may feature "clipped corners" (45-degree chamfers) to evoke cockpit controls. Decorative elements like progress bars or status pips must remain geometric and hard-edged.

## Components
- **Buttons:** Primary buttons are outlined in 1px Gold with a faint gold inner glow. Text is always uppercase `technical-label`.
- **HUD Glass Cards:** Large containers for aircraft specs. Features a 1px white border with "corner bracket" accents—small technical L-shapes at each vertex.
- **Data Inputs:** Ghost-style inputs. Only a bottom border is visible until focused, at which point the entire container gains a faint blue-tinted glass background.
- **Status Indicators:** Small square pips. Gold for "Available," White for "In-Transit," and a dimmed Navy for "Sold."
- **Admin Command Modules:** Collapsible side panels for technical telemetry (engine hours, knot speed, fuel range). These use `mono-data` typography for high-density readability.
- **Telemetry Charts:** Vector-based line graphs using Gold for primary data paths, set against a subtle 10% opacity white grid.