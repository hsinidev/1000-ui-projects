---
name: Clinical Futurist
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#333535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#a2e7ff'
  on-secondary: '#003642'
  secondary-container: '#00d2fd'
  on-secondary-container: '#005669'
  tertiary: '#dbc3a8'
  on-tertiary: '#3c2e1b'
  tertiary-container: '#170c01'
  on-tertiary-container: '#8c7861'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#b4ebff'
  secondary-fixed-dim: '#3cd7ff'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#f8dec3'
  tertiary-fixed-dim: '#dbc3a8'
  on-tertiary-fixed: '#261908'
  on-tertiary-fixed-variant: '#544430'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
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
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-page: 64px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to evoke an atmosphere of absolute precision, medical authority, and hyper-advanced longevity science. It bridges the gap between high-end diagnostic hardware and intuitive software interfaces. The aesthetic leans heavily into **Clinical Futurism**, utilizing a mix of **Glassmorphism** and **High-Contrast Minimalism** to suggest transparency and technical depth.

The user should feel as though they are interacting with a high-fidelity medical console. The interface prioritizes clarity and "quiet" authority, using light-emissive accents to guide attention without overwhelming the critical diagnostic data. Security and sophistication are paramount, achieved through ultra-thin lines and expansive, dark-mode surfaces that mimic the deep blacks of an MRI scan.

## Colors

This design system utilizes a high-authority dark palette to maintain the "black-box" feel of medical imaging.

- **Primary (Deep Indigo):** The foundation. Used for the global background and structural depth.
- **Secondary (Medical-Grade Blue):** The interactive engine. Reserved for CTAs, active states, and data highlights. It should be applied as an emissive "light source."
- **Neutral (Silver):** The technical layer. Used for secondary metadata, thin borders, and non-critical iconography.
- **Surface (Frost White):** The information layer. Used for high-priority typography and alert backgrounds to ensure immediate legibility against dark surfaces.

## Typography

Typography is used to distinguish between human-readable narratives and machine-generated data.

- **Headlines:** Use **Space Grotesk** for its technical, geometric edge. This provides a sense of innovation and clinical modernity.
- **Body:** Use **Inter** for all diagnostic reports and general UI text. Its neutral character ensures high legibility and professional distance.
- **Data Accents:** Use **JetBrains Mono** for medical codes, biometric values, and timestamps. This reinforces the "data-driven" longevity analysis aspect of the service.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop (12-column) to maintain the rigorous structure of a medical document, transitioning to a fluid model for mobile. 

- **Precision Rhythm:** All spacing is based on a 4px baseline grid. 
- **Information Density:** Content should be grouped into clear modular "blocks" with generous 32px vertical stacks between sections to allow the eye to rest.
- **Margins:** Page margins are wide (64px+) to evoke a premium, gallery-like feeling for medical data.

## Elevation & Depth

This design system rejects traditional drop shadows in favor of **Glassmorphism** and **Luminous Depth**.

- **Surface Tiers:** Background depth is achieved by layering semi-transparent "glass" panels over the Deep Indigo base.
- **Backdrop Blur:** Glass overlays must use a 12px to 20px blur radius to maintain legibility while suggesting depth.
- **Accent Lighting:** Instead of shadows, use "Outer Glows" for active or primary elements. A soft, 8px-16px Medical-Grade Blue glow should emanate from buttons and critical status indicators.
- **Thin Borders:** Use 0.5pt or 1pt borders in Silver (low opacity) to define container edges without adding visual weight.

## Shapes

The shape language is controlled and precise.

- **Radii:** A "Soft" approach is used (0.25rem - 0.5rem) to avoid the playfulness of fully rounded corners while remaining more modern than sharp 90-degree angles.
- **Interactive Elements:** Buttons and inputs should maintain a consistent 0.25rem (4px) corner radius to mirror the precision of medical hardware.
- **Iconography:** Use ultra-thin (1pt) stroke weights with no fills, ensuring icons feel like technical schematics rather than illustrations.

## Components

- **Buttons:** Primary buttons feature a solid Medical-Grade Blue fill with a subtle outer glow of the same color. Secondary buttons use a Silver "ghost" style with an ultra-thin border.
- **Diagnostic Cards:** Utilize the glassmorphism style—semi-transparent dark fills with a 1px Silver border at 15% opacity.
- **Data Chips:** Small, monospaced labels used for bio-markers (e.g., "VO2 MAX: 54"). These should have a slight blue tint and be encapsulated in a thin-bordered pill.
- **Input Fields:** Minimalist under-lines or very subtle glass boxes. The focus state must trigger a Medical-Grade Blue glow.
- **MRI Viewer:** A specialized component with a Deep Indigo frame, high-contrast Frost White controls, and a Medical-Grade Blue seeker bar for navigating through scan slices.
- **Critical Alerts:** Use a solid Frost White background with black text to create a high-contrast "system override" feel, ensuring immediate attention.