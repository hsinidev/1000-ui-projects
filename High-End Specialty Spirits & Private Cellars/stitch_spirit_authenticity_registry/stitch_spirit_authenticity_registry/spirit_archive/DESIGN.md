---
name: Spirit-Archive
colors:
  surface: '#12131a'
  surface-dim: '#12131a'
  surface-bright: '#383941'
  surface-container-lowest: '#0d0e15'
  surface-container-low: '#1a1b22'
  surface-container: '#1e1f26'
  surface-container-high: '#292931'
  surface-container-highest: '#33343c'
  on-surface: '#e3e1ec'
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e3e1ec'
  inverse-on-surface: '#2f3038'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#c3c0ff'
  on-secondary: '#272377'
  secondary-container: '#3e3c8f'
  on-secondary-container: '#afadff'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#e2dfff'
  secondary-fixed-dim: '#c3c0ff'
  on-secondary-fixed: '#100563'
  on-secondary-fixed-variant: '#3e3c8f'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#12131a'
  on-background: '#e3e1ec'
  surface-variant: '#33343c'
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
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  container-max: 1440px
---

## Brand & Style

The design system is engineered to evoke absolute trust, permanence, and technical superiority. It caters to a high-stakes environment where blockchain-based verification meets physical luxury assets. The aesthetic is "Hardened Industrial Tech"—a fusion of high-end vault security and advanced cryptography.

The visual style leans heavily into **Brutalism** and **Technical Precision**. It utilizes sharp geometries, double-lined borders to simulate reinforced casings, and "Scanning" UI overlays to provide a sense of active, real-time security processing. The interface should feel less like a standard web app and more like a high-security terminal used for authenticating priceless artifacts.

## Colors

The palette is rooted in a deep, monochromatic base to emphasize the "Hardened" security aspect, contrasted by metallic highlights.

- **Platinum Silver (#E5E4E2):** Used for primary text, iconography, and the "Hardened" metallic gradients. It represents the physical asset being verified.
- **Deep Indigo (#312E81):** A structural "shadow" color used for low-light backgrounds, active glows, and scanning overlays. It provides depth without sacrificing the dark-mode integrity.
- **Black (#0A0A0A):** The foundation. Used for the primary background to create a "void" effect that makes data points pop.
- **Surface Gradients:** "Hardened" surfaces use a linear gradient (45deg) of `#E5E4E2` to `#A1A1AA` to `#E5E4E2` to simulate brushed platinum or cold-rolled steel.

Functional colors (Safe, Warning, Critical) must maintain high saturation to stand out against the dark, technical backdrop.

## Typography

This design system utilizes a tiered typographic approach to separate brand narrative from technical data.

- **Display & Headlines:** Space Grotesk provides a futuristic, geometric edge that feels modern and architectural.
- **Interface & Body:** Inter is used for its legibility and neutral, systematic feel in documentation and descriptions.
- **Technical Data:** JetBrains Mono is the "truth" font. All blockchain hashes, verification IDs, and status timestamps must be rendered in this monospaced typeface to denote raw, untampered data.

All labels should utilize the `label-caps` style to mimic the look of etched industrial plates or technical blueprints.

## Layout & Spacing

The layout is governed by a **Fixed Grid** system to maintain the "Hardened" structure. It utilizes a 12-column grid for desktop with wide gutters to allow for "Scanning" UI elements and side-aligned data overlays.

- **Grid Lines:** Vertical and horizontal grid lines (0.5px stroke in Deep Indigo) should be visible in the background to reinforce the "terminal" aesthetic.
- **Information Density:** High. Content should be grouped in modular "Verification Cards" that snap to the grid.
- **Responsive Behavior:** On mobile, the grid collapses to 4 columns. All "Hardened" borders remain sharp; do not switch to fluid rounded components for mobile.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Tonal Layering** and **Luminous Depth**.

- **Primary Surfaces:** Pure black (#0A0A0A).
- **Secondary Surfaces:** Deep Indigo (#1E1B4B) with 40% opacity, layered over the grid background.
- **Hardened Elevation:** Instead of shadows, use "Double Borders." An outer border (1px Platinum) and an inner border (1px Platinum, 2px offset) create a sense of structural reinforcement.
- **Scanning Overlays:** Use a subtle horizontal "scanline" animation (a 2px linear gradient moving vertically) to give the impression of a live security feed.
- **Interactive Depth:** When an element is pressed, it should "depress" into the interface using an inner stroke rather than an outer glow.

## Shapes

The shape language is strictly **Sharp (0px)**. No rounded corners are permitted in this design system. Every element—from buttons to status badges—must feature 90-degree angles to reinforce the "hardened" and "tamper-proof" narrative. 

For decorative elements, use "clipped corners" (45-degree chamfers) to suggest high-end machining or technical hardware components.

## Components

### Technical Verification Cards
The flagship component. These must feature a "Hardened" metallic header with a double-lined border. The body contains monospaced data points. A "Glitch" hover effect should be applied to the verification hash to simulate active decryption.

### Secure Status Badges
Status badges are not rounded pills. They are rectangular blocks with a thick 2px left-side border. 
- *Verified:* Platinum text on a Deep Indigo background.
- *Tampered:* Red text on Black background with a flickering animation.

### High-Contrast Data Tables
Tables should use "Ghost" vertical lines and solid horizontal lines. Header cells use the `label-caps` typography and a Platinum Silver background with Black text to indicate they are the primary anchors of information.

### Hardened Buttons
Buttons utilize a "Double Frame" design. The button itself is black with platinum text; it sits inside a frame that is 4px larger on all sides, connected by diagonal corner lines (crosshair style).

### Scanning UI Overlays
Small, non-interactive "data decoys" should be placed in corners—rotating hex-codes, scrolling timestamps, and grid coordinates—to enhance the "High-Security Archive" atmosphere.