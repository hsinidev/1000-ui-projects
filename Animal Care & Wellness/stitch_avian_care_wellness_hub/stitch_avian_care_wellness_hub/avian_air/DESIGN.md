---
name: Avian Air
colors:
  surface: '#f9f9ff'
  surface-dim: '#d4daea'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e8eeff'
  surface-container-high: '#e3e8f9'
  surface-container-highest: '#dde2f3'
  on-surface: '#161c27'
  on-surface-variant: '#3f484c'
  inverse-surface: '#2a303d'
  inverse-on-surface: '#ecf0ff'
  outline: '#6f787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0c6780'
  primary: '#0c6780'
  on-primary: '#ffffff'
  primary-container: '#87ceeb'
  on-primary-container: '#005870'
  inverse-primary: '#89d0ed'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#865219'
  on-tertiary: '#ffffff'
  tertiary-container: '#fbb674'
  on-tertiary-container: '#76450c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#baeaff'
  primary-fixed-dim: '#89d0ed'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d62'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdcbf'
  tertiary-fixed-dim: '#feb876'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6a3b01'
  background: '#f9f9ff'
  on-background: '#161c27'
  surface-variant: '#dde2f3'
typography:
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Newsreader
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  button:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system centers on a sense of weightlessness, precision, and warmth, tailored specifically for bird owners and their avian companions. The brand personality is **Nurturing, Specialized, and Uplifting**. It moves away from the sterile, heavy feel of traditional veterinary clinics toward a bright, "sky-first" aesthetic that evokes the natural environment of birds.

The visual style is a hybrid of **Minimalism** and **Modern Corporate**. It prioritizes extreme clarity and vast whitespace to reduce cognitive load for pet owners who may be stressed about their bird's health. High contrast ensures accessibility, while the soft, rounded geometry mirrors the organic forms of feathers and nests, creating a friendly and approachable atmosphere.

## Colors

The palette is dominated by **Sky Blue** and **White** to maintain the airy, open-sky feel. Sky Blue is used for primary actions and brand identifiers, while White serves as the primary canvas to maximize light. 

**Tropical Orange** is reserved strictly for high-priority calls to action (CTAs), such as "Book Appointment" or "Emergency Contact," providing a warm, high-contrast focal point that guides the user's eye instantly. 

For typography and borders, a deep charcoal neutral is used instead of pure black to maintain a softer professional look. Background tints of very pale blue (#F0F9FF) are utilized to differentiate sections without breaking the minimalist aesthetic.

## Typography

This design system employs a sophisticated pairing of **Plus Jakarta Sans** for headlines and **Newsreader** for body text. 

- **Plus Jakarta Sans** provides a modern, geometric, and friendly feel for titles and navigation. Its slightly rounded terminals complement the overall shape language.
- **Newsreader** is used for body copy to provide an authoritative, editorial, and highly legible experience, particularly for medical advice and blog content. This serif choice adds a layer of veterinary expertise and "trust" to the clinic's digital presence.

Headlines should use tight tracking and generous leading to maintain a clean, organized hierarchy.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop (12 columns) and a fluid 4-column model for mobile. To achieve the "airy" look, the design system utilizes an aggressive white-space strategy:

1. **Large Section Padding:** Use `xl` (80px) spacing between major sections to allow the content to breathe.
2. **Generous Gutters:** A 24px gutter ensures that elements never feel cramped.
3. **Information Density:** Keep density low. Information should be grouped into clear, logical clusters with ample negative space around them to prevent visual clutter.

## Elevation & Depth

To maintain the clean and professional aesthetic, this design system avoids heavy drop shadows. Instead, it uses **Ambient Shadows** and **Tonal Layers**:

- **Level 0 (Base):** White (#FFFFFF) background.
- **Level 1 (Cards/Surface):** A very subtle, extra-diffused shadow (Blur: 20px, Y: 4px, Opacity: 4%) with a hint of Sky Blue in the shadow color to give a "floating" effect.
- **Interactive Depth:** On hover, cards should slightly lift (increasing shadow spread) rather than changing color, maintaining the bright aesthetic.
- **Glassmorphism:** Use subtle backdrop blurs (10px) for the main navigation bar to suggest transparency and airiness as the user scrolls.

## Shapes

The shape language is consistently **Rounded**, avoiding sharp corners to evoke a sense of safety and friendliness. 

- **Buttons & Chips:** Use a full pill-shape (3rem radius) for a soft, tactile feel.
- **Cards & Containers:** Use the `rounded-lg` (1rem) setting to provide a structural but soft frame.
- **Input Fields:** Follow the `rounded-md` (0.5rem) standard to balance professionalism with the friendly brand tone.
- **Icons:** Should be feather-light, using 1.5pt or 2pt stroke weights with rounded caps and joins.

## Components

### Buttons
- **Primary:** Sky Blue background with White text. Pill-shaped.
- **CTA:** Tropical Orange background with White text. Reserved for "Book Appointment" or "Shop Now."
- **Secondary:** Transparent background with a Sky Blue border.

### Cards
- **Blog Cards:** Featured image with a 1rem top-radius, followed by a large white area for the title (Plus Jakarta Sans) and a brief excerpt (Newsreader).
- **Product Cards:** Centered product image on a pale blue (#F0F9FF) rounded square, with price and "Add to Cart" clearly separated by whitespace.

### Search & Forms
- **Search Bar:** A robust, wide bar with a 2rem radius. Use a light Sky Blue tint for the search icon.
- **Form Fields:** Large tap targets with 16px internal padding. Labels stay above the field in `label-md` style. Focus states use a 2px Sky Blue ring.

### Specialized Components
- **Health Indicators:** Small, rounded chips used for bird species categorization (e.g., "Parrot," "Finch") using pastel variants of the brand colors.
- **Appointment Timeline:** A vertical stepper with soft rounded nodes to guide owners through the check-in process.