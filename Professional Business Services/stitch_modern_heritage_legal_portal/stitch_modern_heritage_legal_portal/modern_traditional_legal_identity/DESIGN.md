---
name: Modern-Traditional Legal Identity
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#544341'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0ef'
  outline: '#877270'
  outline-variant: '#dac1bf'
  surface-tint: '#954742'
  primary: '#2a0002'
  on-primary: '#ffffff'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#ffb3ad'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#0d1010'
  on-tertiary: '#ffffff'
  tertiary-container: '#222525'
  on-tertiary-container: '#8a8c8c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e3'
  tertiary-fixed-dim: '#c5c7c7'
  on-tertiary-fixed: '#191c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 32px
  margin-desktop: 64px
  section-padding: 120px
---

## Brand & Style

This design system is built upon the pillars of **Heritage, Precision, and Discretion**. It is designed for a top-tier legal institution where authority is conveyed through restraint and quality rather than volume. The aesthetic leans into a **Minimalist-Corporate** fusion, utilizing heavy whitespace and structural alignment to evoke a sense of security and institutional permanence. 

The visual narrative balances the "Traditional"—represented by editorial typography and a deep, historical palette—with the "Modern"—expressed through clean lines, high-performance layouts, and a rejection of unnecessary ornamentation. Users should feel they are in a "digital private office": a space that is quiet, expensive, and profoundly organized.

## Colors

The palette is anchored by **Deep Burgundy**, used strategically for primary actions and key brand moments to signify power and established history. **Gold accents** are reserved strictly for high-priority interactive elements and highlights, serving as a "gold-leaf" detail that guides the eye without overwhelming the layout.

The background system utilizes a **Marble-inspired hierarchy**. Rather than pure white, the interface employs a range of soft greys and cool whites (#F8F9F9 to #E5E7EB) to create a sense of physical texture and depth. Surface dividers should use low-opacity versions of the neutral color to maintain a light, airy feel while providing necessary structural definition.

## Typography

The typography system relies on a high-contrast pairing to distinguish between "The Voice of the Firm" and "Functional Information." 

**Newsreader** is utilized for all editorial and heading levels. Its classic serif terminals convey the gravitas of printed legal documents and academic prestige. **Manrope** is used for all functional text, data entry, and long-form reading. It provides a crisp, contemporary counterpoint that ensures the platform feels technologically advanced and highly legible. 

Generous line-heights and strict adherence to a vertical rhythm are mandatory to maintain the system's sophisticated character. Label styles should frequently employ uppercase styling with tracked-out letter spacing to mimic traditional architectural signage.

## Layout & Spacing

This design system employs a **Fixed-Width Grid** for desktop environments to create a "contained" and stable reading experience, moving to a fluid model only for smaller breakpoints. The layout is defined by its "generous whitespace"—margins and section paddings are intentionally oversized to allow the content to breathe and to signal that the user's time is valued.

The spacing rhythm is built on an 8px base unit. Elements should be grouped with tight internal spacing but separated from other groups by large "voids." This creates a clear visual hierarchy where information density is controlled and never feels cluttered.

## Elevation & Depth

Depth in this system is achieved through **Tonal Layering** and **Subtle Outlines** rather than aggressive shadows. To maintain the "Modern-Traditional" feel:

1.  **Surfaces:** Backgrounds use subtle gradients or CSS-patterned "Marble" textures (micro-noise) to avoid the flatness of digital-only design.
2.  **Borders:** Use 1px solid lines in a light grey-gold or soft-grey. These act as "frames" for content, reinforcing the feeling of a structured legal brief.
3.  **Shadows:** When necessary for functional elevation (like modals), use extremely diffused, low-opacity Burgundy-tinted shadows to suggest a physical object resting on a surface. 
4.  **Glassmorphism:** Use sparingly for navigation bars to maintain a contemporary edge, ensuring high backdrop blur settings to keep text legible against marble textures.

## Shapes

The shape language is **Conservative and Rectilinear**. We use a `Soft` (0.25rem) corner radius for standard components to take the edge off the "harshness" of digital screens while maintaining a disciplined, formal profile. Larger containers and sections should remain sharp (0px) to mimic the edges of high-quality stationery and traditional law books. Interactive elements like buttons may use the soft radius, but should never approach a pill-shape.

## Components

### Buttons
Primary buttons use the Deep Burgundy background with White or Gold text. The hover state should involve a subtle shift in brightness or a Gold bottom-border. Secondary buttons should be "Ghost" style with a 1px border and serif typography for a high-end feel.

### Input Fields
Inputs are minimalist, featuring only a bottom border that transitions to Gold upon focus. Labels use the `label-caps` typography style. Validation errors should be handled with discretion, avoiding loud reds in favor of refined iconography.

### Cards
Cards should feel like "sheets of vellum." Use a white background, a 1px soft-grey border, and zero shadow. Content inside cards should be aligned to a strict internal margin (minimum 24px).

### Selection Controls
Checkboxes and Radios are sharp-edged. The "Checked" state uses the Gold accent to provide a warm, premium confirmation.

### Marble Dividers
Section dividers are not just lines; they are 1px-4px horizontal rules that can occasionally feature a small Gold centered diamond or ornament to reinforce the traditional aesthetic.

### Data Tables
Tables are essential for legal applications. They should feature no vertical borders, only horizontal lines, with headers set in the `label-caps` style for an institutional, organized appearance.