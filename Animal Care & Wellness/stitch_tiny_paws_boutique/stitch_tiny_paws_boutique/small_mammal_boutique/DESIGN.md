---
name: Small Mammal Boutique
colors:
  surface: '#fff8f6'
  surface-dim: '#e4d7d4'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fef1ee'
  surface-container: '#f8ebe8'
  surface-container-high: '#f3e5e2'
  surface-container-highest: '#ede0dd'
  on-surface: '#201a19'
  on-surface-variant: '#3f4944'
  inverse-surface: '#362f2d'
  inverse-on-surface: '#fbeeeb'
  outline: '#6f7973'
  outline-variant: '#bfc9c2'
  surface-tint: '#246a52'
  primary: '#246a52'
  on-primary: '#ffffff'
  primary-container: '#aaf0d1'
  on-primary-container: '#2a6f57'
  inverse-primary: '#90d5b7'
  secondary: '#74593f'
  on-secondary: '#ffffff'
  secondary-container: '#fed9b8'
  on-secondary-container: '#795d43'
  tertiary: '#5c5d6e'
  on-tertiary: '#ffffff'
  tertiary-container: '#e0e0f4'
  on-tertiary-container: '#616373'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#abf1d2'
  primary-fixed-dim: '#90d5b7'
  on-primary-fixed: '#002116'
  on-primary-fixed-variant: '#00513b'
  secondary-fixed: '#ffdcbe'
  secondary-fixed-dim: '#e3c0a0'
  on-secondary-fixed: '#2a1704'
  on-secondary-fixed-variant: '#5a422a'
  tertiary-fixed: '#e1e1f5'
  tertiary-fixed-dim: '#c5c5d8'
  on-tertiary-fixed: '#191b29'
  on-tertiary-fixed-variant: '#444655'
  background: '#fff8f6'
  on-background: '#201a19'
  surface-variant: '#ede0dd'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-sm:
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
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
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

The brand personality of this design system is "Small Friend Energy"—an ethos that prioritizes gentleness, approachability, and the joyful fluffiness of small mammals. The target audience includes pet owners who view their hamsters, rabbits, and guinea pigs as family members, requiring an interface that feels as safe and comforting as a cozy nest.

The design style is a blend of **Soft-Minimalism** and **Tactile UI**. It utilizes expansive white space to reduce cognitive load while employing "squishy" interactive elements that invite touch. The aesthetic avoids sharp edges and aggressive transitions, opting instead for a nurturing, organic flow that evokes a sense of warmth and reliability.

## Colors

The palette is anchored by **Mint (#AAF0D1)** and **Peach (#FFDAB9)**, creating a fresh yet sun-drenched atmosphere. Mint serves as the primary action color, signifying growth and health, while Peach provides a warm, secondary accent for highlights and decorative elements.

A pale **Lavender (#E6E6FA)** is introduced as a tertiary color for background subtle variations and categorizations. The neutral palette eschews harsh blacks in favor of a **Deep Cocoa (#4A4240)** for typography, ensuring high legibility while maintaining the "soft-edged" visual philosophy. Backgrounds should primarily use a warm off-white or very faint cream to keep the interface feeling bright and airy.

## Typography

This design system utilizes **Plus Jakarta Sans** for all levels of the hierarchy. Its naturally rounded terminals and optimistic apertures perfectly complement the soft mammal theme. 

Headlines are set with tight tracking and heavy weights to create a "bouncy" and confident look. Body text is prioritized for readability with generous line heights (1.6x) to ensure the interface remains accessible for pet owners of all ages. Label styles are used for navigation and small call-outs, maintaining a slightly heavier weight to ensure they remain distinct against the pastel background tones.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with an emphasis on "negative space as a feature." Content is organized using a 12-column system for desktop and a 4-column system for mobile, with 24px gutters to allow elements plenty of room to breathe.

A 8px base unit drives the spacing rhythm. To achieve the "playful" look, margins and paddings are intentionally oversized—components should never feel cramped. Container padding typically defaults to `md` (24px) or `lg` (48px) to reinforce the airy, boutique feel of the shop.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layers**. Rather than using traditional gray shadows, this design system uses soft, diffused shadows tinted with the primary or secondary brand colors (e.g., a Peach-tinted shadow on a Peach card).

Surface depth is kept shallow. We use a "Neomorphism-lite" approach where elements appear as soft extrusions from the background. Elevated states are indicated by an increase in shadow blur and a slight scale-up (1.02x) rather than a drastic change in color, mimicking the tactile feedback of pressing into something soft.

## Shapes

The shape language is defined by high-radius **Rounded** corners. There are no sharp points in this design system. Standard UI components utilize a 0.5rem (8px) radius, while larger containers like product cards and hero sections use a 1.5rem (24px) radius to emphasize the "soft-edged" personality.

Interactive elements like buttons often lean toward a pill-shape to maximize the friendly aesthetic. Icons should follow this logic, using rounded stroke caps and joints to ensure visual harmony with the UI containers.

## Components

### Buttons
Primary buttons are pill-shaped, filled with Mint (#AAF0D1), and use Deep Cocoa (#4A4240) for text. They feature a soft, tinted shadow that disappears when "pressed" to simulate a physical push.

### Cards
Product cards use a white background with a 24px corner radius and a 1px soft Peach border. Images within cards should have a 16px radius to create a nested, "framed" look.

### Input Fields
Inputs are large and "pill-esque" with a 32px height minimum. They use a light Lavender or cream background instead of white to look softer against the page, with a Mint-colored border appearing only on focus.

### Chips & Tags
Used for mammal categories (e.g., "Dwarf Hamster," "Lop Rabbit"), these are fully rounded (pill) with pastel backgrounds and slightly darker text of the same hue to ensure a monochromatic, gentle appearance.

### Selection Controls
Checkboxes and radio buttons are oversized and use a Mint fill when active. The "checkmark" icon is thick and rounded to avoid a "sharp" or "clinical" feel.

### Additional Components: "The Fluff"
A custom "Toast" notification component should be used for pet-related alerts, featuring a small mammal icon and a Peach-tinted bubble, positioned at the top-center to mimic a friendly greeting.