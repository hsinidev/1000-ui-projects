---
name: Aura-Atelier
colors:
  surface: '#f4fafd'
  surface-dim: '#d4dbdd'
  surface-bright: '#f4fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef5f7'
  surface-container: '#e8eff1'
  surface-container-high: '#e2e9ec'
  surface-container-highest: '#dde4e6'
  on-surface: '#161d1f'
  on-surface-variant: '#4b463d'
  inverse-surface: '#2b3234'
  inverse-on-surface: '#ebf2f4'
  outline: '#7d766c'
  outline-variant: '#cec5ba'
  surface-tint: '#685d4a'
  primary: '#685d4a'
  on-primary: '#ffffff'
  primary-container: '#f7e7ce'
  on-primary-container: '#726753'
  inverse-primary: '#d3c5ad'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#5d5e64'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e8ef'
  on-tertiary-container: '#66686e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0e0c8'
  primary-fixed-dim: '#d3c5ad'
  on-primary-fixed: '#221b0b'
  on-primary-fixed-variant: '#4f4533'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e2e2e9'
  tertiary-fixed-dim: '#c5c6cd'
  on-tertiary-fixed: '#191c20'
  on-tertiary-fixed-variant: '#45474c'
  background: '#f4fafd'
  on-background: '#161d1f'
  surface-variant: '#dde4e6'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  button-text:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
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
  container-max: 1440px
  gutter: 32px
  margin-desktop: 64px
  margin-mobile: 20px
  stack-lg: 48px
  stack-md: 24px
  stack-sm: 12px
---

## Brand & Style

This design system embodies an **Architectural-Luxe** aesthetic, specifically tailored for the precision and exclusivity of a luxury factory-customization program. The brand personality is one of curated mastery—where bespoke engineering meets high-fashion editorial. The UI must evoke a sense of "quiet luxury," prioritizing clarity and material honesty over decorative excess.

The design style is a sophisticated hybrid of **Minimalism** and **Glassmorphism**. It utilizes expansive whitespace to create an "airy" atmosphere, suggesting room for thought and creative expression. High-performance components are rendered with tactile precision, using subtle shadows and frosted glass (backdrop blurs) to simulate physical layers of silk-finished metal and architectural glazing. The emotional response should be one of calm confidence, professional rigor, and undisputed quality.

## Colors

The palette is anchored by **Soft Champagne**, used as a highlight to signify premium customization points and primary actions. **Slate** provides the structural "architectural" weight, used for secondary elements and borders to ground the ethereal nature of the lighter tones. **Silk White** serves as the primary canvas, providing a crisp, high-contrast background that feels cleaner than a standard white.

For text and deep structural elements, a darkened variant of Slate is used to maintain high legibility and contrast against the champagne and silk surfaces. Transparent variants of these colors are utilized for frosted glass effects, ensuring that the interface feels layered and multi-dimensional without becoming visually cluttered.

## Typography

This design system employs a high-contrast typographic pairing to reinforce the architectural-luxe narrative. **Playfair Display** is reserved for headlines and editorial moments, conveying a heritage-rich, sophisticated tone. Large display sizes should use tighter letter-spacing to appear more structural and "locked-in."

**Inter** serves as the utilitarian workhorse for the UI. It provides the necessary "high-performance" feel—precise, neutral, and highly legible at small scales. To maintain the premium aesthetic, UI labels and small metadata should often be set in uppercase with increased letter-spacing, mimicking the engravings found on luxury machinery and factory plates.

## Layout & Spacing

The layout philosophy follows a **fixed grid** model for desktop to ensure a curated, "gallery-like" presentation that doesn't overstretch on ultra-wide monitors. A 12-column grid is used with generous 32px gutters, allowing content to breathe and preventing the dense feel of typical configuration tools.

On mobile devices, the margins tighten significantly to 20px, but vertical "stack" spacing remains generous to maintain the airy feel. Components should be grouped into logical "zones" separated by significant whitespace (the `stack-lg` unit), treating each section of the customization process as its own architectural floor.

## Elevation & Depth

Hierarchy is established through **Backdrop Blurs** and **Ambient Shadows**. This design system avoids heavy drop shadows in favor of "Soft Depth."

1.  **Base Layer:** Silk White (#F8F8FF) solid background.
2.  **Middling Layer (The Workbench):** Semi-transparent white surfaces (80% opacity) with a 20px backdrop blur. This creates the frosted glass effect for sidebars and floating configuration panels.
3.  **Raised Layer (Tactile Elements):** Elements like active cards or buttons use a very diffused, Slate-tinted shadow (`box-shadow: 0 10px 30px rgba(112, 128, 144, 0.08)`).
4.  **Interactive State:** Upon hover or interaction, elements should appear to "seat" themselves or slightly elevate further, mimicking the mechanical precision of high-end switchgear.

## Shapes

The shape language is disciplined and geometric. A **Soft (0.25rem)** base roundedness is applied to standard UI elements like inputs and buttons, providing just enough approachability without losing the "architectural" edge. 

Large containers and cards utilize `rounded-lg` (0.5rem) to soften the overall composition of the page. Sharp corners (0px) are reserved for dividers and purely decorative architectural lines to maintain a sense of structural rigidity. The goal is to avoid "bubbly" shapes, leaning instead toward the refined corners of machined components.

## Components

### Buttons
Primary buttons use the Soft Champagne fill with Slate text, using a subtle inner-glow to feel tactile. Secondary buttons are "ghost" style with a 1px Slate border. All buttons use a transition that mimics a mechanical press (slight scale down to 0.98).

### Cards & Configuration Modules
Cards should utilize the frosted glass effect. They feature a 1px border in Silk White (at 50% opacity) to catch the light on the "edges" of the glass. Headers within cards use `label-caps` for a technical, serialized look.

### Input Fields
Inputs are minimal, featuring only a bottom border in Slate by default. When focused, the border transitions to Soft Champagne, and a very light champagne tint fills the background. This ensures the user feels the "active" state of the factory customization.

### Customization Steppers
A high-performance stepper component is essential. Use thin Slate lines and small serif numbers (Playfair) to track progress. The active step is highlighted by a Soft Champagne circle.

### Frosted Overlays
Modals and drawers must use heavy backdrop blurs (24px+) to keep the factory/product visible in the background, maintaining context while focusing on the specific customization task.