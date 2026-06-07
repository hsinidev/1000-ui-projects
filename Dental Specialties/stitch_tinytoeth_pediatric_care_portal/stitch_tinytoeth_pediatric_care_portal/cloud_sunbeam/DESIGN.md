---
name: Cloud & Sunbeam
colors:
  surface: '#f6fafe'
  surface-dim: '#d6dade'
  surface-bright: '#f6fafe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f4f8'
  surface-container: '#eaeef2'
  surface-container-high: '#e4e9ed'
  surface-container-highest: '#dfe3e7'
  on-surface: '#171c1f'
  on-surface-variant: '#41484d'
  inverse-surface: '#2c3134'
  inverse-on-surface: '#edf1f5'
  outline: '#71787e'
  outline-variant: '#c1c7ce'
  surface-tint: '#2e6385'
  primary: '#2e6385'
  on-primary: '#ffffff'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#9accf3'
  secondary: '#686000'
  on-secondary: '#ffffff'
  secondary-container: '#f0e269'
  on-secondary-container: '#6d6400'
  tertiary: '#835500'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffc87f'
  on-tertiary-container: '#7d5000'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#f3e56c'
  secondary-fixed-dim: '#d6c953'
  on-secondary-fixed: '#1f1c00'
  on-secondary-fixed-variant: '#4e4800'
  tertiary-fixed: '#ffddb4'
  tertiary-fixed-dim: '#ffb954'
  on-tertiary-fixed: '#291800'
  on-tertiary-fixed-variant: '#633f00'
  background: '#f6fafe'
  on-background: '#171c1f'
  surface-variant: '#dfe3e7'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  section-gap: 80px
---

## Brand & Style
The brand personality centers on "Calm Playfulness." It seeks to dismantle the clinical coldness typically associated with dentistry, replacing it with a soft, breathable atmosphere that appeals to a child's sense of wonder while reassuring parents of clinical excellence. 

This design system utilizes a **Minimalist-Neomorphic hybrid** style. It leverages heavy whitespace to reduce cognitive load and anxiety, paired with soft, extruded "bubble" elements that feel tactile and friendly. The visual language avoids sharp corners and aggressive transitions, opting instead for organic shapes and subtle motion that mimics the gentle floating of bubbles.

## Colors
The palette is anchored by **Pastel Blue**, used to evoke a sense of hygiene, water, and serenity. **Lemon** serves as the energetic accent, used sparingly to draw attention to positive actions and "sunny" achievements like a completed check-up. 

A deep charcoal navy is used for typography to ensure AA/AAA accessibility for parents, while the background remains a soft, off-white "Cloud" grey to prevent the harsh glare of pure white. Success states use a soft mint, and warnings use a warm peach to keep the emotional tone regulated and non-threatening.

## Typography
**Plus Jakarta Sans** is the sole typeface for this design system. Its naturally rounded terminals and geometric clarity provide a friendly, modern rhythm that is easy for children to read and professional enough for medical documentation. 

Headlines use a tighter letter-spacing and heavier weights to feel bold and reassuring. Body text is set with generous line heights to ensure a "breezy" reading experience, preventing parent-facing information from feeling dense or overwhelming.

## Layout & Spacing
The design system employs a **fixed grid** for desktop (12 columns) and a **fluid grid** for mobile (4 columns). The layout philosophy is defined by "Extra-Safe Margins." By utilizing wider-than-average gutters and significant vertical gaps between sections, the UI feels uncrowded and peaceful. 

Components are grouped in "bubble clusters," where related items share a soft background container with internal padding of 24px or 32px to maintain the airy aesthetic.

## Elevation & Depth
Depth is created through **Ambient Shadows** and tonal layering rather than high-contrast lines. Surfaces use a "floating" effect, achieved by applying very soft, diffused shadows tinted with the primary blue color (`rgba(165, 216, 255, 0.3)`). 

Interactive elements should appear slightly extruded from the background. When hovered, elements should use a subtle upward "float" animation (Y-axis shift) and a slight increase in shadow spread to mimic a physical bubble rising toward the user. No harsh black shadows are permitted; all depth must feel atmospheric and light.

## Shapes
The shape language is strictly **Pill-shaped and organic**. Sharp corners are non-existent in this design system. Large containers use the `rounded-xl` (3rem) setting to mimic smooth river stones or soft clouds. Buttons and input fields always use a full-pill radius. 

Icons should follow this logic, using rounded caps and joins to ensure every visual element feels "touch-safe" and friendly. Decorative "bubble" elements—semi-transparent circles of varying sizes—should be scattered in the background layout to reinforce the brand's whimsical nature.

## Components
- **Buttons:** Primary buttons are pill-shaped, using the Lemon accent color with a soft blue shadow. Text is bold and centered.
- **Cards:** Use a white or very pale blue background with a `rounded-xl` corner radius and an ambient shadow. Avoid borders; use color shifts to define boundaries.
- **Input Fields:** Oversized, pill-shaped fields with a light blue background and a secondary lemon border only on focus.
- **Chips:** Small, highly-rounded tags used for categorizing dental services or age groups (e.g., "Toddlers," "Teens").
- **Checkboxes & Radios:** Scaled up by 20% from standard sizes to be more "tappable." Use a soft checkmark icon rather than a sharp "V".
- **Floating Progress Indicators:** For appointment booking or educational modules, use a series of soft, glowing circles that fill with the Pastel Blue color as the user progresses.
- **Instructional Illustrations:** All icons and illustrations must feature soft, rounded edges and be placed within circular or "blob-shaped" frames to maintain the bubble theme.