---
name: High-End Feline Sanctuary
colors:
  surface: '#fdf8f9'
  surface-dim: '#ded9da'
  surface-bright: '#fdf8f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f2f3'
  surface-container: '#f2eded'
  surface-container-high: '#ece7e8'
  surface-container-highest: '#e6e1e2'
  on-surface: '#1d1b1c'
  on-surface-variant: '#48464b'
  inverse-surface: '#323031'
  inverse-on-surface: '#f5eff0'
  outline: '#79767c'
  outline-variant: '#cac5cc'
  surface-tint: '#615c6b'
  primary: '#615c6b'
  on-primary: '#ffffff'
  primary-container: '#ded6e8'
  on-primary-container: '#615c6b'
  inverse-primary: '#cbc3d5'
  secondary: '#5e5e5b'
  on-secondary: '#ffffff'
  secondary-container: '#e1dfdb'
  on-secondary-container: '#63635f'
  tertiary: '#7a581f'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffd290'
  on-tertiary-container: '#7a581f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e7dff1'
  primary-fixed-dim: '#cbc3d5'
  on-primary-fixed: '#1d1a26'
  on-primary-fixed-variant: '#494453'
  secondary-fixed: '#e4e2dd'
  secondary-fixed-dim: '#c8c6c2'
  on-secondary-fixed: '#1b1c19'
  on-secondary-fixed-variant: '#474744'
  tertiary-fixed: '#ffddaf'
  tertiary-fixed-dim: '#ecbf7c'
  on-tertiary-fixed: '#281800'
  on-tertiary-fixed-variant: '#5f4108'
  background: '#fdf8f9'
  on-background: '#1d1b1c'
  surface-variant: '#e6e1e2'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
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
  margin-desktop: 64px
  section-padding: 80px
---

## Brand & Style

The design system is rooted in the concept of "Peace of Mind through Elegance." It targets discerning pet owners who view their cats as family members deserving of a five-star experience. The brand personality is serene, attentive, and exclusive. 

The visual style follows a **Minimalist** approach with **Tactile** influences. By utilizing expansive whitespace and a restrained color palette, the interface mimics the quiet luxury of a boutique hotel. The focus is on high-quality photography—capturing sun-drenched rooms and soft textures—while the UI provides a breathable, unobtrusive framework that evokes a sense of calm and safety.

## Colors

The color palette of this design system is designed to feel airy and prestigious. 
- **Soft Lavender (Primary):** Used for subtle backgrounds, secondary buttons, and active states. It provides a modern, calming alternative to traditional corporate blues.
- **Warm Cream (Secondary/Background):** The canvas of the application. This replaces pure white to add a layer of warmth and "coziness" to the interface.
- **Metallic Gold (Tertiary/Accent):** Reserved strictly for high-priority Call-to-Actions (CTAs) and premium badges. It should be used sparingly to maintain its impact.
- **Deep Slate (Neutral):** Used for typography to ensure high readability against the cream backgrounds without the harshness of pure black.

## Typography

This design system employs a sophisticated typographic hierarchy to differentiate between editorial "storytelling" and functional "utility."

**Noto Serif** is the voice of the brand. Its high-contrast strokes and elegant serifs should be used for all major headings and pull quotes to convey a sense of heritage and premium service. 

**Plus Jakarta Sans** provides a contemporary, friendly balance for body copy. Its open counters and rounded terminals ensure legibility in denser information areas, such as booking details or cat care logs, while maintaining the "soft" visual language of the brand.

## Layout & Spacing

The layout philosophy of this design system centers on a **Fixed Grid** with generous internal padding to create a sense of "breathing room." 

- A 12-column grid is used for desktop, but content is often constrained to the center 8 or 10 columns to prevent line lengths from becoming too long, maintaining a boutique editorial feel.
- Vertical rhythm is built on an 8px base unit. 
- Section spacing is intentionally large (80px+) to ensure that high-quality imagery has room to dominate the visual field without feeling crowded by text.

## Elevation & Depth

To maintain the "cozy" and "boutique" aesthetic, this design system avoids harsh shadows or aggressive layering. 

- **Ambient Depth:** Objects (like cards or modals) use extremely soft, low-opacity shadows with a slight lavender tint (#DED6E8 at 20% opacity) rather than grey. This makes elements feel as though they are gently resting on the cream surface.
- **Tonal Layering:** Depth is primarily communicated through color shifts (e.g., a Cream card on a slightly darker Lavender background) rather than physical elevation.
- **Frosted Glass:** Occasional use of backdrop blurs on navigation bars adds a modern, high-end touch while keeping the focus on the warm imagery beneath.

## Shapes

The shape language of this design system is soft and welcoming. 

Avoid sharp 90-degree angles, which can feel clinical or cold. Instead, use a consistent 0.5rem (8px) corner radius for standard elements like input fields and small cards. Larger containers, such as hero images or feature sections, should utilize a more pronounced "rounded-xl" (1.5rem / 24px) to emphasize the "cozy" and protective nature of the facility.

## Components

### Buttons
- **Primary CTA:** Solid Gold background with white or deep slate text. These should have a slight hover lift and use the "rounded-lg" setting.
- **Secondary:** Lavender-tinted backgrounds with deep slate text. 
- **Ghost:** Gold border and text, used for less urgent actions to maintain the minimalist feel.

### Cards
Cards are the primary vehicle for pet profiles and room descriptions. They should feature large, high-resolution imagery with a "top-heavy" layout. The bottom text area should use the Warm Cream background and Noto Serif for titles.

### Form Fields
Input fields should be minimalist—soft Lavender borders that transition to Gold on focus. Avoid heavy fills; a light Cream background is sufficient to denote interactive areas.

### Interactive Elements
- **Chips/Badges:** Small, pill-shaped tags used for "Available" or "Premium Suite" status, using the Gold accent color.
- **Image Galleries:** Use a masonry or clean grid layout with significant gutters (24px) to let pet photography shine.
- **Booking Progress:** A clean, horizontal stepper with thin lines and serif labels to guide the user through the high-end reservation process.