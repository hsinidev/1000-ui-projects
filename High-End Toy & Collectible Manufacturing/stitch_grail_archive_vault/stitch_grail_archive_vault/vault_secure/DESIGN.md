---
name: Vault-Secure
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
  on-surface-variant: '#cac4ce'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#948f98'
  outline-variant: '#49454d'
  surface-tint: '#cdc0ed'
  primary: '#cdc0ed'
  on-primary: '#342a4f'
  primary-container: '#1a1033'
  on-primary-container: '#867aa3'
  inverse-primary: '#635880'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#001b0f'
  on-tertiary-container: '#009265'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#cdc0ed'
  on-primary-fixed: '#1f1538'
  on-primary-fixed-variant: '#4b4166'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-margin: 20px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-padding: 64px
---

## Brand & Style

The design system is engineered to evoke the feeling of a private high-security vault. The brand personality is prestigious, impenetrable, and authoritative, catering to high-net-worth collectors of graded assets. The visual style merges **Glassmorphism** with **Corporate Modern** stability. 

Key attributes include:
- **Impenetrable Depth:** Use of dark, layered surfaces to create a sense of physical security.
- **Holographic Precision:** Subtle prismatic light effects on glass containers to mimic the security features found on graded card slabs.
- **Tactile Luxury:** High-fidelity imagery paired with metallic accents to reinforce the high-value nature of the marketplace.

## Colors

The palette is anchored in **Midnight Purple** and **Deep Charcoal** to provide a low-light, high-contrast environment where high-fidelity card photography can shine. 

- **Primary (Midnight Purple):** Used for deep backgrounds and primary brand moments.
- **Accent (Gold):** Reserved for "Grail" status items, high-value indicators, and primary calls to action.
- **Neutral (Deep Charcoal):** Used for structural elements and secondary surfaces to provide a grounded, mechanical feel.
- **Success (Emerald Green):** Specifically used for "Verified" badges, secure transaction confirmations, and positive price movements.

## Typography

This design system utilizes **Manrope** for headlines to convey a modern, refined tone. **Inter** is used for all body and UI elements to ensure maximum legibility, especially when displaying complex grading data and serial numbers.

For real-time data and security codes, Inter’s tabular numbers should be enabled to prevent layout shifting during price updates. Labels for "Certificate Numbers" or "Security Status" should use the **label-caps** style to create a structured, institutional appearance.

## Layout & Spacing

The layout follows a **fluid grid** logic with a mobile-first priority. On mobile, a 4-column grid is used, expanding to 12 columns for desktop viewports. 

A tight 4px baseline shift is used to ensure high data density without feeling cluttered. Card containers should use "stack-md" for internal padding to maintain a robust, "thick-walled" appearance. Large sections are separated by significant vertical whitespace (section-padding) to allow the premium assets room to breathe.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Glassmorphism**. 

1. **The Vault (Base):** The darkest canvas layer (#0A0A0C).
2. **The Tray (Level 1):** Midnight Purple surfaces with 1px Deep Charcoal borders.
3. **The Slabs (Level 2):** Glassmorphic containers with a `backdrop-filter: blur(12px)` and a subtle 1px white/gold inner stroke to simulate light hitting the edge of a plastic card slab.
4. **Featured (Level 3):** Items with a soft gold outer glow (`accent_gold_glow`) and a "Holographic" gradient overlay that shifts slightly on scroll or tilt.

Shadows are avoided in favor of inner glows and high-contrast borders to maintain a sharp, digital-first security aesthetic.

## Shapes

The shape language is **Soft (0.25rem)**. This restrained roundedness suggests precision engineering and industrial security rather than consumer friendliness. 

- **Standard Elements:** 4px (0.25rem) radius.
- **Featured Cards:** 8px (0.5rem) radius to match the physical dimensions of graded card slabs.
- **Verification Badges:** Circular (Pill) to differentiate "Status" from "Content".

## Components

- **Primary Action Buttons:** Solid Emerald Green with white text for "Secure Purchase" or "Confirm". For luxury "Grail" actions, use a Gold border with a subtle shimmering hover effect.
- **Glass Slabs (Cards):** The primary container for trading cards. Must feature a "security header" containing the grading scale (e.g., PSA 10) and a holographic shimmer effect on the top-right corner.
- **Data Rows:** Alternating backgrounds using Midnight Purple tints. Use "data-mono" for all pricing and certificate strings.
- **Security Checkboxes:** Custom square boxes with a mechanical "click" animation and gold checkmark.
- **Holographic Chips:** Small status indicators (e.g., "Mint", "Population 1") that use semi-transparent backgrounds and the `holographic_tint` gradient.
- **The "Vault" Input:** Text fields should have a recessed look (inset border) with a 1px Gold focus ring to signify active "Secure Entry".