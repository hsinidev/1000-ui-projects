---
name: ActiveSilver
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#434657'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#747688'
  outline-variant: '#c4c5da'
  surface-tint: '#0045fc'
  primary: '#0034c5'
  on-primary: '#ffffff'
  primary-container: '#0046ff'
  on-primary-container: '#d3d9ff'
  inverse-primary: '#b9c3ff'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8b00'
  on-secondary-container: '#603100'
  tertiary: '#484848'
  on-tertiary: '#ffffff'
  tertiary-container: '#606060'
  on-tertiary-container: '#dbdbdb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b9c3ff'
  on-primary-fixed: '#001257'
  on-primary-fixed-variant: '#0033c1'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  touch-target-min: 48px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 40px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is built to inspire vitality, confidence, and movement for a senior demographic. It rejects the clinical or "fragile" aesthetic often associated with aging, instead favoring an **Energetic & High-Contrast** style that feels modern and empowering. 

The emotional response should be one of motivation and clarity. By utilizing bold color blocking and tactile UI elements, this design system ensures that every interaction is intentional and accessible. The style combines a **High-Contrast Bold** framework with **Tactile** affordances, making interactive elements feel physically "clickable" and unmistakable, reducing cognitive load and physical friction.

## Colors

The palette is optimized for maximum legibility and visual energy. 

- **Primary (Electric Blue):** Used for primary actions and brand presence. It provides high contrast against white backgrounds.
- **Vibrant Accent (Orange):** Reserved for motivational triggers, progress indicators, and highlighting "Active" states.
- **Base (White):** The foundation for all screens to maintain a clean, airy, and clinical-free environment.
- **Neutral/Text:** Pure black or very dark navy is used for typography to ensure the highest possible contrast ratio (WCAG AAA compliance).

Avoid using Orange for small text elements; reserve it for large icons, badges, and primary highlights.

## Typography

This design system uses **Lexend** exclusively. Chosen for its specific design intent to reduce visual stress and improve reading speed, Lexend's expanded character width is ideal for senior users.

The type scale is intentionally oversized. The minimum body size is 18px to ensure readability without strain. High line-heights are maintained across all levels to prevent text crowding. Use bold weights for headlines to create a clear information hierarchy that guides the eye through the layout.

## Layout & Spacing

The layout follows a **fluid grid** model with generous margins to prevent accidental taps near screen edges. A strict 8px spacing system is used to maintain rhythm.

- **Touch Targets:** A non-negotiable minimum of 48x48px for all interactive elements.
- **Vertical Rhythm:** Use large stack spacing (48px+) between distinct content blocks to allow the eye to rest.
- **Scanning:** Information is presented in a single-column or simple two-column layout on larger screens to keep the focus path linear and simple.

## Elevation & Depth

To aid accessibility, this design system uses **Bold Borders** and **Tonal Layers** rather than soft, ambient shadows which can appear blurry to users with visual impairments.

1. **Interactive Elements:** Use a crisp, 2px border or a high-contrast offset shadow (hard edge) to make buttons "pop" from the background.
2. **Surface Hierarchy:** Use subtle grey backgrounds (#F4F4F4) to group related content, creating a clear "card" container without needing complex shadows.
3. **Active States:** When an item is selected, use a thick Electric Blue stroke (3px) to provide unmistakable feedback.

## Shapes

The shape language is **Rounded**, using a 0.5rem (8px) base radius. This strikes a balance between the friendliness of organic shapes and the structural integrity required for high-readability layouts.

- **Standard Elements:** 8px corner radius (e.g., input fields, smaller cards).
- **Large Containers:** 16px corner radius (e.g., feature cards, hero sections).
- **Interactive Pills:** Use full rounding (rounded-full) for chips and tags to differentiate them from primary rectangular buttons.

## Components

### Buttons
Primary buttons must be a minimum of 56px in height. They use the Electric Blue background with White bold text. Use an "inner-glow" or hard-offset shadow to give a tactile, pressable feel.

### Cards
Cards are the primary container for workouts and health data. They must feature a 2px border or a subtle tonal background to define boundaries. Imagery within cards should be high-resolution, featuring seniors in active, energetic poses with high color saturation.

### Input Fields
Inputs must have a minimum height of 56px and a 2px border. Labels must stay visible above the field at all times (no disappearing placeholders).

### Chips & Progress
Use the Orange accent for progress bars and "Active" status chips. These represent energy and completion, providing a warm contrast to the professional Electric Blue.

### Lists
List items should be separated by clear dividers or generous white space. Every list item that is clickable must include a chevron icon or a clear "Go" button to signify the interaction.