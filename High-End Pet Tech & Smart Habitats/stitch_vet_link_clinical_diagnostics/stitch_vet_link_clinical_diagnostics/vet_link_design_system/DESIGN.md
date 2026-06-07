---
name: Vet-Link Design System
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
  on-surface-variant: '#424751'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#727782'
  outline-variant: '#c2c6d3'
  surface-tint: '#1d5fa8'
  primary: '#003b72'
  on-primary: '#ffffff'
  primary-container: '#00529b'
  on-primary-container: '#a5c7ff'
  inverse-primary: '#a6c8ff'
  secondary: '#4e6260'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7e4'
  on-secondary-container: '#536866'
  tertiary: '#004246'
  on-tertiary: '#ffffff'
  tertiary-container: '#005b61'
  on-tertiary-container: '#5bd6e0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3ff'
  primary-fixed-dim: '#a6c8ff'
  on-primary-fixed: '#001c3b'
  on-primary-fixed-variant: '#004787'
  secondary-fixed: '#d0e7e4'
  secondary-fixed-dim: '#b5cbc8'
  on-secondary-fixed: '#0a1f1d'
  on-secondary-fixed-variant: '#364b49'
  tertiary-fixed: '#7df4ff'
  tertiary-fixed-dim: '#5dd8e2'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system is engineered for high-stakes clinical precision in the remote veterinary diagnostic space. The brand personality is authoritative yet calm, bridging the gap between advanced medical technology and empathetic pet care. 

The visual style follows a **Corporate / Modern** movement with a "Clinical-Tech" overlay. It prioritizes clarity over decoration, using a structured hierarchy to instill confidence in practitioners and pet owners. The aesthetic is ultra-clean, utilizing ample whitespace to reduce cognitive load during critical data reviews. Every element is designed to feel "medical-grade"—meaning it is reliable, predictable, and highly functional.

## Colors
The palette is rooted in a "Sterile White" foundation to provide a clean slate for diagnostics. **Medical Blue (#00529B)** serves as the primary anchor, used for headers, primary actions, and brand identification to signal trust and stability. 

**Mint (#E0F7F4)** is utilized as a sophisticated secondary accent for highlighting and soft background containers, providing a calming visual rest from high-contrast data. For interactive states and data visualization, a tertiary teal-leaning blue is introduced to differentiate from the primary brand mark. Grays are kept neutral and cool to maintain the clinical atmosphere without feeling "muddy."

## Typography
This design system utilizes **Inter** exclusively for its exceptional legibility in digital interfaces and its neutral, systematic character. The type scale is disciplined, focusing on hierarchical clarity.

Key typographic rules:
- **Headlines:** Use Semi-Bold weight with slight negative letter-spacing to appear more authoritative.
- **Data Display:** Utilize `font-feature-settings: 'tnum'` for tabular figures in medical charts to ensure numbers align vertically.
- **Labels:** Small, uppercase labels with increased tracking are used for metadata and table headers to distinguish them from primary content.

## Layout & Spacing
The system employs a **Fixed Grid** for administrative and diagnostic dashboards to ensure consistent placement of tools and charts. A 12-column grid is standard for desktop views, with a 24px gutter to maintain breathable separation between dense data modules.

Spacing follows a strict 4px linear scale. Internal card padding is typically set to `lg` (24px) for clinical reports, while dense data tables may use `sm` (8px) for vertical cell padding to maximize information density.

## Elevation & Depth
The design system uses **Tonal Layers** combined with **Ambient Shadows** to create a sense of organized depth. Surfaces are primarily "Sterile White," with the background of the application set to a very light cool-gray or Mint-tinted white to make primary cards pop.

Shadows are soft, highly diffused, and use a slight Medical Blue tint in the shadow color (e.g., `rgba(0, 82, 155, 0.08)`) instead of pure black. This prevents the UI from looking "dirty." Elevation is used sparingly to indicate focus—such as a diagnostic card being hovered or a modal window appearing.

## Shapes
The shape language is "Softly Structured." We use a standard **8px (0.5rem)** radius for most components, including input fields and buttons. Larger containers, such as diagnostic result cards or data visualizations, utilize a **12px (0.75rem)** radius.

This specific roundedness level balances the serious nature of medical equipment with the approachability of modern software. It avoids the aggressive sharpness of legacy medical software while remaining more professional than highly rounded, consumer-focused apps.

## Components
- **Buttons:** Primary buttons are solid Medical Blue with white text. Secondary buttons use a Mint background with Medical Blue text. High-density views should use "Ghost" buttons for tertiary actions.
- **Medical-Grade Tables:** Headers must be Mint or light gray with bold, uppercase labels. Row stripes (Zebra striping) should use a subtle Mint tint (#F5FDFB) for horizontal eye-tracking.
- **Data Visualization Containers:** Use 1px borders in a light gray-blue rather than heavy shadows. Each container should have a clear header and a "fullscreen" or "export" utility icon.
- **Iconography:** Use a consistent 2pt stroke weight. Icons should be functional and literal (e.g., a realistic stethoscope or microscope shape) rather than abstract.
- **Input Fields:** Use a subtle 1px border (#D1D5DB) that shifts to Medical Blue on focus. Error states must include both a color shift to red and a clarifying icon for accessibility.
- **Status Chips:** Use a pill shape for status indicators (e.g., "Critical," "Stable," "Pending"). These use low-saturation background tints with high-saturation text for maximum readability.