---
name: ProductPath
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
  on-surface-variant: '#3e4949'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#6e7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#006a6a'
  primary: '#006565'
  on-primary: '#ffffff'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#76d6d5'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#8b4823'
  on-tertiary: '#ffffff'
  tertiary-container: '#a96039'
  on-tertiary-container: '#fff9f7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#ffdbcb'
  tertiary-fixed-dim: '#ffb692'
  on-tertiary-fixed: '#341100'
  on-tertiary-fixed-variant: '#733512'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
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
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 16px
  margin: 24px
---

## Brand & Style
This design system centers on a "Professional-Intellectual" aesthetic, positioning the product as a high-end accelerator for product leaders. The brand personality is authoritative yet enabling—like a seasoned mentor who provides the structure necessary for rapid growth. 

The UI style follows a **Modern Corporate** approach infused with **Minimalism**, characterized by a rigorous "Bento-box" layout strategy. This modularity ensures that complex product management workflows remain digestible and focused. The emotional response should be one of "Structured Clarity," where the user feels in control of a sophisticated but unobtrusive environment.

## Colors
The palette is intentionally restrained to maintain a focused, high-end educational vibe. 
- **Primary Teal (#008080)**: Used as the "Action" color—buttons, active states, and progress indicators. It represents growth and precision.
- **Charcoal (#333333)**: The anchor for all typography and deep structural accents. It provides high contrast against the light canvas, ensuring legibility and a sense of gravity.
- **Light Grey (#F5F5F5)**: Used for secondary surfaces, background containers, and subtle borders. It creates the "Bento-box" divisions without introducing heavy visual noise.
- **Surface White (#FFFFFF)**: The base for interactive cards and input areas to make them "pop" against the Light Grey background.

## Typography
Inter is selected for its utilitarian excellence and exceptional legibility in SaaS environments. The type scale is optimized for information density.
- **Headlines**: Use heavy weights (600-700) with slight negative letter-spacing to create a "locked-in" professional look.
- **Body Text**: Maintain generous line heights (1.5-1.6) to ensure educational content is easy to consume during long sessions.
- **Labels**: Use uppercase or semi-bold weights for navigation and data labels to distinguish them clearly from prose.

## Layout & Spacing
The layout utilizes a **Fixed Grid** system to maintain the "Bento-box" structure. The modular sections should align to a 12-column grid on desktop, with content grouped into distinct "containers" that have 16px to 24px of internal padding.

The Bento-box philosophy dictates that every piece of information resides in a defined module. These modules should use consistent gaps (16px) to create a rhythmic, structured appearance that feels like an organized dashboard or a premium workbook.

## Elevation & Depth
This design system avoids heavy shadows, instead using **Tonal Layers** and **Low-contrast Outlines** to communicate hierarchy.
- **Level 0**: The main background in Light Grey (#F5F5F5).
- **Level 1**: White (#FFFFFF) Bento-box cards. These use a 1px solid border (#E5E5E5) rather than shadows to define their edges.
- **Interactive State**: A very soft, diffused shadow (0px 4px 12px rgba(0,0,0,0.05)) is reserved strictly for hovered interactive elements (buttons, active cards) to indicate tactility.

## Shapes
In line with the sleek and focused aesthetic, a consistent **Rounded (0.5rem / 8px - 16px)** corner radius is applied. 
- **Standard components** (inputs, small buttons) use 8px.
- **Bento-box containers** use 16px to create a softer, more modern framing for content.
- **Pills** are used only for status indicators (e.g., "In Progress," "Completed") to differentiate them from functional buttons.

## Components
- **Buttons**: Primary buttons are solid Primary Teal with white text. Secondary buttons are Charcoal outlines or ghost styles.
- **Cards (Bento-boxes)**: The core UI element. Cards should have a white background, 16px corner radius, and a 1px #E5E5E5 border. Headers within cards should use `label-md` for clear categorization.
- **Input Fields**: Minimalist design with a 1px border. On focus, the border transitions to Primary Teal with a subtle 2px outer glow.
- **Progress Indicators**: Use thin, precise Teal lines to reinforce the "Accelerator" aspect of the brand.
- **Collaborative Avatars**: Small, circular images with a 2px white border, often stacked to show team presence within a specific Bento module.
- **Data Tables**: High density, using Charcoal for headers and Light Grey dividers; avoid zebra striping to maintain the clean aesthetic.