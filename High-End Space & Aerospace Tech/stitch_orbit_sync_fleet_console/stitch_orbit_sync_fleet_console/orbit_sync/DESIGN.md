---
name: Orbit-Sync
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#ffb3ac'
  on-secondary: '#680008'
  secondary-container: '#c40019'
  on-secondary-container: '#ffd2cd'
  tertiary: '#fff6ed'
  on-tertiary: '#412d00'
  tertiary-container: '#ffd58c'
  on-tertiary-container: '#7e5900'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#ffdad6'
  secondary-fixed-dim: '#ffb3ac'
  on-secondary-fixed: '#410003'
  on-secondary-fixed-variant: '#930010'
  tertiary-fixed: '#ffdea8'
  tertiary-fixed-dim: '#ffba20'
  on-tertiary-fixed: '#271900'
  on-tertiary-fixed-variant: '#5e4200'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  header-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.05em
  micro-code:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style
The design system is engineered for mission-critical aerospace environments where cognitive load management and rapid data ingestion are paramount. The personality is hyper-technical, precise, and authoritative, evoking the atmosphere of a modern orbital command center.

The aesthetic utilizes a **High-Contrast Technical Glassmorphism** style. It merges the utility of industrial instrumentation with futuristic digital interfaces. High-visibility accents guide the eye through complex telemetry, while semi-transparent layers provide depth without sacrificing the "flat" precision required for professional engineering tools. Interactive elements utilize subtle glow effects to simulate self-illuminated physical hardware.

## Colors
The palette is rooted in a "True Dark" philosophy to minimize eye strain during long-duration monitoring. 

- **Deep Space Black (#050505):** The primary canvas, providing a void-like foundation for high-contrast data.
- **Neon Cyan (#00F2FF):** The primary signal color. Used for active states, data highlights, and successful system pings.
- **Pure White (#FFFFFF):** Reserved for primary typography and maximum-priority status icons.
- **Alert Red (#FF3B3B):** Reserved exclusively for critical failures, anomalies, and emergency stop actions.
- **Warning Amber (#FFB800):** Used for cautionary telemetry and non-critical system deviations.

Secondary neutrals should be derived from the Neon Cyan at very low opacities (5-10%) to create "tinted blacks" for subtle section nesting.

## Typography
This design system employs a dual-font strategy to distinguish between narrative UI and technical data.

**Inter** is utilized for standard UI elements, headers, and descriptions to ensure maximum legibility at a glance. **JetBrains Mono** is reserved for all numerical data, telemetry readouts, status labels, and "monitored" terminal output. This monospaced font ensures that rapidly changing numerical values do not cause layout shifts and maintain a distinct "instrumentation" feel. 

All labels should be rendered in uppercase with increased letter spacing to emulate industrial plate engraving.

## Layout & Spacing
The layout follows a **Fluid Grid** model optimized for ultra-wide and multi-monitor setups. It utilizes a 12-column grid system with strict 16px gutters.

Spacing follows a 4px base unit, emphasizing a high-density information architecture. Components should be packed tightly to allow more data on-screen, using thin borders rather than large whitespace gaps to define boundaries. Padding within containers should be consistent (typically 16px) to maintain the structural integrity of a "control panel" layout.

## Elevation & Depth
Depth is communicated through **Glassmorphism and Tonal Layering** rather than traditional drop shadows.

- **Level 0 (Base):** Deep Space Black background.
- **Level 1 (Panels):** Semi-transparent surfaces with a `backdrop-filter: blur(12px)` and a 1px border of `rgba(255, 255, 255, 0.05)`.
- **Level 2 (Overlays):** Increased transparency and a thin Neon Cyan border (20% opacity).
- **Interactive States:** Elements "elevate" by increasing their inner glow or the intensity of their border stroke, simulating a hardware button lighting up. 

Avoid using large, soft shadows. If a shadow is required for an overlay, it must be a sharp, high-opacity "hard shadow" to maintain the industrial aesthetic.

## Shapes
The shape language is primarily linear and architectural. Standard components use a **Soft (0.25rem)** corner radius to prevent the UI from feeling overly aggressive while maintaining a professional, engineered look. 

Buttons and input fields should strictly adhere to this 4px radius. Large container sections may use the same radius or remain entirely sharp (0px) to reinforce the grid-locked structure of the interface. Decorative elements, such as corner notches or 45-degree chamfers, are encouraged for high-level dashboard modules.

## Components
### Buttons
Primary buttons utilize a solid Neon Cyan fill with Pure Black text. On hover, they emit a `box-shadow` glow of the same color. Secondary buttons are "Ghost" style with a 1px Cyan border.

### Chips & Status Indicators
Chips use monospaced typography. Status indicators for "Live" data must include a pulsing 4px dot next to the label to indicate active telemetry.

### Input Fields
Inputs feature a dark background (slightly lighter than the base) with a bottom-only Cyan border that expands to a full frame on focus.

### Cards & Modules
All modules are "Glass" containers. They should include "Technical Accents," such as micro-labels in the top-left corner or simulated "screw-head" icons in the corners to reinforce the industrial hardware metaphor.

### Data Visualization
Charts should avoid fills where possible, preferring high-contrast strokes. Use Neon Cyan for the primary data line, Warning Amber for thresholds, and Alert Red for breaches. Grid lines within charts should be ultra-thin (0.5px) and low-contrast.

### Hexagonal Accents
For specialized aerospace modules, subtle hexagonal tiling can be used as a background pattern within specific containers to reference heat-shield tiling or satellite structures.