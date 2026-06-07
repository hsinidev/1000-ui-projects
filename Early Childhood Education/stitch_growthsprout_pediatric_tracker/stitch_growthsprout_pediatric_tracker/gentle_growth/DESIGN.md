---
name: Gentle Growth
colors:
  surface: '#f8f9ff'
  surface-dim: '#d1dbec'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dfe9fa'
  surface-container-highest: '#d9e3f4'
  on-surface: '#121c28'
  on-surface-variant: '#474552'
  inverse-surface: '#27313e'
  inverse-on-surface: '#eaf1ff'
  outline: '#787583'
  outline-variant: '#c8c4d4'
  surface-tint: '#5950b6'
  primary: '#5950b6'
  on-primary: '#ffffff'
  primary-container: '#9d94ff'
  on-primary-container: '#32258d'
  inverse-primary: '#c6c0ff'
  secondary: '#1b6b4f'
  on-secondary: '#ffffff'
  secondary-container: '#a6f2cf'
  on-secondary-container: '#247155'
  tertiary: '#5c5f60'
  on-tertiary: '#ffffff'
  tertiary-container: '#9fa1a2'
  on-tertiary-container: '#353839'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4dfff'
  primary-fixed-dim: '#c6c0ff'
  on-primary-fixed: '#150066'
  on-primary-fixed-variant: '#41369d'
  secondary-fixed: '#a6f2cf'
  secondary-fixed-dim: '#8bd6b4'
  on-secondary-fixed: '#002115'
  on-secondary-fixed-variant: '#00513a'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f8f9ff'
  on-background: '#121c28'
  surface-variant: '#d9e3f4'
typography:
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Lexend
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  gutter: 16px
  margin: 20px
---

## Brand & Style

The design system is centered on empathy, reassurance, and clarity. It caters to parents navigating the complexities of pediatric care, providing a digital environment that feels like a supportive embrace rather than a clinical tool. The brand personality is "Nurturing Professionalism"—it is soft enough to feel approachable for a nursery setting, yet precise enough to be trusted for medical data.

The aesthetic utilizes **Soft-UI Neumorphism**, characterized by extruded surfaces that appear to emerge from the background. By moving away from flat design and into a tactile, "squishy" world of soft shadows and highlights, the interface creates a calming, low-stress user experience. High-quality whitespace and a minimal color application ensure that the focus remains on the child's health milestones.

## Colors

The color palette for this design system is rooted in the concept of serenity. 

- **Primary (Lavender):** Used for key actions and growth milestones. It provides a sense of calm and spiritual balance.
- **Secondary (Mint):** Used for health indicators and success states. It reflects freshness, healing, and nature.
- **Neutral (White & Soft Gray):** The background is a crisp, clean white, while a very light gray is used for the "sunken" or "raised" neumorphic depth effects.
- **Text:** Deep muted grays are used instead of pure black to maintain a soft visual contrast that is gentle on tired eyes.

## Typography

This design system utilizes **Lexend**, a font family specifically designed to reduce visual stress and improve reading proficiency. Its open counters and rhythmic spacing make it exceptionally legible for parents who may be checking stats in low-light conditions or while multitasking.

Headlines are set with a medium-to-bold weight to provide clear hierarchy without feeling aggressive. Body text maintains a generous line height (1.6) to ensure that health logs and medical notes are easy to scan. Labels use slightly increased letter spacing and a higher font weight to remain distinct even at smaller sizes.

## Layout & Spacing

This design system employs a **Fluid Grid** model with a focus on generous padding. To support the neumorphic style, elements require "breathing room" for their shadows to bleed naturally without overlapping adjacent components.

The spacing rhythm is based on a 4px baseline grid. Layouts should prioritize vertical stacking for mobile ease-of-use. Containers typically utilize `lg` (24px) or `xl` (32px) padding to create a luxurious, spacious feel. Gutters are kept at a consistent 16px to maintain clear separation between cards while maximizing the available screen real estate for health charts.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. We use a **dual-shadow neumorphic approach**:

1.  **Raised Elements:** These appear to pop out of the background. They use a light shadow (white) on the top-left and a soft, muted lavender or gray shadow on the bottom-right.
2.  **Sunken Elements:** Used for input fields or active button states. The shadows are reversed and placed *inside* the element to create an "inset" look.
3.  **Softness:** Shadows must be highly diffused (blur radius should be at least double the offset) and low opacity (10-15%) to avoid a "dirty" or heavy look. 

Avoid using traditional high-contrast drop shadows. Every elevated surface must feel like it is part of the same continuous material as the background.

## Shapes

The shape language is dominated by **extreme roundedness**. There are no sharp corners in this design system.

All interactive elements, such as buttons and cards, use pill-shaped or high-radius corners. This choice reflects the safety-first nature of pediatric products—mimicking "child-safe" rounded furniture and toys. Large containers (cards) should use `rounded-xl` (3rem), while smaller elements like chips and buttons should be fully rounded (pill-shaped).

## Components

- **Buttons:** Primary buttons are Lavender with white text, featuring a subtle raised neumorphic effect. Secondary buttons use the Mint color.
- **Cards:** These are the primary vessels for health data. They must have a subtle background color that matches the app background, distinguished only by their soft dual-shadow borders.
- **Input Fields:** These should appear "hollowed out" or sunken into the UI. Use the inset shadow technique to make them feel tactile.
- **Chips:** Small, pill-shaped tags used for categorizing events (e.g., "Feeding," "Sleep," "Vaccine"). These should use very low-saturation versions of the Lavender and Mint colors.
- **Progress Trackers:** Custom-designed "Growth Bars" using soft gradients of Mint to Lavender, appearing recessed into the page.
- **Milestone Icons:** Simple, monoline icons with rounded caps, housed inside small raised circular "bubbles."