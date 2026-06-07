---
name: Heritage & Traditional
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#434843'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#7f5445'
  on-secondary: '#ffffff'
  secondary-container: '#fec4b2'
  on-secondary-container: '#7a4f41'
  tertiary: '#725c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cba829'
  on-tertiary-container: '#4e3e00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#f2baa8'
  on-secondary-fixed: '#311308'
  on-secondary-fixed-variant: '#643d30'
  tertiary-fixed: '#ffe081'
  tertiary-fixed-dim: '#e8c344'
  on-tertiary-fixed: '#231b00'
  on-tertiary-fixed-variant: '#564500'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
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
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
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
  gutter: 24px
  margin-edge: 40px
  section-gap: 80px
---

## Brand & Style

This design system is built upon the concept of "The Modern Estate," blending the storied prestige of traditional equestrianism with the precision of a professional boarding operation. The aesthetic is rooted in a **Tactile / Skeuomorphic** approach, subtly nodding to the craftsmanship of high-end saddlery and stable architecture.

The target audience consists of discerning horse owners and professional riders who value stability, history, and meticulous care. The UI must evoke a sense of quiet luxury and institutional trust. Visuals should leverage subtle paper textures, fine-lined borders that mimic gold leafing, and a layering system that feels grounded and physical. This is not a "fast" interface; it is a deliberate, atmospheric experience that reflects the slow, rhythmic nature of life at a premier stable.

## Colors

The palette is anchored in deep, organic tones that reflect the landscape and materials of a professional stable. 

- **Primary (Forest Green):** Used for primary navigation backgrounds, hero typography, and heavy structural elements. It represents the lush pastures and the core identity of the establishment.
- **Secondary (Mahogany):** Employed for wood-inspired accents, dividers, and secondary iconography. It provides a warm, grounded contrast to the green.
- **Tertiary (Brass):** Reserved exclusively for high-priority calls to action, buttons, and decorative highlights. It mimics the polished hardware of a bridle or stable door.
- **Neutral (Parchment):** A warm off-white is used for backgrounds instead of pure white to maintain the "Heritage" feel and reduce digital glare, mimicking high-quality stationery.

## Typography

This design system utilizes a high-contrast typographic pairing to balance authority with utility. 

**Newsreader** serves as the primary serif for all headlines. Its literary, authoritative strokes provide the prestige required for an established estate. Large display type should use medium weights to emphasize its classic proportions.

**Work Sans** provides a grounded, neutral counterpoint for body copy and functional data. Its clean, slightly wider aperture ensures legibility when viewing stable schedules or boarding agreements. "Label-caps" style should be used for small headers or category tags to maintain a disciplined, organized appearance.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, centered on the screen to create a sense of balance and composure. A 12-column system is used, but with generous outer margins to ensure the content never feels crowded.

The rhythm is intentionally spacious. Large "Section Gaps" are used to separate different service offerings (e.g., Boarding vs. Training), allowing the high-end photography of the horses and facilities to breathe. Elements should align strictly to the grid to convey the order and discipline expected of a professional riding environment.

## Elevation & Depth

This design system avoids aggressive shadows in favor of **Tonal Layers** and **Low-contrast Outlines**. Depth is achieved through the physical metaphor of stacked materials.

1.  **The Base:** The Parchment background (#F9F7F2).
2.  **The Surface:** White "Paper" cards (#FFFFFF) sit atop the base with a very subtle, large-radius ambient shadow (10% opacity Mahogany tint) to suggest thickness.
3.  **The Details:** Thin, 1px solid borders in Mahogany (#4E2A1E) at 20% opacity are used to define regions without adding visual noise.
4.  **The Inset:** Form fields and input areas should use a slight inner "carved" shadow to feel like embossed leather or engraved brass.

## Shapes

The shape language is conservative and architectural. A "Soft" roundedness (0.25rem) is applied to primary UI elements like buttons and cards, suggesting a handcrafted quality rather than a mass-produced digital one. 

Interactive elements like "Brass" buttons may use a slightly higher roundedness for comfort, but should never reach "Pill-shaped" status, as that would appear too playful for this heritage aesthetic. Decorative flourishes, such as image frames, may feature a double-border effect (a thick Forest Green border with a thin Brass inner stroke) to mimic traditional picture framing.

## Components

### Buttons & Controls
Primary buttons are solid **Brass (#B59410)** with white or Forest Green text, featuring a subtle gradient to suggest a metallic sheen. Secondary buttons use an outlined Mahogany style. Hover states should involve a slight darkening of the color and a subtle lift effect.

### Input Fields
Inputs should feel like high-quality stationery. Use the neutral background color for the field, a thin Mahogany border, and Work Sans for the input text. Labels should always be visible (never floating) in "label-caps" style.

### Cards & Boarding Lists
Cards used for displaying horse profiles or stall availability should feature a Forest Green header bar. Lists should be separated by thin, elegant horizontal lines (Mahogany at 15% opacity).

### Specialized Components
- **The "Stall Map":** A custom UI component using Mahogany outlines to represent the stable layout, with Forest Green indicating occupied stalls and Brass for selected/available stalls.
- **The "Heritage Seal":** A decorative circular element containing the stable’s monogram, used sparingly as a watermark or footer ornament to reinforce the brand's established nature.