---
name: Eco-Compost
colors:
  surface: '#faf9f6'
  surface-dim: '#dadad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f0'
  surface-container: '#efeeea'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2df'
  on-surface: '#1a1c1a'
  on-surface-variant: '#424842'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f1f1ed'
  outline: '#737972'
  outline-variant: '#c2c8c0'
  surface-tint: '#4a654f'
  primary: '#4a654f'
  on-primary: '#ffffff'
  primary-container: '#8daa91'
  on-primary-container: '#253f2b'
  inverse-primary: '#b0ceb4'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#7b545a'
  on-tertiary: '#ffffff'
  tertiary-container: '#c6979e'
  on-tertiary-container: '#523036'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cceacf'
  primary-fixed-dim: '#b0ceb4'
  on-primary-fixed: '#062010'
  on-primary-fixed-variant: '#334d38'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffd9de'
  tertiary-fixed-dim: '#ecbac1'
  on-tertiary-fixed: '#2f1319'
  on-tertiary-fixed-variant: '#613d43'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2df'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  margin-safe: 32px
  gutter: 24px
---

## Brand & Style

The visual identity of this design system centers on "Domestic Serenity." It bridges the gap between high-end kitchen appliances and sustainable technology. The brand personality is quiet, sophisticated, and clean, aiming to transform bio-waste management from a chore into a premium wellness ritual. 

The aesthetic is a refined execution of **Neomorphism (Soft-UI)**, prioritizing tactile feedback and organic depth. By utilizing subtle extrusion and recession effects on a consistent off-white base, the interface feels integrated into the physical environment. This is complemented by **Glassmorphism** for high-level overlays to maintain a sense of airiness and light. The target audience values environmental responsibility but demands a frictionless, luxury-tier digital experience.

## Colors

The palette is derived from natural, muted tones to reinforce the organic nature of composting while maintaining a sterile, clean feel.

- **Primary (Sage Green):** Used for primary actions, success states, and biological progress indicators.
- **Secondary (Silver):** Used for metallic accents, inactive states, and hardware-adjacent UI elements.
- **Background (Off-White):** The foundational surface for all neumorphic shadows. This specific hex is calibrated to allow both pure white highlights and soft cool-grey shadows to remain visible.
- **Accent (Deep Forest Green):** Reserved for high-contrast typography and critical data points to ensure legibility against the soft UI.

## Typography

This design system utilizes **Inter** exclusively to achieve a systematic, modern look. To evoke a premium feel, tracking (letter-spacing) is slightly increased across all levels, particularly in headlines and uppercase labels. 

The typographic hierarchy relies on weight and color contrast rather than size alone. Use Deep Forest Green for primary content and a 60% opacity version for secondary metadata. Ensure all labels have generous vertical breathing room to align with the minimalist philosophy.

## Layout & Spacing

The layout philosophy follows a **fluid grid** with substantial "Safe Margins" of 32px to ensure the UI never feels cramped. This design system uses an 8px base unit rhythm.

Spacing is used to create "islands" of information. Rather than using dividers, use large gutters (24px+) to separate distinct functional areas. Elements should be grouped within neumorphic containers that utilize the spacing units to define internal padding, ensuring no content touches the edge of a rounded corner.

## Elevation & Depth

Hierarchy is established through simulated physical displacement. This design system avoids standard drop shadows in favor of **Dual-Shadow Neumorphism**:

1.  **Outset (Raised):** Elements appear to emerge from the background. Apply a light highlight shadow (top-left) in pure white (#FFFFFF) and a soft dark shadow (bottom-right) in a muted grey-blue (#D1D9E6 or similar).
2.  **Inset (Recessed):** Used for input fields and active button states. The shadows are flipped and moved inside the element's border to create a "pressed" or "carved" look.
3.  **Glassmorphism:** Overlays, such as modals or navigation bars, use a 20px backdrop blur with a 40% opaque Off-White fill and a thin 1px white border to simulate polished glass.

## Shapes

The shape language is ultra-soft and approachable. A minimum corner radius of 24px is applied to all standard cards, while buttons and chips typically use a **Pill-shaped** (fully rounded) radius. 

This extreme roundedness serves to soften the technical nature of the app, making the bio-waste management tool feel more like a lifestyle or wellness accessory. All icons should feature rounded caps and joins to match this curvature.

## Components

- **Neumorphic Cards:** The primary container. Use a subtle gradient (top-left to bottom-right) using #FDFDFD to #F1F3F5 to enhance the 3D effect.
- **Tactile Buttons:** In their default state, they are "Outset" (raised). On tap/click, transition to an "Inset" (pressed) state with a 2px downward shift in content to mimic physical travel.
- **Elegant Progress Rings:** Utilize the Sage Green for the progress fill. The track should be "Inset" to look like a carved groove in the surface. Use a thin stroke weight (2pt to 4pt) for a high-end look.
- **Minimalist Inputs:** Text fields should be "Inset" by default, suggesting a tray or slot ready for data.
- **Glass Overlays:** Bottom sheets and modals should use the glassmorphism style, allowing the soft shadows of the cards beneath to remain partially visible, maintaining spatial context.
- **Iconography:** Use 1.5pt stroke weights. Icons should be open-path where possible, avoiding heavy fills to maintain the airy, minimalist aesthetic.