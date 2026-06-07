---
name: Compassionate Care
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
  on-surface-variant: '#48454e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#79757f'
  outline-variant: '#cac4cf'
  surface-tint: '#625886'
  primary: '#625886'
  on-primary: '#ffffff'
  primary-container: '#968bbd'
  on-primary-container: '#2d244f'
  inverse-primary: '#cbbff4'
  secondary: '#40627d'
  on-secondary: '#ffffff'
  secondary-container: '#bcdefe'
  on-secondary-container: '#41627e'
  tertiary: '#5e5e5d'
  on-tertiary: '#ffffff'
  tertiary-container: '#929290'
  on-tertiary-container: '#2a2b2a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e7deff'
  primary-fixed-dim: '#cbbff4'
  on-primary-fixed: '#1e143f'
  on-primary-fixed-variant: '#4a406d'
  secondary-fixed: '#cbe6ff'
  secondary-fixed-dim: '#a8caea'
  on-secondary-fixed: '#001e31'
  on-secondary-fixed-variant: '#274a64'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  headline-lg:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 32px
  margin: 48px
  container-max: 1200px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built upon a foundation of empathy, stability, and tranquility. It is designed specifically for an audience that requires clarity and emotional reassurance: seniors, their families, and dedicated caregivers. The brand personality is "The Gentle Guardian"—authoritative enough to trust, yet soft enough to comfort.

The visual style leans into a refined **Minimalism** blended with **Soft Corporate** elements. By prioritizing massive amounts of whitespace and a restricted, soothing palette, the UI reduces cognitive load and prevents overstimulation. Every interaction is intentional, moving away from high-energy digital trends toward a more "analog-inspired" digital experience that feels as safe as a physical home. Focus is placed on high-quality, authentic photography of natural light and calm environments to ground the digital experience in reality.

## Colors

The palette is rooted in the psychology of serenity. The primary color is a **Soft Lavender**, chosen for its association with grace and composure. This is complemented by a **Sky Blue** secondary tone that evokes feelings of trust and open horizons. 

An **Off-White** (Warm White) serves as the primary canvas color to avoid the clinical "starkness" of pure white, making the screen easier on the eyes over long periods. Text utilizes a deep charcoal gray rather than pure black to maintain high contrast for accessibility while softening the visual "bite." Interaction states (hover, focus) should use subtle shifts in saturation rather than brightness to maintain the calm atmosphere.

## Typography

This design system utilizes **Public Sans** for all tiers of the hierarchy. Its institutional roots provide a sense of official reliability, while its open counters and clear letterforms ensure maximum legibility for users with visual impairments. 

The type scale is intentionally larger than standard web systems. A generous line height (1.6x for body text) is mandatory to prevent lines from "blurring" together for older readers. Bold weights are used sparingly to highlight critical information, while lighter weights are avoided entirely to ensure every character remains crisp and readable against the off-white background.

## Layout & Spacing

The layout follows a **Fixed Grid** model to provide a sense of "place" and predictability. Users should never feel lost; therefore, navigation and primary content containers remain in consistent, expected locations. 

The spacing rhythm is built on an 8px base unit, but emphasizes "Large" and "Extra Large" values to create an airy, unhurried feel. Gutters are intentionally wide (32px) to clearly separate different content blocks, preventing visual clutter. Vertical stacking uses generous margins to ensure that the user’s eye can rest between sections of information.

## Elevation & Depth

To maintain the "Gentle & Calm" aesthetic, this design system avoids harsh shadows or complex layering. Instead, it utilizes **Ambient Shadows**: extra-diffused, low-opacity shadows with a slight Lavender tint. These shadows should feel like soft light hitting a physical surface, rather than a digital effect.

Depth is used functionally to indicate interactivity. A "floating" card indicates it can be clicked, while flat surfaces represent static information. Backgrounds use tonal layering—subtle shifts between the Off-White base and very light Lavender tints—to define sections without the need for heavy borders.

## Shapes

The shape language is defined by **Rounded** geometry. Sharp corners are perceived as aggressive or clinical; therefore, all containers, buttons, and input fields utilize a 0.5rem (8px) base radius. Large content cards and featured images should use a more pronounced 1.5rem (24px) radius to emphasize the "soft" brand character. 

Icons should follow this logic, utilizing rounded caps and joins rather than shear angles. The goal is to create a UI that feels "tactile and safe" to the touch.

## Components

### Buttons
Buttons are large and highly visible. Primary buttons use the Soft Lavender background with high-contrast white text. They feature a subtle "press" animation that is slow and deliberate, providing clear haptic-style feedback without being jarring.

### Cards
Cards are the primary organizational unit. They should feature generous internal padding (at least 32px) and use the ambient shadow style. Avoid over-stuffing cards; each card should convey one primary thought or action.

### Input Fields
Inputs must have a permanent, visible border in a soft slate color. Do not rely on "bottom-line only" styles. Labels must always be visible (never use disappearing placeholder text) to accommodate users with memory challenges.

### Lists
Lists use high-contrast bullets or icons and increased vertical padding between items. This ensures each list item is a distinct "touch target" and is easy to scan.

### Additional Components
*   **Information Callouts:** Use the Sky Blue palette for "Trust" notes or helpful tips, featuring a soft icon.
*   **Navigation:** A simplified top-tier navigation with large text and clear active-state indicators (a thick, soft-ended underline).
*   **Progress Indicators:** Steppers should be horizontal, clearly labeled, and use soft transitions to show progress in a non-stressful way.