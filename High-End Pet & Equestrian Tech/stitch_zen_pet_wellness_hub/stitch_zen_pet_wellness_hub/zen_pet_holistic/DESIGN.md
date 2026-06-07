---
name: Zen-Pet Holistic
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#424845'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#727875'
  outline-variant: '#c2c8c4'
  surface-tint: '#4e635a'
  primary: '#4e635a'
  on-primary: '#ffffff'
  primary-container: '#8da399'
  on-primary-container: '#263932'
  inverse-primary: '#b5ccc1'
  secondary: '#6a5d43'
  on-secondary: '#ffffff'
  secondary-container: '#f0debd'
  on-secondary-container: '#6e6147'
  tertiary: '#5f5e59'
  on-tertiary: '#ffffff'
  tertiary-container: '#a09e98'
  on-tertiary-container: '#363631'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#f3e0c0'
  secondary-fixed-dim: '#d6c4a5'
  on-secondary-fixed: '#231a06'
  on-secondary-fixed-variant: '#51452d'
  tertiary-fixed: '#e5e2db'
  tertiary-fixed-dim: '#c9c6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#474742'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.03em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.03em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style
The design system is anchored in the concept of restorative care and quiet confidence. It targets pet owners seeking holistic healing, prioritizing an emotional response of tranquility, trust, and empathy. 

The aesthetic is a sophisticated blend of **Minimalism** and **Glassmorphism**, utilizing vast white space to represent clarity and "breathing room" for the user. Visual interest is generated through organic, tactile shapes that mimic natural elements like river stones and polished wood, moving away from rigid geometry toward a more compassionate, human-centric interface. High-quality photography featuring soft natural lighting is central to the brand expression.

## Colors
The palette is derived from nature to evoke a sense of grounding and wellness. 
- **Sage Green (Primary):** Used for primary actions and brand presence, signifying growth and health.
- **Pale Wood (Secondary/Accent):** Used for subtle textural backgrounds and secondary UI accents, adding warmth to the minimalist structure.
- **Soft Charcoal (Text):** Used for all primary legibility to avoid the harshness of pure black while maintaining high accessibility.
- **White (Background):** The primary canvas, ensuring the interface feels airy and clean.
- **Soft Gradients:** Linear gradients should transition gently from Sage Green to a lighter tint of the same hue to simulate depth without adding visual noise.

## Typography
This design system utilizes **Plus Jakarta Sans** for its balanced, friendly, and contemporary humanist qualities. To convey a sense of "compassionate space," letter spacing (tracking) is intentionally increased across all levels, particularly in body copy and labels. Headlines should remain medium to semi-bold to maintain hierarchy, while body text remains light to regular to preserve the airy aesthetic.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy on desktop to ensure content remains focused and intimate, while transitioning to a fluid model for mobile devices. 

A 12-column grid is used with generous gutters to prevent the UI from feeling "crowded." Vertical rhythm is strictly maintained using 8px increments. Spacing between major sections should be expansive (80px–120px) to reinforce the minimalist brand values and allow the organic shapes and photography to stand out as focal points.

## Elevation & Depth
Depth in this design system is achieved through soft, multi-layered shadows and **Glassmorphism**.
- **Surface Layering:** The base is pure White. Elevated elements use a semi-transparent "Glass" effect (White at 60-80% opacity with a 16px-24px backdrop blur).
- **Shadows:** Use "Ambient Shadows"—extremely diffused, low-opacity (#8DA399 at 10% opacity) to create a soft glow rather than a harsh drop.
- **Depth Hierarchy:** Higher elevation is communicated by increasing the blur radius of the shadow and the intensity of the background blur, never by darkening the surface color.

## Shapes
The shape language is strictly **Organic and Pebble-like**. 
- **Buttons and Chips:** Must use a full pill-shape (radius: 999px).
- **Cards and Containers:** Use "extra-large" rounded corners (minimum 32px) to mimic the feel of tumbled stones. 
- **Icons:** Should feature rounded terminals and soft joints to match the typography and container language. Sharp 90-degree angles are prohibited in the design system.

## Components
- **Pebble Buttons:** High-radius pill shapes. Primary buttons use a Sage Green to Light Sage gradient; secondary buttons use a Pale Wood tint with no border.
- **Glassmorphism Cards:** Containers featuring a thin, 1px white inner stroke (low opacity) to define edges, a soft backdrop blur, and the primary ambient shadow.
- **Progress Indicators:** Soft, rounded "track" bars using Pale Wood as the background and Sage Green as the fill. The transition between states should be animated with a slow, easing curve.
- **Inputs:** Minimalist fields with only a soft-colored bottom border or a subtle recessed shadow to indicate "interactive depth."
- **Wellness Tiles:** A custom component for rehab exercises that uses high-quality photography as the background, overlaid with a glassmorphism label at the bottom.
- **Selection Controls:** Radio buttons and checkboxes appear as small, filled "seeds" or rounded pebbles when active, avoiding traditional harsh boxy forms.