---
name: Editorial Noir
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1b1b1b'
  on-tertiary-container: '#848484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Newsreader
    fontSize: 120px
    fontWeight: '300'
    lineHeight: 100px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 64px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.15em
  ui-button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 14px
spacing:
  unit: 4px
  gutter: 24px
  margin: 64px
  section-gap: 160px
  container-max: 1440px
---

## Brand & Style

This design system embodies the "Editorial/High-Fashion Magazine" aesthetic through a Brutalist-Minimalist lens. It is designed for a luxury fashion audience that values authority, artistic disruption, and sophisticated restraint. The UI should evoke the feeling of a prestige physical monograph—heavy, intentional, and expensive.

The style rejects the "friendly" conventions of modern SaaS, opting instead for a raw, architectural structuralism. It balances massive, high-contrast serif typography with an asymmetric grid that feels curated rather than templated. Full-bleed, high-impact photography acts as the primary visual driver, while the interface remains a skeletal, high-contrast frame.

## Colors

The palette is rooted in a stark monochrome foundation to ensure imagery remains the focal point. 

- **Primary:** Absolute Black (#000000) for all typography, borders, and structural lines.
- **Secondary:** Crisp White (#FFFFFF) for the primary canvas and high-light backgrounds.
- **Accent:** Deep Oxblood (#4A0404) used sparingly for interactive states, call-to-action highlights, or editorial emphasis.
- **Neutral:** A subtle Ghost Grey (#F5F5F5) is permitted for secondary background containers or image placeholders to maintain depth without sacrificing the minimalist ethos.

## Typography

Typography is the core architectural element of this design system. 

- **Headlines:** Use **Newsreader**. Display sizes should be oversized and may overlap imagery to create a brutalist, layered effect. High-contrast serifs provide the "high-fashion" editorial voice.
- **UI & Body:** Use **Manrope**. This sans-serif provides a clean, architectural counterpoint to the serif headlines. It should feel invisible but functional.
- **Labels:** Always use uppercase Manrope with wide letter spacing for a technical, curated feel.

## Layout & Spacing

The layout follows an **asymmetric brutalist grid**. While built on a 12-column foundation, elements should intentionally break the expected rhythm.

- **Negative Space:** Use aggressive whitespace (Section Gaps) to force focus onto individual products or editorial stories.
- **Asymmetry:** Align text to the far left while images may be offset to the right or center-column, creating a "magazine spread" feel.
- **Bleeds:** Photography should frequently use "full-bleed" (edge-to-edge) to immerse the user. 
- **Margins:** Generous outer margins (64px+) ensure the content feels framed and exclusive.

## Elevation & Depth

This design system rejects traditional shadows and depth metaphors in favor of **Flat Structuralism**.

- **Layers:** Depth is achieved through stacking and overlapping. An oversized headline may sit directly on top of a high-impact image.
- **Borders:** Use 1px solid black lines to define sections or "boxes" without adding weight. No blurs or soft shadows are allowed.
- **Transparency:** Subtle use of 90-95% opacity on white backgrounds for navigation bars to allow imagery to ghost through.

## Shapes

The shape language is strictly **Sharp (0px)**. Every element—from buttons and input fields to image containers—must maintain a hard 90-degree angle. This reinforces the architectural, brutalist nature of the brand. Circular elements are only permitted for functional iconography or specific "seal of quality" badges.

## Components

- **Buttons:** Rectangular with a 1px solid black border. Use `ui-button` typography. Hover states involve a solid black fill with white text.
- **Inputs:** Minimalist single-line bottom border only. Labels sit above in `label-caps`. Focus state changes the line to the accent color (Oxblood).
- **Cards:** No background or shadow. The "card" is defined by the image and a simple 1px top border separating it from the metadata.
- **Chips/Tags:** Small, sharp rectangles with 1px borders. Typography is `label-caps`.
- **Navigation:** Stark, text-based links. No icons unless strictly necessary (e.g., Shopping Bag, Search).
- **Interactive Hints:** Use subtle micro-interactions like a slow-fade image transition or a text underline that grows from the center on hover.