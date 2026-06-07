---
name: Aero-EVTOL
colors:
  surface: '#0f150e'
  surface-dim: '#0f150e'
  surface-bright: '#353b33'
  surface-container-lowest: '#0a1009'
  surface-container-low: '#171d16'
  surface-container: '#1b211a'
  surface-container-high: '#262c24'
  surface-container-highest: '#30362f'
  on-surface: '#dee4d9'
  on-surface-variant: '#becab9'
  inverse-surface: '#dee4d9'
  inverse-on-surface: '#2c322a'
  outline: '#889484'
  outline-variant: '#3f4a3d'
  surface-tint: '#77dc7a'
  primary: '#ffffff'
  on-primary: '#00390c'
  primary-container: '#93f993'
  on-primary-container: '#007523'
  inverse-primary: '#006e20'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#3d2e10'
  tertiary-container: '#fadfb3'
  on-tertiary-container: '#75623f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#93f993'
  primary-fixed-dim: '#77dc7a'
  on-primary-fixed: '#002105'
  on-primary-fixed-variant: '#005316'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#fadfb3'
  tertiary-fixed-dim: '#dcc399'
  on-tertiary-fixed: '#261901'
  on-tertiary-fixed-variant: '#554424'
  background: '#0f150e'
  on-background: '#dee4d9'
  surface-variant: '#30362f'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
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
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

The brand persona is defined by "Sustainable-Sleek," a fusion of high-performance aerospace engineering and ecological mindfulness. It caters to an elite, tech-forward demographic that values time, discretion, and environmental stewardship. The UI must evoke the sensation of flight: effortless, silent, and expansive.

To achieve this, the design system utilizes a **Glassmorphism** style layered over a deep, dark canvas. Surfaces should feel like the cockpit of a high-end eVTOL—synthetic, high-fidelity, and ultra-modern. The interface prioritizes clarity and "visual aerodynamics," using subtle motion and depth to guide the user through a premium booking and flight management experience.

## Colors

This design system utilizes a high-contrast dark mode as its native environment. 

- **Mint Green (#98FF98)**: Reserved for primary calls to action, active states, and critical flight data. It represents both "go" and "green energy."
- **Carbon Black (#1A1A1A)**: The foundational layer, providing a deep, non-reflective base that minimizes eye strain and emphasizes the premium hardware of the aircraft.
- **Pure White (#FFFFFF)**: Used for primary typography and high-level iconography to ensure maximum legibility against the dark backdrop.
- **Atmospheric Neutrals**: Secondary text and borders should use low-opacity whites (e.g., 60% and 20%) to create hierarchy without introducing new hues.

## Typography

The typography is structured to feel technical yet accessible. **Space Grotesk** is used for headlines to provide a futuristic, geometric edge. **Metropolis** handles body copy, offering a clean, structured, and modern reading experience. For technical readouts, coordinates, and flight numbers, **JetBrains Mono** is employed to evoke a "code-level" precision.

Large display type should utilize tighter letter-spacing to feel more "engineered," while small labels should be tracked out for clarity and a premium, architectural feel.

## Layout & Spacing

This design system employs a **Fluid Grid** model. The layout is designed to feel spacious, mimicking the open sky. 

- **Desktop**: A 12-column grid with generous 64px side margins. Content modules are often centered to create a focused, executive-suite feel.
- **Mobile**: A 4-column grid with 20px margins. 
- **Vertical Rhythm**: Built on an 8px baseline. Spacing between major sections should be aggressive (xl/80px) to allow the "Sustainable-Sleek" aesthetic room to breathe.
- **Safe Areas**: Elements should never touch the edge of their glass containers; a minimum of 24px (md) internal padding is required for all cards.

## Elevation & Depth

Depth is not communicated through traditional drop shadows, but through **Backdrop Blurs** and **Tonal Layering**.

1.  **Level 0 (Base)**: Carbon Black (#1A1A1A).
2.  **Level 1 (Navigation/Sidebars)**: Semi-transparent Carbon (80% opacity) with a 20px backdrop blur.
3.  **Level 2 (Cards/Modals)**: Frosted White (5% opacity) with a 32px backdrop blur and a thin, 1px Pure White border at 10% opacity.
4.  **Level 3 (Popovers/Tooltips)**: Slightly brighter glass with a subtle outer glow using the primary Mint Green at 5% opacity to indicate floating importance.

Transitions between levels should be smooth, mimicking the gradual change of light in the upper atmosphere.

## Shapes

The shape language is inspired by aerodynamic wings and fuselage contours. Sharp 90-degree angles are avoided in favor of "Rounded" (0.5rem) corners for standard elements and "Extra Large" (1.5rem) for main containers and cards.

Interactive elements like buttons should feel "molded" rather than stamped. Secondary buttons may use a "Pill" shape to contrast against the more structural card layouts.

## Components

- **Buttons**: Primary buttons are solid Mint Green with Carbon Black text. They feature a subtle "inner glow" on hover. Secondary buttons are ghost-style with a thin white border and a blur effect behind them.
- **Input Fields**: Subtle glass surfaces with bottom-only borders that animate to a full Mint Green outline upon focus. Text is always Pure White.
- **Cards**: Large-radius glass containers. Headlines within cards should be Space Grotesk. Information density should be low, utilizing JetBrains Mono for data points (e.g., "ETA: 14:00").
- **Chips/Status Indicators**: Small, pill-shaped elements. "Live" flight statuses should feature a pulsing Mint Green dot.
- **Progress Bars**: Ultra-thin lines. The "filled" portion should be a gradient of Mint Green, while the "unfilled" portion is a low-opacity white line.
- **Specialty Components**: 
    - **Altimeter/Horizon Gauges**: Custom circular components used for flight tracking, utilizing high-contrast white strokes and Mint Green needles.
    - **Map Overlays**: Custom dark-mode maps with Mint Green flight paths and glass-morphic info-bubbles.