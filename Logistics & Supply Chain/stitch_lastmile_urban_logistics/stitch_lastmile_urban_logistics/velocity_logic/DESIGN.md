---
name: Velocity Logic
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#5b4138'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#8f7066'
  outline-variant: '#e3bfb3'
  surface-tint: '#ab3600'
  primary: '#ab3600'
  on-primary: '#ffffff'
  primary-container: '#ff5f1f'
  on-primary-container: '#561700'
  inverse-primary: '#ffb59c'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#515f74'
  on-tertiary: '#ffffff'
  tertiary-container: '#8795ac'
  on-tertiary-container: '#1f2e41'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59c'
  on-primary-fixed: '#390c00'
  on-primary-fixed-variant: '#832700'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d5e3fd'
  tertiary-fixed-dim: '#b9c7e0'
  on-tertiary-fixed: '#0d1c2f'
  on-tertiary-fixed-variant: '#3a485c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 20px
  touch-target: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The brand personality of this design system is defined by speed, precision, and relentless energy. It targets a fast-moving logistics environment where every second counts and information must be absorbed at a glance. The UI evokes a sense of "technological urgency"—it is reliable and engineered, yet feels hyper-responsive. 

The aesthetic style is **High-Contrast / Bold** fused with **Technical Minimalism**. It avoids decorative flourishes in favor of structural clarity and aggressive visual hierarchy. This approach ensures that the interface remains functional under harsh outdoor lighting conditions, providing the driver or operator with immediate, unambiguous data.

## Colors

The palette is engineered for maximum visibility. **Electric Orange** serves as the primary action color, cutting through visual noise to highlight critical path tasks and status updates. **Slate** (Secondary and Tertiary) provides the structural weight, used for deep-contrast text and grounding UI containers to prevent eye fatigue.

**White** and **Off-White** are utilized for the base layers to ensure the highest possible contrast ratio against the slate typography. In outdoor environments, this light-mode-first approach minimizes glare and maximizes the legibility of technical data points.

## Typography

Typography in this design system is a functional tool for data density. **Space Grotesk** is used for headlines and technical labels; its geometric and slightly idiosyncratic character reinforces the high-tech, futuristic aesthetic. **Inter** is utilized for body copy and logistical details to ensure neutral, systematic readability at smaller scales.

To emphasize urgency and importance, a heavy reliance on bold weights and tight letter-spacing is applied to headlines. Uppercase styling is reserved for labels and status indicators to create a "heads-up display" (HUD) feel.

## Layout & Spacing

This design system employs a **Fluid Grid** model optimized for handheld devices. The layout relies on a strict 8px rhythmic scale, ensuring that all elements align to a predictable vertical and horizontal cadence. 

Given the "last-mile" context, spacing is generous around interactive elements to accommodate "fat-finger" interactions during high-stress movement. Every primary action maintains a minimum 48px touch target. Content blocks use a 12-column mobile grid with 16px gutters to maintain a compact but breathable information density.

## Elevation & Depth

To maintain a modern, high-tech aesthetic, this design system rejects soft, ambient shadows in favor of **Tonal Layers** and **Bold Borders**. Depth is communicated through stackable surface tiers using slight shifts in neutral values (e.g., Slate 50 to Slate 100).

Elements that require immediate attention use a 2px solid Slate border rather than a shadow. This "Flat-Plus" approach ensures that hierarchy is maintained even when screen brightness is maxed out or under direct sunlight, where subtle shadows would typically wash out and disappear.

## Shapes

The shape language is **Soft (0.25rem)**, leaning towards a sharp, engineered feel. This slight rounding prevents the UI from feeling "aggressive" while maintaining the precision of a professional tool. Large components like cards use a 0.5rem radius, while buttons and input fields stay at the base 0.25rem for a tighter, more utilitarian appearance. High-tech accents, such as clipped corners or 45-degree angles on status badges, may be used sparingly to reinforce the delivery-mechanic aesthetic.

## Components

### Buttons
Primary buttons are solid **Electric Orange** with white bold Space Grotesk text. They use a "high-energy" hover state where the border thickness increases. Secondary buttons use a heavy Slate stroke with no fill.

### Cards
Cards are flat with a 1px Slate border. They do not use shadows. Headers within cards are separated by a subtle 1px horizontal rule to maintain high-density data organization.

### Status Indicators
Status chips use high-contrast fills: "In Transit" (Primary Orange), "Delivered" (Slate), and "Delayed" (High-visibility Yellow). These use the `label-bold` typography for instant recognition.

### Inputs
Input fields feature a 2px Slate border that turns Electric Orange on focus. Labels are always visible above the field in `label-sm` to ensure the user never loses context while typing.

### Progress Trackers
Linear, high-contrast bars. Completed segments are Electric Orange; remaining segments are a light Slate grey. The "current" segment should pulse slightly to indicate active movement.