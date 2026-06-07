---
name: OncoShield
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#43474e'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#74777f'
  outline-variant: '#c4c6d0'
  surface-tint: '#455f8a'
  primary: '#000e24'
  on-primary: '#ffffff'
  primary-container: '#00234b'
  on-primary-container: '#718bb9'
  inverse-primary: '#adc7f8'
  secondary: '#46654f'
  on-secondary: '#ffffff'
  secondary-container: '#c5e8cc'
  on-secondary-container: '#4a6a53'
  tertiary: '#0c0e0f'
  on-tertiary: '#ffffff'
  tertiary-container: '#212425'
  on-tertiary-container: '#898b8c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f8'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2c4771'
  secondary-fixed: '#c7ebcf'
  secondary-fixed-dim: '#accfb3'
  on-secondary-fixed: '#02210f'
  on-secondary-fixed-variant: '#2e4d38'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
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
    lineHeight: '1.6'
  label-bold:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  caption:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is rooted in the "Courageous & Solid" aesthetic, designed specifically for the high-stakes environment of surgical oncology. The brand personality is one of unwavering support—combining the clinical authority of a top-tier surgeon with the compassionate presence of a dedicated caregiver. 

The visual style is **Corporate / Modern** with a lean toward medical minimalism. It avoids the coldness of typical healthcare portals by utilizing a structured, information-rich layout that prioritizes clarity and patient confidence. The UI must feel architectural and stable, using "solid" elements—thick borders where necessary, grounded color blocks, and ample whitespace—to evoke a sense of safety and permanence. Every interaction is designed to reduce anxiety through predictability and high legibility.

## Colors

The color palette centers on Navy Blue to establish an immediate sense of trust and institutional stability. This is balanced by Sage Green, which serves as a "healing" accent for progress indicators, success states, and renewal-themed content. 

- **Primary (Navy Blue):** Used for global navigation, primary buttons, and structural headers to anchor the experience.
- **Secondary (Sage Green):** Applied to highlights, callouts, and health-positive indicators to provide a soothing counterpoint to the deep navy.
- **Surface (White/Off-white):** A high-clarity background strategy ensures a sterile, professional environment that maximizes text contrast.
- **Neutral:** A range of slate grays is used for secondary text and borders to maintain a sophisticated, non-distracting hierarchy.

## Typography

This design system utilizes a sophisticated typographic pairing to balance authority with accessibility. 

**Newsreader** is the primary serif for headings. Its traditional, literary proportions convey clinical expertise and a "classic" medical journal authority. It should be used for page titles and major section headers.

**Public Sans** is used for all body copy, forms, and UI labels. As an institutional sans-serif, it provides exceptional legibility at small sizes and maintains a neutral, trustworthy tone. 

- Use a generous line height (1.6) for body text to ensure long-form medical information is easy to digest without eye strain.
- Heading weights should remain Medium to Semi-Bold; avoid Heavy weights to prevent the UI from feeling aggressive.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop to ensure content remains focused and legible, centering the narrative on the patient’s journey.

- **Grid:** A 12-column system with 24px gutters.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Density:** The system prioritizes a "breathable" layout. Avoid cramming data; use significant vertical "stack" spacing (48px+) between major sections to allow the user's eyes to rest. 
- **Alignment:** Consistent left-alignment is required for all medical data to aid rapid scanning and professional clarity.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. This keeps the interface feeling "solid" and grounded on the page.

- **Planes:** Surfaces use subtle shifts in background color (e.g., from White to a very light Sage-tinted Grey) to distinguish between navigation and content.
- **Borders:** Use 1px solid borders in a light neutral tint for cards and input fields. This creates a "contained" and secure feeling for medical records.
- **Shadows:** When necessary for modals or floating actions, use "Ambient Shadows"—extremely soft, long-spread blurs with low opacity (5-8%) to imply a gentle lift without breaking the clean, clinical aesthetic.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding of corners strikes a balance between the precision of surgery (sharp) and the comfort of care (round). 

- **Standard Elements:** Buttons and input fields use a 4px (0.25rem) radius.
- **Containers:** Large cards or content blocks may use an 8px (0.5rem) radius to feel more approachable.
- **Icons:** Should be encased in square or slightly rounded frames, emphasizing the "shield" aspect of the brand.

## Components

- **Buttons:** Primary buttons are Navy Blue with White text, using a solid, high-contrast appearance. Secondary buttons should use a Sage Green outline to signal "healing" actions like "Save Progress" or "Book Consultation."
- **Cards:** White backgrounds with a subtle 1px border. No heavy drop shadows. Use Sage Green for "Success" accents or status headers.
- **Input Fields:** Clearly labeled using Public Sans Bold. Borders should darken slightly on focus to Navy Blue to provide a "grounded" interaction state.
- **Chips/Badges:** Used for medical tags or status (e.g., "Post-Op," "Consultation Ready"). These use a desaturated version of the Sage Green with dark green text for maximum legibility.
- **Progress Indicators:** Linear steppers are preferred over circular ones to represent a clear, courageous "path forward" in the oncology journey.
- **Specialty Component - The "Shield Header":** A persistent information bar at the top of patient records that uses a Navy Blue background to hold critical, high-level data in a condensed, authoritative format.