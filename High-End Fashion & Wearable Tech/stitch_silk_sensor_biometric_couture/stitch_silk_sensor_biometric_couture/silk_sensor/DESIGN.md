---
name: Silk-Sensor
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d6c2bd'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9e8d88'
  outline-variant: '#514440'
  surface-tint: '#f5b9a6'
  primary: '#ffc9b9'
  on-primary: '#4c261a'
  primary-container: '#e7ac9a'
  on-primary-container: '#6a3f31'
  inverse-primary: '#815344'
  secondary: '#c7c6c5'
  on-secondary: '#2f3130'
  secondary-container: '#484948'
  on-secondary-container: '#b9b8b7'
  tertiary: '#ffc8c5'
  on-tertiary: '#68000f'
  tertiary-container: '#ffa09d'
  on-tertiary-container: '#911922'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#f5b9a6'
  on-primary-fixed: '#321207'
  on-primary-fixed-variant: '#663c2e'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c5'
  on-secondary-fixed: '#1a1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#ffdad8'
  tertiary-fixed-dim: '#ffb3b0'
  on-tertiary-fixed: '#410006'
  on-tertiary-fixed-variant: '#8c1520'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 22px
    fontWeight: '500'
    lineHeight: '1.4'
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
  data-display:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '300'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  margin-safe: 24px
  gutter: 16px
  section-gap: 40px
---

## Brand & Style

This design system embodies the intersection of high-fashion couture and cutting-edge biometric technology. The brand personality is elite, ethereal, and avant-garde, catering to a sophisticated clientele that values both aesthetic excellence and personal data insights. 

The visual style utilizes a high-end **Glassmorphism** approach, mimicking the translucency of fine silk and the precision of glass. It avoids the rigidity of traditional tech interfaces in favor of fluid, organic shapes that mirror the human form. The emotional response is one of calm exclusivity—an intimate, luxurious experience where technology feels like a second skin rather than a tool.

## Colors

The palette is anchored by **Deep Charcoal**, providing a prestigious "Evening Wear" foundation. **Rose Gold** serves as the primary metal accent, used for interactive elements and brand flourishes. **Silk White** is utilized for primary typography and high-contrast surfaces to maintain a sense of airiness.

The **Pulse-Glow** is a specialized functional accent color. It must be used sparingly to represent live biometric data, heartbeat rhythms, and active sensor states. In terms of application, use Silk White at varying opacities (10% to 80%) to create the frosted glass effect against the Deep Charcoal background.

## Typography

This design system employs a high-contrast typographic pairing. **Playfair Display** provides the editorial authority required for high-fashion, used exclusively for headers and prominent quotes. **Inter** handles all functional UI, biometric data, and body copy to ensure maximum legibility against complex glass backgrounds.

For a luxury feel, apply increased letter spacing (tracking) to all-caps labels. Data visualizations should use the light weight of Inter to maintain a "scientific yet chic" aesthetic. Avoid bold weights in body copy; use color shifts (Rose Gold) for emphasis instead.

## Layout & Spacing

The layout follows a fluid, mobile-centric grid with an emphasis on "negative space as luxury." Use a generous **24px side margin** to ensure content feels framed and intentional. Vertical rhythm is based on an **8px base unit**.

Layout components should not feel boxed in. Instead of traditional containers, use vertical transitions and soft gradients to separate content sections. Elements should appear to float within the viewport, utilizing the full width of the screen only when displaying high-resolution fabric textures or immersive imagery.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional shadows. This design system utilizes three distinct layers of elevation:

1.  **The Floor:** Deep Charcoal solid background, occasionally textured with ultra-low-contrast fabric patterns.
2.  **The Surface:** Semi-transparent Silk White (10-15% opacity) with a `backdrop-filter: blur(20px)`. This layer features a 1px solid border at 20% opacity (Silk White) to define edges.
3.  **The Floating Layer:** Interactive elements like buttons and active biometric cards use a higher opacity blur and a subtle inner glow of Rose Gold to appear closer to the user.

Shadows, if used, should be "Ambient Glows"—highly diffused, using the color of the element (e.g., a soft Rose Gold shadow for a primary button) at 10% opacity.

## Shapes

The shape language is **organic and fluid**. While the base roundedness is set to `2` (0.5rem - 1.5rem), the design system encourages the use of asymmetric "pebble" shapes for decorative elements and mask paths. 

Avoid sharp 90-degree corners entirely. Containers should feel soft to the touch. Interactive zones (buttons, inputs) should utilize the higher end of the scale (rounded-xl) to mimic the smooth edges of polished jewelry or high-tech wearables.

## Components

### Buttons
Primary buttons are "Glass Capsules": fully rounded (pill-shaped), with a Rose Gold border and a subtle backdrop blur. The text is Inter Bold, all-caps. Tertiary buttons are simple Silk White text with a 1px Rose Gold underline.

### Cards
Cards are the primary vessel for biometric data. They must feature a `20px` backdrop blur. The background should include a masked, high-resolution fabric texture (e.g., silk weave) at 5% opacity to provide tactile depth.

### Biometric Visualizers
Pulse-Glow lines or circular rings that represent heart rate or skin temperature. These should use a "neon-silk" effect—a thin stroke of `#FF6B6B` with a soft outer glow of the same color.

### Inputs & Toggles
Input fields are "Ghost Fields"—no background fill, only a bottom border in 30% Silk White. Upon focus, the border transitions to Rose Gold. Toggles should behave like jewelry slides, using a Rose Gold "bead" on a Silk White track.

### Fabric Overlays
A unique component for this design system: a full-screen, low-opacity texture overlay that moves slightly with the device's accelerometer to create a shimmering, realistic silk effect over the entire UI.