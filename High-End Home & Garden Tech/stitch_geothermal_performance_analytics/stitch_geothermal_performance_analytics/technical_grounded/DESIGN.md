---
name: Technical Grounded
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1b1b1c'
  on-surface-variant: '#434749'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#747879'
  outline-variant: '#c3c7c8'
  surface-tint: '#586062'
  primary: '#181f21'
  on-primary: '#ffffff'
  primary-container: '#2d3436'
  on-primary-container: '#959c9f'
  inverse-primary: '#c1c8ca'
  secondary: '#79573f'
  on-secondary: '#ffffff'
  secondary-container: '#ffd1b3'
  on-secondary-container: '#7a5840'
  tertiary: '#261b17'
  on-tertiary: '#ffffff'
  tertiary-container: '#3c302b'
  on-tertiary-container: '#a99790'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde4e6'
  primary-fixed-dim: '#c1c8ca'
  on-primary-fixed: '#161d1f'
  on-primary-fixed-variant: '#41484a'
  secondary-fixed: '#ffdcc6'
  secondary-fixed-dim: '#eabda0'
  on-secondary-fixed: '#2d1604'
  on-secondary-fixed-variant: '#5f402a'
  tertiary-fixed: '#f3ded7'
  tertiary-fixed-dim: '#d6c3bb'
  on-tertiary-fixed: '#241915'
  on-tertiary-fixed-variant: '#51443f'
  background: '#fcf9f8'
  on-background: '#1b1b1c'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: IBM Plex Sans
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: IBM Plex Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  mono-small:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 48px
---

## Brand & Style
The brand personality is authoritative, precise, and deeply rooted in engineering excellence. It targets high-end residential users who value data transparency and sustainable performance. The emotional response is one of confidence and reliability—mimicking the stability of the earth itself.

The visual style is **Corporate / Modern** with a **Minimalist** foundation. It prioritizes clarity over decoration, using "Technical-Grounded" principles to make complex geothermal data accessible. High-fidelity visualizations are treated like blueprints, utilizing subtle 3D depth and precise line work to convey sophistication without clutter.

## Colors
The palette is intentionally restrained to maintain a high-end, professional atmosphere. 

- **Deep Slate (#2D3436)** serves as the anchor for primary navigation, headings, and critical labels, providing strong contrast against the white canvas.
- **Earthy Brown (#6F4E37)** is used sparingly as a high-intent accent for data highlights, active states, and call-outs related to thermal energy and efficiency.
- **Pure White (#FFFFFF)** provides a crisp, clinical background that ensures generous whitespace feels intentional rather than empty.
- Neutral grays are used for secondary data and grid lines to maintain a "blueprint" aesthetic.

## Typography
The typography system uses a tri-font approach to differentiate between narrative, interface, and technical data.

- **IBM Plex Sans** is used for headlines to convey a systematic, corporate authority.
- **Inter** provides neutral, highly legible body text for reports and descriptions.
- **JetBrains Mono** is the workhorse for data readouts, coordinates, and labels, providing an "engineering-grade" feel that aligns with the technical nature of geothermal analytics. All labels should be set in this monospaced face to ensure alignment in data tables.

## Layout & Spacing
The layout follows a **Strict Fixed Grid** system based on a 12-column architecture for desktop and 4-column for mobile. Alignment is the highest priority; elements must snap to the grid to maintain a disciplined, technical appearance.

Whitespace is treated as a functional element to separate complex data clusters. Large margins (48px+) are used to frame the primary analytics dashboard, while internal spacing within modules follows a 4px baseline rhythm. Information density is managed through clear hierarchical grouping rather than compression.

## Elevation & Depth
This design system utilizes **Tonal Layers** and **Low-Contrast Outlines** rather than traditional drop shadows.

- **Surface Tiers:** Secondary data modules are housed in containers with a subtle 1px border in a light slate tint (#DFE6E9).
- **Subtle 3D Effects:** For technical diagrams (e.g., ground loop visualizations), use isometric projection with subtle gradient fills and fine-line detailing.
- **Depth:** Depth is achieved through the stacking of white surfaces on very light gray backgrounds (#F9FAFB), creating a sense of physical blueprints on an engineer's desk. High-priority components use a hairline "Deep Slate" border for emphasis.

## Shapes
To reinforce the "Technical-Grounded" aesthetic, the shape language is **Sharp (0)**. Right angles communicate precision and structural integrity. 

Avoid rounded corners on buttons, cards, and input fields. Visual interest is instead generated through the intersection of lines and the use of Earthy Brown as a high-contrast fill for interactive elements. This lack of curvature differentiates the system from consumer-grade "soft" electronics, positioning it as professional infrastructure software.

## Components
- **Buttons:** Sharp 90-degree corners. Primary buttons use Deep Slate with White text. Secondary buttons use a 1px Slate border. 
- **Data Cards:** Simple white containers with a 1px border. Labels are always top-aligned in `label-caps` typography.
- **Charts:** Use thin 1px stroke lines for axes. Data series use Earthy Brown for primary metrics and Slate for baselines.
- **Input Fields:** Bottom-border only or full 1px border. Focus state is indicated by a weight increase in the border or a switch to Earthy Brown.
- **Technical Indicators:** Small, rectangular "chips" used for status (e.g., "ACTIVE," "OPTIMIZING") using monospaced type.
- **Isometric Diagrams:** Technical representations of the geothermal heat pump and ground loops should use clean lines and 45-degree angles to represent the system's physical state.