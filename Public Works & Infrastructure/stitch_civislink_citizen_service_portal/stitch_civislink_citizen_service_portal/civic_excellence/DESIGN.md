---
name: Civic Excellence
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
  on-surface-variant: '#44474e'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#000c18'
  on-tertiary: '#ffffff'
  tertiary-container: '#132330'
  on-tertiary-container: '#7b8b9b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#d4e4f6'
  tertiary-fixed-dim: '#b8c8da'
  on-tertiary-fixed: '#0d1d2a'
  on-tertiary-fixed-variant: '#394857'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
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
    lineHeight: '1.5'
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.04em
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
  xxl: 48px
  gutter: 24px
  container-max: 1280px
---

## Brand & Style

This design system is engineered to evoke a sense of steadfast reliability, institutional transparency, and modern efficiency. The primary objective is to facilitate trust between a municipal government and its citizens by providing a digital environment that feels authoritative yet approachable. 

The aesthetic identity is rooted in a **Corporate/Modern** style with a heavy emphasis on **Bento-box** organization. This structural approach ensures that complex information—from tax records to permit applications—is partitioned into digestible, distinct containers. By utilizing a clean, structured layout, the design system minimizes cognitive load, making the navigation of public services intuitive for users across all levels of digital literacy. The emotional response is one of calm confidence; the interface does not shout, but rather guides with clarity and precision.

## Colors

The palette is anchored by **Deep Navy Blue**, representing the stability and authority of government. **Crisp White** serves as the canvas, providing maximum readability and a clean, sterile environment that feels professional. 

**Metallic Silver** is used for secondary structural elements and borders to define hierarchy without adding visual noise. **Slate Gray** is utilized specifically for secondary text and decorative accents to maintain high contrast while distinguishing between primary information and metadata. The system prioritizes WCAG 2.1 AA compliance across all interactions, ensuring that text is legible against the selected backgrounds for all citizens.

## Typography

The design system utilizes **Public Sans**, an institutional typeface designed specifically for government interfaces. It provides an authoritative tone that is highly legible on screens of all sizes. 

Headlines use a bold weight to establish clear entry points for information, while body copy maintains a generous line height (1.5–1.6) to facilitate comfortable long-form reading. Labels and small utility text use slightly increased letter spacing and a semi-bold weight to remain distinct and readable even at smaller scales. All typographic choices are optimized for accessibility and a clear, top-down information hierarchy.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop views, centered with a maximum width of 1280px. The layout is built on a 12-column system using a 24px gutter. 

The layout philosophy follows a **Bento-box** methodology. Content is grouped into logical modules (cards) that vary in width based on the importance of the content—spanning 4, 6, 8, or 12 columns. This modularity allows for a flexible yet highly organized dashboard-like experience. Vertical spacing is consistent, using an 8px base unit to ensure rhythm and balance across all page templates.

## Elevation & Depth

To maintain a professional and grounded feel, the design system utilizes **Tonal Layers** combined with **Ambient Shadows**. Instead of heavy depth, the system relies on subtle distinctions between the background and container surfaces.

- **Level 0 (Background):** A very light gray or white base.
- **Level 1 (Bento Containers):** Crisp white surfaces with a thin 1px Metallic Silver border and a soft, diffused shadow (0px 4px 20px rgba(0, 0, 0, 0.05)).
- **Level 2 (Hover/Active):** Slightly deeper shadow to provide tactile feedback during user interaction.

This approach creates a sense of "organized stacks" without the distracting complexity of heavy skeuomorphism or glassmorphism.

## Shapes

The shape language is defined by **Rounded** geometry to soften the institutional feel of the portal. A standard radius of 8px to 12px is applied to all primary containers and interactive elements. 

These rounded corners provide a friendly, modern touch that offsets the high-contrast navy and slate palette. Buttons and input fields follow this 8px standard, creating a cohesive visual thread across the entire application. More prominent modules or "bento cards" may utilize the larger 12px radius to emphasize their role as distinct information clusters.

## Components

### Buttons
Primary buttons use the Deep Navy Blue background with White text for high contrast. Secondary buttons utilize the Metallic Silver background with Navy text. All buttons feature 8px rounded corners and a subtle transition on hover to indicate interactivity.

### Status Steppers
For tracking applications and permits, the design system uses a clear linear stepper. Completed steps are indicated in Deep Navy with a checkmark; the active step features a bold Navy outline, and upcoming steps are rendered in Slate Gray. This ensures citizens always know where they stand in a process.

### Form Fields
Inputs are designed for maximum clarity. They feature a 1px Slate Gray border that thickens and changes to Deep Navy upon focus. Labels are always positioned above the field for accessibility, and error states are clearly marked with high-contrast red text and an icon for users with color vision deficiencies.

### Bento Cards
These are the core of the layout. Each card represents a service (e.g., "Pay Taxes," "Report an Issue"). They must have a consistent internal padding (24px) and include a clear header and a call-to-action link or button.

### List Items
Structured lists for records use alternating subtle background fills or thin Metallic Silver dividers to help users scan large amounts of data without losing their place.