---
name: AlpinePeak
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#42474b'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#73787b'
  outline-variant: '#c2c7cb'
  surface-tint: '#4b626c'
  primary: '#4b626c'
  on-primary: '#ffffff'
  primary-container: '#d1e9f6'
  on-primary-container: '#536974'
  inverse-primary: '#b2cad7'
  secondary: '#78583c'
  on-secondary: '#ffffff'
  secondary-container: '#fed1af'
  on-secondary-container: '#79583d'
  tertiary: '#565f6a'
  on-tertiary: '#ffffff'
  tertiary-container: '#dce6f2'
  on-tertiary-container: '#5d6771'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cee6f3'
  primary-fixed-dim: '#b2cad7'
  on-primary-fixed: '#061e28'
  on-primary-fixed-variant: '#344a54'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#e9be9c'
  on-secondary-fixed: '#2c1602'
  on-secondary-fixed-variant: '#5e4027'
  tertiary-fixed: '#dae3f0'
  tertiary-fixed-dim: '#bdc8d3'
  on-tertiary-fixed: '#131d25'
  on-tertiary-fixed-variant: '#3e4852'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '600'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
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
  label-bold:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  max-width: 1440px
---

## Brand & Style

This design system is built upon the "Cozy & Crisp" narrative, merging the structural precision of high-end mountain architecture with the inviting warmth of a fireside retreat. The brand personality is professional and authoritative yet deeply welcoming, catering to high-net-worth individuals seeking both adventure and sanctuary.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. We utilize a "Frost" aesthetic—using semi-transparent layers and heavy background blurs—to mimic the appearance of ice and winter atmosphere. This is balanced by organic textures and warm accents to ensure the UI never feels clinical. The goal is to evoke the sensation of looking through a pristine, fogged window at a breathtaking alpine landscape.

## Colors

The palette is derived from the natural transition between the mountain peak and the chalet interior. 

- **Ice Blue (Primary):** Used for primary accents, active states, and soft background washes. It provides the "Crisp" cooling effect.
- **Warm Wood (Secondary):** Used for call-to-action elements, interactive highlights, and decorative accents. This grounded earth tone provides the "Cozy" contrast to the cooler elements.
- **Silver (Tertiary):** A sophisticated metallic neutral used for borders, secondary buttons, and subtle structural dividers.
- **Slate (Neutral):** Provides deep contrast for typography, ensuring legibility against light "Frost" backgrounds.

The default mode is light, utilizing high-key backgrounds to maximize the luminosity of the glassmorphism effects.

## Typography

This design system employs a sophisticated typographic pairing to reflect luxury real estate standards. 

**Noto Serif** is reserved for headlines and editorial moments. Its classic, timeless proportions signal exclusivity and heritage. **Manrope** is used for all functional text, property data, and body copy. Its modern, geometric construction ensures maximum readability when displaying complex information like "Distance to Lift" or property dimensions. For labels and data points, uppercase styling with slight letter-spacing is preferred to enhance the "Crisp" architectural feel.

## Layout & Spacing

This design system utilizes a **fixed grid** model for desktop to maintain a curated, editorial feel, transitioning to a fluid model for tablet and mobile devices. 

The spacing rhythm is generous, emphasizing whitespace to create a sense of mountain air and openness. We use a 12-column grid with wide 24px gutters. Elements should be grouped using logical clusters, with significant vertical padding (often 80px-120px) between major sections to allow the high-quality property imagery to breathe.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and soft, ambient shadows. 

- **Level 1 (Base):** Solid white or very light Ice Blue surfaces.
- **Level 2 (Frost Panels):** Semi-transparent white (opacity 60-80%) with a 20px backdrop blur and a 1px soft white internal stroke to simulate a "beveled glass" edge.
- **Level 3 (Interactive):** Elements that require focus use an extra-diffused shadow (color: `#1E293B` at 5% opacity, 30px blur) to appear as if they are floating slightly above the frost layer.

Shadows should never be harsh or black; they must always be tinted with the neutral Slate or Ice Blue to maintain the "Crisp" atmosphere.

## Shapes

The shape language reflects the "Cozy & Crisp" duality. We avoid aggressive sharp corners to maintain an inviting feel, opting for **Rounded (0.5rem base)** corners for standard UI components like inputs and small buttons. 

Larger containers, such as property cards and "Frost" panels, use **Rounded-XL (1.5rem)** to create a softer, premium silhouette. This roundedness mimics the soft curves of snowdrifts while maintaining enough structure to feel architecturally sound.

## Components

### Buttons & Interaction
- **Primary CTA:** Solid "Warm Wood" with white Manrope text. High contrast to draw the eye.
- **Secondary CTA:** Ghost style with a "Silver" border and "Ice Blue" text.

### Property Cards
Cards are the centerpiece of this design system. They must feature:
- A "Frost" overlay at the bottom containing the price and location.
- High-resolution imagery with a subtle zoom-on-hover effect.
- Metadata icons (beds, baths, sqft) rendered in "Silver".

### Distance to Lift Calculator
A specialized component featuring a "Silver" track and a "Warm Wood" slider or indicator. The output should be displayed in bold "Noto Serif" to emphasize the proximity—the platform's key luxury metric.

### Video Galleries
Galleries should utilize full-width immersive layouts with minimal UI interference. Play/Pause and navigation controls should be "Frost" circles with 70% opacity, appearing only on interaction to keep the visual experience "Crisp."

### Input Fields
Forms should use a "Silver" 1px bottom-border only (minimalist style) or a light "Ice Blue" filled state with rounded corners, ensuring they feel integrated into the "Frost" panels.