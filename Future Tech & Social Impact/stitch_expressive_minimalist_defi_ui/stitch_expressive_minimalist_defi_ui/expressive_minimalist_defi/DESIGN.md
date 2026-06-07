---
name: Expressive Minimalist DeFi
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c6c6c7'
  primary: '#ffffff'
  on-primary: '#2f3131'
  primary-container: '#e2e2e2'
  on-primary-container: '#636565'
  inverse-primary: '#5d5f5f'
  secondary: '#c8c6c7'
  on-secondary: '#313031'
  secondary-container: '#4a494a'
  on-secondary-container: '#bab8b9'
  tertiary: '#ffffff'
  on-tertiary: '#303032'
  tertiary-container: '#e4e2e4'
  on-tertiary-container: '#656466'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#e5e2e3'
  secondary-fixed-dim: '#c8c6c7'
  on-secondary-fixed: '#1c1b1c'
  on-secondary-fixed-variant: '#474647'
  tertiary-fixed: '#e4e2e4'
  tertiary-fixed-dim: '#c8c6c8'
  on-tertiary-fixed: '#1b1b1d'
  on-tertiary-fixed-variant: '#474649'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-lg:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
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
  container-max: 1440px
  gutter: 32px
  margin: 64px
  section-gap: 80px
---

## Brand & Style

This design system is built on the principle of **Expressive Minimalism**. It strips away the unnecessary to let high-level financial data breathe, while using sophisticated visual treatments to guide the user's attention. The brand personality is institutional yet innovative—balancing the cold precision of high-finance with the vibrant, fluid nature of decentralized technology.

The aesthetic combines **Minimalism** and **Glassmorphism**. By using heavy whitespace and a monochromatic base, we create a "gallery" effect where data visualizations become the primary artwork. Glassmorphic layers provide a sense of physical depth and hierarchy without cluttering the interface with heavy shadows or borders. The target audience is the sophisticated DeFi participant who values clarity, speed, and a premium aesthetic experience.

## Colors

The palette is rooted in a high-contrast foundation of deep charcoals and pure whites. The background strategy uses a tiered dark approach: a primary charcoal for the base and slightly lighter shades for containers to establish hierarchy.

Vibrancy is reserved strictly for data visualization and critical action states. These "electric" accents—cyan, violet, and lime—are designed to pop against the dark background, ensuring that financial trends and portfolio health are instantly legible. Accessibility is maintained through high contrast ratios between typography and surface colors.

## Typography

**Manrope** is selected for its exceptional numeric legibility and modern, geometric character. In a DeFi context, the font’s balanced proportions ensure that complex financial figures remain clear at various sizes.

The typographic hierarchy utilizes significant scale shifts to differentiate between high-level summaries and granular data. Headlines are tight and bold, while body copy is given ample line height for readability. We use a specialized "data-lg" style for primary balances and "label-sm" with increased tracking for metadata, creating a disciplined, editorial feel.

## Layout & Spacing

The layout follows a **Fixed Grid** model to provide a sense of stability and institutional trust. Content is centered within a 1440px container using a 12-column system. 

Whitespace is treated as a functional element rather than "empty" space. Large margins and section gaps are utilized to prevent cognitive overload, which is common in financial dashboards. Elements are spaced using a strict 8px linear scale, ensuring a rhythmic and predictable flow across all views. Data density is managed by prioritizing "high-level" views by default, with granular details tucked into expandable glassmorphic drawers.

## Elevation & Depth

Depth in this design system is achieved through **Backdrop Blurs** and **Tonal Layering**. Instead of traditional heavy shadows, surfaces are defined by:

1.  **Glassmorphism:** Semi-transparent containers with a `20px` to `40px` backdrop blur. This allows the background charcoals to bleed through, maintaining a cohesive "dark mode" feel while separating the active surface.
2.  **Stroke Borders:** A 1px low-opacity white border (approx 10-15% opacity) defines the edge of cards and inputs, mimicking the way light catches the edge of glass.
3.  **Subtle Ambient Shadows:** When a surface is "lifted" (e.g., a modal), a very large, diffused shadow with 0% offset and low opacity is used to create a soft glow rather than a harsh drop.

## Shapes

The design system employs a **Soft (Level 1)** roundedness level. This choice reflects a technical, precise character while avoiding the aggressive sharpness of brutalism. 

Standard components like buttons and cards use a `0.25rem` (4px) radius, while larger container modules use `0.75rem` (12px). This subtle rounding provides a modern touch that feels engineered and sophisticated, fitting for a platform managing high-value financial assets.

## Components

**Buttons:** Primary actions are solid white with charcoal text, providing maximum contrast. Secondary actions utilize a glassmorphic style—transparent background with a subtle border and high-blur effect.

**Cards:** These are the primary containers for data. They feature a `1px` border and a soft backdrop blur. Padding within cards is generous (32px) to ensure that charts and figures do not feel cramped.

**Data Visualization:** Charts should use "glow" effects—lines should have a subtle outer glow in their respective accent color to simulate an illuminated display. Area charts should use vertical gradients that fade to transparent.

**Inputs:** Input fields are minimal, consisting of a subtle background tint and a bottom border that illuminates in an accent color when focused.

**Chips:** Small, pill-shaped indicators for "Trend Up" (Green) or "Trend Down" (Red), using low-opacity backgrounds with high-saturation text to maintain the minimalist aesthetic.

**Portfolio Summary:** A high-level component that uses the largest typography in the system, centered with significant whitespace, serving as the "Hero" of the dashboard.