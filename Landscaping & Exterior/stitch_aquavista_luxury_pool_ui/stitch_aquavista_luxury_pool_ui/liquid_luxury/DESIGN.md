---
name: Liquid Luxury
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#44474e'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#006a6a'
  on-secondary: '#ffffff'
  secondary-container: '#00f8f8'
  on-secondary-container: '#006e6e'
  tertiary: '#050c10'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a2327'
  on-tertiary-container: '#818a90'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#00fbfb'
  secondary-fixed-dim: '#00dddd'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#dbe4ea'
  tertiary-fixed-dim: '#bfc8ce'
  on-tertiary-fixed: '#141d21'
  on-tertiary-fixed-variant: '#3f484d'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: epilogue
    fontSize: 4.5rem
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: epilogue
    fontSize: 3rem
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: epilogue
    fontSize: 2rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: manrope
    fontSize: 1.25rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: manrope
    fontSize: 0.875rem
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
  container-max: 1440px
  gutter: 2rem
  section-padding: 8rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 3rem
---

## Brand & Style

The brand personality is defined by an uncompromising pursuit of serenity and elite craftsmanship. This design system targets high-net-worth individuals seeking a transformative lifestyle investment. The UI must evoke the sensation of standing poolside at dawn: calm, expansive, and crystal clear.

The visual direction combines **Minimalism** with subtle **Glassmorphism**. High-end luxury is communicated through generous whitespace and a "less is more" approach to functional elements, allowing full-bleed, high-resolution cinematography of water and architectural masonry to command the user's attention. Translucent layers are used to mimic the refractive properties of water, creating a sense of depth and fluidity without cluttering the interface.

## Colors

The palette is anchored by **Deep Cobalt**, providing a foundation of authority and depth reminiscent of the deep end of a pool. **Pure White** serves as the primary canvas, ensuring the "breezy" and "refreshing" aesthetic is maintained through high-key compositions. **Crystal Cyan** is used sparingly as a high-vibrancy accent to draw attention to interactive elements and highlights, mimicking sunlight reflecting off water.

A tertiary "Water Vapor" tint (#F0F9FF) is utilized for subtle background shifts and section dividers to prevent visual fatigue from pure white while maintaining a cool, airy atmosphere.

## Typography

This design system employs a sophisticated dual-sans-serif pairing. For headlines, **Epilogue** provides an editorial, contemporary edge; its geometric nature feels architectural and custom-built. Large-scale headlines should utilize light weights to maintain an aspirational, airy feel.

**Manrope** is used for body copy and UI labels to provide a refined, balanced reading experience. It bridges the gap between technical precision and modern elegance. All navigational labels and small headers should use the "label-caps" style with increased letter spacing to instill a sense of premium branding.

## Layout & Spacing

The layout follows a **Fixed Grid** model centered within the viewport, ensuring that high-quality imagery is framed like art in a gallery. A 12-column grid is used with wide gutters to prevent content from feeling cramped. 

The spacing rhythm is intentionally oversized. Vertical section padding is generous to force a slower, more deliberate scrolling pace, reflecting the relaxed luxury of a resort. Elements are grouped using a logical "stacking" scale, where white space is treated as a premium design element rather than "empty" space.

## Elevation & Depth

Visual hierarchy is achieved through **Glassmorphism** and **Ambient Shadows**. Instead of traditional solid cards, surfaces use a 40-60% opacity white background with a heavy "Backdrop Blur" (20px-30px). This allows the colors of the underlying pool photography to bleed through the UI, creating a cohesive, immersive environment.

Shadows are extremely diffused and low-opacity, using a subtle Deep Cobalt tint (#002147 at 5% opacity) rather than pure black. This creates a soft, natural lift that mimics an object floating on the surface of water rather than a heavy object sitting on a table.

## Shapes

The shape language in this design system is **Rounded**, echoing the organic curves of custom lagoon pools and smoothed stone edges. Standard components use a 0.5rem radius, while larger image containers and feature cards use 1rem. 

Interactive elements like primary buttons may occasionally use pill-shaped (rounded-full) geometry to emphasize a "soft-touch" interface. Heavy use of circular apertures for video previews or secondary imagery further reinforces the water-droplet motif.

## Components

### Buttons
Primary actions are rendered as "Ghost" or "Glass" buttons. They feature a thin 1px border of Deep Cobalt or Pure White, with a subtle backdrop blur. On hover, they fill with a gradient transition to Crystal Cyan. Text remains sharp and high-contrast.

### Cards
Cards are the primary vehicle for showcasing custom builds. They should feature full-bleed imagery with a semi-transparent glass overlay at the bottom containing the project title and location. The transition between the image and the text area should be seamless.

### Input Fields
Forms should be minimalist, using only a bottom border (1px Deep Cobalt) that transforms into Crystal Cyan upon focus. Placeholders should be styled in a light weight of Manrope to appear unobtrusive.

### Interactive Elements
- **Project Gallery:** A horizontal carousel with high-quality video autoplay on hover.
- **Floating Navigation:** A fixed-position glassmorphic bar that remains at the top of the viewport, providing a constant sense of orientation without obscuring the content.
- **Process Timeline:** A vertical line in light Crystal Cyan, using circular nodes to represent stages of pool construction.