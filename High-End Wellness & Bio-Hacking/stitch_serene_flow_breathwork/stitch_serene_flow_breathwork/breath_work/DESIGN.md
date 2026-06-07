---
name: Breath-Work
colors:
  surface: '#f3faff'
  surface-dim: '#c7dde9'
  surface-bright: '#f3faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e6f6ff'
  surface-container: '#dbf1fe'
  surface-container-high: '#d5ecf8'
  surface-container-highest: '#cfe6f2'
  on-surface: '#071e27'
  on-surface-variant: '#43474a'
  inverse-surface: '#1e333c'
  inverse-on-surface: '#dff4ff'
  outline: '#73787b'
  outline-variant: '#c3c7cb'
  surface-tint: '#526069'
  primary: '#526069'
  on-primary: '#ffffff'
  primary-container: '#e3f2fd'
  on-primary-container: '#606f78'
  inverse-primary: '#bac9d3'
  secondary: '#655b68'
  on-secondary: '#ffffff'
  secondary-container: '#ecdeee'
  on-secondary-container: '#6b616e'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#f0f0f0'
  on-tertiary-container: '#6b6d6d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e5ef'
  primary-fixed-dim: '#bac9d3'
  on-primary-fixed: '#0f1d25'
  on-primary-fixed-variant: '#3b4951'
  secondary-fixed: '#ecdeee'
  secondary-fixed-dim: '#cfc2d2'
  on-secondary-fixed: '#201924'
  on-secondary-fixed-variant: '#4d4450'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f3faff'
  on-background: '#071e27'
  surface-variant: '#cfe6f2'
typography:
  headline-xl:
    fontFamily: Quicksand
    fontSize: 40px
    fontWeight: '300'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Quicksand
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-md:
    fontFamily: Quicksand
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Quicksand
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Quicksand
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Quicksand
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-margin: 32px
  gutter: 16px
---

## Brand & Style
The brand personality of this design system is centered on the concept of "Air." It is designed to feel ethereal, light, and clinical without the coldness often associated with medical software. The target audience includes individuals seeking stress relief, athletes optimizing performance, and patients managing respiratory health.

The design style merges **Minimalism** with **Glassmorphism**. It utilizes excessive whitespace to allow content to "breathe," reducing cognitive load and lowering the user's heart rate through visual cues. Subtle organic movements—such as pulsing background shapes—mimic the natural rhythm of a lung's expansion and contraction, reinforcing the core utility of the product through the UI itself.

## Colors
The palette is monochromatic and high-key, designed to eliminate visual friction.
- **Soft Blue (#E3F2FD):** The primary color, used for active states, breath indicators, and primary call-to-actions. It evokes a clear sky and clean air.
- **Lavender (#F3E5F5):** The secondary color, used for secondary data points and resting states. It provides a warm, meditative counterpoint to the coolness of the blue.
- **Silk White (#FFFFFF):** The foundation of the design system. Used for surfaces and backgrounds to maximize luminosity.
- **Text & Accents:** A deep Slate Blue-Grey (#455A64) is used for typography to ensure accessibility while maintaining a softer contrast than pure black.

## Typography
This design system employs **Quicksand** exclusively to leverage its rounded terminals and open apertures. The typeface conveys a sense of compassion and friendliness. 

Headlines utilize a lighter weight (300) at larger scales to feel "airy," while body text remains at a medium weight (400) for legibility against translucent backgrounds. Tracking is slightly increased for labels to ensure a sense of openness. All text should be set in sentence case to maintain a conversational, calming tone.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy with extremely generous margins. Content is typically centered to create a focal point for the user during breathing exercises. 

We use a "Breath Rhythm" spacing scale based on 8px increments, but with a preference for the larger tiers (48px and 80px) to separate distinct sections. This "negative space" is intentional; it prevents the interface from feeling cluttered, which is critical for a wellness application. Columns are used sparingly, with most mobile layouts favoring a single-column stack to maintain focus.

## Elevation & Depth
Hierarchy is established through **Glassmorphism** and **Ambient Shadows** rather than traditional rigid borders.

1.  **Surfaces:** Components use a semi-transparent White (80% opacity) with a `backdrop-filter: blur(20px)`. This creates a frosted glass effect that lets the organic background shapes bleed through.
2.  **Shadows:** Shadows are highly diffused and tinted with the primary Soft Blue. Instead of grey shadows, use `#E3F2FD` at 40% opacity with a 30px blur to create a soft "glow" rather than a hard drop shadow.
3.  **Active Depth:** When an element is selected, it should appear to "float" higher through an increased blur radius and a subtle scale-up animation (e.g., 1.02x).

## Shapes
The shape language is strictly organic and hyper-rounded. 
- **UI Elements:** Buttons and containers use a pill-shaped radius (Max) or high-level rounding (24px+) to avoid any sharp "points" that could cause subconscious tension.
- **Organic Motifs:** Background elements are non-geometric "blobs." These shapes should use SVG filters to create a liquid-like appearance.
- **Interaction:** Shapes should pulse. During inhalation, shapes expand; during exhalation, they contract. No shape in the design system should have a 90-degree corner.

## Components
- **Buttons:** Pill-shaped with a Soft Blue to Lavender gradient. Use high horizontal padding (32px+). Text should be bolded but small.
- **Glass Cards:** Used for session summaries. Features a 1px solid Silk White border at 50% opacity to define the edge against the blurred background.
- **The Breath Circle:** The central component of the design system. An organic, pulsing shape that grows and shrinks. It uses a heavy backdrop blur and a soft inner glow.
- **Inputs:** Minimalist bottom-border only, or a fully rounded "pill" input with a very light Lavender fill.
- **Progress Rings:** Use rounded caps and thin strokes. The path should be the Soft Blue, and the unfilled track should be Silk White at 20% opacity.
- **Selection Chips:** Pill-shaped with a soft shadow when active. Inactive chips have no fill, only a 1px Lavender border.