---
name: Precision & Trust
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#45464d'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#001e2c'
  on-tertiary-container: '#008ebf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  code:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The brand personality is rooted in reliability, efficiency, and clarity. This design system bridges the gap between a high-density administrative interface and an inviting user-facing experience. It evokes a sense of "quiet authority"—it is professional without being cold, and modern without being trendy.

The visual style is **Corporate / Modern**. It prioritizes functional aesthetics over decorative elements. It utilizes high-quality typography and a disciplined grid to establish order. By using subtle tonal shifts and precise alignment, the system ensures that complex data in the admin panel remains legible while user-facing content feels spacious and accessible.

## Colors
The palette is centered around a "Deep Slate" primary color to convey stability and institutional trust. 

- **Primary:** Used for key actions, navigation headers, and core branding elements.
- **Secondary:** Used for sub-navigation, icons, and supporting structural elements.
- **Tertiary:** An "Electric Sky" blue used sparingly for interactive accents, progress indicators, or to draw attention to specific data points.
- **Neutrals:** A comprehensive range of slate-tinted greys to maintain visual warmth while defining hierarchy.
- **Semantic Colors:** Critical for the admin panel; green and red are used strictly for status and validation to ensure immediate user recognition of system health.

## Typography
This design system employs a dual-font strategy. **Manrope** is used for headings to provide a modern, refined, and slightly more geometric character to the brand. **Inter** is the workhorse for all body copy, forms, and data tables due to its exceptional legibility and systematic design.

Hierarchy is established through weight and scale. Labels use slightly increased letter spacing and semi-bold weights to remain distinct even at small sizes. For the admin panel, `body-sm` is the default for data density, while user-facing content defaults to `body-md` or `body-lg`.

## Layout & Spacing
The system utilizes a **12-column fluid grid** with fixed maximum widths for desktop screens to ensure readability. 

- **Admin Layout:** Uses a persistent sidebar (256px width) with a fluid content area. Padding inside data containers is tight (16px) to maximize information density.
- **User Content:** Centered fixed-width container (1280px) with generous vertical spacing (64px+) between sections to allow the design to "breathe."
- **Mobile:** Transitions to a single-column layout with 16px horizontal margins. Navigation moves to a bottom-bar or a hidden drawer.

The spacing rhythm is based on a 4px baseline, ensuring all components and layouts scale mathematically and maintain visual alignment.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Low-contrast outlines**. This design system avoids heavy shadows in favor of subtle border-strokes and background color shifts to define hierarchy.

- **Level 0 (Base):** Background color (`#F8FAFC`).
- **Level 1 (Cards/Surface):** White background with a 1px solid border (`#E2E8F0`).
- **Level 2 (Hover/Active):** Very soft, ambient shadow (0px 4px 12px rgba(15, 23, 42, 0.05)) to indicate interactivity.
- **Level 3 (Modals/Popovers):** Higher elevation shadow (0px 10px 25px rgba(15, 23, 42, 0.1)) with a semi-transparent slate backdrop blur to maintain context.

## Shapes
The shape language is "Soft" and disciplined. A corner radius of **4px (0.25rem)** is the standard for most components like buttons, input fields, and small cards. 

Larger containers or decorative elements may use **8px (0.5rem)** to feel more approachable. This subtle rounding maintains the professional "Corporate" aesthetic without feeling too playful or too sharp/aggressive.

## Components
Consistent component styling ensures the platform feels unified across different use cases.

- **Buttons:** 
  - Primary: Solid Deep Slate with white text. 
  - Secondary: Ghost style with Slate border and text.
  - Sizing: Standard (40px height) for general use; Small (32px) for admin tables.
- **Forms:** Input fields use a 1px border. Labels are always positioned above the input in `label-md`. Focus states utilize a 2px Sky Blue ring.
- **Data Tables:** High-density layout. Header rows use a light slate background with `label-sm` uppercase text. Row hover states use a subtle color shift rather than a shadow.
- **Chips/Badges:** Pill-shaped with 100px radius. Use light semantic backgrounds (e.g., light green for "Success") with dark semantic text.
- **Cards:** White surfaces with a light grey border. Avoid shadows unless the card is interactive.
- **Admin Sidebar:** Dark-themed (Deep Slate) to contrast with the light content area, helping users distinguish between navigation and workspace.