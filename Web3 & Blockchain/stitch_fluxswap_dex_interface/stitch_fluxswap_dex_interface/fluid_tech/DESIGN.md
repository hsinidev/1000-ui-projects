---
name: Fluid-Tech
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#323b3b'
  surface-container-lowest: '#071010'
  surface-container-low: '#151d1d'
  surface-container: '#192121'
  surface-container-high: '#232c2b'
  surface-container-highest: '#2e3636'
  on-surface: '#dbe4e3'
  on-surface-variant: '#b9cac9'
  inverse-surface: '#dbe4e3'
  inverse-on-surface: '#293232'
  outline: '#839493'
  outline-variant: '#3a4a49'
  surface-tint: '#00dddd'
  primary: '#ffffff'
  on-primary: '#003737'
  primary-container: '#00fbfb'
  on-primary-container: '#007070'
  inverse-primary: '#006a6a'
  secondary: '#b4c9e0'
  on-secondary: '#1e3244'
  secondary-container: '#35495c'
  on-secondary-container: '#a3b7ce'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#00fbfb'
  primary-fixed-dim: '#00dddd'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#d0e5fc'
  secondary-fixed-dim: '#b4c9e0'
  on-secondary-fixed: '#071d2e'
  on-secondary-fixed-variant: '#35495c'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#0d1515'
  on-background: '#dbe4e3'
  surface-variant: '#2e3636'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  data-display:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 20px
  max_width: 1440px
---

## Brand & Style
The design system is engineered to evoke the sensation of high-frequency trading in a zero-gravity environment. It targets sophisticated DeFi users who demand speed, precision, and visual clarity. The aesthetic combines **Glassmorphism** with **High-Contrast Futuristic** elements, creating a layered interface that feels like a digital cockpit. 

Visual priority is given to real-time data flow, utilizing motion and glowing accents to signify liquidity and active state transitions. The interface should feel expensive, technical, and hyper-responsive, prioritizing "dark mode" aesthetics to reduce eye strain during long-duration trading sessions.

## Colors
This design system utilizes a high-contrast palette optimized for dark environments. 
- **Neon Cyan (#00FFFF)**: The primary driver of action. It is used for CTA buttons, active toggles, and critical data highlights. It carries a native glow effect to simulate light emission.
- **Deep Navy (#011627)**: The foundation layer. Used for the global background to provide a sense of infinite depth.
- **Matte Black (#111111)**: The structural surface. Used for cards and containers to create a distinct separation from the background without losing the dark aesthetic.
- **Functional Colors**: Success and error states use high-vibrancy green and red to cut through the navy base, ensuring immediate cognitive recognition of transaction statuses.

## Typography
The typography strategy leverages a hybrid approach: **Space Grotesk** provides a technical, geometric edge for headlines and financial data, while **Inter** ensures maximum legibility for body text and descriptive content. 

All financial figures should be rendered with generous letter spacing to prevent digit crowding. For ticker animations and live price updates, use medium weights to maintain sharpness against the dark background.

## Layout & Spacing
The design system employs a **Fluid Grid** architecture built on a 4px baseline. The layout uses a 12-column system for dashboard views, transitioning to centered, single-column stacks for focused swap modules. 

Padding within cards is generous (24px - 32px) to allow the glassmorphic effects space to "breathe." Content should be aligned to a rigid grid to reinforce the technical nature of the platform, using white space as a structural separator rather than lines where possible.

## Elevation & Depth
Depth is created through transparency and light, rather than traditional shadows.
- **Level 0 (Background):** Deep Navy (#011627).
- **Level 1 (Surfaces):** Matte Black (#111111) with a subtle 1px border of 10% Cyan.
- **Level 2 (Overlays/Modals):** Glassmorphism with a backdrop-blur (20px) and a semi-transparent Matte Black fill (opacity 70%).
- **Level 3 (Active Elements):** Elements "lift" via a 0 0 15px Neon Cyan outer glow. 

Interactive elements should appear to float above the background, with the background blur providing the necessary contrast for readability.

## Shapes
The design system adopts a **Sharp (0px)** corner radius for all primary containers, buttons, and inputs. This reinforces a precision-engineered, "hard-tech" aesthetic. 

Small UI signals, such as status pips or decorative accents, may use 45-degree chamfered corners to enhance the futuristic look without introducing organic curves. All borders should be 1px or 2px—never thicker—to maintain a sleek, technical profile.

## Components
- **Primary Buttons:** Solid Neon Cyan background with black text. Hover states trigger a high-intensity cyan glow and a slight scale increase.
- **Action Inputs:** Matte Black background with a 1px Neon Cyan border. Focused states utilize a "pulse" animation on the border.
- **Cards:** Sharp-edged Matte Black containers with a backdrop-filter blur when positioned over background gradients.
- **Charts:** Use thin (1.5px) vector lines. The "Area" under the line should use a vertical gradient from Neon Cyan (20% opacity) to transparent. No grid lines; use hover-state crosshairs only.
- **Liquidity Tickers:** Horizontal scrolling text components using Space Grotesk. Speed should be constant and fluid.
- **Swap Module:** A centralized, stacked component with a glassmorphic "connector" icon between input and output fields, glowing when a valid price path is found.