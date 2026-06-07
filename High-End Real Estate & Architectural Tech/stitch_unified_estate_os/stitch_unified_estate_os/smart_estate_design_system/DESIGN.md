---
name: Smart-Estate Design System
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
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c6c6c8'
  on-tertiary: '#2f3132'
  tertiary-container: '#17191b'
  on-tertiary-container: '#808284'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e4'
  tertiary-fixed-dim: '#c6c6c8'
  on-tertiary-fixed: '#1a1c1d'
  on-tertiary-fixed-variant: '#454749'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-xl:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is centered on a "Technical Calm" philosophy. It balances the high-stakes nature of real estate and land management with a serene, glassy aesthetic that conveys security and premium quality. The target audience is high-net-worth individuals and estate managers who require a sophisticated, data-rich environment that doesn't feel overwhelming.

The core style is **Glassmorphism**. This is executed through multi-layered translucency, high-precision silver borders, and deep background blurs. The interface should feel like a custom-machined instrument—precise, cold to the touch but visually warm, and inherently stable.

## Colors

The palette is rooted in **Midnight Blue (#0A192F)**, which serves as the infinite canvas, providing a sense of depth and security. **Silver (#C0C0C0)** is utilized exclusively for structural elements, borders, and technical accents, mimicking the look of brushed metal.

**Soft White (#F5F5F7)** is the primary ink for readability, ensuring high contrast against the dark base without the harshness of pure white. **Alert Red (#FF4C4C)** is reserved strictly for critical system failures, security breaches, or high-priority boundary disputes. All interactive states should use a subtle luminance shift rather than a hue change to maintain the monochromatic premium feel.

## Typography

This design system utilizes **Metropolis** for all primary communication to evoke a sense of architectural structure and modern precision. Headlines are tight and bold, conveying authority. 

For technical data, coordinates, and system labels, **JetBrains Mono** is employed. This monospaced secondary font reinforces the "OS" nature of the platform, signaling to the user when they are looking at raw, secure data points versus editorial content. All labels should be set in uppercase when using the monospaced font to enhance the "technical instrument" feel.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy within a fluid container. Use a 12-column grid for desktop views with a consistent 24px gutter. The layout should prioritize "data-density with breathability"—meaning while information is compact, the margins between major functional blocks (the "glass panels") are generous.

Components should be grouped into logical "zones" or panels. These panels are the primary containment unit for the OS, separated by 24px or 40px depending on the hierarchy of the information. Internal padding within glass panels should never fall below 16px (sm) to maintain the premium, airy feel.

## Elevation & Depth

Elevation is expressed through **Backdrop Blurs** and **Silver Outlines** rather than traditional drop shadows.

1.  **Base Layer:** Midnight Blue (#0A192F).
2.  **Standard Panels:** 5% Soft White fill with a 20px backdrop blur and a 1px Silver border at 20% opacity.
3.  **Raised Elements (Modals/Popovers):** 10% Soft White fill with a 40px backdrop blur and a 1px Silver border at 40% opacity. 
4.  **Interaction:** When an element is hovered, the silver border opacity should increase to 60%, creating a subtle "lit edge" effect.

Shadows, if used at all, should be extremely diffused "Ambient Occlusion" style shadows—very low opacity (10%) Midnight Blue, used only to separate overlapping glassy surfaces.

## Shapes

The shape language is **Rounded**, utilizing a 0.5rem (8px) base radius. This softens the technical edges of the Midnight Blue and Silver, making the "OS" feel approachable and modern rather than cold and industrial.

- **Buttons & Inputs:** 8px (0.5rem)
- **Primary Panels/Cards:** 16px (1rem)
- **Large Container/Outer Wrappers:** 24px (1.5rem)

The consistency of these radii is vital to maintaining the "machined" look of the interface. Avoid "pill" shapes for buttons to stay within the structured, architectural theme.

## Components

**Buttons:**
Primary buttons should feature a semi-transparent Soft White fill (15%) with a high-contrast 1px Silver border. Text should be uppercase JetBrains Mono. Hover states involve a subtle inner glow or increasing the backdrop blur intensity.

**Input Fields:**
Fields are defined by their bottom border (Silver, 40% opacity) rather than a full box, or a very faint glassy container. The focus state should illuminate the entire border to 80% Silver.

**Cards & Panels:**
The "Glass Panel" is the fundamental unit. Every card must have a `backdrop-filter: blur(20px)` and a `border: 1px solid rgba(192, 192, 192, 0.2)`. 

**Chips/Tags:**
Used for land status (e.g., "Zoned," "Secured"). These should be small, monospaced, and use a 1px border with no background fill to keep the interface light.

**Security Indicators:**
A specific component class for "Encrypted" or "Secure" status, featuring a small Silver shield icon and JetBrains Mono text, placed in the top right of panels to constantly reassure the user of the system's integrity.

**Data Maps:**
Maps and land visualizations should be desaturated to fit the Midnight Blue palette, using Silver lines for boundaries and Alert Red only for contested areas.