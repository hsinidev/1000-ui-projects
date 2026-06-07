---
name: SereneMind
colors:
  surface: '#f4faff'
  surface-dim: '#cfdce4'
  surface-bright: '#f4faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e9f6fd'
  surface-container: '#e3f0f8'
  surface-container-high: '#ddeaf2'
  surface-container-highest: '#d7e4ec'
  on-surface: '#111d23'
  on-surface-variant: '#42484b'
  inverse-surface: '#263238'
  inverse-on-surface: '#e6f3fb'
  outline: '#72787b'
  outline-variant: '#c2c7cb'
  surface-tint: '#48626e'
  primary: '#3c5661'
  on-primary: '#ffffff'
  primary-container: '#546e7a'
  on-primary-container: '#d4f0fe'
  inverse-primary: '#afcbd8'
  secondary: '#516161'
  on-secondary: '#ffffff'
  secondary-container: '#d4e6e5'
  on-secondary-container: '#576867'
  tertiary: '#51534f'
  on-tertiary: '#ffffff'
  tertiary-container: '#696b67'
  on-tertiary-container: '#ecece7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cbe7f5'
  primary-fixed-dim: '#afcbd8'
  on-primary-fixed: '#021f29'
  on-primary-fixed-variant: '#304a55'
  secondary-fixed: '#d4e6e5'
  secondary-fixed-dim: '#b8cac9'
  on-secondary-fixed: '#0e1e1e'
  on-secondary-fixed-variant: '#3a4a49'
  tertiary-fixed: '#e3e3de'
  tertiary-fixed-dim: '#c6c7c2'
  on-tertiary-fixed: '#1a1c19'
  on-tertiary-fixed-variant: '#454744'
  background: '#f4faff'
  on-background: '#111d23'
  surface-variant: '#d7e4ec'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
  button:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  section-gap: 80px
---

## Brand & Style

The design system is anchored in the principles of **Soft Minimalism**. It is designed specifically for licensed therapists, prioritizing an environment of psychological safety, clinical professionalism, and digital serenity. The UI avoids cognitive overload by utilizing expansive whitespace and a restrained palette that mirrors a modern, tranquil physical office.

The emotional objective is to reduce the "clinical friction" often associated with medical software. By blending functional clarity with a rhythmic, breathable layout, this design system ensures that practitioners can focus entirely on patient care without visual distraction.

## Colors

The palette uses a "Therapeutic Blue & Sand" motif to establish trust.
- **Primary (#546E7A):** A Slate Blue used for interactive elements, headers, and primary actions. It provides the necessary contrast for clinical authority.
- **Secondary (#E0F2F1):** A Soft Teal/Blue used for large background surfaces and subtle highlighting.
- **Tertiary (#F5F5F0):** A warm Sand/Off-white used to soften the "starkness" of pure white, providing a tactile, paper-like quality to the interface.
- **Neutral (#263238):** A deep charcoal for high-contrast typography, ensuring maximum readability for practitioners during long sessions.

## Typography

This design system utilizes **Manrope** as the primary typeface due to its balanced, modern, and highly legible characteristics. It provides a geometric yet humanistic touch. Headlines are set with tighter letter-spacing for a grounded feel, while body text uses generous line heights (1.6) to prevent eye fatigue during clinical documentation.

**Public Sans** is utilized for functional labels and navigation items to provide a distinct, institutional clarity that signals reliability and accessibility.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to maintain a consistent reading line, which is essential for reviewing patient histories. On smaller viewports, it transitions to a fluid model with generous margins.

The spacing rhythm is based on an 8px base unit. To achieve the "Soft Minimalist" aesthetic, the design system mandates significantly larger section gaps (80px+) than standard SaaS platforms, ensuring that each functional area has "room to breathe." Vertical rhythm should prioritize white space over horizontal dividers.

## Elevation & Depth

This design system avoids traditional heavy drop shadows. Instead, it utilizes **Tonal Layering** and **Ambient Shadows**. 

Depth is communicated by placing #FFFFFF (White) cards on top of #F5F5F0 (Sand) or #E0F2F1 (Soft Teal) backgrounds. Shadows, when used, are extremely diffused: `0px 4px 20px rgba(84, 110, 122, 0.08)`. This creates a "lifted" effect that feels light and airy rather than heavy or artificial. Low-contrast outlines in a slightly darker shade of the background color are preferred over shadows for defining interactive input zones.

## Shapes

The shape language is defined by significant roundedness to convey safety and approachable care. Standard containers use a 0.5rem (8px) radius, while larger cards and modal overlays utilize a 1rem (16px) radius. Sharp 90-degree angles are strictly avoided to maintain the "soft" brand promise. 

Buttons should feel substantial but soft; use a 1rem radius for standard buttons, and fully "pill-shaped" radii for status chips and tags.

## Components

- **Buttons:** Primary buttons use a solid Slate Blue fill with white text. Secondary buttons use a transparent fill with a 1px Slate Blue border. Avoid "ghost" buttons for primary clinical actions.
- **Input Fields:** Soft Sand (#F5F5F0) background with a 1px border that darkens on focus. Labels should always be visible above the field in Public Sans.
- **Cards:** White backgrounds with a 16px corner radius and an 8% Slate Blue ambient shadow. Avoid borders on cards unless they are placed on a white background.
- **Status Chips:** Use highly desaturated versions of semantic colors (e.g., soft sage for "Active", soft amber for "Pending") with 100px border-radius.
- **Patient Timeline:** A unique vertical component using a soft teal line and circular nodes to represent session history, emphasizing the "SereneMind" journey.
- **Lists:** High-contrast text on alternating Soft Teal and White rows with generous internal padding (16px-24px).