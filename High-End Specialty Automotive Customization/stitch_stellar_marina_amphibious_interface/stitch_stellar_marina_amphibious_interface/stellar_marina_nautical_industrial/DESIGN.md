---
name: Stellar-Marina Nautical-Industrial
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#bdc9c8'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#879392'
  outline-variant: '#3e4949'
  surface-tint: '#76d6d5'
  primary: '#76d6d5'
  on-primary: '#003737'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#006a6a'
  secondary: '#b5c8df'
  on-secondary: '#203243'
  secondary-container: '#36485b'
  on-secondary-container: '#a4b7cd'
  tertiary: '#ffb5a0'
  on-tertiary: '#601400'
  tertiary-container: '#d53800'
  on-tertiary-container: '#fff8f6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#d1e4fb'
  secondary-fixed-dim: '#b5c8df'
  on-secondary-fixed: '#091d2e'
  on-secondary-fixed-variant: '#36485b'
  tertiary-fixed: '#ffdbd1'
  tertiary-fixed-dim: '#ffb5a0'
  on-tertiary-fixed: '#3b0900'
  on-tertiary-fixed-variant: '#872000'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for a high-end amphibious context, where precision instruments meet the fluidity of the ocean. It bridges the gap between heavy-duty industrial machinery and the refined elegance of luxury yachting. The aesthetic is defined as "Amphibious Industrial"—prioritizing legibility under harsh glare while maintaining a premium, "liquid" interface.

The visual style utilizes a high-contrast dark-mode baseline to reduce eye strain in marine environments, layered with glass-morphic panels that mimic the transparency of water and high-strength reinforced glass. Tactile elements are inspired by physical deck controls: heavy bezels, brushed metal textures, and clear, high-visibility status indicators.

## Colors

The palette is optimized for visibility and premium feel. 
- **Deep Teal (#008080)** serves as the core functional color, used for primary actions and "on-water" navigation states.
- **Gunmetal Gray (#2C3E50)** provides the industrial foundation, used for structural panels and deep backgrounds.
- **Safety Orange (#FF4500)** is reserved strictly for alerts, critical hazards, and safety-related telemetry, ensuring it cuts through the cooler palette.
- **Crisp White (#FFFFFF)** is used for high-contrast typography and iconography against dark backgrounds.

The "Liquid UI" effect is achieved through varying opacities of the Gunmetal Gray, layered over a deep navy-black (#0F172A) background to simulate depth.

## Typography

This design system employs a tiered typography strategy to ensure readability in vibrating or high-motion environments. **Metropolis** is used for bold, geometric headlines that command attention. **Inter** handles high-density body copy due to its exceptional legibility and neutral tone. **Space Grotesk** is utilized for technical data readouts (depth, speed, heading), providing a monospaced-adjacent feel that emphasizes engineering precision.

For mobile viewports, `display-lg` scales down to 32px to ensure full visibility without excessive scrolling, while maintaining the heavy weight.

## Layout & Spacing

The layout utilizes a **fixed-grid** system on desktop (12 columns) and a **fluid-grid** system on mobile (4 columns). Given the "Industrial" nature, spacing is generous to accommodate touch interactions in wet or moving environments. 

Margins and gutters are wider than standard consumer apps to prevent accidental taps and to create a sense of expansive luxury. All spacing is derived from an 8px base unit, ensuring a consistent rhythmic vertical flow across technical dashboards and marketing landing pages.

## Elevation & Depth

Hierarchy is established through **Glassmorphism and Material Stacking**. 
1. **Base Layer:** The "Deep Navy" solid background.
2. **Mid Layer (Glass):** UI containers use a 70% opacity Gunmetal Gray with a 20px backdrop blur and a 1px solid Teal or White border at 20% opacity. This creates the "water surface" effect.
3. **Top Layer (Tactile):** Interaction elements (buttons) use heavy inner shadows and subtle gradients to appear extruded from the glass surface.

Shadows are not used for depth; instead, depth is communicated through blur intensity and border luminosity.

## Shapes

The design system adopts a **Sharp (0)** roundedness strategy. Every container, button, and input field uses 90-degree corners to reflect heavy-duty industrial fabrication. To prevent the UI from feeling "cheap," these sharp corners are paired with hairline 1px borders and high-precision technical iconography. This rigid geometry reinforces the brand's commitment to structural integrity and engineering excellence.

## Components

**Buttons (Tactile/Rugged):**
Primary buttons feature a solid Teal fill with a subtle vertical brushed-metal gradient. They must include a "beveled" 2px bottom border in a darker shade to feel like a physical toggle. Active states should "depress" by removing the bottom border and shifting the content down by 1px.

**Inputs & Control Knobs:**
Input fields are framed by a 1px Gunmetal border. When focused, the border glows with a Teal outer shadow (5px blur). For amphibious controls, incorporate "Circular Dial" components for depth and speed adjustments.

**Cards & Panels:**
Cards utilize the glass-morphic style (backdrop blur). Headers within cards should have a subtle Teal "strike" (a 2px vertical line) to the left of the title to denote technical categorization.

**Technical Iconography:**
Icons must be "Line-Weight Heavy" (2px stroke) with open terminals. They should resemble blueprints or CAD drawings rather than soft consumer icons.

**Telemetry Chips:**
Small, high-contrast labels for data like "TEMP" or "PSI" use the `label-caps` typography and are encased in a Gunmetal box with a Safety Orange status dot when values exceed safe thresholds.