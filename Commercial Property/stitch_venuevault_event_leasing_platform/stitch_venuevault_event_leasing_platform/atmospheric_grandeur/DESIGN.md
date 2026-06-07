---
name: Atmospheric Grandeur
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#d6bcf4'
  on-secondary: '#3b2754'
  secondary-container: '#523d6c'
  on-secondary-container: '#c4abe1'
  tertiary: '#cfcece'
  on-tertiary: '#303031'
  tertiary-container: '#b3b3b3'
  on-tertiary-container: '#454545'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#eedbff'
  secondary-fixed-dim: '#d6bcf4'
  on-secondary-fixed: '#25113e'
  on-secondary-fixed-variant: '#523d6c'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 64px
---

## Brand & Style

This design system is engineered to evoke a sense of prestige, scale, and exclusivity. The brand personality is authoritative yet welcoming, designed for a target audience of high-end event planners, corporate executives, and gala organizers who seek more than just a space—they seek an experience.

The visual style is a sophisticated blend of **Tactile Modernism** and **High-Contrast Minimalism**. By leveraging deep, immersive backgrounds against luminous accents, the system creates a digital environment that feels as physical and grand as the venues it represents. The aesthetic relies on the interplay of light and shadow, using subtle 3D effects to give UI components weight and presence. Every interaction should feel intentional, reinforcing a narrative of luxury and meticulous curation.

## Colors

The palette is anchored by **Midnight Purple**, used as the primary canvas to create depth and an "after-hours" premium atmosphere. Unlike a standard black or grey dark mode, the purple hue provides a regal warmth that softens high-contrast elements.

**Gold** serves as the primary action color. It is used sparingly but impactfully for Call-to-Action (CTA) elements, key highlights, and brand signatures. This evokes a sense of "the golden ticket" or an exclusive invitation. 

**Smoke** is utilized in two tiers: the lighter #F5F5F5 is reserved for high-readability typography and primary icons, while the muted #848484 is used for secondary metadata, borders, and disabled states. This ensures that the interface remains legible and airy despite the deep background.

## Typography

The typographic hierarchy is built on the contrast between the traditional and the modern. **Noto Serif** is the voice of the system, used for headlines to convey institutional weight and elegance. Large-scale headlines should be set with tight letter spacing to emphasize their editorial quality.

**Manrope** provides a functional counterpoint. Its clean, geometric sans-serif structure ensures that dense logistical information—such as pricing, dimensions, and availability—is processed effortlessly. For specialized UI elements like section headers or navigation links, use the `label-caps` style to provide a structured, architectural feel.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy to maintain an editorial, magazine-like structure. Layouts are built on a 12-column grid with wide gutters and substantial outer margins. This "contained" approach creates a sense of focused luxury, preventing content from feeling stretched or utilitarian.

Spacing should be generous. Negative space is not "empty" in this system; it is filled with the Midnight Purple gradient, contributing to the atmospheric depth. Vertical rhythm should favor larger gaps (`lg` and `xl`) between major sections to allow the user's eye to rest, mirroring the expansive nature of a large convention hall.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Ambient Shadows**. Instead of flat surfaces, the UI uses three distinct levels of depth:

1.  **The Floor (Background):** Deep Midnight Purple with a subtle radial gradient that is slightly lighter in the center of the screen to draw focus.
2.  **The Mezzanine (Cards/Sections):** A slightly lifted purple, achieved through a 5% lighter fill or a very subtle backdrop blur. These containers feature a "low-contrast outline"—a 1px border in #848484 at 20% opacity.
3.  **The Stage (CTAs/Overlays):** These elements use gold gradients and "Ambient Shadows." Shadows are not black; they are deep purple (#1A0F29) with a 24px blur and 40% opacity, making them feel like they are floating naturally in a lit space.

To achieve the "three-dimensional" feel, buttons and cards should feature a subtle top-down linear gradient (e.g., Gold to a slightly darker Ochre) to simulate overhead lighting.

## Shapes

The shape language is **Architectural and Soft**. By utilizing a "Soft" roundedness level (0.25rem to 0.75rem), the system avoids the playfulness of fully rounded "pill" shapes while steering clear of the harshness of sharp 90-degree angles.

This specific corner radius mimics the structural finishes of modern high-end interiors—calculated, clean, and premium. Larger components like hero images or main container cards should utilize `rounded-xl` (0.75rem) to feel like substantial, physical objects, while smaller elements like input fields and tags use the base `rounded` (0.25rem) for precision.

## Components

### Buttons
Primary buttons are the "Gold Standard." They feature a subtle linear gradient from #D4AF37 to #B18F2B. Typography within buttons is Manrope Bold in Midnight Purple for maximum contrast. Secondary buttons are "Smoke Ghost" style: a 1px smoke border with no fill, transitioning to a light smoke fill on hover.

### Cards
Cards are the primary vessel for venue listings. They must use a "Glassmorphism" approach: a semi-transparent purple fill with a 10px backdrop blur. This allows the atmospheric background to peek through, maintaining the sense of depth.

### Inputs & Selects
Input fields should feel recessed into the "floor." This is achieved using a dark inset shadow and a smoke-colored border at 30% opacity. Upon focus, the border glows with a soft Gold outer shadow.

### Chips & Badges
Used for venue features (e.g., "500+ Capacity," "Catering"). These are small, dark purple capsules with a subtle 1px Gold border. Typography is set in `label-caps` for a professional, metadata-heavy look.

### Interactive Floorplans
A unique component for this system. These should be rendered in high-contrast Smoke lines against the Midnight Purple background, with "Booked" sections appearing in a muted purple and "Available" sections highlighted with a Gold glow.