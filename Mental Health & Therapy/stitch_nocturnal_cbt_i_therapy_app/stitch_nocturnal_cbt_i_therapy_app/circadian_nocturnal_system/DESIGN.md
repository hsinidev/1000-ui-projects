---
name: Circadian Nocturnal System
colors:
  surface: '#0e1419'
  surface-dim: '#0e1419'
  surface-bright: '#343a3f'
  surface-container-lowest: '#090f14'
  surface-container-low: '#161c21'
  surface-container: '#1a2025'
  surface-container-high: '#242b30'
  surface-container-highest: '#2f363b'
  on-surface: '#dde3ea'
  on-surface-variant: '#d6c3b0'
  inverse-surface: '#dde3ea'
  inverse-on-surface: '#2b3136'
  outline: '#9f8e7c'
  outline-variant: '#524535'
  surface-tint: '#ffb95a'
  primary: '#ffd7a9'
  on-primary: '#462a00'
  primary-container: '#ffb347'
  on-primary-container: '#704700'
  inverse-primary: '#845400'
  secondary: '#bec7db'
  on-secondary: '#283140'
  secondary-container: '#40495a'
  on-secondary-container: '#b0b9cc'
  tertiary: '#dadeee'
  on-tertiary: '#2b303c'
  tertiary-container: '#bec2d2'
  on-tertiary-container: '#4b505d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb6'
  primary-fixed-dim: '#ffb95a'
  on-primary-fixed: '#2a1800'
  on-primary-fixed-variant: '#643f00'
  secondary-fixed: '#dae3f7'
  secondary-fixed-dim: '#bec7db'
  on-secondary-fixed: '#131c2a'
  on-secondary-fixed-variant: '#3e4757'
  tertiary-fixed: '#dee2f2'
  tertiary-fixed-dim: '#c2c6d6'
  on-tertiary-fixed: '#171b27'
  on-tertiary-fixed-variant: '#424753'
  background: '#0e1419'
  on-background: '#dde3ea'
  surface-variant: '#2f363b'
typography:
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
    letterSpacing: 0.02em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
  margin: 24px
---

## Brand & Style

The design system is engineered for the sensitive transition between wakefulness and sleep. It prioritizes a "nocturnal-first" philosophy, ensuring that users interacting with the interface in low-light environments experience zero eye strain and no circadian disruption. The brand personality is empathetic and quiet, yet retains a clinical authority through precision and clarity.

The aesthetic leans into **Minimalism** with subtle **Glassmorphism**. By using translucent layers and soft background blurs, the interface avoids harsh borders that can create visual "noise" at night. Every element is designed to feel like it is floating in a calm, dark void, providing a sense of depth and tranquility that mirrors the experience of drifting into sleep.

## Colors

The palette is strictly curated to eliminate high-energy blue light (#0000FF). The "Deep Midnight" backgrounds utilize warm-toned navy bases that lean toward slate and charcoal to minimize retinal stimulation.

*   **Primary (Soft Amber):** Used exclusively for primary actions, critical alerts, and active states. This wavelength is biologically chosen to be visible without triggering alertness.
*   **Secondary (Warm Navy):** Used for container backgrounds and secondary cards to create depth against the pure midnight base.
*   **Neutrals:** Text and icons use a "Muted Pearl" rather than pure white to reduce glare. All grays are infused with a hint of warmth to maintain the nocturnal harmony.

## Typography

This design system utilizes **Manrope** for its exceptional balance between modern geometry and humanistic warmth. Given the dark-mode-first constraint, typography focuses on high legibility through increased line-heights (1.6x minimum for body text) and slightly generous letter-spacing to prevent "haloing" effects common in white-on-dark text.

Headlines are kept bold but compact to guide the eye quickly, while body text is prioritized for comfort during long-form reading, such as sleep reports or medical consultations.

## Layout & Spacing

The layout follows a **Fluid Grid** model with an 8px base unit. To maintain a "calming" atmosphere, the system employs aggressive whitespace (padding and margins) to prevent information density from overwhelming the user before sleep.

Content is centered in a single-column focus for mobile, while tablet and desktop views utilize a 12-column grid with wide gutters (24px) to ensure that clinical data and charts have room to breathe.

## Elevation & Depth

Hierarchy in this design system is established through **Tonal Layers** rather than traditional shadows. Because shadows are often lost in near-black environments, we use progressively lighter surface colors to indicate elevation.

1.  **Level 0 (Base):** Midnight Blue (#0A0E14) – Background.
2.  **Level 1 (Cards):** Soft Navy (#0F141F) – Content containers.
3.  **Level 2 (Modals):** Warm Slate (#1B2433) – Floating elements.

To replace the visual cue of shadows, a 1px "Inner Glow" or "Stroke" in a low-opacity Soft Amber is used for high-priority interactive elements, creating a subtle luminescent effect that feels like a physical light source in a dark room.

## Shapes

The shape language is **Rounded**, utilizing a 16px (1rem) base radius for cards and buttons. This softness removes the "edge" from the interface, reinforcing the calming and approachable medical tone. 

Interactive elements like input fields and toggles use the same 16px radius, while larger containers (like sleep diary entries) may use 24px (rounded-lg) to feel more like organic, soft-touch objects.

## Components

### Buttons & Inputs
*   **Primary Action:** Filled Soft Amber with dark text. No hover "flash"; instead, use a subtle opacity pulse.
*   **Ghost Inputs:** 1px stroke in Warm Slate with Amber focus rings. Placeholders are desaturated to avoid competition with user-entered text.

### Audio Player
*   **Waveform Visualization:** Low-contrast Amber bars.
*   **Controls:** Oversized, "squishy" touch targets for easy interaction in the dark. No sharp icons; use rounded glyphs.

### Medical & Professional
*   **Consultation Interfaces:** Video frames are encapsulated in rounded containers with "Sleep Status" badges.
*   **Charts:** Lightweight line charts. Instead of multi-colored lines, use varying weights of Amber and muted opacity fills. Use "Warm Navy" for grid lines to keep them nearly invisible.

### Accessible Forms
*   Labels always sit above fields to maintain a consistent vertical scan. 
*   Error states use a desaturated "Warm Red" to indicate issues without creating a visual "jolt" for the user.