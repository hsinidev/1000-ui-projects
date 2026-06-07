---
name: Wildwood Ethos
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#42493e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0ef'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#393a29'
  on-tertiary: '#ffffff'
  tertiary-container: '#50513f'
  on-tertiary-container: '#c3c4ac'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: Epilogue
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 20px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system captures the raw, tactile essence of the outdoors, tailored for the early education sector. The brand personality is **Earthy & Adventurous**, balancing the safety and warmth of a classroom with the boundless exploration of the forest. The UI evokes a sense of wonder, stability, and organic growth, targeting parents and educators who prioritize nature-based learning.

The design style is **Tactile / Skeuomorphic-Lite**, moving away from sterile digital surfaces toward elements that feel "found" in nature. This is achieved through subtle paper or grain textures, organic "blob" shapes that mimic stones or leaves, and a heavy reliance on high-resolution nature photography. Every interaction should feel grounded and physical, yet maintain the functional clarity required for mobile-first, outdoor usage.

## Colors

The palette is rooted in the natural world to ensure visual harmony with outdoor environments.
- **Forest Green (#2D5A27):** The primary action color, used for growth-oriented elements and primary buttons.
- **Earthy Brown (#5D4037):** Used for structural elements, secondary actions, and grounding typography.
- **Sand (#F5F5DC):** The primary background color, chosen to reduce the harsh glare of white screens in direct sunlight while maintaining high contrast.
- **Supportive Neutrals:** Deep charcoal is used for body text to ensure maximum legibility against the Sand background under bright outdoor conditions.

## Typography

This design system utilizes a high-contrast typographic pairing to ensure readability in variable lighting.
- **Headers (Epilogue):** A rugged, geometric sans-serif that provides a distinct, "etched" look for brand moments and section titles.
- **Body & Labels (Lexend):** Specifically engineered for readability and accessibility. The wider character glyphs of Lexend reduce visual noise, making it the ideal choice for parents navigating the app while outdoors. 
- **Readability Note:** Body text should never fall below 16px to accommodate users viewing the screen in direct sunlight.

## Layout & Spacing

This design system employs a **fluid grid** model optimized for mobile-first touch targets. A base 8px rhythm governs all spatial relationships. 
- **Mobile:** A single-column layout with 20px side margins to ensure thumbs do not obscure content.
- **Desktop:** A centered 12-column max-width container (1280px) with fluid gutters.
- **Philosophy:** Large, generous tap targets (minimum 48px height) are mandatory for all interactive elements to account for active, outdoor use cases where steady hands are not guaranteed.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Subtle Textures** rather than traditional drop shadows.
- **Layering:** Surfaces use slight variations of Sand and Off-white to create "stacked" depth.
- **Textural Depth:** Cards and containers feature a subtle "grain" or "recycled paper" texture overlay (2% opacity) to give the UI a tactile quality.
- **Shadows:** When necessary, use "Earth Shadows"—soft, low-opacity blurs tinted with Earthy Brown (#5D4037) instead of pure black. This maintains the warm, organic feel of the design system.

## Shapes

The shape language is **Organic and Asymmetrical**. 
- **Containers:** While standard cards use a `1rem` (rounded-lg) radius, "Hero" containers or featured images should use irregular, pebble-like border-radii (e.g., `60% 40% 70% 30% / 40% 50% 60% 50%`) to mimic natural forms.
- **Icons:** Use thick-stroke, rounded-cap icons that feel hand-drawn or carved. 
- **Buttons:** Fully rounded (pill-shaped) buttons are reserved for primary calls-to-action to maximize touch comfort.

## Components

- **Buttons:** Primary buttons are Forest Green with white Lexend text. Secondary buttons use an Earthy Brown border with no fill. All buttons feature a subtle "pressed" state that slightly scales the element down (0.98), mimicking physical displacement.
- **Cards:** Use a "Sand" fill with a 1px solid Earthy Brown border at 10% opacity. Include a "Nature Photography" header for high engagement.
- **Inputs:** Fields should have a distinct "Sand-Dark" background (#EBEBCC) to define the field area clearly against the main Sand background, with a 2px bottom-border highlight on focus.
- **Chips/Badges:** Use "Leaf" shapes (pointed at one end) for status tags like "In the Woods" or "Campsite."
- **Checkboxes:** Styled as small circular stones that "fill with moss" (Forest Green) when selected.
- **Weather Widget:** A specialized component showing current outdoor conditions, using the Epilogue typeface for the temperature display.