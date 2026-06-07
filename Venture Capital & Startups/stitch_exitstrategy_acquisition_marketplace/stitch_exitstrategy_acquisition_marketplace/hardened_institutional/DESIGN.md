---
name: Hardened Institutional
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#b1c5ff'
  on-tertiary: '#002c70'
  tertiary-container: '#001640'
  on-tertiary-container: '#507ee4'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#dae2ff'
  tertiary-fixed-dim: '#b1c5ff'
  on-tertiary-fixed: '#001946'
  on-tertiary-fixed-variant: '#00419e'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 60px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to evoke the unyielding security of a private vault and the sophisticated authority of a top-tier investment bank. Targeted at high-net-worth individuals, institutional buyers, and founders, the visual language prioritizes confidentiality and structural integrity. 

The aesthetic is defined as **Hardened Minimalism**. It moves away from soft, playful trends toward a rigid, architectural approach. It utilizes a "fortified" layout where elements feel locked into place. The integration of glassmorphism is used exclusively for blurred previews of sensitive data, acting as a functional metaphor for "confidentiality layers" rather than mere decoration. The result is a high-stakes environment that feels premium, indestructible, and absolute.

## Colors

The palette is anchored in a high-contrast, dark-mode-first execution. **Deep Blue** serves as the primary structural color, providing a sense of depth and professional calm. **Platinum Silver** is used for high-level surfaces, typography, and interactive highlights, offering a metallic, premium sheen. 

**Black** is reserved for the deepest background layers and primary containers to create a "void" effect that makes content pop. Accent colors are used sparingly, primarily for success states or high-priority calls to action, maintaining a monochromatic, institutional atmosphere.

## Typography

This design system utilizes **Inter** for all applications. The typeface is selected for its systematic, utilitarian clarity and its ability to remain legible under dense data conditions. 

The typographic hierarchy relies on heavy weight contrast rather than size alone. Display styles use tight letter-spacing and bold weights to command authority. Label styles utilize all-caps with generous tracking to signify metadata or system-level status, ensuring that secondary information feels organized and intentional.

## Layout & Spacing

The layout follows a **Fixed 12-column Grid** within a maximum container width of 1280px to maintain a focused, high-density professional experience. The rhythm is governed by an 8px base unit.

Spacing in this design system is "hardened"—meaning containers are strictly aligned with zero-tolerance for overlapping elements. Large margins are used to separate major functional areas, while tight gutters within cards and modules create a sense of data density and efficiency. Vertical stacks are used to group related information, emphasizing a clear, top-to-bottom reading path.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines**. Rather than using traditional drop shadows, which can feel too soft for a "hardened" style, depth is achieved by stacking progressively lighter shades of Deep Blue or Black.

Key techniques:
- **Subtle Borders:** Every interactive container or section is defined by a 1px solid border in a muted Platinum Silver (low opacity).
- **Glassmorphism:** Used for non-authorized content states. High-quality background blurs (32px+) create a "frosted vault" look that obscures data until a secure action is taken.
- **Structural Insets:** Use inner shadows (1px-2px) on input fields and secondary buttons to give the impression that they are machined into the interface surface.

## Shapes

The shape language is precise and engineered. We utilize a **Soft (0.25rem)** roundedness for standard UI elements. This subtle rounding prevents the interface from feeling "sharp" or hostile while maintaining the disciplined look of a high-security product. Large containers and cards may scale up to a 0.5rem radius, but never beyond. Elements like buttons and inputs should feel like solid blocks rather than fluid shapes.

## Components

### Buttons
Primary buttons are solid Platinum Silver with Black text, conveying a "master key" aesthetic. They are rectangular with a minimal 4px radius. Secondary buttons are outlined (Ghost style) with a subtle 1px border.

### Cards & Containers
Cards feature a dark background (Black or Deepest Blue) with a mandatory 1px Platinum Silver border at 15% opacity. For premium "exclusive" listings, cards should utilize a glassmorphic header with a heavy backdrop blur.

### Input Fields
Fields are dark, inset, and feature a sharp highlight on focus. The label should always use the `label-caps` style positioned above the field to maintain a structured form layout.

### Blurred Previews
A custom component for the M&A marketplace: blurred listing cards. These use a high-saturation blur with a "Secure Link" icon overlay, indicating that the data is protected by the design system's security protocols.

### Data Tables
Tables are the core of the marketplace. They utilize strict horizontal borders and alternating row fills in Deep Blue shades. No vertical borders are used, allowing the text alignment to create the visual columns.