---
name: DataMastery
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
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#e7bf99'
  on-tertiary: '#432b10'
  tertiary-container: '#281400'
  on-tertiary-container: '#9d7b5a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#e7bf99'
  on-tertiary-fixed: '#2b1701'
  on-tertiary-fixed-variant: '#5d4124'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  grid-gutter: 1px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-performance learning environments, targeting data scientists and AI engineers who value precision, density, and technical rigor. The aesthetic is "Industrial Tech"—a blend of brutalist structural clarity and modern corporate reliability. It evokes the feeling of a sophisticated IDE or a high-frequency trading terminal, signaling authority and deep expertise.

The visual style utilizes a high-contrast dark mode foundation. It relies on structural lines, micro-topography, and data-dense layouts to communicate a "system-first" philosophy. Design elements are treated as modules within a larger machine, emphasizing logic over decoration.

## Colors

The palette is anchored by **Deep Navy**, providing a low-strain, high-focus background for long-form technical work. **Electric Indigo** serves as the primary action color, injecting high-energy technicality into interactive elements. 

**Crisp White** is reserved for primary content and data values to ensure maximum legibility against the dark background. The semantic palette utilizes a specialized "Matrix Green" (Success) and "Terminal Red" (Error) to maintain the industrial aesthetic. Subtle grays are used exclusively for structural elements like grid lines, dividers, and inactive states to keep the visual hierarchy focused on the data.

## Typography

This design system employs a dual-font strategy. **Space Grotesk** is used for headlines and technical data values; its geometric, monospaced-leaning construction reinforces the scientific nature of the content. **Inter** is used for all UI labels and body copy to ensure maximum readability during intense study sessions.

All data values, timestamps, and code snippets must be rendered in the mono-variant of the headline font to distinguish "system output" from "instructional narrative."

## Layout & Spacing

The layout philosophy follows a **Fixed-Modular Grid**. Content is housed in "Cells" defined by 1px borders rather than negative space. This creates a blueprint-like appearance. 

A strict 4px base unit governs all dimensions. Use a 12-column grid for page-level layouts, but utilize nested flexbox containers for data density. Gutters are intentionally narrow (1px to 8px) to maximize the amount of information visible on screen, reflecting the "Data-Dense" requirement.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Structural Outlines** rather than traditional shadows.
- **Level 0 (Floor):** Deep Navy (#0A192F).
- **Level 1 (Cards/Panels):** Neutral Base (#112240) with a 1px border (#233554).
- **Level 2 (Popovers/Tooltips):** Electric Indigo accents on the top border to indicate activity.

Backgrounds may feature a subtle 32px x 32px dot-grid pattern in a low-opacity gray to provide a "technical canvas" feel. Interactive elements use a subtle inner-glow when hovered, simulating a backlit hardware button.

## Shapes

The design system utilizes **Sharp Corners (0px)** for all primary UI components, including buttons, input fields, and cards. This reinforces the industrial, precise nature of data science. 

Small border radii (max 2px) are permitted only for nested status tags or micro-chips to prevent visual vibrating when many small elements are grouped together.

## Components

### Buttons & Inputs
- **Primary Action:** Solid Electric Indigo with Crisp White text. Use a "cut-corner" hover effect or a 1px solid border offset.
- **Ghost Input:** Transparent background with 1px border. On focus, the border glows Electric Indigo.

### Data Visualization
- **Sparklines:** Use high-contrast lines (Electric Indigo or Success Green) without axes for inline trend indicators.
- **Spider Charts:** Use semi-transparent Indigo fills with 1px stroke weight for multivariate analysis.
- **Data Grids:** Use 1px borders for every cell. Header rows should have a slightly darker background than body rows.

### Technical Cards
- Cards must include a "Header" section containing a title and a mono-spaced ID or timestamp. 
- Use "Code-Motif" icons (brackets, slashes, dots) to categorize content types.

### Status Indicators
- Use small, square "LED" indicators. A solid color square represents an active state; an outlined square represents an inactive state.