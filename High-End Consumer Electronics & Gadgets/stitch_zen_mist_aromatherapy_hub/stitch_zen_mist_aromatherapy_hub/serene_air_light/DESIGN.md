---
name: Serene Air & Light
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
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
  secondary: '#645e4f'
  on-secondary: '#ffffff'
  secondary-container: '#e8dfcc'
  on-secondary-container: '#696253'
  tertiary: '#5c5f5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#9c9f9d'
  on-tertiary-container: '#333635'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#ebe1cf'
  secondary-fixed-dim: '#cfc6b3'
  on-secondary-fixed: '#1f1b10'
  on-secondary-fixed-variant: '#4c4638'
  tertiary-fixed: '#e1e3e1'
  tertiary-fixed-dim: '#c5c7c5'
  on-tertiary-fixed: '#191c1b'
  on-tertiary-fixed-variant: '#444746'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 56px
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
    letterSpacing: 0.03em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '400'
    lineHeight: 36px
    letterSpacing: 0.02em
  title-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding-mobile: 24px
  container-padding-desktop: 64px
  gutter: 24px
  section-gap: 80px
---

## Brand & Style

The design system is rooted in the concept of "Digital Breath"—a UI that feels as light and unobtrusive as a gentle mist. It targets a high-end demographic seeking sanctuary from digital noise through smart home wellness. 

The aesthetic is a sophisticated blend of **Minimalism** and **Glassmorphism**, utilizing "Soft UI" principles to create a sense of tactile luxury. Interfaces should feel airy, with high-quality imagery of natural textures (linen, smooth stone, diffused light) integrated into the background layers. Every interaction must be deliberate and slow, avoiding jarring transitions in favor of "breath-like" fades and gentle expansions.

## Colors

This design system utilizes a palette inspired by an indoor botanical garden at dawn. 

- **Sage Green (#8DA399)**: Used for primary actions, active states, and signifying clean air quality.
- **Pale Wood (#F2E8D5)**: Used for subtle containers and secondary background accents to provide warmth.
- **Soft White (#F9FBF9)**: The primary canvas color, used to maximize the sense of space.
- **Deep Charcoal (#2D2D2D)**: Reserved strictly for high-contrast text and critical iconography to ensure legibility without breaking the serene mood.

Gradients should be used sparingly, primarily as background "auras" behind glassmorphic cards to simulate diffused light through mist.

## Typography

The typography system relies exclusively on **Inter**, optimized for maximum airiness. To achieve the "luxury" feel, the design system utilizes generous tracking (letter spacing) across all levels, especially in headlines and labels. 

Headlines should be set with a lighter font weight (300 or 400) to avoid visual heaviness. Body text is kept strictly at a comfortable reading size (16px+) to maintain accessibility and a relaxed reading pace. All uppercase labels are given extra tracking (0.1em) to serve as elegant signposts within the UI.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop (12 columns, 1200px max-width) and a **Fluid Fluid** model for mobile. However, the visual delivery emphasizes "No Grid" aesthetics by using extremely large margins and asymmetrical whitespace.

- **Desktop:** 64px outer margins and 24px gutters. Elements often span the center 8 columns to leave breathable "dead space" on the sides.
- **Mobile:** 24px outer margins. Vertical rhythm is slow, with section gaps often exceeding 80px to prevent the user from feeling "crowded" by information.
- **Vertical Alignment:** Elements should use "Safe Zones" rather than being packed tightly. Prioritize centered layouts for main product controls.

## Elevation & Depth

Depth in this design system is created through **Glassmorphism** and **Ambient Shadows** rather than traditional stacking.

1.  **Surfaces:** Backgrounds are Soft White. Cards use a semi-transparent Soft White (70-80% opacity) with a 20px - 40px backdrop blur.
2.  **Shadows:** Use extremely diffused, low-opacity shadows. Instead of pure black, use a tinted shadow: `rgba(141, 163, 153, 0.1)` (Sage-tinted) to create a soft glow rather than a hard drop.
3.  **Borders:** Use 1px solid borders at 10% opacity of the Sage Green color to define glass edges without adding visual weight.

## Shapes

The shape language is strictly **Organic and Rounded**. Following the pill-shaped logic (Level 3), the minimum corner radius for primary cards and buttons is 24px. 

Interactive elements like "Mist Intensity" sliders or "Scent Profiles" should use pebble-like shapes—asymmetrical but smooth. Sharp 90-degree angles are prohibited; even containers that hit the edge of the screen should maintain a generous internal radius to evoke a sense of softness and comfort.

## Components

- **Buttons:** Primary buttons are pill-shaped with a Sage Green background and Soft White text. Hover states should involve a "soft glow" (increased shadow diffusion) rather than a color change.
- **Inputs:** Text fields are borderless with a subtle Pale Wood background and 24px corner radius. Focus states use a soft Sage Green inner glow.
- **Cards:** Glassmorphic containers with 32px padding and 32px+ corner radius. Content inside cards should be center-aligned to maintain a formal, balanced look.
- **Sliders:** The primary control for scent and air quality. Sliders should have thick, rounded tracks (12px height) and oversized, pebble-like handles for a tactile, friendly feel.
- **Progress Indicators:** Use soft "pulsing" animations for air quality monitoring—a slow, rhythmic expansion and contraction of a Sage Green circle to mimic breathing.
- **Chips/Status:** Small, pill-shaped tags used for "Purifying," "Scenting," or "Standby." These use the Pale Wood background with Sage Green text for a low-intensity visual hierarchy.