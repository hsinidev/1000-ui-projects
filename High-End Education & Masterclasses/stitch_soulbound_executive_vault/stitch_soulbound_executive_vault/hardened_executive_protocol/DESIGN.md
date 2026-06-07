---
name: Hardened Executive Protocol
colors:
  surface: '#0c1324'
  surface-dim: '#0c1324'
  surface-bright: '#33394c'
  surface-container-lowest: '#070d1f'
  surface-container-low: '#151b2d'
  surface-container: '#191f31'
  surface-container-high: '#23293c'
  surface-container-highest: '#2e3447'
  on-surface: '#dce1fb'
  on-surface-variant: '#c5c6ca'
  inverse-surface: '#dce1fb'
  inverse-on-surface: '#2a3043'
  outline: '#8f9194'
  outline-variant: '#44474a'
  surface-tint: '#c4c7ca'
  primary: '#ffffff'
  on-primary: '#2d3134'
  primary-container: '#e0e2e6'
  on-primary-container: '#626568'
  inverse-primary: '#5c5f62'
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#ffffff'
  on-tertiary: '#263143'
  tertiary-container: '#d8e3fb'
  on-tertiary-container: '#5a6579'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e2e6'
  primary-fixed-dim: '#c4c7ca'
  on-primary-fixed: '#191c1f'
  on-primary-fixed-variant: '#44474a'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#0c1324'
  on-background: '#dce1fb'
  surface-variant: '#2e3447'
typography:
  display-xl:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  security-hash:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.0'
spacing:
  base: 8px
  container-margin: 40px
  gutter: 24px
  card-padding: 32px
  border-width-standard: 2px
  border-width-heavy: 3px
---

## Brand & Style

The design system is engineered for an elite executive audience, prioritizing high-security, permanence, and intellectual authority. The "Hardened" aesthetic moves away from the ephemeral nature of standard web apps toward a digital architecture that feels forged, immutable, and cryptographic.

The brand personality is **Institutional, Fortified, and Precise**. It evokes the feeling of a private vault or a high-stakes command center. The visual language utilizes a mix of **Modern Minimalism** and **Technical Industrialism**, characterized by thick structural lines that suggest physical durability and premium "Platinum" finishes that distinguish Soulbound NFT certifications from standard digital assets. Every interaction should feel intentional and secure, reinforcing the value of the non-transferable credentials stored within.

## Colors

The palette is strictly limited to reinforce a sense of discipline and high-fidelity security.

- **Primary (Platinum Silver):** Used for headlines, key icons, and the "forged" metallic elements. It represents the value of the certification.
- **Secondary (Deep Navy) & Neutral (Deep Black):** These colors provide the foundational depth. The background is a "void" black to ensure high contrast, while navy is used for structural containers.
- **Platinum Gradient:** A multi-stop linear gradient used exclusively for premium UI elements, such as "Verified" badges, Soulbound NFT cards, and primary call-to-actions.
- **Status Colors:** Use a muted "Vault Green" (#22C55E) for success/verified states and a "Signal Red" (#EF4444) for security alerts, both restricted to high-contrast execution against dark backgrounds.

## Typography

This design system uses **Geist** for all core interface elements due to its technical precision and readability in high-stakes environments. 

- **Headlines:** Set with tight tracking and high weights to feel authoritative.
- **Body:** Standardized for maximum legibility against dark backgrounds, using generous line-height to prevent eye strain during long-form executive education modules.
- **Technical Labels:** **JetBrains Mono** is introduced for all cryptographic strings, hash addresses, and metadata labels to provide a "blockchain-native" aesthetic. This distinction helps users immediately identify data that is immutable and secured by the protocol.

## Layout & Spacing

The layout philosophy is a **Fixed, Structured Grid** based on an 8px rhythmic scale. 

- **The Grid:** A 12-column system with substantial 24px gutters. Content is strictly aligned to the grid edges to emphasize the "hardened" structural integrity.
- **The "Vault" Margin:** Screens utilize wide 40px outer margins to create a sense of focus and exclusivity. 
- **Density:** High information density is acceptable, provided that containers are clearly demarcated by the signature 2px or 3px borders. Whitespace is used not for "airiness," but for "separation" of distinct security protocols or content modules.

## Elevation & Depth

In this design system, depth is conveyed through **Tonal Layering and Border Intensity** rather than soft shadows. 

- **No Ambient Shadows:** Traditional drop shadows are discarded in favor of a "flat-etched" look.
- **Layering:** The base layer is pure black (#020617). Secondary containers use Deep Navy (#0F172A). Active or floating elements use a lighter Tertiary Slate (#1E293B).
- **Hard Borders:** Elevation is signaled by the thickness and color of the border. A 2px border in #475569 represents a standard container, while a 3px border in Platinum Silver represents a high-priority "Active" or "Verified" state.
- **Interactive States:** When hovered, containers do not rise; instead, their borders "illuminate" with a solid Platinum color, suggesting a mechanical engagement.

## Shapes

The design system utilizes **Sharp (0px) corners** for all primary containers, buttons, and input fields. 

This rejection of roundness is a deliberate choice to convey "Hardened" security—mimicking the sharp, precise edges of a machined metal vault or an industrial computer terminal. In rare cases where readability of an icon or a specific sub-component requires it, a maximum of 2px rounding may be applied, but the primary interface must remain strictly rectilinear to maintain its technical, authoritative character.

## Components

- **Buttons:** Rectangular with 2px borders. Primary buttons use the Platinum Gradient background with black text. Secondary buttons are transparent with 2px Silver borders and Silver text. Use `label-mono` for button text.
- **Soulbound NFT Cards:** These are the centerpiece. Use a 3px Platinum Silver border. The background should feature a subtle "technical grid" watermark. Display the "Minting Hash" at the bottom using the `security-hash` type style.
- **Input Fields:** Pure black backgrounds with a 2px Deep Navy border that turns Silver on focus. Use JetBrains Mono for user input to reinforce the "entering data into a protocol" feel.
- **Status Chips:** Small, rectangular tags with 1px borders. No background fill—only colored borders and text (e.g., a green border for "Verified").
- **Progress Bars:** Segmented blocks rather than a smooth continuous bar, evoking a loading sequence of a secure terminal.
- **The "Seal" (Certification Badge):** A high-fidelity, etched icon that utilizes the full Platinum Gradient, used to denote successful completion of an executive track. It should feel like a physical coin or emblem.
- **Data Tables:** Use 1px horizontal dividers and 2px vertical "anchors" at the start of rows to provide a strong structural framework for executive grade reports and transcripts.