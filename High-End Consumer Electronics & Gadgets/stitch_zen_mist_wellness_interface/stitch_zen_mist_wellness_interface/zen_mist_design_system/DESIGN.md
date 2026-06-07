---
name: Zen-Mist Design System
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
  on-surface-variant: '#424845'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#727875'
  outline-variant: '#c2c8c4'
  surface-tint: '#4e635a'
  primary: '#4e635a'
  on-primary: '#ffffff'
  primary-container: '#8da399'
  on-primary-container: '#263932'
  inverse-primary: '#b5ccc1'
  secondary: '#665e4b'
  on-secondary: '#ffffff'
  secondary-container: '#ebdec6'
  on-secondary-container: '#6a624f'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#9d9e9e'
  on-tertiary-container: '#343536'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#ede1c9'
  secondary-fixed-dim: '#d1c5ae'
  on-secondary-fixed: '#211b0c'
  on-secondary-fixed-variant: '#4d4634'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: manrope
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
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
  container-margin: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
  max-width: 1200px
---

## Brand & Style

This design system is built upon a philosophy of "Atmospheric Luxury." It prioritizes the emotional state of the user, transforming the interface into a digital sanctuary that mirrors the calming effects of the physical product. The brand personality is serene, sophisticated, and intentionally airy, ensuring that technology feels like a natural extension of a wellness routine rather than a digital intrusion.

The visual style blends **Minimalism** with **Glassmorphism**. By utilizing heavy whitespace, a restricted natural palette, and translucent frosted layers, the interface achieves a sense of depth and lightness. Every interaction is designed to feel effortless, utilizing fluid motion and soft visuals to reduce cognitive load and evoke a sense of professional-grade tranquility.

## Colors

The color palette is inspired by natural elements: fog-covered forests, light-grained timber, and morning mist. 

- **Sage Green (#8DA399):** The primary brand color, used for active states, primary actions, and representing healthy air quality levels.
- **Pale Wood (#E8DCC4):** The secondary accent, providing a tactile, organic warmth to the digital experience. It is used for subtle highlights and secondary interactive elements.
- **Soft White (#F9F9F9):** The foundation of the interface. It provides an expansive, airy background that allows other elements to breathe.
- **Text & Accents:** A deep charcoal-grey (#4A4A4A) is used for text to maintain high legibility while avoiding the harshness of pure black, preserving the soft aesthetic.

## Typography

This design system utilizes **Manrope** as the sole typeface. Manrope is a modern, refined sans-serif that balances geometric precision with organic softness, making it ideal for a luxury wellness context.

- **Headlines:** Set with generous line height and slightly tighter letter-spacing for a modern, editorial feel. Display sizes use a lighter weight (300) to convey elegance.
- **Body Text:** Optimized for readability with comfortable line heights.
- **Labels:** Set in uppercase with increased letter-spacing to provide a clear hierarchy for metadata and navigation without feeling cluttered.

## Layout & Spacing

The layout philosophy follows a **fluid grid** model with significant emphasis on "Safe Zones" to prevent visual crowding. 

- **Grid:** A 12-column system is used for desktop/tablet, while a flexible single-column layout is used for mobile. 
- **Rhythm:** Spacing follows an 8px base unit. 
- **Margins:** Generous 24px outer margins ensure content never feels cramped against the screen edges. 
- **Whitespace:** Elements are grouped with narrow internal spacing (stack-sm) but separated from other groups with large vertical gaps (stack-lg) to emphasize the airy personality of the brand.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Ambient Shadows** rather than traditional solid layering.

1.  **Base Layer:** The Soft White background provides a flat, matte foundation.
2.  **Floating Containers:** Content cards use a semi-transparent white fill (60% opacity) with a `backdrop-filter: blur(20px)`. This creates a "frosted glass" effect that feels high-end and lightweight.
3.  **Shadows:** Shadows are extremely diffused (Blur: 30px+) with low opacity (5-10%) and a slight Sage Green tint (#8DA399) to keep the depth feeling natural and integrated with the brand palette.
4.  **Borders:** Glass elements are defined by a 1px solid border at 20% opacity to provide crisp edges without adding visual weight.

## Shapes

The shape language is organic and fluid. Sharp corners are entirely avoided to maintain a "soft" emotional response.

- **Standard Containers:** Use a 16px (1rem) radius.
- **Feature Cards:** Use a 24px (1.5rem) radius for a more prominent, friendly appearance.
- **Buttons and Inputs:** These should lean toward a "squircle" or fully pill-shaped aesthetic to mimic the ergonomic design of luxury physical products.
- **Fluid Elements:** Background decorative elements should use irregular, organic vector blobs to simulate movement of mist and air.

## Components

- **Buttons:** Primary buttons use a solid Sage Green fill with white text. Secondary buttons use a glassmorphic background with a Sage Green border. All buttons have high internal horizontal padding for a premium, spacious look.
- **Chips:** Used for aromatherapy "scent" profiles. These are pill-shaped, using Pale Wood backgrounds with dark charcoal text.
- **Input Fields:** Minimalist design featuring only a bottom border (1px) in Sage Green when active, or a subtle glass container with a Pale Wood border.
- **Progress Indicators:** Circular air-quality rings that use gentle gradients from Soft White to Sage Green to represent purity levels.
- **Cards:** Glassmorphic containers with soft-rounded corners. Content within cards is always left-aligned to maintain the minimalist structure.
- **Sensory Sliders:** Thick, organic slider tracks for mist intensity, featuring a soft "Pale Wood" handle that feels tactile and easy to manipulate.