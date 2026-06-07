---
name: Fluid-Tech
colors:
  surface: '#081425'
  surface-dim: '#081425'
  surface-bright: '#2f3a4c'
  surface-container-lowest: '#040e1f'
  surface-container-low: '#111c2d'
  surface-container: '#152031'
  surface-container-high: '#1f2a3c'
  surface-container-highest: '#2a3548'
  on-surface: '#d8e3fb'
  on-surface-variant: '#bdc8d2'
  inverse-surface: '#d8e3fb'
  inverse-on-surface: '#263143'
  outline: '#87929b'
  outline-variant: '#3d4850'
  surface-tint: '#81cfff'
  primary: '#8ad2ff'
  on-primary: '#00344b'
  primary-container: '#00baff'
  on-primary-container: '#004764'
  inverse-primary: '#00658d'
  secondary: '#b9c8de'
  on-secondary: '#233143'
  secondary-container: '#39485a'
  on-secondary-container: '#a7b6cc'
  tertiary: '#52e2a6'
  on-tertiary: '#003824'
  tertiary-container: '#2bc58c'
  on-tertiary-container: '#004c32'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c6e7ff'
  primary-fixed-dim: '#81cfff'
  on-primary-fixed: '#001e2d'
  on-primary-fixed-variant: '#004c6b'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#081425'
  on-background: '#d8e3fb'
  surface-variant: '#2a3548'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
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
  code-sm:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter-mobile: 16px
  gutter-desktop: 24px
  margin-safe: 20px
  stack-compact: 8px
  stack-loose: 24px
---

## Brand & Style

This design system is engineered for the high-velocity world of DevOps. It prioritizes technical precision and engineering excellence, evoking an emotional response of competence, reliability, and speed. The visual narrative is built around "momentum"—the idea that cloud infrastructure is a living, flowing system rather than a static stack.

The aesthetic blends **Minimalism** with sophisticated **Glassmorphism**. By using transparent layers and blurred backdrops, the UI suggests depth and complex architecture without sacrificing clarity. "Node-Based" visual patterns—thin connecting lines and dot-grid backgrounds—are utilized to reinforce the mental model of networked systems and infrastructure topology.

## Colors

The color palette is anchored in a deep **Graphite** environment to reduce eye strain during long engineering sessions. **Sky Blue** serves as the primary action color, used strategically for "deployment" triggers and primary navigation. **Silver** provides a neutral secondary layer, used for structural borders and secondary text to maintain a clean, metallic finish.

Functional colors are critical for system status:
- **Success/Uptime:** Vibrant Emerald, indicating healthy clusters.
- **Warning/Latency:** Amber, used for resource pressure.
- **Critical/Incident:** Crimson, reserved for deployment failures and high-priority alerts.

## Typography

This design system utilizes a dual-font strategy to balance legibility with a technical "hacker" aesthetic. **Space Grotesk** is used for headlines and data labels, providing a geometric, futuristic feel that aligns with modern infrastructure tools. **Inter** is the workhorse for all body copy and technical documentation, chosen for its exceptional readability on mobile devices.

Technical data, CLI snippets, and log outputs must always use a monospaced font. All labels for system metrics should be rendered in uppercase with slight tracking (letter-spacing) to mimic industrial equipment readouts.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model optimized for high-density information. Given the mobile-first requirement, the system uses a compact 4px baseline grid to ensure that technical dashboards remain functional on smaller screens.

Layouts should favor a vertical stack on mobile, transitioning to a multi-column dashboard on desktop. Use "compact" spacing for data tables and logs to maximize information density, and "loose" spacing for educational content and documentation to improve focus.

## Elevation & Depth

Depth in this design system is communicated through **Tonal Layering** and **Glassmorphism** rather than traditional heavy shadows. 

1.  **Base Layer:** The Graphite background, often textured with a subtle node-link pattern or dot grid.
2.  **Surface Layer:** Slightly lighter than the base, used for cards and main content areas.
3.  **Overlay Layer:** Use a semi-transparent Sky Blue or Silver tint with a `backdrop-filter: blur(12px)`. This is reserved for modals, navigation bars, and "sticky" status indicators.
4.  **Interaction Layer:** Thin, 1px high-contrast borders (Sky Blue) signify active or focused states, simulating the "glow" of a live circuit.

## Shapes

The shape language is "Soft-Technical." A low roundedness (0.25rem) is applied to buttons and input fields to maintain a professional, precise appearance. Sharp 90-degree corners should be avoided as they feel dated; however, excessively round "pill" shapes are also avoided as they appear too consumer-oriented. 

Status indicators (uptime pips) and node connectors should be perfect circles to contrast against the rectangular structure of the dashboard containers.

## Components

### Buttons
Primary buttons use a Sky Blue fill with white or deep graphite text. Secondary buttons are "Ghost" style with a Silver border. All buttons should have a subtle inner glow on hover to simulate "powering up."

### Uptime Gauges & Status Indicators
Status is visualized through "Pulsing Pips." A green pulse indicates a healthy deployment. Deployment progress is shown via a thin, high-contrast loading bar that spans the top of the card or the entire viewport.

### Cards & Glass Overlays
Cards use a subtle 1px border in a Silver tint with a low-opacity fill. When stacked, the background blur of the top layer should clearly distinguish it from the content beneath.

### Code Blocks
Code snippets must feature syntax highlighting using a "Neon-Dark" theme. These blocks should include a "Copy to Clipboard" shortcut and a "Line Number" toggle to assist in technical troubleshooting.

### Node-Based Visuals
In dashboards, use thin (0.5px) Silver lines to connect related data points or to show the flow between a "Source" and a "Destination" in a deployment pipeline.