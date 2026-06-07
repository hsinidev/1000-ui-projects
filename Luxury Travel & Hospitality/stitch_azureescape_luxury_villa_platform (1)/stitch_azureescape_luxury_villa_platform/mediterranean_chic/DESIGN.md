---
name: Mediterranean Chic
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#434653'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#2559bd'
  primary: '#00327d'
  on-primary: '#ffffff'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#b1c5ff'
  secondary: '#6a5e33'
  on-secondary: '#ffffff'
  secondary-container: '#f3e2ac'
  on-secondary-container: '#706439'
  tertiary: '#353737'
  on-tertiary: '#ffffff'
  tertiary-container: '#4b4d4e'
  on-tertiary-container: '#bdbebe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#f3e2ac'
  secondary-fixed-dim: '#d6c692'
  on-secondary-fixed: '#231b00'
  on-secondary-fixed-variant: '#51461e'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
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
  gutter: 24px
  margin-page: 64px
  section-gap: 120px
  container-max: 1440px
---

## Brand & Style

This design system is anchored in the concept of "Mediterranean Chic," a philosophy that marries the effortless elegance of coastal living with the precision of ultra-luxury service. The brand personality is aspirational, serene, and authoritative, targeting a high-net-worth audience that values exclusivity and tranquility.

The visual style is a refined take on **Minimalism**, utilizing expansive white space to evoke the airy openness of a private villa overlooking the Aegean. Every element is intentional; the UI never feels crowded, allowing high-contrast, high-production photography of architectural details and sea vistas to act as the primary storyteller. The emotional response is one of immediate decompression and sophisticated indulgence.

## Colors

The palette for this design system is derived from the natural elements of a luxury coastal escape. **Crisp White** serves as the primary canvas, providing a clinical yet inviting foundation that emphasizes cleanliness and light. **Cobalt Blue** is used strategically as the primary action and signature color, representing the depth of the Mediterranean and providing high-contrast focal points.

**Sand** acts as a sophisticated secondary accent, used for subtle highlights, divider lines, or soft backgrounds to provide warmth and organic texture against the cooler primary tones. Neutrals are kept to a minimum, using a deep charcoal rather than pure black for text to maintain a softer, high-end editorial feel.

## Typography

Typography in this design system creates a rhythmic contrast between traditional elegance and modern utility. **Noto Serif** is the voice of the brand, used for all headlines to convey a sense of heritage, luxury, and editorial authority. Headlines should be set with generous leading and slight negative tracking in larger sizes to feel more "locked-in."

**Inter** provides a clean, functional counterpoint for body copy and UI elements. It ensures high readability for property details, booking flows, and technical data. The "label-caps" style is particularly important for secondary metadata, utilizing wide letter spacing to maintain a premium feel even at small scales.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to ensure the content remains curated and centered, preventing the high-end photography from stretching awkwardly. On larger screens, the maximum container width is strictly enforced, surrounded by vast margins that act as "negative space frames" for the content.

The spacing rhythm is intentionally oversized. Rather than standard tight grouping, this design system utilizes large "section-gaps" to allow each property or feature to breathe independently. Gutters are wide to prevent a cluttered appearance, ensuring that the interface feels as expansive as the villas it showcases.

## Elevation & Depth

This design system rejects heavy drop shadows in favor of **Ambient Shadows** and **Tonal Layers**. Depth is conveyed through subtle differences in surface color—moving from Crisp White to a very faint Sand-tinted off-white for nested containers.

Shadows, when used, are extremely diffused with low opacity (3-5%) and a slight Cobalt or Sand tint to avoid the "dirty" look of grey shadows. This creates a soft "lift" rather than a hard separation. Minimalist, 1px borders in a Sand or light grey tone are preferred over shadows for defining structural boundaries like input fields or property cards, maintaining a flat, architectural aesthetic.

## Shapes

The shape language is refined and "Soft." By utilizing a low-radius `rounded-sm` (0.25rem) approach, the UI retains the structured, professional feel of high-end architecture while avoiding the clinical coldness of sharp 90-degree corners.

Interactive elements like buttons and cards follow this subtle rounding. Larger containers or property images may use a slightly more pronounced radius (up to 0.5rem) to feel more inviting, but the system never moves into "pill-shaped" territory, as that would detract from the sophisticated, editorial tone of the design system.

## Components

### Buttons
Primary buttons are solid **Cobalt Blue** with white text, utilizing Noto Serif for a unique, high-end look on the label. Secondary buttons use a **Sand** 1px border with a transparent background. Hover states should involve a subtle shift in background opacity or a gentle lift via an ambient shadow.

### Cards
Property cards are the centerpiece. They feature full-bleed imagery with a minimal white footer for details. Typography within cards should be highly hierarchical—the price and location in Noto Serif, and amenities in Inter labels.

### Input Fields
Inputs are minimalist: a 1px Sand border on the bottom only, or a very light four-sided border. The focus state transitions the border to Cobalt Blue. Labels are always placed above the field in "label-caps" Inter.

### Date Pickers & Search
As a travel product, the search bar is a high-visibility component. It should be designed as a single, floating white bar with soft elevation, using thin vertical Sand dividers to separate location, dates, and guest count.

### Navigation
The header is sticky but ultra-slim, utilizing a transparent background that transitions to Crisp White upon scroll. Navigation links are set in Inter with a Cobalt active state indicator.