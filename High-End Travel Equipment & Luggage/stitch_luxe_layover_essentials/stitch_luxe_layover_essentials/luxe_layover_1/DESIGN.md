---
name: Luxe-Layover
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#46464c'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#77767d'
  outline-variant: '#c7c5cc'
  surface-tint: '#5c5d6e'
  primary: '#5c5d6e'
  on-primary: '#ffffff'
  primary-container: '#e6e6fa'
  on-primary-container: '#656677'
  inverse-primary: '#c5c5d8'
  secondary: '#546256'
  on-secondary: '#ffffff'
  secondary-container: '#d5e4d5'
  on-secondary-container: '#58665b'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e8e8'
  on-tertiary-container: '#666868'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e1f5'
  primary-fixed-dim: '#c5c5d8'
  on-primary-fixed: '#191b29'
  on-primary-fixed-variant: '#444655'
  secondary-fixed: '#d8e6d8'
  secondary-fixed-dim: '#bccabc'
  on-secondary-fixed: '#121e15'
  on-secondary-fixed-variant: '#3d4a3f'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 34px
    fontWeight: '700'
    lineHeight: 42px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-padding: 24px
  element-gap: 16px
  section-margin: 40px
---

## Brand & Style

This design system embodies a "Chic Velocity" aesthetic—a fusion of high-end travel luxury and the rhythmic energy of global transit. It is designed for the discerning traveler who views organization as a form of self-care. The visual language utilizes **Neumorphism (Soft-UI)** to create a tactile, physical interface that feels like touching premium luggage or embossed leather. By moving away from flat, clinical surfaces, the UI invites interaction through depth, mimicking the soft-touch surfaces of luxury travel goods. The emotional response is one of calm preparedness and high-status excitement.

## Colors

The palette is rooted in an ethereal, "above the clouds" atmosphere. **Soft Lavender** serves as the primary brand anchor, providing a sense of sophisticated calm. **Mint** is used as a high-energy accent for success states, calls-to-action, and fresh highlights. **Silk White** acts as the foundation for the neumorphic base, allowing for the subtle shadow play required to create depth.

To achieve the tactile effect, two specific shadow tones are utilized:
- **Light Source:** #FFFFFF (Pure White) for top-left highlights.
- **Depth Shadow:** #D1D1E9 (Muted Lavender-Grey) for bottom-right extrusion.

## Typography

The typography strategy employs **Plus Jakarta Sans** for its modern, clean, and slightly geometric terminals which echo the rounded corners of the UI. Headlines are set with tight letter-spacing to feel "organized" and "packed," while body copy is given generous line-height to maintain an air of premium luxury and readability. We use uppercase labels for categorization to provide a clear information hierarchy in a mobile-first environment.

## Layout & Spacing

This design system utilizes a **Fluid Mobile Grid** with a baseline unit of 8px. Given the tactile nature of the elements, generous margins (24px) are required to let the soft shadows "breathe" without overlapping adjacent components. The layout philosophy relies on vertical stacking with clear, airy separations, mimicking the way items are perfectly nested within a travel kit.

## Elevation & Depth

Depth is the primary communicator of hierarchy. Unlike traditional shadow systems, this design system uses **Dual-Shadow Extrusion**:
1.  **Extruded (Raised):** Elements like buttons and cards use a light shadow on the top-left and a dark shadow on the bottom-right.
2.  **Inverted (Sunken):** Input fields and active button states use inner shadows to appear recessed into the surface.
3.  **Softness:** All shadow blurs are high (20px+) with low opacity to ensure the "soft-ui" feel remains sophisticated rather than muddy.

## Shapes

The shape language is defined by "Squircle" aesthetics. Sharp corners are avoided entirely to maintain the "Luxe" and "Soft" brand pillars. 
- **Standard Cards/Buttons:** 16px (rounded-lg) to provide a friendly, approachable hand-feel.
- **Small Elements (Chips/Tags):** Fully rounded (pill-shaped) to differentiate them from functional interaction points.
- **Container Surfaces:** 24px (rounded-xl) to create a soft frame for the viewport.

## Components

**Buttons**
Primary buttons appear extruded from the background in Soft Lavender. Upon press, they transition to an "inset" (sunken) state with no change in color, only a change in shadow direction to provide haptic visual feedback.

**Cards (Travel Kits)**
Cards use a subtle 1px Silk White border and a soft outer shadow. They act as the primary vessel for product imagery. The product should appear to "float" within the card.

**Input Fields**
Search bars and checkout inputs are always recessed (inverted neumorphism). This directs the user's focus "into" the form, suggesting a secure, contained space for information.

**Chips & Filters**
Used for sorting travel kits (e.g., "Business," "Tropical"). These are pill-shaped and use a Mint background when active to inject high-energy contrast into the soft layout.

**The Kit Progress Tracker**
A unique component for this design system: a tactile timeline that shows the assembly of a travel kit, using sunken "wells" for incomplete steps and extruded "beads" for completed ones.