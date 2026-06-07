---
name: Fresh & Functional
colors:
  surface: '#f7f9ff'
  surface-dim: '#d7dae0'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4fa'
  surface-container: '#ebeef4'
  surface-container-high: '#e5e8ee'
  surface-container-highest: '#dfe3e8'
  on-surface: '#181c20'
  on-surface-variant: '#3f4940'
  inverse-surface: '#2d3135'
  inverse-on-surface: '#eef1f7'
  outline: '#6f7a6f'
  outline-variant: '#becabd'
  surface-tint: '#006d36'
  primary: '#006a34'
  on-primary: '#ffffff'
  primary-container: '#268549'
  on-primary-container: '#f6fff3'
  inverse-primary: '#7eda95'
  secondary: '#5d5e61'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e5'
  on-secondary-container: '#636467'
  tertiary: '#595d5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#717574'
  on-tertiary-container: '#fafdfb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9af7af'
  primary-fixed-dim: '#7eda95'
  on-primary-fixed: '#00210c'
  on-primary-fixed-variant: '#005227'
  secondary-fixed: '#e2e2e5'
  secondary-fixed-dim: '#c6c6c9'
  on-secondary-fixed: '#1a1c1e'
  on-secondary-fixed-variant: '#454749'
  tertiary-fixed: '#e0e3e1'
  tertiary-fixed-dim: '#c4c7c5'
  on-tertiary-fixed: '#181c1b'
  on-tertiary-fixed-variant: '#434846'
  background: '#f7f9ff'
  on-background: '#181c20'
  surface-variant: '#dfe3e8'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
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
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
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
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is anchored in the concept of "Logistical Empathy." It balances the cold efficiency required for food rescue logistics with the warm, human-centric nature of community service. The aesthetic leans into **Corporate Modernism** with a **Minimalist** filter—prioritizing information density and clarity above all else. 

Visuals are characterized by high-contrast layouts, generous whitespace to signify "freshness," and a complete absence of decorative clutter. The emotional response should be one of immediate trust and operational readiness; users should feel that the platform is a reliable tool for solving a time-sensitive problem.

## Colors

The palette is restricted to ensure high accessibility and visual focus. **Leaf Green** serves as the primary action color, symbolizing growth and sustainability while maintaining a professional depth that avoids "neon" territory. **Charcoal** provides the structural grounding, used for all primary text and heavy UI accents to ensure AAA contrast ratios. 

**White** is the essential background canvas, used to emphasize cleanliness and food safety. A soft **Tertiary Sage-Grey** is utilized for subtle containment and background layering, preventing the interface from feeling clinical or sterile.

## Typography

This design system utilizes **Plus Jakarta Sans** for its exceptional balance of modern geometry and approachable warmth. It is a highly legible typeface that maintains its character across various screen densities. 

Hierarchy is established through weight and scale rather than color. Headlines are bold and tight to convey urgency and importance, while body text uses a generous line height to ensure readability for volunteers in high-speed environments. Labels use a slightly heavier weight and occasional uppercase styling to differentiate data points from prose.

## Layout & Spacing

The design system employs a **Fixed-Fluid Hybrid Grid** based on an 8px square rhythm. For desktop, a 12-column grid with a max-width of 1280px is preferred, while mobile layouts use a 4-column fluid system. 

Layouts are intentionally sparse, using white space as a functional separator rather than lines where possible. Information is grouped into "Logical Containers" that utilize standard 24px internal padding. Vertical rhythm is strictly enforced to maintain a sense of professional order.

## Elevation & Depth

To maintain the "Fresh & Functional" aesthetic, this design system avoids heavy drop shadows and faux-3D effects. Depth is communicated via **Tonal Layers** and **Low-contrast Outlines**.

1.  **Level 0 (Base):** Pure White (#FFFFFF) for the main background.
2.  **Level 1 (Containers):** Tertiary Gray (#F4F7F5) or White with a 1px solid border (#E0E4E1).
3.  **Level 2 (Interaction):** Subtle 12% opacity Charcoal shadows are reserved exclusively for floating elements like Modals or Popovers to denote temporary presence.

Hierarchy is primarily achieved through thickness and contrast of borders rather than "height" in a 3D space.

## Shapes

The shape language is "Softly Geometric." A standard radius of **0.5rem (8px)** is used for buttons, input fields, and cards. This provides enough softness to feel "community-oriented" while remaining sharp enough to look "professional." 

Smaller elements like tags or badges may use a full pill-shape (circular ends) to contrast against the more rigid structural containers. Large-scale imagery should follow the container radius to maintain a cohesive visual unit.

## Components

### Buttons
Primary buttons use solid Leaf Green with White text. Secondary buttons use a 2px Charcoal border with Charcoal text. All buttons have a minimum height of 48px to ensure touch-accessibility for volunteers in the field.

### Input Fields
Inputs are defined by a 1px Charcoal border (30% opacity) that strengthens to 100% on focus. Labels are always persistent above the field to ensure clarity during data entry.

### Chips & Tags
Used for "Food Type" or "Urgency Level." These use low-saturation background tints of the primary color to avoid distracting from the main call-to-action.

### Cards
Cards are the primary vehicle for food listings. They feature a 1px border, no shadow, and clear typographic hierarchy. Action buttons within cards are always right-aligned or full-width.

### High-Utility Icons
Iconography must be stroke-based, 2px weight, and Charcoal. Icons are never merely decorative; they must always represent a functional action or a critical data category (e.g., Temperature, Weight, Time).