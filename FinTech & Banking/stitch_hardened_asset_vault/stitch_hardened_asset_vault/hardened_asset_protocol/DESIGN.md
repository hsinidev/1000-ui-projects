---
name: Hardened Asset Protocol
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#343535'
  on-surface: '#e4e2e2'
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e4e2e2'
  inverse-on-surface: '#303030'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#afc8f0'
  on-secondary: '#163152'
  secondary-container: '#2f486a'
  on-secondary-container: '#9eb7de'
  tertiary: '#ffffff'
  on-tertiary: '#303030'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#646464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#d4e3ff'
  secondary-fixed-dim: '#afc8f0'
  on-secondary-fixed: '#001c3a'
  on-secondary-fixed-variant: '#2f486a'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#131314'
  on-background: '#e4e2e2'
  surface-variant: '#343535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  monospace-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-padding: 20px
  stack-gap: 12px
  section-margin: 32px
  border-width-thin: 1px
  border-width-thick: 3px
  armored-inset: 4px
---

## Brand & Style

The design system is built on the principles of "Defensive Architecture." It targets high-net-worth individuals and institutional custodians who require a visual assurance of impenetrability. The aesthetic is a hybrid of **Brutalism** and **Tactile Industrialism**, mimicking the physical properties of a high-security bank vault or a military command console.

The emotional response is one of absolute permanence and unyielding security. Every UI element is designed to feel heavy, structural, and "bolted down." The style utilizes thick structural borders, high-contrast readability, and a mechanical interface logic that prioritizes clarity over ornamentation. "Armored" containers feature double-stroke borders and inset bevels to simulate reinforced plating.

## Colors

The palette is restricted to a high-contrast, "Cold Metal" scheme. **Platinum Silver** serves as the primary action and highlight color, providing a metallic sheen against the abyssal **Black** background. **Deep Blue** is utilized for structural depth and secondary surfaces, creating a "low-light" tactical environment.

Functional colors (Success/Error) bypass the primary palette for maximum visibility, utilizing high-chroma variants to signal system status. Metallic gradients should be applied sparingly, using a linear transition from `#B0AFC0` to `#E5E4E2` at a 45-degree angle to simulate brushed steel on primary interactive surfaces.

## Typography

This design system employs a dual-typeface strategy. **Space Grotesk** is used for all headings, labels, and technical data displays; its geometric, futuristic construction reinforces the "Hardened" aesthetic. **Inter** is reserved for long-form body copy to ensure legibility within dense technical documentation.

For asset balances, transaction hashes, and log entries, use the `monospace-data` style. All tactical labels must be rendered in `label-caps` to evoke military hardware markings. Typography contrast is strictly maintained: Platinum Silver text on Black or Deep Blue backgrounds only.

## Layout & Spacing

The layout philosophy follows a **Rigid Grid** model. On mobile, content is housed within "Armored" containers that span the full width of the safe area. The spacing rhythm is based on a 4px incremental scale, but margins are intentionally generous (20px minimum) to prevent the UI from feeling cluttered under pressure.

Elements are stacked vertically in a "Modular Block" fashion. Each block is separated by a 12px gap, creating a clear distinction between different data sets. Containers use a "double-border" technique: a 3px outer border in Platinum Silver and a 1px inner inset in Deep Blue to create a recessed, protected appearance.

## Elevation & Depth

Elevation is not conveyed through shadows, but through **Structural Layering** and **Tonal Stacking**. 

1.  **Floor (Level 0):** Pure Black (#000000). The base layer of the device.
2.  **Plating (Level 1):** Deep Blue (#001F3F) containers with 3px Platinum Silver borders. These are the primary "Armored" vessels for content.
3.  **Active Modules (Level 2):** Elements within containers use subtle metallic linear gradients to appear slightly raised or "bolted onto" the Plating.
4.  **Interaction States:** When a component is pressed, it should appear to physically depress into the UI. This is achieved by swapping the border color to a darker neutral and removing the metallic gradient, simulating a "mechanical click."

## Shapes

The design system utilizes **Zero-Radius Geometry**. All containers, buttons, and input fields feature 90-degree sharp corners. This lack of "softness" reinforces the industrial, military-grade nature of the platform.

Internal decorative elements, such as "corner brackets" or "status pips," should also adhere to strict square or rectangular shapes. The only exception is the "Safe-Dial" interaction pattern, which may use a circular motion, but must be contained within a square frame.

## Components

**Buttons (Primary):** Solid Platinum Silver background with Black text. 3px borders. No rounded corners. Must include a "Tactical Notch" (a 45-degree clipped corner) in the top-right to indicate interactivity.

**Armored Containers:** The signature component. Thick 3px borders in Platinum Silver. Use `label-caps` in the top-left corner as an integrated header tab.

**Input Fields:** Black background with 1px Platinum Silver borders. Monospaced font for user input. Active state increases border width to 3px.

**Status Chips:** Rectangular boxes with monospaced text. For "Secured" status, use a solid Green (#00FF41) border with a flickering "Active" dot.

**Data Logs:** Monospaced technical logs presented in a "Read-Only" console view. Each line is separated by a 1px Deep Blue divider.

**Biometric Lock Screen:** A full-screen container with a central metallic scan area, utilizing a brushed steel gradient and structural crosshair graphics.