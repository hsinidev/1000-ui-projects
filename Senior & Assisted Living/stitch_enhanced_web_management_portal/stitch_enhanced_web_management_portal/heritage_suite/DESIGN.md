---
name: Heritage Suite
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#44474d'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#75777e'
  outline-variant: '#c5c6ce'
  surface-tint: '#515f7a'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#0c1b33'
  on-primary-container: '#7684a1'
  inverse-primary: '#b9c7e6'
  secondary: '#775a1d'
  on-secondary: '#ffffff'
  secondary-container: '#fdd48b'
  on-secondary-container: '#775a1d'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1c19'
  on-tertiary-container: '#858480'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e3ff'
  primary-fixed-dim: '#b9c7e6'
  on-primary-fixed: '#0c1b33'
  on-primary-fixed-variant: '#394761'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e8c179'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5c4204'
  tertiary-fixed: '#e5e2de'
  tertiary-fixed-dim: '#c8c6c2'
  on-tertiary-fixed: '#1c1c19'
  on-tertiary-fixed-variant: '#474744'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
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
  gutter: 32px
  section-padding: 120px
  margin-sm: 16px
  margin-md: 32px
  margin-lg: 64px
---

## Brand & Style

The design system is anchored in the concept of "Restorative Elegance." It moves away from the clinical aesthetic typical of senior care and instead adopts the visual language of a five-star boutique hotel. The brand personality is poised, serene, and deeply attentive. 

The chosen style is **Editorial Minimalism**. It prioritizes high-end photography and "lean-back" readability, creating a sense of calm and spaciousness. This approach honors the user's dignity by providing a premium digital experience that feels like browsing a luxury travel magazine. The UI is quiet, allowing the quality of the service and the beauty of the environments to take center stage.

## Colors

The palette for this design system is rooted in tradition and luxury. 
- **Deep Navy (Primary):** Evokes trust, stability, and professional excellence. It is used for primary navigation and core structural elements.
- **Gold Accents (Secondary):** Used sparingly to denote premium quality and success. It serves as the primary call-to-action color and for delicate ornamentation.
- **Marble & Parchment (Tertiary):** Soft off-whites and very light greys provide a tactile, organic warmth that prevents the UI from feeling cold.
- **Marble Textures:** Applied as subtle CSS background overlays or high-resolution image assets to add depth and a sense of physical permanence to the digital space.

## Typography

Typography in this design system creates an authoritative yet welcoming hierarchy. 
- **Headlines:** Use **Noto Serif**. Its classic proportions and refined serifs communicate sophistication and literary quality. Large headlines should use tighter letter spacing to maintain a premium "masthead" look.
- **Body:** Use **Inter**. It provides exceptional legibility for older eyes while remaining modern and unobtrusive.
- **Labels:** Small labels and overlines should use Inter in all-caps with generous letter spacing to evoke the feeling of luxury brand engravings.

## Layout & Spacing

The layout follows a **Fixed Grid** model with an emphasis on "The Golden Gap"—large areas of intentional whitespace that guide the eye and reduce cognitive load. 

- **The Editorial Grid:** A 12-column grid is used, but content often occupies only the center 8 columns to create wide, luxurious margins.
- **Asymmetric Balance:** Photography should often break the grid or overlap containers slightly to feel like a custom-designed book.
- **Vertical Rhythm:** Generous section padding (120px+) ensures that different topics have room to "breathe," reinforcing the stress-free nature of the brand.

## Elevation & Depth

This design system uses **Ambient Shadows** and **Tonal Layering** to create a sense of architectural depth. 

- **Shadows:** Instead of harsh black shadows, use very soft, diffused shadows with a slight Navy tint (`rgba(12, 27, 51, 0.05)`). This makes components feel like they are resting lightly on a surface rather than floating in space.
- **Marble Surfaces:** Backgrounds of cards or sections can use subtle marble grain textures. These should be high-resolution and low-contrast to ensure they do not interfere with text legibility.
- **Glass Overlays:** Semi-transparent Navy or White panels with a backdrop-blur (10px-20px) are used for navigation bars to maintain a sense of context and continuity.

## Shapes

The shape language is **Architectural and Soft**. 

Edges are not sharp, as that can feel aggressive, but they are not overly rounded, which can feel juvenile. The `0.25rem` (Soft) base roundedness provides a subtle human touch to otherwise geometric forms. Large containers and imagery should use a slightly larger radius (`0.75rem`) to feel like framed art. Buttons are rectangular with a very slight corner soften to maintain a professional, high-end hotel stationery feel.

## Components

Components in this design system are characterized by restraint and fine detail.

- **Buttons:** Primary buttons are Solid Navy with White text or Solid Gold with Navy text. They use a subtle 1px inset border to give them a "pressed" quality. Secondary buttons use a simple Gold bottom-border (2px) and no background.
- **Input Fields:** Use a "Minimalist Tray" style—only a bottom border (1px) in Navy or Gold, with floating labels in Inter (label-caps).
- **Cards:** Cards should be borderless, using a very light Parchment (`#F4F1ED`) background or a subtle Marble texture. They should have generous internal padding (40px).
- **Photography Containers:** Images should always have a slight "fade-in" transition and use subtle zoom-on-hover effects to enhance the premium interactive feel.
- **Booking Bar:** A persistent, elegant horizontal bar at the bottom or top of the screen that utilizes the Gold accent for the primary "Reserve" action.
- **Date Pickers:** Should feel like a personal desk calendar, using Noto Serif for dates and high-contrast Navy for selections.