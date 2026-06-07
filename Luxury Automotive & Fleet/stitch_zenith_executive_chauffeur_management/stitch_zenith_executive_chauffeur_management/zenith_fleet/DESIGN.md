---
name: Zenith-Fleet
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#181a1a'
  on-tertiary-container: '#818383'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  title-sm:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  section-gap: 48px
  stack-tight: 4px
  stack-base: 12px
---

## Brand & Style

The design system is engineered for the ultra-high-net-worth individual and C-suite executive. It prioritizes discretion, precision, and an elite sense of arrival. The brand personality is "The Silent Concierge"—present when needed, invisible when not. 

The aesthetic combines **Minimalism** with **Glassmorphism**. We utilize a dark-mode-first environment to reduce eye strain and maintain a low-profile presence in professional settings. The interface relies on generous whitespace (negative space) to convey a sense of calm and exclusivity, while subtle metallic accents and frosted surfaces provide a tactile, premium feel reminiscent of a luxury vehicle’s interior.

## Colors

This design system utilizes a high-contrast, prestigious palette designed for low-light environments and executive privacy.

- **Deep Charcoal (#1A1A1A):** The foundation. Used for all primary backgrounds to ensure the hardware bezel of mobile devices disappears into the UI.
- **Champagne Gold (#D4AF37):** The signature accent. Reserved for primary actions, success states, and elite status indicators. Use sparingly to maintain its value.
- **Crisp White (#FFFFFF):** Used for primary content and body text to ensure maximum readability against the charcoal base.
- **Surface Neutrals:** Mid-tone charcoals (#2C2C2C) are used for secondary containers and input backgrounds to create subtle layering without breaking the dark-mode immersion.

## Typography

The typography system establishes a rigorous hierarchy using a mix of traditional authority and modern efficiency.

- **Headlines (Noto Serif):** Evokes the heritage of fine print and luxury editorial. Used for screen titles, driver names, and premium service tiers.
- **Body & Functional UI (Manrope):** A refined, geometric sans-serif that ensures high legibility for logistical data, ETAs, and security codes. 
- **Tracking:** Use wider letter-spacing for "label-caps" to enhance the premium, airy feel of the brand. Use tighter tracking for large display headings to maintain a compact, powerful look.

## Layout & Spacing

This design system follows a **Fixed-Fluid hybrid** approach optimized for mobile. On handheld devices, it uses a 4-column grid with generous 24px outer margins to keep interactive elements away from the screen edges, facilitating one-handed operation.

The spacing rhythm is strictly based on an 8px scale. High-priority information (like a "Current Ride" status) is given significant vertical breathing room—utilizing the "section-gap" variable—to isolate the data and reduce cognitive load for busy executives.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and light-source simulation rather than traditional drop shadows.

- **Surface Tiers:** The base layer is pure Charcoal. Floating cards use a semi-transparent background (`rgba(255, 255, 255, 0.04)`) with a high-intensity `backdrop-filter: blur(20px)`.
- **Metallic Accents:** A 1px "inner glow" or "stroke" using a linear gradient of Champagne Gold to Transparent is applied to the top edge of primary cards to simulate the catch-light of a metal bezel.
- **Interactive State:** When an element is pressed, it should "recede" (lower opacity) rather than lift, maintaining the discreet, grounded nature of the service.

## Shapes

The shape language is "Soft-Technical." Elements use a subtle 0.25rem (4px) base radius. This creates a profile that is modern and sharp enough to feel professional and architectural, without being as aggressive as 0px hard corners. 

- **Primary Buttons:** Use a standard `rounded-lg` (8px) to provide a clear hit-target.
- **Profile Avatars & Security Icons:** These remain strictly circular to provide a soft contrast to the otherwise rectangular and structural layout.

## Components

- **Action Buttons:** Primary buttons are solid Champagne Gold with Black text. Secondary actions use "Ghost" styling—White text with a 1px White border at 20% opacity.
- **The "Executive Card":** A glassmorphic container for ride details. It must feature a high-blur background and a 1px top-border gradient to define its presence against the dark background.
- **Status Indicators:** Discreet pulses or thin lines of Champagne Gold. Avoid bright reds or greens unless critical (security alerts); keep the interface monochrome and gold.
- **Input Fields:** Minimalist under-lined inputs or subtly filled containers (#2C2C2C). The active state is indicated by a Champagne Gold underline.
- **Security Key/QR:** Displayed in a high-contrast white container within a glass card, ensuring scanning efficiency for the chauffeur while maintaining the aesthetic.
- **Signature List Items:** Used for ride history. High whitespace between items, using `label-caps` for dates and `notoSerif` for destinations.