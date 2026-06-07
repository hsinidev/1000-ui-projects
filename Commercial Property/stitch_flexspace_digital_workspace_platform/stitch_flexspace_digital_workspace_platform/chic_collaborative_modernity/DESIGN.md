---
name: Chic Collaborative Modernity
colors:
  surface: '#fff8f4'
  surface-dim: '#e1d9d2'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2eb'
  surface-container: '#f5ece5'
  surface-container-high: '#efe7e0'
  surface-container-highest: '#eae1da'
  on-surface: '#1f1b17'
  on-surface-variant: '#56423d'
  inverse-surface: '#34302b'
  inverse-on-surface: '#f8efe8'
  outline: '#89726c'
  outline-variant: '#dcc0ba'
  surface-tint: '#9d422b'
  primary: '#9a4028'
  on-primary: '#ffffff'
  primary-container: '#b9573e'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb4a2'
  secondary: '#356667'
  on-secondary: '#ffffff'
  secondary-container: '#b6e9ea'
  on-secondary-container: '#396a6b'
  tertiary: '#625b51'
  on-tertiary: '#ffffff'
  tertiary-container: '#7b7469'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd2'
  primary-fixed-dim: '#ffb4a2'
  on-primary-fixed: '#3c0800'
  on-primary-fixed-variant: '#7e2b16'
  secondary-fixed: '#b9eced'
  secondary-fixed-dim: '#9dd0d0'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#1a4e4f'
  tertiary-fixed: '#ebe1d4'
  tertiary-fixed-dim: '#cfc5b9'
  on-tertiary-fixed: '#1f1b13'
  on-tertiary-fixed-variant: '#4c463c'
  background: '#fff8f4'
  on-background: '#1f1b17'
  surface-variant: '#eae1da'
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
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-margin: 20px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-padding: 64px
---

## Brand & Style

The design system is engineered for the sophisticated professional who values both productivity and community. It strikes a precise balance between corporate reliability and lifestyle warmth, moving away from sterile office aesthetics toward a "hospitality-first" workspace model.

The visual style is **Glassmorphism**, utilized strategically to suggest transparency and openness. By layering translucent surfaces over soft, warm backgrounds, the UI achieves a sense of physical depth that feels airy and modern. This approach mirrors the physical architecture of premium co-working spaces—glass partitions, open floor plans, and tactile materials. The overall mood is "Chic & Collaborative," ensuring users feel they are entering a high-end, curated environment rather than a utilitarian booking tool.

## Colors

The palette is rooted in an earthy, sophisticated trio. **Terracotta** serves as the primary energetic driver, representing the warmth of brick and human connection. **Teal** provides a professional, calming counter-weight, used for secondary actions and navigation to ensure visual stability.

**Warm Grey** acts as the foundation, used for backgrounds and surfaces to prevent the "cold" feeling of pure white or standard grey. This design system utilizes a light-mode default to maximize the clarity of the glass effects, using subtle gradients of the tertiary color to create the "frosted" backdrop necessary for translucent elements to pop.

## Typography

The design system utilizes **Manrope** for its geometric yet functional character. Its high x-height and open counters provide excellent readability on mobile screens while maintaining a refined, editorial feel on desktop. 

Headlines use tighter letter spacing and heavier weights to command attention and convey authority. Body copy is generously spaced to ensure a comfortable reading experience during long browsing sessions. A specialized "label-caps" style is used for metadata and category tags to provide high-contrast hierarchy without requiring large font sizes.

## Layout & Spacing

This design system adopts a **Mobile-First Fluid Grid**. Layouts are built on a base 8px rhythm to ensure consistent vertical cadence. On mobile devices, the system uses a single-column stack with 20px side margins. As screen real estate increases, it transitions into a 12-column grid.

Spacing is used to group collaborative features together, using "stack" tokens to define the relationship between elements. Larger section padding is employed to create a sense of luxury and "breathability," reflecting the spaciousness of a well-designed office.

## Elevation & Depth

Hierarchy is established through **Glassmorphism and layered transparency**. Instead of traditional heavy shadows, this design system uses:

1.  **Backdrop Blurs:** Surfaces use a 12px to 20px blur to separate content from the background.
2.  **Translucent Fills:** Card backgrounds are white or warm grey with 40-70% opacity.
3.  **Subtle Borders:** Elements are defined by 1px semi-transparent white borders that act as "inner glows," mimicking the edge of a glass pane.
4.  **Soft Shadows:** When used, shadows are highly diffused (20-30px blur) with very low opacity (5-10%) and a slight tint of the primary Terracotta color to maintain warmth.

## Shapes

The shape language is defined by **Rounded (0.5rem base)** corners. This creates a soft, approachable aesthetic that removes the "clinical" feel of sharp-edged corporate software. 

Cards and major containers utilize `rounded-xl` (1.5rem) to emphasize the glass pane metaphor, while buttons and input fields use the standard `rounded` (0.5rem) for a more precise, actionable feel. Interactive elements should never be sharp, ensuring the UI always feels "inviting" to the touch.

## Components

### Buttons
Primary buttons use a solid Terracotta fill with white text. Secondary buttons utilize a Teal outline or a "glass" style with Teal text. All buttons feature a 200ms ease-in-out transition on hover/active states, with a slight scale-up (1.02) to feel dynamic.

### Glass Cards
The signature component. These must feature `backdrop-filter: blur()`, a 1px white border at 20% opacity, and a soft-tinted shadow. They are used for office listings, amenity highlights, and user profiles.

### Input Fields
Inputs are minimalist with a soft warm-grey background. Upon focus, the border transitions to Teal with a subtle outer glow, providing clear feedback without breaking the chic aesthetic.

### Chips & Tags
Used for "Amenities" (e.g., High-speed WiFi, Coffee Bar). These are pill-shaped with a low-opacity Teal or Terracotta background and matching text color, ensuring they are readable but subordinate to the main card content.

### Dynamic Transitions
Navigation between views should use "fade and slide" motions. When a user selects an office, the card should seem to expand into the full-page view, maintaining the glass layer's continuity.