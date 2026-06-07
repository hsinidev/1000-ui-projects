---
name: Flora-Security
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e4e2e3'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e4e2e3'
  inverse-on-surface: '#303031'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bfc6db'
  primary: '#bfc6db'
  on-primary: '#293041'
  primary-container: '#0a1221'
  on-primary-container: '#767d90'
  inverse-primary: '#575e70'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#121212'
  on-tertiary-container: '#7e7d7d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe2f8'
  primary-fixed-dim: '#bfc6db'
  on-primary-fixed: '#141c2b'
  on-primary-fixed-variant: '#3f4758'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131314'
  on-background: '#e4e2e3'
  surface-variant: '#353436'
typography:
  headline-xl:
    fontFamily: JetBrains Mono
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0em
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
  margin: 24px
  panel-padding: 20px
---

## Brand & Style

The design system is engineered to project absolute authority, technical precision, and unwavering security. It targets high-stakes environments where vegetation management and perimeter integrity are critical, such as utilities, border control, and industrial campuses.

The visual style is **Industrial Modern with Glassmorphism**. It blends the raw, structural rigidity of industrial design with the sophisticated transparency of high-tech digital interfaces. Users should feel they are operating a military-grade monitoring suite—efficient, precise, and serious. The aesthetic relies on high-contrast data visualization and tactical overlays that suggest real-time processing and forensic accuracy.

## Colors

The palette is rooted in a deep **Midnight Blue** that serves as the foundation for all backgrounds, ensuring maximum contrast for status indicators. **Graphite** is utilized for structural elements—dividers, nested panels, and inactive states—providing a subtle hierarchy within the dark UI.

**Silver** acts as the primary accent color, used for interactive triggers, borders, and "metallic" trims that define the industrial aesthetic. Status indicators are binary and aggressive: **Neon Green** signifies a secure state and healthy vegetation, while **Alert Red** is reserved strictly for perimeter breaches or critical system failures.

## Typography

This design system utilizes a dual-font strategy to balance technical utility with information density. **JetBrains Mono** is the primary font for headlines, labels, and data points, providing a monospaced "terminal" aesthetic that emphasizes the technical nature of the software. **Inter** is used for body copy and descriptions to maintain high legibility during extended monitoring sessions.

All labels must be high-contrast and often rendered in uppercase with increased letter spacing to mimic industrial hardware labeling. Numbers and telemetry data should always use monospaced characters to prevent layout shifting during real-time updates.

## Layout & Spacing

The layout follows a **Fluid Grid** model designed for multi-monitor command centers. Content is organized into modular "Monitoring Panels" that can scale to fit available screen real estate while maintaining a strict 4px baseline rhythm.

The UI is built on a 12-column system, but utilizes "Safe Zones" for map-based interfaces where glassmorphic overlays float at the margins. Spacing is intentionally tight to maximize information density, using 16px gutters to separate distinct data streams without wasting screen space.

## Elevation & Depth

Elevation in this design system is achieved through **Glassmorphism and Tonal Layering** rather than traditional shadows. 

1.  **Base Layer:** Midnight Blue (Solid).
2.  **Structural Layer:** Graphite (Solid or 80% opacity) used for sidebars and background panels.
3.  **Overlay Layer:** Semi-transparent Midnight Blue with a high-density backdrop blur (20px+) and a 1px Silver "micro-border" (20% opacity).
4.  **Active Layer:** Elements that require focus use a more vibrant Silver trim and higher opacity.

The "Silver Trim" is a signature element—a thin, high-contrast 1px border that gives components a machined, metallic look, separating panels from the dark background without the need for heavy shadows.

## Shapes

The shape language is strictly **Soft-Industrial**. Rectilinear forms dominate to reinforce the feeling of stability and structural integrity. A minimal border radius (4px) is applied to prevent the UI from feeling dated or hostile, but larger radii (like pills) are strictly avoided to maintain the professional, technical tone.

Buttons and input fields use the `rounded-sm` (4px) setting. "Alert" cards and major panels may use `rounded-lg` (8px) to subtly distinguish them as container-level elements.

## Components

### Buttons
Interactive elements use a "Machined" look. Primary actions are Silver with Midnight Blue text; secondary actions are outlined in Graphite with Silver text. Hover states should include a subtle "inner glow" using the Neon Green color to indicate system readiness.

### Alert Cards
High-priority components designed for immediate attention. These cards feature a thick (4px) Alert Red left-hand border, a dark glassmorphic background, and JetBrains Mono headers. In a critical state, the Silver trim should pulse with a low-opacity Red glow.

### Monitoring Panels
Data-rich containers featuring Graphite headers and Silver micro-borders. Use small, monospaced "Status Chips" (Neon Green for 'Active', Silver for 'Standby') to denote the health of individual sensors or perimeter segments.

### Map Overlays
Map-based UI elements must use the glassmorphic style with a heavy backdrop blur. This ensures that the technical telemetry data remains readable regardless of the map's satellite or topographic complexity beneath it.

### Inputs & Sliders
Inputs are dark with Silver bottom-borders only, mimicking hardware gauges. Sliders and toggles use Neon Green for 'on' states to provide a clear, high-contrast visual feedback loop for system configuration.