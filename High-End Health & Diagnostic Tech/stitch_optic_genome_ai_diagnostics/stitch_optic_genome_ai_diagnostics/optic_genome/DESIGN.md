---
name: Optic-Genome
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
  on-surface-variant: '#424654'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737785'
  outline-variant: '#c3c6d6'
  surface-tint: '#0657ce'
  primary: '#003f9c'
  on-primary: '#ffffff'
  primary-container: '#0055cc'
  on-primary-container: '#c8d5ff'
  inverse-primary: '#b1c5ff'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#2a4478'
  on-tertiary: '#ffffff'
  tertiary-container: '#435c91'
  on-tertiary-container: '#c7d6ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001947'
  on-primary-fixed-variant: '#00419f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#d9e2ff'
  tertiary-fixed-dim: '#afc6ff'
  on-tertiary-fixed: '#001943'
  on-tertiary-fixed-variant: '#2c4579'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
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
    letterSpacing: '0'
  data-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  button-text:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The visual identity of this design system is rooted in the precision of ophthalmology and the clarity of advanced genomic sequencing. It targets medical professionals, laboratory technicians, and clinical researchers who require high-density data visualization without cognitive fatigue. 

The aesthetic is **Clinical Modernism**: a fusion of sterile, high-tech environments and sophisticated digital interfaces. The atmosphere is quiet, focused, and authoritative. By utilizing heavy whitespace and a strictly controlled color palette, the system evokes the feeling of looking through a high-end surgical microscope—crisp, illuminated, and undistorted. Every element is intentional, removing visual noise to prioritize diagnostic accuracy and professional trust.

## Colors

The color strategy uses a **High-Key** approach to maintain a "Sterile White" environment. 

- **Medical Blue (#0055CC)** is the primary driver for action and focus, representing scientific reliability.
- **Deep Navy (#002255)** is reserved for high-contrast typography and navigational headers to ground the layout.
- **Sleek Silver (#C0C0C0)** and lighter slate tones provide structural definition for borders and inactive states, mimicking the brushed metal of medical hardware.
- **Sterile White (#FFFFFF)** is the dominant background color to ensure maximum "optical clarity" and to make data visualizations pop.

Functional colors for alerts (Red/Green) are slightly desaturated to maintain the professional, medical-grade tone while ensuring immediate legibility against the white backdrop.

## Typography

This design system utilizes a multi-font approach to balance geometric precision with functional readability.

- **Metropolis** is used for headlines and UI controls. Its geometric structure feels engineered and modern, providing the "high-tech" foundation.
- **Inter** handles all body copy and complex descriptive text. Its high x-height and neutral tone ensure legibility in dense clinical reports.
- **JetBrains Mono** is introduced for data points, genomic coordinates, and timestamps. The monospaced nature emphasizes the "data-driven" and "precise" requirements of the system.

All text should be rendered with optimized legibility settings (antialiasing enabled) and maintain generous line heights to prevent visual crowding in data-heavy screens.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid** model. Diagnostic viewers and data dashboards use a fluid grid to maximize screen real estate, while documentation and settings use a centered fixed grid for focus.

A 12-column grid is standard, utilizing a strict **8px base unit** for all spacing. 
- **Spacious Layout:** Horizontal margins are generous (32px+) to prevent the interface from feeling "cramped" like legacy medical software.
- **Geometric Patterns:** Content blocks should be separated by clear, 1px silver borders rather than excessive gaps, creating a "technical blueprint" aesthetic.
- **Information Density:** While the layout is spacious, internal component padding is tight (sm/md) to allow for the display of high-resolution ocular scans and multi-variant genomic lists.

## Elevation & Depth

To maintain the "Optical-Clear" aesthetic, this design system eschews heavy shadows in favor of **Tonal Layering** and **Crisp Borders**.

- **Depth through Borders:** 1px borders in `#E2E8F0` or `#C0C0C0` define surfaces. 
- **Surface Tiers:** The base background is white. Secondary containers use a very subtle cool-grey tint (#F8FAFC) to sit "behind" primary cards.
- **Focused Elevation:** Only active modals or critical popovers utilize an "Ambient Shadow"—a very soft, highly diffused blue-tinted shadow (e.g., `0px 10px 30px rgba(0, 85, 204, 0.08)`) to suggest a slight lift without breaking the sterile, flat aesthetic.
- **Backdrop Blurs:** When overlays are present, use a 12px backdrop blur on the underlying content to simulate the look of looking through frosted medical glass.

## Shapes

The shape language is strictly **Geometric and Sharp**. 

- **0px Corner Radius:** All primary containers, buttons, and input fields must have sharp, 90-degree corners. This reinforces the feeling of precision, accuracy, and "medical-grade" engineering.
- **Hairline Strokes:** Use 1px or 1.5px strokes for all icons and borders. Avoid thick or "friendly" rounded shapes.
- **Functional Geometry:** Use 45-degree angles sparingly in decorative UI patterns (such as corner accents on scan frames) to emphasize the high-tech, diagnostic nature of the tool.

## Components

- **Buttons:** Sharp-edged with solid Medical Blue backgrounds for primary actions. Ghost buttons with 1px Silver borders for secondary actions. Use uppercase text for high-level "System" actions (e.g., "START SCAN").
- **Data Cards:** White backgrounds, sharp corners, and a 1px border. Top headers of cards should have a subtle 4px vertical blue accent bar on the left to indicate importance.
- **Inputs:** Simple bottom-border or 4-sided 1px border. Focus state changes the border color to Medical Blue and adds a subtle 1px internal glow. Use monospaced font for numeric inputs.
- **Status Chips:** Small, rectangular badges with light background tints and matching text colors. No rounding.
- **Diagnostic Viewer:** A specialized component with a deep navy or black background to house ocular imaging, surrounded by silver technical calipers and measurement readouts.
- **Progress Indicators:** Linear, thin bars using high-contrast blue against a silver track. Avoid circular "spinners" in favor of "System Loading" bars to maintain the technical aesthetic.