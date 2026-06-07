---
name: WellnessWare
colors:
  surface: '#fbf9f7'
  surface-dim: '#dbdad8'
  surface-bright: '#fbf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1b'
  on-surface-variant: '#424844'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ee'
  outline: '#737874'
  outline-variant: '#c2c8c3'
  surface-tint: '#4f6359'
  primary: '#4f6359'
  on-primary: '#ffffff'
  primary-container: '#a7bcb0'
  on-primary-container: '#394c43'
  inverse-primary: '#b6cbbf'
  secondary: '#5b5c77'
  on-secondary: '#ffffff'
  secondary-container: '#ddddfc'
  on-secondary-container: '#5f607b'
  tertiary: '#5c5f60'
  on-tertiary: '#ffffff'
  tertiary-container: '#b5b7b8'
  on-tertiary-container: '#464849'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d2e8db'
  primary-fixed-dim: '#b6cbbf'
  on-primary-fixed: '#0d1f17'
  on-primary-fixed-variant: '#384b42'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#c4c4e2'
  on-secondary-fixed: '#181a30'
  on-secondary-fixed-variant: '#43455e'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fbf9f7'
  on-background: '#1b1c1b'
  surface-variant: '#e4e2e0'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  emergency-ui:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '800'
    lineHeight: '1'
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

The design system is centered on the principles of psychological safety, tranquility, and immediate accessibility. It targets employees navigating high-stress environments, providing a digital sanctuary that feels supportive rather than clinical. 

The aesthetic is **Neomorphic (Soft-UI)**, utilizing a play of light and shadow to create a tactile, "squishy" interface that feels organic and non-threatening. By mimicking physical surfaces that are extruded from or recessed into the background, the design system avoids the harshness of traditional flat UI, fostering an emotional response of comfort and ease. The interface prioritizes anonymity and speed of action, ensuring that users in distress feel both seen by the system and hidden from their immediate physical surroundings.

## Colors

The palette is derived from nature and twilight, designed to lower the user's heart rate. 
- **Soft Sage** acts as the primary grounding element, used for main structural components and active states.
- **Lavender** serves as the secondary accent, highlighting moments of growth, reflection, and mindfulness.
- **Background Tones** are not pure white but a very light "Sage-White" to facilitate the Neumorphic light-source effect (white highlights against a slightly darker base).
- **Emergency Accent** is a desaturated, compassionate coral-red, used exclusively for the "Quick Exit" and crisis support features to ensure high visibility without triggering alarm.

## Typography

This design system utilizes **Manrope** for its entire type scale. Manrope strikes a perfect balance between modern geometric precision and organic warmth. 

Headlines use a tighter letter-spacing and heavier weights to feel grounded and authoritative, while body copy utilizes generous line heights to ensure readability for users who may be experiencing cognitive load or distress. Descriptive labels and secondary information use a slightly wider tracking to maintain clarity at small sizes.

## Layout & Spacing

The layout follows a **fluid grid** model with significant emphasis on "Negative Space" to prevent visual clutter. 

A 12-column system is used for desktop, scaling down to 4 columns for mobile. However, content width is strictly capped at 800px for long-form reading to maintain focus. Spacing follows an 8pt linear scale, but padding within Neomorphic cards is intentionally oversized (minimum 24px) to emphasize the soft, pillowy nature of the containers.

## Elevation & Depth

Depth is the primary communicator of hierarchy in this design system. Instead of traditional drop shadows, we use **Dual-Shadow Neomorphism**:
- **Elevated Elements (Buttons/Cards):** A top-left shadow in pure white (#FFFFFF) and a bottom-right shadow in a darker tint of the background (#D1D9D4), both with a 16px to 32px blur.
- **Sunken Elements (Input Fields/Depressed States):** Inner shadows that create a "pressed-in" look, signaling that the user is providing information or entering a private space.
- **Glassmorphism Overlays:** Modals and the "Quick Exit" bar use a subtle backdrop blur (20px) with 80% opacity to maintain a sense of the user's current context while providing a focused layer.

## Shapes

The shape language is defined by extreme smoothness. There are no sharp corners in the design system. 

Standard components use a **16px (1rem)** radius, while interactive elements like buttons and chips utilize **full-pill** rounding. The goal is to eliminate any visual "points" that might feel aggressive or clinical. Large containers may use up to 32px rounding to emphasize their soft, protective nature.

## Components

### Quick Exit Button
The most critical component. It is a persistent, high-elevation pill-shaped button fixed to the bottom-right or top-right of the viewport. It uses the `accent_emergency` color with white text. Upon clicking, it instantly redirects to a neutral page (e.g., Google or a weather site) and clears the local session state.

### Neomorphic Buttons
Buttons should appear to be molded from the background. The "Default" state is elevated; the "Active/Pressed" state uses inner shadows to appear physically pushed into the interface.

### Input Fields
To distinguish from buttons, input fields are always "Sunken" (inner shadows), creating a visual well for the user to place their thoughts or data into.

### Safety Cards
Information is housed in large, soft-shadowed cards. These cards should have a subtle gradient from the top-left (lighter) to the bottom-right (darker) to reinforce the 3D effect.

### Anonymity Indicators
A persistent "Shield" icon in the status bar, using a soft Lavender glow, to constantly reassure the user that their session is encrypted and private.