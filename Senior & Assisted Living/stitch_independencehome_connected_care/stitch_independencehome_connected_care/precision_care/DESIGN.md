---
name: Precision Care
colors:
  surface: '#fcf8fa'
  surface-dim: '#dcd9db'
  surface-bright: '#fcf8fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f5'
  surface-container: '#f0edef'
  surface-container-high: '#eae7e9'
  surface-container-highest: '#e4e2e4'
  on-surface: '#1b1b1d'
  on-surface-variant: '#45464d'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f2'
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
  tertiary-container: '#271901'
  on-tertiary-container: '#98805d'
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
  tertiary-fixed: '#fcdeb5'
  tertiary-fixed-dim: '#dec29a'
  on-tertiary-fixed: '#271901'
  on-tertiary-fixed-variant: '#574425'
  background: '#fcf8fa'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
typography:
  display:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
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
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is rooted in the intersection of high-touch human care and high-tech integration. The brand personality is authoritative yet approachable, evoking a sense of institutional stability through a "Corporate Modern" aesthetic. It prioritizes clarity and precision to reassure families of the technical sophistication behind the care, while maintaining a clean, non-clinical warmth that feels residential.

The visual style utilizes a structured, mathematical approach to layout. It balances heavy whitespace with a refined, technical finish—employing subtle depth and crisp iconography to guide users through complex health and facility data without cognitive overhead.

## Colors

The palette is anchored by **Deep Navy Blue**, providing a foundation of trust and technological sophistication. **Slate** serves as a secondary bridge, offering stability in UI chrome and secondary text. 

To ensure maximum legibility for residents, the system utilizes a high-contrast ratio between text and backgrounds. **Pure White** is reserved for primary content containers to signify cleanliness, while **Light Grey** defines the canvas and differentiates distinct functional zones. **Subtle Sky Blues** are applied exclusively to interactive elements (links, active states, and primary actions) to provide a clear, recognizable "path of intent" for the user.

## Typography

This design system utilizes **Inter** for all applications. Inter’s tall x-height and distinct letterforms ensure maximum readability for residents who may have visual impairments, while its geometric construction maintains a technical, modern feel for professional staff.

The type hierarchy is intentionally exaggerated. Headlines are oversized and high-contrast (Deep Navy on White) to provide immediate context. Body text begins at a generous 18px base for primary reading experiences. Line heights are kept airy (1.5–1.6) to prevent "crowding" of text blocks, facilitating easier scanning and tracking for older eyes.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to maintain a controlled, predictable experience across devices. A 12-column system is used for desktop views, with a maximum content width of 1280px to prevent excessive eye travel. 

A strict 8px baseline grid governs all spatial relationships. Generous margins (32px) and gutters (24px) are used to create "breathing room," which is essential for reducing user anxiety in technical or health-related contexts. Grouping is achieved through consistent padding—related items are kept within 12-24px of one another, while distinct sections are separated by 48-80px of whitespace.

## Elevation & Depth

Visual hierarchy is established through a combination of **Tonal Layers** and **Ambient Shadows**. 

1.  **Canvas:** The base background is Light Grey (#F8FAFC).
2.  **Plates:** Primary content sits on Pure White cards. These cards use a "Low-contrast outline" (1px border in Slate-200) to define their boundaries.
3.  **Interaction Depth:** Interactive elements like buttons or active cards utilize a soft, diffused shadow (0px 4px 12px, 5% opacity Navy tint) to lift them off the page. 

This multi-layered approach mimics physical paper on a desk, providing a mental model of depth that is intuitive for seniors while appearing sophisticated to technical stakeholders.

## Shapes

The shape language centers on a **Rounded** (0.5rem / 8px) corner radius for standard components like input fields, buttons, and small cards. For larger layout containers or informational dashboards, a "Large" radius (1rem / 16px) is preferred. 

This moderate rounding softens the technical "edge" of the system, making the interface feel safe and approachable without veering into the playfulness of a consumer social app. Icons should follow the same corner logic, utilizing rounded caps and joins to ensure visual harmony with the UI containers.

## Components

### Buttons & Inputs
Buttons feature a minimum height of 48px to ensure a generous "hit area" for users with reduced motor control. Primary actions use the Deep Navy background with white text; secondary actions use a Slate outline. Input fields are clearly labeled above the field, never relying on placeholder text for critical information.

### Navigation & Icons
Navigation utilizes "Icon + Label" combinations exclusively. Icons are used as functional signposts (e.g., a heart for vitals, a house for suite controls) to aid in visual recognition and memory. Icons should be stroke-based with a 2px weight for clarity.

### Cards
Cards are the primary container for resident data. They must feature a 1px Slate-200 border and a subtle hover-state elevation. Content inside cards should be strictly gridded, with clear "Label: Value" pairings in high-contrast text.

### Status Indicators
Status chips (e.g., "Active," "Alert," "Stable") use a pill-shape to distinguish them from interactive buttons. They utilize low-saturation background tints with high-saturation text to convey information without being visually jarring.