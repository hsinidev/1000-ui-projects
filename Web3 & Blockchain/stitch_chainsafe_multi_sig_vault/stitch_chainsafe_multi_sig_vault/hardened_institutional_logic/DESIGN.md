---
name: Hardened Institutional Logic
colors:
  surface: '#111316'
  surface-dim: '#111316'
  surface-bright: '#37393d'
  surface-container-lowest: '#0c0e11'
  surface-container-low: '#1a1c1f'
  surface-container: '#1e2023'
  surface-container-high: '#282a2d'
  surface-container-highest: '#333538'
  on-surface: '#e2e2e6'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e2e2e6'
  inverse-on-surface: '#2f3034'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#bdc8ce'
  on-tertiary: '#283237'
  tertiary-container: '#8e999f'
  on-tertiary-container: '#273136'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#d9e4ea'
  tertiary-fixed-dim: '#bdc8ce'
  on-tertiary-fixed: '#131d22'
  on-tertiary-fixed-variant: '#3e484d'
  background: '#111316'
  on-background: '#e2e2e6'
  surface-variant: '#333538'
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
    lineHeight: '1.2'
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
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
spacing:
  unit: 8px
  container-margin: 32px
  gutter: 16px
  border-width-thin: 1px
  border-width-thick: 3px
---

## Brand & Style

This design system is engineered to evoke the psychological weight of a physical bank vault combined with the digital precision of cryptographic security. The brand personality is uncompromising, stoic, and authoritative, targeting institutional stakeholders who prioritize asset safety over trendiness.

The visual style utilizes **Industrial Brutalism**. It rejects soft, organic forms in favor of rigid geometry, heavy structural lines, and high-contrast interactions. The interface should feel less like a software application and more like a high-performance hardware terminal. Visual density is balanced by strict alignment and a mathematical approach to whitespace, ensuring that every element on the screen feels intentional and "bolted down."

## Colors

The palette is built upon a foundation of structural greys and a singular, high-visibility kinetic color. 

- **Gunmetal (#2A3439) & Deep Neutral (#121417):** These serve as the primary environment colors, creating a low-light, high-focus workspace that reduces eye strain and implies a "black-box" secure environment.
- **Platinum (#E5E4E2):** Used for primary typography and structural outlines. It provides a cool, metallic sheen that contrasts sharply against the dark background.
- **Safety Orange (#FF6700):** This is the high-alert accent. It is reserved strictly for primary actions (Submit, Approve, Sign) and critical alerts. It represents the "active" state of the vault.
- **Functional Accents:** A pure Terminal Green and Warning Red are used sparingly for status indicators (Valid/Invalid signatures) to maintain the technical, industrial aesthetic.

## Typography

The typography strategy reinforces the technical nature of multi-sig custody. 

**Space Grotesk** is used for all headlines and UI labels. Its geometric quirks and tabular-adjacent feel provide a futuristic, hardware-interface vibe. For information-dense data—such as wallet addresses and transaction hashes—this font's clear character distinction is vital for security.

**Inter** is utilized for body copy and descriptions. Its neutral, highly legible design provides the "Institutional Trust" required for long-form legal text or instructional modals, ensuring that the interface remains readable even during complex multi-step processes.

All labels for inputs and small status indicators must use the **label-caps** style to emulate industrial plate engraving.

## Layout & Spacing

The layout philosophy follows a **Fixed Rigid Grid**. Elements are locked into an 8px modular scale. This design system avoids fluid, "airy" layouts in favor of a packed, efficient density that suggests professional-grade tooling.

- **The Grid:** A 12-column grid with heavy 16px gutters. Containers do not float; they are anchored to the grid edges.
- **Structural Padding:** Interior padding for containers should be generous (24px or 32px) to ensure that despite the "heavy" industrial aesthetic, the data remains legible and actionable.
- **Alignment:** Strict left-alignment for all data points to facilitate rapid visual scanning of transaction ledgers.

## Elevation & Depth

This design system eschews shadows and blurs. Depth is communicated through **Bold Borders** and **Tonal Layering**.

- **Surface Tiers:** The base background is the darkest neutral. Interactive containers use a slightly lighter Gunmetal shade. Active or "focused" containers are outlined in Platinum.
- **Insetting:** Instead of shadows to lift elements, use "inset" styling (inner borders) to make inputs and data fields feel etched into the interface.
- **Dividers:** Use 1px Platinum lines with 20% opacity for secondary separation, and 3px solid lines for primary structural breaks. This creates a blueprint-like quality.

## Shapes

The shape language is strictly **Sharp (0px)**. 

There are no rounded corners in this design system. Every button, input field, modal, and card utilizes 90-degree angles. This rejection of softness communicates rigidity, strength, and an uncompromising stance on security. It echoes the form factor of server racks and physical security hardware.

## Components

- **Buttons:** Primary buttons use a solid Safety Orange fill with black text. They feature a 3px bottom-and-right "block shadow" (a solid offset fill, not a blur) in Platinum to give a tactile, mechanical feel.
- **Inputs:** High-contrast fields with Gunmetal backgrounds and 1px Platinum borders. When focused, the border weight increases to 2px and the label shifts to Safety Orange.
- **Cards/Containers:** These are "Industrial Vaults." They must have a 2px Gunmetal border and a header bar with a contrasting background color to house the title and status.
- **Multi-Sig Status Chips:** These should look like hardware LEDs. Square icons with high-saturation colors (Green for Signed, Orange for Pending, Red for Rejected) placed inside thick-bordered boxes.
- **Transaction Progress:** Use a "Segmented Progress Bar" style, where each required signature is represented by a physical block in the sequence, filling with Safety Orange as they are completed.
- **Data Tables:** Heavy horizontal rules between rows. Hover states should highlight the entire row in a subtle metallic grey to provide a clear line of sight across complex transaction data.