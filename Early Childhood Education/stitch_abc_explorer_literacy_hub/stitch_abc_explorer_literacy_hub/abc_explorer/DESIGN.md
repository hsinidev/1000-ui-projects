---
name: ABC-Explorer
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
  on-surface-variant: '#5d3f3b'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#926f6a'
  outline-variant: '#e7bdb7'
  surface-tint: '#c0000a'
  primary: '#bc000a'
  on-primary: '#ffffff'
  primary-container: '#e2241f'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb4aa'
  secondary: '#0058bc'
  on-secondary: '#ffffff'
  secondary-container: '#0070eb'
  on-secondary-container: '#fefcff'
  tertiary: '#745b00'
  on-tertiary: '#ffffff'
  tertiary-container: '#d0a600'
  on-tertiary-container: '#4f3d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#930005'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a41'
  on-secondary-fixed-variant: '#004493'
  tertiary-fixed: '#ffe08b'
  tertiary-fixed-dim: '#f1c100'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#584400'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: lexend
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
  headline-lg:
    fontFamily: lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: lexend
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: lexend
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: lexend
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.02em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  margin-mobile: 24px
  gutter: 16px
  touch-target-min: 48px
  card-padding: 24px
---

## Brand & Style

The design system is engineered for early learners, focusing on a high-energy, encouraging, and tactile environment. The brand personality is "The Patient Playmate"—energetic and vibrant, yet organized and dependable. It targets children aged 3–7, requiring a UI that minimizes cognitive load while maximizing joy and discovery.

The design style is **Tactile / High-Contrast**. It utilizes "squishy" physical metaphors for buttons to encourage interaction, combined with a bold color palette that aids in visual hierarchy and accessibility for developing motor skills. For the parents' dashboard, the style shifts toward a **Corporate / Modern** refinement of the same DNA—maintaining the color palette but increasing whitespace and reducing decorative elements to facilitate quick data scanning.

## Colors

The palette is rooted in the three primary colors of early childhood education. **Bold Red** serves as the action color for primary tasks and highlights; **Bright Blue** is used for navigation and steady-state elements; **Sunny Yellow** acts as a reward and secondary accent color.

The neutral background is a pure, clean White to ensure maximum contrast for text and illustrations. Feedback states use a vibrant Green for "correct" interactions to provide instant positive reinforcement. The parents' dashboard utilizes the same colors but leans more heavily on the Blue and White to create a calmer, more administrative atmosphere.

## Typography

This design system uses **Lexend** exclusively. Chosen for its specific design intent to reduce visual stress and improve reading proficiency, its hyper-legible, rounded letterforms perfectly match the "playful yet educational" requirement.

Headlines for children should always be at the `display-xl` or `headline-lg` level to ensure readability on mobile devices held at arm's length. Tracking is kept at default for body text to maintain the font's rhythmic integrity, while labels are slightly tracked out for clarity in the parent-facing interface.

## Layout & Spacing

The layout follows a **Fluid Grid** model with generous safe areas. For the child-facing side, a simplified 4-column grid is used to prevent layout density. On the parents' dashboard, a standard 12-column grid is implemented for complex data tables and progress charts.

The spacing rhythm is based on an 8px base unit. Interaction targets must never fall below 48px to accommodate the less precise motor skills of young children. Use wide gutters (16px+) to ensure that tappable elements are distinct and to prevent accidental "fat-finger" errors.

## Elevation & Depth

This design system utilizes **Tactile Depth** to communicate interactivity. Surfaces do not use traditional ambient shadows; instead, they use "block shadows"—solid, darker-tinted offsets that give buttons a 3D, physical appearance.

When a button is pressed, it should "depress" by moving 2–4px downward and losing its shadow, simulating a physical toy. Elements meant to be non-interactive (like information cards) should use low-contrast outlines or very soft, diffused shadows to stay visually "flat" against the background, keeping the focus on the interactive components.

## Shapes

The shape language is **Pill-shaped**. There are no sharp corners in this design system, reflecting a "child-safe" environment. All buttons, containers, and cards use large radii. Small elements use a minimum radius of 1rem, while larger cards and primary containers use 2rem to 3rem. Illustrations should follow this logic, utilizing rounded strokes and soft terminals.

## Components

### Buttons
Primary buttons are large, pill-shaped, and use the "block shadow" technique. They must contain both a text label and a clear icon (e.g., a "Play" triangle) to assist non-readers. 

### Chips & Badges
Used for progress markers and rewards. These should be vibrant (Yellow or Red) and use a bouncy animation when they appear on screen.

### Lists & Progress Cards
In the parents' dashboard, cards should be white with a subtle 1px border. In the child's view, cards should be brightly colored with large, chunky illustrations.

### Input Fields
Inputs for parents are clean and standard. For children, inputs (like letter-tracing boxes) should be oversized with dashed stroke guides and high-contrast touch feedback.

### Feedback States
- **Success:** Element pulses and turns Green with a star icon.
- **Error:** Element shakes horizontally and turns Red with a gentle "oops" visual cue.
- **Active:** Buttons shift down 4px to simulate being pressed.