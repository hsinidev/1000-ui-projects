---
name: Clinical Excellence Global
colors:
  surface: '#f6f9ff'
  surface-dim: '#d4dbe2'
  surface-bright: '#f6f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef4fc'
  surface-container: '#e8eef6'
  surface-container-high: '#e3e9f1'
  surface-container-highest: '#dde3eb'
  on-surface: '#161c22'
  on-surface-variant: '#45464d'
  inverse-surface: '#2b3137'
  inverse-on-surface: '#ebf1f9'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#191c1e'
  on-tertiary-container: '#818486'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f6f9ff'
  on-background: '#161c22'
  surface-variant: '#dde3eb'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
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
  container-max: 1280px
  gutter: 24px
  margin: 32px
  stack-xs: 4px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system centers on the concept of "Clinical Authority." The brand personality is rooted in unwavering reliability, global scale, and meticulous dental care. It targets an international demographic seeking high-end, specialized healthcare where trust is the primary currency.

The visual style is **Corporate / Modern** with a lean toward **Minimalism**. It prioritizes clarity and order through strict alignment, ample negative space, and a refined structural grid. By combining sterile cleanliness with high-end metallic accents, the UI evokes the feeling of a premium, state-of-the-art medical facility.

## Colors

The palette is anchored by **Global Blue**, a deep, sophisticated navy that communicates stability and institutional wisdom. This is complemented by a range of **Metallic Greys** that provide a clean, modern framework.

- **Primary (Global Blue):** Used for headers, primary actions, and brand-heavy components.
- **Secondary (Metallic Grey):** Reserved for supporting text, iconography, and subtle UI borders to maintain a professional, high-end feel.
- **Surface (Tertiary):** A clinical, off-white background that reduces eye strain while maintaining a sterile aesthetic.
- **Accents:** Use of metallic silver gradients is encouraged for certificate badges and trust indicators.

## Typography

This design system utilizes **Public Sans**, an institutional and neutral typeface designed for clarity and accessibility. Its strong geometric foundations provide the legibility required for healthcare information while maintaining a contemporary corporate edge.

Headlines should use heavy weights with slightly tightened letter spacing to project authority. Body text utilizes a generous line height (1.6) to ensure medical information is easy to consume. Labels and metadata should be rendered in uppercase with increased tracking to evoke the feel of a premium architectural or medical plaque.

## Layout & Spacing

The design system employs a **Fixed Grid** model to maintain a controlled and prestigious presentation. A 12-column grid system is used for desktop layouts, ensuring that medical certificates and professional accolades have a structured home.

Spacing follows a strict **8px base unit**, emphasizing "Professional Spacing"—which means favoring larger gaps between sections to prevent the interface from feeling cluttered or stressful. All content should be centered within a maximum container width of 1280px to ensure an optimal reading experience on wide monitors.

## Elevation & Depth

To maintain a grounded and reliable aesthetic, the system avoids heavy, floating shadows. Instead, it uses **Low-Contrast Outlines** and **Tonal Layers**.

Depth is created by:
- **Hairline Borders:** 1px borders in `neutral_color_hex` to define component boundaries with surgical precision.
- **Subtle Ambient Shadows:** Only used for hover states on primary cards, using a very low opacity (5-10%) navy-tinted shadow.
- **Surface Tiering:** Using the tertiary grey for section backgrounds to separate "Trust" sections (testimonials, certificates) from primary medical content.

## Shapes

The shape language is **Soft**, utilizing a 4px (0.25rem) base radius. This minimal rounding softens the "hardness" of the medical environment to feel approachable, without losing the precision and order of a corporate hospital.

Special elements, such as "Verified Physician" badges or "Global Accreditation" seals, should maintain sharp or circular profiles to distinguish them from standard UI elements.

## Components

- **Buttons:** Primary buttons use the Global Blue background with white text and a subtle 1px metallic border. Secondary buttons are ghost-style with a navy outline.
- **Trust Badges:** High-contrast, circular or shield-shaped components containing metallic gradients and small-caps labels. These should be placed near primary calls to action.
- **Cards:** Clean, white surfaces with a 1px slate border. Headers within cards should have a subtle grey background to differentiate the "header" from the "body" of the data.
- **Input Fields:** Professional and high-contrast. Use a 1px slate border that thickens slightly on focus. Ensure labels are always visible and positioned above the field.
- **Accreditation List:** A specialized list component featuring small icons of medical boards and certificates, emphasizing the hospital's global credentials.
- **Progress Steppers:** Used for patient intake forms, featuring thin lines and Global Blue nodes to guide the user through complex processes with ease.