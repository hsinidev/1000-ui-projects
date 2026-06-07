---
name: Industrial-Sleek Fleet Systems
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#9a9898'
  on-tertiary-container: '#313131'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
  data-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 16px
  margin: 20px
---

## Brand & Style
This design system embodies the "Industrial-Sleek" aesthetic, tailored for professional autonomous fleet management. The brand personality is authoritative, precise, and resilient. It targets operations managers and technical field staff who require high-performance tools that function reliably under intense conditions.

The visual style is a hybrid of **Modern Minimalism** and **Technical Brutalism**. It prioritizes utility and speed of recognition through high-contrast interfaces, crisp structural lines, and a dark-mode-first approach that reduces eye strain in low-light industrial environments. Every element is designed to feel like a high-end physical controller—tactile, responsive, and indestructible.

## Colors
The palette is rooted in industrial safety standards. **Matte Black (#121212)** serves as the core background to ground the interface and provide maximum contrast for data. **Safety Orange (#FF6B00)** is the primary action color, reserved strictly for critical interactions, primary buttons, and active autonomous status. 

**Charcoal (#333333)** is used for structural elements such as headers, sidebars, and card backgrounds to create subtle layering. Text and data visualizations utilize a high-readability scale of cool grays to ensure the hierarchy remains clear without competing with the primary orange alerts.

## Typography
The typography system prioritizes legibility in high-vibration or outdoor mobile environments. **Inter** is the primary typeface for its exceptional clarity and neutral, professional tone. 

For technical data points, coordinates, and telemetry, the design system utilizes **Geist** to provide a monospaced, precise feel that aids in scanning numerical values. Headers use tight letter-spacing and bold weights to evoke a sense of strength and urgency.

## Layout & Spacing
This system employs a **mobile-first fluid grid** based on a 4px baseline rhythm. For mobile views, a 4-column grid with 16px gutters is the standard, expanding to a 12-column grid on desktop dashboards. 

Padding within cards and containers is generous to ensure "fat-finger" friendliness for operators in the field. Interactive elements follow a minimum touch target size of 48x48px. Layouts should be dense with information but organized through strict vertical rhythm and clear grouping of related telemetry data.

## Elevation & Depth
Depth is communicated through **Tonal Layers** rather than soft shadows. Surfaces are stacked using color luminosity:
- **Level 0 (Base):** Matte Black (#121212)
- **Level 1 (Cards/Panels):** Charcoal (#1E1E1E)
- **Level 2 (Active Elements):** Lighter Charcoal (#2A2A2A)

To reinforce the technical aesthetic, use **crisp 1px borders** (#333333) to define edges. Subtle linear gradients (top-to-bottom, 5% opacity variance) can be applied to buttons and headers to give them a machined, metallic quality. Shadows, when used for modals, should be sharp and high-opacity to feel heavy and grounded.

## Shapes
The shape language is "Soft-Industrial." Elements use a **0.25rem (4px)** corner radius to maintain a rugged, precision-engineered look while preventing the interface from feeling dangerously sharp. 

Circular shapes are reserved exclusively for status indicators (e.g., "Active" or "Offline" LEDs) and profile avatars. Large containers like cards should maintain the 4px radius, while primary buttons may utilize a slightly more pronounced 8px radius to distinguish them as high-priority touchpoints.

## Components
- **Buttons:** Primary buttons are solid Safety Orange with black text. Secondary buttons use a Charcoal stroke with white text. Use a subtle inner-bevel effect to simulate a physical push-button.
- **Status Chips:** Use high-contrast backgrounds with white text. For example, a "Mowing" status chip should feature a Safety Orange left-border or glow to indicate active mechanical movement.
- **Input Fields:** Dark backgrounds (#0A0A0A) with a 1px border. When focused, the border transitions to Safety Orange with a subtle outer glow.
- **Cards:** Use #1E1E1E as the background. Include a "Header-Strip" at the top of cards for specific fleet categories (e.g., a 2px orange line for "Active Units").
- **Telemetry Lists:** High-density rows with Geist mono-spaced fonts for numerical values. Use Zebra-striping for long data sets to aid horizontal scanning.
- **Additional Components:**
    - **Joystick/D-Pad:** A mobile-optimized touch controller for manual override of autonomous units.
    - **Gauges:** Circular and linear progress bars using Safety Orange to represent battery life, fuel, or blade wear.