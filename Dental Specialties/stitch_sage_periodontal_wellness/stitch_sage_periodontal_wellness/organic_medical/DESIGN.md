---
name: Organic Medical
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
  on-surface-variant: '#434842'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#747872'
  outline-variant: '#c3c8c0'
  surface-tint: '#516352'
  primary: '#4e604f'
  on-primary: '#ffffff'
  primary-container: '#677967'
  on-primary-container: '#f7fff3'
  inverse-primary: '#b8ccb7'
  secondary: '#605e57'
  on-secondary: '#ffffff'
  secondary-container: '#e3dfd6'
  on-secondary-container: '#64635b'
  tertiary: '#5b5c5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#747573'
  on-tertiary-container: '#fdfcfa'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e8d2'
  primary-fixed-dim: '#b8ccb7'
  on-primary-fixed: '#0f1f12'
  on-primary-fixed-variant: '#3a4b3b'
  secondary-fixed: '#e6e2d9'
  secondary-fixed-dim: '#cac6be'
  on-secondary-fixed: '#1c1c16'
  on-secondary-fixed-variant: '#484740'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

This design system is built upon the "Organic-Medical" aesthetic, a fusion of clinical precision and natural serenity tailored for high-end periodontics. The brand personality is empathetic, authoritative, and tranquil, aiming to reduce patient anxiety associated with dental surgery. 

The design style leans into **Minimalism** with a **Tactile** edge. It utilizes generous whitespace to signify cleanliness and breathing room, while employing soft, layered surfaces to create a sense of approachability. The goal is to move away from the cold, sterile hospital feel toward a restorative, spa-like medical environment.

## Colors

The palette is rooted in nature and stability.
- **Sage Green (Primary):** A muted, organic green used for primary actions, branding elements, and reassuring accents. It represents growth and healing.
- **Warm Stone (Secondary/Neutral):** A sophisticated, warm beige used for backgrounds and container surfaces to avoid the harshness of pure white.
- **Clean White:** Reserved for card faces and input fields to maintain a sense of clinical hygiene.
- **Deep Slate (Neutral Text):** A soft black used for typography to ensure readability without the aggressive contrast of #000000.

## Typography

This design system uses a pairing of **Newsreader** and **Manrope**. 
- **Newsreader** provides a traditional, authoritative serif voice for headlines, suggesting years of medical expertise and academic rigor.
- **Manrope** offers a balanced, modern sans-serif feel for body copy and UI labels, ensuring clarity and a progressive, tech-forward outlook on dental health. 

Use Newsreader for all editorial headings and Manrope for instructional text, buttons, and navigation.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop, transitioning to a fluid single-column for mobile.
- Use a 12-column grid with 24px gutters.
- Vertical rhythm is highly spacious; section margins should typically be `xl` (80px) to prevent the interface from feeling "crowded" or stressful.
- Alignment should be primarily center-weighted for marketing sections and left-aligned for clinical information and forms.

## Elevation & Depth

Depth is achieved through **Ambient Shadows** and tonal layering. 
- Avoid heavy, dark shadows. Instead, use "Organic Glows"—soft, multi-layered shadows with a slight Sage Green or Warm Stone tint in the blur to make elements feel like they are floating gently above the surface.
- Surfaces should use a subtle hierarchy: the `Warm Stone` background is the lowest level, and `Clean White` cards sit atop it with a soft shadow (Blur: 20px, Y: 10px, Opacity: 4%).

## Shapes

The shape language is defined by comfort. All corners are rounded to remove visual "points" of tension.
- Standard components (buttons, inputs) use a `0.5rem` radius.
- Larger containers and treatment cards use `1.5rem` radius (`rounded-xl`).
- Imagery should always feature rounded corners or soft-masked organic edges to match the typography's curves.

## Components

### Sticky Mobile Appointment Bar
A persistent footer component on mobile devices. It features a translucent "Warm Stone" glass effect background with a single, high-contrast Sage Green button labeled "Request Consultation." This ensures the primary conversion goal is always within thumb-reach.

### Soft Treatment Cards
Used for displaying services like "Dental Implants" or "Gum Grafting." These cards use a white background, a soft shadow, and a top-aligned placeholder for professional imagery. Text within the card should lead with a Newsreader H3 and follow with Manrope body text.

### Medical Imagery Placeholders
Placeholders for clinical photos should use a desaturated, high-key style. When actual medical photography is used, apply a subtle warm filter to align the reds/pinks of gingival tissue with the "Warm Stone" palette, making them less jarring.

### Buttons & Inputs
- **Primary Button:** Solid Sage Green with white Manrope text.
- **Secondary Button:** Outlined Sage Green or ghost style.
- **Inputs:** White background with a `Warm Stone` border that shifts to `Sage Green` on focus. Labels sit outside the field in "label-caps" style.