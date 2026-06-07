---
name: Warmth & Wisdom
colors:
  surface: '#fff8f4'
  surface-dim: '#e2d8d1'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fcf2ea'
  surface-container: '#f6ece5'
  surface-container-high: '#f1e6df'
  surface-container-highest: '#ebe1da'
  on-surface: '#1f1b17'
  on-surface-variant: '#56423d'
  inverse-surface: '#352f2b'
  inverse-on-surface: '#f9efe8'
  outline: '#89726c'
  outline-variant: '#dcc0b9'
  surface-tint: '#9d4227'
  primary: '#9a4025'
  on-primary: '#ffffff'
  primary-container: '#ba573b'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb5a0'
  secondary: '#75593f'
  on-secondary: '#ffffff'
  secondary-container: '#ffd9b9'
  on-secondary-container: '#7a5d43'
  tertiary: '#5c5c56'
  on-tertiary: '#ffffff'
  tertiary-container: '#75756f'
  on-tertiary-container: '#fffdf5'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a0'
  on-primary-fixed: '#3b0900'
  on-primary-fixed-variant: '#7e2b12'
  secondary-fixed: '#ffdcc0'
  secondary-fixed-dim: '#e5bfa0'
  on-secondary-fixed: '#2b1704'
  on-secondary-fixed-variant: '#5b412a'
  tertiary-fixed: '#e4e3db'
  tertiary-fixed-dim: '#c8c7bf'
  on-tertiary-fixed: '#1b1c17'
  on-tertiary-fixed-variant: '#474742'
  background: '#fff8f4'
  on-background: '#1f1b17'
  surface-variant: '#ebe1da'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.2'
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
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built on the pillars of dignity, warmth, and professional reliability. It centers the human experience of aging, moving away from clinical coldness toward a "home-first" aesthetic. The style leverages a **refined minimalism** blended with **tactile softness**, ensuring that the interface feels like an extension of a comfortable home rather than a medical tool.

The target audience includes both seniors and their family caregivers. To accommodate varying levels of digital literacy and visual acuity, the system prioritizes high-legibility paths, generous hit targets, and an unhurried visual rhythm. The emotional response should be one of immediate relief and trust—a "deep breath" in a stressful period of life.

## Colors

The color strategy uses an earthy, sunset-inspired palette to evoke comfort and maturity. 

- **Primary (Terracotta):** Used for primary actions, branding, and structural emphasis. It provides a grounded, professional foundation.
- **Secondary (Soft Peach):** Used for supportive elements, soft backgrounds, and highlights. It injects warmth and approachable energy.
- **Tertiary (Ivory):** The primary surface color. It reduces eye strain compared to pure white while maintaining a premium, "paper-like" feel.
- **Neutral (Warm Charcoal):** Used for text and icons to ensure high contrast without the harshness of pure black.

Avoid using pure black or vibrating brights; all colors must feel "baked" or organic.

## Typography

This design system utilizes a sophisticated pairing of a classic serif and a modern, rounded sans-serif to bridge the gap between tradition and technology.

- **Headlines:** `notoSerif` provides a sense of literary authority and timelessness. It is used to convey important messages with a "human" voice.
- **Body & UI:** `plusJakartaSans` was selected for its friendly, open apertures and high legibility at larger scales. 

**Accessibility Note:** Base body text starts at 18px to ensure seniors can read comfortably without squinting. Line heights are intentionally generous (1.6) to prevent lines of text from blurring together.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to maintain a controlled, editorial feel. On desktop, a 12-column grid is centered with wide margins to create a focused reading experience. 

Spacing is governed by an 8px rhythmic scale. This design system favors "Ample Whitespace," meaning that when in doubt, increase padding. This reduces cognitive load and makes individual interactive elements easier to distinguish. Sections of content should be separated by large vertical gaps (`xl`) to allow the eye to rest.

## Elevation & Depth

To maintain the "soft and premium" aesthetic, this design system avoids harsh dropshadows. Instead, it utilizes **Tonal Layers** and **Ambient Shadows**.

- **Surface Tiers:** Ivory is the base. Elements like cards use a slightly lighter "Super White" or the Soft Peach color to suggest elevation.
- **Shadows:** Use extremely diffused, low-opacity shadows (10-15% opacity) with a slight Terracotta tint (`#C05C3F`) rather than grey. This makes shadows feel like natural "warm light" rather than digital depth.
- **Depth Cues:** Depth is used sparingly to signify interactivity (e.g., a card lifting slightly on hover).

## Shapes

The shape language is defined by **organic softness**. Sharp corners are strictly avoided as they feel clinical or aggressive. 

- **Primary Elements:** Buttons and Input fields use a 0.5rem (`rounded-md`) radius.
- **Containers:** Cards and modals use a 1rem (`rounded-lg`) or 1.5rem (`rounded-xl`) radius to create a "cradled" look.
- **Decorative:** Small circular accents can be used to mirror the rounded terminals of the typography.

## Components

### Buttons
Primary buttons are solid Terracotta with white or Ivory text. They feature generous internal padding (16px top/bottom, 32px left/right) to ensure a large hit area for aging hands. Secondary buttons use a Soft Peach fill with Terracotta text.

### Cards
Cards are the primary container for information. They should feature a subtle 1px border in a darkened Peach or a soft ambient shadow. Large imagery within cards should always have rounded corners to match the container.

### Inputs
Input fields must have clear, persistent labels (never use placeholder-only labels). The stroke should thicken and change to Terracotta when focused, providing a clear visual indicator of the active field.

### Progress Indicators
For multi-step care forms, use soft, rounded progress bars in Soft Peach, filling with Terracotta. This provides a gentle, encouraging sense of movement.

### Accessibility Components
Include a "Text Size" toggle and high-contrast mode switch in the global utility navigation to empower users with varying visual needs.