---
name: Serene-Biological
colors:
  surface: '#f5fde2'
  surface-dim: '#d5ddc3'
  surface-bright: '#f5fde2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff7dc'
  surface-container: '#e9f1d7'
  surface-container-high: '#e4ebd1'
  surface-container-highest: '#dee6cb'
  on-surface: '#171e0e'
  on-surface-variant: '#46483c'
  inverse-surface: '#2c3321'
  inverse-on-surface: '#ecf4d9'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#56642b'
  primary: '#56642b'
  on-primary: '#ffffff'
  primary-container: '#8a9a5b'
  on-primary-container: '#253000'
  inverse-primary: '#bdce89'
  secondary: '#5c5d6e'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1f5'
  on-secondary-container: '#626374'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#929393'
  on-tertiary-container: '#2a2c2d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9eaa3'
  primary-fixed-dim: '#bdce89'
  on-primary-fixed: '#161f00'
  on-primary-fixed-variant: '#3e4c16'
  secondary-fixed: '#e1e1f5'
  secondary-fixed-dim: '#c5c5d8'
  on-secondary-fixed: '#191b29'
  on-secondary-fixed-variant: '#444655'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f5fde2'
  on-background: '#171e0e'
  surface-variant: '#dee6cb'
typography:
  display-lg:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.03em
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
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
  container-max: 1200px
  gutter: 2rem
  margin-page: 3rem
  stack-sm: 1rem
  stack-md: 2.5rem
  stack-lg: 5rem
---

## Brand & Style

The design system is centered on the concept of **Cognitive Restoration**. It aims to lower the cortisol levels of learners by mimicking the soft, predictable patterns found in nature. The brand personality is compassionate, scholarly, and restorative—moving away from the frantic, high-pressure aesthetic of traditional "hustle-culture" ed-tech.

The visual style utilizes a refined **Neumorphism (Soft UI)** approach. Rather than the harsh transitions of flat design, this system treats the screen as a tactile, biological surface where elements emerge from and recede into the background. Every interaction is designed to feel soft to the touch, utilizing "breathing" transitions to pace the user's focus. 

The system serves a dual-purpose audience: students seeking deep focus and educators looking for a sustainable, low-stress delivery platform.

## Colors

The palette is derived from the botanical world. **Sage Green (#8A9A5B)** serves as the primary anchor, chosen for its association with growth and cognitive clarity. **Lavender (#E6E6FA)** is used as a secondary "serenity" color to highlight interactive moments and progress indicators. 

For the high-contrast dark mode, the system pivots to a deep, mossy charcoal background with lavender-tinted text. This ensures maximum legibility and eye comfort during late-night study sessions while maintaining the biological theme. Shadows in dark mode are handled with "negative glow" rather than pure black, maintaining the soft UI depth.

## Typography

This design system uses **Lexend** exclusively. Originally designed to reduce visual stress and improve reading speed, Lexend aligns perfectly with the cognitive-optimization goals of the platform.

The type hierarchy is characterized by **generous letter spacing** and increased line heights. This "airy" typesetting prevents cognitive overload by making word shapes distinct and easy to parse. Body text should always prioritize readability over density; never crowd the page. Headlines are set with a slightly heavier weight but remain approachable and rounded.

## Layout & Spacing

The layout philosophy follows a **Fluid Organic Grid**. Content is housed within wide margins to minimize eye travel and peripheral distraction. Instead of a rigid column structure, the design system utilizes "islands" of content that float with significant negative space between them.

Spacing units are large and intentional. The "stack-lg" unit is frequently used to separate distinct learning modules, ensuring the user is never presented with too much information at once. The focus is on a single, clear path down the page, mimicking a natural trail.

## Elevation & Depth

Depth in this design system is achieved through **Soft UI Neumorphism**. Surfaces are not "placed on top" of the background; they are part of the background itself, pushed out (convex) or pressed in (concave).

1.  **Convex Surfaces (Buttons, Cards):** Created using two shadows. A light shadow (pure white at 80% opacity) on the top-left and a dark shadow (Sage-tinted grey at 20% opacity) on the bottom-right.
2.  **Concave Surfaces (Input fields, Progress tracks):** Created by reversing the shadow direction (Inner Shadows). This gives the impression of a carved, biological vessel.
3.  **The "Breathing" Pulse:** Active elements should feature a subtle scale and shadow-blur animation (duration: 3000ms, ease-in-out) that mimics a slow respiratory rhythm.

## Shapes

The shape language is strictly **organic and non-aggressive**. Sharp 90-degree corners are forbidden as they trigger "edge-avoidance" responses in the brain. 

Standard components use a `0.5rem` radius, while large containers and buttons use `1.5rem` (rounded-xl) to feel like smoothed river stones. Where possible, use slightly asymmetrical border-radii (e.g., 24px 28px 22px 30px) for high-level decorative elements to enhance the "biological" feel, suggesting growth rather than industrial manufacturing.

## Components

### Buttons
Primary buttons are convex Sage Green shapes with white text. They do not have borders. On hover, the "breathing" pulse animation increases in intensity slightly, and the shadow depth softens, simulating the button being "pressed" into the surface.

### Cards & Modules
Learning modules are housed in large, soft-white convex cards with `rounded-xl` corners. Padding inside cards is extremely generous (minimum 40px) to maintain the serene atmosphere.

### Input Fields
Search bars and text inputs are concave (inset). They should feel like a soft physical indentation in the UI. When focused, the inner shadow color shifts from neutral to a soft Lavender glow.

### Progress Indicators
Progress is shown using a "Vine" pattern—a thick, Sage Green line that grows organically. The leading edge of the progress bar features a soft pulse to indicate the "living" nature of the user's journey.

### Chips & Tags
Chips are pill-shaped and use a Lavender background with a low-opacity border. They function as "petals" of information, easily scannable and soft to the eye.

### Interactive "Breathing" Element
Every interactive state transition must last at least 200ms with an `ease-in-out` curve. Avoid "snapping" transitions; every UI change should feel like a natural movement.