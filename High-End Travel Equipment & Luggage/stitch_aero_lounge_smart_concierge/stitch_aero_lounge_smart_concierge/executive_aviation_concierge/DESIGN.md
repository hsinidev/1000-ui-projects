---
name: Executive Aviation Concierge
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444650'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#121516'
  on-tertiary: '#ffffff'
  tertiary-container: '#26292a'
  on-tertiary-container: '#8e9091'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  button:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
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
  container-margin: 24px
  gutter: 16px
  section-gap: 40px
  glass-padding: 20px
---

## Brand & Style

This design system is engineered for the high-altitude lifestyle of the global business traveler. The brand personality is **Elite, Serene, and Intelligent**. It balances the heritage of luxury travel with the precision of modern technology.

The visual style is a fusion of **High-End Minimalism** and **Glassmorphism**. By using semi-transparent layers and soft background blurs, the interface feels lightweight and airy—mimicking the sensation of flight. The aesthetic avoids clutter, opting for generous whitespace to reduce cognitive load for users navigating complex travel schedules. Every interaction must feel frictionless, conveying a sense of "quiet luxury" through restrained motion and impeccable alignment.

## Colors

The palette is anchored in **Royal Blue (#002366)**, a color that commands authority and establishes trust. This is used for primary structural elements and high-level navigation.

**Gold (#D4AF37)** is reserved strictly for premium touchpoints: primary Call-to-Actions (CTAs), membership status indicators, and subtle decorative accents. It should be used sparingly to maintain its value.

The background environment is a **Crisp White**, ensuring the "Glass" elements have a clean canvas to sit upon. For functional states, use a sophisticated scale of cool greys to maintain the professional tone.

## Typography

This design system utilizes a high-contrast typographic pairing. **Playfair Display** provides an editorial, sophisticated character for headings, evoking the feeling of a premium travel journal or a first-class lounge menu. 

For functional interface elements and long-form text, **Manrope** is used for its modern, geometric clarity and exceptional legibility at small sizes. 

**Usage Notes:**
- Use `display-lg` for hero welcome screens only.
- `label-caps` should be used for section headers above lists or small metadata like flight numbers.
- Ensure all body text maintains a minimum of 16px to accommodate travelers in varying lighting conditions.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop (12 columns, 1140px max-width) and a **Fluid Grid** for mobile (4 columns). 

A strict 8px baseline grid ensures vertical rhythm. Spacing is intentionally generous; elements are given "room to breathe" to reinforce the premium brand positioning. 

**Breakpoints:**
- **Mobile:** < 600px (Margins: 20px)
- **Tablet:** 600px - 1024px (Margins: 32px)
- **Desktop:** > 1024px (Margins: Auto)

On mobile, use full-width "Glass" cards with 20px internal padding to maximize the interactive surface area for travelers on the move.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** rather than traditional heavy shadows.

- **Level 1 (Base):** Solid White background.
- **Level 2 (Cards/Content):** Semi-transparent White (Opacity: 70-80%) with a `20px` Backdrop Blur and a very thin `0.5px` stroke in White (Opacity: 30%) to simulate a glass edge.
- **Level 3 (Modals/Overlays):** Semi-transparent White (Opacity: 90%) with a `40px` Backdrop Blur and a soft, diffused `0 12px 24px` Royal Blue shadow at 5% opacity to provide a subtle lift.

This stacking creates a sense of physical layers that feels high-tech and premium.

## Shapes

The shape language is **Refined and Geometric**. A `0.5rem` (8px) base radius is applied to standard components like input fields and buttons. 

Larger containers and Glass cards utilize the `rounded-xl` (1.5rem/24px) setting to create a softer, more inviting appearance. This curvature contrasts with the sharp, elegant serifs of the typography, balancing classical style with modern industrial design.

## Components

### Buttons
- **Primary:** Solid Gold (#D4AF37) with Navy text. Bold, high-contrast, and used for the main journey action (e.g., "Book Concierge").
- **Secondary:** Ghost style with a Royal Blue border and text.
- **Tertiary:** Text-only with a small Gold chevron icon.

### Glass Cards
The signature component of this design system. Used for flight details, lounge access passes, and baggage tracking. They must feature a blurred background to ensure text remains legible regardless of what is behind the card.

### Input Fields
Clean, minimalist design. Use a simple bottom border in Royal Blue for the inactive state. Upon focus, the border thickens and a very subtle Gold glow is applied to the label.

### Concierge Chips
Small, rounded indicators used for status updates (e.g., "In Transit", "Delivered"). Use Royal Blue for background with White text, except for "Priority" status which uses Gold.

### Navigation
A bottom navigation bar on mobile using a frosted glass effect. Active icons are rendered in Gold; inactive in a muted Royal Blue.