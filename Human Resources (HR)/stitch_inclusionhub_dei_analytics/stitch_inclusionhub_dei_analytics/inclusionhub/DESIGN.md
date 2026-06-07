---
name: InclusionHub
colors:
  surface: '#f7fafa'
  surface-dim: '#d7dbdb'
  surface-bright: '#f7fafa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f4'
  surface-container: '#ebeeef'
  surface-container-high: '#e5e9e9'
  surface-container-highest: '#e0e3e3'
  on-surface: '#181c1d'
  on-surface-variant: '#3e494a'
  inverse-surface: '#2d3132'
  inverse-on-surface: '#eef1f2'
  outline: '#6e797a'
  outline-variant: '#bec8ca'
  surface-tint: '#006972'
  primary: '#005c64'
  on-primary: '#ffffff'
  primary-container: '#0d7680'
  on-primary-container: '#bbf7ff'
  inverse-primary: '#80d4de'
  secondary: '#712ae2'
  on-secondary: '#ffffff'
  secondary-container: '#8a4cfc'
  on-secondary-container: '#fffbff'
  tertiary: '#893c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#ae4f03'
  on-tertiary-container: '#ffe8dd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9cf0fb'
  primary-fixed-dim: '#80d4de'
  on-primary-fixed: '#001f23'
  on-primary-fixed-variant: '#004f56'
  secondary-fixed: '#eaddff'
  secondary-fixed-dim: '#d2bbff'
  on-secondary-fixed: '#25005a'
  on-secondary-fixed-variant: '#5a00c6'
  tertiary-fixed: '#ffdbca'
  tertiary-fixed-dim: '#ffb68e'
  on-tertiary-fixed: '#331200'
  on-tertiary-fixed-variant: '#763300'
  background: '#f7fafa'
  on-background: '#181c1d'
  surface-variant: '#e0e3e3'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
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
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  label-md:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-numeral:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.0'
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
  xl: 40px
  gutter: 24px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

The design system is rooted in the philosophy of "Radical Empathy through Data." It balances the analytical rigor required for corporate DEI (Diversity, Equity, and Inclusion) reporting with a human-centric warmth that acknowledges the individuals behind the numbers. The target audience includes HR leaders, Chief Diversity Officers, and executive stakeholders who require high-density information without the clinical coldness of traditional BI tools.

The visual style is **Corporate / Modern** with a **Tactile** warmth. It utilizes a vast "white-space-first" architecture to ensure clarity, punctuated by a vibrant multi-chromatic palette that symbolizes the spectrum of human identity. The interface avoids the rigidness of traditional finance apps, opting instead for organic roundedness and soft, expressive interactions that feel welcoming and safe.

## Colors

This design system utilizes a "Diversity Spectrum" palette. To ensure WCAG AAA compliance against a white background, all accent colors have been calibrated for high luminance contrast while maintaining their vibrant saturation.

- **Primary (Teal - #0D7680):** Represents growth and stability. Used for primary actions and core navigation.
- **Secondary (Purple - #7C3AED):** Represents equity and creativity. Used for specialized data segments.
- **Tertiary (Amber - #B45309):** Represents warmth and attention. Used for warning states and highlighting progress.
- **Quaternary (Rose - #BE123C):** Represents humanity and urgency. Used for critical gaps in diversity metrics.
- **Neutrals:** A range of cool grays (Slate) provides the structural scaffolding, ensuring the focus remains on the multi-color data visualizations.

## Typography

The typography strategy prioritizes legibility in data-dense environments. **Manrope** is used for headlines and large data callouts; its modern, geometric construction feels progressive and professional. **Public Sans** is utilized for all body copy and UI labels; its neutral, institutional roots ensure maximum readability for screen readers and users with visual impairments.

For data visualizations, "data-numeral" styling should be applied to ensure figures are prominent and distinct from descriptive text. Line heights are intentionally generous to reduce cognitive load during long reading sessions.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop views to maintain focus and a **Fluid Grid** for mobile devices. The layout is built on a 12-column system with a 24px gutter. 

Spacing follows a strict 4pt linear scale. Large 40px (xl) padding is used to separate major thematic sections of a report, while 16px (md) is the standard for internal card padding. This generous use of space prevents the "data-clutter" common in analytics platforms, reinforcing a sense of calm and clarity.

## Elevation & Depth

Visual hierarchy is established through **Ambient Shadows** and **Tonal Layers**. Instead of harsh black shadows, this design system uses ultra-diffused shadows with a slight tint of the primary Teal color (#0D7680) at 4% opacity.

- **Level 0 (Base):** Pure white background.
- **Level 1 (Cards):** Soft 1px border (#E5E7EB) with a subtle shadow to lift the content.
- **Level 2 (Modals/Popovers):** Deeper shadow to focus attention on the interaction.
- **Tonal Depth:** Secondary information is housed in light gray (#F9FAFB) containers to create a "nested" effect without adding additional shadows.

## Shapes

The shape language is consistently **Rounded**, avoiding sharp corners to maintain a "human-centric" feel. 

- **Standard Buttons & Inputs:** 0.5rem (8px) radius.
- **Data Cards:** 1rem (16px) radius to soften the presentation of complex charts.
- **Feedback Toasts & Chips:** 1.5rem (24px) radius to create a pill-like, friendly appearance.

Icons should feature rounded terminals and consistent stroke weights (1.5px or 2px) to match the curvature of the UI components.

## Components

- **Buttons:** Primary buttons use a solid Teal fill with white text. Secondary buttons use a Rose or Purple outline (2px) to differentiate actions. All buttons include a subtle "bounce" transition on hover.
- **Cards:** Dashboard cards must include a "Highlight Bar" at the top—a 4px horizontal strip using one of the four accent colors to categorize the data type (e.g., Rose for Gender, Teal for Ethnicity).
- **Chips:** Used for filtering and status tags. They feature a low-opacity background of the accent color (10%) with high-contrast text of the same hue for maximum accessibility.
- **Data Inputs:** Fields use a 1px Slate border that transitions to a 2px Teal border on focus. Labels are always persistent above the field, never as placeholder text.
- **Expressive Iconography:** Icons should be multi-tone or utilize "Spot Color" (e.g., a gray icon with a single Teal dot) to add personality to the navigation.
- **Diversity Progress Bars:** Instead of a single color, progress bars should utilize a soft gradient or segmented blocks representing the multi-color palette to reinforce the brand's core mission.