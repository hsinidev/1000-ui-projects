---
name: Zenith Focus
colors:
  surface: '#fbf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#fbf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f0'
  surface-container: '#efeeea'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e4e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#434841'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ed'
  outline: '#747871'
  outline-variant: '#c4c8bf'
  surface-tint: '#51634e'
  primary: '#51634e'
  on-primary: '#ffffff'
  primary-container: '#8da189'
  on-primary-container: '#263725'
  inverse-primary: '#b8ccb3'
  secondary: '#576156'
  on-secondary: '#ffffff'
  secondary-container: '#d9e3d4'
  on-secondary-container: '#5c655a'
  tertiary: '#75565f'
  on-tertiary: '#ffffff'
  tertiary-container: '#b7929c'
  on-tertiary-container: '#462c34'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8ce'
  primary-fixed-dim: '#b8ccb3'
  on-primary-fixed: '#0f1f0f'
  on-primary-fixed-variant: '#394b38'
  secondary-fixed: '#dbe5d7'
  secondary-fixed-dim: '#bfc9bb'
  on-secondary-fixed: '#151e15'
  on-secondary-fixed-variant: '#40493f'
  tertiary-fixed: '#ffd9e2'
  tertiary-fixed-dim: '#e4bcc7'
  on-tertiary-fixed: '#2c141c'
  on-tertiary-fixed-variant: '#5c3f47'
  background: '#fbf9f6'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2df'
typography:
  display:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
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
  container-padding-mobile: 24px
  container-padding-desktop: 64px
  gutter: 16px
  section-gap: 48px
  element-gap: 12px
---

## Brand & Style

The design system is anchored in the concept of "Cognitive Ease." It targets solo founders who are often overwhelmed by complex, high-density project management tools. The brand personality is calm, intentional, and premium, acting more as a digital sanctuary than a traditional utility.

By blending **Minimalism** with **Soft-UI (Neomorphism)**, this design system creates a tactile, approachable interface that feels physical yet digital. The "Zen Mode" capability is the core differentiator, stripping away all non-essential depth and color to leave only high-contrast text and essential actionable elements. The visual narrative prioritizes the "Single Task" philosophy, using expansive whitespace to isolate elements and reduce decision fatigue.

## Colors

The palette is organic and low-strain. 
- **Soft Sage (Primary):** Used for primary actions, active states, and progress indicators. It is muted to prevent visual vibration.
- **Cream (Background):** A warm, off-white surface that reduces the harshness of pure white backgrounds, essential for long-form productivity.
- **Charcoal (Text):** A deep, soft black used for high-contrast readability without the "piercing" effect of #000.
- **Accent/Surface:** Lighter tints of cream are used to create the "raised" highlights in the Neumorphic shadows.

In **Zen Mode**, the background shifts to a flatter, higher-contrast Cream/White and Sage accents are used sparingly only for the most critical calls to action.

## Typography

This design system utilizes **Manrope** for its modern, geometric, and highly legible characteristics. It strikes a balance between professional SaaS aesthetics and approachable warmth. 

Typography is used as a structural element. Large "Display" and "Headline" sizes are used to create clear hierarchy in the absence of heavy borders or loud background colors. Body text uses a generous 1.6 line height to ensure maximum legibility for project descriptions and task notes. Label styles are set in uppercase with slight letter spacing to differentiate them from interactive body text.

## Layout & Spacing

The layout philosophy follows a **Mobile-First** approach, ensuring that solo founders can manage tasks on the go. It utilizes a fluid grid with safe areas that expand into a centered, fixed-width column on desktop (max-width 900px) to maintain focus and prevent eye-strain across wide monitors.

Whitespace is treated as a first-class citizen. Padding within cards and buttons is intentionally oversized to provide a luxurious, airy feel. Elements are grouped using generous "Section Gaps" (48px+) to visually separate different project phases or daily priorities without needing aggressive separators.

## Elevation & Depth

Visual hierarchy is achieved through **Neumorphism (Soft-UI)**. Surfaces appear to be pushed out from or indented into the Cream background.

1.  **Raised Elements (Cards, Primary Buttons):** Created using dual shadows. A light-colored shadow (White, #FFFFFF) on the top-left and a soft dark shadow (Charcoal tint, 10% opacity) on the bottom-right.
2.  **Inset Elements (Input Fields, Active States):** Shadows are reversed and placed inside the element to create a "pressed" look, indicating a state of data entry or engagement.
3.  **Zen Mode Depth:** When Zen Mode is active, all dual-shadow elevation is removed. Depth is replaced by subtle 1px outlines in Soft Sage or Charcoal to ensure the interface remains high-contrast and distraction-free.

## Shapes

The shape language is "Soft-Organic." All interactive elements use a base roundedness of **0.5rem (8px)**, while larger card containers utilize **1rem (16px)** to emphasize the pillowy, tactile nature of the Neumorphic style. 

Avoid sharp 90-degree angles entirely, as they conflict with the "Zen" and "Soft-UI" narrative. The roundedness should be consistent across buttons, input fields, and progress bars to create a unified visual rhythm.

## Components

### Buttons
Primary buttons are "raised" Soft-UI elements with Soft Sage text. On hover, the elevation increases slightly. On click/active state, the button transitions to an "inset" shadow to mimic a physical press.

### Cards
Cards are the primary container for tasks and projects. They should have no visible border, relying entirely on the dual-shadow Neumorphic effect for definition. Internal padding must be at least 24px.

### Input Fields
Inputs use the "inset" shadow style by default. This makes the field look like a cavity ready to be filled, contrasting with the "raised" buttons.

### Chips & Tags
Chips are used for category labels. They should be flat with a 1px Soft Sage border or a very light Sage background tint to avoid competing with the primary elevated cards.

### Zen Toggle
A unique, prominent component at the top of the interface. When toggled, it triggers a global CSS transition that flattens shadows and simplifies the UI to a high-contrast, text-heavy mode.

### Progress Bars
Progress bars should be inset (concave) with the "fill" being a flat, Soft Sage color, creating a clear visual distinction between the container and the progress.