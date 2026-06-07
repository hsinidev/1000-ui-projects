---
name: Biometric Haute Couture
colors:
  surface: '#16130f'
  surface-dim: '#16130f'
  surface-bright: '#3d3834'
  surface-container-lowest: '#110e0a'
  surface-container-low: '#1f1b17'
  surface-container: '#231f1b'
  surface-container-high: '#2d2925'
  surface-container-highest: '#393430'
  on-surface: '#eae1db'
  on-surface-variant: '#d3c4b7'
  inverse-surface: '#eae1db'
  inverse-on-surface: '#34302c'
  outline: '#9c8e82'
  outline-variant: '#4f453b'
  surface-tint: '#edbe8c'
  primary: '#ffce9b'
  on-primary: '#462a05'
  primary-container: '#e1b382'
  on-primary-container: '#65441d'
  inverse-primary: '#7b572e'
  secondary: '#c5c7c8'
  on-secondary: '#2e3132'
  secondary-container: '#494c4d'
  on-secondary-container: '#babcbd'
  tertiary: '#d9d7d8'
  on-tertiary: '#303031'
  tertiary-container: '#bdbbbc'
  on-tertiary-container: '#4b4b4c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddbb'
  primary-fixed-dim: '#edbe8c'
  on-primary-fixed: '#2b1700'
  on-primary-fixed-variant: '#604019'
  secondary-fixed: '#e1e3e4'
  secondary-fixed-dim: '#c5c7c8'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#454748'
  tertiary-fixed: '#e5e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474647'
  background: '#16130f'
  on-background: '#eae1db'
  surface-variant: '#393430'
typography:
  h1:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0em
  h3:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

This design system embodies "Biometric Luxury," a fusion of high-fashion elegance and futuristic physiological monitoring. The brand personality is elite, ethereal, and hyper-sophisticated. It speaks to a target audience of high-net-worth individuals who view technology as an invisible, exquisite enhancement to their physical presence.

The UI utilizes a **Glassmorphic** style, prioritizing depth through translucent layers and high-fidelity background blurs. The emotional response should be one of "serene intelligence"—a calm, expensive environment where technical biometric data is presented with the same reverence as a silk garment. Visual elements should feel lightweight, as if floating in a dimly lit, high-end gallery space.

## Colors

The palette centers on **Deep Charcoal** as the base to evoke the atmosphere of an evening gala. **Rose Gold** serves as the primary signature color, used for critical biometric highlights, interactive states, and luxury accents. **Silk White** provides a crisp, high-contrast secondary tone for primary typography and essential iconography.

Glassmorphism is achieved through a specific `glass_surface` blend of Deep Charcoal with 60% opacity, layered over blurred backgrounds. A "Pulse-Glow" effect is implemented using the `accent_glow_hex`, creating a breathing, rhythmic light effect behind key biometric data points to simulate a heartbeat or metabolic flow.

## Typography

Typography follows a strict hierarchy of "The Artistic" vs "The Technical." 

- **Playfair Display** is reserved for headlines, names of collections, and editorial statements. It should be treated as a design element with generous leading.
- **Inter** handles all biometric readouts, technical descriptions, and UI controls. 
- For technical data, use the `data-mono` style with increased letter spacing to emphasize the precision of the sensors. 
- Body text should maintain a light weight (300) to preserve the airy, silk-like aesthetic of the brand.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model within a maximum width of 1440px to ensure a curated, editorial feel. A 12-column grid is employed with wide gutters (32px) and significant outer margins (64px) to create "breathing room" typical of luxury boutiques.

Spacing is aggressive and intentional; use `section-gap` to separate biometric modules from garment visuals. The rhythm is based on an 8px scale, but preference should always be given to more white space (or "dark space") rather than less, to avoid a cluttered "tech-heavy" appearance.

## Elevation & Depth

This design system rejects traditional drop shadows in favor of **Layered Glassmorphism**. Depth is established through:

1.  **Backdrop Blur:** All floating surfaces must use a `20px` to `40px` Gaussian blur on the background layer.
2.  **Stroke Definition:** Instead of shadows, use a `1px` inner-border (stroke) in a semi-transparent Silk White (10% opacity) to define the edges of glass containers.
3.  **Luminous Depth:** Use the "Pulse-Glow" on the lowest z-index layer to create a sense of internal light emanating from within the garment sensors.
4.  **Z-Axis Stacking:** Biometric data overlays should feel 20-30 pixels "above" the fabric photography, created through varying blur intensities.

## Shapes

The shape language is "Soft-Technical." Elements use a subtle `0.25rem` (Soft) corner radius to bridge the gap between organic fabric curves and the precision of hardware sensors. 

- **Containers:** Use `rounded-lg` (0.5rem) for glass cards.
- **Interactive Elements:** Buttons and inputs use `rounded-xl` (0.75rem) to feel more inviting to the touch.
- **Data Points:** Biometric dots and pulse indicators are the only perfectly circular elements, representing the "Sensor" aspect of the brand.

## Components

**Buttons:**
Primary buttons are Silk White with Deep Charcoal text, featuring a subtle Rose Gold outer glow on hover. Secondary buttons are ghost-style with a 1px Rose Gold border and glass background.

**Biometric Cards:**
Glassmorphic containers with a backdrop blur of 30px. The header of the card uses `label-sm` in Rose Gold. Vital signs (e.g., heart rate) should feature a subtle "Pulse-Glow" animation.

**Input Fields:**
Minimalist underlines in Silk White (40% opacity). Upon focus, the underline transitions to Rose Gold with a faint glow. Labels use `label-sm` positioned above the field.

**Chips/Tags:**
Used for fabric types or sensor status. These are pill-shaped with a Deep Charcoal fill and 1px Silk White border. Text is `data-mono`.

**Navigation:**
A top-fixed, ultra-thin glass bar. Links are `data-mono` with a 12px vertical offset for the active state indicator—a single Rose Gold dot.

**Pulse-Glow Indicators:**
A custom component for the 'Silk-Sensor' feed. A circular element that expands and fades its outer glow in time with the user's recorded heart rate or biometric cadence.