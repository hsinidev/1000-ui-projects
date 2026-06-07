---
name: TeamSync Design System
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#3d4947'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#6d7a77'
  outline-variant: '#bcc9c6'
  surface-tint: '#006a61'
  primary: '#00685f'
  on-primary: '#ffffff'
  primary-container: '#008378'
  on-primary-container: '#f4fffc'
  inverse-primary: '#6bd8cb'
  secondary: '#555f70'
  on-secondary: '#ffffff'
  secondary-container: '#d6e0f4'
  on-secondary-container: '#596374'
  tertiary: '#006860'
  on-tertiary: '#ffffff'
  tertiary-container: '#248279'
  on-tertiary-container: '#f3fffc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#89f5e7'
  primary-fixed-dim: '#6bd8cb'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#d9e3f7'
  secondary-fixed-dim: '#bdc7db'
  on-secondary-fixed: '#121c2a'
  on-secondary-fixed-variant: '#3d4757'
  tertiary-fixed: '#9cf2e8'
  tertiary-fixed-dim: '#80d5cb'
  on-tertiary-fixed: '#00201d'
  on-tertiary-fixed-variant: '#00504a'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
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
    lineHeight: '1.25'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
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
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
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
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system is built to facilitate psychological safety within high-stakes performance environments. The brand personality is one of a "Trusted Advisor"—sophisticated, objective, and composed. By prioritizing a Corporate/Modern aesthetic with minimalist restraint, the UI reduces the cognitive load and emotional friction often associated with performance reviews.

The visual language avoids "loud" interruptions, opting instead for a balanced hierarchy that promotes constructive dialogue. It utilizes generous whitespace and a refined color palette to create a sanctuary for professional growth, ensuring that the platform feels like a tool for empowerment rather than surveillance.

## Colors

The palette is anchored by a sophisticated Teal primary, chosen for its association with clarity and emotional balance. Charcoal is utilized for typography and headers to provide a grounded, authoritative contrast without the harshness of pure black. 

The background system relies on a tiered series of Light Greys to define work areas without the need for heavy borders. Accent colors for status indicators (Success, Warning, Error) should be desaturated to maintain the "stress-reducing" mandate of the system, ensuring that even critical feedback is presented in a calm, professional context.

## Typography

The design system utilizes **Manrope** as its sole typeface. This choice provides a modern, refined, and balanced feel that bridges the gap between geometric precision and humanist warmth. 

To maintain professional clarity, a strict typographic scale is enforced. Headlines use tighter letter spacing and heavier weights to command attention, while body copy prioritizes generous line heights (1.6) to enhance readability during long-form feedback sessions. Upper-case labels are reserved for small metadata or section categories to provide structural variety without compromising the calm aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid hybrid grid**. Primary content is housed within a 1280px central container to prevent eye strain on ultra-wide monitors, while internal dashboards utilize a 12-column fluid system. 

Spacing is governed by an 8px rhythmic scale. "Generous whitespace" is a functional requirement here: vertical margins between major sections should default to `lg` (40px) or `xl` (64px) to allow content to breathe. This intentional "emptiness" directs focus toward individual feedback items and reduces the perceived complexity of the performance data.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** supplemented by **Ambient Shadows**. Instead of heavy dropshadows, we use ultra-diffused, low-opacity shadows (e.g., 4% - 8% alpha) with a subtle Teal tint in the shadow color to maintain palette harmony.

- **Level 0 (Background):** Light Grey (#F9FAFB), flat.
- **Level 1 (Cards/Containers):** White background with a 1px border (#E5E7EB) and no shadow.
- **Level 2 (Interactive/Hover):** White background with a soft, diffused shadow to indicate lift.
- **Level 3 (Modals/Overlays):** White background with a multi-layered ambient shadow and a backdrop blur (5px) to maintain context without visual noise.

## Shapes

The shape language is defined by a "Rounded" (Level 2) approach. Standard components like buttons and input fields utilize a 0.5rem (8px) corner radius. This creates a modern, approachable feel that softens the "clinical" nature of performance data.

For larger layout containers like cards and modals, the radius increases to `rounded-lg` (1rem) or `rounded-xl` (1.5rem) to emphasize their role as distinct, safe areas for content. Circular shapes are strictly reserved for user avatars and status pips to ensure they stand out against the predominantly rectangular UI.

## Components

### Buttons
Primary buttons use a solid Teal fill with white text. Secondary buttons utilize a ghost style with a Charcoal border and text. The "stress-reducing" vibe requires that buttons have ample internal padding (12px 24px) to feel substantial and easy to interact with.

### Cards
Cards are the primary vehicle for feedback. They should feature a white surface, a subtle grey border, and 24px internal padding. Avoid heavy shadows; use spacing to define the card's boundaries.

### Input Fields
Inputs must have a clear, 14px label above the field. Use a 1px border (#E5E7EB) that transitions to Teal on focus. Error states should be handled with a soft rose-tinted border rather than a vibrant red to remain within the neutral atmosphere.

### Progress & Metrics
Performance visualizations should use the Teal palette. Avoid "Red-Yellow-Green" traffic light systems which can trigger anxiety; instead, use Teal for progress and Charcoal for benchmarks.

### Lists
Lists should be "airy," with 16px of vertical padding between items and subtle horizontal dividers. This ensures that a list of 20 feedback items doesn't feel overwhelming.