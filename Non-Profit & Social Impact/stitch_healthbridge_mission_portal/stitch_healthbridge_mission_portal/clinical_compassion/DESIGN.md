---
name: Clinical Compassion
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
  on-surface-variant: '#3f4850'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#6f7881'
  outline-variant: '#bec7d1'
  surface-tint: '#006492'
  primary: '#006492'
  on-primary: '#ffffff'
  primary-container: '#2d9cdb'
  on-primary-container: '#003049'
  inverse-primary: '#8ccdff'
  secondary: '#516161'
  on-secondary: '#ffffff'
  secondary-container: '#d4e6e5'
  on-secondary-container: '#576867'
  tertiary: '#5d5e5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#939494'
  on-tertiary-container: '#2b2d2d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cae6ff'
  primary-fixed-dim: '#8ccdff'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#004b6f'
  secondary-fixed: '#d4e6e5'
  secondary-fixed-dim: '#b8cac9'
  on-secondary-fixed: '#0e1e1e'
  on-secondary-fixed-variant: '#3a4a49'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: Public Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-display:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 28px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  margin-mobile: 20px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  touch-target: 48px
---

## Brand & Style

This design system is engineered for high-stakes medical environments where clarity saves lives and empathy sustains missions. The brand personality is **Clinical & Compassionate**, striking a balance between rigorous professional standards and the human-centric nature of non-profit work.

The visual style follows a **Corporate / Modern** approach with a focus on extreme legibility and structural integrity. By utilizing a "Quiet UI" philosophy, the interface minimizes cognitive load for practitioners in remote areas. Every element is designed to inspire trust through mathematical precision, generous whitespace, and a rhythmic layout that remains stable even under the pressure of emergency triage.

## Colors

The palette is optimized for visibility in varied lighting conditions, from bright outdoor mobile clinics to dimly lit rural wards. 

- **Primary Action**: Use #2D9CDB for all high-priority touchpoints, ensuring medical practitioners can identify the "next step" instantly.
- **Surface & Background**: #E0F2F1 acts as a soft tint for secondary containers to reduce screen glare. #FFFFFF is the primary workspace color to maintain a sterile, clinical feel.
- **Structure & Accents**: #BDBDBD defines boundaries without creating visual noise, while #F5F5F5 provides subtle section differentiation to organize complex patient data.

## Typography

This design system utilizes **Public Sans** for headings to provide an institutional, authoritative presence. **Inter** is used for all body and UI labels due to its exceptional x-height and legibility on mobile screens. 

Hierarchy is enforced through strict vertical rhythm. Large data displays (e.g., vital signs) use a semi-bold weight to ensure information is scannable at arm's length. Avoid using weights below 400 to maintain accessibility in low-resource environments.

## Layout & Spacing

The layout utilizes a **Fluid Grid** for mobile devices with a 4-column structure. A core principle of this design system is "Generous Breathing Room," which prevents accidental taps during high-stress interactions.

Margins are set to 20px to keep content away from screen edges where grip interference may occur. All interactive elements must adhere to a minimum 48px touch target. Section spacing follows a base-8 scale, ensuring consistent vertical flow across patient records and diagnostic checklists.

## Elevation & Depth

Visual hierarchy is established using **Tonal Layers** and **Low-Contrast Outlines** rather than heavy shadows. This maintains the "Clinical" aesthetic.

- **Level 0 (Base)**: #F5F5F5 for the canvas.
- **Level 1 (Cards)**: #FFFFFF surfaces with a 1px border of #BDBDBD.
- **Level 2 (Active/Modal)**: #FFFFFF with a very soft, diffused ambient shadow (Y: 4, Blur: 12, Opacity: 5% Black).

Depth should be used sparingly to highlight critical diagnostic tools and urgent notifications, keeping the primary interface flat and focused.

## Shapes

The shape language is consistently **Rounded** (8px / 0.5rem base). This softens the technical nature of the medical data, making the software feel more approachable and "Compassionate." 

All input fields, cards, and primary buttons must use the 8px radius. Secondary elements like tags or chips may use the `rounded-xl` (1.5rem) setting to create a pill-shaped distinction from primary structural components.

## Components

### Buttons
Primary buttons use the #2D9CDB fill with White text for maximum contrast. They should span the full width of the mobile grid in critical action zones. Secondary buttons use a #BDBDBD outline.

### Structured Form Fields
Forms must feature top-aligned labels in `label-md` for clarity. Input fields use #FFFFFF backgrounds with #BDBDBD borders. Error states must be clearly marked with high-contrast icons to assist color-blind users.

### Interactive Checklist Items
Designed for medical protocols, these are large-format rows with 8px rounded corners. The hit area covers the entire row, and the completion state triggers a subtle color shift to the secondary Teal (#E0F2F1).

### Data Visualization Cards
Used for patient vitals or mission statistics. These cards use `data-display` typography for the primary metric and `body-sm` for the units/context. They are bordered to maintain a "structured" feel.

### Medical-Grade Iconography
Icons must be "Line" style with a 2px stroke weight. Avoid filled icons unless they represent an active toggle state. Use universal medical symbols (cross, heart, vial, chart) to ensure immediate recognition across language barriers.