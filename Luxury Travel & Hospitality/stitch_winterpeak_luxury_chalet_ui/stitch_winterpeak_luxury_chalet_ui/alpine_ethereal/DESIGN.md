---
name: Alpine Ethereal
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#43474b'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#73787b'
  outline-variant: '#c3c7cb'
  surface-tint: '#4e616d'
  primary: '#4e616d'
  on-primary: '#ffffff'
  primary-container: '#d6eaf8'
  on-primary-container: '#576a76'
  inverse-primary: '#b6c9d7'
  secondary: '#5c5f62'
  on-secondary: '#ffffff'
  secondary-container: '#dee0e4'
  on-secondary-container: '#606366'
  tertiary: '#545f72'
  on-tertiary: '#ffffff'
  tertiary-container: '#dde8ff'
  on-tertiary-container: '#5d687c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e5f3'
  primary-fixed-dim: '#b6c9d7'
  on-primary-fixed: '#0a1e28'
  on-primary-fixed-variant: '#374954'
  secondary-fixed: '#e0e2e6'
  secondary-fixed-dim: '#c4c7ca'
  on-secondary-fixed: '#191c1f'
  on-secondary-fixed-variant: '#44474a'
  tertiary-fixed: '#d8e3fa'
  tertiary-fixed-dim: '#bcc7dd'
  on-tertiary-fixed: '#111c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
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
---

## Brand & Style
This design system captures the essence of elite mountain living through a visual language that balances the warmth of a luxury fireside with the crisp, crystalline beauty of the peaks. The aesthetic is rooted in **Glassmorphism**, specifically a style termed "Frost," which utilizes high-translucency layers to mimic ice and snow. 

The brand personality is serene and prestigious, catering to an audience that values exclusivity and quiet luxury. By combining a minimalist structural approach with tactile, frosted surfaces, the UI evokes a sense of calm and breathtaking clarity. The goal is to make the user feel as though they are looking through a panoramic window at a private mountain range.

## Colors
The palette is derived from the natural landscape of a winter morning. The **Ice Blue** (Primary) serves as the highlight color, used for interactive elements and subtle accents that draw the eye without overwhelming the serenity of the layout. **Silver** (Secondary) provides the structural metalwork of the UI, appearing in borders and dividers.

**Warm Grey** (Tertiary) adds the necessary depth and grounding, used primarily for text and iconography to ensure legibility against the bright, translucent backgrounds. The background surface is a clean, near-white neutral that allows the frosted glass effects to catch "light" realistically.

## Typography
The typography strategy employs a classic "Editorial High-Low" pairing. **Noto Serif** is reserved for headlines and large display text, providing a traditional, literary authority that feels expensive and established. It should be typeset with generous leading to allow the letterforms to breathe.

**Inter** handles the functional UI elements. Its neutral, utilitarian structure ensures that complex information—such as booking details or lodge amenities—remains perfectly legible. Labels should frequently use uppercase styling with increased letter spacing to lean into the luxury fashion aesthetic.

## Layout & Spacing
The layout follows a **fixed grid** philosophy to maintain a structured, gallery-like feel. Large margins (64px on desktop) are essential to prevent the UI from feeling cluttered, emphasizing the "serene" brand pillar. 

Elements are organized on a 12-column grid with generous 24px gutters. Spacing should prioritize vertical rhythm, using multiples of 8px. Negative space is not just a gap but a design element that signifies prestige; do not be afraid of large, empty areas in the layout.

## Elevation & Depth
Depth is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces use a "Backdrop Filter" blur (ranging from 10px to 20px) and a highly translucent white fill (10% to 40% opacity). 

To define these floating planes, use a **1px solid border** in a very light Silver or Ice Blue with low opacity (20%). This creates a "glint" effect on the edge of the glass. When elements need to feel more prominent, increase the blur intensity and the border opacity rather than adding dark shadows. A very faint, diffused ambient shadow (0% saturation, 5% opacity) may be used for the highest-level modals.

## Shapes
This design system utilizes **Rounded** geometry (0.5rem base) to soften the "coldness" of the ice-inspired palette. This level of roundedness feels organic and inviting, reminiscent of smooth river stones or weathered mountain peaks. 

Buttons and input fields should strictly adhere to the base roundedness, while larger container cards can scale up to 1.5rem (`rounded-xl`) to emphasize the "cozy" aspect of the chalet experience.

## Components
- **Buttons:** Primary buttons should be "Frost" style with a high-blur background and a subtle 1px Ice Blue border. Text should be uppercase Inter with slight letter spacing.
- **Cards:** Use high-translucency backgrounds. For a "Premium Card," add a subtle linear gradient to the border (top-left to bottom-right) using Silver and Ice Blue.
- **Inputs:** Fields are minimal, using a Silver bottom-border only or a very light "Frost" fill. Focus states should transition the border color to a solid Ice Blue.
- **Chips/Badges:** Small, pill-shaped elements with a solid Silver background and Dark Grey text for high contrast.
- **Specialty Component - The 'Lodge Viewport':** An image-heavy carousel with glassmorphic overlays for captions, used to showcase room interiors and mountain vistas.
- **Navigation:** A fixed header with a high-blur frost effect that allows the mountain photography to bleed through as the user scrolls.