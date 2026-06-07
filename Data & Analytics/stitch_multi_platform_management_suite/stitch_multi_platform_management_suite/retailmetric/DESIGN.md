---
name: RetailMetric
colors:
  surface: '#fef7ff'
  surface-dim: '#ded8e3'
  surface-bright: '#fef7ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f1fc'
  surface-container: '#f2ebf7'
  surface-container-high: '#ece6f1'
  surface-container-highest: '#e7e0eb'
  on-surface: '#1d1a22'
  on-surface-variant: '#494453'
  inverse-surface: '#322f37'
  inverse-on-surface: '#f5eef9'
  outline: '#7a7484'
  outline-variant: '#cbc3d5'
  surface-tint: '#6b46c1'
  primary: '#532aa8'
  on-primary: '#ffffff'
  primary-container: '#6b46c1'
  on-primary-container: '#e1d2ff'
  inverse-primary: '#d0bcff'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#444749'
  on-tertiary: '#ffffff'
  tertiary-container: '#5c5f61'
  on-tertiary-container: '#d7d9db'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#522aa7'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#fef7ff'
  on-background: '#1d1a22'
  surface-variant: '#e7e0eb'
typography:
  display:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-num:
    fontFamily: Manrope
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  bento-gap: 20px
  container-padding: 40px
---

## Brand & Style

This design system is engineered for the high-stakes world of omni-channel retail analytics. The brand personality is authoritative yet vibrant, bridging the gap between traditional corporate reliability and modern data agility. It evokes a sense of "clarity through complexity," transforming massive data streams into actionable intelligence.

The visual style is a sophisticated blend of **Minimalism** and **Modern Corporate**, utilizing a high-density "Bento Box" layout to organize disparate data points into a cohesive story. The interface remains clean and airy to prevent cognitive overload, while the vibrant purple accents provide the energy and focus required for a modern SaaS platform.

## Colors

The palette is anchored by **Royal Purple**, used strategically for primary actions, branding, and key data highlights. **Slate** serves as the functional backbone, providing professional grounding for text, iconography, and secondary UI elements.

- **Primary (Royal Purple):** High-energy, luxury-tier purple used for focus states and primary calls to action.
- **Secondary (Slate):** Neutral blue-greys used for secondary information and structural borders.
- **Surface (White/Off-white):** Clean, expansive backgrounds to ensure maximum readability and data "pop."
- **Data Visualization:** A secondary spectrum of teal, amber, and rose is used alongside the primary purple to differentiate multi-channel data streams.

## Typography

The typographic hierarchy utilizes **Manrope** for headlines and data hero numbers to project a modern, geometric, and trustworthy feel. **Inter** is employed for all body copy and UI labels due to its exceptional legibility at small sizes and high-density environments.

Large "Display" sizes are reserved for high-level KPIs, while "Label-caps" are used for categorization within the bento-box grid. Data points should always prioritize Manrope’s medium or bold weights to ensure they are the first thing a user sees.

## Layout & Spacing

This design system uses a **Fixed-Fluid Hybrid Grid**. The main content dashboard utilizes a 12-column system that scales with the viewport width but maintains strict maximum container sizes to preserve data readability.

The layout philosophy is defined by the **Bento Box** model. Each data visualization or metric set is housed in a distinct, rounded card. These cards should span a varying number of columns (typically 3, 4, 6, or 12) but maintain a uniform gutter of 20px. This creates a rhythmic, organized "modular dashboard" that feels structured and intentional.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and extremely soft, diffused **Ambient Shadows**. 

- **Level 0 (Background):** Slate-50 or pure White.
- **Level 1 (Bento Cards):** White background with a 1px Slate-100 border.
- **Level 2 (Active/Hover):** A subtle 8% opacity Royal Purple shadow with a 20px blur, giving the card a "lifted" effect.
- **Level 3 (Modals/Popovers):** Higher contrast shadows (15% opacity) to separate critical interactions from the data-rich background.

Avoid heavy dark shadows; the goal is a clean, "backlit" feel that suggests transparency and lightness.

## Shapes

The shape language is defined by **Soft Geometricism**. A standard corner radius of 12px (rounded-lg) is applied to all primary bento boxes and containers to soften the density of the data. Buttons and input fields follow a slightly tighter 8px radius to maintain a professional, crisp edge. Small utility chips and tags use a fully rounded (pill) style to distinguish them from interactive containers.

## Components

- **Bento Cards:** The foundational component. Must include a title, optional subtitle, and a standardized "action" area in the top right. Content should have 24px internal padding.
- **Buttons:** Primary buttons are solid Royal Purple with white text. Secondary buttons use a Ghost style with a Slate-200 border. All buttons have a subtle 2px vertical lift on hover.
- **Data Chips:** Small, pill-shaped indicators used for "Channel" (e.g., Online, In-Store, Social). These use low-saturation background tints of the primary colors with high-saturation text.
- **Input Fields:** Minimalist design with a Slate-200 bottom border that transforms into a 2px Royal Purple border on focus.
- **Charts:** High-contrast line and bar charts using the primary Purple and secondary Slate colors. Use "Area" fills with 10% opacity gradients to add depth.
- **Metric Heroes:** Large-format Manrope typography displaying a single KPI, accompanied by a small trend indicator (arrow + percentage).