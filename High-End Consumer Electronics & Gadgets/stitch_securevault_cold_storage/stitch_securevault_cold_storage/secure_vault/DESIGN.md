---
name: Secure-Vault
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a29'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#c6c4df'
  on-secondary: '#2f2e43'
  secondary-container: '#47475d'
  on-secondary-container: '#b8b6d0'
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
  secondary-fixed: '#e2e0fc'
  secondary-fixed-dim: '#c6c4df'
  on-secondary-fixed: '#1a1a2e'
  on-secondary-fixed-variant: '#45455b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
spacing:
  base: 8px
  container-padding: 24px
  gutter: 16px
  border-width: 3px
  touch-target: 56px
---

## Brand & Style

This design system is engineered to evoke absolute structural integrity and cryptographic resilience. The brand personality is "Hardened"—a digital fortress that prioritizes security over decoration. It targets high-net-worth crypto-asset holders and security professionals who demand a UI that feels as unyielding as physical hardware.

The design style utilizes **Brutalist-lite** influences: raw, honest, and high-contrast. It rejects soft gradients in favor of thick, industrial borders and tactile mechanical cues. The aesthetic response should be one of "Cold Confidence," where the user feels they are interacting directly with the hardware's secure enclave rather than a generic software layer.

## Colors

The palette is strictly limited to an industrial, high-contrast range. **Platinum Silver (#E5E4E2)** serves as the primary action and stroke color, providing a metallic, premium feel. **Solid Black (#000000)** provides the void-like background required for maximum focus and privacy. **Deep Indigo (#1A1A2E)** is used sparingly for secondary containers to provide depth without breaking the "vault" atmosphere. 

Functional colors are hyper-saturated: "Matrix Green" for successful biometric verification and "Warning Red" for security alerts, ensuring critical information is never missed against the monochromatic base.

## Typography

Typography functions as a technical readout. **Space Grotesk** is used for primary headings, providing a geometric and futuristic tone that feels engineered. **Inter** is utilized for body text to ensure maximum legibility during complex security flows. 

All sensitive data—including wallet addresses, transaction hashes, and recovery phrases—must be rendered in **Space Mono**. This monospaced font ensures that every character is distinct, reducing the risk of error during manual verification. Headlines should always be bold and impactful, while labels use all-caps monospaced styling to mimic industrial equipment labeling.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on mobile to maintain a "contained" feel, expanding to a centered column on larger screens. The spacing rhythm is based on an 8px technical grid, but with unusually generous "safe area" margins (24px) to emphasize the isolation of data.

On mobile, the interface uses a single-column stack to prevent accidental taps. Elements are separated by 16px gutters. Every interactive element must adhere to a minimum 56px touch target to accommodate secure, intentional interactions (e.g., biometric triggers).

## Elevation & Depth

This design system avoids soft ambient shadows. Instead, it uses **physical displacement** and **inset depth**. Hierarchy is established through:
1.  **Inset Shadows:** Interactive areas like biometric touchpoints and input fields use 2px–4px internal shadows to look "pressed" into the hardware frame.
2.  **Tonal Stacking:** The background is always #000000. Active cards or modules sit on #1A1A2E containers with a 3px #E5E4E2 border.
3.  **Industrial Textures:** A subtle noise grain or micro-grid pattern is applied to backgrounds to mimic the matte finish of anodized aluminum.
4.  **Zero-Blur Outlines:** All depth is defined by hard-edged lines. No blurs are permitted; "elevation" is simply a stroke offset.

## Shapes

The shape language is strictly **Sharp (0px)**. Rounded corners are perceived as "soft" or "friendly," which contradicts the brand's focus on "hardened" security. All buttons, containers, cards, and input fields must have 90-degree corners. This reinforces the brutalist-lite influence and the feeling of a milled metal chassis.

## Components

**Heavy-Duty Buttons:**
Buttons are the primary interaction point. They feature a 3px Platinum Silver border. On "active" states, the button should invert (Black text on Silver background) with a hard-offset shadow that creates a "mechanical click" feel.

**Masked Data Fields:**
Input fields for private keys or sensitive values use a "Masked Pattern" overlay—a micro-grid that obscures text until a biometric hold is maintained. 

**Secure-Touch Interaction Cues:**
Rather than simple taps, high-stakes actions (like "Send") require a "Press and Hold" interaction. A progress bar or expanding stroke should fill the border of the button as the user maintains contact.

**Data Lists:**
Lists of transactions should look like a system log. Use monospaced fonts, no dividers, and 3px vertical "status bars" on the left edge of each item to indicate transaction state (Success: Green, Pending: Silver).

**Status Chips:**
Small, rectangular badges with monospaced labels. They do not have backgrounds—only a 1px border and high-contrast text.

**Privacy Shields:**
A global component that overlays a technical "static" texture or blurred noise over the entire viewport when the app loses focus or sensitive data is on-screen.