---
name: ArtsCivic
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1b1b1b'
  on-surface-variant: '#4c4546'
  inverse-surface: '#303030'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#bc0100'
  on-secondary: '#ffffff'
  secondary-container: '#ea0703'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1b1b1b'
  on-tertiary-container: '#848484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#930100'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1b1b1b'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 80px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  margin-mobile: 24px
  margin-desktop: 80px
  gutter: 16px
  asymmetric-offset: 120px
---

## Brand & Style
The design system is rooted in the "Gallery as Interface" philosophy. It evokes the prestige of a high-end institution through a rigorous adherence to minimalism and white space. The aesthetic is sophisticated and intellectual, designed to act as a silent frame for the student and faculty work it showcases. 

The primary style is **Minimalist with Editorial influence**, utilizing high-contrast visuals and intentional asymmetry to create a sense of rhythm and discovery. The emotional response is one of reverence and immersion, stripping away standard UI patterns in favor of a "white cube" digital experience that prioritizes visual art over decorative interface elements.

## Colors
The palette is intentionally stark to maximize the impact of artistic content. 

- **Pure White (#FFFFFF):** Used for the vast majority of the canvas to provide "breathable" space and a gallery-like backdrop.
- **Deep Black (#000000):** Used for primary typography and structural borders to ensure maximum legibility and authority.
- **Bold Accent Red (#E60000):** Reserved strictly for high-priority calls to action, active states, and critical highlights. It represents the "curator's mark."
- **Soft Neutral (#F5F5F5):** Occasional use for secondary backgrounds or image placeholders to provide subtle depth without breaking the minimalist aesthetic.

## Typography
This design system employs a high-contrast typographic pairing to mirror the look of a printed art catalog. 

- **Headings:** Use **Noto Serif**. This font provides the "Sophisticated" and "Traditional" authority of a fine arts institution. Headlines should often use "Display" sizing to dominate the layout.
- **Body & Interface:** Use **Manrope**. This modernist sans-serif offers a clean, neutral counterpoint to the serif headings. Its geometric but refined nature ensures readability in dense descriptions of artwork.
- **Labels:** Use uppercase **Manrope** with increased letter spacing for a curated, architectural feel on metadata and tags.

## Layout & Spacing
The layout follows an **asymmetrical editorial grid**. Unlike standard symmetrical web layouts, this design system pushes content off-center to create visual tension and interest.

- **Asymmetry:** Content blocks should alternate between left-aligned and right-aligned with significant "white gaps."
- **Immersive Gallery:** Images should often break the grid, spanning from the center to the far edge of the screen (Full-bleed on one side).
- **Whitespace:** Use aggressive vertical padding between sections (120px+) to ensure each piece of content feels like its own "exhibit."
- **Mobile-first:** On small screens, the layout collapses into a single-column immersive flow, while the navigation remains hidden behind a minimalist "Menu" trigger.

## Elevation & Depth
This design system rejects shadows and traditional depth metaphors. Depth is achieved through **Tonal Layering** and **Scale** rather than artificial light sources.

- **Flat Aesthetic:** No ambient shadows or blurs. Use solid 1px black borders or shifts from white to light grey (#F5F5F5) to define areas.
- **Overlays:** For immersive galleries, use full-screen black overlays with white text to shift the user's focus entirely to the content.
- **Foreground/Background:** Use high-contrast overlap where text may partially sit over an image to create a sophisticated, layered look typical of contemporary print design.

## Shapes
The shape language is strictly **Sharp (0px)**. 

Every element—including buttons, input fields, image containers, and cards—must have 90-degree corners. This reinforces the "architectural" and "prestigious" nature of the school, mimicking the hard edges of a picture frame or a structural blueprint.

## Components
- **Buttons:** Primary buttons are solid Black with White text. Secondary buttons are Ghost-style with a 1px Black border. All hover states trigger a transition to the Accent Red (#E60000).
- **Navigation:** A "Hidden" drawer approach. The trigger is a simple "MENU" text label or a thin two-line icon. The menu itself is a full-screen takeover with large-scale serif links.
- **Cards:** Cards for artwork should have no visible borders or backgrounds by default. The image is the hero, with typography (Title in Noto Serif, Artist in Manrope) appearing beneath or overlapping upon hover.
- **Inputs:** Simple bottom-border only (1px Black). Labels are small, uppercase Manrope.
- **Immersive Gallery:** A horizontal-scroll or staggered vertical masonry component that prioritizes high-resolution imagery with minimal UI chrome.
- **Breadcrumbs & Metadata:** Use small-caps or spaced-out labels to give the impression of museum wall text.