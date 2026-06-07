---
name: Clinical-Elite
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#43474f'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#737780'
  outline-variant: '#c3c6d1'
  surface-tint: '#3a5f94'
  primary: '#001e40'
  on-primary: '#ffffff'
  primary-container: '#003366'
  on-primary-container: '#799dd6'
  inverse-primary: '#a7c8ff'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#1d1f1f'
  on-tertiary: '#ffffff'
  tertiary-container: '#323434'
  on-tertiary-container: '#9b9c9c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3ff'
  primary-fixed-dim: '#a7c8ff'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#1f477b'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
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

This design system embodies the "Clinical-Elite" aesthetic, tailored for the high-stakes environment of prestigious medical institutions. The brand personality is authoritative, precise, and uncompromisingly professional. It prioritizes clarity over decoration, evoking an emotional response of absolute trust and institutional excellence.

The visual style is a refined **Corporate Modern** approach with **Minimalist** discipline. It utilizes high-contrast interfaces to ensure legibility in high-pressure clinical settings. The aesthetic avoids unnecessary depth, instead relying on crisp structural lines and generous whitespace to organize complex medical data. Every visual element is designed to feel like a precision instrument: cold, clean, and reliable.

## Colors

The palette is anchored by **Deep Blue (#003366)**, representing institutional authority, scientific rigor, and trust. This is offset by **Sterile White (#FFFFFF)** which serves as the primary canvas, ensuring a hygienic and open feel. **Silver (#C0C0C0)** is utilized for structural elements, borders, and secondary details to introduce a high-tech, metallic precision.

Color application is strictly functional. Deep Blue is reserved for primary actions and brand headers. Silver is used for "hairline" borders and inactive states. Functional status colors (Critical, Stable, Warning) are high-chroma variants to ensure they pierce through the clinical neutral palette for immediate recognition of patient or system status.

## Typography

The typography system relies exclusively on **Inter**, chosen for its tall x-height and exceptional legibility in digital interfaces. In a medical context, the distinction between similar characters (like 'i', 'I', and '1') is critical to prevent errors.

Headlines use tighter tracking and heavier weights to project authority. Body text is optimized for long-form clinical notes with increased line height. A specialized "Data Mono" style (utilizing Inter's tabular lining features) is designated for vital signs, lab results, and timestamps to ensure vertical alignment in high-density data tables.

## Layout & Spacing

This design system employs a **Fixed Grid** model on a 4px baseline to achieve surgical precision. Layouts are structured around a 12-column system with generous 24px gutters to prevent information density from becoming overwhelming.

Whitespace is treated as a functional tool to separate distinct clinical modules (e.g., Patient Info vs. Treatment Plan). Margins are wide (32px+) to provide visual breathing room, ensuring that even when a screen is crowded with data, the user's eye can quickly find the required entry point.

## Elevation & Depth

Elevation in this design system is achieved primarily through **Bold Borders** and **Tonal Layers** rather than soft shadows. This maintains the "flat-clinical" aesthetic. 

- **Surface Levels:** The base layer is always Sterile White. Secondary modules (sidebars or inspector panels) use a very light Silver tint or a 1px Silver border.
- **Borders:** All containers use a crisp 1px border in Silver (#C0C0C0). 
- **Active State Elevation:** Only the highest-priority modals or pop-overs use a minimal, high-precision shadow (4px blur, 10% opacity Deep Blue) to suggest they are temporarily "floating" above the clinical workspace. 
- **Focus:** Active input states use a 2px Deep Blue border.

## Shapes

The shape language is strictly **Sharp (0px)**. All containers, buttons, and input fields utilize 90-degree corners. This evokes a sense of technical precision, architectural stability, and the "no-frills" nature of medical equipment. The only exceptions are circular indicators for status (e.g., "Stable" pulse dots) and toggle switches, where the geometry serves a specific functional metaphor.

## Components

- **Buttons:** High-contrast, sharp-edged rectangles. Primary buttons are solid Deep Blue with White text. Secondary buttons are White with a 1px Silver border and Deep Blue text.
- **Clinical Status Indicators:** Use a "Badge" system with high-contrast fills for critical alerts and 1px outlined borders for non-urgent status updates.
- **Data Charts:** Use high-contrast line graphs with 2px stroke weights. Grid lines must be Silver (#C0C0C0) at 0.5px thickness to remain visible but unobtrusive.
- **Input Fields:** Strict rectangular boxes with 1px Silver borders. Labels are always positioned above the field in `label-caps` style for maximum clarity.
- **Cards/Modules:** Defined by 1px Silver borders and no shadows. Headers within cards should have a thin Silver divider line separating the title from the content.
- **Iconography:** Use "Medical-Grade" icons—thin, consistent 2px stroke weights, non-rounded terminals, and strictly functional metaphors (e.g., a precise heart shape, a literal beaker).