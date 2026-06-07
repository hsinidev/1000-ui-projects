---
name: Biometric-Vault OS
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c7c6ca'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#919094'
  outline-variant: '#46464a'
  surface-tint: '#c8c6c7'
  primary: '#c8c6c7'
  on-primary: '#313031'
  primary-container: '#0a0a0b'
  on-primary-container: '#7a797a'
  inverse-primary: '#5f5e5f'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#00dce6'
  on-tertiary: '#00373a'
  tertiary-container: '#000c0d'
  on-tertiary-container: '#00878e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e3'
  primary-fixed-dim: '#c8c6c7'
  on-primary-fixed: '#1c1b1c'
  on-primary-fixed-variant: '#474647'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#6ff6ff'
  tertiary-fixed-dim: '#00dce6'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f53'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353437'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
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
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  container-padding: 32px
  border-width-thick: 3px
  border-width-standard: 1.5px
---

## Brand & Style
The design system embodies a "Hardened Industrial" aesthetic, merging the precision of aerospace engineering with the exclusivity of luxury goods. It is designed to evoke absolute trust and a sense of impenetrable security. 

The style utilizes a **Neo-Brutalist** foundation characterized by heavy structural lines, but refined with high-fidelity "Physical Digital" elements. The UI should feel like a machined piece of hardware—tactile, weighted, and responsive. Visual motifs include scanning horizontal bars, coordinate grids, and micro-animations that suggest data being processed in real-time. The emotional goal is to make the user feel like they are operating a command center for their most valuable assets.

## Colors
This design system utilizes a high-contrast, dark-mode-first palette to emphasize the "Vault" concept.

- **Midnight Black (#0A0A0B):** The primary void. Used for deep backgrounds to create a sense of infinite depth and focus.
- **Platinum (#E5E4E2):** The structural alloy. Used for primary surfaces, thick borders, and high-emphasis text. It provides a metallic, premium feel.
- **Electric Cyan (#00F3FF):** The energy source. Reserved for active states, biometric scanning indicators, and successful authentication. This color should always feature a subtle glow (`drop-shadow`).
- **Deep Carbon (#1A1A1C):** Used for secondary containers and elevated surfaces to create a tiered hierarchy within the dark interface.

## Typography
The typographic system utilizes a trio of fonts to distinguish between brand presence, readability, and technical data.

- **Space Grotesk** is used for major headings. Its geometric, slightly futuristic construction reinforces the high-tech narrative.
- **Inter** handles all primary body copy, ensuring maximum legibility even in low-light environments typical for travel.
- **JetBrains Mono** is utilized for all "system-level" information, such as battery percentages, biometric IDs, weight data, and coordinate tracking. This reinforces the "hardened" OS feel.

All labels and data points should be uppercase when using the monospaced font to maintain a "readout" aesthetic.

## Layout & Spacing
The layout follows a strict, rigid grid reminiscent of technical blueprints. 

- **The 4px Rule:** All spacing increments must be multiples of 4px to maintain mathematical precision.
- **Fixed-Width Containers:** On desktop, the OS centers content within a fixed 1200px container to simulate a hardware console. On mobile, it uses a fluid 1-column layout with aggressive 20px margins.
- **Heavy Gutters:** 24px gutters ensure that "Hardened" components with thick borders have enough breathing room to feel distinct and heavy.
- **Inset Spacing:** Deep padding (32px) is used within cards to emphasize the "Vault" metaphor—content is protected by a significant physical margin.

## Elevation & Depth
Elevation in this design system is not achieved through light or "airiness," but through **mechanical stacking and shadows.**

1.  **Base Layer:** Midnight Black (#0A0A0B).
2.  **Tier 1 Surfaces:** Deep Carbon containers with a 3px Platinum border.
3.  **Shadows:** Use "Heavy Hard Shadows." Instead of soft blurs, use high-opacity (40-60%), 0-blur offsets (e.g., `8px 8px 0px #000000`). This mimics the look of stacked plates.
4.  **Glow FX:** Electric Cyan elements use an outer glow (`0px 0px 15px rgba(0, 243, 255, 0.4)`) to suggest active power or laser-scanning tech.
5.  **Texture:** Apply a subtle 3% grain or "noise" overlay to Platinum surfaces to give them a bead-blasted metal texture.

## Shapes
The shape language is **Sharp (0px)**. 

To reinforce the industrial and secure nature of the product, rounded corners are strictly avoided. Every button, input field, and card must have 90-degree angles. This conveys a sense of rigidity, strength, and lack of "softness." 

For decorative elements, use "clipped corners" (45-degree chamfers) to suggest specialized military-grade hardware, but the primary structural containers must remain perfectly rectangular.

## Components
- **Buttons:** Use a 3px Platinum border. Text is JetBrains Mono, uppercase. On hover, the background fills with Platinum and text flips to Midnight Black. Active buttons use Electric Cyan text and a matching 3px Electric Cyan border.
- **Biometric Inputs:** Feature a constant "scanning" horizontal line (Electric Cyan) moving vertically within the field.
- **Cards:** Heavy Deep Carbon backgrounds with a 3px Platinum stroke. Cards should have a "Header Bar" area where technical metadata (e.g., `STATUS: LOCKED`) is displayed in 12px Mono text.
- **Status Indicators:** Small square pips. Electric Cyan for `OK`, Platinum for `STANDBY`, and Red for `BREACH`.
- **Progress Bars:** Segmented bars (not smooth). Each segment represents 10% to look like an industrial battery or signal meter.
- **Lists:** Separated by 1.5px Platinum lines. Each list item should include a "Index Number" (e.g., `001`, `002`) in the left margin to maintain the data-heavy OS feel.