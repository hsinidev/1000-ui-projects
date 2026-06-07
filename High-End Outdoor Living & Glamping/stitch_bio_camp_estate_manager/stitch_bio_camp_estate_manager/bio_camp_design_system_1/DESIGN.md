---
name: Bio-Camp Design System
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
  secondary: '#ffb693'
  on-secondary: '#561f00'
  secondary-container: '#fe6b00'
  on-secondary-container: '#572000'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#191919'
  on-tertiary-container: '#838281'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#ffb693'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7a3000'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-lg:
    fontFamily: JetBrains Mono
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: '0'
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
  margin: 24px
---

## Brand & Style
The design system is engineered for mission-critical environmental monitoring and campsite security. It evokes a sense of "Industrial Intelligence"—robust, precise, and uncompromising. The target audience includes field rangers, ecological researchers, and site security personnel who operate in high-stakes environments where data clarity can impact safety and conservation efforts.

The visual style is a blend of **Technical Minimalism** and **High-Contrast Utility**. It prioritizes immediate cognitive processing over decorative flair. The aesthetic borrows from avionics and military HUDs, using dark modes to reduce eye fatigue during night operations and intense color accents to signal status and priority.

## Colors
This design system utilizes a deep, nocturnal palette to establish a high-security atmosphere. 

- **Primary Background (Midnight Blue):** Used for the base canvas to provide depth and reduce glare.
- **Action/Alert (Safety Orange):** Reserved for primary calls to action, critical sensor alerts, and "active" states. It must be used sparingly to maintain its psychological impact.
- **Secondary/Surface (Graphite):** Applied to card backgrounds, secondary buttons, and structural dividers to provide subtle contrast against the Midnight Blue.
- **Functional Accents:** Vibrant greens and reds are used strictly for ecological health indicators and security breaches.

## Typography
The typography system uses a dual-font approach to balance readability with a technical aesthetic. 

- **JetBrains Mono** is utilized for headlines, labels, and data points. Its monospaced nature ensures that numerical sensor data (coordinates, temperatures, animal counts) remains perfectly aligned and legible at a glance.
- **Inter** is used for long-form text and body descriptions. Its humanist qualities ensure high legibility on mobile devices used in the field.
- **Information Hierarchy:** Heavy use of All-Caps for labels signals a "Command Center" feel. Data should always be more prominent than its descriptive label.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model. While the dashboard containers use a fluid grid to maximize screen real estate on rugged tablets, individual data modules (cards) adhere to a strict 8px spacing rhythm.

- **Grid:** A 12-column grid system for desktop; 4-column for mobile.
- **Density:** High density is preferred. Field staff need to see as much telemetry as possible without scrolling. 
- **Gutters:** Tight 16px gutters reinforce the robust, structured feel of a technical instrument.

## Elevation & Depth
Elevation in this design system is communicated through **Tonal Layering** and **Subtle Glows** rather than traditional shadows.

- **Layer 0:** Midnight Blue (#0A192F) base.
- **Layer 1:** Graphite (#333333) for card containers.
- **Layer 2:** Neutral Surface (#162235) for inset elements like input fields.
- **Active State Depth:** Active sensors or critical alerts utilize a "Safety Orange" outer glow (0px 0px 12px) to simulate a backlit hardware button. 
- **Borders:** Thin, 1px high-contrast borders (#2D3E50) are used to define boundaries in place of soft shadows, maintaining a crisp, technical look.

## Shapes
This design system employs a **Sharp (0px)** corner radius for all primary structural elements. 

The use of 90-degree angles emphasizes the "High-Security" and "Technical" nature of the software. It mimics industrial hardware casings and blueprints. Small exceptions may be made for status pips or specialized ecological icons, but all containers, buttons, and input fields must remain strictly rectangular to reinforce the feeling of a robust, calibrated tool.

## Components
- **Buttons:** Primary buttons use a solid Safety Orange fill with JetBrains Mono bold text. Secondary buttons use a Graphite background with a 1px border. No rounded corners.
- **Alert Cards:** High-priority cards feature a 4px left-hand border in Safety Orange or Status Red. Backgrounds remain Graphite to maintain contrast.
- **Sensor Toggles:** Designed to look like physical heavy-duty switches. When 'On', the toggle handle glows Safety Orange.
- **Data Tables:** Striped rows using Midnight Blue and a slightly lighter tint. Column headers are always uppercase JetBrains Mono with a distinct border-bottom.
- **Telemetry Chips:** Small, rectangular tags used to show sensor status (e.g., "GPS: LOCKED", "BAT: 84%"). 
- **Input Fields:** Dark background (#162235) with a 1px border that turns Safety Orange on focus. Labels are positioned above the field in uppercase.
- **Active Sensor Indicator:** A pulsating dot with a subtle glow, placed next to live ecological feeds to indicate real-time connectivity.