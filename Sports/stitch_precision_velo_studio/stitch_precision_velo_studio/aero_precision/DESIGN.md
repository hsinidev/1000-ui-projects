---
name: Aero Precision
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
  on-surface-variant: '#3f4753'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#707884'
  outline-variant: '#bfc7d5'
  surface-tint: '#0061a7'
  primary: '#0061a7'
  on-primary: '#ffffff'
  primary-container: '#0096ff'
  on-primary-container: '#002d52'
  inverse-primary: '#a1c9ff'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#909395'
  on-tertiary-container: '#292c2e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d2e4ff'
  primary-fixed-dim: '#a1c9ff'
  on-primary-fixed: '#001c37'
  on-primary-fixed-variant: '#00487f'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
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
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built on the intersection of technical performance and artisanal craftsmanship. It targets the discerning road cyclist who values both the aerodynamics of a carbon frame and the aesthetic purity of a boutique studio. 

The visual style is **Minimalist / High-Fidelity**, utilizing generous negative space to allow high-resolution product photography to breathe. The atmosphere is quiet and confident, avoiding loud marketing tropes in favor of a sophisticated, gallery-like experience. Every element should feel engineered—precise, lightweight, and purposeful.

## Colors

The palette is anchored by **Sky Blue**, used sparingly for primary actions and technical highlights to symbolize the open road and clarity of focus. **Slate** serves as the primary typographic and structural color, providing a softer, more premium alternative to pure black. 

- **Primary (Sky Blue):** Interactive states, active indicators, and brand accents.
- **Secondary (Slate):** Headings, icons, and high-contrast UI borders.
- **Surface (White):** The dominant background color to emphasize a clean, professional environment.
- **Muted (Slate-Light):** Used for secondary text, data labels, and subtle dividers.

## Typography

The typographic hierarchy prioritizes legibility and a modern, technical feel. **Manrope** is used for headlines to provide a refined, bespoke character with its geometric but humanist curves. **Inter** is utilized for body copy and technical specifications due to its exceptional clarity and neutral, functional aesthetic.

For technical bike specifications (e.g., weight, gear ratios), use the "data-mono" style to evoke the feeling of a performance computer. All caps should be reserved for small labels and utility links to maintain a sophisticated hierarchy.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to ensure product compositions remain balanced and high-fidelity. A 12-column grid is used with wide 64px outer margins to create a "boutique" feel, pushing content toward the center to focus the user's eye.

Vertical rhythm is strictly based on an 8px baseline. Large section gaps (120px) are intentional, used to separate distinct product stories or community features, reinforcing the minimalist, premium atmosphere.

## Elevation & Depth

Depth is communicated through **Ambient Shadows** and **Tonal Layering** rather than heavy borders. The goal is to make components feel like high-quality physical objects resting on a clean surface.

- **Level 1 (Product Cards):** Very soft, highly diffused shadows (15% opacity Slate) that expand on hover to simulate the card lifting toward the user.
- **Level 2 (Modals/Configurator Panels):** Medium diffusion with a slight Sky Blue tint in the shadow to tie the element to the brand identity.
- **Overlays:** Use a subtle backdrop blur (8px) on navigation bars and configurator menus to maintain context while ensuring legibility.

## Shapes

The shape language is **Soft (0.25rem / 4px)**. This choice reflects the precision-machined parts of a road bike—not aggressively sharp, but purposeful and aerodynamic. 

- **Buttons:** Small corner radius (4px) to maintain a professional, high-performance look.
- **Product Cards:** Standardized 8px radius (`rounded-lg`) to soften the large photographic areas.
- **Selection States:** Use a 2px inner stroke in Sky Blue for active selections in the configurator, ensuring the shape remains crisp.

## Components

### Product Cards
Cards should be oversized with edge-to-edge high-fidelity imagery. Typography is placed in the bottom third with a subtle gradient overlay if necessary. Price and weight should be displayed in a clean "data-mono" style.

### Interactive Configurator
Selection states for frame colors or component groups must use a bold Sky Blue border (2px) and a subtle scale transform (1.02x) on interaction. Use clear, high-contrast radio buttons for technical choices, where the "selected" state is a Sky Blue solid fill.

### Map Modules
Integrated maps for the community section should use a customized "Slate" theme—removing standard Google/Apple map saturation. The route itself should be a vibrant Sky Blue polyline with a subtle glow effect to highlight the "active path."

### Buttons
- **Primary:** Solid Slate background with White text. High contrast, no gradient.
- **Secondary:** Ghost style with a 1px Slate border.
- **Action:** Sky Blue background used only for "Add to Cart" or "Confirm Build" to draw immediate attention.

### Input Fields
Minimalist underline or light-grey filled fields with 4px rounding. Focus states should transition the border color to Sky Blue with a soft outer glow.