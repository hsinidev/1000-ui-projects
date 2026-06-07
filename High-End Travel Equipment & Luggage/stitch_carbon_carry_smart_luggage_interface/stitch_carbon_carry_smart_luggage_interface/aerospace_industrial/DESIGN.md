---
name: Aerospace Industrial
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
  on-surface-variant: '#c4c7c8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c6'
  primary: '#ffffff'
  on-primary: '#2f3131'
  primary-container: '#e2e2e2'
  on-primary-container: '#636465'
  inverse-primary: '#5d5f5f'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#fffffb'
  on-tertiary: '#003920'
  tertiary-container: '#4dffab'
  on-tertiary-container: '#007347'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#52ffac'
  tertiary-fixed-dim: '#00e290'
  on-tertiary-fixed: '#002111'
  on-tertiary-fixed-variant: '#005231'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1280px
---

## Brand & Style

This design system is engineered to evoke the high-stakes precision of aerospace engineering and the rugged durability of carbon-fiber manufacturing. It targets a demographic that values mechanical integrity, performance metrics, and industrial luxury. The emotional response is one of "Technical Authority"—the UI feels like a diagnostic interface for a high-performance aircraft.

The design style is a synthesis of **Brutalism** and **Tactile Minimalism**. It utilizes raw, unrefined structural elements—like heavy borders and visible grid lines—balanced with sophisticated textures and high-contrast precision. Backgrounds feature subtle technical schematics and blueprint overlays that suggest every pixel has been calculated for structural stability.

## Colors

The palette is anchored in deep, Matte Black and structural Silvers. 
- **Primary (Silver):** Used for primary text, iconography, and active structural borders to simulate machined aluminum.
- **Secondary (Matte Black):** The base surface color, providing a non-reflective, high-performance feel.
- **Tertiary (Signal Green):** A high-visibility accent used sparingly for status indicators, data points, and "active" mission-critical states, reminiscent of radar or night-vision HUDs.
- **Neutral:** Shades of "Carbon" (dark grays with woven texture overlays) define different container levels.

Apply a 5% opacity "Blueprint Blue" or "Tech White" grid pattern over the base Matte Black to reinforce the industrial aesthetic.

## Typography

This design system utilizes a high-contrast typographic pairing to distinguish between "Technical Data" and "Operational Guidance." 

**Space Grotesk** is used for all headers, labels, and data readouts. It provides a geometric, mono-spaced feel that suggests computerized output and industrial marking. Headers should often be paired with serial numbers or "Part IDs" in smaller caps.

**Inter** handles the body copy. Its neutral, utilitarian clarity ensures high legibility against complex background textures. It provides the "high-performance" feel required for lengthy technical specifications or product descriptions.

## Layout & Spacing

The layout follows a **Fixed Grid** model based on a rigorous 4px baseline. All components must align to a 12-column structure with visible, high-contrast gutters that mimic technical drawings.

Margins are generous to prevent the dense "carbon" textures from feeling claustrophobic. Use "Technical Drawing Frames"—thin 1px silver lines that define the safe area of the screen, with coordinate markers (A1, B2, etc.) in the corners to enhance the aerospace blueprint aesthetic.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. Shadows are strictly prohibited to maintain the "flat" industrial print feel.

1.  **Floor:** Matte Black base with a subtle technical grid pattern.
2.  **Chassis:** Carbon Fiber textures for primary containers, defined by 1px Silver borders.
3.  **Components:** Elements that sit on the chassis use a slightly lighter matte gray or semi-transparent "glass" to indicate interactivity.
4.  **Overlays:** Technical "Blueprint" overlays (HUD-style) use additive blending modes to appear as if projected onto the surface.

## Shapes

The shape language is **Sharp (0)**. In the world of industrial aerospace, "rounded" is often synonymous with "soft." To project durability and precision, all containers, buttons, and input fields utilize 90-degree angles. 

Occasional "clipped corners" (45-degree chamfers) may be used on primary action buttons or decorative elements to mimic machined parts or heavy-duty casing.

## Components

*   **Buttons:** Rectangular with 1px silver borders. Primary buttons use a Silver background with Black text. Secondary buttons use a transparent background with a Silver border. Hover states should trigger a "Signal Green" glow or a shift in the background texture.
*   **Chips:** Styled as "Service Tags" or "Part Labels." Use small, uppercase mono-spaced text inside a border, often accompanied by a small "dot" status indicator.
*   **Lists:** Divided by 1px horizontal lines. Each list item should begin with a numerical index (e.g., 01, 02, 03) in a smaller font size.
*   **Input Fields:** Ghost-style inputs with only a bottom border or a full 1px border. The cursor should be a solid block rather than a line to reinforce the terminal aesthetic.
*   **Cards:** Use a subtle Carbon Fiber texture background. Include "Technical Metadata" in the top right corner of every card (e.g., weight, material grade, or serial number).
*   **Telemetry Gauges:** Custom components that display data (like battery life or luggage weight) using linear bar graphs rather than circular charts, maintaining the blueprint aesthetic.