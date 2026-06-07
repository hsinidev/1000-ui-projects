---
name: Kinetic Luxury System
colors:
  surface: '#fcf9f6'
  surface-dim: '#dcdad7'
  surface-bright: '#fcf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f0'
  surface-container: '#f0edea'
  surface-container-high: '#eae8e5'
  surface-container-highest: '#e5e2df'
  on-surface: '#1c1c1a'
  on-surface-variant: '#58413e'
  inverse-surface: '#31302f'
  inverse-on-surface: '#f3f0ed'
  outline: '#8b716d'
  outline-variant: '#dfbfba'
  surface-tint: '#a83729'
  primary: '#390000'
  on-primary: '#ffffff'
  primary-container: '#600000'
  on-primary-container: '#ee6a57'
  inverse-primary: '#ffb4a8'
  secondary: '#7b580d'
  on-secondary: '#ffffff'
  secondary-container: '#fdcd79'
  on-secondary-container: '#785509'
  tertiary: '#151818'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a2c2c'
  on-tertiary-container: '#929393'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#871f15'
  secondary-fixed: '#ffdea8'
  secondary-fixed-dim: '#eebf6d'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5e4200'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f6'
  on-background: '#1c1c1a'
  surface-variant: '#e5e2df'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
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
    letterSpacing: 0.15em
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
  margin: 64px
---

## Brand & Style

This design system embodies "Architectural-Chic," a fusion of structural precision and organic softness. It is designed for a discerning, high-net-worth audience that values both heritage craftsmanship and cutting-edge technology. 

The aesthetic strategy utilizes **Neumorphism-lite**—a refined version of soft-UI that avoids the cluttered "plastic" look of early skeuomorphism in favor of subtle, tactile depth. The emotional response should be one of "Quiet Luxury": a sense of calm, exclusivity, and effortless sophistication. Surfaces should feel molded and physical, like fine-pressed leather or polished metal, while maintaining the airy, high-contrast clarity of a modern fashion editorial.

## Colors

The palette is anchored by **Deep Burgundy**, used sparingly for high-impact brand moments and primary actions. **Tan Leather** serves as the secondary structural color, providing warmth and a tactile connection to the product's physical materials. 

The primary surface is a crisp **White**, though the design system relies on a slightly off-white neutral (`#F8F5F2`) for background layers to allow the white "Soft-UI" elements to pop with light-source highlights. Accents are handled with high-contrast Tan/Gold to evoke hardware finishes. Interaction states should prioritize subtle shifts in shadow depth rather than aggressive color changes.

## Typography

This design system employs a classic high-contrast pairing. **Playfair Display** provides the editorial authority required for a luxury brand, used for large headlines and evocative quotes. Its serif terminals reflect the "Architectural" side of the brand.

**Inter** handles all functional UI elements, ensuring maximum legibility on small screens and digital interfaces. To maintain the premium feel, use the `label-caps` style for navigation and small headers—wide letter spacing is essential here to create an "airy" and modern look. Maintain generous vertical rhythm between serif headlines and sans-serif body text.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop (12-column, 1200px max-width) to ensure content remains centered and curated, like a gallery display. On mobile, the system transitions to a fluid model with generous 24px side margins.

"Airy" is the guiding principle. Avoid crowding elements; use `xl` spacing (80px) between major sections to allow the eye to rest. Internal component spacing should follow an 8px baseline, but external margins for "Soft-UI" cards must be larger than traditional flat designs to allow room for diffused shadows to breathe without overlapping adjacent elements.

## Elevation & Depth

Depth is achieved through **Neumorphism-lite**. Instead of heavy extrusion, use "Soft-UI" layers that appear to be molded from the background surface.

1.  **Raised Elements:** Use two shadows. A top-left highlight (White, 80% opacity, 12px blur) and a bottom-right shadow (Deep Tan or Burgundy-tinted Grey, 10% opacity, 16px blur).
2.  **Sunken Elements (Inputs/Active States):** Reverse the shadows to create an "inset" look, suggesting the element has been pressed into leather.
3.  **Tonal Tiers:** Use the Tan Leather color for thin (1px) architectural borders on primary cards to define edges where shadows are too subtle. 
4.  **Blur:** Use backdrop blurs (20px) only for top-level navigation overlays to maintain the "Glassmorphism" hint within a luxury context.

## Shapes

The shape language is "Rounded" (Level 2). A 0.5rem (8px) base radius is the standard for most components, while larger cards and containers should use `rounded-xl` (1.5rem / 24px). 

This level of roundness mimics the softened corners of a structured luxury handbag. Avoid sharp 0px corners, as they feel too aggressive for the "Soft-UI" aesthetic. However, avoid pill-shapes for primary buttons—keep them as rounded rectangles to maintain a sense of architectural stability.

## Components

- **Buttons:** Primary buttons use a Deep Burgundy background with White Inter text. They should have a subtle "raised" soft-UI shadow. Secondary buttons are Tan Leather with an inset shadow effect on hover.
- **Cards:** Cards should be White or very light Cream (`#FAF9F6`) against the neutral background. Use the dual-shadow technique to make them feel like they are rising out of the page.
- **Input Fields:** Use an "inset" shadow style to make fields look carved into the interface. Labels should use the `label-caps` typography style placed above the field.
- **Chips/Badges:** Small, pill-shaped elements with a Tan Leather border and 12px Inter medium text.
- **Lists:** Use 1px Tan Leather dividers with 50% opacity. Leading icons should be minimal, geometric line art in Deep Burgundy.
- **Smart-Status Indicators:** Since this is a "smart" bag, include a "Battery/Connectivity" component that uses a subtle glow effect (burgundy or gold) to indicate active status.
- **Navigation:** A centered, minimalist header with high letter-spacing. On scroll, apply a backdrop blur with a faint White tint.