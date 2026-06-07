---
name: Aero-Vault
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
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
  secondary: '#bac6e7'
  on-secondary: '#24304a'
  secondary-container: '#3b4662'
  on-secondary-container: '#a9b5d5'
  tertiary: '#ffffff'
  on-tertiary: '#003828'
  tertiary-container: '#36ffc4'
  on-tertiary-container: '#007255'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#d9e2ff'
  secondary-fixed-dim: '#bac6e7'
  on-secondary-fixed: '#0e1b34'
  on-secondary-fixed-variant: '#3b4662'
  tertiary-fixed: '#36ffc4'
  tertiary-fixed-dim: '#00e1ab'
  on-tertiary-fixed: '#002116'
  on-tertiary-fixed-variant: '#00513c'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: IBM Plex Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: IBM Plex Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: IBM Plex Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  container-padding: 32px
  gutter: 24px
  border-width: 2px
  border-width-heavy: 3px
---

## Brand & Style

The design system is engineered to evoke absolute trust, structural integrity, and industrial permanence. It targets aerospace engineers, logistics officers, and blockchain auditors who require high-density data visualization and "zero-fail" interfaces. 

The aesthetic is **Neo-Brutalist / Industrial**, emphasizing physical mass and security. Every element must feel "bolted down" and immutable. This is achieved through high-contrast layering, thick strokes that mimic architectural steel beams, and a technical clarity that eliminates all unnecessary decorative flourishes in favor of functional robustness.

## Colors

The palette is strictly high-contrast to ensure maximum legibility in high-stress environments. 

- **Jet Black (#0A0A0A):** The primary foundation. It serves as the "vault floor," providing a deep, void-like background for all content.
- **Platinum Silver (#E5E4E2):** Used for primary text and core structural outlines. It represents the hardened exterior of aerospace components.
- **Deep Indigo (#1E2A44):** Used for secondary containers and surface differentiation. It adds depth without compromising the "dark mode" security feel.
- **Status Accents:** An uncompromised **Cyber Mint (#00FFC2)** is used exclusively for "Verified" or "Secure" blockchain states, while a **Warning Red (#FF4D4D)** is used for security breaches or logistics delays.

## Typography

This design system utilizes a tiered typographic approach to balance corporate authority with technical precision. 

**IBM Plex Sans** is used for headlines to provide a structured, engineering-grade feel. **Inter** is the workhorse for all body copy, ensuring high legibility in dense logistics manifests. **JetBrains Mono** is reserved for metadata, blockchain hashes, and technical labels, reinforcing the platform's "verified" nature. All labels should be uppercase with slight tracking (letter-spacing) to mimic industrial stamping.

## Layout & Spacing

The layout philosophy follows a **Rigid Grid** model. Content is organized into a 12-column grid on desktop with no rounded corners on the layout containers, creating a "panelized" look similar to an aircraft cockpit.

- **Desktop (1440px+):** 12 columns, 24px gutters, 40px margins.
- **Tablet (768px):** 6 columns, 16px gutters, 24px margins.
- **Mobile (375px):** 2 columns, 12px gutters, 16px margins.

Use white space intentionally to separate high-security zones. Avoid fluid "web-like" transitions; instead, use hard cuts and clear structural divides. Elements should feel snapped to the grid.

## Elevation & Depth

Elevation in this design system is conveyed through **Physical Layering and Thick Borders** rather than shadows. 

1. **Base:** Jet Black (#0A0A0A).
2. **Floor Level:** Deep Indigo (#1E2A44) surfaces with a 2px Platinum Silver border.
3. **Elevated (Active):** Platinum Silver surfaces with Jet Black text.
4. **Interactive States:** Use "Inverted Contrast" for hover states. When a user interacts with a tile, the background and border colors should swap.

Shadows are strictly forbidden. Depth is purely a matter of border thickness and color value. A 3px border indicates a high-priority "Vault" container, while a 2px border indicates standard logistical data.

## Shapes

The design system employs a **Sharp-Edge (0px)** philosophy. There are no rounded corners. Every button, card, and input field must have 90-degree angles to maintain the "Hardened" industrial aesthetic. This sharp geometry communicates precision, security, and a lack of compromise.

## Components

### Buttons
- **Primary:** Platinum Silver background, Jet Black text, bold weight. No border (the fill defines the shape).
- **Secondary:** Jet Black background, Platinum Silver text, 2px Platinum Silver border.
- **Ghost:** No background, Platinum Silver text, Jet Black border.

### Inputs & Form Fields
Fields must have a 2px border on all sides. When focused, the border increases to 3px or changes to Cyber Mint. Labels sit strictly above the field in JetBrains Mono.

### High-Security Cards
Containers used for blockchain verification must feature a "stamped" header—a solid Platinum Silver bar with Jet Black text—connected to a Deep Indigo body with a 2px border.

### Progress & Status
Logistics tracking should use "Segmented Bars" rather than smooth gradients. Each segment represents a verified block on the chain, separated by a 1px vertical line.

### Data Tables
Tables are the heart of the system. Use a "Heavy Header" (3px bottom border). Rows should alternate between Jet Black and a slightly lighter Indigo tint for scanability. No vertical grid lines; use horizontal lines only to emphasize the "flow" of logistics.