---
name: Fluid-Tech Security
colors:
  surface: '#101416'
  surface-dim: '#101416'
  surface-bright: '#363a3c'
  surface-container-lowest: '#0b0f11'
  surface-container-low: '#181c1e'
  surface-container: '#1c2023'
  surface-container-high: '#262b2d'
  surface-container-highest: '#313538'
  on-surface: '#e0e3e6'
  on-surface-variant: '#cdc3d2'
  inverse-surface: '#e0e3e6'
  inverse-on-surface: '#2d3133'
  outline: '#968e9b'
  outline-variant: '#4b4450'
  surface-tint: '#d9b9ff'
  primary: '#d9b9ff'
  on-primary: '#421871'
  primary-container: '#7851a9'
  on-primary-container: '#eddbff'
  inverse-primary: '#724ba3'
  secondary: '#ffffff'
  on-secondary: '#003737'
  secondary-container: '#00fbfb'
  on-secondary-container: '#007070'
  tertiary: '#bfc2fb'
  on-tertiary: '#282c5b'
  tertiary-container: '#5d6093'
  on-tertiary-container: '#dfdfff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#eedbff'
  primary-fixed-dim: '#d9b9ff'
  on-primary-fixed: '#2a0054'
  on-primary-fixed-variant: '#593289'
  secondary-fixed: '#00fbfb'
  secondary-fixed-dim: '#00dddd'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#e0e0ff'
  tertiary-fixed-dim: '#bfc2fb'
  on-tertiary-fixed: '#131645'
  on-tertiary-fixed-variant: '#3f4273'
  background: '#101416'
  on-background: '#e0e3e6'
  surface-variant: '#313538'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  code:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 32px
  gutter: 24px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  glass-padding: 24px
---

## Brand & Style

This design system is built upon a "Fluid-Tech" aesthetic, specifically tailored for the high-stakes environment of Cloud Security Posture Management (CSPM). The brand personality is authoritative yet visionary, combining the impenetrable nature of deep-space security with the fluid, dynamic nature of cloud infrastructure. 

The visual style leverages **Glassmorphism** to represent transparency and insight into complex data. By utilizing translucent layers and vibrant background blurs, the UI suggests a multi-dimensional workspace where security professionals can see "through" the data to find vulnerabilities. The emotional response is one of sophisticated control, high-tech precision, and unwavering reliability.

## Colors

The palette for this design system is anchored in **Deep Navy (#000033)**, providing a vast, stable foundation that evokes the depth of the cloud. **Royal Purple (#7851A9)** serves as the primary brand driver, used for primary actions and key brand moments to signify premium security and intelligence.

**Glass-Cyan (#00FFFF)** is the secondary accent, utilized as a high-energy neon highlight for interactive elements, status indicators, and data visualizations. This color should be used sparingly to maintain its "glow" effect against the dark background. Functional colors for alerts and statuses are tuned to a neon spectrum to ensure high visibility against the translucent glass layers.

## Typography

The typography system balances technical precision with modern readability. **Space Grotesk** is used for headlines and labels; its geometric and slightly futuristic letterforms reinforce the high-tech narrative and provide a clear hierarchy for technical data points.

**Inter** is the primary body face, chosen for its exceptional legibility at small sizes and its systematic, neutral tone. This ensures that long-form security logs and policy descriptions remain readable. For technical data and status labels, a heavier weight of Space Grotesk in all-caps is preferred to create a distinct "instrument panel" feel.

## Layout & Spacing

The layout utilizes a **fluid grid** model to accommodate the vast amount of data inherent in CSPM workflows. The system is built on an 8px base unit, ensuring a consistent rhythm across all components.

Containers should maintain generous internal padding (24px) to allow the glassmorphic background blurs to feel airy and unobstructed. Layouts should prioritize a "Dashboard-as-a-Service" feel, where information density is high but clearly segmented by the structural hierarchy of glassy containers and wide gutters.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional shadows. Hierarchy is established by the stacking of semi-transparent layers.

1.  **Level 1 (Base):** Deep Navy background with subtle radial gradients of Royal Purple.
2.  **Level 2 (Panels):** Translucent surfaces with a 10px backdrop blur and a 1px solid border (White at 10% opacity) to define edges.
3.  **Level 3 (Modals/Popovers):** Higher opacity blurs (20px+) with a subtle inner glow on the top edge to simulate light hitting the glass.
4.  **Accent Depth:** Status indicators and critical nodes use a "Neon Glow" effect, employing a soft outer shadow using the secondary color (Cyan) to make them appear as if they are floating above the glass surfaces.

## Shapes

The design system employs a **Rounded (Level 2)** shape language. This level of roundedness (0.5rem base) softens the technical intensity of the data, making the platform feel approachable and modern. 

- **Cards and Panels:** 1rem (rounded-lg) to create a soft, containerized look.
- **Buttons and Inputs:** 0.5rem (rounded) for a crisp, professional appearance.
- **Status Chips:** Pill-shaped (rounded-full) to distinguish them from interactive buttons.
- **Connection Lines:** All 3D connection lines in network graphs should utilize "S-curve" paths rather than hard angles to reinforce the "Fluid" aspect of the aesthetic.

## Components

### Glassy Cards
The primary container for all data. Cards feature a 15% opacity white fill, 15px backdrop-blur, and a subtle Cyan border for active or "high-priority" states. Headers within cards should be separated by a 1px low-opacity divider.

### Buttons
- **Primary:** Solid Royal Purple with a slight Glass-Cyan outer glow on hover.
- **Secondary/Ghost:** Transparent with a Glass-Cyan border and text.
- **Actionable Icons:** Small Cyan glows behind icons to indicate interactivity.

### Status Indicators & Chips
Status indicators use neon-functional colors. A "Critical" status is not just red; it is a glowing neon red with a pulse animation to draw immediate attention.

### 3D Connection Lines
For cloud topology maps, use 2px lines with a gradient stroke (Purple to Cyan). These lines should feature "data packets" (small glowing dots) moving along the paths to visualize traffic flow and connectivity.

### Technical Data Tables
Tables should forgo heavy vertical borders. Instead, use alternating row opacities and "Glass-Cyan" highlights for row hover states. Column headers should use the Label-MD typography style for maximum clarity.

### Input Fields
Inputs are dark with a 1px Royal Purple border. Upon focus, the border transitions to Glass-Cyan with a subtle 4px outer glow, giving the impression of the field "powering on."