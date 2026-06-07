---
name: Cyber-Kinetic AR
colors:
  surface: '#121318'
  surface-dim: '#121318'
  surface-bright: '#38393f'
  surface-container-lowest: '#0d0e13'
  surface-container-low: '#1a1b21'
  surface-container: '#1e1f25'
  surface-container-high: '#292a2f'
  surface-container-highest: '#34343a'
  on-surface: '#e3e1e9'
  on-surface-variant: '#b9cac9'
  inverse-surface: '#e3e1e9'
  inverse-on-surface: '#2f3036'
  outline: '#839493'
  outline-variant: '#3a4a49'
  surface-tint: '#00dddd'
  primary: '#ffffff'
  on-primary: '#003737'
  primary-container: '#00fbfb'
  on-primary-container: '#007070'
  inverse-primary: '#006a6a'
  secondary: '#ffb0d0'
  on-secondary: '#63003d'
  secondary-container: '#90015a'
  on-secondary-container: '#ff99c6'
  tertiary: '#ffffff'
  on-tertiary: '#2f3131'
  tertiary-container: '#e2e2e2'
  on-tertiary-container: '#636565'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#00fbfb'
  primary-fixed-dim: '#00dddd'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#ffd8e6'
  secondary-fixed-dim: '#ffb0d0'
  on-secondary-fixed: '#3d0024'
  on-secondary-fixed-variant: '#8c0058'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#121318'
  on-background: '#e3e1e9'
  surface-variant: '#34343a'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
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
  touch-target-min: 48px
  margin-mobile: 24px
  gutter: 16px
  safe-area-top: 64px
---

## Brand & Style

This design system is built for a high-octane, digital-physical hybrid experience. The brand personality is electric, competitive, and hyper-modern, aiming to evoke a sense of adrenaline and immersion. 

The visual style merges **Glassmorphism** with **High-Contrast/Bold** aesthetics. It utilizes deep, dark backgrounds as a canvas for radiant neon accents, creating a "cyber-glow" effect that feels native to augmented reality. UI elements prioritize "the pulse"—dynamic, overlapping layers that suggest speed and depth. This is a "Mobile-First/AR-First" approach where every interaction feels tactile and reactive.

## Colors

The palette is anchored in a deep midnight spectrum to ensure maximum contrast for neon elements.
- **Electric Blue (#00FFFF):** Used for primary actions, system status, and active AR markers. It represents energy and connectivity.
- **Hot Pink (#FF69B4):** Reserved for secondary highlights, competitive notifications, and "hype" moments.
- **Pure White (#FFFFFF):** Used exclusively for high-priority text and iconography to ensure legibility against vibrant glows.
- **Midnight Blue (#0A0B10):** The primary surface color, providing a sophisticated, low-light base that prevents eye fatigue in AR environments.

## Typography

This design system uses a dual-font strategy to balance technical aesthetics with readability. 
- **Space Grotesk** is used for headlines and labels. Its geometric, futuristic skeleton mirrors the precision of AR tracking and gaming hardware.
- **Be Vietnam Pro** serves as the body typeface. It provides a contemporary, friendly contrast that remains exceptionally clear at smaller sizes or when rendered on semi-transparent background blurs.

Typography should frequently utilize uppercase for labels and small headings to lean into the gaming-interface aesthetic.

## Layout & Spacing

The layout follows a **Fluid Grid** model designed for handheld mobile use. 
- **Rhythm:** An 8px base grid governs all spatial relationships. 
- **Safety Zones:** Large 24px side margins ensure UI elements don't get lost in the curvature of modern mobile displays or obscured by thumbs during active gameplay. 
- **Composition:** Elements are encouraged to overlap. For example, a card might slightly break the margin or overlap a background glow to create a sense of three-dimensional space within the viewport.

## Elevation & Depth

Depth is not communicated through traditional shadows, but through **Luminance and Blur**.
- **The Glass Layer:** Surfaces use a 20% opacity white fill with a high backdrop-filter blur (20px-40px). This allows the real-world AR background or underlying game elements to peek through while maintaining text legibility.
- **Neon Glows:** Instead of black shadows, use "Bloom" effects. Primary buttons and active states feature a drop-shadow tinted with the element's own color (e.g., a blue button has a blurred #00FFFF shadow) to simulate light emission.
- **Stacking:** Critical HUD elements exist on the highest Z-index, featuring the strongest glow and most opaque glass.

## Shapes

The shape language is defined by **High-Radius Curves**. 
- **Touch Targets:** All interactive elements use a pill-shaped (fully rounded) or `rounded-xl` (1.5rem) radius. This creates a soft, approachable feel that balances the "sharp" technical nature of the typography.
- **Visual Flow:** Large radii help the UI feel like organic "bubbles" floating in the AR space rather than rigid, flat boxes.

## Components

- **Buttons:** Large, pill-shaped targets. Primary buttons use a solid Electric Blue fill with a matching neon bloom. Secondary buttons use a thick 2px Hot Pink border with transparent centers.
- **Glass Cards:** Containers for game stats and inventory. They feature a 1px inner border (white at 10% opacity) to define edges against complex backgrounds.
- **HUD Chips:** Small, semi-transparent labels used for real-time data like "Ping" or "Player Count," featuring the Space Grotesk font in all-caps.
- **Input Fields:** Deep charcoal backgrounds with a "bottom-glow" border that turns Electric Blue when active.
- **Navigation:** Floating bottom bars with large, circular icons that scale up by 15% and emit a glow when tapped, providing immediate haptic and visual feedback.
- **AR Reticles:** Dynamic, geometric shapes centered in the viewport that pulse and change color based on proximity to physical objects.