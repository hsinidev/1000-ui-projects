---
name: Stratospheric HUD
colors:
  surface: '#111318'
  surface-dim: '#111318'
  surface-bright: '#37393e'
  surface-container-lowest: '#0c0e12'
  surface-container-low: '#1a1c20'
  surface-container: '#1e2024'
  surface-container-high: '#282a2e'
  surface-container-highest: '#333539'
  on-surface: '#e2e2e8'
  on-surface-variant: '#bec7d4'
  inverse-surface: '#e2e2e8'
  inverse-on-surface: '#2f3035'
  outline: '#88919d'
  outline-variant: '#3f4852'
  surface-tint: '#98cbff'
  primary: '#98cbff'
  on-primary: '#003354'
  primary-container: '#00a3ff'
  on-primary-container: '#00375a'
  inverse-primary: '#00629d'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#9c9d9d'
  on-tertiary-container: '#333535'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#cfe5ff'
  primary-fixed-dim: '#98cbff'
  on-primary-fixed: '#001d33'
  on-primary-fixed-variant: '#004a77'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#111318'
  on-background: '#e2e2e8'
  surface-variant: '#333539'
typography:
  display-telemetry:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-instrument:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-standard:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-monospace:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  data-readout:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  instrument-gap: 8px
  container-padding: 20px
---

## Brand & Style

This design system is engineered for the high-stakes environment of stratospheric research. The aesthetic prioritizes **scientific precision** and **operational clarity**, evoking the feeling of a glass cockpit at 100,000 feet. 

The visual style is a hybrid of **Glassmorphism** and **Technical Minimalism**. It utilizes semi-transparent overlays to maintain a sense of environmental depth, while thin, high-contrast borders ensure data integrity. Every element must feel like a calibrated instrument; there is no room for decorative flourishes that do not serve an informational purpose. The emotional response is one of calm, focused authority—mimicking the quiet, cold, and expansive nature of high-altitude flight.

## Colors

The palette is strictly atmospheric. The background is a deep, near-black "Space" neutral to maximize contrast for the light-emitting UI. 

- **Primary (Sky Blue):** Used for active data streams, primary indicators, and critical telemetry lines. It should have a subtle 2px outer glow to simulate a light-emitting phosphor display.
- **Secondary (Silver):** Used for structural elements, scales, and inactive units of measurement.
- **Tertiary (Cloud White):** Reserved for high-priority readouts and critical labels that require immediate legibility against the dark background.
- **Functional Accents:** Success, Warning, and Error colors are desaturated to fit the "technical" vibe but remain distinct for rapid diagnostic scanning.

## Typography

The typography strategy employs a hierarchy of technicality. **Space Grotesk** is used for structural headings and instrument names, providing a futuristic, geometric foundation. **Hanken Grotesk** handles dense instructional text due to its exceptional legibility. 

**JetBrains Mono** is the workhorse of the system, used for all numerical data, telemetry strings, and labels. Its fixed-width nature ensures that fluctuating data points do not cause horizontal layout shifts, allowing operators to track numerical changes with high precision. All labels should be rendered in uppercase to mimic aviation standards.

## Layout & Spacing

The layout follows a **Fixed Grid** system inspired by flight deck displays. The screen is divided into primary "Instrument Clusters." 

- **The Main HUD:** A central viewport for primary mission data (altitude, ascent rate, coordinates).
- **Lateral Panels:** Fixed-width sidebars (320px) for subsystem monitoring (battery, gas pressure, thermal).
- **Footer Status Bar:** A persistent 40px bar for global system health and connectivity status.

Spacing is tight and systematic, utilizing a 4px base unit. Information density is high, but logical grouping via 16px gutters prevents cognitive overload.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism and Luminance** rather than traditional shadows. 

- **Base Layer:** The "Space" background.
- **Mid Layer:** Semi-transparent "Cloud" surfaces (White at 5-10% opacity) with a 20px backdrop blur. These represent the instrument housings.
- **Top Layer:** High-contrast text and interactive elements.
- **Borders:** Every container must have a 1px solid Silver border at 20% opacity. 
- **Glow:** Interactive elements or critical warnings use a "Phosphor Glow"—a drop shadow with 0 offset, a 4-8px blur, and a color matching the element (Primary or Error).

## Shapes

The shape language is **Sharp (0)**. To reinforce the scientific and industrial nature of the system, all containers, buttons, and input fields utilize 90-degree angles. 

Occasional 45-degree "clipped corners" (chamfers) may be used for primary action buttons or high-level navigation tabs to further the aeronautical aesthetic. Circles are reserved exclusively for circular gauges, compasses, and radial dials.

## Components

### Buttons & Inputs
Buttons are thin-bordered rectangles. The "Primary" state features a subtle inner glow and a 10% Sky Blue fill. Input fields should resemble data entry terminals, with a blinking underscore cursor and mono-spaced text.

### Telemetry Chips
Small, high-density labels used for tagging data streams (e.g., `ALT`, `VEL`, `TMP`). These use a Silver background with black text for maximum contrast or a transparent background with a Sky Blue border.

### Instrument Cards
These are the primary containers. They feature a "Header Bar" with a chamfered edge and a thin 1px border. Backgrounds use the semi-transparent glass effect to ensure the underlying atmospheric map or camera feed remains visible.

### Flight Indicators
Specialized components include a vertical "Tape Altimeter," a radial "Heading Indicator," and a "Trend Vector" line graph. These must use the primary Sky Blue color and thin stroke weights (1px to 1.5px).

### Navigation
The main navigation is a "Mode Selector" at the top of the screen, mimicking physical toggle switches. Clicking a mode should trigger a "scanning" animation across the screen to signal a state change.