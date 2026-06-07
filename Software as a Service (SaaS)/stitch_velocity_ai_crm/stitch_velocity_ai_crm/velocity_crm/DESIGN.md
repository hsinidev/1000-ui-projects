---
name: Velocity-CRM
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434654'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737685'
  outline-variant: '#c3c6d6'
  surface-tint: '#0c56d0'
  primary: '#003d9b'
  on-primary: '#ffffff'
  primary-container: '#0052cc'
  on-primary-container: '#c4d2ff'
  inverse-primary: '#b2c5ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#3b4358'
  on-tertiary: '#ffffff'
  tertiary-container: '#535a70'
  on-tertiary-container: '#cbd2ec'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#dae2fd'
  tertiary-fixed-dim: '#bec6e0'
  on-tertiary-fixed: '#131b2e'
  on-tertiary-fixed-variant: '#3f465c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Work Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Work Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Work Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
  metric-lg:
    fontFamily: Work Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max-width: 1440px
  gutter: 1.5rem
  margin: 2rem
  bento-gap: 1rem
---

## Brand & Style

This design system is built upon the pillars of precision, authority, and high-velocity decision-making. It is designed for high-performance sales and success teams who require a data-rich environment that remains visually calm and organized. 

The aesthetic identity is **Corporate Modern** with a structural **Bento-box** influence. It prioritizes information hierarchy through clear containment and modularity. The visual language conveys reliability and sophistication, moving away from decorative elements toward a functionalist, grid-driven interface. The emotional response should be one of "controlled power"—the user should feel they have total mastery over vast amounts of data without feeling overwhelmed.

## Colors

The color palette centers on **Royal Blue** as the primary driver for action and branding, signaling trust and professional stability. The background is a clean, pure **White**, providing the necessary canvas for high-density data. 

**Slate Grey** is utilized in varying scales to manage text hierarchy and UI accents. Deep Slate is reserved for primary headings and body text to ensure maximum contrast, while lighter Slate washes are used for borders and secondary metadata. This system avoids vibrant decorative colors, using color strictly for utility: Royal Blue for primary actions, and Slate for structural grounding.

## Typography

This design system employs a dual-font strategy to balance professional character with utilitarian clarity. **Work Sans** is used for headlines and key metrics; its slightly wider stance and geometric terminals provide a grounded, authoritative feel for data points. 

**Inter** is utilized for all body copy, inputs, and UI labels. Chosen for its exceptional legibility at small sizes and high x-height, Inter allows for dense data tables and complex forms to remain readable. High contrast is maintained by using dark Slate Grey (#0F172A) for primary text against the White background, ensuring accessibility and focus.

## Layout & Spacing

The layout is governed by a **Fixed Grid** system centered on a 1440px canvas, utilizing a 12-column structure. The core layout philosophy is "Bento-box" inspired—content is partitioned into logical, rectangular containers that span varying column widths (e.g., 3-column, 6-column, or 12-column modules).

Spacing follows a strict 8px linear scale. A consistent 1rem (16px) gap is maintained between all Bento modules to ensure the "grid" is visually obvious. Large page margins (32px) provide breathing room, while internal module padding is kept tight (16px or 24px) to maximize the "data-rich" nature of the CRM.

## Elevation & Depth

This design system uses a **Tonal Layering** and **Bold Border** approach rather than heavy skeuomorphism. Depth is achieved through "low-contrast outlines" and very subtle shadows that define the edges of the Bento modules.

Bento boxes utilize a 1px solid border in a light Slate (#E2E8F0) to create clear separation. To add a modern "lift," a soft ambient shadow is applied to the containers (Y: 2px, Blur: 4px, Color: Slate with 5% opacity). This creates a subtle sense of objects sitting just above the background without breaking the clean, flat aesthetic. Overlays and modals use a more pronounced shadow to indicate a higher Z-index, while buttons utilize a subtle inner-shadow when pressed to provide tactile feedback.

## Shapes

The shape language is disciplined and "Soft-Sharp." We use a 4px (0.25rem) base corner radius for all standard UI elements, including buttons, input fields, and Bento modules. 

This specific radius provides just enough softness to feel modern and approachable while maintaining the "crisp" and professional edge required for a data-heavy SaaS tool. Level 1 roundedness ensures that when multiple modules are grouped together, the grid lines feel continuous and structural rather than bubbly.

## Components

### Buttons
Primary buttons are solid Royal Blue with white text, using a 4px corner radius. Secondary buttons use a Slate-100 background with Slate-800 text. Hover states are signaled by a 10% darkening of the background color.

### Bento Cards
The core layout component. Features a 1px Slate-200 border, white background, and Level 1 roundedness. Headers within cards should use a bottom border of 1px Slate-100 to separate the title from the data.

### Input Fields
Inputs use a white background with a 1px Slate-300 border. Upon focus, the border transitions to Royal Blue with a 2px outer glow (Royal Blue at 10% opacity). Labels are positioned above the field in `label-md` style.

### Data Tables
Tables are designed for high density. Row heights are set to 40px or 48px. Use alternating row stripes in a very faint Slate-50 for increased scanability. 

### Chips & Status Indicators
Used for "Lead Status" or "Stage." These are rectangular with Level 1 roundedness. They use a muted color palette (e.g., light blue background with dark blue text) to ensure they don't compete with primary action buttons.

### Metrics & KPIs
Key numbers within Bento boxes are displayed using the `metric-lg` typography style, ensuring they are the first thing a user sees when scanning a dashboard.