---
name: ZenPoint
colors:
  surface: '#fff8f5'
  surface-dim: '#dfd9d6'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f2ef'
  surface-container: '#f3ede9'
  surface-container-high: '#ede7e4'
  surface-container-highest: '#e8e1de'
  on-surface: '#1d1b19'
  on-surface-variant: '#434842'
  inverse-surface: '#33302e'
  inverse-on-surface: '#f6efec'
  outline: '#747872'
  outline-variant: '#c4c8c0'
  surface-tint: '#546254'
  primary: '#516051'
  on-primary: '#ffffff'
  primary-container: '#6a7869'
  on-primary-container: '#f7fff3'
  inverse-primary: '#bbcbb9'
  secondary: '#6b5c4c'
  on-secondary: '#ffffff'
  secondary-container: '#f4dfcb'
  on-secondary-container: '#716252'
  tertiary: '#5c5c58'
  on-tertiary: '#ffffff'
  tertiary-container: '#757571'
  on-tertiary-container: '#fefcf7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e7d4'
  primary-fixed-dim: '#bbcbb9'
  on-primary-fixed: '#121e13'
  on-primary-fixed-variant: '#3c4a3d'
  secondary-fixed: '#f4dfcb'
  secondary-fixed-dim: '#d7c3b0'
  on-secondary-fixed: '#241a0e'
  on-secondary-fixed-variant: '#524436'
  tertiary-fixed: '#e4e2dd'
  tertiary-fixed-dim: '#c8c6c2'
  on-tertiary-fixed: '#1b1c19'
  on-tertiary-fixed-variant: '#474744'
  background: '#fff8f5'
  on-background: '#1d1b19'
  surface-variant: '#e8e1de'
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
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0em
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
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.08em
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
  gutter: 24px
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style

This design system embodies the intersection of ancient healing wisdom and contemporary luxury wellness. The brand personality is grounded, restorative, and sophisticated, targeting an affluent audience seeking holistic balance without sacrificing modern refinement. 

The visual style is rooted in **Minimalism** with a **Tactile** edge. It prioritizes "negative space as breathing room," ensuring the UI never feels cluttered or clinical. The emotional response should be an immediate sense of lowered cortisol—a digital sanctuary that mirrors the physical experience of a high-end acupuncture clinic. Organic textures, such as rice paper grains or soft linen weaves, should be used subtly in backgrounds to prevent the interface from feeling "flat" or cold.

## Colors

The palette is derived from natural elements found in Traditional Chinese Medicine: dried herbs, stone, and unprocessed silk. 

- **Primary (Soft Sage):** Used for primary actions, active states, and brand accents. It represents growth and vitality.
- **Secondary (Earthy Beige):** Used for subtle backgrounds, dividers, and decorative elements to ground the UI.
- **Tertiary (Off-White):** The canvas color. It is a warm, "paper" white that reduces eye strain compared to pure hex white.
- **Neutral (Charcoal Stone):** Used exclusively for typography and deep contrast to ensure legibility while maintaining a softer look than pure black.

## Typography

The typography strategy pairs the intellectual authority of a serif with the functional clarity of a modern sans-serif.

- **Headlines:** Use **Noto Serif**. This font provides a literary, high-end editorial feel. For large displays, use lower-case or sentence-case to maintain a humble, approachable tone.
- **Body & Labels:** Use **Manrope**. Its geometric yet slightly softened terminals offer excellent readability for health-related information while appearing more premium than standard system fonts.
- **Stylistic Note:** All-caps should be reserved for small labels and navigation items with increased letter spacing to create an "architectural" feel.

## Layout & Spacing

This design system utilizes a **Fixed Grid** for desktop and a **Fluid Grid** for mobile devices. The rhythm is intentionally slow and spacious.

- **Generous Whitespace:** Vertical gaps between sections should be significant (minimum 120px) to allow the eye to rest between pieces of content.
- **Content Alignment:** Center-aligned layouts are preferred for landing pages to evoke a sense of balance (Zen). For dashboard or booking flows, use left-aligned content with wide gutters.
- **Asymmetry:** Occasionally break the grid with an offset image or an overlapping text block to mimic the organic, non-linear nature of natural textures.

## Elevation & Depth

To maintain a minimalist aesthetic, depth is achieved through **Tonal Layers** rather than heavy shadows.

- **Surface Tiers:** Use the Tertiary (Off-White) for the base page. Use secondary (Earthy Beige) or a slightly lighter tint for cards and containers to create subtle separation.
- **Ambient Shadows:** When necessary for functional elevation (e.g., a modal or floating action button), use a very soft, diffused shadow: `0px 12px 32px rgba(62, 59, 57, 0.04)`. The shadow should feel like a soft glow of light rather than a hard drop shadow.
- **Low-Contrast Outlines:** Buttons and inputs should use a 1px border in a shade slightly darker than the background (the Secondary color) to define shape without adding visual weight.

## Shapes

The shape language is "Softened Geometry." While the system is modern and structured, pure 90-degree angles are avoided to prevent a clinical feel. 

- **Primary Radius:** Use 0.25rem (4px) for most interactive elements like inputs and buttons. This provides just enough softness to feel "human" while maintaining a sophisticated, crisp profile.
- **Imagery:** Photography should either be perfectly rectangular or use a very large, organic "pebble" radius on one or two corners to mimic smoothed river stones.

## Components

- **Buttons:** Primary buttons are solid Soft Sage with Off-White text. Secondary buttons are outlined in Charcoal Stone with generous internal padding (16px 32px). Labels are always in the Label-MD style, all-caps.
- **Input Fields:** Minimalist design with only a bottom border or a very light Earthy Beige background. Labels sit above the field in a bold, small font. Focus states should be a subtle transition to the Soft Sage color.
- **Cards:** No heavy borders. Use a slightly different tonal background (Tertiary to Secondary) and soft padding. Cards for services (Acupuncture, Cupping) should feature high-resolution, macro photography of textures (bamboo, silk, skin).
- **Chips / Tags:** Pill-shaped with a low-opacity Soft Sage fill. Used for treatment categories or practitioner specialties.
- **Progress Indicators:** For booking flows, use thin, elegant lines and Noto Serif numerals. Avoid bulky "step" icons.
- **Specialty Component - The "Ritual" Loader:** A custom loading animation involving a slow-expanding circle or a fading ink-drop effect, reinforcing the calming nature of the brand during wait times.