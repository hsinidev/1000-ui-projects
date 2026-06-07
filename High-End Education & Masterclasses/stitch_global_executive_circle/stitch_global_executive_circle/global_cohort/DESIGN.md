---
name: Global-Cohort
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#c6c6ce'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#909098'
  outline-variant: '#46464d'
  surface-tint: '#bfc5e4'
  primary: '#bfc5e4'
  on-primary: '#292f48'
  primary-container: '#0a1128'
  on-primary-container: '#767c99'
  inverse-primary: '#575d78'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#111313'
  on-tertiary-container: '#7d7e7e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#bfc5e4'
  on-primary-fixed: '#141a32'
  on-primary-fixed-variant: '#3f465f'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.15em
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 24px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
  gutter: 16px
---

## Brand & Style

This design system embodies an **Executive-Chic** aesthetic, tailored for a high-net-worth peer networking environment. The brand personality is authoritative yet discreet, prioritizing quiet luxury over loud patterns. 

The visual style leverages **Glassmorphism** to create depth and hierarchy. Surfaces appear as semi-translucent, frosted layers that float above a deep, immersive background. The interface is characterized by high-end minimalism, using generous negative space and precision-aligned elements to convey a sense of curated exclusivity. Every interaction should feel intentional, mimicking the tactile experience of a premium physical concierge service.

## Colors

The color palette is built on a foundation of deep contrast and metallic accents.

*   **Midnight Blue (#0A1128):** The primary canvas. This deep, near-black blue provides a sense of stability and institutional trust. It serves as the base for all glass effects.
*   **Gold-Foil (#D4AF37):** Used sparingly for high-impact accents, such as call-to-action borders, thin separators, and active states. It represents the "Executive" tier of the platform.
*   **Silk White (#F8F9FA):** The primary typography and iconography color. It is softened slightly from pure white to reduce eye strain and provide a more "analog paper" feel.
*   **Glass Surface:** A semi-transparent overlay (rgba(255, 255, 255, 0.04)) combined with a heavy backdrop blur (20px-40px) to create the frosted glass effect.

## Typography

This design system utilizes a sophisticated typographic pairing to balance heritage with modernity.

**Playfair Display** is reserved for headlines and large display quotes. Its high-contrast serifs convey the authority and tradition of a legacy publication or private club.

**Hanken Grotesk** is used for all functional text, navigation, and body copy. Its clean, geometric proportions ensure high legibility on mobile screens while maintaining a contemporary, technical edge. 

*   Use **label-caps** for section headers and small navigational cues to evoke the feeling of a premium watch face or luxury stationery.
*   Keep line lengths for body text controlled to maintain a vertical, "columnar" editorial feel.

## Layout & Spacing

This design system follows a **Mobile-First, Contextual Grid** model. 

The primary layout relies on a 24px side margin to give content "room to breathe," reflecting the minimalist brand values. Vertical rhythm is strictly governed by a 4px base unit, with components typically separated by 16px (stack-md) or 32px (stack-lg) to maintain visual hierarchy.

In place of heavy grid lines, the system uses "white space as a separator." When grouping content, rely on glass containers rather than visible lines, ensuring the layout feels light and fluid.

## Elevation & Depth

Hierarchy is established through **Backdrop Blur** and **Ambient Glows** rather than traditional drop shadows.

*   **Layer 0 (Base):** Midnight Blue background.
*   **Layer 1 (Cards/Navigation):** Frosted glass (4% white opacity) with a 30px backdrop blur. These elements feature a 0.5px "Silk White" border at 10% opacity to define the edge.
*   **Layer 2 (Modals/Popovers):** Higher opacity glass (8% white) with a 40px blur. 
*   **Shadows:** Use extremely diffused, large-radius shadows (Blur: 40px, Spread: -10px) with a dark navy tint (rgba(0, 0, 0, 0.4)) to create a subtle "lift" for interactive cards.
*   **Accents:** Gold-Foil lines (1px height) are used at the top or bottom of high-priority containers to signify premium status.

## Shapes

The shape language is refined and disciplined. Rectilinear forms predominate, but with a **Soft (0.25rem)** corner radius to prevent the UI from feeling sharp or aggressive.

*   **Buttons & Inputs:** Use the standard soft radius (4px) to maintain a professional, architectural feel.
*   **Feature Cards:** May use the **rounded-lg (8px)** setting to feel more approachable and "touchable" on mobile.
*   **Dividers:** Use ultra-thin (0.5px) horizontal lines, often fading out at the edges (linear gradient) to create a sophisticated, disappearing-point effect.

## Components

### Buttons
*   **Primary:** Transparent background with a 1px Gold-Foil border. Text is Silk White in "label-caps" style.
*   **Secondary:** Glass surface with a subtle Silk White border.
*   **Interaction:** On press, provide a subtle haptic pulse and increase the border glow of the gold-foil.

### Cards
Premium cards are the core of the networking experience. They feature a frosted glass background, a subtle 1px Silk White border at 10% opacity, and a soft shadow. High-priority cards (e.g., "Featured Peer") include a 1px Gold-Foil line at the top edge.

### Input Fields
Inputs are minimalist, consisting of a Silk White "label-caps" header and a simple underline in 10% Silk White. Upon focus, the underline transitions to Gold-Foil.

### Lists & Peer Rows
Rows are separated by thin, fading dividers. Icons are always Silk White and utilize a minimalist, thin-stroke (1.5px) icon set.

### Haptic Feedback
Since the platform is mobile-first, utilize "Light" haptics for navigation transitions and "Medium" haptics for successful connections or gold-tier interactions. This adds a physical sense of quality to the digital interface.