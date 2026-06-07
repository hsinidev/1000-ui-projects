---
name: Pristine Clinical
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#404850'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#707881'
  outline-variant: '#bfc7d1'
  surface-tint: '#006399'
  primary: '#005d90'
  on-primary: '#ffffff'
  primary-container: '#0077b6'
  on-primary-container: '#f3f7ff'
  inverse-primary: '#94ccff'
  secondary: '#516072'
  on-secondary: '#ffffff'
  secondary-container: '#d2e1f7'
  on-secondary-container: '#556477'
  tertiary: '#565a5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#6f7274'
  on-tertiary-container: '#f6f8fa'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cde5ff'
  primary-fixed-dim: '#94ccff'
  on-primary-fixed: '#001d32'
  on-primary-fixed-variant: '#004b74'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-padding: 80px
---

## Brand & Style

The brand identity for this design system is rooted in the intersection of clinical rigor and holistic clarity. It targets a discerning audience seeking professional-grade acute care through a modern homeopathic lens. The emotional response is one of immediate calm, absolute cleanliness, and scientific authority.

The chosen design style is **Minimalism** with a heavy emphasis on **Corporate Modern** structures. Every element exists to serve a functional purpose; there is no visual noise. The "Pristine" aspect is achieved through expansive whitespace and a strict adherence to a cool-toned palette, suggesting an environment as sterile and safe as a modern laboratory.

## Colors

The palette is anchored by "Clinical Blue," a precise, medium-light blue that communicates medical reliability without the coldness of darker navies. "Sterling Silver" acts as the secondary accent, providing a metallic, high-end finish to borders and dividers. 

The background strategy utilizes "Pure White" to ensure maximum legibility and the "Pristine" aesthetic. Success and error states should be handled with muted, low-saturation versions of green and red to maintain the calm, understated atmosphere of the design system.

## Typography

This design system utilizes **Manrope** for all type treatments. Its geometric yet refined structure provides a "medical-grade" feel that is both contemporary and highly legible. 

Headlines utilize tighter letter-spacing and heavier weights to establish a confident hierarchy. Body text is prioritized for readability with a generous 1.6 line height, ensuring that medical information is accessible and never feels cramped. Labels are set in uppercase with increased letter-spacing to mimic the look of pharmaceutical labeling and scientific notation.

## Layout & Spacing

A **Fixed Grid** model is employed to maintain a sense of structural stability and institutional trust. Content is centered within a 1200px container, utilizing a 12-column system. 

The spacing rhythm is governed by an 8px baseline. Whitespace is used aggressively—not as "empty" space, but as a functional tool to separate complex medical data. Section heights are generous (80px+) to allow the UI to "breathe," reinforcing the pristine, premium nature of the service. Gutters are kept wide to prevent visual clutter in data-heavy views.

## Elevation & Depth

Depth in this design system is subtle and atmospheric. To maintain the scientific feel, we avoid heavy, dark shadows. Instead, we use:

1.  **Low-contrast outlines:** Surfaces are primarily defined by 1px "Sterling Silver" (#E2E8F0) borders rather than shadows.
2.  **Tonal layers:** The use of "Tertiary Blue-Grey" (#F8FAFC) backgrounds for container elements creates a gentle "stacked" effect against the pure white page background.
3.  **Soft Ambient Shadows:** For high-priority floating elements like modals or dropdowns, use a multi-layered, ultra-diffused shadow with 4% opacity and 20px blur, tinted with the primary blue to prevent a "dirty" grey look.

## Shapes

The shape language is "Soft Professional." We avoid sharp 0px corners, which can feel overly aggressive or dated, but we also avoid high-radius "bubbly" shapes that feel too casual or consumer-focused. 

A consistent 4px (0.25rem) radius is applied to all buttons, input fields, and small cards. Larger containers may scale up to 8px, but no further. This creates a silhouette that is modern and approachable while maintaining the precision of a scientific instrument.

## Components

### Buttons
Primary buttons use a solid "Clinical Blue" fill with white text. Secondary buttons use the "Sterling Silver" border with a transparent background. Hover states should involve a subtle shift in saturation rather than brightness to keep the palette clean.

### Input Fields
Inputs are defined by a 1px silver border and generous internal padding (12px 16px). Focus states transition the border to the primary blue with a 2px outer glow of 10% opacity blue.

### Cards
Cards are "flat" with a 1px silver border. There is no shadow in the default state. Content within cards must adhere to the 24px internal padding rule to ensure clarity.

### Chips & Tags
Used for medical categories or symptoms. These should have a light blue tinted background (#F0F7FF) and primary blue text, utilizing the 4px corner radius.

### Medical Progress Indicators
Thin, 4px-high linear bars using a light silver track and the primary blue for the fill. Avoid rounded caps on progress bars to maintain the scientific, linear aesthetic.

### Data Lists
Standardized with 1px bottom borders in silver. Vertical spacing between items should be at least 16px to ensure "purity" of information.