---
name: GlobalStudy Design Narrative
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
  on-surface-variant: '#3e4944'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6e7a74'
  outline-variant: '#bdc9c2'
  surface-tint: '#006c52'
  primary: '#006c52'
  on-primary: '#ffffff'
  primary-container: '#98ffd9'
  on-primary-container: '#00785c'
  inverse-primary: '#73d9b5'
  secondary: '#695c50'
  on-secondary: '#ffffff'
  secondary-container: '#f2dfd0'
  on-secondary-container: '#706256'
  tertiary: '#5f5e5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#eeebea'
  on-tertiary-container: '#6b6a69'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#8ff6d0'
  primary-fixed-dim: '#73d9b5'
  on-primary-fixed: '#002117'
  on-primary-fixed-variant: '#00513d'
  secondary-fixed: '#f2dfd0'
  secondary-fixed-dim: '#d5c3b5'
  on-secondary-fixed: '#231a11'
  on-secondary-fixed-variant: '#51453a'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  caption:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max-width: 1280px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
---

## Brand & Style
This design system bridges the gap between academic rigor and the evocative spirit of global exploration. The brand personality is **Aspirational, Scholarly, and Boundless**. It targets students and parents who seek the security of an established institution paired with the life-changing thrill of international travel.

The visual style is a refined **Minimalism** infused with **High-Fidelity accents**. It utilizes generous whitespace to create a sense of openness—mirroring a vast horizon—while maintaining a strict, underlying grid to communicate reliability. Travel-inspired motifs, such as subtle topographic line patterns and coordinate-based iconography, serve as sophisticated textural overlays rather than literal decorations.

## Colors
The palette is inspired by the intersection of land and sea. **Seafoam Green** serves as the primary action color, providing a fresh, energetic spark that symbolizes growth and new beginnings. **Sand** acts as the grounding secondary tone, used for containers, secondary surfaces, and tonal depth to evoke the warmth of a physical campus or a distant shore. 

**White** is the dominant canvas color, ensuring the interface remains airy and uncluttered. A deep charcoal (#1A1A1A) is reserved for typography and high-contrast UI elements to ensure accessibility and a sense of institutional weight.

## Typography
The typographic pairing is a deliberate tension between the old world and the new. **Noto Serif** is used for headlines to convey the authority of a traditional university and the storytelling aspect of a travel journal. It should be typeset with slightly tighter tracking in large display sizes to maintain a premium feel.

**Work Sans** provides a functional, modern counterpoint. Its clean, geometric construction ensures legibility in dense informational layouts such as course listings or visa requirements. All body copy should utilize generous line height to maintain the "airy" quality of the design system.

## Layout & Spacing
This design system employs a **Fixed Grid** model for desktop views to maintain a structured, editorial appearance. The layout is built on a 12-column system with a 24px gutter and significant 64px outer margins to "frame" the content like a high-end travel magazine.

Spacing follows a strict 8px base unit. To achieve the "generous whitespace" requested, vertical section margins should default to the `stack-xl` (64px) or even double that for major content transitions. Proximity should be used to clearly group academic requirements while separating distinct "adventures" or destination cards.

## Elevation & Depth
Depth is handled through **Tonal Layers** and **Ambient Shadows**. This design system avoids heavy shadows, opting instead for ultra-diffused, low-opacity shadows (e.g., 4% opacity) that give the impression of elements floating slightly above a white surface.

To differentiate between "Adventure" content and "Academic" content, use the **Sand** color as a subtle background tint for container surfaces. When an element requires focus, use a thin, 1px border in a slightly darker Sand tint rather than a shadow to maintain the "Structured" aspect of the aesthetic. Backdrop blurs (Glassmorphism) are reserved exclusively for navigation overlays and sticky headers to keep the travel imagery visible as the user scrolls.

## Shapes
The shape language is **Rounded**, utilizing a 0.5rem (8px) base radius. This softening of the "Structured" grid makes the interface feel approachable and human. 

- **Small elements** (buttons, inputs): 0.5rem.
- **Large elements** (cards, images, modal containers): 1rem (rounded-lg).
- **Interactive Accents**: Use circular (pill-shaped) geometry for tags and category chips to contrast against the more rigid rectangular grid of the content cards.

## Components
### Buttons & Inputs
Primary buttons are styled in **Seafoam Green** with black text, using the base roundedness. Hover states should involve a subtle scale-up (1.02x) rather than a dramatic color shift, emphasizing the high-fidelity feel. Input fields utilize a 1px Sand border that thickens and shifts to Seafoam upon focus.

### Cards
Cards are the primary vehicle for destination discovery. They should feature full-bleed imagery at the top with a 1rem top-radius. The content area of the card should use a White or Sand background. A subtle "Stamp" or "Postmark" icon can be used in the corner of featured cards as a travel-inspired accent.

### Navigation & Progress
Progress trackers (for application phases) should be linear and structured, using Seafoam for completed steps. Navigation utilizes **Work Sans** in all-caps for a rhythmic, professional header.

### Special Accents
- **The Horizon Line**: A thin, horizontal Seafoam or Sand rule used to separate major editorial sections.
- **Map Overlays**: UI components that float over map views should use a light Glassmorphism effect (backdrop-blur: 12px) to maintain the aspirational quality of the photography.