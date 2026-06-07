---
name: Nomad-Secure Identity
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#bdc8d3'
  on-secondary: '#28313b'
  secondary-container: '#3e4852'
  on-secondary-container: '#acb6c2'
  tertiary: '#c4c7c9'
  on-tertiary: '#2d3133'
  tertiary-container: '#16191b'
  on-tertiary-container: '#7f8284'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#dae3f0'
  secondary-fixed-dim: '#bdc8d3'
  on-secondary-fixed: '#131d25'
  on-secondary-fixed-variant: '#3e4852'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  status-code:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
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
  container-padding-mobile: 1.5rem
  container-padding-desktop: 4rem
  gutter: 1rem
  section-gap: 3rem
---

## Brand & Style

The design system is engineered to project absolute operational security, calm under pressure, and elite professionalism. It targets high-net-worth individuals and corporate entities requiring discreet, high-risk protection services. The aesthetic is a fusion of **Modern Minimalism** and **Corporate Precision**, emphasizing "Tactical Elegance." 

Visual noise is eliminated to facilitate rapid decision-making. The "composed" feel is achieved through a rigid adherence to alignment, ample breathing room, and a palette that evokes the silence of deep-sea operations and the clinical precision of high-tech surveillance. The interface must feel like a secure vault: impenetrable, organized, and responsive.

## Colors

This design system utilizes a sophisticated, low-light color palette optimized for discretion and reduced eye strain in operational environments.

- **Deep Navy Blue (#0A192F):** The primary foundation, used for backgrounds and primary surfaces to provide a sense of depth and authority.
- **Metallic Silver (#CBD5E1):** Used for primary iconography, borders, and secondary text, providing a cold, technical contrast.
- **Cloud White (#F8FAFC):** Reserved for critical data points, primary headings, and active states to ensure maximum legibility against the navy backdrop.
- **Surface Tones:** A secondary navy (#112240) is used to differentiate cards and containers from the base background.

## Typography

The design system employs **Inter** exclusively to ensure a utilitarian and functional appearance. The typographic hierarchy is strictly enforced to manage information density.

- **Headlines:** Use tighter letter spacing and semi-bold weights for a structured, authoritative look.
- **Body Text:** Generous line heights are maintained to prevent visual crowding in dense reports.
- **Labels:** Small-cap labels with increased letter spacing are used for metadata and form headers, mimicking military and technical documentation.
- **Functional States:** Use the 'status-code' style for real-time data feeds and coordinate tracking.

## Layout & Spacing

The design system follows a **Mobile-First, Modular Grid** philosophy. It prioritizes single-column clarity on mobile and expands into a 12-column fixed-width grid for desktop monitoring dashboards.

- **Whitespace:** Use "Generous Whitespace" as a functional tool. Margins should be wide (24px on mobile, 64px+ on desktop) to isolate critical information.
- **Rhythm:** All spacing is based on an 8px base unit. 
- **Alignment:** Content must be strictly left-aligned to establish a clear vertical scanning line for the user's eye.
- **Density:** While the margins are wide, internal component padding is compact to maintain a "composed" and efficient feel.

## Elevation & Depth

To maintain a discreet and modern profile, the design system avoids heavy drop shadows and traditional skeuomorphism.

- **Low-Contrast Outlines:** Surfaces are separated by 1px solid borders in Silver (#CBD5E1) at 10-20% opacity.
- **Tonal Layering:** Depth is achieved by placing lighter Navy surfaces (#112240) on top of the base Navy (#0A192F).
- **Z-Index:** Interactive elements (modals, dropdowns) use a subtle, highly-diffused ambient shadow (0% blur, 10% opacity) to provide just enough separation without breaking the flat, technical aesthetic.
- **Active States:** Depth is conveyed through color shift rather than physical lift; an active state might shift from Navy to a slightly brighter Metallic Silver tint.

## Shapes

The design system uses a **Soft (0.25rem)** roundedness level. This choice strikes a balance between the aggressive rigidity of sharp corners (which can feel dated or hostile) and the overly friendly nature of fully rounded elements.

- **Component Corners:** Standard buttons, input fields, and cards use a 4px (0.25rem) radius.
- **Status Indicators:** Small dots and icons remain sharp or use minimal 2px rounding to maintain a technical, vector-line feel.
- **Iconography:** Use thin-line (1px or 1.5px stroke) vector icons. Avoid filled shapes unless indicating an active toggle state.

## Components

The components within this design system are purpose-built for high-stakes environments.

- **Secure-Entry Forms:** Fields use a "ghost" style—transparent backgrounds with subtle 1px bottom or full borders. Focused states use a Cloud White border. Masked inputs for sensitive data include a "quick-clear" functional icon.
- **High-Contrast Data Visualizations:** Charts use Silver (#CBD5E1) lines against the Navy background. Data points are highlighted in Cloud White. Use high-contrast "Success" green or "Error" red only for actionable alerts.
- **Functional Status Indicators:** Indicators utilize a small dot paired with 'label-caps' text. A "pulsing" animation on the dot is permitted only for active, real-time tracking states.
- **Buttons:** Primary buttons are Silver with Navy text. Secondary buttons are outlined (Ghost) with Silver text. This ensures the primary action is always the most prominent element on a dark screen.
- **Cards:** Used for tactical summaries. Cards have no shadows; they are defined by a 1px border (#CBD5E1, 15% opacity) and a background one shade lighter than the page base.