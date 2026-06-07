---
name: Ethereal Presence
colors:
  surface: '#fdf9f4'
  surface-dim: '#ddd9d5'
  surface-bright: '#fdf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3ee'
  surface-container: '#f2ede8'
  surface-container-high: '#ece7e3'
  surface-container-highest: '#e6e2dd'
  on-surface: '#1c1b19'
  on-surface-variant: '#49473d'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f4f0eb'
  outline: '#7a776c'
  outline-variant: '#cbc6b9'
  surface-tint: '#635f40'
  primary: '#635f40'
  on-primary: '#ffffff'
  primary-container: '#b2ac88'
  on-primary-container: '#444024'
  inverse-primary: '#cec7a2'
  secondary: '#5e604d'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1c9'
  on-secondary-container: '#636451'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#aaabab'
  on-tertiary-container: '#3e4040'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#eae3bc'
  primary-fixed-dim: '#cec7a2'
  on-primary-fixed: '#1f1c04'
  on-primary-fixed-variant: '#4b472b'
  secondary-fixed: '#e4e4cc'
  secondary-fixed-dim: '#c8c8b0'
  on-secondary-fixed: '#1b1d0e'
  on-secondary-fixed-variant: '#474836'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fdf9f4'
  on-background: '#1c1b19'
  surface-variant: '#e6e2dd'
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
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
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
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built upon the principle of "Quiet Luxury"—a sophisticated intersection of clinical precision and holistic sanctuary. The brand personality is grounded, wise, and restorative, targeting a discerning audience that values silence and intentionality over volume. 

The aesthetic is a purist form of **Minimalism**. It rejects unnecessary ornamentation, favoring maximum white space to allow content to breathe and reduce cognitive load. The UI should evoke an immediate sense of lowered heart rate and clarity. Every element is intentional, creating an interface that feels less like a tool and more like a serene digital extension of a physical retreat.

## Colors

The palette is derived from natural, tactile elements to foster a sense of organic well-being.
- **Sage Green (#B2AC88):** Used as the primary signal for action and brand identity, representing growth and healing.
- **Pale Wood (#F5F5DC):** Provides a warm, structural foundation. Use this for large surface areas to prevent the interface from feeling "cold" or "sterile."
- **Pure White (#FFFFFF):** The primary background color, used aggressively to create "air" and luxury.
- **Deep Olive (#4A4D40):** A custom neutral used for high-contrast typography and essential UI borders to ensure accessibility while maintaining the earthy tone.

## Typography

This design system utilizes a high-contrast typographic pairing to balance tradition with modernity. **Noto Serif** provides the editorial authority and timeless elegance required for a high-end retreat, while **Manrope** offers a clean, ultra-readable framework for complex medical or scheduling information. 

Headlines should be set with generous leading and occasional italics for emphasis. Body text relies on a light font weight (300) to maintain the "airy" aesthetic, ensuring that even dense information feels light and approachable.

## Layout & Spacing

The layout follows a **Fixed Grid** model to create a sense of stable, architectural order. Content is centered within a generous container with wide page margins that act as a visual "buffer" from the edges of the viewport.

The spacing rhythm is intentionally oversized. Rather than packing elements tightly, this design system mandates large vertical gaps (`section-gap`) between content blocks to facilitate a slow, meditative scrolling experience. Components should never feel crowded; when in doubt, increase padding.

## Elevation & Depth

To maintain a minimalist and "Zen" atmosphere, this design system avoids traditional drop shadows. Depth is instead communicated through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surfaces:** Use the Pale Wood tone to create "containers" on top of White backgrounds.
- **Borders:** Utilize 0.5pt to 1pt delicate borders in Sage Green or Deep Olive at 20% opacity. 
- **Interaction:** Depth is hinted at through subtle shifts in background opacity (e.g., a button moving from a Pale Wood fill to a Pure White fill) rather than physical extrusion or shadows.

## Shapes

The shape language is "Soft," utilizing a 4px (0.25rem) base radius. This creates a subtle hint of organic warmth without the "playfulness" associated with highly rounded or pill-shaped buttons. 

Geometric precision is key; corners should feel intentional and crisp, reflecting the "medical" aspect of the brand, while the slight rounding softens the overall interface to align with the "wellness" aspect. Larger containers like image frames or cards may occasionally use `rounded-lg` (8px) to emphasize their role as a soft landing spot for the eye.

## Components

### Buttons
Primary buttons use a solid Sage Green fill with White text. Secondary buttons are "Ghost" style, featuring a delicate 1px border in Deep Olive with high letter-spacing on the label. All buttons should have generous internal padding (16px vertical / 32px horizontal).

### Cards
Cards are defined by a Pale Wood background or a thin, low-opacity Sage border. They do not use shadows. They should contain ample internal padding to ensure text does not crowd the edges.

### Input Fields
Inputs are minimalist, consisting of a single bottom border (underline) rather than a full box, or a very light Pale Wood fill. Focus states are signaled by the underline transitioning to a solid Sage Green.

### Lists & Navigation
Navigation items should be spaced widely. Use delicate horizontal dividers (1px height, 10% opacity) between list items to maintain structure without adding visual noise.

### Specialized Components: "The Breath"
Include a custom loading component or progress indicator called "The Breath"—a soft, pulsing Sage Green circle that expands and contracts slowly, reinforcing the brand's focus on calm and mindfulness.