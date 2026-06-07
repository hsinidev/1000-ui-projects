---
name: LedgerAudit Identity
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#ffb4a8'
  on-secondary: '#690000'
  secondary-container: '#920703'
  on-secondary-container: '#ff9a8a'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#101213'
  on-tertiary-container: '#7c7d7e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#920703'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  code-sm:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max: 1280px
---

## Brand & Style

The brand personality is clinical, authoritative, and uncompromisingly precise. This design system is engineered for smart contract auditors and security-conscious developers who value technical rigor over visual fluff. The aesthetic follows a **Precise-Scientific** direction, blending the functional clarity of Swiss Minimalism with the structural rigidity of Technical Brutalism.

The UI evokes an emotional response of absolute security through high-contrast interfaces and data-dense layouts. It avoids soft gradients and rounded corners in favor of "hard" edges and thin, hairline borders that suggest architectural blueprints and laboratory instruments.

## Colors

This design system utilizes a high-contrast tri-color palette optimized for legibility in complex auditing environments. 

- **Primary (Charcoal #121212):** The foundation of the dark mode interface, used for all background surfaces to reduce eye strain during long code reviews.
- **Surface (White #FFFFFF):** Reserved for high-readability text, primary UI borders, and active surface layers.
- **Accent/Risk (Deep Red #8B0000):** Used sparingly but aggressively for critical alerts, vulnerability badges, and primary action buttons to signal importance and urgency.
- **Subtle Neutral (#2A2A2A):** Utilized for secondary borders and container backgrounds to create depth without relying on shadows.

## Typography

Typography is used as a functional tool rather than a decorative element. 

- **Headlines & Labels:** **Space Grotesk** provides a technical, geometric feel that mimics scientific instrumentation. Use `label-caps` for metadata, table headers, and status indicators.
- **UI & Body:** **Inter** is the primary typeface for its exceptional legibility at small scales, particularly in data-dense tables and report summaries.
- **Code Elements:** For all smart contract snippets and hash addresses, use a system-level monospace font (e.g., JetBrains Mono) to ensure character alignment and mathematical clarity.

## Layout & Spacing

The layout philosophy is **Data-Dense Fluidity**. This design system prioritizes the maximum amount of visible information per screen to assist in rapid scanning of contract vulnerabilities.

- **Grid:** A 12-column fluid grid for desktop and a 4-column grid for mobile.
- **Rhythm:** An 8px linear scale is used for structural spacing, while a 4px "micro-scale" is used for tight internal component padding.
- **Mobile-First:** Layouts collapse into vertical stacks of "Security Grade Cards," where critical information (Risk Level, Audit Status) is anchored to the top of the viewport.

## Elevation & Depth

This design system rejects shadows and blurs. Depth is communicated strictly through **Tonal Layering** and **High-Contrast Outlines**.

- **Level 0 (Base):** Charcoal (#121212) background.
- **Level 1 (Containers):** Neutral (#2A2A2A) background with a 1px White (#FFFFFF) border at 20% opacity.
- **Level 2 (Active/Hover):** White (#FFFFFF) or Deep Red (#8B0000) 1px solid borders.
- **Visual Stacking:** Use thin vertical and horizontal lines (hairlines) to separate sections, creating a grid-like, "blueprinted" appearance that feels structural and secure.

## Shapes

The shape language is strictly **Rectilinear**. All components—including buttons, input fields, cards, and badges—must have 0px border-radius. 

Sharp edges symbolize precision and the "cutting edge" of security technology. This lack of curvature differentiates the product from consumer-facing fintech and positions it as a professional-grade technical tool.

## Components

### Buttons
Primary buttons use a solid Deep Red (#8B0000) background with White (#FFFFFF) text in all-caps Space Grotesk. Secondary buttons are "Ghost" style: 1px White border with no fill. All hover states involve a 100% color inversion or a high-contrast weight shift in the border.

### Risk Badges
Badges are the most critical visual element. Use Deep Red (#8B0000) backgrounds for 'High Risk' and pure White (#FFFFFF) for 'Informational' or 'Fixed'. Text must be bold and utilize the `label-caps` typography style.

### Security Grade Cards
Cards must have a 1px solid border. The top-right corner of every card is reserved for a "Security Grade" (A through F) set in large Space Grotesk. The card footer should always contain a timestamp and a "Verification Hash" in monospace.

### Input Fields & Terminal Blocks
Input fields are Charcoal (#121212) with a 1px White bottom border only (resembling a terminal prompt). Code blocks use a darker-than-base background (#0A0A0A) to create a "well" effect, ensuring the code is the focal point.

### Lists & Tables
Tables are the heart of the audit experience. Use thin White lines to separate rows. No zebra-striping; use border-bottoms and hover-state highlights to guide the eye. All data cells should use Inter, while IDs and addresses use monospace.