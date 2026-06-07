---
name: Shadow-Master
colors:
  surface: '#fbf9fa'
  surface-dim: '#dbd9da'
  surface-bright: '#fbf9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f4'
  surface-container: '#efedee'
  surface-container-high: '#eae7e9'
  surface-container-highest: '#e4e2e3'
  on-surface: '#1b1c1d'
  on-surface-variant: '#43474c'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f1'
  outline: '#74777c'
  outline-variant: '#c4c7cc'
  surface-tint: '#50606f'
  primary: '#4e5e6d'
  on-primary: '#ffffff'
  primary-container: '#667686'
  on-primary-container: '#fdfcff'
  inverse-primary: '#b8c8da'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#705740'
  on-tertiary: '#ffffff'
  tertiary-container: '#8b6f57'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e4f6'
  primary-fixed-dim: '#b8c8da'
  on-primary-fixed: '#0d1d2a'
  on-primary-fixed-variant: '#394857'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdcbf'
  tertiary-fixed-dim: '#e2c0a4'
  on-tertiary-fixed: '#291806'
  on-tertiary-fixed-variant: '#59422d'
  background: '#fbf9fa'
  on-background: '#1b1c1d'
  surface-variant: '#e4e2e3'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  control-val:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '300'
    lineHeight: '1'
    letterSpacing: '0'
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
  container-max: 1200px
  gutter: 24px
---

## Brand & Style
The design system is engineered to evoke a sense of quiet luxury, precision, and effortless control. Targeting high-end homeowners and interior designers, the UI prioritizes a tactile, calm atmosphere that mirrors the physical experience of premium automated window treatments.

The style is **Neumorphic / Soft-UI**, utilizing subtle highlights and shadows to create "extruded" surfaces that look integrated into the background. This approach moves away from flat digital abstractions toward a more physical, sensory interface. The aesthetic is clean and minimalist, avoiding unnecessary visual noise to focus the user’s attention on light filtration and privacy settings.

## Colors
This design system utilizes a monochromatic base with varied tonal depths to achieve the neumorphic effect. The core background is not pure white, but a soft, cool grey (#E0E5EC) which allows white highlights and slate shadows to remain visible.

- **Primary (Slate Grey):** Used for critical iconography, active states, and primary typography. It provides the necessary contrast against the soft UI.
- **Secondary (Silver):** Applied to decorative elements and inactive slider tracks.
- **Surface Palette:** Neumorphism relies on the interaction between "Light" (#FFFFFF) and "Shadow" (#A3B1C6) to create depth. Every interactive element must utilize these two tones to appear raised from or recessed into the background.

## Typography
The design system employs **Inter** for its utilitarian precision and exceptional readability at various scales. To maintain a premium feel, typography is used sparingly. 

Headlines use a medium weight with tighter tracking to feel structural. Body copy is set with generous line heights to promote breathability. Labels for controls and settings are set in a slightly smaller, bold, all-caps format to differentiate them from interactive data points like "Percentage Open" or "Time Remaining," which utilize a light weight and larger scale for a sophisticated, modern look.

## Layout & Spacing
The layout follows a **fluid grid** model with significant negative space to emphasize the minimalist aesthetic. A 12-column system is used for desktop views, while mobile transitions to a single-column stack with generous side margins (24px).

Spacing rhythm is based on an 8px baseline. Neumorphic elements require more "breathing room" than flat elements because their shadows occupy visual space; therefore, the "md" (24px) unit is the default padding for cards and containers to prevent the UI from feeling cramped.

## Elevation & Depth
Depth is the primary communicator of hierarchy in this design system. Instead of using Z-index layers and overlays, we use surface deformation:

- **Raised (Extruded):** Standard buttons, cards, and toggles use two shadows: a light shadow (top-left) at #FFFFFF and a dark shadow (bottom-right) at #A3B1C6. This suggests the element is coming toward the user.
- **Sunken (Inverted):** Active states, input fields, and slider tracks use inner shadows to appear as if they are pressed into the surface.
- **Softness:** Shadow blurs should be generous (typically 12px to 20px) to maintain the "Soft-UI" look. Harsh, small-radius shadows are prohibited as they break the premium, organic feel.

## Shapes
The shape language is defined by "Softened Geometry." We use a **Rounded** (Level 2) approach to ensure that the light and shadow effects wrap naturally around corners, mimicking high-quality injection-molded plastic or brushed metal.

- **Standard Elements:** 0.5rem (8px) radius.
- **Large Containers/Cards:** 1rem (16px) radius.
- **Pill Elements:** Used specifically for sliders and toggle switches to emphasize their tactile, movable nature.

## Components
- **Buttons:** Primary buttons appear extruded. On "tap" or "click," they transition to a sunken state with inner shadows to provide haptic-like visual feedback.
- **Sliders:** These are the hero components. The track is sunken (inverted), and the handle is a highly-rounded extruded disc. As the handle moves, the "active" portion of the track fills with Slate Grey.
- **Toggles:** Use a pill-shaped sunken track. The "switch" is a circular extruded element that slides horizontally.
- **Cards:** Cards should have the same background color as the page, defined only by their soft external shadows. No borders are used.
- **Input Fields:** Always displayed as sunken (inner shadow) wells. Text is Slate Grey, and the cursor/focus state uses a subtle Silver glow.
- **Visual Feedback:** Use "Glow" effects (Slate Grey with a soft outer blur) instead of sharp outlines for focus states to maintain the soft aesthetic.
- **Glass Overlays:** For rare modal moments (e.g., "Advanced Schedule"), use a high-blur backdrop filter with 70% opacity white to maintain a sense of space without breaking the soft-UI logic.