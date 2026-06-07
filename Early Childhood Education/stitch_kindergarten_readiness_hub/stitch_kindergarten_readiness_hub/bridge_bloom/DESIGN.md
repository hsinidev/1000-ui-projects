---
name: Bridge & Bloom
colors:
  surface: '#f8f9ff'
  surface-dim: '#ccdbf3'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d5e3fc'
  on-surface: '#0d1c2e'
  on-surface-variant: '#3d4947'
  inverse-surface: '#233144'
  inverse-on-surface: '#eaf1ff'
  outline: '#6d7a77'
  outline-variant: '#bcc9c6'
  surface-tint: '#006a61'
  primary: '#00685f'
  on-primary: '#ffffff'
  primary-container: '#008378'
  on-primary-container: '#f4fffc'
  inverse-primary: '#6bd8cb'
  secondary: '#855300'
  on-secondary: '#ffffff'
  secondary-container: '#fea619'
  on-secondary-container: '#684000'
  tertiary: '#924628'
  on-tertiary: '#ffffff'
  tertiary-container: '#b05e3d'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#89f5e7'
  primary-fixed-dim: '#6bd8cb'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#ffddb8'
  secondary-fixed-dim: '#ffb95f'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#653e00'
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#ffb59a'
  on-tertiary-fixed: '#370e00'
  on-tertiary-fixed-variant: '#773215'
  background: '#f8f9ff'
  on-background: '#0d1c2e'
  surface-variant: '#d5e3fc'
typography:
  h1:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Lexend
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  button:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.0'
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
  lg: 40px
  xl: 64px
  gutter: 16px
  margin: 20px
---

## Brand & Style
This design system centers on the "Organized & Encouraging" aesthetic, bridging the gap between the structured environment of a classroom and the warmth of a home. The style leverages a **Modern Corporate** foundation—ensuring parents feel the app is a reliable educational tool—blended with **Soft Tactile** elements to keep the experience engaging and non-intimidating for young children. 

The visual language emphasizes clarity and steady progress. High-density layouts are avoided in favor of generous whitespace, ensuring that both parents and children can navigate without cognitive overload. The emotional goal is to transform the potentially stressful transition to kindergarten into a series of achievable, celebrated milestones.

## Colors
The color palette is anchored by a calming, professional **Teal**, signifying growth and stability. **White** serves as the primary canvas, maintaining a clean and "organized" feel that highlights content. **Slate Grey** is utilized for text and subtle UI accents, providing high legibility without the harshness of pure black.

To support the "Encouraging" aspect of the design system, a warm **Amber/Gold** is introduced specifically for achievement markers and stars. This secondary accent color is reserved for moments of celebration to ensure it retains its psychological impact as a reward.

## Typography
This design system utilizes **Lexend**, a typeface specifically engineered to improve reading proficiency. Its expanded character spacing and friendly, sans-serif terminals make it exceptionally legible for both adults and early readers. 

Headlines use a semi-bold weight to provide clear structural signposts. Body text is set with generous line heights to enhance the "Organized" feel. For child-facing labels, font sizes should never drop below 16px to accommodate developing visual tracking skills.

## Layout & Spacing
The layout follows a **Fluid Grid** model designed for mobile and tablet surfaces. It uses an 8px base unit to maintain a consistent rhythmic scale. 

- **Margins:** A standard 20px outer margin ensures content doesn't feel cramped against the bezel.
- **Gutters:** 16px gutters provide distinct separation between cards and interactive elements.
- **Vertical Rhythm:** Sections are separated by "Large" (40px) or "Extra Large" (64px) spacing to create clear thematic breaks, reinforcing the "Organized" nature of the curriculum.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and soft, diffused shadows. Surfaces do not "float" aggressively; instead, they sit just above the background to feel tactile and reachable.

- **Level 0 (Background):** Pure White (#FFFFFF).
- **Level 1 (Cards/Containers):** Surface color (#F8FAFC) with a 1px Slate Grey stroke at 10% opacity.
- **Level 2 (Active/Interactive):** Subtle 12px blur shadow with 5% opacity Slate Grey, used for buttons and active progress steps.
- **Level 3 (Modals/Pop-overs):** 24px blur shadow with 10% opacity, creating focus without detaching from the friendly aesthetic.

## Shapes
To ensure the app feels "Approachable," the design system employs a **Rounded** (Level 2) shape language. 

- **Buttons & Inputs:** Use a 0.5rem (8px) radius. 
- **Cards & Progress Containers:** Use a 1rem (16px) radius to create a soft, protective frame for content.
- **Achievement Markers:** The "Star" marker uses rounded points rather than sharp geometric angles to maintain the friendly visual metaphor.

## Components

### Buttons
Primary buttons are solid Teal with White text. Secondary buttons use a Teal border with a White fill. All buttons feature a minimum height of 48px to ensure a "child-friendly" hit target.

### Progress Steppers
The progress stepper is a horizontal track of rounded circles. Completed steps are filled with Teal and contain a checkmark; the current step features a Teal border and a pulsing "focus" ring. Incomplete steps are Slate Grey at 20% opacity.

### Achievement 'Star' Markers
Stars are the primary reward component. They use the Amber/Gold secondary color and feature a slight "inner glow" or subtle gradient to appear more physical and rewarding. When earned, stars should trigger a scale-up animation.

### Cards
Cards are the primary organizational unit. They must have a 1px Slate Grey border (low opacity) and a 16px corner radius. Content within cards should follow the standard 8px spacing rhythm.

### Input Fields
Inputs use a thick 2px border in Slate Grey (20% opacity), which turns Teal when focused. Labels are always persistent (not floating) to help users with shorter attention spans maintain context.