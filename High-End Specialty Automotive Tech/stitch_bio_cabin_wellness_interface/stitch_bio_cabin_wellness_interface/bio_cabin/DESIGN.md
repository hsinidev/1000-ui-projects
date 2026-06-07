---
name: Bio-Cabin
colors:
  surface: '#f9f9f8'
  surface-dim: '#d9dad9'
  surface-bright: '#f9f9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f3'
  surface-container: '#edeeed'
  surface-container-high: '#e7e8e7'
  surface-container-highest: '#e1e3e2'
  on-surface: '#191c1c'
  on-surface-variant: '#434840'
  inverse-surface: '#2e3131'
  inverse-on-surface: '#f0f1f0'
  outline: '#73796f'
  outline-variant: '#c3c8bd'
  surface-tint: '#496640'
  primary: '#334f2b'
  on-primary: '#ffffff'
  primary-container: '#4a6741'
  on-primary-container: '#c2e4b4'
  inverse-primary: '#afd0a1'
  secondary: '#6c538b'
  on-secondary: '#ffffff'
  secondary-container: '#dbbdfd'
  on-secondary-container: '#624980'
  tertiary: '#464849'
  on-tertiary: '#ffffff'
  tertiary-container: '#5e6060'
  on-tertiary-container: '#dadbdb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#caecbc'
  primary-fixed-dim: '#afd0a1'
  on-primary-fixed: '#062104'
  on-primary-fixed-variant: '#324e2a'
  secondary-fixed: '#eedbff'
  secondary-fixed-dim: '#d8bafa'
  on-secondary-fixed: '#260e43'
  on-secondary-fixed-variant: '#543b71'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f8'
  on-background: '#191c1c'
  surface-variant: '#e1e3e2'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Manrope
    fontSize: 24px
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
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.03em
  display-lg-mobile:
    fontFamily: Manrope
    fontSize: 36px
    fontWeight: '300'
    lineHeight: '1.1'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  section-gap: 64px
  touch-target: 48px
---

## Brand & Style

The design system is centered on "Biological Serenity"—a synthesis of clinical precision and organic warmth. It is designed for high-end automotive environments where the vehicle acts as a sanctuary for health and cognitive restoration. The visual language avoids the cold, mechanical aesthetic of traditional car interfaces in favor of a "living" UI that feels as though it is breathing in sync with the passenger.

The style leverages **Organic Minimalism** combined with **Glassmorphism**. Surfaces are translucent, evoking the quality of frosted glass or cellular membranes, allowing light and soft gradients to permeate the interface. Motion is not just a transition but a biological function; elements should pulse gently (a "breathing" rhythm) to indicate active monitoring or system readiness.

## Colors

The palette is anchored in restorative nature and cognitive clarity. 
- **Moss Green (#4A6741)**: Used for primary actions and "Health" indicators. It represents vitality and biological equilibrium.
- **Lavender (#967BB6)**: Used for "Focus" and "Calm" states. It serves as a secondary accent for cognitive wellness features.
- **Pure White (#FFFFFF)**: The base for clarity and clinical cleanliness. Used for high-elevation surfaces.
- **Neutral (#F8F9F8)**: A soft, off-white "Bone" color used for backgrounds to reduce eye strain compared to pure white.

Gradients are essential; they should always be radial and soft, transitioning from a core color into a transparent wash to mimic the diffusion of light through biological matter.

## Typography

This design system utilizes **Manrope** as the primary typeface for its modern, balanced, and highly legible characteristics. It feels clinical yet approachable. Headlines use lighter weights with tighter tracking to convey a high-end, editorial feel.

**Plus Jakarta Sans** is employed for labels and micro-copy. Its slightly softer, rounded terminals complement the organic shape language and ensure that even technical data feels supportive and "friendly." All body text should maintain a generous line height (1.6) to ensure breathability and ease of reading while in motion.

## Layout & Spacing

The layout philosophy is based on **Dynamic Breathing Zones**. Instead of a rigid grid, the system uses generous whitespace to separate medical data from environmental controls. 

- **Desktop/Console:** A centered, fluid container with a maximum width of 1440px. Large margins (40px+) act as "negative space buffers" to keep the user from feeling overwhelmed.
- **Mobile/Handheld:** A single-column flow with 24px side margins. 
- **Rhythm:** All spacing is derived from an 8px base unit, but elements should be grouped with larger "gap" values (64px+) to maintain the "serene" and "luxury" aesthetic. Content should never feel cramped; if a screen feels full, information hierarchy must be reassessed.

## Elevation & Depth

Depth is achieved through **Luminous Layering** rather than traditional shadows.
- **Base Level:** Neutral background with a very subtle radial gradient of Moss Green in one corner.
- **Surface Level:** Translucent white panels with a 20px backdrop blur and a 1px soft white border (30% opacity). This creates a "glass" effect.
- **Active Level:** Elements that are "breathing" or active use a soft, colored glow (box-shadow: 0 0 30px) using the Primary or Secondary color at low opacity (15-20%).
- **Shadows:** Avoid dark, heavy shadows. Use "Ambient Occlusion" style shadows—very large blur (40px+), very low opacity (5%), and tinted with the primary Moss Green to maintain a biological feel.

## Shapes

The shape language is strictly **Organic and Fluid**. Sharp corners are non-existent in this design system. 
- Standard containers and cards utilize a high radius (rounded-lg or rounded-xl).
- Buttons and interactive chips are fully **Pill-shaped** to evoke the form of medicinal capsules and smooth river stones.
- "Squircle" geometries are preferred over perfect circles for a more custom, high-end feel.

## Components

- **Buttons:** Large, pill-shaped, and filled with soft gradients. The primary button uses a Moss Green gradient. On hover or interaction, the button should "swell" slightly (1.05x scale) with a gentle spring animation.
- **Wellness Chips:** Used for status (e.g., "Air Quality: Pure"). These should have a glassmorphic background and a small, pulsing dot icon to indicate live monitoring.
- **Bio-Cards:** Cards do not have visible borders; they are defined by their backdrop blur and a very subtle inner glow. 
- **Breathing Progress Bars:** For health metrics, use thick, rounded bars where the fill color has a subtle "pulse" animation, moving between 80% and 100% opacity to mimic a heartbeat or breath.
- **Input Fields:** Minimalist under-lines or very soft, recessed (inner shadow) pill shapes. Focus states should trigger a soft Lavender glow around the entire field.
- **Luxury Sliders:** The slider thumb should be a large, soft-glow circle, providing a tactile, "squishy" visual feedback when dragged.
- **Biometric Visualizers:** Custom components like heart-rate waves or lung-capacity rings should use variable stroke widths to feel hand-drawn and biological rather than mathematically perfect.