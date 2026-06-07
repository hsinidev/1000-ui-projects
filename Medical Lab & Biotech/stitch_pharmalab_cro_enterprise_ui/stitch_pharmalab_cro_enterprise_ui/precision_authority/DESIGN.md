---
name: Precision & Authority
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
  on-surface-variant: '#43474f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#737780'
  outline-variant: '#c3c6d1'
  surface-tint: '#3a5f94'
  primary: '#001e40'
  on-primary: '#ffffff'
  primary-container: '#003366'
  on-primary-container: '#799dd6'
  inverse-primary: '#a7c8ff'
  secondary: '#1f5eac'
  on-secondary: '#ffffff'
  secondary-container: '#75a9fd'
  on-secondary-container: '#003d7a'
  tertiary: '#1d1e1e'
  on-tertiary: '#ffffff'
  tertiary-container: '#333333'
  on-tertiary-container: '#9c9b9b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3ff'
  primary-fixed-dim: '#a7c8ff'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#1f477b'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#a9c7ff'
  on-secondary-fixed: '#001b3d'
  on-secondary-fixed-variant: '#00468b'
  tertiary-fixed: '#e4e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
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
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Monospace
    fontSize: 13px
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
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  grid-columns: '12'
  grid-gutter: 24px
  container-max-width: 1280px
---

## Brand & Style

This design system is built to project an image of global authority and unwavering scientific precision. It targets stakeholders in the pharmaceutical and biotech industries who require a Contract Research Organization that balances high-end technical capability with absolute institutional trust. 

The aesthetic follows a **Corporate / Modern** movement, characterized by high data density, structured grid systems, and a restrained decorative palette. It avoids trends in favor of a timeless, archival quality that feels both premium and secure. The UI should evoke the feeling of a sophisticated laboratory environment: clean, organized, and meticulously calibrated.

## Colors

The color palette centers on "Global Blue," a deep, institutional navy that signals stability and tradition. This is supported by a more vibrant secondary blue for interactive elements, ensuring clarity of action without sacrificing professionalism.

The neutral scale utilizes a cool light grey for background layering and a mid-tone grey for secondary text and borders. White is used extensively to provide "intellectual breathing room," ensuring that complex data visualizations do not become overwhelming. Functional colors for success and error states are desaturated to maintain the sophisticated, high-end atmosphere.

## Typography

The design system utilizes **Inter** for its exceptional legibility in technical contexts. As a professional sans-serif, it provides the "utilitarian" yet modern look required for complex scientific reporting.

Hierarchy is established through weight and scale rather than color. Large headlines use a tighter letter-spacing for a grounded, editorial feel. Technical data and tabular information may utilize a monospace fallback to ensure alignment and readability of numerical figures. All labels should be clear and concise, with "label-caps" reserved for metadata and table headers.

## Layout & Spacing

The layout philosophy relies on a **Fixed Grid** for marketing and information pages to maintain a controlled, high-end editorial feel. For data-intensive applications, the system transitions to a **Fluid Grid** that maximizes screen real estate.

A strict 4px baseline grid ensures vertical rhythm. Elements are spaced using increments of 8px to maintain a rigid, engineering-inspired structure. Margins are generous on the outer edges of the container to frame the content, while internal gutters remain tight (24px) to emphasize the relationship between technical data points.

## Elevation & Depth

This design system prioritizes **Tonal Layers** and **Low-Contrast Outlines** over heavy drop shadows. Depth is communicated through subtle shifts in background color—for example, moving from a White (#FFFFFF) surface to a Light Grey (#F4F4F4) container.

Where shadows are necessary for functional elevation (such as modals or dropdowns), use "Ambient Shadows": extremely diffused, low-opacity (8-10%) navy-tinted blurs that feel like natural lighting rather than digital effects. Elements should feel "seated" on the page rather than floating, reinforcing the themes of stability and grounded authority.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding takes the "edge" off the corporate aesthetic, making the interface feel modern and accessible without losing its professional rigor. 

Larger components like service cards or the login module may use `rounded-lg` (0.5rem) to provide a gentle containerization, but buttons and input fields must remain at the standard 4px radius to maintain a technical, precise appearance. Decorative elements should be geometric; avoid organic or fluid shapes.

## Components

### Technical Data Tables
Tables are the core of the scientific experience. They must feature:
- Sticky headers with `label-caps` typography.
- Subtle zebra-striping using #F4F4F4.
- High-density layouts with minimal cell padding (8px vertical).
- Inline status badges (e.g., "In Progress," "Validated") using desaturated semantic colors.

### Service Cards
Cards should be clean and structured:
- White background with a 1px border (#666666 at 20% opacity).
- Top-aligned iconography in Global Blue (#003366).
- Clear h3 titles followed by body-sm descriptions.
- Subtle hover state: 1px primary blue border or a very soft ambient shadow.

### Secure Login Area
The login interface must evoke confidence and security:
- A centered, narrow card layout.
- Heavy focus on "Field Validation" states with clear typography.
- Inclusion of a "Security Badge" or "Encrypted Connection" icon near the primary action button.
- Primary buttons in #003366 with white text, using the full width of the card.

### Input Fields
Fields should use a 1px border (#666666) with a white fill. On focus, the border transitions to Secondary Blue (#00509E) with a subtle 2px outer glow in the same color at 10% opacity. Label placement should be consistent, ideally top-aligned for readability in forms.