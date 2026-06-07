---
name: Specialist Medical Care
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#3e4949'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#6e7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#00696b'
  primary: '#006769'
  on-primary: '#ffffff'
  primary-container: '#1e8183'
  on-primary-container: '#f3ffff'
  inverse-primary: '#7ed5d6'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#555e5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#6d7676'
  on-tertiary-container: '#f5fefe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9af1f3'
  primary-fixed-dim: '#7ed5d6'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f51'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#dbe4e4'
  tertiary-fixed-dim: '#bfc8c8'
  on-tertiary-fixed: '#151d1d'
  on-tertiary-fixed-variant: '#404849'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

The brand personality of the design system is rooted in empathetic precision. It balances the sterile reliability of a specialist clinic with the warmth of human-centric care. The goal is to lower the patient's heart rate from the moment they interact with the interface, replacing clinical anxiety with a sense of being in expert, caring hands.

The chosen style is **Corporate / Modern** with a heavy influence of **Minimalism**. This approach prioritizes clarity and accessibility above all else. By using generous whitespace and a restricted palette, the design system ensures that critical medical information is never obscured by decorative elements. The interface feels "airy" and "breathable," mirroring the physical environment of a modern, high-end medical practice.

## Colors

The color strategy for the design system centers on psychological safety. 

- **Primary (Soft Teal):** A muted, medium-tone teal that suggests healing and vitality without being overly clinical. It is reserved for primary actions, progress indicators, and brand accents.
- **Secondary (Slate):** A deep, stable blue-gray used for headings and navigational elements to project authority and professional stability.
- **Tertiary (Teal Tint):** An ultra-light wash of the primary color used for subtle backgrounds and card fills to soften the transition between elements.
- **Neutral (Slate Gray):** Mid-tone grays used for secondary text and borders to maintain a soft contrast that reduces eye strain.
- **Background (White):** Pure white serves as the canvas, ensuring the "clinical-yet-welcoming" atmosphere and maximizing legibility.

## Typography

The typography in the design system is optimized for high-stress environments where information must be parsed quickly and accurately.

- **Public Sans** is utilized for headlines and labels. Its institutional heritage provides a sense of official trustworthiness and stability.
- **Inter** is used for body copy and data entry. Its systematic, neutral design ensures that patient records and medical instructions are perfectly legible across all screen sizes.

Hierarchy is established through weight and vertical rhythm. Headlines use a tighter letter-spacing and heavier weights to anchor sections, while body text uses a generous 1.6 line-height to prevent "walls of text" that might overwhelm a patient.

## Layout & Spacing

The design system employs a **Fixed Grid** model to create a sense of order and predictability. On desktop, content is housed within a 1200px centered container, while on mobile, it adheres to a fluid single-column layout with 24px side margins.

The spacing rhythm follows an 8px base unit. To achieve the "airy" feel, padding within cards and sections should lean toward the larger end of the scale (`lg` and `xl`). Information density should be kept low; group related medical data into distinct clusters separated by `xxl` vertical spacing to allow the user's eye to rest between sections.

## Elevation & Depth

Visual hierarchy is conveyed through **Ambient Shadows** and **Tonal Layers**. Rather than heavy black shadows, the design system uses soft, diffused shadows with a subtle Slate-blue tint (`rgba(51, 65, 85, 0.08)`). This prevents the UI from feeling "heavy."

- **Level 0 (Base):** White background.
- **Level 1 (Cards/Surface):** White surface with a 1px border in a very light Slate-Teal mix, or a very soft shadow.
- **Level 2 (Overlays/Dropdowns):** A more pronounced shadow to indicate temporary interaction.

Interactive elements should appear to lift slightly toward the user on hover, reinforcing the "approachable" nature of the system without using literal skeuomorphism.

## Shapes

The shape language of the design system is defined by "Approachable Softness." All interactive elements—including buttons, input fields, and containers—utilize a 0.5rem (8px) corner radius. Large patient-facing cards and modals utilize a 1rem (16px) radius.

These rounded forms are intentional; they move away from the "sharp" and "scary" corners often associated with traditional medical software. Circles are used exclusively for avatars and icon containers to provide a friendly, organic contrast to the structured grid.

## Components

### Buttons
Primary buttons use the Soft Teal background with white text. Secondary buttons use a Slate outline. All buttons feature a minimum height of 48px to ensure they are easy to tap for patients who may have limited dexterity or high levels of stress.

### Input Fields
Inputs are simplified with large labels placed above the field. Help text is always visible, never hidden behind tooltips. Active states use a Soft Teal border glow to guide the user's focus.

### Cards
Cards are the primary organizational unit. They should have generous internal padding (`lg`) and use subtle borders rather than heavy shadows. In the context of patient onboarding, cards should represent "steps" in the process to prevent cognitive overload.

### Navigation
The navigation bar is icon-supported, using thin-stroke icons in Slate. Each icon is accompanied by a label in `label-md` typography to ensure there is no ambiguity about the destination.

### Patient Progress Indicators
For onboarding or medical questionnaires, a horizontal progress bar in Soft Teal provides a clear sense of completion, reducing the "unknown" factor for the patient.