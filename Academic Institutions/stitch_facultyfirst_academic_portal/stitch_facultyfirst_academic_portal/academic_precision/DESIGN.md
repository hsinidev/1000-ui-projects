---
name: Academic Precision
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#44474c'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#75777d'
  outline-variant: '#c5c6cd'
  surface-tint: '#515f74'
  primary: '#1d2b3e'
  on-primary: '#ffffff'
  primary-container: '#334155'
  on-primary-container: '#9eadc5'
  inverse-primary: '#b9c7e0'
  secondary: '#516072'
  on-secondary: '#ffffff'
  secondary-container: '#d2e1f7'
  on-secondary-container: '#556477'
  tertiary: '#252b31'
  on-tertiary: '#ffffff'
  tertiary-container: '#3a4147'
  on-tertiary-container: '#a6adb4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3fd'
  primary-fixed-dim: '#b9c7e0'
  on-primary-fixed: '#0d1c2f'
  on-primary-fixed-variant: '#3a485c'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
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
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.03em
  data-tabular:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max-width: 1440px
  gutter: 24px
  margin-edge: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

This design system is built for the high-stakes environment of academic administration, where clarity, authority, and efficiency are paramount. The brand personality is institutional yet modern—evoking the stability of a long-standing university with the streamlined efficiency of a contemporary SaaS platform. 

The visual style is **Corporate / Modern** with a strong emphasis on **Minimalism**. It utilizes a rigorous grid system to manage complex HR data without overwhelming the user. The aesthetic prioritizes functionality and information density, ensuring that faculty records, tenure tracks, and payroll data are legible at a glance. The emotional response is one of trust, organization, and professional calm.

## Colors

The palette is rooted in a "Slate Blue" spectrum to maintain a scholarly and serious tone. 

- **Primary (Slate Blue):** Used for primary actions, navigation headers, and critical wayfinding. It provides the "heavy" anchor for the interface.
- **Secondary (Silver/Steel):** Used for borders, icons, and secondary metadata to provide structure without creating visual noise.
- **Tertiary (Soft Silver):** Reserved for background layering and subtle groupings within complex forms.
- **Neutral (White/Off-white):** The primary canvas color, ensuring high contrast and a "paper-like" feel that mimics traditional academic documents.

High-contrast accessibility is maintained by using the Primary Slate against White for all essential text, ensuring WCAG AA compliance across the portal.

## Typography

This design system utilizes **Public Sans** for its institutional and neutral character, providing excellent readability in dense administrative layouts. **Inter** is used for labels and tabular data due to its superior performance at small scales and its precise numerical glyphs.

To handle high information density, the type scale is compact. We use tight line heights for labels to keep form fields grouped closely, while maintaining generous line heights for body text to ensure long-form faculty bios or policy documents remain legible. All headers use a slight negative letter spacing to maintain a "tight," authoritative look.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to ensure that complex data tables do not stretch awkwardly on ultra-wide monitors, preserving scanability. We use a 12-column grid with 24px gutters.

The spacing rhythm is strictly based on a **4px baseline grid**. This "atomic" unit allows for precise alignment of form labels and input fields. In dense data views, we prioritize vertical "stacking" (using `stack-sm`) to fit more information above the fold, while using `stack-lg` to separate distinct logical sections of a faculty member's profile.

## Elevation & Depth

To maintain a clean and professional "academic" feel, this design system avoids heavy shadows. Depth is primarily communicated through **Tonal Layers** and **Low-Contrast Outlines**.

1.  **Level 0 (Surface):** The main background using the neutral canvas color.
2.  **Level 1 (Section):** White cards with a 1px solid border in the Secondary Silver color. No shadow.
3.  **Level 2 (Interaction):** Subtle, tight ambient shadows (4px blur, 2% opacity) are reserved exclusively for floating elements like dropdown menus or active modal dialogs.

This "flat-plus" approach ensures the UI feels structural and grounded, like a well-organized physical filing system.

## Shapes

The shape language is conservative and disciplined. A **Soft (0.25rem)** roundedness is applied to standard UI components like buttons and input fields. This subtle rounding removes the harshness of "sharp" corners while maintaining a professional, rigid structure. Large containers like cards or modal overlays may use the `rounded-lg` (0.5rem) setting to create a distinct visual container for grouped data.

## Components

- **Buttons:** Primary buttons use the Slate Blue background with White text. Secondary buttons use a Silver border with Slate Blue text. All buttons have a fixed height (36px or 40px) to maintain grid alignment.
- **Input Fields:** Use a 1px Silver border. On focus, the border shifts to Slate Blue with a subtle 2px outer "halo" in the tertiary color. Labels are always positioned above the field for maximum clarity.
- **Data Tables:** The core of the portal. Rows use alternating subtle Silver backgrounds (zebra striping) to aid horizontal scanning. Headers are Slate Blue with White text for high contrast.
- **Status Chips:** Used for "Tenured," "On Leave," or "Active" statuses. These use a "de-saturated" palette—Slate Blue for neutral states, soft green for active, and soft amber for pending—to avoid a "cluttered" or overly colorful interface.
- **Academic Timeline:** A custom vertical list component with a center-aligned Silver spine, used to track a faculty member's career milestones and promotions.
- **Cards:** Used for faculty "snapshots." These should have a 1px border, no shadow, and clear internal padding (24px) to separate biography, contact info, and department details.