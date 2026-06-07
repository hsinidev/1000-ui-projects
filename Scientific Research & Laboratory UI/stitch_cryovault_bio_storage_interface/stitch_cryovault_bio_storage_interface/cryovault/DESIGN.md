---
name: CryoVault
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#c1c7ce'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#303031'
  outline: '#8b9198'
  outline-variant: '#41484d'
  surface-tint: '#9accf3'
  primary: '#e1f0ff'
  on-primary: '#00344d'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#2e6385'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#ffeae8'
  on-tertiary: '#68000b'
  tertiary-container: '#ffc4bf'
  on-tertiary-container: '#b41120'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdad7'
  tertiary-fixed-dim: '#ffb3ae'
  on-tertiary-fixed: '#410004'
  on-tertiary-fixed-variant: '#930014'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
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
  data-display:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
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
  margin-mobile: 20px
---

## Brand & Style

The design system establishes a "Cold-Tech" aesthetic, engineered for the high-stakes environment of bio-banking. The brand personality is clinical, ultra-precise, and immovable, evoking the absolute stillness of cryogenic preservation. 

The visual style utilizes a refined **Glassmorphism** approach—specifically "Frost"—where UI layers appear as sheets of high-density polycarbonate or frozen glass. This is paired with **Minimalism** to ensure that critical biometric and thermal data remain the primary focus. The emotional response is one of total reliability; the user should feel that the samples are secured within a vault that is as technologically advanced as it is physically robust.

## Colors

The palette is anchored in a deep **Matte Black** to represent the void of a vacuum-sealed chamber. **Ice Blue** serves as the primary functional color, used for active states, data visualizations, and highlighting "safe" temperature zones. **Silver** provides the metallic infrastructure, used for borders and secondary iconography to simulate hardware components.

A critical tertiary **Alert Red (#FF4D4D)** is reserved exclusively for temperature deviations and hardware failures. This color should rarely appear, ensuring maximum psychological impact when it does. Metallic gradients should be subtle, moving from #C0C0C0 to #8E8E8E at a 135-degree angle to simulate brushed aluminum.

## Typography

This design system utilizes a dual-font strategy. **Space Grotesk** is used for headlines and high-priority data points (like temperature readouts) to provide a technical, futuristic edge that remains highly legible. **Inter** handles all body copy and UI labels, providing a neutral, utilitarian foundation that doesn't distract from the data.

Data points should often utilize a fixed-width feel (supported by Space Grotesk's geometric nature) to ensure that shifting numbers do not cause layout reflows during live monitoring.

## Layout & Spacing

This design system follows a **Mobile-First Fluid Grid** model. Given the precision required, the layout relies on a strict 4px baseline shift to ensure all elements align to a technical "blueprint" logic. 

On mobile, a single-column stack is preferred for sample lists, while critical metrics (Temp, Pressure, O2) are displayed in a 2x2 grid. Margins are generous (20px) to prevent accidental interactions in high-stress environments. Vertical rhythm is tight to maximize the information density necessary for scientific monitoring.

## Elevation & Depth

Depth is achieved through **Frost Glassmorphism** rather than traditional shadows. 

1.  **Base Layer:** Solid Matte Black (#1A1A1B).
2.  **Surface Layer:** Semi-transparent Ice Blue tint with a heavy backdrop blur (20px–30px) and a 1px Silver "inner glow" border to simulate the edge of a glass pane.
3.  **Active Layer:** Higher transparency with a subtle "inner shadow" to suggest the element is recessed into the interface.

Avoid ambient shadows; instead, use light-bleed effects (subtle Ice Blue outer glows) to indicate active power states or high-priority modals.

## Shapes

The shape language is **Soft (0.25rem)**. While the aesthetic is clinical, sharp 0px corners feel too aggressive and "digital," whereas slight rounding suggests high-end industrial design (like CNC-milled aluminum). 

Buttons and input containers use a 4px radius. Larger cards and "frost" panels may use 8px (rounded-lg) to distinguish between structural containers and interactive elements.

## Components

### Buttons
Primary buttons use a metallic gradient fill with Space Grotesk "Label-Caps" text. Secondary buttons are "Ghost" style with a 1px Silver border and no fill, becoming Ice Blue on hover.

### Progress & Alerts
The **Red-Pulse Animation** is a critical component. When a temperature threshold is crossed, the border of the affected card and the data readout must pulse from #FF4D4D to a 50% opacity red with a 2-second ease-in-out duration.

### Cards
Cards are the primary container for sample data. They must feature a "Frost" glass effect with a 1px Silver top-border to catch a simulated overhead light source.

### Input Fields
Inputs are recessed (inset shadow) with a Matte Black background and Ice Blue focus borders. Labels always sit above the field in "Label-Caps" typography.

### Specialized Components
*   **Thermal Sparkline:** A simplified, monochromatic line chart showing the last 24 hours of temperature stability, placed within sample list items.
*   **Cryo-Status Chip:** Small pill-shaped badges (e.g., "FROZEN", "THAWING", "STABLE") using low-saturation versions of the primary palette.