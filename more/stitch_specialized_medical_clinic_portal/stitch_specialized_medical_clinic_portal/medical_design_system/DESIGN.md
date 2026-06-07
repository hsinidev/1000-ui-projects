---
name: Medical Design System
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#3e4949'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#6f7979'
  outline-variant: '#bec9c9'
  surface-tint: '#01696c'
  primary: '#006669'
  on-primary: '#ffffff'
  primary-container: '#2a7f82'
  on-primary-container: '#ebffff'
  inverse-primary: '#85d4d6'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#4d5c72'
  on-tertiary: '#ffffff'
  tertiary-container: '#65758c'
  on-tertiary-container: '#fcfbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a1f0f3'
  primary-fixed-dim: '#85d4d6'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#004f52'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
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
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  caption:
    fontFamily: Public Sans
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 80px
---

## Brand & Style

The visual identity of the design system is anchored in the concepts of "Clinical Precision" and "Empathetic Care." It utilizes a **Modern Corporate** aesthetic filtered through a **Minimalist** lens to ensure the interface never feels overwhelming for patients or practitioners. 

The goal is to evoke a sense of clinical expertise without the sterile coldness often associated with medical environments. This is achieved through the use of expansive white space, a breathy layout, and high-quality professional imagery that depicts human connection and advanced technology. The design system prioritizes clarity and accessibility above all, ensuring that users in potentially high-stress situations can navigate the interface with ease and confidence.

## Colors

The palette is intentionally restrained to maintain a serene atmosphere. 

- **Primary (Soft Teal):** Used for primary actions, branding elements, and active states. It provides a sense of growth and healing.
- **Secondary (Slate Grey):** Utilized for secondary buttons, icons, and supporting information.
- **Typography:** Primary text uses a deep Slate (#1E293B) to ensure maximum contrast against white backgrounds, exceeding WCAG AAA standards.
- **Functional Colors:** Success and error states use desaturated versions of green and red to maintain the calming tone while still providing clear feedback.
- **White Space:** The "color" of the background is as important as the brand colors; generous use of white creates a clean, sanitary, and organized feel.

## Typography

This design system uses a dual-font strategy to balance character with institutional clarity.

- **Manrope** is used for headings to provide a modern, refined, and approachable personality. Its geometric yet soft construction feels high-tech and human.
- **Public Sans** is the workhorse for all body copy and UI elements. It was chosen for its exceptional legibility at small sizes and its neutral, trustworthy tone.

Strong hierarchy is established through significant scale differences between headers and body text. Line heights are kept generous (minimum 1.5 for body) to reduce cognitive load and improve readability for older patients or those with visual impairments.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop, centering content within a 1280px max-width container to prevent line lengths from becoming too long for comfortable reading. 

Spacing follows a strict 8px linear scale. Large section gaps (80px+) are used to separate different medical services or informational blocks, ensuring the "plenty of white space" requirement is met. Components within cards use a standard 24px internal padding to provide elements room to breathe. Navigation and critical information should always align with the 12-column grid to maintain a sense of expert organization.

## Elevation & Depth

To maintain a serene and clean aesthetic, the design system avoids heavy shadows or complex textures. Instead, it utilizes **Ambient Shadows** and **Tonal Layers**.

- **Level 1 (Base):** Flat white background.
- **Level 2 (Cards/Containers):** Subtle, extra-diffused shadows (e.g., `0 4px 20px rgba(71, 85, 105, 0.05)`) with a slight slate-grey tint. 
- **Level 3 (Hover/Modals):** A more pronounced but still soft shadow to indicate interactivity or focus.

Interactive elements use a 1px border in a light Slate Grey (#E2E8F0) to define boundaries without adding visual weight. Depth is primarily communicated through color-blocking with the subtle Surface Grey (#F8FAFC) to distinguish different content zones.

## Shapes

The design system employs **Rounded** shapes to convey approachability and care. Sharp corners are avoided as they can feel aggressive or clinical in an unwelcoming way.

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) corner radius.
- **Container Elements:** Large cards and section containers use a 1rem (16px) radius to create a soft, modern container for information.
- **Form Elements:** Checkboxes use a small 4px radius to balance the rounded language with the precision required for functional UI.

## Components

### Buttons
Primary buttons use a solid Soft Teal background with white text. Hover states shift the background to a slightly deeper shade. Focus states must feature a high-contrast 2px offset ring.

### Cards
Cards are the primary organizational unit. They should feature a white background, the Level 2 ambient shadow, and 24px padding. Medical practitioner cards should include circular or soft-rounded profile imagery.

### Input Fields
Inputs use a white background with a 1px Slate Grey border. Active focus states utilize a Teal border with a soft outer glow. Labels are always positioned above the field for maximum legibility.

### Chips & Badges
Used for medical categories or status updates (e.g., "Available", "Specialty"). These use desaturated background tints of the primary or functional colors with darkened text to ensure legibility while remaining subtle.

### Specialized Medical Components
- **Appointment Timeline:** A vertical stepper using the Soft Teal for the "current" state and Slate for "upcoming."
- **Doctor Profile:** A structured layout combining high-quality imagery with clear Manrope headers for credentials.
- **Search/Filter Bar:** A prominent, clean input group used for finding specialists, emphasizing the "Accessible" brand trait.